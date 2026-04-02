import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import execute_approved_queue  # noqa: E402


class ExecuteApprovedQueueTests(unittest.TestCase):
    def test_flatten_approved_actions_only(self):
        review = {
            "accounts": {
                "TheCesarCross": {
                    "approved_actions": [
                        {"account": "TheCesarCross", "action": "root_post"},
                        {"account": "TheCesarCross", "action": "reply", "target_user": "alice"},
                    ],
                    "rejected_actions": [
                        {"account": "TheCesarCross", "action": "reply", "target_user": "bob"}
                    ],
                },
                "sovren_software": {
                    "approved_actions": [
                        {"account": "sovren_software", "action": "reply", "target_user": "carol"}
                    ],
                    "rejected_actions": [],
                },
            }
        }

        actions = execute_approved_queue.flatten_approved_actions(review)

        self.assertEqual(3, len(actions))
        self.assertEqual("root_post", actions[0]["action"])
        self.assertEqual("carol", actions[2]["target_user"])

    def test_build_execution_plan_requires_payload(self):
        review = {
            "mode": "dry-run",
            "accounts": {
                "TheCesarCross": {
                    "approved_actions": [
                        {"account": "TheCesarCross", "action": "root_post"},
                        {"account": "TheCesarCross", "action": "reply", "target_user": "alice"},
                    ],
                }
            },
        }

        plan = execute_approved_queue.build_execution_plan(review, live=False)

        self.assertEqual(2, plan["summary"]["total_approved"])
        self.assertEqual(0, plan["summary"]["ready_to_execute"])
        reasons = {x["reason"] for x in plan["actions"]}
        self.assertIn("missing_root_text", reasons)
        self.assertIn("missing_reply_payload", reasons)


if __name__ == "__main__":
    unittest.main()
