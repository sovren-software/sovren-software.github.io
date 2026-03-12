<svelte:head>
  <title>Sovren Software — Sovereign Command Infrastructure</title>
  <meta name="description" content="Sovereign command infrastructure for the high-leverage operator. Esver OS, Visage, and Mr. Haven — compute, identity, and capital. UX, privacy, and security — none sacrificed." />
  <link rel="canonical" href="https://sovren.software/" />
  <meta property="og:title" content="Sovren Software — Sovereign Command Infrastructure" />
  <meta property="og:description" content="Sovereign command infrastructure for the high-leverage operator. Compute, identity, and capital — UX, privacy, and security without compromise." />
  <meta property="og:url" content="https://sovren.software/" />
  <meta name="twitter:title" content="Sovren Software — Sovereign Command Infrastructure" />
  <meta name="twitter:description" content="Sovereign command infrastructure for the high-leverage operator. Compute, identity, and capital — UX, privacy, and security without compromise." />
</svelte:head>

<script>
  const products = [
    {
      number: '01',
      category: 'OS',
      name: 'ESVER OS',
      href: '/esver',
      description: 'Voice-native command interface. Biometric-secured access. Local AI co-pilot. Declarative NixOS substrate. UX, privacy, and security — none sacrificed.',
    },
    {
      number: '02',
      category: 'IDENTITY',
      name: 'VISAGE',
      href: '/visage',
      description: 'Linux face authentication via PAM. ONNX inference runs entirely on-device — no cloud enrollment, no biometric database. Open source, MIT licensed.',
    },
    {
      number: '03',
      category: 'FINANCE',
      name: 'MR. HAVEN',
      href: '/mrhaven',
      description: 'Non-custodial USDC time vault on Base L2. Set conditions, name beneficiaries, define schedules — or designate autonomous agents as recipients. Smart contract executes regardless of who holds the keys.',
    },
  ]
</script>

<main>
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-copy">
        <h1 class="preserve-3d">THE SOVREN<br />STACK.</h1>
        <p class="hero-sub">Sovereign compute. Local identity. Programmable capital.</p>
      </div>
      <div class="scroll-hint">[ SCROLL TO EXPLORE ]</div>
    </div>
  </section>

  <section class="products" aria-labelledby="products-heading">
    <h2 id="products-heading" class="sr-only">Products</h2>
    <div class="product-grid">
      {#each products as p}
        <a href={p.href} class="product-card">
          <span class="product-label">{p.number} / {p.category}</span>
          <h3 class="product-name">{p.name}</h3>
          <p class="product-desc">{p.description}</p>
          <span class="product-cta">LEARN MORE →</span>
        </a>
      {/each}
    </div>
  </section>

  <section class="thesis">
    <div class="thesis-inner glitch-subtle preserve-3d">
      <h2 class="thesis-statement">
        Privacy is not a feature.<br />
        Security is not a tradeoff.<br />
        Sovereignty is the only<br />
        acceptable default.
      </h2>
      <div class="thesis-foot">
        <p>We build infrastructure for operators who refuse to rent their own stack. Sovereign compute, local identity, and programmable capital — UX, privacy, and security without compromise.</p>
        <a href="/ecosystem" class="btn-primary">READ THE MANIFESTO</a>
      </div>
    </div>
  </section>
</main>

<style>
  .hero {
    min-height: calc(100vh - var(--nav-h));
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
  }

  .hero-inner {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: var(--space-3xl);
    padding: var(--space-5xl) var(--space-2xl);
    z-index: 10;
  }

  h1 {
    font-size: var(--fs-hero);
    font-weight: var(--fw-bold);
    letter-spacing: var(--ls-wide);
    line-height: 1.0;
    color: var(--text-primary);
    text-transform: uppercase;
    text-shadow: none;
  }

  .hero-sub {
    font-size: 0.95rem;
    color: var(--text-secondary);
    letter-spacing: var(--ls-moderate);
    text-transform: uppercase;
    margin-top: var(--space-lg);
  }

  .scroll-hint {
    font-size: var(--fs-scroll-hint);
    letter-spacing: var(--ls-widest);
    color: var(--text-muted);
    position: absolute;
    bottom: var(--space-4xl);
  }

  /* Products */
  .products {
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    position: relative;
  }

  .product-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    max-width: var(--max-w);
    margin: 0 auto;
    position: relative;
    z-index: 10;
  }

  .product-card {
    padding: var(--space-4xl) var(--space-3xl);
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
    border-right: 1px solid var(--border);
    min-height: 400px;
    transition: background var(--transition-slow), border-color var(--transition-slow);
    text-decoration: none;
    background: transparent;
  }

  .product-card:last-child {
    border-right: none;
  }

  .product-card:hover {
    background: var(--surface);
    border-color: var(--border-glow);
  }

  .product-label {
    font-size: var(--fs-label);
    letter-spacing: var(--ls-wider);
    color: var(--text-muted);
    text-transform: uppercase;
    transition: color var(--transition-fast);
  }

  .product-name {
    font-size: clamp(1.4rem, 2.5vw, 1.9rem);
    font-weight: var(--fw-bold);
    letter-spacing: 0.14em;
    color: var(--text-primary);
    text-transform: uppercase;
    text-shadow: none;
    transition: text-shadow var(--transition-slow);
  }

  .product-card:hover .product-name {
    text-shadow: 0 0 20px var(--border-glow);
  }

  .product-desc {
    font-size: 0.82rem;
    color: var(--text-secondary);
    line-height: var(--lh-relaxed);
    flex: 1;
    letter-spacing: var(--ls-default);
  }

  .product-cta {
    font-size: var(--fs-label);
    letter-spacing: var(--ls-wider);
    color: var(--text-muted);
    transition: color var(--transition-fast);
    text-transform: uppercase;
  }

  .product-card:hover .product-cta,
  .product-card:hover .product-label {
    color: var(--text-primary);
  }

  /* Thesis */
  .thesis {
    background: transparent;
    color: var(--text-primary);
    padding: var(--pad-section-lg);
    position: relative;
    overflow: hidden;
  }

  .thesis::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at center, rgba(255,255,255,0.03) 0%, transparent 70%);
    pointer-events: none;
    z-index: -1;
  }

  .thesis-inner {
    max-width: var(--max-w);
    margin: 0 auto;
  }

  .thesis-statement {
    font-size: var(--fs-thesis);
    font-weight: var(--fw-bold);
    letter-spacing: var(--ls-tight);
    line-height: 1.25;
    margin-bottom: var(--space-5xl);
    text-shadow: 0 4px 20px rgba(0,0,0,0.5);
  }

  .thesis-foot {
    display: flex;
    align-items: center;
    gap: var(--space-5xl);
    flex-wrap: wrap;
  }

  .thesis-foot p {
    font-size: var(--fs-body-sm);
    line-height: var(--lh-relaxed);
    max-width: var(--max-w-body);
    color: var(--text-secondary);
    letter-spacing: var(--ls-default);
  }

  .sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
  }

  /* Responsive */
  @media (max-width: 768px) {
    .product-grid {
      grid-template-columns: 1fr;
    }

    .product-card {
      border-right: none;
      border-bottom: 1px solid var(--border);
      min-height: auto;
      padding: var(--space-2xl) var(--space-xl);
    }

    .product-card:last-child {
      border-bottom: none;
    }

    h1 {
      font-size: clamp(2.5rem, 14vw, 4rem);
    }

    .thesis {
      padding: var(--space-5xl) var(--space-xl);
    }

    .thesis-foot {
      flex-direction: column;
      gap: var(--space-2xl);
    }
  }
</style>
