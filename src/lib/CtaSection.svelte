<script>
  /** @type {string} */
  export let title;
  /** @type {string} */
  export let body;
  /** @type {Array<{label: string, href: string, style?: 'primary'|'secondary', external?: boolean}>} */
  export let actions = [];
</script>

<section class="cta">
  <div class="cta-inner">
    <h2>{@html title}</h2>
    <p>{body}</p>
    {#if actions.length === 1}
      <a
        href={actions[0].href}
        class="btn-primary"
        target={actions[0].external ? '_blank' : undefined}
        rel={actions[0].external ? 'noreferrer' : undefined}
      >
        {actions[0].label}
      </a>
    {:else if actions.length > 1}
      <div class="cta-links">
        {#each actions as a}
          <a
            href={a.href}
            class={a.style === 'secondary' ? 'btn-secondary' : 'btn-primary'}
            target={a.external ? '_blank' : undefined}
            rel={a.external ? 'noreferrer' : undefined}
          >
            {a.label}
          </a>
        {/each}
      </div>
    {/if}
  </div>
</section>

<style>
  .cta {
    background: var(--light-bg);
    color: var(--light-text-primary);
    padding: var(--pad-section);
    border-top: 1px solid var(--light-border);
  }

  .cta-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: var(--space-xl);
  }

  h2 {
    font-size: var(--fs-h2);
    font-weight: var(--fw-bold);
    letter-spacing: 0.08em;
    line-height: var(--lh-heading);
  }

  p {
    font-size: var(--fs-body-sm);
    color: var(--light-text-secondary);
    max-width: var(--max-w-body);
    line-height: 1.7;
    letter-spacing: var(--ls-default);
  }

  .cta-links {
    display: flex;
    gap: var(--space-lg);
    flex-wrap: wrap;
    margin-top: var(--space-sm);
  }

  .btn-primary {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: var(--fs-btn);
    letter-spacing: var(--ls-wider);
    padding: var(--btn-pad);
    background: var(--light-text-primary);
    color: var(--light-bg);
    text-decoration: none;
    transition: opacity var(--transition-fast);
    align-self: flex-start;
    margin-top: var(--space-sm);
  }

  .btn-primary:hover {
    opacity: 0.75;
  }

  .btn-secondary {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: var(--fs-btn);
    letter-spacing: var(--ls-wider);
    padding: var(--btn-pad);
    border: 1px solid var(--light-text-primary);
    background: transparent;
    color: var(--light-text-primary);
    text-decoration: none;
    transition: background var(--transition-fast), color var(--transition-fast);
  }

  .btn-secondary:hover {
    background: var(--light-text-primary);
    color: var(--light-bg);
  }
</style>
