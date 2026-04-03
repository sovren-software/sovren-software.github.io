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
URL_RE = re.compile(r"https?://\S+|www\.\S+", flags=re.IGNORECASE)
HASHTAG_RE = re.compile(r"(^|\s)#\w+")

LOW_SIGNAL_RE = re.compile(
    r"\b(giveaway|airdrop|retweet\s+to\s+win|win\s+free|pump|moon|token\s+price|telegram\s+community)\b",
    flags=re.IGNORECASE,
)


def load_json(path: Path):
    if not path.exists():
        raise SystemExit(f"Missing required input: {path}")
    return json.loads(path.read_text())


def load_credential_mapping() -> None:
    """Load X API credentials. Hydration uses bearer token for tweet lookups."""
    bearer = os.getenv("X_BEARER_TOKEN")
    if not bearer:
        raise SystemExit("Missing required credential: X_BEARER_TOKEN")
    os.environ["X_BEARER_TOKEN"] = bearer
    for key in ("X_API_KEY", "X_API_SECRET"):
        val = os.getenv(key)
        if val:
            os.environ[key] = val


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


def strip_noise(text: str) -> str:
    s = URL_RE.sub("", text or "")
    s = HASHTAG_RE.sub("", s)
    s = re.sub(r"@\w+", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def enforce_style(text: str, *, remove_links: bool = False, no_hashtags: bool = False) -> str:
    s = text or ""
    s = s.replace("!", "")
    s = s.replace("—", " ").replace("–", " ")
    s = EMOJI_RE.sub("", s)
    if remove_links:
        s = URL_RE.sub("", s)
    if no_hashtags:
        s = HASHTAG_RE.sub("", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:278]


def root_ideas(role: str) -> str:
    ideas = {
        "founder": "We are building accountable AI operations where identity, bounds, and receipts are structural, not optional.",
        "brand": "Structural trust means governance lives in infrastructure and every meaningful action is verifiable.",
        "product-agent": "Agent systems get reliable when memory, orchestration, and verification are designed as one operating model.",
    }
    return ideas.get(role, ideas["brand"])


def detect_topic(source_text: str) -> tuple[str, str]:
    s = (source_text or "").lower()
    topic_map = [
        ("evals", ["eval", "benchmark", "test", "score", "grade", "leaderboard"]),
        ("memory", ["memory", "context", "recall", "state", "retrieval", "rag"]),
        ("orchestration", ["orchestration", "workflow", "pipeline", "automation", "scheduler", "queue", "routing"]),
        ("governance", ["governance", "policy", "compliance", "guardrail", "control", "constraints"]),
        ("verification", ["verify", "proof", "receipt", "audit", "on-chain", "attestation"]),
        ("agent", ["agent", "autonomous", "multi-agent", "copilot"]),
        ("distribution", ["distribution", "growth", "retention", "onboarding", "funnel", "activation"]),
        ("shipping", ["ship", "release", "roadmap", "milestone", "launch", "repo", "sdk", "api", "integration", "supports"]),
    ]
    for topic, kws in topic_map:
        for kw in kws:
            if kw in s:
                return topic, kw
    return "general", ""

def build_reply_text(role: str, target_user: str, source_text: str, idx_seed: int) -> str:
    topic, kw = detect_topic(source_text)
    k = kw or "this"

    variants = {
        "founder": {
            "evals": [
                f"@{target_user} Strong point on evals. In practice, {k} only matters if it changes routing decisions and failure handling.",
                f"@{target_user} Agree on eval direction. We treat {k} as an operating control, not a reporting artifact.",
            ],
            "verification": [
                f"@{target_user} This maps to our view. Verification has to be built into execution, not added after the fact.",
                f"@{target_user} Yes. Without verifiable receipts, accountability collapses into trust claims.",
            ],
            "distribution": [
                f"@{target_user} Distribution is the constraint most teams underprice. Measurable retention is what validates the channel.",
                f"@{target_user} Good framing. Distribution quality shows up in repeatable retention, not reach spikes.",
            ],
            "general": [
                f"@{target_user} Useful angle. What matters is whether this improves operator control or reliability under load.",
                f"@{target_user} I look at this through execution quality. If it is measurable in production, it is worth building on.",
            ],
        },
        "product-agent": {
            "evals": [
                f"@{target_user} Useful thread. How are you feeding eval outcomes back into orchestration policy after deployment?",
                f"@{target_user} Curious about your eval loop design. Do failed cases automatically update routing or guardrails?",
            ],
            "memory": [
                f"@{target_user} Good point on memory. Are you separating short-term context from durable decisions in your pipeline?",
                f"@{target_user} Memory quality usually decides reliability. How are you handling stale context detection?",
            ],
            "orchestration": [
                f"@{target_user} Strong orchestration point. Are you optimizing for throughput, reliability, or reversibility first?",
                f"@{target_user} Practical question: what part of the orchestration stack is your current bottleneck?",
            ],
            "general": [
                f"@{target_user} Useful angle. What has this changed in your production workflow so far?",
                f"@{target_user} Thanks for sharing. What metric improved most after this change?",
            ],
        },
        "brand": {
            "governance": [
                f"@{target_user} This is aligned with how we think about governance. Constraints need to be enforceable in system behavior.",
                f"@{target_user} Agreed. Governance only works when the system can prove what was allowed and what was blocked.",
            ],
            "verification": [
                f"@{target_user} Exactly. Verification quality determines whether trust is operational or just narrative.",
                f"@{target_user} Same view here. Verifiable proof creates accountability that survives handoffs and scale.",
            ],
            "orchestration": [
                f"@{target_user} Strong point. Reliable orchestration is usually the difference between demos and durable systems.",
                f"@{target_user} We see this too. Orchestration quality compounds faster than model-level tuning.",
            ],
            "general": [
                f"@{target_user} Solid perspective. The key test is whether it improves measurable outcomes in production.",
                f"@{target_user} Useful perspective. Operational value shows up when the idea survives real deployment constraints.",
            ],
        },
    }

    role_bucket = variants.get(role, variants["brand"])
    options = role_bucket.get(topic) or role_bucket["general"]
    return options[idx_seed % len(options)]


def contains_denylist(text: str, keywords: list[str]) -> bool:
    t = (text or "").lower()
    return any(k.lower() in t for k in keywords)


def source_anchor(text: str) -> str:
    stop = {
        "this", "that", "with", "from", "your", "about", "into", "once", "when", "what",
        "have", "been", "they", "them", "then", "than", "will", "just", "more", "less",
    }
    words = re.findall(r"[a-zA-Z0-9]+", (text or "").lower())
    keep = [w for w in words if len(w) > 3 and w not in stop]
    if not keep:
        return ""
    return " ".join(keep[:4])


def canonical_reply(text: str) -> str:
    s = (text or "").lower().strip()
    s = re.sub(r"@\w+", "", s)
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def default_resolver(target_user: str | None, account: str) -> dict | None:
    account_queries = {
        "TheCesarCross": "AI founders OR agentic workflow OR product distribution",
        "sovren_software": "AI automation OR workflow systems OR developer tools",
    }

    if target_user:
        query = f"from:{target_user} -is:retweet"
    else:
        query = account_queries.get(account, "AI products OR automation")

    data = run_json(["x-cli", "-j", "tweet", "search", query, "--max", "15"])
    if not isinstance(data, list) or not data:
        return None

    for t in data:
        if not isinstance(t, dict):
            continue
        tweet_id = t.get("id")
        text = t.get("text") or ""
        author = (t.get("author", {}).get("username") if isinstance(t.get("author"), dict) else None)
        if not tweet_id or not text:
            continue
        if LOW_SIGNAL_RE.search(text):
            continue
        return {"id": str(tweet_id), "text": text, "author": author}
    return None


def hydrate_single_action(action: dict, policy: dict, resolver: Resolver, seen: dict) -> dict:
    out = dict(action)
    account = out.get("account", "")
    role = policy.get("account_strategy", {}).get(account, {}).get("role", "brand")
    founder_keywords = policy.get("founder_denylist", {}).get("keywords", [])

    style = policy.get("copy_style", {}).get("for_all_accounts", {})
    no_hashtags = bool(style.get("no_hashtags", True))
    no_links_in_replies = bool(style.get("no_links_in_replies", True))

    if out.get("action") == "root_post":
        post_text = enforce_style(root_ideas(role), no_hashtags=no_hashtags)
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

        tweet_id = str(candidate["id"])
        if tweet_id in seen["tweet_ids"]:
            out["hydration_status"] = "blocked"
            out["hydration_reason"] = "duplicate_target_tweet"
            return out

        source_text = strip_noise(candidate.get("text", ""))
        if not source_text or LOW_SIGNAL_RE.search(source_text):
            out["hydration_status"] = "blocked"
            out["hydration_reason"] = "low_signal_source"
            return out

        topic, _ = detect_topic(source_text)
        anchor = source_anchor(source_text)
        if topic == "general" and len(anchor.split()) < 2:
            out["hydration_status"] = "blocked"
            out["hydration_reason"] = "insufficient_context_specificity"
            return out

        target_user = out.get("target_user") or candidate.get("author") or "builder"
        idx_seed = len(seen["reply_norms"]) + len(target_user) + len(tweet_id)
        reply_raw = build_reply_text(role, target_user, source_text, idx_seed)
        if anchor and len(anchor.split()) >= 2:
            reply_raw = f"{reply_raw} Specific to {anchor}."
        reply_text = enforce_style(reply_raw, remove_links=no_links_in_replies, no_hashtags=no_hashtags)

        if role == "founder" and contains_denylist(reply_text, founder_keywords):
            out["hydration_status"] = "blocked"
            out["hydration_reason"] = "founder_denylist_hit"
            return out

        norm = canonical_reply(reply_text)
        if norm in seen["reply_norms"]:
            out["hydration_status"] = "blocked"
            out["hydration_reason"] = "duplicate_reply_text"
            return out

        seen["tweet_ids"].add(tweet_id)
        seen["reply_norms"].add(norm)

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

    seen = {"tweet_ids": set(), "reply_norms": set()}

    for account, payload in review.get("accounts", {}).items():
        approved = payload.get("approved_actions", [])
        hydrated_approved = []
        for action in approved:
            total += 1
            h = hydrate_single_action(action, policy, resolver, seen)
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
