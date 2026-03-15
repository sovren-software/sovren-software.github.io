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
  import StackDiagram from '$lib/StackDiagram.svelte';
  import { reveal } from '$lib/reveal.js';

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
      <div class="hero-frame panel--strong">
        <span class="hero-label hero-label--left">// 001</span>
        <span class="hero-label hero-label--right">V1.0</span>
        <div class="hero-copy">
          <h1>THE SOVREN<br />STACK.</h1>
          <p class="hero-sub">&gt; Sovereign compute. Local identity. Programmable capital.</p>
        </div>
      </div>
      <div class="scroll-hint">[ SCROLL TO EXPLORE ]</div>
    </div>
  </section>

  <section class="products" aria-labelledby="products-heading">
    <h2 id="products-heading" class="sr-only">Products</h2>
    <div class="product-grid">
      {#each products as p, i}
        <a href={p.href} class="product-card reveal reveal-delay-{i + 1}" use:reveal>
          <span class="product-num">{p.number}</span>
          <span class="product-label tag">{p.category}</span>
          <h3 class="product-name">{p.name}</h3>
          <p class="product-desc">{p.description}</p>
          <span class="product-cta">LEARN MORE →</span>
        </a>
      {/each}
    </div>
  </section>

  <section class="stack-vis" use:reveal>
    <div class="stack-vis-inner reveal">
      <span class="panel-header">// ARCHITECTURE</span>
      <StackDiagram />
    </div>
  </section>

  <section class="thesis" use:reveal>
    <div class="thesis-inner panel--strong reveal">
      <div class="panel-header">// DOCTRINE</div>
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
    background: var(--bg);
  }

  .hero-inner {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: var(--space-3xl);
    padding: var(--space-5xl) var(--space-2xl);
    z-index: 10;
    width: 100%;
    max-width: var(--max-w);
  }

  .hero-frame {
    position: relative;
    border: var(--panel-border-strong);
    padding: var(--space-5xl) var(--space-4xl);
    width: 100%;
  }

  .hero-label {
    position: absolute;
    top: var(--space-lg);
    font-size: var(--fs-label-xs);
    letter-spacing: var(--ls-ultra);
    color: var(--text-ghost);
    text-transform: uppercase;
  }

  .hero-label--left {
    left: var(--space-xl);
  }

  .hero-label--right {
    right: var(--space-xl);
  }

  .hero-copy {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--space-xl);
  }

  h1 {
    font-size: var(--fs-hero);
    font-weight: var(--fw-bold);
    letter-spacing: var(--ls-wide);
    line-height: 1.0;
    color: var(--text-primary);
    text-transform: uppercase;
  }

  .hero-sub {
    font-size: 0.95rem;
    color: var(--text-secondary);
    letter-spacing: var(--ls-moderate);
    text-transform: uppercase;
  }

  .scroll-hint {
    font-size: var(--fs-label-xs);
    letter-spacing: var(--ls-ultra);
    color: var(--text-muted);
    position: absolute;
    bottom: var(--space-4xl);
  }

  /* Products */
  .products {
    border-top: var(--panel-border-strong);
    border-bottom: var(--panel-border-strong);
    position: relative;
    background: var(--bg);
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
    border-right: var(--panel-border);
    min-height: 400px;
    transition: background var(--transition-slow);
    text-decoration: none;
    background: transparent;
  }

  .product-card:last-child {
    border-right: none;
  }

  .product-card:hover {
    background: var(--accent-surface);
  }

  .product-num {
    font-size: var(--fs-label);
    letter-spacing: var(--ls-wider);
    color: var(--accent);
  }

  .product-label {
    align-self: flex-start;
  }

  .product-name {
    font-size: clamp(1.4rem, 2.5vw, 1.9rem);
    font-weight: var(--fw-bold);
    letter-spacing: 0.14em;
    color: var(--text-primary);
    text-transform: uppercase;
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

  .product-card:hover .product-cta {
    color: var(--accent);
  }

  /* Stack Visualization */
  .stack-vis {
    background: var(--bg);
    padding: var(--space-5xl) var(--space-3xl);
    border-bottom: var(--panel-border);
  }

  .stack-vis-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--space-3xl);
  }

  /* Thesis */
  .thesis {
    background: var(--bg);
    color: var(--text-primary);
    padding: var(--pad-section-lg);
  }

  .thesis-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    border: var(--panel-border-strong);
    padding: var(--panel-pad);
  }

  .thesis-statement {
    font-size: var(--fs-thesis);
    font-weight: var(--fw-bold);
    letter-spacing: var(--ls-tight);
    line-height: 1.25;
    margin-bottom: var(--space-5xl);
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

  /* Responsive */
  @media (max-width: 768px) {
    .product-grid {
      grid-template-columns: 1fr;
    }

    .product-card {
      border-right: none;
      border-bottom: var(--panel-border);
      min-height: auto;
      padding: var(--space-2xl) var(--space-xl);
    }

    .product-card:last-child {
      border-bottom: none;
    }

    h1 {
      font-size: clamp(2.5rem, 14vw, 4rem);
    }

    .hero-frame {
      padding: var(--space-3xl) var(--space-xl);
    }

    .thesis {
      padding: var(--space-5xl) var(--space-xl);
    }

    .thesis-inner {
      padding: var(--space-xl);
    }

    .thesis-foot {
      flex-direction: column;
      gap: var(--space-2xl);
    }
  }
</style>
