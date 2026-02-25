<script>
  /** @type {string} */
  export let lead;
  /** @type {Array<{label: string, value: string, dim?: boolean}>} */
  export let specs = [];
  /** @type {string|undefined} */
  export let stackNote = undefined;
</script>

<section class="overview">
  <div class="overview-inner">
    <div class="overview-text">
      <p class="overview-lead">{lead}</p>
      <slot />
      {#if stackNote}
        <p class="overview-stack">{stackNote}</p>
      {/if}
    </div>
    {#if specs.length}
      <div class="overview-specs">
        {#each specs as s}
          <div class="spec-row">
            <span class="spec-label">{s.label}</span>
            <span class="spec-value" class:dim={s.dim}>{s.value}</span>
          </div>
        {/each}
      </div>
    {/if}
  </div>
</section>

<style>
  .overview {
    background: var(--light-bg);
    color: var(--light-text-primary);
    padding: var(--pad-section);
    border-bottom: 1px solid var(--light-border);
  }

  .overview-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--space-6xl);
    align-items: start;
  }

  .overview-text {
    display: flex;
    flex-direction: column;
    gap: var(--space-2xl);
  }

  .overview-lead {
    font-size: var(--fs-lead);
    font-weight: var(--fw-bold);
    letter-spacing: var(--ls-moderate);
    line-height: 1.2;
    color: var(--light-text-primary);
  }

  .overview-text :global(p) {
    font-size: var(--fs-body);
    line-height: var(--lh-loose);
    color: var(--light-text-body);
    letter-spacing: var(--ls-default);
  }

  .overview-stack {
    font-size: var(--fs-body-xs);
    line-height: 1.7;
    color: var(--light-text-muted);
    letter-spacing: var(--ls-moderate);
    padding-top: var(--space-xs);
    border-top: 1px solid var(--light-border);
  }

  .overview-specs {
    display: flex;
    flex-direction: column;
    border: 1px solid var(--light-border);
  }

  .spec-row {
    display: flex;
    justify-content: space-between;
    padding: var(--space-md) 1.25rem;
    border-bottom: 1px solid var(--light-border);
    font-size: var(--fs-spec);
    letter-spacing: var(--ls-wide);
  }

  .spec-row:last-child {
    border-bottom: none;
  }

  .spec-label {
    color: var(--light-text-muted);
  }

  .spec-value {
    color: #111;
    text-align: right;
  }

  .spec-value.dim {
    color: var(--light-text-dim);
  }

  @media (max-width: 768px) {
    .overview-inner {
      grid-template-columns: 1fr;
      gap: var(--space-4xl);
    }
  }
</style>
