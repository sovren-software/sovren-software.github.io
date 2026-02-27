<script>
  /** @type {string} */
  export let lead;
  /** @type {Array<{label: string, value: string, dim?: boolean}>} */
  export let specs = [];
  /** @type {string|undefined} */
  export let stackNote = undefined;
</script>

<section class="overview">
  <div class="overview-inner preserve-3d">
    <div class="overview-text">
      <p class="overview-lead">{lead}</p>
      <div class="overview-body">
        <slot />
      </div>
      {#if stackNote}
        <!-- eslint-disable-next-line svelte/no-at-html-tags -->
        <p class="overview-stack">{@html stackNote}</p>
      {/if}
    </div>

    {#if specs.length > 0}
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
    background: transparent;
    color: var(--text-primary);
    padding: var(--pad-section-lg);
    border-bottom: 1px solid var(--border);
    position: relative;
    overflow: hidden;
  }

  /* Cinematic ambient lighting */
  .overview::before {
    content: '';
    position: absolute;
    top: 50%; left: -20%;
    width: 60%; height: 100%;
    background: radial-gradient(ellipse at center, rgba(255,255,255,0.02) 0%, transparent 60%);
    pointer-events: none;
    z-index: -1;
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
    letter-spacing: var(--ls-tight);
    line-height: var(--lh-heading);
    color: var(--text-primary);
    text-shadow: 0 0 15px rgba(255, 255, 255, 0.1);
    padding-bottom: var(--space-xl);
    border-bottom: 1px solid var(--border);
  }

  .overview-body {
    display: flex;
    flex-direction: column;
    gap: var(--space-lg);
  }

  :global(.overview-body p) {
    font-size: var(--fs-body-sm);
    line-height: var(--lh-relaxed);
    color: var(--text-secondary);
    letter-spacing: var(--ls-default);
    max-width: var(--max-w-body);
  }

  :global(.overview-body strong) {
    color: var(--text-primary);
    font-weight: var(--fw-semibold);
  }

  .overview-stack {
    font-size: var(--fs-spec);
    line-height: var(--lh-relaxed);
    color: var(--text-muted);
    letter-spacing: var(--ls-moderate);
    padding-top: var(--space-lg);
    border-top: 1px solid var(--border);
  }

  .overview-specs {
    display: flex;
    flex-direction: column;
    border: 1px solid var(--border);
    background: rgba(255, 255, 255, 0.01);
    backdrop-filter: blur(10px);
  }

  .spec-row {
    display: flex;
    justify-content: space-between;
    padding: var(--space-md) var(--space-xl);
    border-bottom: 1px solid var(--border);
    font-size: var(--fs-spec);
    letter-spacing: var(--ls-wide);
    font-family: var(--font-mono);
  }

  .spec-row:last-child {
    border-bottom: none;
  }

  .spec-label {
    color: var(--text-muted);
  }

  .spec-value {
    color: var(--text-primary);
    text-align: right;
  }

  .spec-value.dim {
    color: var(--text-muted);
  }

  @media (max-width: 768px) {
    .overview {
      padding: var(--space-5xl) var(--space-xl);
    }

    .overview-inner {
      grid-template-columns: 1fr;
      gap: var(--space-4xl);
    }

    .spec-row {
      flex-direction: column;
      gap: var(--space-sm);
      padding: var(--space-lg) var(--space-md);
    }

    .spec-value {
      text-align: left;
    }
  }
</style>
