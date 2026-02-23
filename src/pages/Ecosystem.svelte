<svelte:head>
  <title>The Manifesto — Sovren Software Ecosystem</title>
  <meta name="description" content="Privacy is not a feature. Control is not an option. Sovereignty is the baseline. The Sovren Stack: Augmentum OS, Visage, and Mr. Haven." />
  <meta property="og:title" content="The Manifesto — Sovren Software" />
  <meta property="og:description" content="Three pillars. One thesis. Sovereign computing, local identity, self-custodied assets." />
  <meta property="og:url" content="https://sovren.software/#/ecosystem" />
</svelte:head>

<script>
  import { onMount } from 'svelte'
  onMount(() => window.scrollTo(0, 0))

  const pillars = [
    {
      n: '01',
      domain: 'COMPUTING',
      product: 'AUGMENTUM OS',
      href: '#/augmentum',
      thesis: 'Your OS should execute your intent, not enforce someone else\'s update policy.',
      body: 'Every system you\'ve run was designed by a vendor whose incentives diverge from yours. Telemetry, forced updates, locked-down hardware. Augmentum OS is declarative by design — your entire system state in a single file, reproducible across hardware, answerable only to you.',
    },
    {
      n: '02',
      domain: 'IDENTITY',
      product: 'VISAGE',
      href: '#/visage',
      thesis: 'Biometric data belongs to you, processed on your hardware.',
      body: 'Every face recognition system you\'ve used sends your biometrics somewhere. Visage runs entirely on-device. No cloud enrollment. No external database. Your face authenticates you locally, via the same PAM stack that\'s been securing Linux for decades.',
    },
    {
      n: '03',
      domain: 'ASSETS',
      product: 'MR. HAVEN',
      href: '#/mrhaven',
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
      <p>The Sovren Stack covers computing, identity, and assets. Each product stands alone. Together they form the infrastructure for one person to operate at the scale of a team.</p>
      <a href="#/" class="btn-primary">EXPLORE THE STACK →</a>
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
    font-size: clamp(4rem, 14vw, 10rem);
    font-weight: 700;
    letter-spacing: 0.06em;
    line-height: 0.95;
    margin-bottom: 2rem;
  }

  .tagline {
    font-size: clamp(0.95rem, 2vw, 1.1rem);
    color: var(--text-secondary);
    max-width: 600px;
    line-height: 1.65;
    letter-spacing: 0.02em;
  }

  /* Thesis expanded */
  .thesis-expanded {
    background: #ffffff;
    color: #000;
    padding: 7rem 2.5rem;
    border-bottom: 1px solid #e5e5e5;
  }

  .thesis-inner {
    max-width: 760px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }

  .thesis-lede {
    font-size: clamp(1.1rem, 2.5vw, 1.4rem);
    font-weight: 600;
    line-height: 1.6;
    letter-spacing: -0.01em;
    color: #000;
  }

  .thesis-body {
    font-size: 0.95rem;
    line-height: 1.85;
    color: #444;
    letter-spacing: 0.02em;
  }

  blockquote {
    border-left: 2px solid #000;
    padding-left: 2rem;
    margin: 1rem 0;
    font-size: clamp(1rem, 2vw, 1.25rem);
    font-weight: 600;
    line-height: 1.7;
    letter-spacing: 0.01em;
  }

  /* Pillars */
  .pillars {
    padding: 6rem 2.5rem;
    border-top: 1px solid var(--border);
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

  .pillar {
    display: grid;
    grid-template-columns: 200px 1fr;
    gap: 4rem;
    padding: 3rem 0;
    border-top: 1px solid var(--border);
  }

  .pillar:last-child {
    border-bottom: 1px solid var(--border);
  }

  .pillar-header {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    padding-top: 0.25rem;
  }

  .pillar-n {
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    color: var(--text-muted);
  }

  .pillar-domain {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.16em;
    color: var(--text-secondary);
  }

  .pillar-body {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .pillar-thesis {
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--text-primary);
    line-height: 1.55;
    letter-spacing: 0.01em;
  }

  .pillar-text {
    font-size: 0.85rem;
    color: var(--text-secondary);
    line-height: 1.75;
    letter-spacing: 0.02em;
    max-width: 600px;
  }

  .pillar-link {
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    color: var(--text-muted);
    text-decoration: none;
    transition: color 0.15s;
    text-transform: uppercase;
  }

  .pillar-link:hover {
    color: var(--text-primary);
  }

  /* Closing */
  .closing {
    background: #fff;
    color: #000;
    padding: 7rem 2.5rem;
    border-top: 1px solid #e5e5e5;
  }

  .closing-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }

  .closing h2 {
    font-size: clamp(2.5rem, 6vw, 5rem);
    font-weight: 700;
    letter-spacing: 0.08em;
    line-height: 1.0;
  }

  .closing p {
    font-size: 0.9rem;
    color: #555;
    max-width: 520px;
    line-height: 1.75;
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

  /* Responsive */
  @media (max-width: 768px) {
    .hero {
      padding: 3rem 1.5rem 4rem;
    }

    h1 {
      font-size: clamp(3.5rem, 18vw, 6rem);
    }

    .pillar {
      grid-template-columns: 1fr;
      gap: 1.5rem;
    }
  }
</style>
