<svelte:head>
  <title>Sovren Software — Sovereign Computing Stack</title>
  <meta name="description" content="Sovereign OS. Local identity. Programmable assets. Augmentum OS, Visage, and Mr. Haven — computing, identity, and finance fully under your control." />
  <meta property="og:title" content="Sovren Software — Sovereign Computing Stack" />
  <meta property="og:description" content="Sovereign OS. Local identity. Programmable assets. The stack for people who refuse to be owned by their software vendor." />
  <meta property="og:url" content="https://sovren.software/" />
</svelte:head>

<script>

  const asciiArt = `      _______________
     /              /|
    /              / |
   /______________/  |
   |  __________  |  |
   | |          | |  |
   | |  [S.S.]  | | /
   | |__________| |/
   |______________|`

  const products = [
    {
      number: '01',
      category: 'OS',
      name: 'AUGMENTUM OS',
      href: '/augmentum',
      description: 'Declarative NixOS system. Your entire OS in a single reproducible config — version-controlled, rollback-capable, answerable only to you. No silent updates. No telemetry.',
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
      <pre class="ascii-art">{asciiArt}</pre>
      <div class="hero-copy">
        <h1>THE SOVREN<br />STACK.</h1>
        <p class="hero-sub">Sovereign OS. Local identity. Programmable assets.</p>
      </div>
      <div class="scroll-hint">[ SCROLL TO EXPLORE ]</div>
    </div>
  </section>

  <section class="products">
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
    <div class="thesis-inner">
      <h2 class="thesis-statement">
        Privacy is not a feature.<br />
        Control is not an option.<br />
        Sovereignty is the baseline for the<br />
        future of digital existence.
      </h2>
      <div class="thesis-foot">
        <p>We build tools for those who want more of themselves — more capacity, more control, more surface area. The stack is open, inspectable, and answerable only to you.</p>
        <a href="/ecosystem" class="btn-manifesto">READ THE MANIFESTO</a>
      </div>
    </div>
  </section>
</main>

<style>
  .hero {
    min-height: calc(100vh - 60px);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .hero-inner {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 2.5rem;
    padding: 4rem 2rem;
  }

  .ascii-art {
    font-family: var(--font-mono);
    font-size: 0.8rem;
    line-height: 1.45;
    color: var(--text-muted);
    white-space: pre;
    user-select: none;
  }

  h1 {
    font-size: clamp(3.5rem, 11vw, 8rem);
    font-weight: 700;
    letter-spacing: 0.1em;
    line-height: 1.0;
    color: var(--text-primary);
    text-transform: uppercase;
  }

  .hero-sub {
    font-size: 0.95rem;
    color: var(--text-secondary);
    letter-spacing: 0.06em;
  }

  .scroll-hint {
    font-size: 0.65rem;
    letter-spacing: 0.25em;
    color: var(--text-muted);
  }

  /* Products */
  .products {
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
  }

  .product-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    max-width: var(--max-w);
    margin: 0 auto;
  }

  .product-card {
    padding: 3rem 2.5rem;
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
    border-right: 1px solid var(--border);
    min-height: 400px;
    transition: background 0.15s;
    text-decoration: none;
  }

  .product-card:last-child {
    border-right: none;
  }

  .product-card:hover {
    background: rgba(255, 255, 255, 0.025);
  }

  .product-label {
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    color: var(--text-muted);
    text-transform: uppercase;
  }

  .product-name {
    font-size: clamp(1.4rem, 2.5vw, 1.9rem);
    font-weight: 700;
    letter-spacing: 0.14em;
    color: var(--text-primary);
    text-transform: uppercase;
  }

  .product-desc {
    font-size: 0.82rem;
    color: var(--text-secondary);
    line-height: 1.75;
    flex: 1;
    letter-spacing: 0.02em;
  }

  .product-cta {
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    color: var(--text-muted);
    transition: color 0.15s;
    text-transform: uppercase;
  }

  .product-card:hover .product-cta {
    color: var(--text-primary);
  }

  /* Thesis */
  .thesis {
    background: #ffffff;
    color: #000000;
    padding: 7rem 2.5rem;
  }

  .thesis-inner {
    max-width: var(--max-w);
    margin: 0 auto;
  }

  .thesis-statement {
    font-size: clamp(1.75rem, 3.5vw, 3.25rem);
    font-weight: 700;
    letter-spacing: -0.01em;
    line-height: 1.25;
    margin-bottom: 4rem;
  }

  .thesis-foot {
    display: flex;
    align-items: center;
    gap: 4rem;
    flex-wrap: wrap;
  }

  .thesis-foot p {
    font-size: 0.875rem;
    line-height: 1.75;
    max-width: 480px;
    color: #555;
    letter-spacing: 0.02em;
  }

  .btn-manifesto {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 0.7rem;
    font-weight: 500;
    letter-spacing: 0.18em;
    padding: 0.85rem 1.75rem;
    border: 1px solid #000;
    background: transparent;
    color: #000;
    cursor: pointer;
    transition: background 0.15s, color 0.15s;
    white-space: nowrap;
    text-transform: uppercase;
    text-decoration: none;
  }

  .btn-manifesto:hover {
    background: #000;
    color: #fff;
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
      padding: 2rem 1.5rem;
    }

    .product-card:last-child {
      border-bottom: none;
    }

    h1 {
      font-size: clamp(2.5rem, 14vw, 4rem);
    }

    .ascii-art {
      font-size: 0.6rem;
    }

    .thesis {
      padding: 4rem 1.5rem;
    }

    .thesis-foot {
      flex-direction: column;
      gap: 2rem;
    }
  }
</style>
