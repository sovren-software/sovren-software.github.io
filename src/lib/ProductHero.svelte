<script>
  /** @type {string} */
  export let title;
  /** @type {string|undefined} */
  export let category = undefined;
  /** @type {string|undefined} */
  export let status = undefined;
  /** @type {string|undefined} */
  export let tagline = undefined;
  /** @type {'default'|'large'} */
  export let size = 'default';
</script>

<section class="hero" class:large={size === 'large'}>
  <div class="hero-inner panel--strong">
    {#if category}
      <span class="category">{category}</span>
      <div class="category-rule"></div>
    {/if}
    <!-- eslint-disable-next-line svelte/no-at-html-tags -->
    <h1 class="hero-title size-{size}">{@html title}</h1>
    {#if status}
      <span class="tag tag--accent">{status}</span>
    {/if}
    {#if tagline}
      <p class="tagline">{tagline}</p>
    {/if}
  </div>
</section>

<style>
  .hero {
    min-height: calc(100vh - var(--nav-h));
    display: flex;
    align-items: flex-end;
    padding: var(--pad-hero);
    background: var(--bg);
    border-bottom: var(--panel-border-strong);
  }

  .hero-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    width: 100%;
    padding: var(--panel-pad);
    border: var(--panel-border-strong);
  }

  .category {
    display: block;
    font-size: var(--fs-label);
    letter-spacing: var(--ls-ultra);
    color: var(--text-muted);
    margin-bottom: var(--space-lg);
    text-transform: uppercase;
  }

  .category-rule {
    height: 1px;
    background: var(--border);
    margin-bottom: var(--space-2xl);
  }

  h1 {
    font-size: var(--fs-hero-product);
    font-weight: var(--fw-bold);
    letter-spacing: 0.06em;
    line-height: var(--lh-tight);
    margin-bottom: var(--space-2xl);
  }

  .large h1 {
    font-size: var(--fs-hero-large);
    line-height: 0.9;
  }

  .tagline {
    font-size: var(--fs-tagline);
    color: var(--text-secondary);
    max-width: var(--max-w-tagline);
    line-height: 1.65;
    letter-spacing: var(--ls-default);
    margin-top: var(--space-xl);
  }

  @media (max-width: 768px) {
    .hero {
      padding: var(--space-4xl) var(--space-xl) var(--space-5xl);
    }

    .hero-inner {
      padding: var(--space-xl);
    }

    h1 {
      font-size: clamp(3rem, 16vw, 5rem);
    }

    .large h1 {
      font-size: clamp(4rem, 22vw, 7rem);
    }
  }
</style>
