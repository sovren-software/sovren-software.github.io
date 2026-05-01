<svelte:head>
  <title>The Codex — Sovren Stack Doctrine | Sovren Software</title>
  <meta name="description" content="The doctrine behind Sovren Software: verified work, local identity, programmable capital, and customer-owned infrastructure for reliable agents." />
  <link rel="canonical" href="https://sovren.software/ecosystem" />
  <meta property="og:title" content="The Sovren Codex. Own the work agents run." />
  <meta property="og:description" content="Verified workflows, local identity, programmable capital, and customer-owned control." />
  <meta property="og:url" content="https://sovren.software/ecosystem" />
  <meta name="twitter:title" content="The Sovren Codex. Own the work agents run." />
  <meta name="twitter:description" content="Verified workflows, local identity, programmable capital, and customer-owned control." />
</svelte:head>

<script>
  import TrifectaDiagram from '$lib/TrifectaDiagram.svelte';
  import HeroGlyph from '$lib/HeroGlyph.svelte';
  import Icon from '$lib/Icon.svelte';
  import { reveal } from '$lib/reveal.js';

  const pillars = [
    {
      num: '01',
      domain: 'COMPUTING',
      icon: 'compute',
      title: 'THE MACHINE IS WHERE VERIFIED WORK RUNS.',
      desc: 'Esver OS turns repeated company workflows into verified executable skills that agents can run under customer-owned control. The core unit is not a chat thread. It is a skill: a workflow with context, boundaries, evidence gates, and a repeatable execution path on local or customer-controlled infrastructure.',
      link: { label: 'ESVER OS →', href: '/esver' }
    },
    {
      num: '02',
      domain: 'IDENTITY',
      icon: 'identity',
      title: 'YOU ARE NOT A ROW IN A DATABASE.',
      desc: 'Biometrics should never leave the hardware they were captured on. Verification is a local cryptographic process, not a cloud API call. If a system requires your face to authenticate, it must prove it cannot steal it.',
      link: { label: 'VISAGE →', href: '/visage' }
    },
    {
      num: '03',
      domain: 'CAPITAL',
      icon: 'capital',
      title: 'NO HUMANS IN THE LOOP.',
      desc: 'Assets require custody or cryptography. We choose cryptography. A programmable vault should execute rules without hesitation, without exception, and without permission from a compliance department.',
      link: { label: 'MR. HAVEN →', href: '/mrhaven' }
    }
  ]
</script>

<main>
  <section class="hero">
    <div class="hero-split">
      <div class="hero-frame panel--strong">
        <span class="category">DOCTRINE</span>
        <div class="category-rule"></div>
        <h1>THE CODEX.</h1>
        <p class="tagline">We reject the premise that extraction is the default state of technology.</p>
      </div>
      <div class="hero-glyph">
        <HeroGlyph id="codex" />
      </div>
    </div>
  </section>

  <section class="thesis-expanded">
    <div class="thesis-inner panel">
      <p class="thesis-lede">The industry convinced you that convenience requires compromise. That good UX means accepting telemetry. That strong security means sacrificing usability. That privacy is a premium feature. None of that is true. It is just what the vendor model requires.</p>

      <div class="thesis-body">
        <p>Your operating system is a managed endpoint in someone else's deployment. Your identity lives in a database you do not control. Your assets are held by institutions that decide when you can access them. At every layer of the stack, a vendor inserted themselves between you and your own infrastructure — and called it a service.</p>

        <blockquote>You are not the root user of your own life. You are a tenant. Sovren Software exists to change that.</blockquote>

        <p>We build infrastructure for work, identity, and assets that should stay under owner control. The work layer turns repeated company workflows into verified executable skills. The identity layer keeps authentication local to the machine. The capital layer makes asset rules programmable without a custodian. The stack is sovereign because control lives with the owner, not with the vendor running the service.</p>
      </div>

      <div class="trifecta-vis reveal" use:reveal>
        <span class="panel-header">// THE TRIFECTA</span>
        <TrifectaDiagram />
      </div>
    </div>
  </section>

  <section class="pillars">
    <div class="pillars-inner">
      <span class="section-label">// THE THREE PILLARS</span>

      {#each pillars as p}
        <div class="pillar panel reveal" use:reveal>
          <div class="pillar-header">
            <span class="pillar-n">{p.num}</span>
            <span class="pillar-icon"><Icon name={p.icon} size={24} /></span>
            <span class="pillar-domain tag--accent">{p.domain}</span>
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
    <div class="closing-inner panel--strong reveal" use:reveal>
      <h2>OWN THE WORK<br />AGENTS RUN.</h2>
      <p>The Sovren Stack is customer-owned infrastructure for reliable agentic work. Esver OS turns repeated workflows into verified executable skills. Visage keeps identity local to the machine. Mr. Haven makes capital follow programmable rules without a custodian. Together they move control of work, identity, and assets back to the owner.</p>
      <a href="/" class="btn-peak">EXPLORE THE STACK →</a>
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
    border-bottom: var(--panel-border-strong);
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
    border: var(--panel-border-strong);
    padding: var(--panel-pad);
    background: var(--bg);
  }

  .category {
    display: block;
    font-size: var(--fs-label);
    letter-spacing: var(--ls-ultra);
    color: var(--text-muted);
    margin-bottom: var(--space-lg);
    text-transform: uppercase;
  }

  .category-rule {
    height: 1px;
    background: var(--border);
    margin-bottom: var(--space-2xl);
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
    background: var(--bg);
    color: var(--text-primary);
    padding: var(--pad-section-lg);
    border-bottom: var(--panel-border);
  }

  .thesis-inner {
    max-width: var(--max-w-prose);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: var(--space-2xl);
    border: var(--panel-border);
    padding: var(--panel-pad);
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

  .trifecta-vis {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--space-2xl);
    padding-top: var(--space-2xl);
    border-top: var(--panel-border);
  }

  blockquote {
    border-left: 3px solid var(--accent);
    padding: var(--space-lg) var(--space-2xl);
    margin: var(--space-lg) 0;
    font-size: clamp(1rem, 2vw, 1.25rem);
    font-weight: var(--fw-semibold);
    line-height: 1.7;
    letter-spacing: 0.01em;
    background: var(--accent-surface);
  }

  /* Pillars */
  .pillars {
    padding: var(--pad-section);
    border-top: var(--panel-border);
    background: var(--bg);
  }

  .pillars-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: var(--space-lg);
  }

  .section-label {
    display: block;
    font-size: var(--fs-label-sm);
    letter-spacing: var(--ls-ultra);
    color: var(--text-ghost);
    margin-bottom: var(--space-3xl);
    text-transform: uppercase;
  }

  .pillar {
    display: grid;
    grid-template-columns: 200px 1fr;
    gap: var(--space-5xl);
    padding: var(--space-3xl) var(--panel-pad);
    border: var(--panel-border);
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
    color: var(--accent);
  }

  .pillar-icon {
    color: var(--accent);
    opacity: 0.5;
  }

  .pillar-domain {
    font-size: var(--fs-btn);
    font-weight: var(--fw-bold);
    letter-spacing: 0.16em;
    color: var(--accent);
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
    color: var(--accent);
  }

  /* Closing */
  .closing {
    background: var(--bg);
    color: var(--text-primary);
    padding: var(--pad-section-lg);
    border-top: var(--panel-border);
  }

  .closing-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: var(--space-xl);
    border: var(--panel-border-strong);
    padding: var(--panel-pad);
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

  /* Responsive */
  @media (max-width: 768px) {
    .hero {
      padding: var(--space-4xl) var(--space-xl);
    }

    .hero-split {
      grid-template-columns: 1fr;
    }

    .hero-glyph {
      order: -1;
    }

    .hero-frame {
      padding: var(--space-xl);
    }

    h1 {
      font-size: clamp(3.5rem, 18vw, 6rem);
    }

    .pillar {
      grid-template-columns: 1fr;
      gap: var(--space-xl);
      padding: var(--space-xl);
    }

    .thesis-inner {
      padding: var(--space-xl);
    }

    .closing-inner {
      padding: var(--space-xl);
    }
  }
</style>
