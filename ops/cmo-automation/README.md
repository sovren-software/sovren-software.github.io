CMO Automation (X/Twitter)

Purpose
- Internal, data-driven replacement for outsourced engagement operations.
- Covers two coordinated accounts:
  - @TheCesarCross (founder)
  - @sovren_software (brand)

What this does today
1) Collect snapshot data from X API (profile + timeline)
2) Analyze behavior and output baseline metrics
3) Generate a conservative dry-run engagement queue
4) Score the queue for risk/quality before any execution
5) Hydrate approved actions with copy + x-cli commands
6) Build execution report from approved actions (dry-run default)

Current mode
- Scheduled root posts only. No automated replies or quotes.
- @mrhaven_agent was removed after X suspension for inauthentic behavior (2026-04-03).
- API credentials are per-account (X_FOUNDER_* for @TheCesarCross, X_SOVREN_* for @sovren_software).
- See reports/CMO-AUTOMATION-IMPLEMENTATION-PLAN.md Phase 7 for full decision log.

Structure
- config/cmo_accounts.yaml
- config/operating_policy.json
- scripts/collect_x_data.py
- scripts/analyze_x_cmo.py
- scripts/generate_engagement_queue.py
- scripts/review_engagement_queue.py
- scripts/reconstruct_fiverr_playbook.py
- scripts/hydrate_approved_queue.py
- scripts/execute_approved_queue.py
- reports/CMO-AUTOMATION-IMPLEMENTATION-PLAN.md
- reports/CMO-CUTOVER-48H-RUNBOOK.md
- reports/CMO-ECOSYSTEM-MARKETING-BRIEF.md
- reports/CMO-QUALITY-UPGRADE-2026-04-02.md

Quick start
1) Export credentials (or source ~/.claude/secrets.env)
   - App credentials: X_API_KEY, X_API_SECRET, X_BEARER_TOKEN
   - Per-account tokens: X_FOUNDER_ACCESS_TOKEN, X_FOUNDER_ACCESS_SECRET (for @TheCesarCross)
   - Per-account tokens: X_SOVREN_ACCESS_TOKEN, X_SOVREN_ACCESS_SECRET (for @sovren_software)
2) Run:
   - python3 scripts/collect_x_data.py
   - python3 scripts/analyze_x_cmo.py
  - python3 scripts/generate_engagement_queue.py
  - python3 scripts/review_engagement_queue.py
  - python3 scripts/reconstruct_fiverr_playbook.py
  - python3 scripts/hydrate_approved_queue.py
  - python3 scripts/execute_approved_queue.py --input reports/cmo-hydrated-queue.json

Outputs
- data/latest.json
- reports/cmo-analysis.json
- reports/cmo-analysis.md
- data/engagement-queue.json
- reports/cmo-queue-review.json
- reports/cmo-queue-review.md
- reports/cmo-hydrated-queue.json
- reports/cmo-hydrated-queue.md
- reports/cmo-execution-report.json
- reports/cmo-execution-report.md

Guardrails
- Generic short-reply behavior is penalized.
- Repetitive opener patterns are penalized.
- Per-account recommended caps are enforced by policy review before execution.
- Voice style enforcement for generated copy: no exclamation marks, no emojis, no em/en dashes.
- Additional quality constraints: no hashtags, no links in replies, no duplicate target tweet IDs, no duplicate reply patterns.
- Context-specificity gate blocks generic or low-signal reply candidates.

Notes
- Standard practice is to commit strategy/docs/scripts and avoid volatile runtime snapshots.
- For major cutovers or upgrades, commit representative execution artifacts to preserve auditability of behavior changes.
