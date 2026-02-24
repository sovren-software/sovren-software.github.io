<svelte:head>
  <title>Mr. Haven — Non-Custodial USDC Time Vault on Base L2 | Sovren Software</title>
  <meta name="description" content="Programmable non-custodial USDC vault on Base L2. Set time-based schedules, inactivity triggers, and beneficiary designations. No intermediary. Live on mainnet." />
  <meta property="og:title" content="Mr. Haven — Non-Custodial USDC Time Vault on Base L2" />
  <meta property="og:description" content="Programmable asset control for humans and autonomous agents. Your keys, your conditions, your beneficiaries. Smart contract only." />
  <meta property="og:url" content="https://sovren.software/mrhaven" />
</svelte:head>

<script>

  const steps = [
    { n: '01', label: 'DEPOSIT', desc: 'Lock USDC into a smart contract. Set a time-based schedule or an inactivity threshold.' },
    { n: '02', label: 'DESIGNATE', desc: 'Name your beneficiaries and their share. Conditions are encoded in contract logic — not held by a custodian.' },
    { n: '03', label: 'RELEASE', desc: 'When conditions are met, funds transfer automatically on-chain. No intermediary. No approval required.' },
  ]

  const features = [
    {
      label: 'TIME VAULT',
      desc: 'Lock USDC for any duration. Set exact unlock timestamps or recurring release schedules. The contract enforces the rules — no humans in the loop.',
    },
    {
      label: 'INACTIVITY TRIGGER',
      desc: 'Set a threshold: if you go offline for X days, funds transfer. An on-chain dead man\'s switch for the assets that matter most.',
    },
    {
      label: 'BENEFICIARY DESIGNATIONS',
      desc: 'Designate multiple beneficiaries with percentage splits. Update designations anytime while funds are locked. Remove or replace beneficiaries until conditions are met.',
    },
    {
      label: 'AUTONOMOUS AGENTS',
      desc: 'Designed for both human and autonomous principals. AI agents can hold funds, trigger transfers, and execute plans with the same non-custodial guarantees as any human user. No API key. No service account. No trust required — the contract enforces the rules regardless of who calls it.',
    },
  ]
</script>

<main>
  <section class="hero">
    <div class="hero-inner">
      <span class="category">03 / FINANCE</span>
      <h1>MR.<br />HAVEN.</h1>
      <p class="status">Live on Base L2</p>
      <p class="tagline">Non-custodial USDC time vault on Base L2. Programmable asset control for humans and autonomous agents — no custodian, no intermediary, no exceptions.</p>
    </div>
  </section>

  <section class="overview">
    <div class="overview-inner">
      <div class="overview-text">
        <p>Traditional financial institutions hold your assets on your behalf. They decide when you can access them, who can receive them, and under what conditions. MrHaven removes them from the equation entirely.</p>
        <p>Deployed on Base L2, MrHaven is a set of auditable smart contracts. Deposit USDC, define conditions, name beneficiaries — or designate autonomous agents as authorized recipients. The contract handles execution — autonomously, verifiably, permanently.</p>
        <p>This matters for AI agents as much as for humans. Autonomous agents that manage capital need programmable infrastructure with no human approval bottleneck in the execution path. MrHaven is designed from the start for both human and autonomous principals — the protocol doesn't distinguish between who holds the keys.</p>
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
          <span class="spec-label">STATUS</span>
          <span class="spec-value spec-live">Live · Mainnet</span>
        </div>
      </div>
    </div>
  </section>

  <section class="how-it-works">
    <div class="how-inner">
      <span class="section-label">HOW IT WORKS</span>
      <div class="steps">
        {#each steps as s}
          <div class="step">
            <span class="step-n">{s.n}</span>
            <div class="step-body">
              <span class="step-label">{s.label}</span>
              <p class="step-desc">{s.desc}</p>
            </div>
          </div>
        {/each}
      </div>
    </div>
  </section>

  <section class="features">
    <div class="features-inner">
      <span class="section-label">CAPABILITIES</span>
      <div class="feature-grid">
        {#each features as f}
          <div class="feature-card">
            <span class="feature-label">{f.label}</span>
            <p class="feature-desc">{f.desc}</p>
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

  /* Overview */
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
    gap: 1.5rem;
  }

  .overview-text p {
    font-size: 0.9rem;
    line-height: 1.8;
    color: #333;
    letter-spacing: 0.02em;
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

  .spec-live {
    color: #111;
  }

  /* How it works */
  .how-it-works {
    background: #fff;
    color: #000;
    padding: 6rem 2.5rem;
    border-top: 1px solid #e5e5e5;
  }

  .how-inner {
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

  .steps {
    display: flex;
    flex-direction: column;
    border: 1px solid #e5e5e5;
  }

  .step {
    display: flex;
    gap: 3rem;
    padding: 2.5rem;
    border-bottom: 1px solid #e5e5e5;
    align-items: flex-start;
  }

  .step:last-child {
    border-bottom: none;
  }

  .step-n {
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    color: #bbb;
    flex-shrink: 0;
    padding-top: 0.15rem;
  }

  .step-body {
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
  }

  .step-label {
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    color: #111;
  }

  .step-desc {
    font-size: 0.875rem;
    color: #555;
    line-height: 1.7;
    letter-spacing: 0.02em;
  }

  /* Features */
  .features {
    padding: 6rem 2.5rem;
    border-top: 1px solid var(--border);
  }

  .features-inner {
    max-width: var(--max-w);
    margin: 0 auto;
  }

  .feature-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    border: 1px solid var(--border);
  }

  .feature-card {
    padding: 2.5rem;
    border-right: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .feature-card:nth-child(2n) {
    border-right: none;
  }

  .feature-card:nth-child(3),
  .feature-card:nth-child(4) {
    border-bottom: none;
  }

  .feature-label {
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    color: var(--text-muted);
    text-transform: uppercase;
  }

  .feature-desc {
    font-size: 0.85rem;
    color: var(--text-secondary);
    line-height: 1.75;
    letter-spacing: 0.02em;
  }

  /* CTA */
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

  /* Responsive */
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

    .feature-grid {
      grid-template-columns: 1fr;
    }

    .feature-card {
      border-right: none;
    }

    .feature-card:nth-child(3),
    .feature-card:nth-child(4) {
      border-bottom: 1px solid var(--border);
    }

    .feature-card:last-child {
      border-bottom: none;
    }

    .step {
      gap: 1.5rem;
    }
  }
</style>
