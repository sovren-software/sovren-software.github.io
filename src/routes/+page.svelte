<svelte:head>
  <title>Sovren Software — Customer-Owned Infrastructure for Agentic Work</title>
  <meta name="description" content="Sovren Software builds customer-owned infrastructure for reliable agentic work: Esver OS for verified workflows, Visage for local identity, and Mr. Haven for programmable capital." />
  <link rel="canonical" href="https://sovren.software/" />
  <meta property="og:title" content="Sovren Software — Customer-Owned Infrastructure for Agentic Work" />
  <meta property="og:description" content="Esver OS turns repeated company workflows into verified executable skills. Visage keeps identity local. Mr. Haven keeps capital programmable." />
  <meta property="og:url" content="https://sovren.software/" />
  <meta name="twitter:title" content="Sovren Software — Customer-Owned Infrastructure for Agentic Work" />
  <meta name="twitter:description" content="Esver OS turns repeated company workflows into verified executable skills. Visage keeps identity local. Mr. Haven keeps capital programmable." />
</svelte:head>

<script>
  import StackDiagram from '$lib/StackDiagram.svelte';
  import HeroGlyph from '$lib/HeroGlyph.svelte';
  import Icon from '$lib/Icon.svelte';
  import { reveal } from '$lib/reveal.js';

  const products = [
    {
      number: '01',
      category: 'OS',
      icon: 'compute',
      name: 'ESVER OS',
      href: '/esver',
      description: 'Customer-owned operating layer for reliable agentic work. Esver turns repeated company workflows into verified executable skills agents can run on local or customer-controlled infrastructure.',
    },
    {
      number: '02',
      category: 'IDENTITY',
      icon: 'identity',
      name: 'VISAGE',
      href: '/visage',
      description: 'Linux face authentication via PAM. ONNX inference runs entirely on-device — no cloud enrollment, no biometric database. Open source, MIT licensed.',
    },
    {
      number: '03',
      category: 'FINANCE',
      icon: 'capital',
      name: 'MR. HAVEN',
      href: '/mrhaven',
      description: 'Non-custodial USDC time vault on Base L2. Set conditions, name beneficiaries, define schedules — or designate autonomous agents as recipients. Smart contract executes regardless of who holds the keys.',
    },
  ]
</script>

<main>
  <section class="hero">
    <div class="hero-split">
      <div class="hero-frame panel--strong">
        <span class="hero-label hero-label--left">// 001</span>
        <span class="hero-label hero-label--right">V1.0</span>
        <h1>THE SOVREN<br />STACK.</h1>
        <p class="hero-sub">&gt; Verified work. Local identity. Programmable capital.</p>
        <div class="scroll-hint">[ SCROLL TO EXPLORE ]</div>
      </div>
      <div class="hero-glyph">
        <HeroGlyph id="sovren" />
      </div>
    </div>
  </section>

  <section class="products" aria-labelledby="products-heading">
    <div class="section-rule">
      <span class="rule-label">// PRODUCTS</span>
      <span class="rule-line"></span>
      <span class="rule-marker">+</span>
    </div>
    <h2 id="products-heading" class="sr-only">Products</h2>
    <div class="product-grid">
      {#each products as p, i}
        <a href={p.href} class="product-card reveal reveal-delay-{i + 1}" use:reveal>
          <div class="product-top">
            <span class="product-num">{p.number}</span>
            <span class="product-icon"><Icon name={p.icon} size={18} /></span>
          </div>
          <span class="product-label tag">{p.category}</span>
          <h3 class="product-name">{p.name}</h3>
          <p class="product-desc">{p.description}</p>
          <span class="product-cta">LEARN MORE →</span>
        </a>
      {/each}
    </div>
  </section>

  <section class="stack-vis">
    <div class="stack-vis-inner reveal panel" use:reveal>
      <div class="panel-header">// ARCHITECTURE</div>
      <div class="stack-vis-body">
        <div class="stack-vis-annotations">
          <span class="anno">COMPUTE</span>
          <span class="anno">IDENTITY</span>
          <span class="anno">CAPITAL</span>
        </div>
        <StackDiagram />
        <div class="stack-vis-legend">
          <span class="legend-item"><span class="legend-dot"></span> CONVERGENCE POINT</span>
          <span class="legend-item">--- SIGNAL PATH</span>
        </div>
      </div>
    </div>
  </section>

  <section class="thesis">
    <div class="thesis-inner panel--strong reveal" use:reveal>
      <div class="panel-header">// DOCTRINE</div>
      <h2 class="thesis-statement">
        Work should be verifiable.<br />
        Identity should stay local.<br />
        Capital should obey code.<br />
        Control should stay with the owner.
      </h2>
      <div class="thesis-foot">
        <p>We build customer-owned infrastructure for people and companies that need agents to act reliably without giving vendors control of the workflow, identity, or assets underneath.</p>
        <a href="/ecosystem" class="btn-peak">READ THE CODEX</a>
      </div>
    </div>
  </section>
</main>

<style>
  .hero {
    min-height: calc(100vh - var(--nav-h));
    display: flex;
    align-items: center;
    padding: var(--space-5xl) var(--space-3xl);
    background: var(--bg);
  }

  .hero-split {
    max-width: var(--max-w);
    margin: 0 auto;
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--space-4xl);
    align-items: center;
  }

  .hero-glyph {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .hero-frame {
    position: relative;
    border: var(--panel-border-strong);
    padding: var(--space-4xl) var(--space-3xl);
    background: var(--bg);
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
    margin-top: var(--space-2xl);
  }

  /* Section Rule Decorator */
  .section-rule {
    display: flex;
    align-items: center;
    gap: var(--space-lg);
    max-width: var(--max-w);
    margin: 0 auto;
    padding: var(--space-lg) var(--space-3xl);
  }

  .rule-label {
    font-size: var(--fs-label-xs);
    letter-spacing: var(--ls-ultra);
    color: var(--text-ghost);
    text-transform: uppercase;
    white-space: nowrap;
  }

  .rule-line {
    flex: 1;
    height: 1px;
    background: var(--border);
  }

  .rule-marker {
    font-size: var(--fs-label);
    color: var(--accent);
    opacity: 0.4;
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

  .product-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .product-num {
    font-size: var(--fs-label);
    letter-spacing: var(--ls-wider);
    color: var(--accent);
  }

  .product-icon {
    color: var(--text-ghost);
    transition: color var(--transition-fast);
  }

  .product-card:hover .product-icon {
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
  }

  .stack-vis-inner {
    max-width: 680px;
    margin: 0 auto;
  }

  .stack-vis-body {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--space-2xl);
  }

  .stack-vis-annotations {
    display: flex;
    justify-content: space-between;
    width: 100%;
    max-width: 420px;
  }

  .anno {
    font-size: 9px;
    letter-spacing: var(--ls-ultra);
    color: var(--text-ghost);
    text-transform: uppercase;
  }

  .stack-vis-legend {
    display: flex;
    gap: var(--space-3xl);
    justify-content: center;
  }

  .legend-item {
    font-size: 9px;
    letter-spacing: var(--ls-wider);
    color: var(--text-ghost);
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: var(--space-xs);
  }

  .legend-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--accent);
    opacity: 0.5;
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
    .hero-split {
      grid-template-columns: 1fr;
    }

    .hero-glyph {
      order: -1;
    }

    .hero-frame {
      padding: var(--space-3xl) var(--space-xl);
    }

    .stack-vis-annotations,
    .stack-vis-legend {
      display: none;
    }
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
