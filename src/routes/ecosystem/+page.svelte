<svelte:head>
  <title>Ecosystem Manifesto — The Sovren Stack | Sovren Software</title>
  <meta name="description" content="Privacy is not a feature. Control is not an option. Sovereignty is the baseline. The manifesto for the Sovren Software computing stack." />
  <meta property="og:title" content="The Sovren Ecosystem Manifesto." />
  <meta property="og:description" content="We build tools for those who want more of themselves — more capacity, more control, more surface area. The stack is open, inspectable, and answerable only to you." />
  <meta property="og:url" content="https://sovren.software/ecosystem" />
</svelte:head>

<script>
  import CtaSection from '$lib/CtaSection.svelte';

  const pillars = [
    {
      num: '01',
      domain: 'COMPUTING',
      title: 'THE MACHINE MUST BE OBEDIENT.',
      desc: 'An operating system should do exactly what it is told, and nothing else. No telemetry, no silent updates, no background tasks you cannot kill. Your hardware is your property. The software running on it must behave like a tool, not a tenant.',
      link: { label: 'AUGMENTUM OS →', href: '/augmentum' }
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
      <p class="thesis-lede">The industry has accepted a tradeoff that was never necessary: surrender your data, your attention, and your agency in exchange for convenience.</p>
      
      <div class="thesis-body">
        <p>The modern software stack treats the user as the product. Operating systems harvest telemetry. Identity providers silo your biometrics in the cloud. Financial institutions gatekeep your assets.</p>
        
        <blockquote>You are not the root user of your own life. You are a guest in someone else's walled garden.</blockquote>
        
        <p>Sovren Software exists to build the alternative. We do not believe in walled gardens. We do not believe in "trusted third parties." We believe in cryptographic guarantees, open-source foundations, and software that answers only to the person running it.</p>
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
