<svelte:head>
  <title>Augmentum OS — Governance-First NixOS Operating System | Sovren Software</title>
  <meta name="description" content="An OS with a cognitive loop that learns your system — local inference, cryptographic receipts, consent that expires at reboot. Governance built into the substrate, not bolted on top." />
  <meta property="og:title" content="Augmentum OS — Stop Managing Your OS. Start Commanding It." />
  <meta property="og:description" content="Local intelligence at the OS layer. Governance built into the substrate. Actions that prove they executed. Ships Summer 2026." />
  <meta property="og:url" content="https://sovren.software/augmentum" />
</svelte:head>

<script>

  const features = [
    {
      label: 'COGNITIVE LOOP',
      desc: 'The OS observes system health, detects patterns, and surfaces recommendations — using local LLMs on your hardware, without your private data leaving your fleet. Every 5 minutes. Hourly trend analysis. This is not telemetry. It is a system that knows what it is doing.',
    },
    {
      label: 'GOVERNANCE IS STRUCTURAL',
      desc: 'Actions in the governance pipeline produce cryptographic receipts — hash-chained, Ed25519-signed, auditable. Every agent operates within explicitly defined capability bounds. Scoped, time-limited permits are required before any privileged operation proceeds.',
    },
    {
      label: 'CONSENT AS INFRASTRUCTURE',
      desc: 'Privacy controls are encoded as sentinel files on a RAM-only filesystem. They expire on reboot — requiring active re-authorization every time the system starts. The system asks to be trusted again rather than assuming it still is. Cryptographic erasure is available on demand.',
    },
    {
      label: 'SOVEREIGN IDENTITY',
      desc: 'Your Ethereum wallet signs your identity. No external identity provider. SSH key derives to age key derives to ETH address — a complete identity chain without trusting anyone else\'s infrastructure. One declarative config governs the entire fleet.',
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
        <p>Most operating systems host your programs and stay out of the way. Augmentum OS runs a persistent cognitive layer: it observes system health, detects trends, and surfaces recommendations — locally, without sending anything to a vendor. The system learns the longer it runs. This is a different category of machine.</p>
        <p>Governance is built into the substrate, not bolted on top. Every action in the pipeline produces a cryptographic receipt. Consent is encoded as sentinel files that expire on reboot — requiring active re-authorization every time the system starts. What the system knows about you, it can provably erase on command. A unified CLI puts diagnostics, privacy controls, authentication, AI health, and governance behind a single entry point.</p>
        <p>Augmentum OS is also the integration layer for the Sovren Stack. Visage face authentication runs as a hardware-verified identity primitive at the OS level. MrHaven vault access is a first-class credential. The three products are each useful alone — together they form a complete sovereign computing platform.</p>
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

  <section class="features">
    <div class="features-inner">
      <span class="section-label">ARCHITECTURE</span>
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
      <h2>BE NOTIFIED<br />AT LAUNCH.</h2>
      <p>Augmentum OS ships Summer 2026. No early access. No waitlist. Email us if you want a single notification the day it launches.</p>
      <a href="mailto:hello@sovren.software?subject=Augmentum OS Launch Notification" class="btn-primary">
        NOTIFY ME AT LAUNCH →
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

  .spec-upcoming {
    color: #888;
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

  .section-label {
    display: block;
    font-size: 0.62rem;
    letter-spacing: 0.2em;
    color: var(--text-muted);
    margin-bottom: 3rem;
    text-transform: uppercase;
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
      font-size: clamp(3rem, 16vw, 5rem);
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
  }
</style>
