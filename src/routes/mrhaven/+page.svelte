<svelte:head>
  <title>Mr. Haven — Non-Custodial USDC Time Vault on Base L2 | Sovren Software</title>
  <meta name="description" content="Programmable non-custodial USDC vault on Base L2. Set conditions, name beneficiaries, designate autonomous agents. No custodian. No intermediary. Live on mainnet." />
  <meta property="og:title" content="Mr. Haven — Your Assets. Your Rules." />
  <meta property="og:description" content="Programmable asset control for humans and autonomous agents. Your keys, your conditions, your beneficiaries. Smart contract only. SDK coming soon." />
  <meta property="og:url" content="https://sovren.software/mrhaven" />
</svelte:head>

<script>
  const pillars = [
    {
      num: '01',
      label: 'LOCK IT. SET THE RULES.',
      desc: 'Deposit USDC into a smart contract. Set a time-based schedule, an unlock date, or a recurring release. The contract enforces the rules — no humans in the loop, no approval required.',
    },
    {
      num: '02',
      label: 'IF YOU GO DARK, IT STILL EXECUTES.',
      desc: 'Set an inactivity threshold: if you go offline for X days, funds transfer automatically. An on-chain dead man\'s switch for the assets that matter most.',
    },
    {
      num: '03',
      label: 'BUILT FOR AGENTS, NOT JUST HUMANS.',
      desc: 'Autonomous agents can hold funds, trigger transfers, and execute plans with the same non-custodial guarantees as any human user. No API key. No service account. The contract enforces the rules regardless of who calls it.',
    },
    {
      num: '04',
      label: 'SDK — COMING SOON.',
      desc: 'A developer SDK for integrating MrHaven vaults directly into applications and autonomous agent workflows. Programmatic vault creation, condition setting, and beneficiary management without touching the UI.',
    },
  ]
</script>

<main>
  <section class="hero">
    <div class="hero-inner">
      <span class="category">03 / FINANCE</span>
      <h1>MR.<br />HAVEN.</h1>
      <p class="status">Live on Base L2</p>
      <p class="tagline">Programmable asset control for humans and autonomous agents. No custodian, no intermediary, no exceptions.</p>
    </div>
  </section>

  <section class="overview">
    <div class="overview-inner">
      <div class="overview-text">
        <p class="overview-lead">Your assets. Your rules. No one else in the room.</p>
        <p class="overview-body">Traditional financial institutions hold your assets on your behalf. They decide when you can access them, who can receive them, and under what conditions. MrHaven removes them from the equation entirely.</p>
        <p class="overview-body">Deployed on Base L2, MrHaven is a set of auditable smart contracts. Deposit USDC, define conditions, name beneficiaries — or designate autonomous agents as authorized recipients. The contract handles execution: autonomously, verifiably, permanently.</p>
        <p class="overview-stack">Integrates with Augmentum OS as part of the Sovren Stack — programmable finance at the OS level.</p>
      </div>
      <div class="overview-specs">
        <div class="spec-row">
          <span class="spec-label">CHAIN</span>
          <span class="spec-value">Base L2 (Coinbase)</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">ASSET</span>
          <span class="spec-value">USDC</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">CUSTODY</span>
          <span class="spec-value">Non-custodial</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">CONTRACT</span>
          <span class="spec-value">Auditable · Open</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">SDK</span>
          <span class="spec-value spec-soon">Coming soon</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">STATUS</span>
          <span class="spec-value">Live · Mainnet</span>
        </div>
      </div>
    </div>
  </section>

  <section class="pillars">
    <div class="pillars-inner">
      <span class="section-label">HOW IT WORKS</span>
      <div class="pillar-rows">
        {#each pillars as p}
          <div class="pillar-row">
            <div class="pillar-left">
              <span class="pillar-num">{p.num}</span>
              <h3 class="pillar-title">{p.label}</h3>
            </div>
            <p class="pillar-desc">{p.desc}</p>
          </div>
        {/each}
      </div>
    </div>
  </section>

  <section class="cta">
    <div class="cta-inner">
      <h2>YOUR ASSETS.<br />YOUR RULES.</h2>
      <p>MrHaven is live on Base mainnet. Connect a wallet and set up your first vault in minutes.</p>
      <a href="https://mrhaven.io" target="_blank" rel="noreferrer" class="btn-primary">
        LAUNCH APP →
      </a>
    </div>
  </section>
</main>

<style>
  /* ── Hero ── */
  .hero {
    min-height: calc(100vh - 60px);
    display: flex;
    align-items: flex-end;
    padding: 5rem 2.5rem;
    border-bottom: 1px solid var(--border);
  }

  .hero-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    width: 100%;
  }

  .category {
    display: block;
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    color: var(--text-muted);
    margin-bottom: 1.75rem;
    text-transform: uppercase;
  }

  h1 {
    font-size: clamp(5rem, 18vw, 12rem);
    font-weight: 700;
    letter-spacing: 0.06em;
    line-height: 0.9;
    margin-bottom: 2rem;
  }

  .status {
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    color: var(--text-muted);
    text-transform: uppercase;
    margin-bottom: 1.5rem;
  }

  .tagline {
    font-size: clamp(0.95rem, 2vw, 1.1rem);
    color: var(--text-secondary);
    max-width: 600px;
    line-height: 1.65;
    letter-spacing: 0.02em;
  }

  /* ── Overview ── */
  .overview {
    background: #ffffff;
    color: #000;
    padding: 6rem 2.5rem;
    border-bottom: 1px solid #e5e5e5;
  }

  .overview-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6rem;
    align-items: start;
  }

  .overview-text {
    display: flex;
    flex-direction: column;
    gap: 1.75rem;
  }

  .overview-lead {
    font-size: clamp(1.3rem, 2.5vw, 1.7rem);
    font-weight: 700;
    letter-spacing: 0.04em;
    line-height: 1.2;
    color: #000;
  }

  .overview-body {
    font-size: 0.9rem;
    line-height: 1.85;
    color: #333;
    letter-spacing: 0.02em;
  }

  .overview-stack {
    font-size: 0.75rem;
    line-height: 1.7;
    color: #999;
    letter-spacing: 0.04em;
    padding-top: 0.25rem;
    border-top: 1px solid #e5e5e5;
  }

  .overview-specs {
    display: flex;
    flex-direction: column;
    border: 1px solid #e5e5e5;
  }

  .spec-row {
    display: flex;
    justify-content: space-between;
    padding: 0.85rem 1.25rem;
    border-bottom: 1px solid #e5e5e5;
    font-size: 0.72rem;
    letter-spacing: 0.1em;
  }

  .spec-row:last-child {
    border-bottom: none;
  }

  .spec-label {
    color: #999;
  }

  .spec-value {
    color: #111;
    text-align: right;
  }

  .spec-soon {
    color: #888;
  }

  /* ── Pillars ── */
  .pillars {
    padding: 6rem 2.5rem;
  }

  .pillars-inner {
    max-width: var(--max-w);
    margin: 0 auto;
  }

  .section-label {
    display: block;
    font-size: 0.62rem;
    letter-spacing: 0.2em;
    color: var(--text-muted);
    margin-bottom: 3rem;
    text-transform: uppercase;
  }

  .pillar-rows {
    display: flex;
    flex-direction: column;
    border-top: 1px solid var(--border);
  }

  .pillar-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    padding: 3rem 0;
    border-bottom: 1px solid var(--border);
    align-items: start;
  }

  .pillar-left {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .pillar-num {
    font-size: 0.62rem;
    letter-spacing: 0.2em;
    color: var(--text-muted);
  }

  .pillar-title {
    font-size: clamp(0.95rem, 1.5vw, 1.15rem);
    font-weight: 700;
    letter-spacing: 0.1em;
    color: var(--text-primary);
    line-height: 1.3;
    text-transform: uppercase;
    margin: 0;
  }

  .pillar-desc {
    font-size: 0.875rem;
    color: var(--text-secondary);
    line-height: 1.8;
    letter-spacing: 0.02em;
    padding-top: 0.25rem;
  }

  /* ── CTA ── */
  .cta {
    background: #fff;
    color: #000;
    padding: 6rem 2.5rem;
    border-top: 1px solid #e5e5e5;
  }

  .cta-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }

  .cta h2 {
    font-size: clamp(2rem, 5vw, 4rem);
    font-weight: 700;
    letter-spacing: 0.08em;
    line-height: 1.05;
  }

  .cta p {
    font-size: 0.875rem;
    color: #555;
    max-width: 480px;
    line-height: 1.7;
    letter-spacing: 0.02em;
  }

  .btn-primary {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    padding: 0.85rem 1.75rem;
    background: #000;
    color: #fff;
    text-decoration: none;
    transition: opacity 0.15s;
    align-self: flex-start;
    margin-top: 0.5rem;
  }

  .btn-primary:hover {
    opacity: 0.75;
  }

  /* ── Responsive ── */
  @media (max-width: 768px) {
    .hero {
      padding: 3rem 1.5rem 4rem;
    }

    h1 {
      font-size: clamp(4rem, 22vw, 7rem);
    }

    .overview-inner {
      grid-template-columns: 1fr;
      gap: 3rem;
    }

    .pillar-row {
      grid-template-columns: 1fr;
      gap: 1.5rem;
      padding: 2rem 0;
    }
  }
</style>
