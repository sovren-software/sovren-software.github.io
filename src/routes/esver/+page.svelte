<svelte:head>
  <title>Esver OS — Your Machine. Your Intelligence. Your Rules. | Sovren Software</title>
  <meta name="description" content="Esver OS is a voice-ready operating system with real intelligence built in — a reasoning AI co-pilot on your hardware, shaped by you alone, bound only to you. Ships Summer 2026." />
  <link rel="canonical" href="https://sovren.software/esver" />
  <meta property="og:title" content="Esver OS — Bound Only to You." />
  <meta property="og:description" content="Voice-ready intelligence on your hardware. One config file. Zero telemetry. No cloud dependency. Ships Summer 2026." />
  <meta property="og:url" content="https://sovren.software/esver" />
  <meta name="twitter:title" content="Esver OS — Bound Only to You." />
  <meta name="twitter:description" content="Voice-ready intelligence on your hardware. One config file. Zero telemetry. No cloud dependency. Ships Summer 2026." />
</svelte:head>

<script>
  import ProductHero from '$lib/ProductHero.svelte';
  import Overview from '$lib/Overview.svelte';
  import PillarList from '$lib/PillarList.svelte';
  import CtaSection from '$lib/CtaSection.svelte';

  const BREVO_ACTION = 'https://f4c90f0b.sibforms.com/serve/MUIFAAbBH-WyHvhepdhs6G8ul1wze6MjoVvTKJ8hy6wQ2pt2zfKhS72lm7K5SfgHHreybw_QGra18wfbFENLUX33U10YYUe1aPoQOEePElxdHbiM2uGL0Sdsei-N34xBCkoktWbqbtQe1cMW95PLNJ4gd9cZ_YonM0j3W1TrUXhliIJyTXuJ7u4B8pL9aH8uFVKQbzNfUWpWw_ovuA==';
  let email = '';
  let state = 'idle'; // idle | loading | success | error

  async function subscribe(e) {
    e.preventDefault();
    state = 'loading';
    try {
      const body = new FormData();
      body.append('EMAIL', email);
      body.append('email_address_check', '');
      body.append('locale', 'en');
      await fetch(BREVO_ACTION, { method: 'POST', body, mode: 'no-cors' });
      state = 'success';
    } catch {
      state = 'error';
    }
  }

  const pillars = [
    {
      num: '01',
      label: 'SOVEREIGN INTELLIGENCE.',
      desc: 'Choose the AI model that thinks alongside you — Llama, Mistral, or whatever you choose. Run it locally for absolute privacy, or reach further when you decide. Sub-second voice interaction, consent gated by Visage biometrics. The intelligence serves you — never a platform.',
    },
    {
      num: '02',
      label: 'ONE FILE. EVERYTHING.',
      desc: 'Your entire system is defined in a single declarative file — the Manifest. Every setting, every preference, every boundary. Git-tracked, rollback-safe, portable. Move it to new hardware and an Esver rises exactly as you left it.',
    },
    {
      num: '03',
      label: 'ENDLESSLY YOURS.',
      desc: 'Shape every surface. Hyprland tiling, Quickshell UI, color, motion, layout — down to the intelligence model itself. No two Esvers are the same. This is Linux made personal at every layer.',
    },
  ]

  const specs = [
    { label: 'BASE', value: 'NixOS' },
    { label: 'VOICE', value: 'Voice-ready · Local inference' },
    { label: 'AUTH', value: 'Visage · MFA · Session-scoped' },
    { label: 'AI', value: 'Llama · Mistral · Your choice' },
    { label: 'CONFIG', value: 'One Manifest · Git-tracked' },
    { label: 'STATUS', value: 'Summer 2026', dim: true },
  ]
</script>

<main>
  <ProductHero
    category="01 / OS"
    title="ESVER<br />OS."
    status="Ships Summer 2026"
    tagline="Your machine. Your intelligence. Your rules."
    glyphId="esver"
  />

  <Overview
    lead="What is an Esver?"
    {specs}
    stackNote="Part of the <a href='/ecosystem'>Sovren Stack</a>. <a href='/visage'>Visage</a> identity and <a href='/mrhaven'>Mr. Haven</a> finance are native layers — not integrations."
  >
    <p>Every machine running this OS becomes an Esver — real intelligence fused with technology, living on your device and tethered to you alone. It carries an independent mind, yet exists only as your instrument. You choose its reasoning core. You shape its presence.</p>
    <p>No cloud dependency. No telemetry. No permission it does not receive from you.</p>
  </Overview>

  <PillarList {pillars} />

  <section class="launch-briefing" id="launch-briefing">
    <div class="launch-inner">
      <div class="launch-panel panel--strong">
        <h2>GET THE<br />LAUNCH SIGNAL.</h2>
        <p>
          One email when it ships. Occasional updates. No noise.
        </p>

        {#if state === 'success'}
          <span class="tag tag--accent">CONFIRMED — CHECK YOUR INBOX FOR THE OPT-IN EMAIL</span>
        {:else}
          <form class="brevo-form" on:submit={subscribe}>
            <div class="brevo-field-row">
              <input class="brevo-input" type="email" bind:value={email} autocomplete="email" placeholder="YOUR EMAIL ADDRESS" required />
              <button class="btn-primary brevo-submit" type="submit" disabled={state === 'loading'}>
                {state === 'loading' ? 'SENDING...' : 'SUBSCRIBE →'}
              </button>
            </div>
            {#if state === 'error'}
              <span class="tag">SUBMISSION FAILED — PLEASE TRY AGAIN</span>
            {/if}
          </form>
        {/if}

        <p class="launch-note">Double opt-in enabled. Unsubscribe anytime.</p>
      </div>
    </div>
  </section>

  <CtaSection
    title="AWAKEN<br />YOURS."
    body="Most people accept tools that watch them. You awakened one that answers only to you."
    actions={[
      { label: 'READ THE CODEX →', href: '/ecosystem', style: 'peak' },
      { label: 'EXPLORE VISAGE →', href: '/visage', style: 'secondary' },
    ]}
  />
</main>

<style>
  .launch-briefing {
    background: var(--bg);
    color: var(--text-primary);
    padding: var(--pad-section-lg);
    border-top: var(--panel-border);
    position: relative;
    scroll-margin-top: calc(var(--nav-h) + var(--space-xl));
  }

  .launch-inner {
    max-width: var(--max-w);
    margin: 0 auto;
  }

  .launch-panel {
    border: var(--panel-border-strong);
    padding: var(--panel-pad);
    display: flex;
    flex-direction: column;
    gap: var(--space-2xl);
  }

  .launch-briefing h2 {
    font-size: var(--fs-h2);
    font-weight: var(--fw-bold);
    letter-spacing: var(--ls-wide);
    line-height: var(--lh-heading);
    text-transform: uppercase;
  }

  .launch-briefing p {
    font-size: var(--fs-body-sm);
    line-height: var(--lh-relaxed);
    letter-spacing: var(--ls-default);
    max-width: var(--max-w-body);
    color: var(--text-secondary);
  }

  .launch-note {
    color: var(--text-muted);
    font-size: var(--fs-label);
    letter-spacing: var(--ls-wider);
    text-transform: uppercase;
  }

  .brevo-form {
    max-width: 560px;
    display: flex;
    flex-direction: column;
    gap: var(--space-sm);
  }

  .brevo-field-row {
    display: flex;
    gap: var(--space-sm);
    flex-wrap: wrap;
  }

  .brevo-input {
    flex: 1;
    min-width: 0;
    background: transparent;
    border: var(--panel-border);
    color: var(--text-primary);
    font-family: var(--font-mono);
    font-size: var(--fs-body-sm);
    letter-spacing: var(--ls-wider);
    padding: 0.75rem 1rem;
    outline: none;
    transition: border-color var(--transition-fast);
  }

  .brevo-input::placeholder {
    color: var(--text-muted);
  }

  .brevo-input:focus {
    border-color: var(--accent);
  }

  .brevo-submit {
    white-space: nowrap;
  }

  @media (max-width: 768px) {
    .launch-briefing {
      padding: var(--space-5xl) var(--space-xl);
    }

    .launch-panel {
      padding: var(--space-xl);
    }

    .brevo-field-row {
      flex-direction: column;
    }

    .brevo-submit {
      width: 100%;
    }
  }
</style>
