<svelte:head>
  <title>Visage — Linux Face Authentication via PAM | Sovren Software</title>
  <meta name="description" content="Open source Linux face authentication via PAM. Inference runs on-device — no cloud enrollment, no biometric database. Rust. MIT licensed. v0.2.0." />
  <meta property="og:title" content="Visage — Your Face Is Your Key." />
  <meta property="og:description" content="Linux face authentication that runs entirely on your hardware. No cloud enrollment. No biometric database. Open source, MIT licensed." />
  <meta property="og:url" content="https://sovren.software/visage" />
</svelte:head>

<script>
  const pillars = [
    {
      num: '01',
      label: 'YOUR BIOMETRICS STAY ON YOUR HARDWARE.',
      desc: 'Face recognition runs entirely on-device. No cloud enrollment. No biometric database. Your face never leaves your machine — not during setup, not during authentication, not ever.',
    },
    {
      num: '02',
      label: 'DROPS INTO ANY LINUX AUTH STACK.',
      desc: 'Visage is a PAM module. It works with sudo, screen lock, and login without modifying your existing system configuration. If your system supports PAM, Visage works.',
    },
    {
      num: '03',
      label: 'BUILT FOR IR. RESISTANT TO SPOOFING.',
      desc: 'Native support for Windows Hello-compatible IR cameras. Liveness detection is built in. Works in low light. Resistant to photo-based spoofing attacks.',
    },
    {
      num: '04',
      label: 'UNDER ONE SECOND.',
      desc: 'The persistent daemon keeps the model resident — no cold start on every lock. Authentication finishes before your hand leaves the trackpad.',
    },
  ]
</script>

<main>
  <section class="hero">
    <div class="hero-inner">
      <span class="category">02 / IDENTITY</span>
      <h1>VISAGE.</h1>
      <p class="status">Open source · MIT · v0.2.0</p>
      <p class="tagline">Your face is your key. Processed locally. Never broadcast to the cloud.</p>
    </div>
  </section>

  <section class="overview">
    <div class="overview-inner">
      <div class="overview-text">
        <p class="overview-lead">Face authentication the way it should work.</p>
        <p class="overview-body">Windows Hello has worked on Windows for years. Linux users were left out. Visage closes that gap — a native, open-source face authentication daemon built in Rust, with no external dependencies and no data leaving your hardware.</p>
        <p class="overview-body">v0.x is MIT-licensed and works on any Linux system. v2, in active development, integrates at the Augmentum OS identity layer — your face-verified credential becomes a system-level primitive, not just a PAM module.</p>
        <p class="overview-stack">The open/closed split is intentional. The open-source foundation earns trust. The OS-native layer delivers the full vision.</p>
      </div>
      <div class="overview-specs">
        <div class="spec-row">
          <span class="spec-label">LANGUAGE</span>
          <span class="spec-value">Rust</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">INFERENCE</span>
          <span class="spec-value">On-device · No cloud</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">AUTH</span>
          <span class="spec-value">PAM module</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">CAMERA</span>
          <span class="spec-value">RGB + IR · V4L2</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">LICENSE</span>
          <span class="spec-value">MIT · Open source</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">STATUS</span>
          <span class="spec-value">Live · v0.2.0</span>
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
      <h2>OPEN SOURCE.<br />AUDIT IT.</h2>
      <p>Visage is MIT-licensed and fully open. Read the code, fork it, contribute. Security through obscurity is not security.</p>
      <div class="cta-links">
        <a href="https://github.com/sovren-software/visage" target="_blank" rel="noreferrer" class="btn-primary">
          VIEW ON GITHUB →
        </a>
        <a href="https://github.com/sovren-software/visage/releases" target="_blank" rel="noreferrer" class="btn-secondary">
          RELEASES
        </a>
      </div>
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
    font-size: clamp(5rem, 18vw, 12rem);
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

  /* ── Pillars ── */
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

  .cta-links {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    margin-top: 0.5rem;
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
  }

  .btn-primary:hover {
    opacity: 0.75;
  }

  .btn-secondary {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    padding: 0.85rem 1.75rem;
    border: 1px solid #000;
    background: transparent;
    color: #000;
    text-decoration: none;
    transition: background 0.15s, color 0.15s;
  }

  .btn-secondary:hover {
    background: #000;
    color: #fff;
  }

  /* ── Responsive ── */
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

    .pillar-row {
      grid-template-columns: 1fr;
      gap: 1.5rem;
      padding: 2rem 0;
    }
  }
</style>
