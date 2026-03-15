<svelte:head>
  <title>Mr. Haven — Non-Custodial USDC Time Vault on Base L2 | Sovren Software</title>
  <meta name="description" content="Programmable non-custodial USDC vault on Base L2. Set conditions, name beneficiaries, designate autonomous agents. No custodian. No intermediary. Live on mainnet." />
  <link rel="canonical" href="https://sovren.software/mrhaven" />
  <meta property="og:title" content="Mr. Haven — Your Assets. Your Rules." />
  <meta property="og:description" content="Programmable asset control for humans and autonomous agents. Your keys, your conditions, your beneficiaries. Smart contract only. SDK coming soon." />
  <meta property="og:url" content="https://sovren.software/mrhaven" />
  <meta name="twitter:title" content="Mr. Haven — Your Assets. Your Rules." />
  <meta name="twitter:description" content="Programmable asset control for humans and autonomous agents. Your keys, your conditions, your beneficiaries. Smart contract only. SDK coming soon." />
</svelte:head>

<script>
  import ProductHero from '$lib/ProductHero.svelte';
  import Overview from '$lib/Overview.svelte';
  import PillarList from '$lib/PillarList.svelte';
  import CtaSection from '$lib/CtaSection.svelte';

  const pillars = [
    {
      num: '01',
      label: 'LOCK IT. SET THE RULES.',
      desc: 'Deposit USDC. Set a time-based schedule, an unlock date, or a recurring release. The contract enforces the rules — no humans in the loop, no approval required, no exceptions.',
    },
    {
      num: '02',
      label: 'IF YOU GO DARK, IT STILL EXECUTES.',
      desc: 'Set an inactivity threshold. If you go offline for X days, funds transfer automatically to your named beneficiary. An on-chain dead man\'s switch for the assets that matter most.',
    },
    {
      num: '03',
      label: 'BUILT FOR AGENTS, NOT JUST HUMANS.',
      desc: 'Autonomous agents can hold funds, trigger transfers, and execute plans — same non-custodial guarantees as any human. No API key. No service account. The contract enforces rules regardless of who calls it.',
    },
    {
      num: '04',
      label: 'SDK — COMING SOON.',
      desc: 'Programmatic vault creation, condition setting, and beneficiary management — without touching the UI. Direct integration into applications and autonomous agent workflows.',
    },
  ]

  const specs = [
    { label: 'CHAIN', value: 'Base L2 (Coinbase)' },
    { label: 'ASSET', value: 'USDC' },
    { label: 'CUSTODY', value: 'Non-custodial' },
    { label: 'CONTRACT', value: 'Auditable · Open' },
    { label: 'SDK', value: 'Coming soon', dim: true },
    { label: 'STATUS', value: 'Live · Mainnet' },
  ]
</script>

<main>
  <ProductHero
    category="03 / FINANCE"
    title="MR.<br />HAVEN."
    status="Live on Base L2"
    tagline="Programmable asset control for humans and autonomous agents. No custodian, no intermediary, no exceptions."
    size="large"
    glyphId="mrhaven"
  />

  <Overview
    lead="Your assets. Your rules. No one else in the room."
    {specs}
    stackNote="Integrates with <a href='/esver'>Esver OS</a> as part of the Sovren Stack — programmable finance at the OS level. <a href='/visage'>Visage</a> identity is a first-class primitive."
  >
    <p>Traditional institutions hold your assets on your behalf. They decide when you access them, who can receive them, and under what conditions. Mr. Haven removes them from the equation entirely.</p>
    <p>Deposit USDC. Define conditions. Name beneficiaries — or designate autonomous agents as recipients. The contract handles execution: autonomously, verifiably, permanently. No custodian. No intermediary. No exceptions.</p>
  </Overview>

  <PillarList {pillars} />

  <CtaSection
    title="YOUR ASSETS.<br />YOUR RULES."
    body="MrHaven is live on Base mainnet. Connect a wallet and set up your first vault in minutes."
    actions={[{ label: 'LAUNCH APP →', href: 'https://mrhaven.io', external: true }]}
  />
</main>
