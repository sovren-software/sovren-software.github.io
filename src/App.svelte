<script>
  const products = [
    {
      name: 'Augmentum OS',
      url: 'https://augmentum.computer',
      tag: 'Ships Summer 2026',
      description:
        'A NixOS-based operating system for people who want to own their computing environment. Declarative system state, reproducible builds, AI-native services, hardware-verified trust.',
      status: 'upcoming',
    },
    {
      name: 'Visage',
      url: 'https://github.com/sovren-software/visage',
      tag: 'Open source · MIT',
      description:
        'Linux face authentication via PAM. Persistent daemon, IR camera support, ONNX inference — sub-second warm authentication. The Windows Hello equivalent that runs on real Linux hardware.',
      status: 'live',
    },
    {
      name: 'MrHaven',
      url: 'https://mrhaven.io',
      tag: 'Live on Base L2',
      description:
        'Non-custodial USDC time vault. Set a schedule or an inactivity threshold — funds reach your designated beneficiaries when conditions are met. No custodian. No intermediary.',
      status: 'live',
    },
  ]

  const roadmap = [
    { phase: 'Now', items: ['Visage v0.1.0 release', 'Sovren Software launch'] },
    { phase: 'Q2 2026', items: ['Augmentum OS beta', 'MrHaven Passport SDK'] },
    { phase: 'Summer 2026', items: ['Augmentum OS 1.0', 'Full ecosystem integration'] },
  ]
</script>

<nav>
  <div class="nav-inner">
    <span class="wordmark">Sovren Software</span>
    <div class="nav-links">
      <a href="#products">Products</a>
      <a href="#roadmap">Roadmap</a>
      <a href="https://github.com/sovren-software" target="_blank" rel="noreferrer">GitHub</a>
    </div>
  </div>
</nav>

<main>
  <!-- Hero -->
  <section class="hero">
    <p class="overline">Sovereign computing</p>
    <h1>Most software extracts value from users.<br />We build software that extends their capability.</h1>
    <p class="hero-sub">
      Your OS runs on someone else's update schedule.<br />
      Your biometrics are stored in someone else's database.<br />
      Your assets move through someone else's infrastructure.<br /><br />
      We build the alternative.
    </p>
    <div class="hero-cta">
      <a href="https://augmentum.computer" class="btn-primary" target="_blank" rel="noreferrer">Augmentum OS →</a>
      <a href="https://github.com/sovren-software/visage" class="btn-secondary" target="_blank" rel="noreferrer">Visage on GitHub</a>
    </div>
  </section>

  <!-- Products -->
  <section id="products" class="products">
    <h2 class="section-label">Products</h2>
    <div class="product-grid">
      {#each products as p}
        <a
          href={p.url}
          class="product-card"
          class:live={p.status === 'live'}
          class:upcoming={p.status === 'upcoming'}
          target="_blank"
          rel="noreferrer"
        >
          <div class="product-header">
            <span class="product-name">{p.name}</span>
            <span class="product-tag">{p.tag}</span>
          </div>
          <p class="product-desc">{p.description}</p>
          <span class="product-link">Visit →</span>
        </a>
      {/each}
    </div>
  </section>

  <!-- Why -->
  <section class="why">
    <h2 class="section-label">Why sovereign computing</h2>
    <div class="pillars">
      <div class="pillar">
        <h3>Computing</h3>
        <p>Your OS should execute your intent, not someone else's update policy. Augmentum OS gives you a declarative, reproducible system — your exact configuration, every time.</p>
      </div>
      <div class="pillar">
        <h3>Identity</h3>
        <p>Biometric data belongs to you, processed locally on your hardware. Visage runs face authentication entirely on-device — no cloud enrollment, no external database.</p>
      </div>
      <div class="pillar">
        <h3>Assets</h3>
        <p>Financial infrastructure should be programmable without a custodian. MrHaven automates value transfer on-chain — your keys, your rules, your beneficiaries.</p>
      </div>
    </div>
  </section>

  <!-- Roadmap -->
  <section id="roadmap" class="roadmap">
    <h2 class="section-label">Roadmap</h2>
    <div class="timeline">
      {#each roadmap as r, i}
        <div class="timeline-item">
          <div class="timeline-phase">{r.phase}</div>
          <ul class="timeline-items">
            {#each r.items as item}
              <li>{item}</li>
            {/each}
          </ul>
          {#if i < roadmap.length - 1}
            <div class="timeline-connector" aria-hidden="true"></div>
          {/if}
        </div>
      {/each}
    </div>
  </section>
</main>

<footer>
  <div class="footer-inner">
    <span class="wordmark-sm">Sovren Software</span>
    <div class="footer-links">
      <a href="https://sovren.software">sovren.software</a>
      <a href="https://github.com/sovren-software" target="_blank" rel="noreferrer">GitHub</a>
      <a href="https://augmentum.computer" target="_blank" rel="noreferrer">Augmentum OS</a>
      <a href="https://mrhaven.io" target="_blank" rel="noreferrer">MrHaven</a>
    </div>
  </div>
</footer>

<style>
  /* ─── Nav ─── */
  nav {
    position: sticky;
    top: 0;
    z-index: 10;
    background: rgba(10, 10, 10, 0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border);
  }

  .nav-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    padding: 0 2rem;
    height: 56px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .wordmark {
    font-size: 0.9rem;
    font-weight: 500;
    letter-spacing: 0.02em;
    color: var(--text-primary);
  }

  .nav-links {
    display: flex;
    gap: 2rem;
    font-size: 0.85rem;
    color: var(--text-secondary);
  }

  .nav-links a:hover {
    color: var(--text-primary);
  }

  /* ─── Main ─── */
  main {
    max-width: var(--max-w);
    margin: 0 auto;
    padding: 0 2rem;
  }

  /* ─── Hero ─── */
  .hero {
    padding: 7rem 0 5rem;
    max-width: 680px;
  }

  .overline {
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 1.25rem;
  }

  h1 {
    font-size: clamp(1.75rem, 4vw, 2.5rem);
    font-weight: 600;
    line-height: 1.25;
    letter-spacing: -0.02em;
    color: var(--text-primary);
    margin-bottom: 1.5rem;
  }

  .hero-sub {
    font-size: 1rem;
    color: var(--text-secondary);
    line-height: 1.7;
    margin-bottom: 2.5rem;
  }

  .hero-cta {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
  }

  .btn-primary {
    display: inline-block;
    padding: 0.6rem 1.25rem;
    background: var(--text-primary);
    color: var(--bg);
    font-size: 0.875rem;
    font-weight: 500;
    border-radius: 4px;
    transition: opacity 0.15s;
  }

  .btn-primary:hover {
    opacity: 0.85;
    color: var(--bg);
  }

  .btn-secondary {
    display: inline-block;
    padding: 0.6rem 1.25rem;
    border: 1px solid var(--border);
    color: var(--text-secondary);
    font-size: 0.875rem;
    font-weight: 500;
    border-radius: 4px;
    transition: border-color 0.15s, color 0.15s;
  }

  .btn-secondary:hover {
    border-color: var(--text-muted);
    color: var(--text-primary);
  }

  /* ─── Section labels ─── */
  .section-label {
    font-size: 0.7rem;
    font-weight: 500;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 2rem;
  }

  /* ─── Products ─── */
  .products {
    padding: 4rem 0;
    border-top: 1px solid var(--border);
  }

  .product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1px;
    background: var(--border);
    border: 1px solid var(--border);
    border-radius: 6px;
    overflow: hidden;
  }

  .product-card {
    background: var(--surface);
    padding: 1.75rem;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    transition: background 0.15s;
    cursor: pointer;
  }

  .product-card:hover {
    background: var(--surface-2);
  }

  .product-header {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 0.75rem;
  }

  .product-name {
    font-size: 1rem;
    font-weight: 600;
    color: var(--text-primary);
  }

  .product-tag {
    font-size: 0.7rem;
    color: var(--text-muted);
    white-space: nowrap;
  }

  .product-card.live .product-tag {
    color: var(--text-secondary);
  }

  .product-desc {
    font-size: 0.875rem;
    color: var(--text-secondary);
    line-height: 1.6;
    flex: 1;
  }

  .product-link {
    font-size: 0.8rem;
    color: var(--text-muted);
    margin-top: 0.25rem;
    transition: color 0.15s;
  }

  .product-card:hover .product-link {
    color: var(--text-secondary);
  }

  /* ─── Why ─── */
  .why {
    padding: 4rem 0;
    border-top: 1px solid var(--border);
  }

  .pillars {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 2.5rem;
  }

  .pillar h3 {
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 0.75rem;
    color: var(--text-primary);
  }

  .pillar p {
    font-size: 0.875rem;
    color: var(--text-secondary);
    line-height: 1.7;
  }

  /* ─── Roadmap ─── */
  .roadmap {
    padding: 4rem 0;
    border-top: 1px solid var(--border);
  }

  .timeline {
    display: flex;
    gap: 0;
  }

  .timeline-item {
    flex: 1;
    position: relative;
    padding-right: 2rem;
  }

  .timeline-phase {
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    color: var(--text-muted);
    margin-bottom: 0.75rem;
    text-transform: uppercase;
  }

  .timeline-items {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
  }

  .timeline-items li {
    font-size: 0.875rem;
    color: var(--text-secondary);
    padding-left: 0.75rem;
    border-left: 1px solid var(--border);
  }

  .timeline-connector {
    position: absolute;
    top: 0.55rem;
    right: 0;
    width: 2rem;
    height: 1px;
    background: var(--border);
  }

  /* ─── Footer ─── */
  footer {
    border-top: 1px solid var(--border);
    margin-top: 4rem;
  }

  .footer-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    padding: 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
  }

  .wordmark-sm {
    font-size: 0.8rem;
    font-weight: 500;
    color: var(--text-muted);
  }

  .footer-links {
    display: flex;
    gap: 1.5rem;
    font-size: 0.8rem;
    color: var(--text-muted);
  }

  .footer-links a:hover {
    color: var(--text-secondary);
  }

  /* ─── Responsive ─── */
  @media (max-width: 640px) {
    .hero {
      padding: 4rem 0 3rem;
    }

    h1 {
      font-size: 1.6rem;
    }

    .timeline {
      flex-direction: column;
      gap: 2rem;
    }

    .timeline-connector {
      display: none;
    }

    .timeline-item {
      padding-right: 0;
    }

    .footer-inner {
      flex-direction: column;
      align-items: flex-start;
    }
  }
</style>
