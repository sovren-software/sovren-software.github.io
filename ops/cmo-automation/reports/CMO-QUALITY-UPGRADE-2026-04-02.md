# CMO Quality Upgrade — Decisions and Completion Notes

Date: 2026-04-02
Scope: X CMO automation quality and policy hardening
Status: Upgrade implemented with documented platform constraint

## Summary
This upgrade moved the pipeline from generic high-volume engagement behavior to strict quality-gated engagement with policy-enforced copy constraints and duplicate prevention.

Implemented outcomes:
- No hashtags in generated copy
- No links in replies
- No duplicated reply text patterns in a run
- No duplicate target tweet IDs in a run
- Context-specific reply requirement with low-signal filtering
- Mission-aligned relevance gate in policy

Latest dry-run before live:
- 18 approved actions
- 16 hydrated and ready
- 2 blocked (low_signal_source or duplicate_target_tweet)
- 0 hashtag violations, 0 link violations, 0 duplicate reply patterns

Live execution result:
- 3 root posts executed successfully
- Most quote-style replies failed with X API 403 due conversation/mention restriction

## Decisions made

### D1. Enforce hard copy constraints at policy + generator layer
Decision:
- Added policy flags for no hashtags, no links in replies, and unique contextual replies.
- Enforced these during hydration, not just review.

Rationale:
- Guarantees style consistency even if queue inputs vary.
- Prevents low-quality copy from reaching execution stage.

Trade-offs:
- Fewer candidate actions survive gating.
- More blocked actions in noisy cycles.

Expected benefits:
- Higher output quality floor.
- Lower reputational risk from spam-like formatting.

### D2. Deduplicate both content and targets
Decision:
- Blocked duplicate target tweet IDs and duplicate reply text patterns within a run.

Rationale:
- Repetition is visible and degrades account quality perception.

Trade-offs:
- Reduced throughput when candidate pools are narrow.

Expected benefits:
- Distinct engagement footprint.
- Better perceived intent and originality.

### D3. Add context-specificity gate and low-signal filter
Decision:
- Reply generation requires either recognizable topic signal or meaningful source anchor.
- Low-signal content (giveaway/airdrop-like noise) is blocked.

Rationale:
- Generic responses were the primary failure mode.

Trade-offs:
- Higher block rate on weak timelines.

Expected benefits:
- Replies are more defensible and relevant.
- Better alignment with founder and brand voice requirements.

### D4. Keep quote-workaround execution path, document platform constraint
Decision:
- Retained quote execution mode where direct reply constraints apply.
- Documented X API restriction observed during live run.

Rationale:
- Maintains one executable path while policy and quality gates improve.

Trade-offs:
- Quote eligibility depends on conversation relationship and can fail at runtime.

Expected benefits:
- Immediate operability for eligible targets.
- Clear visibility into where platform constraints block execution.

## Drawbacks and known limitations
- X platform restriction: quote attempts can fail with HTTP 403 when account is not mentioned or in-thread.
- Current pipeline does not preflight quote eligibility before live execution.
- Some context anchors are concise and can still read mechanically in edge cases.
- Candidate discovery quality depends on `x-cli tweet search` result quality and available context.

## Remaining work to fully complete upgrade
1) Add quote eligibility preflight
- Before execution, verify target is quote-eligible for the posting account.
- Auto-skip or reroute ineligible targets.

2) Add fallback action strategy per failed reply
- If quote ineligible, either:
  - switch to root-post reserve queue, or
  - store as manual-review candidate.

3) Add stronger context semantic scoring
- Replace lightweight heuristics with a richer contextual scorer.
- Require topic + claim + value-add structure.

4) Add per-account command routing/auth isolation
- Ensure execution uses correct account credentials/session context for each action.

5) Add post-execution telemetry loop
- Track executed vs failed by reason and adapt candidate selection weights.

## Files changed in this upgrade window
- config/operating_policy.json
- scripts/hydrate_approved_queue.py
- reports/CMO-ECOSYSTEM-MARKETING-BRIEF.md
- reports/cmo-hydrated-queue.json
- reports/cmo-hydrated-queue.md
- reports/cmo-execution-report.json
- reports/cmo-execution-report.md

## Recommended next checkpoint
- Implement quote eligibility preflight and fallback routing, then rerun live with target success threshold >= 80% for ready actions.
