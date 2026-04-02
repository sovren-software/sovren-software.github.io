#!/usr/bin/env python3
import json
import re
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
REPORTS.mkdir(parents=True, exist_ok=True)

OPENERS = ["Totally agree", "Agree", "Appreciate", "Nice take", "We value", "Right then"]
LOOKBACK_DAYS = 21
SHORT_REPLY_THRESHOLD = 90


def parse_dt(s: str):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def is_reply(tweet: dict) -> bool:
    return any(r.get("type") == "replied_to" for r in (tweet.get("referenced_tweets") or []) if isinstance(r, dict))


def opener_tag(text: str) -> str | None:
    for o in OPENERS:
        if o.lower() in text.lower():
            return o
    return None


def main() -> None:
    src = DATA / "latest.json"
    if not src.exists():
        raise SystemExit(f"Missing {src}. Run collect_x_data.py first.")

    payload = json.loads(src.read_text())
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=LOOKBACK_DAYS)

    report = {
        "generated_at": now.isoformat(),
        "lookback_days": LOOKBACK_DAYS,
        "accounts": {},
        "cross_account": {},
    }

    account_reply_users = {}

    for handle, account in payload["accounts"].items():
        profile = account["profile"]
        timeline = account["timeline"]

        recent = [t for t in timeline if t.get("created_at") and parse_dt(t["created_at"]) >= cutoff]
        replies = [t for t in recent if is_reply(t)]
        roots = [t for t in recent if not is_reply(t)]

        short_replies = [t for t in replies if len(t.get("text", "")) <= SHORT_REPLY_THRESHOLD]
        opener_hits = [opener_tag(t.get("text", "")) for t in replies]
        opener_hits = [x for x in opener_hits if x]

        mention_users = []
        for t in replies:
            for m in t.get("entities", {}).get("mentions", []):
                u = m.get("username")
                if u:
                    mention_users.append(u.lower())

        account_reply_users[handle] = set(mention_users)

        impressions = [t.get("public_metrics", {}).get("impression_count", 0) for t in recent]
        likes = [t.get("public_metrics", {}).get("like_count", 0) for t in recent]

        report["accounts"][handle] = {
            "followers": profile.get("public_metrics", {}).get("followers_count", 0),
            "following": profile.get("public_metrics", {}).get("following_count", 0),
            "tweet_count": profile.get("public_metrics", {}).get("tweet_count", 0),
            "posts_in_window": len(recent),
            "reply_count": len(replies),
            "root_count": len(roots),
            "reply_ratio": round(len(replies) / len(recent), 3) if recent else None,
            "short_reply_ratio": round(len(short_replies) / len(replies), 3) if replies else None,
            "avg_impressions": round(sum(impressions) / len(impressions), 2) if impressions else 0,
            "avg_likes": round(sum(likes) / len(likes), 2) if likes else 0,
            "top_openers": Counter(opener_hits).most_common(5),
            "top_reply_targets": Counter(mention_users).most_common(10),
            "recent_samples": [
                {
                    "id": t.get("id"),
                    "created_at": t.get("created_at"),
                    "text": t.get("text", "")[:160],
                    "impressions": t.get("public_metrics", {}).get("impression_count", 0),
                    "likes": t.get("public_metrics", {}).get("like_count", 0),
                }
                for t in recent[:8]
            ],
        }

    # Audience overlap from reply targets
    handles = list(account_reply_users.keys())
    overlap = {}
    for i in range(len(handles)):
        for j in range(i + 1, len(handles)):
            a, b = handles[i], handles[j]
            inter = sorted(account_reply_users[a].intersection(account_reply_users[b]))
            overlap[f"{a}__{b}"] = {
                "count": len(inter),
                "sample": inter[:20],
            }
    report["cross_account"]["reply_target_overlap"] = overlap

    out_json = REPORTS / "cmo-analysis.json"
    out_md = REPORTS / "cmo-analysis.md"
    out_json.write_text(json.dumps(report, indent=2))

    lines = [
        "# Automated CMO Baseline Analysis",
        f"Generated: {report['generated_at']}",
        "",
    ]
    for h, r in report["accounts"].items():
        lines += [
            f"## @{h}",
            f"- followers/following: {r['followers']}/{r['following']}",
            f"- posts in {LOOKBACK_DAYS}d window: {r['posts_in_window']}",
            f"- reply ratio: {r['reply_ratio']}",
            f"- short reply ratio (<= {SHORT_REPLY_THRESHOLD} chars): {r['short_reply_ratio']}",
            f"- avg impressions: {r['avg_impressions']}",
            f"- avg likes: {r['avg_likes']}",
            f"- top openers: {r['top_openers']}",
            "",
        ]

    lines += ["## Cross-account reply target overlap", ""]
    for k, v in overlap.items():
        lines.append(f"- {k}: {v['count']} overlap")

    out_md.write_text("\n".join(lines))
    print(str(out_json))
    print(str(out_md))


if __name__ == "__main__":
    main()
