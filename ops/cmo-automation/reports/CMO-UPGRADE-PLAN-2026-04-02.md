# CMO Automation Upgrade Plan

> For Hermes: use subagent-driven-development if executing this plan task-by-task.

Goal: strengthen the X CMO automation system where it is currently failing, preserve the quality gains already achieved, and capture the highest-impact quick wins first.

Architecture: keep the current pipeline shape, but tighten the weak joints. The immediate focus is not “more autonomy.” It is better execution preflight, reliable fallback behavior, stronger telemetry, and higher-signal root-post generation from internal product activity. Reply automation remains quality-gated and should only execute live when the platform path is verifiably eligible.

Tech Stack: Python 3, x-cli, JSON report artifacts, unittest, Git-based internal source material.

---

## Current state summary

What is already working:
- collection, analysis, queue generation, review, hydration, and execution reports
- hard copy-style enforcement
- duplicate suppression and context-specific reply gating
- root-post live execution

What is weak:
- reply execution relies on `quote_workaround` and often fails at runtime with X API 403
- no preflight for execution eligibility before live send
- no fallback routing when reply execution is impossible
- no structured telemetry loop that changes future behavior
- root-post generation is not yet driven by real internal product signals
- no per-account execution isolation beyond generic credential mapping

High-impact quick wins:
1. Add execution preflight before live reply attempts
2. Add fallback routing for ineligible replies
3. Add structured failure taxonomy and telemetry report
4. Generate root-post candidates from internal repo activity
5. Tighten review recommendations around execution readiness, not just content readiness

---

## Phase order

Phase 1: stop wasting live attempts
- execution preflight
- fallback routing
- structured failure reasons

Phase 2: increase output quality where execution already works
- internal-signal root posts
- reserve root-post queue

Phase 3: make the system learn
- telemetry rollup
- execution-aware review scoring

Phase 4: harden account operations
- per-account auth routing
- safer live mode controls

---

## Task 1: Introduce explicit execution capability metadata

Objective: make action readiness depend on execution feasibility, not only hydrated copy.

Files:
- Modify: `ops/cmo-automation/config/operating_policy.json`
- Modify: `ops/cmo-automation/README.md`
- Modify: `ops/cmo-automation/reports/CMO-QUALITY-UPGRADE-2026-04-02.md`

Changes:
- Add an `execution_policy` block to `config/operating_policy.json`
- Define allowed execution modes:
  - `root_post`
  - `reply_direct`
  - `quote_workaround`
  - `manual_review`
  - `skip`
- Add fallback order for reply actions:
  - `reply_direct`
  - `quote_workaround`
  - `manual_review`
  - `root_post_reserve`
- Add policy booleans:
  - `preflight_required_for_live_replies`
  - `block_live_when_preflight_unknown`
  - `emit_root_post_reserve_candidates`

Suggested JSON fragment:
```json
"execution_policy": {
  "preflight_required_for_live_replies": true,
  "block_live_when_preflight_unknown": true,
  "emit_root_post_reserve_candidates": true,
  "reply_execution": {
    "preferred_order": ["reply_direct", "quote_workaround", "manual_review", "root_post_reserve"],
    "default_live_mode": "quote_workaround"
  }
}
```

Verification:
- Read policy file and confirm new block exists
- Confirm docs describe that hydrated != live-ready

Commit:
```bash
git -C ~/cDesign/sovren-website add ops/cmo-automation/config/operating_policy.json ops/cmo-automation/README.md ops/cmo-automation/reports/CMO-QUALITY-UPGRADE-2026-04-02.md
git -C ~/cDesign/sovren-website commit -m "docs(cmo): define execution policy and reply fallback model"
```

---

## Task 2: Add execution preflight in hydration

Objective: determine whether a reply candidate is executable before it reaches live execution.

Files:
- Modify: `ops/cmo-automation/scripts/hydrate_approved_queue.py`
- Modify: `ops/cmo-automation/tests/test_hydrate_approved_queue.py`

Changes:
- Add a `preflight_reply_candidate(...)` helper in `hydrate_approved_queue.py`
- Return normalized fields on hydrated reply actions:
  - `preflight_status`: `eligible | ineligible | unknown`
  - `preflight_reason`
  - `planned_execution_mode`
  - `fallback_mode`
- For now, keep preflight heuristic-based if X API cannot expose true eligibility cleanly. Use conservative rules:
  - if candidate tweet missing id -> `ineligible:no_candidate_tweet_id`
  - if target source is low-signal -> already blocked earlier
  - if reply path depends on quote workaround -> mark `unknown` unless explicit eligibility can be checked
- If policy requires preflight for live replies and status is `unknown`, set planned execution to `manual_review` or reserve root-post fallback instead of pretending the action is live-ready.

Suggested output shape:
```json
{
  "action": "reply",
  "target_tweet_id": "123",
  "preflight_status": "unknown",
  "preflight_reason": "quote_eligibility_unverified",
  "planned_execution_mode": "manual_review",
  "fallback_mode": "root_post_reserve"
}
```

Tests to add:
- reply with valid candidate but unknown quote eligibility does not become live-ready
- reply with missing tweet id is blocked or rerouted correctly
- root posts remain unaffected

Run:
```bash
cd ~/cDesign/sovren-website/ops/cmo-automation && python3 -m unittest tests/test_hydrate_approved_queue.py -v
```

Expected:
- all tests pass

Commit:
```bash
git -C ~/cDesign/sovren-website add ops/cmo-automation/scripts/hydrate_approved_queue.py ops/cmo-automation/tests/test_hydrate_approved_queue.py
git -C ~/cDesign/sovren-website commit -m "feat(cmo): add reply preflight and planned execution metadata"
```

---

## Task 3: Add execution fallback routing in executor

Objective: prevent known-bad reply actions from burning live attempts.

Files:
- Modify: `ops/cmo-automation/scripts/execute_approved_queue.py`
- Modify: `ops/cmo-automation/tests/test_execute_approved_queue.py`

Changes:
- Update `classify_action` to treat planned execution metadata as first-class
- Distinguish:
  - `content_ready`
  - `live_ready`
- Only live-execute if:
  - explicit command exists
  - planned execution mode is allowed for live run
  - preflight status is `eligible`
- If `preflight_status` is `unknown` or `ineligible`, mark action as:
  - `status = rerouted` or `status = manual_review`
  - `reason = preflight_unknown` or `reason = preflight_ineligible`
- Add top-level summary counters:
  - `manual_review`
  - `rerouted`
  - `preflight_blocked`

Tests to add:
- action with explicit x command but `preflight_status=unknown` is not executed live
- action with `planned_execution_mode=manual_review` is reported correctly
- root post with explicit command still executes

Run:
```bash
cd ~/cDesign/sovren-website/ops/cmo-automation && python3 -m unittest tests/test_execute_approved_queue.py -v
```

Expected:
- all tests pass

Commit:
```bash
git -C ~/cDesign/sovren-website add ops/cmo-automation/scripts/execute_approved_queue.py ops/cmo-automation/tests/test_execute_approved_queue.py
git -C ~/cDesign/sovren-website commit -m "feat(cmo): block unsafe live replies and report reroutes"
```

---

## Task 4: Normalize failure taxonomy and telemetry artifacts

Objective: make every blocked or failed action usable as feedback for the next cycle.

Files:
- Modify: `ops/cmo-automation/scripts/execute_approved_queue.py`
- Create: `ops/cmo-automation/scripts/summarize_execution_telemetry.py`
- Create: `ops/cmo-automation/reports/README-TELEMETRY.md`

Changes:
- Normalize runtime failure reasons into stable categories:
  - `platform_403_restriction`
  - `missing_payload`
  - `preflight_unknown`
  - `preflight_ineligible`
  - `credential_error`
  - `rate_limit`
  - `transport_error`
  - `unknown_runtime_error`
- Add a telemetry summary script that reads `reports/cmo-execution-report.json` and emits:
  - totals by account
  - totals by action type
  - totals by failure category
  - live success rate by executable mode
- Write outputs to:
  - `reports/cmo-telemetry-summary.json`
  - `reports/cmo-telemetry-summary.md`

Run:
```bash
cd ~/cDesign/sovren-website/ops/cmo-automation && python3 scripts/summarize_execution_telemetry.py
```

Expected:
- two new telemetry summary files written

Commit:
```bash
git -C ~/cDesign/sovren-website add ops/cmo-automation/scripts/summarize_execution_telemetry.py ops/cmo-automation/scripts/execute_approved_queue.py ops/cmo-automation/reports/README-TELEMETRY.md
git -C ~/cDesign/sovren-website commit -m "feat(cmo): add telemetry summary and normalized failure taxonomy"
```

---

## Task 5: Generate root-post candidates from internal product signals

Objective: shift more output toward the highest-signal content we can reliably publish.

Files:
- Create: `ops/cmo-automation/scripts/build_internal_signal_digest.py`
- Modify: `ops/cmo-automation/scripts/generate_engagement_queue.py`
- Create: `ops/cmo-automation/data/internal-signal-digest.json`
- Create: `ops/cmo-automation/reports/internal-signal-digest.md`
- Modify: `ops/cmo-automation/README.md`

Changes:
- Build a digest from repo activity using `git log --oneline` and selected docs
- Start with a narrow allowlist of sources:
  - `~/cDesign/esver-os`
  - `~/cDesign/mr-haven`
  - `~/cDesign/dendrite`
  - `~/cDesign/sovren-website`
- Extract signal items into structured categories:
  - `shipping_change`
  - `architecture_change`
  - `roadmap_milestone`
  - `proof_point`
- Modify `generate_engagement_queue.py` to attach root-post seed context from the digest instead of emitting purely generic root-post placeholders

Suggested queue extension:
```json
{
  "account": "sovren_software",
  "action": "root_post",
  "content_source": "internal_signal_digest",
  "signal_type": "architecture_change",
  "source_repo": "esver-os",
  "source_ref": "59368351",
  "why": "Anchor narrative with a real milestone or proof point."
}
```

Verification:
```bash
cd ~/cDesign/sovren-website/ops/cmo-automation && python3 scripts/build_internal_signal_digest.py && python3 scripts/generate_engagement_queue.py
```

Expected:
- digest files written
- generated queue root posts contain source-backed metadata

Commit:
```bash
git -C ~/cDesign/sovren-website add ops/cmo-automation/scripts/build_internal_signal_digest.py ops/cmo-automation/scripts/generate_engagement_queue.py ops/cmo-automation/README.md
git -C ~/cDesign/sovren-website commit -m "feat(cmo): seed root posts from internal product signals"
```

---

## Task 6: Add reserve root-post fallback queue

Objective: when replies cannot be executed safely, replace them with stronger root content instead of dead-ending.

Files:
- Modify: `ops/cmo-automation/scripts/hydrate_approved_queue.py`
- Modify: `ops/cmo-automation/scripts/execute_approved_queue.py`
- Modify: `ops/cmo-automation/scripts/generate_engagement_queue.py`
- Modify: `ops/cmo-automation/tests/test_hydrate_approved_queue.py`
- Modify: `ops/cmo-automation/tests/test_execute_approved_queue.py`

Changes:
- Add a reserve queue of root-post candidates per account
- When reply action preflight is unknown or ineligible, route to:
  - `manual_review`, or
  - `root_post_reserve`
- Preserve traceability by linking fallback action to original target action:
  - `rerouted_from_action_id`
  - `reroute_reason`

Verification:
- queue shows reserve candidates
- execution report shows reroute instead of failed live attempts for known-bad reply actions

Commit:
```bash
git -C ~/cDesign/sovren-website add ops/cmo-automation/scripts/hydrate_approved_queue.py ops/cmo-automation/scripts/execute_approved_queue.py ops/cmo-automation/scripts/generate_engagement_queue.py ops/cmo-automation/tests/test_hydrate_approved_queue.py ops/cmo-automation/tests/test_execute_approved_queue.py
git -C ~/cDesign/sovren-website commit -m "feat(cmo): reroute unsafe replies to reserve root content"
```

---

## Task 7: Make review scoring execution-aware

Objective: stop approving actions based only on content quality when platform execution risk is high.

Files:
- Modify: `ops/cmo-automation/scripts/review_engagement_queue.py`
- Modify: `ops/cmo-automation/reports/CMO-CUTOVER-48H-RUNBOOK.md`

Changes:
- Add new review dimensions:
  - execution reliability risk
  - recent failure rate by account and action type
  - reserve-root capacity available
- Lower approval confidence when recent reply execution success rate is below threshold
- Change `global_recommendation` semantics to distinguish:
  - `content_ready_assisted`
  - `root_only_live`
  - `manual_review_only`
  - `hold`

Verification:
- review markdown includes execution-aware recommendation language
- known poor reply modes reduce live recommendation severity

Commit:
```bash
git -C ~/cDesign/sovren-website add ops/cmo-automation/scripts/review_engagement_queue.py ops/cmo-automation/reports/CMO-CUTOVER-48H-RUNBOOK.md
git -C ~/cDesign/sovren-website commit -m "feat(cmo): make review recommendations execution-aware"
```

---

## Task 8: Add per-account execution isolation

Objective: reduce the chance of cross-account misrouting and prepare for cleaner live execution.

Files:
- Modify: `ops/cmo-automation/config/cmo_accounts.yaml`
- Modify: `ops/cmo-automation/scripts/execute_approved_queue.py`
- Modify: `ops/cmo-automation/README.md`

Changes:
- Add account-specific execution metadata in `cmo_accounts.yaml`
  - account handle
  - auth profile name or env prefix
  - live-enabled boolean
- Update executor to read account metadata and emit it in reports even if the underlying auth strategy remains shared for now
- Add a hard guard: live execution must refuse any account not marked `live_enabled: true`

Suggested YAML fragment:
```yaml
accounts:
  - handle: TheCesarCross
    role: founder
    live_enabled: true
    auth_profile: founder
```

Verification:
- execution report includes account profile metadata
- live mode blocks accounts without explicit enablement

Commit:
```bash
git -C ~/cDesign/sovren-website add ops/cmo-automation/config/cmo_accounts.yaml ops/cmo-automation/scripts/execute_approved_queue.py ops/cmo-automation/README.md
git -C ~/cDesign/sovren-website commit -m "feat(cmo): add per-account live execution guards"
```

---

## Task 9: Add an operator runbook for safe daily use

Objective: make the improved system operable without re-deriving policy from code.

Files:
- Create: `ops/cmo-automation/reports/CMO-DAILY-OPERATIONS-RUNBOOK.md`
- Modify: `ops/cmo-automation/README.md`

Sections to include:
- dry-run cycle
- assisted-review cycle
- root-only live cycle
- what to do when reply preflight is unknown
- what to do when live failures spike
- which artifacts to inspect first

Minimum checklist:
1. run collection and analysis
2. generate queue
3. review queue
4. hydrate queue
5. inspect preflight summary
6. if reply live-readiness is weak, run root-only live mode
7. generate telemetry summary after run

Commit:
```bash
git -C ~/cDesign/sovren-website add ops/cmo-automation/reports/CMO-DAILY-OPERATIONS-RUNBOOK.md ops/cmo-automation/README.md
git -C ~/cDesign/sovren-website commit -m "docs(cmo): add daily operations runbook"
```

---

## Task 10: Verification pass across the full pipeline

Objective: prove the upgrade changes behavior in the intended direction.

Files:
- No code changes required unless bugs are found

Run:
```bash
cd ~/cDesign/sovren-website/ops/cmo-automation && \
python3 -m unittest tests/test_hydrate_approved_queue.py tests/test_execute_approved_queue.py -v && \
python3 scripts/build_internal_signal_digest.py && \
python3 scripts/generate_engagement_queue.py && \
python3 scripts/review_engagement_queue.py && \
python3 scripts/hydrate_approved_queue.py && \
python3 scripts/execute_approved_queue.py --input reports/cmo-hydrated-queue.json && \
python3 scripts/summarize_execution_telemetry.py
```

Expected outcomes:
- tests pass
- hydrated queue distinguishes content-ready from live-ready
- execution report contains rerouted/manual-review items instead of burning all weak replies
- telemetry summary exposes failure categories cleanly
- root-post candidates are sourced from internal signals, not only generic templates

---

## Success criteria

The upgrade is successful when:
- known-weak reply actions are blocked or rerouted before live failure
- root-post throughput increases using internal product signals
- execution reports distinguish `hydrated`, `live_ready`, `manual_review`, `rerouted`, `executed`, and `failed`
- telemetry shows a meaningful drop in avoidable live failures
- operators can choose `root-only live` as a first-class mode

---

## Recommended execution order for maximum impact

Do these first:
1. Task 2 — preflight in hydration
2. Task 3 — executor fallback behavior
3. Task 4 — telemetry normalization
4. Task 5 — internal-signal root posts
5. Task 6 — reserve root-post fallback

Do these second:
6. Task 7 — execution-aware review
7. Task 8 — per-account execution isolation
8. Task 9 — operator runbook

---

## One-week target state

By the end of the first upgrade week, the system should behave like this:
- root posts: source-backed, reliable, and live-capable
- replies: quality-gated and execution-aware, with manual-review or reroute fallback when uncertain
- reports: useful enough to adapt the next run automatically
- operator choice: explicit modes instead of accidental all-or-nothing live execution
