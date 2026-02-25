<svelte:head>
  <title>Mr. Haven — Non-Custodial USDC Time Vault on Base L2 | Sovren Software</title>
  <meta name="description" content="Programmable non-custodial USDC vault on Base L2. Set conditions, name beneficiaries, designate autonomous agents. No custodian. No intermediary. Live on mainnet." />
  <meta property="og:title" content="Mr. Haven — Your Assets. Your Rules." />
  <meta property="og:description" content="Programmable asset control for humans and autonomous agents. Your keys, your conditions, your beneficiaries. Smart contract only. SDK coming soon." />
  <meta property="og:url" content="https://sovren.software/mrhaven" />
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
      desc: 'Deposit USDC into a smart contract. Set a time-based schedule, an unlock date, or a recurring release. The contract enforces the rules — no humans in the loop, no approval required.',
    },
    {
      num: '02',
      label: 'IF YOU GO DARK, IT STILL EXECUTES.',
      desc: 'Set an inactivity threshold: if you go offline for X days, funds transfer automatically. An on-chain dead man\'s switch for the assets that matter most.',
    },
    {
      num: '03',
      label: 'BUILT FOR AGENTS, NOT JUST HUMANS.',
      desc: 'Autonomous agents can hold funds, trigger transfers, and execute plans with the same non-custodial guarantees as any human user. No API key. No service account. The contract enforces the rules regardless of who calls it.',
    },
    {
      num: '04',
      label: 'SDK — COMING SOON.',
      desc: 'A developer SDK for integrating MrHaven vaults directly into applications and autonomous agent workflows. Programmatic vault creation, condition setting, and beneficiary management without touching the UI.',
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
  />

  <Overview
    lead="Your assets. Your rules. No one else in the room."
    {specs}
    stackNote="Integrates with Augmentum OS as part of the Sovren Stack — programmable finance at the OS level."
  >
    <p>Traditional financial institutions hold your assets on your behalf. They decide when you can access them, who can receive them, and under what conditions. MrHaven removes them from the equation entirely.</p>
    <p>Deployed on Base L2, MrHaven is a set of auditable smart contracts. Deposit USDC, define conditions, name beneficiaries — or designate autonomous agents as authorized recipients. The contract handles execution: autonomously, verifiably, permanently.</p>
  </Overview>

  <PillarList {pillars} />

  <CtaSection
    title="YOUR ASSETS.<br />YOUR RULES."
    body="MrHaven is live on Base mainnet. Connect a wallet and set up your first vault in minutes."
    actions={[{ label: 'LAUNCH APP →', href: 'https://mrhaven.io', external: true }]}
  />
</main>
