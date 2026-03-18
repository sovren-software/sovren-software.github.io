<script>
  /** @type {string} */
  export let title;
  /** @type {string} */
  export let body;
  /** @type {Array<{label: string, href: string, style?: string, external?: boolean}>} */
  export let actions = [];
</script>

<section class="cta">
  <div class="cta-inner panel--strong">
    <!-- eslint-disable-next-line svelte/no-at-html-tags -->
    <h2>{@html title}</h2>
    <p>{body}</p>

    {#if actions.length > 0}
      <div class="cta-links">
        {#each actions as a}
          <a
            href={a.href}
            class={a.style === 'secondary' ? 'btn-secondary' : a.style === 'peak' ? 'btn-peak' : 'btn-primary'}
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
    background: var(--bg);
    color: var(--text-primary);
    padding: var(--pad-section-lg);
    border-top: var(--panel-border);
  }

  .cta-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: var(--space-2xl);
    padding: var(--panel-pad);
    border: var(--panel-border-strong);
  }

  .cta h2 {
    font-size: var(--fs-h2);
    font-weight: var(--fw-bold);
    letter-spacing: var(--ls-wide);
    line-height: var(--lh-heading);
    text-transform: uppercase;
  }

  .cta p {
    font-size: var(--fs-body-sm);
    color: var(--text-secondary);
    max-width: var(--max-w-body);
    line-height: var(--lh-relaxed);
    letter-spacing: var(--ls-default);
  }

  .cta-links {
    display: flex;
    gap: var(--space-lg);
    flex-wrap: wrap;
    margin-top: var(--space-md);
  }

  @media (max-width: 768px) {
    .cta {
      padding: var(--space-5xl) var(--space-xl);
    }

    .cta-inner {
      padding: var(--space-xl);
    }
  }
</style>
