<script>
  /** @type {string} */
  export let title;
  /** @type {string} */
  export let body;
  /** @type {Array<{label: string, href: string, style?: string, external?: boolean}>} */
  export let actions = [];
</script>

<section class="cta">
  <div class="cta-inner preserve-3d">
    <!-- eslint-disable-next-line svelte/no-at-html-tags -->
    <h2 class="glitch-subtle">{@html title}</h2>
    <p>{body}</p>

    {#if actions.length > 0}
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
    background: transparent;
    color: var(--text-primary);
    padding: var(--pad-section-lg);
    border-top: 1px solid var(--border);
    position: relative;
    overflow: hidden;
  }

  /* Cinematic light bleed from bottom */
  .cta::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 30vh;
    background: linear-gradient(to top, rgba(255,255,255,0.03), transparent);
    pointer-events: none;
    z-index: -1;
  }

  .cta-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: var(--space-2xl);
  }

  .cta h2 {
    font-size: var(--fs-h2);
    font-weight: var(--fw-bold);
    letter-spacing: var(--ls-wide);
    line-height: var(--lh-heading);
    text-transform: uppercase;
    text-shadow: 0 0 30px rgba(255,255,255,0.1);
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
  }
</style>
