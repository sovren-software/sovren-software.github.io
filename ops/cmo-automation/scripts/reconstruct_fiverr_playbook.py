#!/usr/bin/env python3
import json
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
REPORTS.mkdir(parents=True, exist_ok=True)

OUT_JSON = REPORTS / "fiverr-playbook-reconstruction.json"
OUT_MD = REPORTS / "fiverr-playbook-reconstruction.md"

LOOKBACK_DAYS = 21
SHORT_LEN = 90
OPENERS = ["Totally agree", "Agree", "Appreciate", "Nice take", "We value", "Right then"]


def parse_dt(ts: str):
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def is_reply(tweet: dict) -> bool:
    return any(r.get("type") == "replied_to" for r in (tweet.get("referenced_tweets") or []) if isinstance(r, dict))


def normalize_snapshot(path: Path):
    payload = json.loads(path.read_text())
    captured_at = payload.get("captured_at")
    items = []
    for handle, account in payload.get("accounts", {}).items():
        for t in account.get("timeline", []):
            created = t.get("created_at")
            if not created:
                continue
            text = t.get("text", "")
            pm = t.get("public_metrics", {})
            items.append(
                {
                    "handle": handle,
                    "tweet_id": t.get("id"),
                    "created_at": created,
                    "captured_at": captured_at,
                    "is_reply": is_reply(t),
                    "is_short": len(text) <= SHORT_LEN,
                    "starts_with_at": text.startswith("@"),
                    "opener": next((o for o in OPENERS if o.lower() in text.lower()), None),
                    "impressions": pm.get("impression_count", 0),
                    "likes": pm.get("like_count", 0),
                    "text": text,
                }
            )
    return items


def main() -> None:
    snapshots = sorted(DATA.glob("snapshot-*.json"))
    if not snapshots:
        raise SystemExit("No snapshots found. Run collect_x_data.py over multiple intervals first.")

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=LOOKBACK_DAYS)

    merged = {}
    for snap in snapshots:
        for i in normalize_snapshot(snap):
            try:
                created = parse_dt(i["created_at"])
            except Exception:
                continue
            if created < cutoff:
                continue
            key = (i["handle"], i["tweet_id"])
            merged[key] = i

    records = list(merged.values())

    by_account = {}
    for r in records:
        by_account.setdefault(r["handle"], []).append(r)

    report = {
        "generated_at": now.isoformat(),
        "lookback_days": LOOKBACK_DAYS,
        "snapshot_count": len(snapshots),
        "accounts": {},
    }

    for handle, arr in by_account.items():
        replies = [x for x in arr if x["is_reply"]]
        short_replies = [x for x in replies if x["is_short"]]
        generic = [x for x in replies if x["opener"]]

        # proxy “worked” vs “did not” (can be improved later with follower-normalized rates)
        worked = [x for x in replies if (x["likes"] > 0 or x["impressions"] >= 10)]
        failed = [x for x in replies if (x["likes"] == 0 and x["impressions"] < 10)]

        report["accounts"][handle] = {
            "total_posts": len(arr),
            "reply_count": len(replies),
            "reply_ratio": round(len(replies) / len(arr), 3) if arr else None,
            "short_reply_ratio": round(len(short_replies) / len(replies), 3) if replies else None,
            "generic_opener_ratio": round(len(generic) / len(replies), 3) if replies else None,
            "top_openers": Counter([x["opener"] for x in generic]).most_common(6),
            "worked_count": len(worked),
            "failed_count": len(failed),
            "worked_examples": [{"id":x["tweet_id"],"text":x["text"][:140],"likes":x["likes"],"impressions":x["impressions"]} for x in worked[:5]],
            "failed_examples": [{"id":x["tweet_id"],"text":x["text"][:140],"likes":x["likes"],"impressions":x["impressions"]} for x in failed[:5]],
        }

    OUT_JSON.write_text(json.dumps(report, indent=2))

    lines = [
        "# Fiverr-Style Playbook Reconstruction",
        f"Generated: {report['generated_at']}",
        f"Snapshots analyzed: {report['snapshot_count']}",
        "",
    ]
    for h, s in report["accounts"].items():
        lines += [
            f"## @{h}",
            f"- total posts: {s['total_posts']}",
            f"- reply ratio: {s['reply_ratio']}",
            f"- short-reply ratio: {s['short_reply_ratio']}",
            f"- generic opener ratio: {s['generic_opener_ratio']}",
            f"- worked/failed (proxy): {s['worked_count']}/{s['failed_count']}",
            f"- top openers: {s['top_openers']}",
            "",
        ]

    OUT_MD.write_text("\n".join(lines))
    print(str(OUT_JSON))
    print(str(OUT_MD))


if __name__ == "__main__":
    main()
