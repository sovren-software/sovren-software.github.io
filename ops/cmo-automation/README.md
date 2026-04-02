CMO Automation (X/Twitter)

Purpose
- Internal, data-driven replacement for outsourced engagement operations.
- Covers three coordinated accounts:
  - @TheCesarCross
  - @sovren_software
  - @mrhaven_agent

What this does today
1) Collect snapshot data from X API (profile + timeline)
2) Analyze behavior and output baseline metrics
3) Generate a conservative dry-run engagement queue
4) Score the queue for risk/quality before any execution
5) Build execution report from approved actions (dry-run default)

Current mode
- Dry-run / assisted only.
- No autonomous posting in this module yet.

Structure
- config/cmo_accounts.yaml
- config/operating_policy.json
- scripts/collect_x_data.py
- scripts/analyze_x_cmo.py
- scripts/generate_engagement_queue.py
- scripts/review_engagement_queue.py
- scripts/reconstruct_fiverr_playbook.py
- scripts/execute_approved_queue.py
- reports/CMO-AUTOMATION-IMPLEMENTATION-PLAN.md
- reports/CMO-CUTOVER-48H-RUNBOOK.md

Quick start
1) Export credentials (or source ~/.claude/secrets.env)
   - Required: X_API_KEY, X_API_SECRET, X_BEARER_TOKEN, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
   - Script also maps from TWITTER_* variables.
2) Run:
   - python3 scripts/collect_x_data.py
   - python3 scripts/analyze_x_cmo.py
  - python3 scripts/generate_engagement_queue.py
  - python3 scripts/review_engagement_queue.py
  - python3 scripts/reconstruct_fiverr_playbook.py
  - python3 scripts/execute_approved_queue.py

Outputs
- data/latest.json
- reports/cmo-analysis.json
- reports/cmo-analysis.md
- data/engagement-queue.json
- reports/cmo-queue-review.json
- reports/cmo-queue-review.md
- reports/cmo-execution-report.json
- reports/cmo-execution-report.md

Guardrails
- Generic short-reply behavior is penalized.
- Repetitive opener patterns are penalized.
- Per-account recommended caps are enforced by policy review before execution.

Notes
- Generated JSON/analysis artifacts are ignored in git by default.
- Commit strategy/docs/scripts, not volatile runtime snapshots.
