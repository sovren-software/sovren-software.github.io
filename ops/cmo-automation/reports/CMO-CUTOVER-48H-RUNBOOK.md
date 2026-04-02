# CMO 48-Hour Cutover Runbook (No-Pause)

Objective
- Stop Fiverr after a 48-hour overlap window and maintain uninterrupted engagement cadence with in-house automation.

Decisions captured
- Overlap: 48h
- Volume: 80% of Fiverr volume, higher quality
- Primary KPI: qualified audience growth
- Automation: hybrid-autonomous, including founder account
- Targeting: 80% whitelist core + 20% discovery
- Founder policy: strict deny-list (no unrelated consumer-brand/meme/politics/price-gambling engagement)
- Fallback on failures/rate-limits/platform eligibility failures: root posts only

## T-48h (start now)
1) Run full pipeline and verify outputs:
   - collect_x_data.py
   - analyze_x_cmo.py
   - generate_engagement_queue.py
   - review_engagement_queue.py
   - reconstruct_fiverr_playbook.py
2) Ensure global recommendation is not "hold".
3) Keep Fiverr active during overlap.
4) Record baseline metrics snapshot for all 3 accounts.

## T-24h
1) Re-run pipeline.
2) Compare quality vs prior cycle:
   - short-generic reply share
   - per-account avg impressions
   - approved action counts
3) If any account degrades materially, throttle replies for that account and keep roots active.

## T-0h (Fiverr off)
1) Disable Fiverr service.
2) Keep in-house automation active with current caps.
3) Run execution preflight:
   - verify no hashtag/link violations
   - verify no duplicate targets/reply patterns
   - verify quote eligibility assumptions for candidate targets
4) Post-hoc audit sample (minimum 20% of sent actions).

## T+24h and T+48h
1) Rebuild playbook report and trend deltas.
2) If founder account drifts from strategy, tighten founder scope to whitelist-only for next cycle.
3) If rate limits trigger, switch to root-only fallback for affected cycle.

## Exit criteria (first 30 days)
- Qualified follower growth >= 8%
- Median engagement per post lift >= 25%
- Short-generic reply share <= 30%

## Failure criteria
- Repeated unrelated founder engagements
- Sustained decline in median impressions over 3+ cycles
- High rejection rate from review gate due low relevance

## Owner checklist
- [ ] Fiverr cancellation timestamp recorded
- [ ] Cron status healthy
- [ ] Review gate report reviewed each cycle
- [ ] Weekly KPI review published
