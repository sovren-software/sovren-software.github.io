<svelte:head>
  <title>The Manifesto — Sovren Software Ecosystem</title>
  <meta name="description" content="Privacy is not a feature. Control is not an option. Sovereignty is the baseline. The Sovren Stack: Augmentum OS, Visage, and Mr. Haven." />
  <meta property="og:title" content="The Manifesto — Sovren Software" />
  <meta property="og:description" content="Three pillars. One thesis. Sovereign computing, local identity, self-custodied assets." />
  <meta property="og:url" content="https://sovren.software/ecosystem" />
</svelte:head>

<script>

  const pillars = [
    {
      n: '01',
      domain: 'COMPUTING',
      product: 'AUGMENTUM OS',
      href: '/augmentum',
      thesis: 'Your OS should execute your intent, not enforce someone else\'s update policy.',
      body: 'Every system you\'ve run was designed by a vendor whose incentives diverge from yours. Telemetry, forced updates, locked-down hardware. Augmentum OS is declarative by design — your entire system state in a single file, reproducible across hardware, answerable only to you.',
    },
    {
      n: '02',
      domain: 'IDENTITY',
      product: 'VISAGE',
      href: '/visage',
      thesis: 'Biometric data belongs to you, processed on your hardware.',
      body: 'Every face recognition system you\'ve used sends your biometrics somewhere. Visage runs entirely on-device. No cloud enrollment. No external database. Your face authenticates you locally, via the same PAM stack that\'s been securing Linux for decades.',
    },
    {
      n: '03',
      domain: 'ASSETS',
      product: 'MR. HAVEN',
      href: '/mrhaven',
      thesis: 'Financial infrastructure should be programmable without requiring a custodian.',
      body: 'Banks, brokerages, and custody services exist as intermediaries between you and your wealth. Smart contracts don\'t need them. MrHaven automates value transfer on-chain — your keys, your conditions, your beneficiaries.',
    },
  ]
</script>

<main>
  <section class="hero">
    <div class="hero-inner">
      <span class="category">ECOSYSTEM</span>
      <h1>THE<br />MANIFESTO.</h1>
      <p class="tagline">We are building the infrastructure for digital autonomy. Three layers. One thesis.</p>
    </div>
  </section>

  <section class="thesis-expanded">
    <div class="thesis-inner">
      <p class="thesis-lede">
        The default state of modern technology is extraction. Your operating system reports back to its maker. Your biometrics are stored in someone else's database. Your assets move through someone else's rails.
      </p>
      <p class="thesis-body">
        This is not an accident. It is the product of incentive structures that reward scale and lock-in over user control. The vendors who built these systems are not malicious — they are optimizing for their shareholders, not for you.
      </p>
      <p class="thesis-body">
        We reject the premise that this is the only way. Computing can be sovereign. Identity can be local. Assets can be self-custodied. The tools exist. We are building the stack that makes it practical — and proving, in the process, that one person with the right infrastructure can outbuild what once required a team.
      </p>
      <p class="thesis-body">
        Each product stands on its own. Augmentum OS runs without Visage. Visage installs on any Linux system. MrHaven works without either. But the convergence is the point: Visage identity becomes a hardware-verified OS primitive. MrHaven vaults become a first-class OS credential. The three layers compose into something no single product delivers alone.
      </p>
      <blockquote>
        Privacy is not a feature.<br />
        Control is not an option.<br />
        Sovereignty is the baseline.
      </blockquote>
    </div>
  </section>

  <section class="pillars">
    <div class="pillars-inner">
      <span class="section-label">THE THREE PILLARS</span>
      {#each pillars as p}
        <div class="pillar">
          <div class="pillar-header">
            <span class="pillar-n">{p.n}</span>
            <span class="pillar-domain">{p.domain}</span>
          </div>
          <div class="pillar-body">
            <p class="pillar-thesis">"{p.thesis}"</p>
            <p class="pillar-text">{p.body}</p>
            <a href={p.href} class="pillar-link">{p.product} →</a>
          </div>
        </div>
      {/each}
    </div>
  </section>

  <section class="closing">
    <div class="closing-inner">
      <h2>WE BUILD<br />THE ALTERNATIVE.</h2>
      <p>The Sovren Stack covers computing, identity, and assets. Each product stands alone. Together — Augmentum OS as the substrate, Visage as the identity primitive, MrHaven as the capital layer — they form the infrastructure for one person to operate at the scale of a team.</p>
      <a href="/" class="btn-primary">EXPLORE THE STACK →</a>
    </div>
  </section>
</main>

<style>
  .hero {
    min-height: calc(100vh - var(--nav-h));
    display: flex;
    align-items: flex-end;
    padding: var(--pad-hero);
    border-bottom: 1px solid var(--border);
  }

  .hero-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    width: 100%;
  }

  .category {
    display: block;
    font-size: var(--fs-label);
    letter-spacing: var(--ls-wider);
    color: var(--text-muted);
    margin-bottom: var(--space-2xl);
    text-transform: uppercase;
  }

  h1 {
    font-size: clamp(4rem, 14vw, 10rem);
    font-weight: var(--fw-bold);
    letter-spacing: 0.06em;
    line-height: var(--lh-tight);
    margin-bottom: var(--space-2xl);
  }

  .tagline {
    font-size: var(--fs-tagline);
    color: var(--text-secondary);
    max-width: var(--max-w-tagline);
    line-height: 1.65;
    letter-spacing: var(--ls-default);
  }

  /* Thesis expanded */
  .thesis-expanded {
    background: var(--light-bg);
    color: var(--light-text-primary);
    padding: var(--pad-section-lg);
    border-bottom: 1px solid var(--light-border);
  }

  .thesis-inner {
    max-width: var(--max-w-prose);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: var(--space-2xl);
  }

  .thesis-lede {
    font-size: clamp(1.1rem, 2.5vw, 1.4rem);
    font-weight: var(--fw-semibold);
    line-height: var(--lh-default);
    letter-spacing: var(--ls-tight);
    color: var(--light-text-primary);
  }

  .thesis-body {
    font-size: 0.95rem;
    line-height: var(--lh-loose);
    color: #444;
    letter-spacing: var(--ls-default);
  }

  blockquote {
    border-left: 2px solid var(--light-text-primary);
    padding-left: var(--space-2xl);
    margin: var(--space-lg) 0;
    font-size: clamp(1rem, 2vw, 1.25rem);
    font-weight: var(--fw-semibold);
    line-height: 1.7;
    letter-spacing: 0.01em;
  }

  /* Pillars */
  .pillars {
    padding: var(--pad-section);
    border-top: 1px solid var(--border);
  }

  .pillars-inner {
    max-width: var(--max-w);
    margin: 0 auto;
  }

  .section-label {
    display: block;
    font-size: var(--fs-label-sm);
    letter-spacing: 0.2em;
    color: var(--text-muted);
    margin-bottom: var(--space-4xl);
    text-transform: uppercase;
  }

  .pillar {
    display: grid;
    grid-template-columns: 200px 1fr;
    gap: var(--space-5xl);
    padding: var(--space-4xl) 0;
    border-top: 1px solid var(--border);
  }

  .pillar:last-child {
    border-bottom: 1px solid var(--border);
  }

  .pillar-header {
    display: flex;
    flex-direction: column;
    gap: var(--space-sm);
    padding-top: var(--space-xs);
  }

  .pillar-n {
    font-size: var(--fs-label);
    letter-spacing: var(--ls-wider);
    color: var(--text-muted);
  }

  .pillar-domain {
    font-size: var(--fs-btn);
    font-weight: var(--fw-bold);
    letter-spacing: 0.16em;
    color: var(--text-secondary);
  }

  .pillar-body {
    display: flex;
    flex-direction: column;
    gap: var(--space-lg);
  }

  .pillar-thesis {
    font-size: 0.95rem;
    font-weight: var(--fw-semibold);
    color: var(--text-primary);
    line-height: 1.55;
    letter-spacing: 0.01em;
  }

  .pillar-text {
    font-size: var(--fs-body-xs);
    color: var(--text-secondary);
    line-height: var(--lh-relaxed);
    letter-spacing: var(--ls-default);
    max-width: var(--max-w-tagline);
  }

  .pillar-link {
    font-size: var(--fs-label);
    letter-spacing: var(--ls-wider);
    color: var(--text-muted);
    text-decoration: none;
    transition: color var(--transition-fast);
    text-transform: uppercase;
  }

  .pillar-link:hover {
    color: var(--text-primary);
  }

  /* Closing */
  .closing {
    background: var(--light-bg);
    color: var(--light-text-primary);
    padding: var(--pad-section-lg);
    border-top: 1px solid var(--light-border);
  }

  .closing-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: var(--space-xl);
  }

  .closing h2 {
    font-size: var(--fs-h2-large);
    font-weight: var(--fw-bold);
    letter-spacing: 0.08em;
    line-height: 1.0;
  }

  .closing p {
    font-size: var(--fs-body);
    color: var(--light-text-secondary);
    max-width: 520px;
    line-height: var(--lh-relaxed);
    letter-spacing: var(--ls-default);
  }

  .btn-primary {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: var(--fs-btn);
    letter-spacing: var(--ls-wider);
    padding: var(--btn-pad);
    background: var(--light-text-primary);
    color: var(--light-bg);
    text-decoration: none;
    transition: opacity var(--transition-fast);
    align-self: flex-start;
    margin-top: var(--space-sm);
  }

  .btn-primary:hover {
    opacity: 0.75;
  }

  /* Responsive */
  @media (max-width: 768px) {
    .hero {
      padding: var(--space-4xl) var(--space-xl) var(--space-5xl);
    }

    h1 {
      font-size: clamp(3.5rem, 18vw, 6rem);
    }

    .pillar {
      grid-template-columns: 1fr;
      gap: var(--space-xl);
    }
  }
</style>
