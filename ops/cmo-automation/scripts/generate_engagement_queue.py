#!/usr/bin/env python3
import json
import random
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "cmo-analysis.json"
OUT = ROOT / "data" / "engagement-queue.json"


def main() -> None:
    if not REPORT.exists():
        raise SystemExit("Run analyze_x_cmo.py first")

    r = json.loads(REPORT.read_text())

    queue = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "dry-run",
        "actions": [],
    }

    # Very conservative starter policy: propose root posts + selective replies.
    for handle, stats in r["accounts"].items():
        # root content recommendation
        queue["actions"].append(
            {
                "account": handle,
                "action": "root_post",
                "priority": "high",
                "why": "Keep account voice anchored with original thesis/product narrative.",
                "constraints": {
                    "min_gap_minutes": 180,
                    "must_pass_voice_review": True,
                },
            }
        )

        # reply recommendation from top targets, but cap volume
        targets = [u for u, _ in stats.get("top_reply_targets", [])][:5]
        for t in targets:
            queue["actions"].append(
                {
                    "account": handle,
                    "action": "reply",
                    "target_user": t,
                    "priority": "medium",
                    "why": "User appears in recent interaction graph.",
                    "constraints": {
                        "max_replies_to_same_user_per_24h": 1,
                        "min_delay_seconds": random.randint(45, 180),
                        "must_be_contextual": True,
                    },
                }
            )

    OUT.write_text(json.dumps(queue, indent=2))
    print(str(OUT))


if __name__ == "__main__":
    main()
