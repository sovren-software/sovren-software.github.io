<svelte:head>
  <title>Ecosystem Manifesto — The Sovren Stack | Sovren Software</title>
  <meta name="description" content="Privacy is not a feature. Security is not a tradeoff. Sovereignty is the only acceptable default. The manifesto behind Sovren Software's sovereign command infrastructure." />
  <link rel="canonical" href="https://sovren.software/ecosystem" />
  <meta property="og:title" content="The Sovren Manifesto. Command Your Infrastructure." />
  <meta property="og:description" content="We build sovereign infrastructure for operators who refuse to be tenants. Compute, identity, and capital — under a single chain of command." />
  <meta property="og:url" content="https://sovren.software/ecosystem" />
  <meta name="twitter:title" content="The Sovren Manifesto. Command Your Infrastructure." />
  <meta name="twitter:description" content="We build sovereign infrastructure for operators who refuse to be tenants. Compute, identity, and capital — under a single chain of command." />
</svelte:head>

<script>
  const pillars = [
    {
      num: '01',
      domain: 'COMPUTING',
      title: 'THE MACHINE IS A COMMAND CENTER, NOT A SUBSCRIPTION.',
      desc: 'An operating system that serves the vendor is not yours. Esver OS is built on the trifecta: UX that does not demand technical sacrifice, privacy that is architectural rather than cosmetic, and security that is the perimeter of your authority. Voice-native interface. Local AI co-pilot. Biometric-secured sessions. Declarative NixOS substrate. None of these properties trade off against the others. That is the point.',
      link: { label: 'ESVER OS →', href: '/esver' }
    },
    {
      num: '02',
      domain: 'IDENTITY',
      title: 'YOU ARE NOT A ROW IN A DATABASE.',
      desc: 'Biometrics should never leave the hardware they were captured on. Verification is a local cryptographic process, not a cloud API call. If a system requires your face to authenticate, it must prove it cannot steal it.',
      link: { label: 'VISAGE →', href: '/visage' }
    },
    {
      num: '03',
      domain: 'CAPITAL',
      title: 'NO HUMANS IN THE LOOP.',
      desc: 'Assets require custody or cryptography. We choose cryptography. A programmable vault should execute rules without hesitation, without exception, and without permission from a compliance department.',
      link: { label: 'MR. HAVEN →', href: '/mrhaven' }
    }
  ]
</script>

<main>
  <section class="hero">
    <div class="hero-inner">
      <span class="category">COMPANY</span>
      <h1>THE MANIFESTO.</h1>
      <p class="tagline">We reject the premise that extraction is the default state of technology.</p>
    </div>
  </section>

  <section class="thesis-expanded">
    <div class="thesis-inner glitch-subtle preserve-3d">
      <p class="thesis-lede">The industry convinced you that convenience requires compromise. That good UX means accepting telemetry. That strong security means sacrificing usability. That privacy is a premium feature. None of that is true. It is just what the vendor model requires.</p>

      <div class="thesis-body">
        <p>Your operating system is a managed endpoint in someone else's deployment. Your identity lives in a database you do not control. Your assets are held by institutions that decide when you can access them. At every layer of the stack, a vendor inserted themselves between you and your own infrastructure — and called it a service.</p>

        <blockquote>You are not the root user of your own life. You are a tenant. Sovren Software exists to change that.</blockquote>

        <p>We build infrastructure on a single engineering commitment: UX, privacy, and security are not a tradeoff triangle. They are a trifecta. Every design decision moves along all three axes without sacrificing any of them. A command center you actually want to use. An identity layer that cannot be stolen. A capital layer no one else can touch. The stack is sovereign because it was built to be — not because sovereignty was bolted on after the fact.</p>
      </div>
    </div>
  </section>

  <section class="pillars">
    <div class="pillars-inner">
      <span class="section-label">THE THREE PILLARS</span>

      {#each pillars as p}
        <div class="pillar">
          <div class="pillar-header">
            <span class="pillar-n">{p.num}</span>
            <span class="pillar-domain">{p.domain}</span>
          </div>
          <div class="pillar-body">
            <h3 class="pillar-thesis">{p.title}</h3>
            <p class="pillar-text">{p.desc}</p>
            <a href={p.link.href} class="pillar-link">{p.link.label}</a>
          </div>
        </div>
      {/each}

    </div>
  </section>

  <section class="closing">
    <div class="closing-inner">
      <h2>ONE OPERATOR.<br />TOTAL AUTHORITY.</h2>
      <p>The Sovren Stack is unified sovereign infrastructure built on a single commitment: UX, privacy, and security without compromise at every layer. Esver OS is the command center — voice-native, biometric-secured, AI-augmented, declaratively configured. Visage is the identity primitive — your face, verified on your hardware, never leaving it. Mr. Haven is the capital layer — programmable rules, autonomous execution, no custodian. Together they give one operator total authority over compute, identity, and capital.</p>
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
    background: transparent;
    color: var(--text-primary);
    padding: var(--pad-section-lg);
    border-bottom: 1px solid var(--border);
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
    color: var(--text-primary);
  }

  .thesis-body {
    font-size: 0.95rem;
    line-height: var(--lh-loose);
    color: var(--text-secondary);
    letter-spacing: var(--ls-default);
  }

  blockquote {
    border-left: 2px solid var(--text-primary);
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
    background: transparent;
    color: var(--text-primary);
    padding: var(--pad-section-lg);
    border-top: 1px solid var(--border);
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
    color: var(--text-secondary);
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
    background: var(--bg);
    color: var(--text-primary);
    border: 1px solid var(--text-primary);
    text-decoration: none;
    transition: all var(--transition-slow);
    align-self: flex-start;
    margin-top: var(--space-sm);
  }

  .btn-primary:hover {
    background: var(--text-primary);
    color: var(--bg);
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
