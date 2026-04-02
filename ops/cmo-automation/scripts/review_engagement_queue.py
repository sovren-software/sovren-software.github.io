#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "data" / "engagement-queue.json"
ANALYSIS_PATH = ROOT / "reports" / "cmo-analysis.json"
POLICY_PATH = ROOT / "config" / "operating_policy.json"
OUT_JSON = ROOT / "reports" / "cmo-queue-review.json"
OUT_MD = ROOT / "reports" / "cmo-queue-review.md"


def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def has_denylist_hit(action: dict, deny_keywords: list[str]) -> bool:
    text = " ".join(
        [
            str(action.get("target_user") or ""),
            str(action.get("why") or ""),
            str(action.get("target_pool") or ""),
        ]
    ).lower()
    return any(k.lower() in text for k in deny_keywords)


def main() -> None:
    for p in [QUEUE_PATH, ANALYSIS_PATH, POLICY_PATH]:
        if not p.exists():
            raise SystemExit(f"Missing required input: {p}")

    queue = json.loads(QUEUE_PATH.read_text())
    analysis = json.loads(ANALYSIS_PATH.read_text())
    policy = json.loads(POLICY_PATH.read_text())

    actions = queue.get("actions", [])
    account_stats = analysis.get("accounts", {})
    account_policy = policy.get("account_strategy", {})

    MAX_REPLY_SHARE = 0.9
    MAX_SHORT_REPLY_SHARE = 0.8

    by_account = {}
    for a in actions:
        by_account.setdefault(a["account"], []).append(a)

    review = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": queue.get("mode", "unknown"),
        "accounts": {},
        "global_recommendation": "hold",
        "notes": [],
    }

    approves = 0
    total = 0

    founder_deny_keywords = policy.get("founder_denylist", {}).get("keywords", [])

    for account, items in by_account.items():
        stats = account_stats.get(account, {})
        caps = account_policy.get(account, {})
        daily_reply_cap = int(caps.get("daily_reply_cap", 6))

        reply_items = [i for i in items if i.get("action") == "reply"]
        root_items = [i for i in items if i.get("action") == "root_post"]

        reply_ratio = stats.get("reply_ratio")
        short_reply_ratio = stats.get("short_reply_ratio")

        risk_flags = []
        if reply_ratio is not None and reply_ratio > MAX_REPLY_SHARE:
            risk_flags.append(f"historical reply ratio high: {reply_ratio}")
        if short_reply_ratio is not None and short_reply_ratio > MAX_SHORT_REPLY_SHARE:
            risk_flags.append(f"historical short-reply ratio high: {short_reply_ratio}")

        founder_filtered = []
        if account == "TheCesarCross":
            for r in reply_items:
                if has_denylist_hit(r, founder_deny_keywords):
                    founder_filtered.append(r)

        # confidence score
        conf = 0.55
        conf -= 0.1 if risk_flags else 0.0
        conf -= 0.1 if founder_filtered else 0.0
        conf += 0.1 if stats.get("avg_likes", 0) >= 1 else 0.0
        conf += 0.1 if stats.get("avg_impressions", 0) >= 10 else 0.0
        conf = round(clamp(conf, 0.0, 1.0), 2)

        # approval logic: keep automation moving, but enforce caps and denylist
        approved_replies = [r for r in reply_items if r not in founder_filtered][:daily_reply_cap]

        # if history is risky, throttle replies but do not halt entirely
        if risk_flags:
            approved_replies = approved_replies[: max(1, daily_reply_cap // 2)]
            recommendation = "throttled_autonomous"
        else:
            recommendation = "autonomous_with_posthoc"

        approved = root_items + approved_replies
        rejected = [r for r in reply_items if r not in approved_replies]

        approves += len(approved)
        total += len(items)

        review["accounts"][account] = {
            "historical": {
                "reply_ratio": reply_ratio,
                "short_reply_ratio": short_reply_ratio,
                "avg_impressions": stats.get("avg_impressions"),
                "avg_likes": stats.get("avg_likes"),
            },
            "queue_counts": {
                "total": len(items),
                "reply": len(reply_items),
                "root": len(root_items),
            },
            "applied_cap": daily_reply_cap,
            "confidence": conf,
            "risk_flags": risk_flags,
            "founder_denylist_rejections": len(founder_filtered),
            "recommendation": recommendation,
            "approved_count": len(approved),
            "rejected_count": len(rejected),
            "approved_actions": approved,
            "rejected_actions": rejected,
        }

    if total == 0:
        review["global_recommendation"] = "no_actions"
        review["notes"].append("Queue contains no actions.")
    else:
        approval_rate = approves / total
        review["global_recommendation"] = (
            "autonomous_with_posthoc" if approval_rate >= 0.5 else "throttled_autonomous"
        )
        review["notes"].append(f"approval_rate={approval_rate:.2f}")

    OUT_JSON.write_text(json.dumps(review, indent=2))

    md = [
        "# CMO Engagement Queue Review",
        f"Generated: {review['generated_at']}",
        f"Global recommendation: {review['global_recommendation']}",
        "",
    ]
    for account, r in review["accounts"].items():
        md += [
            f"## @{account}",
            f"- confidence: {r['confidence']}",
            f"- recommendation: {r['recommendation']}",
            f"- queue (total/reply/root): {r['queue_counts']['total']}/{r['queue_counts']['reply']}/{r['queue_counts']['root']}",
            f"- approved: {r['approved_count']} | rejected: {r['rejected_count']}",
            f"- cap applied: {r['applied_cap']}",
            f"- founder denylist rejections: {r['founder_denylist_rejections']}",
            f"- risk flags: {r['risk_flags']}",
            "",
        ]

    OUT_MD.write_text("\n".join(md))
    print(str(OUT_JSON))
    print(str(OUT_MD))


if __name__ == "__main__":
    main()
