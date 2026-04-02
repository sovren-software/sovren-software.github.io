#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "data" / "engagement-queue.json"
ANALYSIS_PATH = ROOT / "reports" / "cmo-analysis.json"
OUT_JSON = ROOT / "reports" / "cmo-queue-review.json"
OUT_MD = ROOT / "reports" / "cmo-queue-review.md"

# policy thresholds
MAX_REPLY_SHARE = 0.6
MAX_SHORT_REPLY_SHARE = 0.6


def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def main() -> None:
    if not QUEUE_PATH.exists():
        raise SystemExit("Missing engagement queue; run generate_engagement_queue.py first")
    if not ANALYSIS_PATH.exists():
        raise SystemExit("Missing analysis report; run analyze_x_cmo.py first")

    queue = json.loads(QUEUE_PATH.read_text())
    analysis = json.loads(ANALYSIS_PATH.read_text())

    actions = queue.get("actions", [])
    account_stats = analysis.get("accounts", {})

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

    for account, items in by_account.items():
        stats = account_stats.get(account, {})
        reply_items = [i for i in items if i.get("action") == "reply"]
        root_items = [i for i in items if i.get("action") == "root_post"]

        reply_ratio = stats.get("reply_ratio")
        short_reply_ratio = stats.get("short_reply_ratio")

        risk_flags = []
        if reply_ratio is not None and reply_ratio > MAX_REPLY_SHARE:
            risk_flags.append(f"historical reply ratio too high: {reply_ratio}")
        if short_reply_ratio is not None and short_reply_ratio > MAX_SHORT_REPLY_SHARE:
            risk_flags.append(f"historical short-reply ratio too high: {short_reply_ratio}")

        # confidence: start conservative, add/subtract based on historical quality
        conf = 0.5
        conf -= 0.2 if risk_flags else 0.0
        conf += 0.2 if stats.get("avg_likes", 0) >= 1 else 0.0
        conf += 0.1 if stats.get("avg_impressions", 0) >= 10 else 0.0
        conf = round(clamp(conf, 0.0, 1.0), 2)

        # decision: if risky history, recommend root-heavy only
        if risk_flags:
            approved = [i for i in root_items]
            rejected = [i for i in reply_items]
            recommendation = "root_only"
        else:
            approved = items
            rejected = []
            recommendation = "approve_with_caps"

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
            "confidence": conf,
            "risk_flags": risk_flags,
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
        if approval_rate >= 0.7:
            review["global_recommendation"] = "assisted_execute"
        elif approval_rate > 0:
            review["global_recommendation"] = "root_only_assisted"
        else:
            review["global_recommendation"] = "hold"
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
            f"- risk flags: {r['risk_flags']}",
            "",
        ]

    OUT_MD.write_text("\n".join(md))
    print(str(OUT_JSON))
    print(str(OUT_MD))


if __name__ == "__main__":
    main()
