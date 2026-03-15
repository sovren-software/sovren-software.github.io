<svelte:head>
  <title>Visage — Linux Face Authentication via PAM | Sovren Software</title>
  <meta name="description" content="Open source Linux face authentication via PAM. Inference runs on-device — no cloud enrollment, no biometric database. Rust. MIT licensed. v0.2.0." />
  <link rel="canonical" href="https://sovren.software/visage" />
  <meta property="og:title" content="Visage — Your Face Is Your Key." />
  <meta property="og:description" content="Linux face authentication that runs entirely on your hardware. No cloud enrollment. No biometric database. Open source, MIT licensed." />
  <meta property="og:url" content="https://sovren.software/visage" />
  <meta name="twitter:title" content="Visage — Your Face Is Your Key." />
  <meta name="twitter:description" content="Linux face authentication that runs entirely on your hardware. No cloud enrollment. No biometric database. Open source, MIT licensed." />
</svelte:head>

<script>
  import ProductHero from '$lib/ProductHero.svelte';
  import Overview from '$lib/Overview.svelte';
  import PillarList from '$lib/PillarList.svelte';
  import CtaSection from '$lib/CtaSection.svelte';

  const pillars = [
    {
      num: '01',
      label: 'YOUR BIOMETRICS STAY ON YOUR HARDWARE.',
      desc: 'Face recognition runs entirely on-device. No cloud enrollment. No biometric database. Your face never leaves your machine — not during setup, not during auth, not ever.',
    },
    {
      num: '02',
      label: 'DROPS INTO ANY LINUX AUTH STACK.',
      desc: 'Visage is a PAM module. Drop it into sudo, screen lock, or login without touching your existing config. If your system supports PAM, Visage works.',
    },
    {
      num: '03',
      label: 'BUILT FOR IR. RESISTANT TO SPOOFING.',
      desc: 'Native support for Windows Hello-compatible IR cameras. Liveness detection is built in. Works in low light. A photo does not unlock your machine.',
    },
    {
      num: '04',
      label: 'UNDER ONE SECOND.',
      desc: 'The persistent daemon keeps the model resident in memory. No cold start on every auth. Authentication completes before your hand leaves the trackpad.',
    },
  ]

  const specs = [
    { label: 'LANGUAGE', value: 'Rust' },
    { label: 'INFERENCE', value: 'On-device · No cloud' },
    { label: 'AUTH', value: 'PAM module' },
    { label: 'CAMERA', value: 'RGB + IR · V4L2' },
    { label: 'LICENSE', value: 'MIT · Open source' },
    { label: 'STATUS', value: 'Live · v0.2.0' },
  ]
</script>

<main>
  <ProductHero
    category="02 / IDENTITY"
    title="VISAGE."
    status="Open source · MIT"
    tagline="Your face is your key. Processed locally. Never broadcast to the cloud."
    size="large"
    glyphId="visage"
  />

  <Overview
    lead="Your face is your key — processed locally, never broadcast."
    {specs}
    stackNote="Visage ships as a native identity primitive in <a href='/esver'>Esver OS</a>. It also integrates with <a href='/mrhaven'>Mr. Haven</a> for biometric-gated asset access."
  >
    <p>Windows Hello has worked on Windows for years. Linux users were left out. Visage closes that gap — open-source, built in Rust, no external dependencies, no data leaving your hardware.</p>
    <p>The current release is MIT-licensed and runs on any PAM-compatible Linux system. The next version integrates natively into Esver OS — your face-verified credential becomes a system-level primitive, not a PAM module bolted on from outside.</p>
  </Overview>

  <PillarList {pillars} />

  <CtaSection
    title="OPEN SOURCE.<br />AUDIT IT."
    body="Visage is MIT-licensed and fully open. Read the code, fork it, contribute. Security through obscurity is not security."
    actions={[
      { label: 'VIEW ON GITHUB →', href: 'https://github.com/sovren-software/visage', external: true },
      { label: 'RELEASES', href: 'https://github.com/sovren-software/visage/releases', style: 'secondary', external: true },
    ]}
  />
</main>
