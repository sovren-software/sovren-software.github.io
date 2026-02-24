<svelte:head>
  <title>Visage — Linux Face Authentication via PAM | Sovren Software</title>
  <meta name="description" content="Open source Linux face authentication via PAM. ONNX inference runs on-device — no cloud enrollment, no biometric database. Rust. MIT licensed. v0.2.0." />
  <meta property="og:title" content="Visage — Linux Face Authentication via PAM" />
  <meta property="og:description" content="Windows Hello for Linux. ONNX face recognition runs entirely on your hardware. No cloud enrollment. MIT licensed, written in Rust." />
  <meta property="og:url" content="https://sovren.software/visage" />
</svelte:head>

<script>

  const features = [
    {
      label: 'LOCAL INFERENCE',
      desc: 'ONNX face recognition model runs entirely on your hardware. No cloud enrollment. No biometric database. Your face never leaves your machine.',
    },
    {
      label: 'PAM INTEGRATION',
      desc: 'Drop-in replacement for any PAM-based authentication stack. Works with sudo, screen lock, and login — without modifying existing system configuration.',
    },
    {
      label: 'IR CAMERA SUPPORT',
      desc: 'Native support for Windows Hello-compatible IR cameras. Liveness detection built in. Works in low light, resistant to photo-based spoofing attacks.',
    },
    {
      label: 'SUB-SECOND AUTH',
      desc: 'Under one second on IR camera hardware with a warm daemon. The persistent daemon keeps the model resident — no cold start on every lock. Authentication finishes before your hand leaves the trackpad.',
    },
  ]
</script>

<main>
  <section class="hero">
    <div class="hero-inner">
      <span class="category">02 / IDENTITY</span>
      <h1>VISAGE.</h1>
      <p class="status">Open source · MIT · v0.2.0</p>
      <p class="tagline">Linux face authentication via PAM. Your face is your key — processed locally, never broadcast to the cloud.</p>
    </div>
  </section>

  <section class="overview">
    <div class="overview-inner">
      <div class="overview-text">
        <p>Windows Hello has worked for years on Windows. Linux users have been left out. Visage closes that gap with a native, open-source face authentication daemon that works with any PAM-compatible application.</p>
        <p>Built in Rust for performance and safety. The ONNX inference engine keeps model weights local. No account creation. No enrollment servers. No biometric data leaving your hardware.</p>
        <p>v0.x is MIT-licensed and works on any Linux system. v2, in active development, integrates at the Augmentum OS identity layer — your face-verified credential becomes a system-level primitive, not just a PAM module. The open/closed split is intentional: the open-source foundation earns trust; the OS-native layer delivers the full vision.</p>
      </div>
      <div class="overview-specs">
        <div class="spec-row">
          <span class="spec-label">LANGUAGE</span>
          <span class="spec-value">Rust</span>
        </div>
        <div class="spec-row">
          <span class="spec-label">INFERENCE</span>
          <span class="spec-value">ONNX · On-device</span>
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
          <span class="spec-value spec-live">Live · v0.2.0</span>
        </div>
      </div>
    </div>
  </section>

  <section class="features">
    <div class="features-inner">
      <span class="section-label">CAPABILITIES</span>
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

  .spec-live {
    color: #111;
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

  /* Responsive */
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
