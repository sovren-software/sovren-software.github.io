<script>
  /** @type {string} */
  export let label = 'HOW IT WORKS';
  /** @type {Array<{num: string, label: string, desc: string}>} */
  export let pillars = [];
</script>

<section class="pillars">
  <div class="pillars-inner">
    <span class="section-label">// {label}</span>
    <div class="pillar-rows">
      {#each pillars as p}
        <div class="pillar-row panel">
          <div class="pillar-left">
            <span class="pillar-num">{p.num}</span>
            <h3 class="pillar-title">{p.label}</h3>
          </div>
          <p class="pillar-desc">{p.desc}</p>
        </div>
      {/each}
    </div>
  </div>
</section>

<style>
  .pillars {
    padding: var(--pad-section);
    background: var(--bg);
  }

  .pillars-inner {
    max-width: var(--max-w);
    margin: 0 auto;
  }

  .section-label {
    display: block;
    font-size: var(--fs-label-sm);
    letter-spacing: var(--ls-ultra);
    color: var(--text-ghost);
    margin-bottom: var(--space-4xl);
    text-transform: uppercase;
  }

  .pillar-rows {
    display: flex;
    flex-direction: column;
    gap: var(--space-lg);
  }

  .pillar-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--space-5xl);
    padding: var(--space-2xl);
    border: var(--panel-border);
    align-items: start;
  }

  .pillar-left {
    display: flex;
    flex-direction: column;
    gap: var(--space-md);
  }

  .pillar-num {
    font-size: var(--fs-label-sm);
    letter-spacing: var(--ls-wider);
    color: var(--accent);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 2rem;
    height: 2rem;
    border: 1px solid var(--accent);
  }

  .pillar-title {
    font-size: var(--fs-pillar-title);
    font-weight: var(--fw-bold);
    letter-spacing: var(--ls-wide);
    color: var(--text-primary);
    line-height: 1.3;
    text-transform: uppercase;
    margin: 0;
  }

  .pillar-desc {
    font-size: var(--fs-body-sm);
    color: var(--text-secondary);
    line-height: var(--lh-relaxed);
    letter-spacing: var(--ls-default);
    padding-top: var(--space-xs);
    max-width: var(--max-w-body);
  }

  @media (max-width: 768px) {
    .pillar-row {
      grid-template-columns: 1fr;
      gap: var(--space-xl);
      padding: var(--space-xl);
    }
  }
</style>
