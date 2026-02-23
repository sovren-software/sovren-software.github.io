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
      name: 'AUGMENTUM',
      url: 'https://augmentum.computer',
      description: 'A hard-kernel operating system designed for zero-trust environments. Total isolation of critical processes from public networks.',
    },
    {
      number: '02',
      category: 'IDENTITY',
      name: 'VISAGE',
      url: 'https://github.com/sovren-software/visage',
      description: 'A biometric wedge for decentralized authentication. Your face is your key, stored locally and never broadcast to the cloud.',
    },
    {
      number: '03',
      category: 'FINANCE',
      name: 'MR. HAVEN',
      url: 'https://mrhaven.io',
      description: 'The ultimate financial passport. Encrypted asset management and private transaction relay for the global citizen.',
    },
  ]
</script>

<nav>
  <div class="nav-inner">
    <span class="wordmark">SOVREN</span>
    <div class="nav-links">
      <a href="https://augmentum.computer" target="_blank" rel="noreferrer">AUGMENTUM</a>
      <a href="https://github.com/sovren-software/visage" target="_blank" rel="noreferrer">VISAGE</a>
      <a href="https://mrhaven.io" target="_blank" rel="noreferrer">MR. HAVEN</a>
      <a href="#thesis">ECOSYSTEM</a>
    </div>
  </div>
</nav>

<main>
  <section class="hero">
    <div class="hero-inner">
      <pre class="ascii-art">{asciiArt}</pre>
      <div class="hero-copy">
        <h1>THE SOVREN<br />STACK.</h1>
        <p class="hero-sub">Building the infrastructure for digital autonomy.</p>
      </div>
      <div class="scroll-hint">[ SCROLL TO EXPLORE ]</div>
    </div>
  </section>

  <section id="products" class="products">
    <div class="product-grid">
      {#each products as p}
        <a href={p.url} class="product-card" target="_blank" rel="noreferrer">
          <span class="product-label">{p.number} / {p.category}</span>
          <h3 class="product-name">{p.name}</h3>
          <p class="product-desc">{p.description}</p>
          <span class="product-cta">LEARN MORE →</span>
        </a>
      {/each}
    </div>
  </section>

  <section id="thesis" class="thesis">
    <div class="thesis-inner">
      <h2 class="thesis-statement">
        Privacy is not a feature.<br />
        Control is not an option.<br />
        Sovrenity is the baseline for the<br />
        future of digital existence.
      </h2>
      <div class="thesis-foot">
        <p>We build tools for those who refuse to be tracked, profiled, or boxed in. Our stack is open for inspection, closed to intrusion.</p>
        <button class="btn-manifesto">READ THE MANIFESTO</button>
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="footer-inner">
    <div class="footer-top">
      <span class="footer-wordmark">SOVREN</span>
      <nav class="footer-nav">
        <a href="https://twitter.com/sovren_software" target="_blank" rel="noreferrer">TWITTER</a>
        <a href="https://github.com/sovren-software" target="_blank" rel="noreferrer">GITHUB</a>
        <a href="#" class="muted">WHITEPAPER</a>
        <a href="mailto:hello@sovren.software" class="muted">CONTACT</a>
        <a href="#" class="muted">PRIVACY</a>
        <a href="#" class="muted">LEGAL</a>
        <a href="#" class="muted">CAREERS</a>
        <a href="#" class="muted">NODES</a>
      </nav>
    </div>
    <div class="footer-copy">© 2025 SOVREN SOFTWARE. BUILT FOR AUTONOMY.</div>
  </div>
</footer>

<style>
  /* ─── Nav ─── */
  nav {
    position: sticky;
    top: 0;
    z-index: 10;
    background: var(--bg);
    border-bottom: 1px solid var(--border);
  }

  .nav-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    padding: 0 2.5rem;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .wordmark {
    font-size: 0.875rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    color: var(--text-primary);
  }

  .nav-links {
    display: flex;
    gap: 2.5rem;
    font-size: 0.7rem;
    letter-spacing: 0.14em;
    color: var(--text-secondary);
  }

  .nav-links a:hover {
    color: var(--text-primary);
  }

  /* ─── Hero ─── */
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

  /* ─── Products ─── */
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

  /* ─── Thesis ─── */
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
  }

  .btn-manifesto:hover {
    background: #000;
    color: #fff;
  }

  /* ─── Footer ─── */
  footer {
    background: var(--bg);
    border-top: 1px solid var(--border);
    padding: 3.5rem 2.5rem;
  }

  .footer-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }

  .footer-top {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 2rem;
    flex-wrap: wrap;
  }

  .footer-wordmark {
    font-size: 0.875rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    color: var(--text-primary);
  }

  .footer-nav {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem 2rem;
    font-size: 0.65rem;
    letter-spacing: 0.14em;
  }

  .footer-nav a {
    color: var(--text-secondary);
  }

  .footer-nav a.muted {
    color: var(--text-muted);
  }

  .footer-nav a:hover {
    color: var(--text-primary);
  }

  .footer-copy {
    font-size: 0.6rem;
    letter-spacing: 0.12em;
    color: var(--text-muted);
  }

  /* ─── Responsive ─── */
  @media (max-width: 768px) {
    .product-grid {
      grid-template-columns: 1fr;
    }

    .product-card {
      border-right: none;
      border-bottom: 1px solid var(--border);
      min-height: auto;
    }

    .product-card:last-child {
      border-bottom: none;
    }

    h1 {
      font-size: 3rem;
    }

    .thesis-statement {
      font-size: 1.6rem;
    }

    .nav-links {
      gap: 1.25rem;
      font-size: 0.62rem;
    }

    .thesis-foot {
      flex-direction: column;
      gap: 2rem;
    }
  }
</style>
