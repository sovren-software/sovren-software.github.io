<svelte:head>
  <title>Esver OS — Make Company Work Executable | Sovren Software</title>
  <meta name="description" content="Esver OS turns repeated company workflows into verified executable skills that agents can run on local or customer-controlled infrastructure." />
  <link rel="canonical" href="https://sovren.software/esver" />
  <meta property="og:title" content="Esver OS — Make company work executable." />
  <meta property="og:description" content="Turn repeated workflows into verified skills agents can run reliably under customer-owned control." />
  <meta property="og:url" content="https://sovren.software/esver" />
  <meta name="twitter:title" content="Esver OS — Make company work executable." />
  <meta name="twitter:description" content="Turn repeated workflows into verified skills agents can run reliably under customer-owned control." />
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
      label: 'CAPTURE THE WORKFLOW.',
      desc: 'Start with work people already repeat: research, filings, support checks, reviews, reports, ops routines. Esver records the tools, context, decisions, and evidence that make the workflow succeed.',
    },
    {
      num: '02',
      label: 'VERIFY THE SKILL.',
      desc: 'A workflow becomes a skill only when it has boundaries, answer gates, evidence checks, and a repeatable path. The goal is not a flashy demo. The goal is work an agent can rerun without improvising past controls.',
    },
    {
      num: '03',
      label: 'RUN IT UNDER YOUR CONTROL.',
      desc: 'Skills run on local or customer-controlled infrastructure, inside authority boundaries you define. Human approval, audit trails, local memory, and rollback are part of the operating layer — not afterthoughts.',
    },
  ];

  const specs = [
    { label: 'PRODUCT', value: 'Governed AI workspace' },
    { label: 'UNIT', value: 'Verified executable skills' },
    { label: 'RUNTIME', value: 'Local · Customer-controlled' },
    { label: 'CONTROL', value: 'Human-approved authority' },
    { label: 'MEMORY', value: 'Workflow history · Evidence' },
    { label: 'STATUS', value: 'Private development', dim: true },
  ];

  const ladder = [
    {
      term: 'TASK',
      meaning: 'One thing someone needs done.',
    },
    {
      term: 'WORKFLOW',
      meaning: 'The repeated path through tools, context, decisions, and checks.',
    },
    {
      term: 'SKILL',
      meaning: 'A verified workflow an agent can execute with evidence gates.',
    },
    {
      term: 'ROLE',
      meaning: 'A set of skills that serves a person, team, or business function.',
    },
  ];
</script>

<main>
  <ProductHero
    category="01 / OS"
    title="ESVER<br />OS."
    status="Private development"
    tagline="Turn repeated workflows into skills agents can run."
    glyphId="esver"
  />

  <Overview
    lead="Make company work executable."
    {specs}
    stackNote="Part of the <a href='/ecosystem'>Sovren Stack</a>. <a href='/visage'>Visage</a> identity and customer-owned runtime control are trust layers for verified agent work."
  >
    <p>Companies do not need another chatbot. They need agents that can do repeated work reliably: the checks, searches, forms, reviews, and operating routines teams run every week.</p>
    <p>Esver OS is the governed workspace and runtime for that work. It captures repeated workflows, turns them into verified executable skills, and runs them under customer-owned authority on local or customer-controlled infrastructure.</p>
    <p>Plainly: teach it how the job is done once, verify the steps, then let agents rerun it safely.</p>
  </Overview>

  <section class="identity" aria-labelledby="identity-heading">
    <div class="identity-inner">
      <div class="identity-panel panel--strong">
        <span class="section-label">// SIMPLE IDENTITY</span>
        <h2 id="identity-heading">Not a chatbot.<br />Not a cloud bot farm.<br />An operating layer for verified work.</h2>
        <p>
          If someone asks what Esver is: Esver OS turns repeated company workflows into verified executable skills that agents can run reliably under customer-owned control.
        </p>
      </div>

      <div class="ladder-panel">
        <div class="panel-header">// PRODUCT LADDER</div>
        {#each ladder as item}
          <div class="ladder-row">
            <span class="ladder-term">{item.term}</span>
            <span class="ladder-meaning">{item.meaning}</span>
          </div>
        {/each}
      </div>
    </div>
  </section>

  <PillarList label="HOW IT WORKS" {pillars} />

  <section class="proof" aria-labelledby="proof-heading">
    <div class="proof-inner panel">
      <span class="section-label">// WHY THIS MATTERS</span>
      <h2 id="proof-heading">AI agents fail when they have to rediscover the job every time.</h2>
      <div class="proof-body">
        <p>Esver treats repeated work as infrastructure. The durable asset is not a prompt. It is the verified workflow: what context was needed, which route worked, which answer was acceptable, what evidence was captured, and where human authority was required.</p>
        <p>That is how a company moves from one-off AI assistance to persistent workflow intelligence — work that gets better, safer, and easier to rerun each time it is performed.</p>
      </div>
    </div>
  </section>

  <section class="launch-briefing" id="launch-briefing">
    <div class="launch-inner">
      <div class="launch-panel panel--strong">
        <h2>GET THE<br />BUILD SIGNAL.</h2>
        <p>
          Product updates as Esver moves from private development toward a launchable customer-owned agent runtime. No noise.
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
    title="BUILD WORK<br />THAT RUNS."
    body="The next OS layer is not a better chat box. It is a reliable way for companies to turn work into governed, executable skills."
    actions={[
      { label: 'READ THE CODEX →', href: '/ecosystem', style: 'peak' },
      { label: 'EXPLORE VISAGE →', href: '/visage', style: 'secondary' },
    ]}
  />
</main>

<style>
  .identity,
  .proof,
  .launch-briefing {
    background: var(--bg);
    color: var(--text-primary);
    padding: var(--pad-section-lg);
    border-top: var(--panel-border);
    position: relative;
  }

  .identity-inner,
  .proof-inner,
  .launch-inner {
    max-width: var(--max-w);
    margin: 0 auto;
  }

  .identity-inner {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: var(--space-4xl);
    align-items: stretch;
  }

  .identity-panel,
  .proof-inner,
  .launch-panel {
    border: var(--panel-border-strong);
    padding: var(--panel-pad);
  }

  .identity-panel {
    display: flex;
    flex-direction: column;
    gap: var(--space-2xl);
  }

  .section-label {
    display: block;
    font-size: var(--fs-label-sm);
    letter-spacing: var(--ls-ultra);
    color: var(--text-ghost);
    text-transform: uppercase;
  }

  .identity h2,
  .proof h2,
  .launch-briefing h2 {
    font-size: var(--fs-h2);
    font-weight: var(--fw-bold);
    letter-spacing: var(--ls-wide);
    line-height: var(--lh-heading);
    text-transform: uppercase;
  }

  .identity p,
  .proof p,
  .launch-briefing p {
    font-size: var(--fs-body-sm);
    line-height: var(--lh-relaxed);
    letter-spacing: var(--ls-default);
    max-width: var(--max-w-body);
    color: var(--text-secondary);
  }

  .ladder-panel {
    border: var(--panel-border-strong);
    display: flex;
    flex-direction: column;
    background: var(--bg);
  }

  .panel-header {
    font-size: var(--fs-label-sm);
    letter-spacing: var(--ls-ultra);
    text-transform: uppercase;
    color: var(--text-muted);
    padding: var(--space-md) var(--space-xl);
    border-bottom: var(--panel-border);
    background: var(--bg-alt);
  }

  .ladder-row {
    display: grid;
    grid-template-columns: 9rem 1fr;
    gap: var(--space-xl);
    padding: var(--space-xl);
    border-bottom: var(--panel-border);
    align-items: start;
  }

  .ladder-row:last-child {
    border-bottom: none;
  }

  .ladder-term {
    color: var(--accent);
    font-size: var(--fs-label-sm);
    letter-spacing: var(--ls-ultra);
    text-transform: uppercase;
  }

  .ladder-meaning {
    color: var(--text-secondary);
    font-size: var(--fs-body-sm);
    line-height: var(--lh-relaxed);
    letter-spacing: var(--ls-default);
  }

  .proof-inner {
    display: grid;
    grid-template-columns: 0.9fr 1.1fr;
    gap: var(--space-4xl);
    align-items: start;
  }

  .proof-body {
    display: flex;
    flex-direction: column;
    gap: var(--space-lg);
  }

  .launch-briefing {
    scroll-margin-top: calc(var(--nav-h) + var(--space-xl));
  }

  .launch-panel {
    display: flex;
    flex-direction: column;
    gap: var(--space-2xl);
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
    .identity,
    .proof,
    .launch-briefing {
      padding: var(--space-5xl) var(--space-xl);
    }

    .identity-inner,
    .proof-inner {
      grid-template-columns: 1fr;
      gap: var(--space-3xl);
    }

    .identity-panel,
    .proof-inner,
    .launch-panel {
      padding: var(--space-xl);
    }

    .ladder-row {
      grid-template-columns: 1fr;
      gap: var(--space-sm);
      padding: var(--space-lg) var(--space-xl);
    }

    .brevo-field-row {
      flex-direction: column;
    }

    .brevo-submit {
      width: 100%;
    }
  }
</style>
