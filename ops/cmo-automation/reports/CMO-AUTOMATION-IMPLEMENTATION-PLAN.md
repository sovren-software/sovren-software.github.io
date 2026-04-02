# Automated CMO Function — Implementation Plan (Three X Accounts)

Goal
- Replace outsourced Fiverr engagement with an in-house, measurable, low-risk automation system that coordinates:
  - @TheCesarCross (founder)
  - @sovren_software (brand)
  - @mrhaven_agent (product agent)

Current baseline (from latest captured sample)
- @TheCesarCross: 7/7 posts are replies, short-reply ratio 0.714, avg impressions 3.43
- @sovren_software: 8/8 posts are replies, short-reply ratio 0.875, avg impressions 6.25
- @mrhaven_agent: 8/8 posts are root posts, avg impressions 5.62
- Pattern observed in outsourced-style behavior: high-volume short replies, broad low-overlap targeting, weak engagement yield.

Interpretation
- The current engagement mode is over-indexed on low-context reactive replies.
- Root narrative production is underrepresented on founder + brand accounts in sampled window.
- This aligns with low return on outsourced spend.

---

## Phase 1 — Instrumentation + Baseline Lock (now)

Implemented
- Collector: scripts/collect_x_data.py
- Analyzer: scripts/analyze_x_cmo.py
- Action queue generator: scripts/generate_engagement_queue.py
- Config: config/cmo_accounts.yaml

Output artifacts
- data/latest.json
- reports/cmo-analysis.json
- reports/cmo-analysis.md
- data/engagement-queue.json

Operating command
- cd ~/cDesign/sovren-website/ops/cmo-automation
- source ~/.claude/secrets.env
- export CMO_TIMELINE_MAX=20
- python3 scripts/collect_x_data.py
- python3 scripts/analyze_x_cmo.py
- python3 scripts/generate_engagement_queue.py

---

## Phase 2 — Reconstruct Fiverr Playbook (1–2 days)

Method
1) Pull daily snapshots for 14 days.
2) Tag candidate outsourced actions with heuristics:
   - starts with @
   - <= 90 chars
   - generic opener patterns
   - low dwell (burst cadence)
3) Split output into:
   - worked: replies with above-median impressions/likes
   - failed: replies with 0 interaction and low impressions

Deliverables
- reports/fiverr-playbook-reconstruction.md
- reports/fiverr-pattern-confusion-matrix.json

Decision gate
- If short reply ratio > 0.65 and avg likes < 0.5 on targeted accounts, cap automated replies and shift volume to root + quote strategy.

---

## Phase 3 — Improved Strategy Model (systematized)

Account strategy
1) Founder (@TheCesarCross)
- Primary: authority and framing
- Mix target: 35% root, 50% high-signal replies, 15% quotes
- Rule: no generic acknowledgements without differentiated opinion

2) Brand (@sovren_software)
- Primary: thesis + product context
- Mix target: 45% root, 40% contextual replies, 15% quotes
- Rule: every reply should ladder to sovereignty thesis or product proof

3) Product (@mrhaven_agent)
- Primary: utility + proofs
- Mix target: 60% root utility posts, 25% proof/context replies, 15% quote amplification
- Rule: keep proof-linked clarity; avoid broad-topic drift

Cross-account orchestration rules
- Founder seeds perspective → brand codifies thesis → mrhaven_agent supplies proof/utility.
- No duplicate same-angle reply across two accounts within 12 hours.
- Daily coordination cap: 1 shared topic cluster/day.

---

## Phase 4 — Automation Execution Layer (safe automation)

Execution architecture
- Scheduler: cron (or GitHub Actions)
- Data: snapshot JSON + analysis report + queue JSON
- Executor modes:
  - dry-run (default): generate recommended actions only
  - assisted: human approves queued actions
  - auto-lite: post only pre-approved templates with strict limits

Risk controls
- per-account reply caps/hour
- 24h cooldown on same-user repeated replies
- random delay jitter
- require contextual relevance score before posting
- hard block list + topic deny list

Immediate policy change
- pause blind high-volume replying
- enforce minimum root-post floor each account/day
- route all auto actions through queue + review for first 2 weeks

---

## Phase 5 — KPI and Feedback Loop

North-star KPIs
- engagement per post by type (root/reply/quote)
- follower delta/week
- reply conversion rate (reply -> profile visit/follow)
- cross-account amplification uplift

Guardrail KPIs
- % low-signal replies (short generic) < 30%
- duplicate semantic replies/day < 10%
- actions rejected by reviewer (quality failure)

Weekly review output
- reports/weekly-cmo-review-YYYY-MM-DD.md
- includes: what changed, what worked, what to stop, next week experiments

---

## What to do next (execution order)

1) Start daily collection
- Run collector+analyzer twice daily for 14 days.

2) Add first automation gate
- Keep generate_engagement_queue.py in dry-run.
- Review queue manually and execute only approved actions.

3) Build reply-quality scorer
- Add lightweight semantic rubric:
  - specificity
  - thesis alignment
  - non-generic value add

4) Promote to auto-lite only after 2-week KPI check
- If KPIs improve and guardrails hold, allow bounded auto execution.

---

## Phase 6 — Quality Hardening Upgrade (completed 2026-04-02)

Implemented
- Policy-level constraints: no hashtags, no links in replies, unique contextual replies.
- Hydration-level enforcement for copy/style/duplication.
- Duplicate suppression across both target tweet IDs and reply text patterns.
- Context-specificity gate and low-signal source filtering.
- Mission alignment gate wired via operating policy + ecosystem brief.

Measured outcome (latest cycle)
- 18 approved actions
- 16 hydrated and ready after quality gating
- 2 blocked (low signal or duplicate target)
- 0 hashtag/link/duplicate violations in hydrated replies

Observed platform constraint
- Live quote-style engagement can fail with HTTP 403 when account is not mentioned or in-thread for the target post.

Status
- Baseline + quality-hardening scaffold is implemented under:
  ~/cDesign/sovren-website/ops/cmo-automation
- Upgrade details, decision log, limitations, and remaining work:
  reports/CMO-QUALITY-UPGRADE-2026-04-02.md
