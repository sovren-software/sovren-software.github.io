<svelte:head>
  <title>Augmentum OS — A Cognitive Operating System for High-Leverage Operators | Sovren Software</title>
  <meta name="description" content="One operator. Team-scale output. Augmentum OS is a cognitive operating system that watches, learns, and surfaces what matters — without compromising on privacy, security, or usability." />
  <meta property="og:title" content="Augmentum OS — One Operator. Team-Scale Output." />
  <meta property="og:description" content="A cognitive operating system for founders, operators, and high-leverage individuals. UX, privacy, and security — none sacrificed. Ships Summer 2026." />
  <meta property="og:url" content="https://sovren.software/augmentum" />
</svelte:head>

<script>
  const pillars = [
    {
      num: '01',
      label: 'ALWAYS WATCHING. NEVER LEAKING.',
      desc: 'The OS observes your system continuously and surfaces what matters — using AI that runs entirely on your hardware. Nothing leaves without your explicit permission. You control the privacy dial, and you can change it at any time.',
    },
    {
      num: '02',
      label: 'YOU OWN THE CONSENT',
      desc: 'Every AI feature is gated. You grant access. You revoke it. Session permissions expire when you reboot — so nothing persists without you actively choosing it. Before anything leaves your machine, the system tells you exactly what, and asks.',
    },
    {
      num: '03',
      label: 'EVERY ACTION IS RECEIPTED',
      desc: 'Agents operate within boundaries you define. Every action is logged, signed, and auditable. You can see what happened, when, and why. Control does not end when you delegate — it follows the work.',
    },
    {
      num: '04',
      label: 'SECURE BY DEFAULT. USABLE BY DESIGN.',
      desc: 'The secure path is the easy path. One command to check system status. One command to diagnose a problem. One command to change your privacy posture. Good defaults. No gotchas.',
    },
  ]
</script>

<main>
  <section class="hero">
    <div class="hero-inner">
      <span class="category">01 / OS</span>
      <h1>AUGMENTUM<br />OS.</h1>
      <p class="status">Ships Summer 2026</p>
      <p class="tagline">One operator. Team-scale output.</p>
    </div>
  </section>

  <section class="overview">
    <div class="overview-inner">
      <div class="overview-text">
        <p class="overview-lead">A cognitive operating system.</p>
        <p class="overview-body">Most operating systems make you choose: convenience or privacy. Ease of use or security. Augmentum OS does not accept that tradeoff.</p>
        <p class="overview-body">It is built for founders, operators, and high-leverage individuals who need the output of a team — without surrendering control of their own machine. The system watches, learns, and surfaces what matters. You decide what it sees, what it retains, and when it acts. That clarity compounds over time.</p>
        <p class="overview-stack">Visage face authentication and MrHaven programmable finance are first-class primitives at the OS level. The Sovren Stack runs as a unified command layer.</p>
      </div>
      <div class="overview-specs">
        <div class="spec-row">
          <span class="spec-label">BASE</span>
          <span class="spec-value">NixOS 25.05 (Warbler)</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">CONFIG</span>
          <span class="spec-value">Declarative · Version-controlled · Rollback-capable</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">INFERENCE</span>
          <span class="spec-value">Runs locally · Your data stays on your hardware</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">CONSENT</span>
          <span class="spec-value">Granular · Revocable · Expires on reboot</span>
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
      <h2>BUILT FOR THE<br />OPERATOR.</h2>
      <p>Augmentum OS ships Summer 2026. No early access. No waitlist. One email when it is ready — send us your address.</p>
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
