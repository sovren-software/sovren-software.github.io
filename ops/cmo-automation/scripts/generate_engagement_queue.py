#!/usr/bin/env python3
import json
import random
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "reports" / "cmo-analysis.json"
POLICY = ROOT / "config" / "operating_policy.json"
OUT = ROOT / "data" / "engagement-queue.json"


def load_json(path: Path):
    if not path.exists():
        raise SystemExit(f"Missing {path}")
    return json.loads(path.read_text())


def split_counts(total: int, core_pct: int):
    core = int(round(total * core_pct / 100.0))
    discovery = max(0, total - core)
    return core, discovery


def main() -> None:
    analysis = load_json(ANALYSIS)
    policy = load_json(POLICY)

    queue = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "dry-run" if policy.get("automation", {}).get("dry_run_default", True) else "live",
        "policy_ref": str(POLICY),
        "actions": [],
    }

    targeting = policy.get("targeting", {})
    core_pct = targeting.get("core_whitelist_pct", 80)

    for handle, stats in analysis.get("accounts", {}).items():
        account_policy = policy.get("account_strategy", {}).get(handle, {})
        daily_reply_cap = int(account_policy.get("daily_reply_cap", 6))
        windows = account_policy.get("time_windows_est", [])

        # Always include one root post anchor action per run cycle.
        queue["actions"].append(
            {
                "account": handle,
                "action": "root_post",
                "priority": "high",
                "window_est": windows,
                "why": "Anchor narrative with original voice-aligned post.",
                "constraints": {
                    "must_pass_voice_review": True,
                    "must_align_strategy": True,
                    "min_gap_minutes": 180,
                },
            }
        )

        # Build candidate pools from observed high-frequency targets.
        observed_targets = [u for u, _ in stats.get("top_reply_targets", [])]
        core_count, discovery_count = split_counts(daily_reply_cap, core_pct)

        # Core (whitelist-style): historically engaged users.
        for target in observed_targets[:core_count]:
            queue["actions"].append(
                {
                    "account": handle,
                    "action": "reply",
                    "target_user": target,
                    "target_pool": "core",
                    "priority": "medium",
                    "window_est": windows,
                    "why": "Continuation of existing interaction graph.",
                    "constraints": {
                        "max_replies_to_same_user_per_24h": 1,
                        "must_be_contextual": True,
                        "must_clear_relevance_score": targeting.get("minimum_relevance_score", 0.7),
                        "min_delay_seconds": random.randint(
                            policy["risk_controls"].get("random_delay_seconds_min", 45),
                            policy["risk_controls"].get("random_delay_seconds_max", 180),
                        ),
                    },
                }
            )

        # Discovery budget: placeholders to be filled by candidate-harvest stage.
        for _ in range(discovery_count):
            queue["actions"].append(
                {
                    "account": handle,
                    "action": "reply",
                    "target_user": None,
                    "target_pool": "discovery",
                    "priority": "low",
                    "window_est": windows,
                    "why": "Exploration budget for net-new qualified audience.",
                    "constraints": {
                        "must_be_contextual": True,
                        "must_clear_relevance_score": targeting.get("minimum_relevance_score", 0.7),
                        "must_not_hit_founder_denylist": handle == "TheCesarCross",
                    },
                }
            )

    OUT.write_text(json.dumps(queue, indent=2))
    print(str(OUT))


if __name__ == "__main__":
    main()
