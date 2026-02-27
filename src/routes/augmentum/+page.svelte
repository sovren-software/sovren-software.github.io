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
      desc: 'Augmentum OS is built around a single principle: you are the operator, the system is the co-pilot. Issue commands by voice. Query your environment in natural language. Trigger workflows, interrogate processes, orchestrate tasks — the interface adapts to how you think. The entire command layer runs on local inference. Nothing is transcribed in the cloud. The UX is fast because the system is yours.',
    },
    {
      num: '02',
      label: 'PRIVACY IS WHAT MAKES REAL CAPABILITY POSSIBLE.',
      desc: 'A system that phones home cannot be trusted as a command center. Augmentum\'s AI co-pilot runs entirely on your hardware — no telemetry, no behavioral profiles, no vendor with a copy of your activity. This is not a privacy feature bolted on after the fact. The architecture is local-first because local-first is the only way to give you genuine control. Intelligence without surveillance is not a tradeoff. It is the design.',
    },
    {
      num: '03',
      label: 'SECURITY IS THE PERIMETER OF YOUR AUTHORITY.',
      desc: 'Access to your command infrastructure is governed by biometric authentication — Visage integrated at the OS level as a native primitive, not a plugin. Face verification happens via on-device ONNX inference. Your face never leaves your hardware. Sessions are scoped, privileges are gated, and every elevated action requires explicit authorization. Weak authentication is a hole in your perimeter. Augmentum does not have one.',
    },
    {
      num: '04',
      label: 'THE STACK IS YOURS. FULLY AND WITHOUT EXCEPTION.',
      desc: 'The entire OS state is declared in a single reproducible configuration — version-controlled, auditable, rollback-capable. No silent updates. No background processes you did not authorize. No vendor lock-in. Clone your machine to new hardware in minutes. Every package, service, and setting answers to your config file. If you did not write it, it does not run.',
    },
  ]

  const specs = [
    { label: 'BASE', value: 'NixOS — declarative, version-controlled, rollback-capable' },
    { label: 'INTERFACE', value: 'Voice-native · Natural language command layer · Local inference' },
    { label: 'AUTHENTICATION', value: 'Biometric (Visage) · MFA · Session-scoped privileges' },
    { label: 'AI LAYER', value: 'On-device co-pilot · No telemetry · No cloud dependency' },
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
    <p>Every operating system makes an implicit promise about who it serves. Most serve the vendor: they harvest telemetry, enforce update schedules you did not choose, and treat your machine as a managed endpoint in someone else's deployment. Augmentum OS makes a different promise.</p>
    <p>It is your command center. The interface is voice-native — you speak, the system responds, all inference runs locally. The access layer is biometric — your face, verified on-device, governs your sessions. The AI co-pilot surfaces context and executes tasks inside boundaries you define, with no data leaving the machine. And the entire OS is declarative — one config file, version-controlled, reproducible on any hardware. UX, privacy, and security do not trade off against each other here. Each one reinforces the others. That is the engineering commitment.</p>
  </Overview>

  <PillarList {pillars} />

  <CtaSection
    title="BUILT WITHOUT<br />COMPROMISE."
    body="Augmentum OS ships Summer 2026. One email when it is ready — send us your address."
    actions={[{ label: 'NOTIFY ME AT LAUNCH →', href: 'mailto:hello@sovren.software?subject=Augmentum OS Launch Notification' }]}
  />
</main>
