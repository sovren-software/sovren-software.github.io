#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "reports" / "cmo-queue-review.json"
OUT_JSON = ROOT / "reports" / "cmo-execution-report.json"
OUT_MD = ROOT / "reports" / "cmo-execution-report.md"


def load_json(path: Path):
    if not path.exists():
        raise SystemExit(f"Missing required input: {path}")
    return json.loads(path.read_text())


ACCOUNT_TOKEN_MAP = {
    "TheCesarCross": ("X_FOUNDER_ACCESS_TOKEN", "X_FOUNDER_ACCESS_SECRET"),
    "sovren_software": ("X_SOVREN_ACCESS_TOKEN", "X_SOVREN_ACCESS_SECRET"),
}


def load_credential_mapping() -> None:
    """Load X API app credentials. Per-account tokens are set before each action."""
    for key in ("X_API_KEY", "X_API_SECRET", "X_BEARER_TOKEN"):
        val = os.getenv(key)
        if not val:
            raise SystemExit(f"Missing required credential: {key}")
        os.environ[key] = val
    # Validate per-account tokens exist
    for account, (tok, sec) in ACCOUNT_TOKEN_MAP.items():
        if not os.getenv(tok) or not os.getenv(sec):
            raise SystemExit(f"Missing access tokens for @{account}: {tok}, {sec}")


def set_account_tokens(account: str) -> None:
    """Set X_ACCESS_TOKEN/SECRET for the given account before x-cli execution."""
    token_keys = ACCOUNT_TOKEN_MAP.get(account)
    if not token_keys:
        raise RuntimeError(f"No credentials configured for @{account}")
    os.environ["X_ACCESS_TOKEN"] = os.getenv(token_keys[0], "")
    os.environ["X_ACCESS_TOKEN_SECRET"] = os.getenv(token_keys[1], "")


def flatten_approved_actions(review: dict) -> list[dict]:
    actions: list[dict] = []
    for account, payload in review.get("accounts", {}).items():
        for action in payload.get("approved_actions", []):
            if not action.get("account"):
                action = {**action, "account": account}
            actions.append(action)
    return actions


def classify_action(action: dict) -> tuple[bool, str]:
    if isinstance(action.get("x_cli_command"), list) and action["x_cli_command"]:
        return True, "explicit_command"

    kind = action.get("action")
    if kind == "root_post":
        text = action.get("post_text") or action.get("text")
        if not text:
            return False, "missing_root_text"
        return False, "missing_x_cli_command"

    if kind == "reply":
        if not action.get("reply_to_tweet_id") or not (action.get("reply_text") or action.get("text")):
            return False, "missing_reply_payload"
        return False, "missing_x_cli_command"

    return False, "unsupported_action_type"


def run_live(action: dict) -> dict:
    cmd = action.get("x_cli_command")
    if not isinstance(cmd, list) or not cmd:
        return {"status": "blocked", "reason": "missing_x_cli_command"}

    proc = subprocess.run(cmd, capture_output=True, text=True)
    return {
        "status": "executed" if proc.returncode == 0 else "failed",
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
    }


def build_execution_plan(review: dict, live: bool = False) -> dict:
    actions = flatten_approved_actions(review)
    result_actions = []

    for idx, action in enumerate(actions, start=1):
        ready, reason = classify_action(action)
        row = {
            "id": idx,
            "account": action.get("account"),
            "action": action.get("action"),
            "target_user": action.get("target_user"),
            "ready": ready,
            "reason": reason,
            "source": action,
        }
        if live and ready:
            set_account_tokens(action.get("account", ""))
            row.update(run_live(action))
        elif live:
            row.update({"status": "blocked"})
        else:
            row.update({"status": "planned" if ready else "blocked"})
        result_actions.append(row)

    ready_count = sum(1 for a in result_actions if a["ready"])
    executed_count = sum(1 for a in result_actions if a.get("status") == "executed")
    failed_count = sum(1 for a in result_actions if a.get("status") == "failed")

    plan = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "live" if live else "dry-run",
        "input_review_mode": review.get("mode", "unknown"),
        "summary": {
            "total_approved": len(actions),
            "ready_to_execute": ready_count,
            "blocked": len(actions) - ready_count,
            "executed": executed_count,
            "failed": failed_count,
        },
        "actions": result_actions,
    }
    return plan


def write_reports(plan: dict) -> None:
    OUT_JSON.write_text(json.dumps(plan, indent=2))

    lines = [
        "# CMO Approved Queue Execution Report",
        f"Generated: {plan['generated_at']}",
        f"Mode: {plan['mode']}",
        f"Input review mode: {plan['input_review_mode']}",
        "",
        "## Summary",
        f"- total approved: {plan['summary']['total_approved']}",
        f"- ready to execute: {plan['summary']['ready_to_execute']}",
        f"- blocked: {plan['summary']['blocked']}",
        f"- executed: {plan['summary']['executed']}",
        f"- failed: {plan['summary']['failed']}",
        "",
        "## Action status",
    ]

    for row in plan["actions"]:
        lines.append(
            f"- #{row['id']} @{row.get('account')} {row.get('action')} target={row.get('target_user')} status={row.get('status')} reason={row.get('reason')}"
        )

    OUT_MD.write_text("\n".join(lines) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Execute approved CMO queue actions from review output")
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="Path to cmo-queue-review.json")
    parser.add_argument("--live", action="store_true", help="Attempt to execute actions with explicit x_cli_command")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    review = load_json(Path(args.input))

    if args.live:
        load_credential_mapping()

    plan = build_execution_plan(review, live=args.live)
    write_reports(plan)

    print(str(OUT_JSON))
    print(str(OUT_MD))


if __name__ == "__main__":
    main()
