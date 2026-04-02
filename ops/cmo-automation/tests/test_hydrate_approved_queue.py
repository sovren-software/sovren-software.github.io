import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import hydrate_approved_queue  # noqa: E402


class HydrateApprovedQueueTests(unittest.TestCase):
    def test_enforce_style_removes_exclamation_emoji_and_em_dash(self):
        raw = "Useful launch 🚀 with fast rollout — now live!"
        cleaned = hydrate_approved_queue.enforce_style(raw)
        self.assertNotIn("!", cleaned)
        self.assertNotIn("🚀", cleaned)
        self.assertNotIn("—", cleaned)

    def test_hydrate_root_post_adds_text_and_command(self):
        action = {"account": "sovren_software", "action": "root_post", "priority": "high"}
        policy = {
            "account_strategy": {"sovren_software": {"role": "brand"}},
            "founder_denylist": {"keywords": []},
        }

        out = hydrate_approved_queue.hydrate_single_action(action, policy, resolver=lambda *_: None)

        self.assertEqual("hydrated", out["hydration_status"])
        self.assertTrue(out["post_text"])
        self.assertEqual("x-cli", out["x_cli_command"][0])
        self.assertEqual("post", out["x_cli_command"][3])

    def test_hydrate_reply_uses_quote_workaround_with_candidate(self):
        action = {"account": "TheCesarCross", "action": "reply", "target_user": "alice"}
        policy = {
            "account_strategy": {"TheCesarCross": {"role": "founder"}},
            "founder_denylist": {"keywords": ["giveaway"]},
        }

        def resolver(target_user, account):
            return {"id": "12345", "text": "Shipping useful agent products this week."}

        out = hydrate_approved_queue.hydrate_single_action(action, policy, resolver=resolver)

        self.assertEqual("hydrated", out["hydration_status"])
        self.assertEqual("12345", out["target_tweet_id"])
        self.assertEqual(["x-cli", "-j", "tweet", "quote"], out["x_cli_command"][0:4])
        self.assertIn("@alice", out["reply_text"])

    def test_hydrate_reply_blocks_without_candidate(self):
        action = {"account": "mrhaven_agent", "action": "reply", "target_user": "nobody"}
        policy = {
            "account_strategy": {"mrhaven_agent": {"role": "product-agent"}},
            "founder_denylist": {"keywords": []},
        }

        out = hydrate_approved_queue.hydrate_single_action(action, policy, resolver=lambda *_: None)

        self.assertEqual("blocked", out["hydration_status"])
        self.assertEqual("no_candidate_tweet", out["hydration_reason"])


if __name__ == "__main__":
    unittest.main()
