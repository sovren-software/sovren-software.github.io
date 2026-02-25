<svelte:head>
  <title>Augmentum OS — A Cognitive Operating System for High-Leverage Operators | Sovren Software</title>
  <meta name="description" content="One operator. Team-scale output. Augmentum OS is a cognitive operating system that watches, learns, and surfaces what matters — without compromising on privacy, security, or usability." />
  <meta property="og:title" content="Augmentum OS — One Operator. Team-Scale Output." />
  <meta property="og:description" content="A cognitive operating system for founders, operators, and high-leverage individuals. UX, privacy, and security — none sacrificed. Ships Summer 2026." />
  <meta property="og:url" content="https://sovren.software/augmentum" />
</svelte:head>

<script>
  import ProductHero from '$lib/ProductHero.svelte';
  import Overview from '$lib/Overview.svelte';
  import PillarList from '$lib/PillarList.svelte';
  import CtaSection from '$lib/CtaSection.svelte';

  const pillars = [
    {
      num: '01',
      label: 'ALWAYS WATCHING. NEVER LEAKING.',
      desc: 'The OS observes your system continuously and surfaces what matters — using AI that runs entirely on your hardware. Nothing leaves without your explicit permission. You control the privacy dial, and you can change it at any time.',
    },
    {
      num: '02',
      label: 'YOU OWN THE CONSENT',
      desc: 'Every AI feature is gated. You grant access. You revoke it. Session permissions expire when you reboot — so nothing persists without you actively choosing it. Before anything leaves your machine, the system tells you exactly what, and asks.',
    },
    {
      num: '03',
      label: 'EVERY ACTION IS RECEIPTED',
      desc: 'Agents operate within boundaries you define. Every action is logged, signed, and auditable. You can see what happened, when, and why. Control does not end when you delegate — it follows the work.',
    },
    {
      num: '04',
      label: 'SECURE BY DEFAULT. USABLE BY DESIGN.',
      desc: 'The secure path is the easy path. One command to check system status. One command to diagnose a problem. One command to change your privacy posture. Good defaults. No gotchas.',
    },
  ]

  const specs = [
    { label: 'BASE', value: 'NixOS 25.05 (Warbler)' },
    { label: 'CONFIG', value: 'Declarative · Version-controlled · Rollback-capable' },
    { label: 'INFERENCE', value: 'Runs locally · Your data stays on your hardware' },
    { label: 'CONSENT', value: 'Granular · Revocable · Expires on reboot' },
    { label: 'STATUS', value: 'Ships Summer 2026', dim: true },
  ]
</script>

<main>
  <ProductHero
    category="01 / OS"
    title="AUGMENTUM<br />OS."
    status="Ships Summer 2026"
    tagline="One operator. Team-scale output."
  />

  <Overview
    lead="A cognitive operating system."
    {specs}
    stackNote="Visage face authentication and MrHaven programmable finance are first-class primitives at the OS level. The Sovren Stack runs as a unified command layer."
  >
    <p>Most operating systems make you choose: convenience or privacy. Ease of use or security. Augmentum OS does not accept that tradeoff.</p>
    <p>It is built for founders, operators, and high-leverage individuals who need the output of a team — without surrendering control of their own machine. The system watches, learns, and surfaces what matters. You decide what it sees, what it retains, and when it acts. That clarity compounds over time.</p>
  </Overview>

  <PillarList {pillars} />

  <CtaSection
    title="BUILT FOR THE<br />OPERATOR."
    body="Augmentum OS ships Summer 2026. No early access. No waitlist. One email when it is ready — send us your address."
    actions={[{ label: 'NOTIFY ME AT LAUNCH →', href: 'mailto:hello@sovren.software?subject=Augmentum OS Launch Notification' }]}
  />
</main>
