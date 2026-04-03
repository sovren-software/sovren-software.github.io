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

---

## Phase 7 — Account Restructure and Credential Migration (2026-04-03)

Context
- @mrhaven_agent suspended by X on 2026-04-02 for "inauthentic behaviors."
- Root causes: unverified bot-labeled account (no blue check, no delegated admin, 4 followers),
  13 consecutive HTTP 403 failures from quote attempts to conversations the account was not
  part of, coordinated API usage across 3 accounts sharing one developer app.
- The X Developer App was registered under @mrhaven_agent. Suspension revoked all API
  credentials (HTTP 401 on bearer-token read-only calls confirmed).
- @TheCesarCross and @sovren_software survived due to blue check verification and delegated
  admin access — protective factors @mrhaven_agent lacked.

Decisions

D1. Abandon @mrhaven_agent without appeal
- Rationale: account carried bot-labeled baggage, only 4 followers, no organic social graph.
  Appealing risks drawing further scrutiny to the coordinated account cluster.
  Product updates flow through @sovren_software instead.
- Trade-off: lose the handle and any residual SEO value. X Premium subscription requires
  manual cancellation (X does not auto-cancel on suspension).
- Expected benefit: clean break, no residual risk to surviving accounts.

D2. Register new X Developer App under @TheCesarCross
- Rationale: strongest account (verified, 974 followers, established). App owner gets
  simplest auth flow for self-posting.
- Trade-off: ties API infrastructure to the founder's personal account. If founder account
  is ever restricted, API access is lost again.
- Expected benefit: API app inherits the trust signals of the founder account.

D3. Per-account access tokens with unified app credentials
- Rationale: each account (@TheCesarCross, @sovren_software) gets its own OAuth access
  token pair. App-level credentials (API key, API secret, bearer token) are shared.
  This enables per-account credential routing in the execution layer.
- Trade-off: more credentials to manage (7 vars vs 5). Scripts need account-to-token mapping.
- Expected benefit: eliminates single-token-for-all-accounts pattern that contributed to
  coordinated behavior detection. Each account's posting is independently authenticated.

D4. Hybrid model — roots auto-scheduled, replies/quotes manual-review only
- Rationale: the 13 consecutive 403 failures on quote attempts were the primary trigger
  signal. Fully automated reply/quote posting is too risky. But the pipeline's candidate
  generation and hydration are still valuable for surfacing engagement opportunities.
  Human-in-the-loop on all engagement actions eliminates the automation detection risk
  while preserving reach.
- Trade-off: slower engagement cadence (manual review bottleneck). Founder must review
  cmo-hydrated-queue.md each cycle and run approved x-cli commands individually.
- Expected benefit: maintains engagement volume at human quality. The founder is the
  circuit breaker — no risk of automated 403 cascades or template-fingerprinted replies.
  Free tier API limits (1,500 writes/month, 10K reads/month) are sufficient.

Implemented changes
- secrets.env: removed dead mrhaven_agent credentials, added 7-variable per-account structure
  (X_API_KEY, X_API_SECRET, X_BEARER_TOKEN, X_FOUNDER_ACCESS_TOKEN, X_FOUNDER_ACCESS_SECRET,
  X_SOVREN_ACCESS_TOKEN, X_SOVREN_ACCESS_SECRET). Values empty pending new app creation.
- collect_x_data.py: removed mrhaven_agent from account list, simplified to bearer-only auth.
- execute_approved_queue.py: added ACCOUNT_TOKEN_MAP for per-account credential routing,
  set_account_tokens() called before each action execution.
- hydrate_approved_queue.py: simplified to bearer-only auth, removed mrhaven_agent queries.
- daily-post.js: updated to use X_SOVREN_ACCESS_TOKEN/SECRET for @sovren_software posting.
- daily-post.yml: GitHub Actions secrets updated to new variable names.
- cmo_accounts.yaml: removed mrhaven_agent entry.
- operating_policy.json: removed mrhaven_agent account strategy.
- CMO-ECOSYSTEM-MARKETING-BRIEF.md: removed mrhaven_agent messaging intent.
- CLAUDE.md: updated credential references.
- Tests: fixed pre-existing seen parameter bug, updated fixtures. 6/6 passing.

Drawbacks and known limitations
- The hydration layer still produces templated replies with "Specific to [keyword salad]"
  suffixes. This copy quality issue predates the restructure and needs a generator rewrite
  before reply automation could safely resume.
- No circuit breaker in execute_approved_queue.py — manual execution mitigates this, but
  if automated execution is ever re-enabled, the script should abort after N consecutive
  failures to avoid triggering platform detection.
- X Premium subscription on @mrhaven_agent must be cancelled manually (via App Store,
  Google Play, or X support depending on how it was purchased).

Completed items (verified 2026-04-03)
1. DONE: X Developer App created under @TheCesarCross (Read+Write, Production package)
2. DONE: All 9 credential values filled in ~/.engram/envrc/secrets/secrets.env
3. DONE: 4 GitHub Actions secrets set in sovren-software repo (X_API_KEY, X_API_SECRET,
   X_SOVREN_ACCESS_TOKEN, X_SOVREN_ACCESS_SECRET)
4. DONE: Both accounts verified via x-cli (TheCesarCross 985 followers, sovren_software 67)
5. DONE: Daily Thesis Post dry-run passed in GitHub Actions

Remaining work
1. Cancel @mrhaven_agent X Premium subscription
2. Fix "Specific to [keyword salad]" suffix in hydration generator — blocks reply quality
3. Add quote eligibility preflight check before including candidates in hydrated queue
