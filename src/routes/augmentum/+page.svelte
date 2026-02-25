<svelte:head>
  <title>Augmentum OS — Governance-First NixOS Operating System | Sovren Software</title>
  <meta name="description" content="An OS with a cognitive loop that learns your system — local inference, cryptographic receipts, consent that expires at reboot. Governance built into the substrate, not bolted on top." />
  <meta property="og:title" content="Augmentum OS — Stop Managing Your OS. Start Commanding It." />
  <meta property="og:description" content="Local intelligence at the OS layer. Governance built into the substrate. Actions that prove they executed. Ships Summer 2026." />
  <meta property="og:url" content="https://sovren.software/augmentum" />
</svelte:head>

<script>
  const pillars = [
    {
      num: '01',
      label: 'COGNITIVE LOOP',
      desc: 'The OS observes system health every 5 minutes, detects patterns hourly, and surfaces recommendations — using local LLMs on your hardware, without your private data leaving your fleet.',
    },
    {
      num: '02',
      label: 'GOVERNANCE BY DESIGN',
      desc: 'Actions in the governance pipeline produce cryptographic receipts — hash-chained, Ed25519-signed, auditable. Every agent operates within explicitly defined, time-limited capability bounds.',
    },
    {
      num: '03',
      label: 'CONSENT AS INFRASTRUCTURE',
      desc: 'Privacy controls are encoded as sentinel files on a RAM-only filesystem. They expire on reboot — requiring active re-authorization every time the system starts.',
    },
    {
      num: '04',
      label: 'SOVEREIGN IDENTITY',
      desc: 'Your Ethereum wallet signs your identity. SSH key derives to age key derives to ETH address — a complete identity chain with no external provider.',
    },
  ]
</script>

<main>
  <section class="hero">
    <div class="hero-inner">
      <span class="category">01 / OS</span>
      <h1>AUGMENTUM<br />OS.</h1>
      <p class="status">Ships Summer 2026</p>
      <p class="tagline">Stop managing your OS. Start commanding it.</p>
    </div>
  </section>

  <section class="overview">
    <div class="overview-inner">
      <div class="overview-text">
        <p class="overview-lead">A different category of machine.</p>
        <p class="overview-body">Most operating systems host your programs and stay out of the way. Augmentum OS runs a persistent cognitive layer — observing system health, detecting trends, surfacing recommendations — locally, on your hardware, without your private data leaving your fleet. Governance is built into the substrate: every action receipted, every agent bounded, consent that expires at reboot.</p>
        <p class="overview-stack">Integration layer for the Sovren Stack — Visage face authentication and MrHaven vault access are first-class primitives at the OS level.</p>
      </div>
      <div class="overview-specs">
        <div class="spec-row">
          <span class="spec-label">BASE</span>
          <span class="spec-value">NixOS 25.05 (Warbler)</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">CONFIG</span>
          <span class="spec-value">Declarative · Git-tracked · 8 hosts</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">AI LAYER</span>
          <span class="spec-value">Local inference · Fleet-distributed</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">GOVERNANCE</span>
          <span class="spec-value">Cryptographic receipts · Consent-gated</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">STATUS</span>
          <span class="spec-value spec-upcoming">Ships Summer 2026</span>
        </div>
      </div>
    </div>
  </section>

  <section class="pillars">
    <div class="pillars-inner">
      <span class="section-label">ARCHITECTURE</span>
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
      <h2>BE NOTIFIED<br />AT LAUNCH.</h2>
      <p>Augmentum OS ships Summer 2026. No early access. No waitlist. Email us if you want a single notification the day it launches.</p>
      <a href="mailto:hello@sovren.software?subject=Augmentum OS Launch Notification" class="btn-primary">
        NOTIFY ME AT LAUNCH →
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
    font-size: clamp(4rem, 12vw, 9rem);
    font-weight: 700;
    letter-spacing: 0.06em;
    line-height: 0.95;
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

  .spec-upcoming {
    color: #888;
  }

  /* ── Architecture pillars ── */
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
      font-size: clamp(3rem, 16vw, 5rem);
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
