<svelte:head>
  <title>Augmentum OS — Sovereign Command Infrastructure | Sovren Software</title>
  <meta name="description" content="Augmentum OS is your command center. Voice-native interface. Biometric-secured access. Local AI co-pilot. UX, privacy, and security — none sacrificed. Ships Summer 2026." />
  <link rel="canonical" href="https://sovren.software/augmentum" />
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

  <CtaSection
    title="BUILT WITHOUT<br />COMPROMISE."
    body="Augmentum OS ships Summer 2026. One email when it is ready — send us your address."
    actions={[{ label: 'NOTIFY ME AT LAUNCH →', href: 'mailto:hello@sovren.software?subject=Augmentum OS Launch Notification' }]}
  />
</main>
