<svelte:head>
  <title>Esver OS — Talk to Your Machine | Sovren Software</title>
  <meta name="description" content="Talk to your OS. It listens, it acts, nothing leaves your machine. Voice-native commands, face unlock, local AI co-pilot, one-file system config. Ships Summer 2026." />
  <link rel="canonical" href="https://sovren.software/esver" />
  <meta property="og:title" content="Esver OS — Talk to Your Machine." />
  <meta property="og:description" content="Voice-native commands. Face unlock. Local AI co-pilot. One config file = your whole OS. No telemetry. No cloud. Ships Summer 2026." />
  <meta property="og:url" content="https://sovren.software/esver" />
  <meta name="twitter:title" content="Esver OS — Talk to Your Machine." />
  <meta name="twitter:description" content="Voice-native commands. Face unlock. Local AI co-pilot. One config file = your whole OS. No telemetry. No cloud. Ships Summer 2026." />
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
      label: 'SPEAK. IT ACTS.',
      desc: 'The interface is voice-native. Local inference. Sub-second. Nothing transcribed in the cloud.',
    },
    {
      num: '02',
      label: 'SECURITY AT EVERY LAYER.',
      desc: 'Biometric identity. Session-scoped privileges. Per-action authorization. Full-stack, not bolted on.',
    },
    {
      num: '03',
      label: 'ONE CONFIG. ENTIRE OS.',
      desc: 'Declarative. Version-controlled. Rollback in seconds. Clone to new hardware in minutes.',
    },
    {
      num: '04',
      label: 'YOUR AI. YOUR DATA.',
      desc: 'Local co-pilot. Zero telemetry. Cloud when you choose it. The default is silence.',
    },
  ]

  const specs = [
    { label: 'BASE', value: 'NixOS' },
    { label: 'VOICE', value: 'Local inference · Sub-second' },
    { label: 'AUTH', value: 'Visage · MFA · Session-scoped' },
    { label: 'AI', value: 'Local-first · Zero telemetry' },
    { label: 'CONFIG', value: 'One file · Git-tracked' },
    { label: 'STATUS', value: 'Summer 2026', dim: true },
  ]
</script>

<main>
  <ProductHero
    category="01 / OS"
    title="ESVER<br />OS."
    status="Ships Summer 2026"
    tagline="Speak. It acts. Nothing leaves the machine."
    glyphId="esver"
  />

  <Overview
    lead="Talk to your machine. It listens."
    {specs}
    stackNote="Part of the <a href='/ecosystem'>Sovren Stack</a>. <a href='/visage'>Visage</a> identity and <a href='/mrhaven'>Mr. Haven</a> finance are native layers — not integrations."
  >
    <p>Say what you need. The system handles the rest — local inference, no round-trip to someone else's server. The architecture underneath is deep, but the surface is simple: speak, and it acts.</p>
    <p>Everything is sovereign by default. Your config, your data, your keys. Nothing phones home. Nothing runs without your authorization.</p>
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
    title="YOUR MACHINE.<br />YOUR RULES."
    body="Esver OS is one layer of a three-layer sovereign stack. Read the thesis."
    actions={[
      { label: 'READ THE CODEX →', href: '/ecosystem' },
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
