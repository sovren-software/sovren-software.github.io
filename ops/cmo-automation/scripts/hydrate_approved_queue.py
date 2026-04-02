#!/usr/bin/env python3
import argparse
import json
import os
import re
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REVIEW = ROOT / "reports" / "cmo-queue-review.json"
POLICY = ROOT / "config" / "operating_policy.json"
OUT_JSON = ROOT / "reports" / "cmo-hydrated-queue.json"
OUT_MD = ROOT / "reports" / "cmo-hydrated-queue.md"

Resolver = Callable[[str | None, str], dict | None]

EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F5FF"
    "\U0001F600-\U0001F64F"
    "\U0001F680-\U0001F6FF"
    "\U0001F700-\U0001F77F"
    "\U0001F780-\U0001F7FF"
    "\U0001F800-\U0001F8FF"
    "\U0001F900-\U0001F9FF"
    "\U0001FA00-\U0001FAFF"
    "\U00002700-\U000027BF"
    "\U00002600-\U000026FF"
    "]+",
    flags=re.UNICODE,
)


def load_json(path: Path):
    if not path.exists():
        raise SystemExit(f"Missing required input: {path}")
    return json.loads(path.read_text())


def load_credential_mapping() -> None:
    mapping = {
        "X_API_KEY": os.getenv("X_API_KEY") or os.getenv("TWITTER_API_KEY"),
        "X_API_SECRET": os.getenv("X_API_SECRET") or os.getenv("TWITTER_API_SECRET"),
        "X_BEARER_TOKEN": os.getenv("X_BEARER_TOKEN") or os.getenv("TWITTER_BEARER_TOKEN"),
        "X_ACCESS_TOKEN": os.getenv("X_ACCESS_TOKEN") or os.getenv("TWITTER_ACCESS_TOKEN"),
        "X_ACCESS_TOKEN_SECRET": os.getenv("X_ACCESS_TOKEN_SECRET") or os.getenv("TWITTER_ACCESS_SECRET"),
    }
    missing = [k for k, v in mapping.items() if not v]
    if missing:
        raise SystemExit(f"Missing required credentials: {', '.join(missing)}")
    os.environ.update(mapping)


def run_json(cmd: list[str], retries: int = 2):
    for attempt in range(retries + 1):
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode == 0:
            return json.loads(p.stdout)

        reset_match = re.search(r"Resets at (\d+)", p.stderr)
        if reset_match and attempt < retries:
            reset_ts = int(reset_match.group(1))
            sleep_for = max(1, reset_ts - int(time.time()) + 1)
            time.sleep(min(sleep_for, 30))
            continue

        raise RuntimeError(f"Command failed: {' '.join(cmd)}\nSTDERR:\n{p.stderr}")


def normalize_text(text: str, limit: int = 100) -> str:
    clean = re.sub(r"\s+", " ", (text or "")).strip()
    if len(clean) <= limit:
        return clean
    return clean[: limit - 1].rstrip() + "…"


def enforce_style(text: str) -> str:
    s = text or ""
    s = s.replace("!", "")
    s = s.replace("—", " ").replace("–", " ")
    s = EMOJI_RE.sub("", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:278]


def build_root_text(account: str, role: str) -> str:
    ideas = {
        "founder": "Building AI products is mostly distribution math plus feedback loops. Own both and ship faster.",
        "brand": "Good AI products win when onboarding is instant, outcomes are measurable, and support feels human.",
        "product-agent": "Agent workflows improve when memory, orchestration, and evals are designed as one system.",
    }
    base = ideas.get(role, ideas["brand"])
    return enforce_style(f"{base} #{account}")


def safe_founder_reply(target_user: str, excerpt: str) -> str:
    raw = (
        f"@{target_user} Good signal. I care less about hype and more about repeatable distribution plus retention. "
        f"{excerpt}"
    )
    return enforce_style(raw)


def build_reply_text(account: str, role: str, target_user: str, source_text: str) -> str:
    excerpt = normalize_text(source_text, limit=80)
    if role == "founder":
        return safe_founder_reply(target_user, excerpt)
    if role == "product-agent":
        return enforce_style(
            f"@{target_user} Useful thread. Curious what your eval loop looks like once this is in production. {excerpt}"
        )
    return enforce_style(
        f"@{target_user} Solid point. We see the same pattern in shipping: clear UX plus measurable outcomes compound. {excerpt}"
    )


def contains_denylist(text: str, keywords: list[str]) -> bool:
    t = (text or "").lower()
    return any(k.lower() in t for k in keywords)


def default_resolver(target_user: str | None, account: str) -> dict | None:
    account_queries = {
        "TheCesarCross": "AI founders OR agentic workflow OR product distribution",
        "sovren_software": "AI automation OR workflow systems OR developer tools",
        "mrhaven_agent": "agent memory OR orchestration OR evals",
    }

    if target_user:
        query = f"from:{target_user} -is:retweet"
    else:
        query = account_queries.get(account, "AI products OR automation")

    data = run_json(["x-cli", "-j", "tweet", "search", query, "--max", "10"])
    if not isinstance(data, list) or not data:
        return None

    for t in data:
        if not isinstance(t, dict):
            continue
        tweet_id = t.get("id")
        text = t.get("text")
        author = ((t.get("author") or {}).get("username") if isinstance(t.get("author"), dict) else None)
        if tweet_id and text:
            return {"id": str(tweet_id), "text": text, "author": author}
    return None


def hydrate_single_action(action: dict, policy: dict, resolver: Resolver) -> dict:
    out = dict(action)
    account = out.get("account", "")
    role = policy.get("account_strategy", {}).get(account, {}).get("role", "brand")
    founder_keywords = policy.get("founder_denylist", {}).get("keywords", [])

    if out.get("action") == "root_post":
        post_text = build_root_text(account, role)
        if role == "founder" and contains_denylist(post_text, founder_keywords):
            out["hydration_status"] = "blocked"
            out["hydration_reason"] = "founder_denylist_hit"
            return out

        out["post_text"] = post_text
        out["x_cli_command"] = ["x-cli", "-j", "tweet", "post", post_text]
        out["hydration_status"] = "hydrated"
        return out

    if out.get("action") == "reply":
        candidate = resolver(out.get("target_user"), account)
        if not candidate:
            out["hydration_status"] = "blocked"
            out["hydration_reason"] = "no_candidate_tweet"
            return out

        target_user = out.get("target_user") or candidate.get("author") or "builder"
        reply_text = build_reply_text(account, role, target_user, candidate.get("text", ""))

        if role == "founder" and contains_denylist(reply_text, founder_keywords):
            out["hydration_status"] = "blocked"
            out["hydration_reason"] = "founder_denylist_hit"
            return out

        tweet_id = str(candidate["id"])
        out["target_user"] = target_user
        out["target_tweet_id"] = tweet_id
        out["reply_text"] = reply_text
        out["execution_mode"] = "quote_workaround"
        out["x_cli_command"] = ["x-cli", "-j", "tweet", "quote", tweet_id, reply_text]
        out["hydration_status"] = "hydrated"
        return out

    out["hydration_status"] = "blocked"
    out["hydration_reason"] = "unsupported_action_type"
    return out


def hydrate_review(review: dict, policy: dict, resolver: Resolver) -> dict:
    hydrated = dict(review)
    hydrated_accounts = {}

    total = 0
    ready = 0
    blocked = 0

    for account, payload in review.get("accounts", {}).items():
        approved = payload.get("approved_actions", [])
        hydrated_approved = []
        for action in approved:
            total += 1
            h = hydrate_single_action(action, policy, resolver)
            hydrated_approved.append(h)
            if h.get("hydration_status") == "hydrated":
                ready += 1
            else:
                blocked += 1

        new_payload = dict(payload)
        new_payload["approved_actions"] = hydrated_approved
        hydrated_accounts[account] = new_payload

    hydrated["accounts"] = hydrated_accounts
    hydrated["hydrated_at"] = datetime.now(timezone.utc).isoformat()
    hydrated["hydration_summary"] = {
        "total_approved": total,
        "hydrated": ready,
        "blocked": blocked,
    }
    return hydrated


def write_reports(hydrated: dict) -> None:
    OUT_JSON.write_text(json.dumps(hydrated, indent=2))

    s = hydrated.get("hydration_summary", {})
    lines = [
        "# CMO Hydrated Queue",
        f"Hydrated at: {hydrated.get('hydrated_at')}",
        f"- total approved: {s.get('total_approved', 0)}",
        f"- hydrated: {s.get('hydrated', 0)}",
        f"- blocked: {s.get('blocked', 0)}",
        "",
    ]

    for account, payload in hydrated.get("accounts", {}).items():
        actions = payload.get("approved_actions", [])
        ok = sum(1 for a in actions if a.get("hydration_status") == "hydrated")
        no = len(actions) - ok
        lines.append(f"## @{account} hydrated={ok} blocked={no}")
        for a in actions:
            lines.append(
                f"- {a.get('action')} target={a.get('target_user')} status={a.get('hydration_status')} reason={a.get('hydration_reason')}"
            )
        lines.append("")

    OUT_MD.write_text("\n".join(lines))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Hydrate approved queue actions with copy and executable x-cli commands")
    parser.add_argument("--input", default=str(DEFAULT_REVIEW), help="Path to cmo-queue-review.json")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    load_credential_mapping()
    review = load_json(Path(args.input))
    policy = load_json(POLICY)
    hydrated = hydrate_review(review, policy, default_resolver)
    write_reports(hydrated)
    print(str(OUT_JSON))
    print(str(OUT_MD))


if __name__ == "__main__":
    main()
