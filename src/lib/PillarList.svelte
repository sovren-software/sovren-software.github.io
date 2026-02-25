<script>
  /** @type {string} */
  export let label = 'HOW IT WORKS';
  /** @type {Array<{num: string, label: string, desc: string}>} */
  export let pillars = [];
</script>

<section class="pillars">
  <div class="pillars-inner">
    <span class="section-label">{label}</span>
    <div class="pillar-rows">
      {#each pillars as p}
        <div class="pillar-row">
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
  }

  .pillars-inner {
    max-width: var(--max-w);
    margin: 0 auto;
  }

  .section-label {
    display: block;
    font-size: var(--fs-label-sm);
    letter-spacing: 0.2em;
    color: var(--text-muted);
    margin-bottom: var(--space-4xl);
    text-transform: uppercase;
  }

  .pillar-rows {
    display: flex;
    flex-direction: column;
    border-top: 1px solid var(--border);
  }

  .pillar-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--space-5xl);
    padding: var(--space-4xl) 0;
    border-bottom: 1px solid var(--border);
    align-items: start;
  }

  .pillar-left {
    display: flex;
    flex-direction: column;
    gap: var(--space-md);
  }

  .pillar-num {
    font-size: var(--fs-label-sm);
    letter-spacing: 0.2em;
    color: var(--text-muted);
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
    line-height: 1.8;
    letter-spacing: var(--ls-default);
    padding-top: var(--space-xs);
  }

  @media (max-width: 768px) {
    .pillar-row {
      grid-template-columns: 1fr;
      gap: var(--space-xl);
      padding: var(--space-2xl) 0;
    }
  }
</style>
