<svelte:head>
  <title>Augmentum OS — Sovereign Command Infrastructure | Sovren Software</title>
  <meta name="description" content="Augmentum OS is your command center. Voice-native interface. Biometric-secured access. Local AI co-pilot. UX, privacy, and security — none sacrificed. Ships Summer 2026." />
  <link rel="canonical" href="https://sovren.software/augmentum" />
  <link rel="stylesheet" href="https://sibforms.com/forms/end-form/build/sib-styles.css" />
  <script>
    window.REQUIRED_CODE_ERROR_MESSAGE = 'Please choose a country code';
    window.LOCALE = 'en';
    window.EMAIL_INVALID_MESSAGE = window.SMS_INVALID_MESSAGE = "The information provided is invalid. Please review the field format and try again.";
    window.REQUIRED_ERROR_MESSAGE = "This field cannot be left blank.";
    window.GENERIC_INVALID_MESSAGE = "The information provided is invalid. Please review the field format and try again.";
    window.translation = { common: { selectedList: '{quantity} list selected', selectedLists: '{quantity} lists selected', selectedOption: '{quantity} selected', selectedOptions: '{quantity} selected' } };
    var AUTOHIDE = Boolean(0);
  </script>
  <script defer src="https://sibforms.com/forms/end-form/build/main.js"></script>
  <meta property="og:title" content="Augmentum OS — One Operator. Total Authority." />
  <meta property="og:description" content="Voice-native command interface. Biometric-secured sessions. Local AI co-pilot. UX, privacy, and security — none sacrificed. Sovereign infrastructure for high-leverage operators." />
  <meta property="og:url" content="https://sovren.software/augmentum" />
  <meta name="twitter:title" content="Augmentum OS — One Operator. Total Authority." />
  <meta name="twitter:description" content="Voice-native command interface. Biometric-secured sessions. Local AI co-pilot. UX, privacy, and security — none sacrificed. Sovereign infrastructure for high-leverage operators." />
</svelte:head>

<script>
  import ProductHero from '$lib/ProductHero.svelte';
  import Overview from '$lib/Overview.svelte';
  import PillarList from '$lib/PillarList.svelte';
  import CtaSection from '$lib/CtaSection.svelte';
  import { AUGMENTUM_SIGNUP_URL } from '$lib/marketing';

  const pillars = [
    {
      num: '01',
      label: 'COMMAND THE MACHINE. DON\'T NEGOTIATE WITH IT.',
      desc: 'You are the operator. The system is the co-pilot. Issue commands by voice, query your environment in natural language, trigger workflows — the interface adapts to how you think. Local inference runs by default. Cloud inference is available when you choose it. Nothing leaves your machine without explicit authorization.',
    },
    {
      num: '02',
      label: 'PRIVACY IS WHAT MAKES REAL CAPABILITY POSSIBLE.',
      desc: 'A system that phones home is not a command center. It is a managed endpoint. Local inference is the default — no telemetry collected by us. Your operational data belongs to you. Intelligence without surveillance is the design.',
    },
    {
      num: '03',
      label: 'SECURITY IS THE PERIMETER OF YOUR AUTHORITY.',
      desc: 'Access is governed by biometric authentication — Visage at the OS level, not a plugin. Face verification runs on-device via ONNX inference. Your biometrics never leave your hardware. Sessions are scoped. Privileges are gated. Every elevated action requires explicit authorization. Weak auth is a hole in your perimeter. Augmentum does not have one.',
    },
    {
      num: '04',
      label: 'THE STACK IS YOURS. FULLY AND WITHOUT EXCEPTION.',
      desc: 'The entire OS state lives in one reproducible config — version-controlled, auditable, rollback-capable. No silent updates. No unauthorized background processes. Clone your machine to new hardware in minutes. Every package, service, and setting answers to your config file. If you did not write it, it does not run.',
    },
  ]

  const specs = [
    { label: 'BASE', value: 'NixOS — declarative, version-controlled, rollback-capable' },
    { label: 'INTERFACE', value: 'Voice-native · Natural language command layer · Local inference' },
    { label: 'AUTHENTICATION', value: 'Biometric (Visage) · MFA · Session-scoped privileges' },
    { label: 'AI LAYER', value: 'Local-first by default · Optional cloud inference · Your telemetry, your data' },
    { label: 'ORCHESTRATION', value: 'Programmable automation · Explicit agent authority boundaries' },
    { label: 'STATUS', value: 'Ships Summer 2026', dim: true },
  ]
</script>

<main>
  <ProductHero
    category="01 / OS"
    title="AUGMENTUM<br />OS."
    status="Ships Summer 2026"
    tagline="One operator. Total authority. UX, privacy, and security — none sacrificed."
  />

  <Overview
    lead="Your command center. Built without compromise."
    {specs}
    stackNote="<a href='/visage'>Visage</a> biometric authentication runs as a native OS primitive — not an app, not a plugin, not a third-party service. <a href='/mrhaven'>Mr. Haven</a> programmable asset control is wired directly into the operator layer. The full Sovren Stack is unified sovereign infrastructure."
  >
    <p>Most operating systems serve the vendor. They harvest telemetry, push updates on their schedule, and treat your machine as a managed endpoint. Augmentum OS is built on the opposite premise.</p>
    <p>The interface is voice-native — speak a command, the system responds, local inference by default with optional cloud when you need it. Access is biometric — your face, verified on-device, governs your sessions. The AI co-pilot surfaces context and executes tasks inside boundaries you define; your operational data stays yours. The entire OS is one declarative config — version-controlled, reproducible, rollback-capable.</p>
    <p>UX, privacy, and security do not trade off against each other. Each one reinforces the others. That is the engineering commitment.</p>
  </Overview>

  <PillarList {pillars} />

  <section class="launch-briefing" id="launch-briefing">
    <div class="launch-inner preserve-3d">
      <h2 class="glitch-subtle">GET THE<br />LAUNCH BRIEFING.</h2>
      <p>
        One operational briefing when Augmentum OS goes live, then occasional high-signal updates across the
        sovereign stack.
      </p>

      <div class="brevo-form-wrap">
        <div id="sib-form-container" class="sib-form-container">
          <div id="error-message" class="sib-form-message-panel brevo-msg brevo-msg--error">
            <div class="sib-form-message-panel__text sib-form-message-panel__text--center">
              <span class="sib-form-message-panel__inner-text">Your subscription could not be saved. Please try again.</span>
            </div>
          </div>
          <div id="success-message" class="sib-form-message-panel brevo-msg brevo-msg--success">
            <div class="sib-form-message-panel__text sib-form-message-panel__text--center">
              <span class="sib-form-message-panel__inner-text">Confirmed. You will receive the launch briefing.</span>
            </div>
          </div>
          <form id="sib-form" method="POST" action="https://f4c90f0b.sibforms.com/serve/MUIFAAbBH-WyHvhepdhs6G8ul1wze6MjoVvTKJ8hy6wQ2pt2zfKhS72lm7K5SfgHHreybw_QGra18wfbFENLUX33U10YYUe1aPoQOEePElxdHbiM2uGL0Sdsei-N34xBCkoktWbqbtQe1cMW95PLNJ4gd9cZ_YonM0j3W1TrUXhliIJyTXuJ7u4B8pL9aH8uFVKQbzNfUWpWw_ovuA==" data-type="subscription" class="brevo-form">
            <div class="brevo-field-row">
              <input class="brevo-input" type="text" id="EMAIL" name="EMAIL" autocomplete="off" placeholder="YOUR EMAIL ADDRESS" data-required="true" required />
              <button class="btn-primary brevo-submit" form="sib-form" type="submit">SUBSCRIBE →</button>
            </div>
            <div class="entry__error entry__error--primary brevo-error-label" aria-live="polite"></div>
            <input type="text" name="email_address_check" value="" class="input--hidden" style="display:none" />
            <input type="hidden" name="locale" value="en" />
          </form>
        </div>
      </div>

      <p class="launch-note">Double opt-in enabled. Unsubscribe anytime.</p>
    </div>
  </section>

  <CtaSection
    title="BUILD SOVEREIGNLY."
    body="Augmentum OS, Visage, and MrHaven are designed as one command layer. Read the operating thesis behind the stack."
    actions={[
      { label: 'READ THE MANIFESTO →', href: '/ecosystem' },
      { label: 'EXPLORE VISAGE →', href: '/visage', style: 'secondary' },
    ]}
  />
</main>

<style>
  .launch-briefing {
    background: transparent;
    color: var(--text-primary);
    padding: var(--pad-section-lg);
    border-top: 1px solid var(--border);
    position: relative;
    scroll-margin-top: calc(var(--nav-h) + var(--space-xl));
  }

  .launch-inner {
    max-width: var(--max-w);
    margin: 0 auto;
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

  .brevo-form-wrap {
    max-width: 560px;
  }

  .brevo-form {
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
    border: 1px solid var(--border);
    color: var(--text-primary);
    font-family: var(--font-mono);
    font-size: var(--fs-body-sm);
    letter-spacing: var(--ls-wider);
    padding: 0.75rem 1rem;
    outline: none;
    transition: border-color 0.15s;
  }

  .brevo-input::placeholder {
    color: var(--text-muted);
  }

  .brevo-input:focus {
    border-color: var(--text-primary);
  }

  .brevo-submit {
    white-space: nowrap;
  }

  .brevo-error-label {
    font-size: var(--fs-body-xs);
    color: var(--text-secondary);
    font-family: var(--font-mono);
    min-height: 1.2em;
  }

  .brevo-msg {
    display: none;
    padding: var(--space-sm) var(--space-md);
    font-family: var(--font-mono);
    font-size: var(--fs-body-sm);
    letter-spacing: var(--ls-default);
    border: 1px solid var(--border);
  }

  .brevo-msg--error {
    color: var(--text-secondary);
    border-color: var(--border);
  }

  .brevo-msg--success {
    color: var(--text-primary);
    border-color: var(--text-primary);
  }

  @media (max-width: 768px) {
    .launch-briefing {
      padding: var(--space-5xl) var(--space-xl);
    }

    .brevo-field-row {
      flex-direction: column;
    }

    .brevo-submit {
      width: 100%;
    }
  }
</style>
