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
  /** @type {string|undefined} */
  export let glyphId = undefined;

  import HeroGlyph from '$lib/HeroGlyph.svelte';
</script>

<section class="hero" class:large={size === 'large'} class:has-glyph={glyphId}>
  <div class="hero-split">
    <div class="hero-text panel--strong">
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
    {#if glyphId}
      <div class="hero-glyph">
        {#if glyphId === 'esver'}
          <div class="circuit-bg" aria-hidden="true">
            <svg viewBox="0 0 1000 1000" fill="none" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <radialGradient id="circuit-fade" cx="50%" cy="50%" r="50%">
                  <stop offset="0%" stop-color="white" stop-opacity="1" />
                  <stop offset="30%" stop-color="white" stop-opacity="1" />
                  <stop offset="55%" stop-color="white" stop-opacity="0.7" />
                  <stop offset="75%" stop-color="white" stop-opacity="0.35" />
                  <stop offset="90%" stop-color="white" stop-opacity="0.1" />
                  <stop offset="100%" stop-color="white" stop-opacity="0" />
                </radialGradient>
                <mask id="circuit-mask">
                  <rect width="1000" height="1000" fill="url(#circuit-fade)" />
                </mask>
              </defs>
              <g mask="url(#circuit-mask)" stroke="var(--text-muted)" fill="none">
                <!-- Ring 6 — innermost (r=200) — BOLDEST -->
                <circle cx="500" cy="500" r="200" stroke-width="2" opacity="0.7" stroke-dasharray="30 70 50 50 40 60 25 55" stroke-dashoffset="60" />
                <circle cx="345" cy="345" r="4" fill="var(--text-muted)" stroke="none" opacity="0.7" />
                <circle cx="655" cy="655" r="4" fill="var(--text-muted)" stroke="none" opacity="0.7" />
                <circle cx="680" cy="400" r="3.5" fill="var(--text-muted)" stroke="none" opacity="0.6" />
                <circle cx="320" cy="600" r="3.5" fill="var(--text-muted)" stroke="none" opacity="0.6" />
                <line x1="345" y1="345" x2="370" y2="360" stroke-width="1.5" opacity="0.6" />
                <line x1="655" y1="655" x2="630" y2="640" stroke-width="1.5" opacity="0.6" />

                <!-- Ring 5 (r=250) -->
                <circle cx="500" cy="500" r="250" stroke-width="1.8" opacity="0.6" stroke-dasharray="40 60 70 40 50 55 30 50" stroke-dashoffset="30" />
                <circle cx="290" cy="360" r="4" fill="var(--text-muted)" stroke="none" opacity="0.65" />
                <circle cx="710" cy="640" r="4" fill="var(--text-muted)" stroke="none" opacity="0.65" />
                <circle cx="740" cy="440" r="3.5" fill="var(--text-muted)" stroke="none" opacity="0.55" />
                <circle cx="260" cy="560" r="3.5" fill="var(--text-muted)" stroke="none" opacity="0.55" />
                <line x1="290" y1="360" x2="315" y2="380" stroke-width="1.3" opacity="0.5" />
                <line x1="710" y1="640" x2="685" y2="620" stroke-width="1.3" opacity="0.5" />
                <polyline points="740,440 725,430 730,418" stroke-width="1.2" opacity="0.5" />
                <polyline points="260,560 275,570 270,582" stroke-width="1.2" opacity="0.5" />

                <!-- Ring 4 (r=300) -->
                <circle cx="500" cy="500" r="300" stroke-width="1.6" opacity="0.5" stroke-dasharray="55 55 80 35 65 50 40 45" stroke-dashoffset="120" />
                <circle cx="240" cy="340" r="3.5" fill="var(--text-muted)" stroke="none" opacity="0.55" />
                <circle cx="760" cy="660" r="3.5" fill="var(--text-muted)" stroke="none" opacity="0.55" />
                <line x1="240" y1="340" x2="268" y2="360" stroke-width="1.2" opacity="0.45" />
                <line x1="760" y1="660" x2="732" y2="640" stroke-width="1.2" opacity="0.45" />

                <!-- Ring 3 (r=360) -->
                <circle cx="500" cy="500" r="360" stroke-width="1.4" opacity="0.4" stroke-dasharray="90 40 50 60 110 30 65 45" stroke-dashoffset="80" />
                <circle cx="190" cy="310" r="3" fill="var(--text-muted)" stroke="none" opacity="0.45" />
                <circle cx="810" cy="690" r="3" fill="var(--text-muted)" stroke="none" opacity="0.45" />

                <!-- Ring 2 (r=420) -->
                <circle cx="500" cy="500" r="420" stroke-width="1.2" opacity="0.3" stroke-dasharray="60 50 100 30 75 45 85 40" stroke-dashoffset="40" />

                <!-- Ring 1 — outermost (r=480) — faintest -->
                <circle cx="500" cy="500" r="480" stroke-width="1" opacity="0.2" stroke-dasharray="80 30 120 25 90 40 110 35" />

                <!-- Radial connectors near center -->
                <line x1="500" y1="300" x2="500" y2="270" stroke-width="1.5" opacity="0.5" />
                <line x1="500" y1="700" x2="500" y2="730" stroke-width="1.5" opacity="0.5" />
                <line x1="300" y1="500" x2="270" y2="500" stroke-width="1.5" opacity="0.5" />
                <line x1="700" y1="500" x2="730" y2="500" stroke-width="1.5" opacity="0.5" />
              </g>
            </svg>
          </div>
        {/if}
        <HeroGlyph id={glyphId} />
      </div>
    {/if}
  </div>
</section>

<style>
  .hero {
    min-height: calc(100vh - var(--nav-h));
    display: flex;
    align-items: center;
    padding: var(--space-5xl) var(--space-3xl);
    background: var(--bg);
    border-bottom: var(--panel-border-strong);
    position: relative;
    overflow: hidden;
  }

  .circuit-bg {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 1000px;
    height: 1000px;
    pointer-events: none;
    z-index: 0;
    opacity: 0.1;
  }

  .circuit-bg svg {
    width: 100%;
    height: 100%;
  }

  .hero-split {
    max-width: var(--max-w);
    margin: 0 auto;
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--space-4xl);
    align-items: center;
    position: relative;
    z-index: 1;
  }

  .hero:not(.has-glyph) .hero-split {
    grid-template-columns: 1fr;
  }

  .hero-text {
    padding: var(--panel-pad);
    border: var(--panel-border-strong);
    background: var(--bg);
    position: relative;
    z-index: 1;
  }

  .hero-glyph {
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
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
      padding: var(--space-4xl) var(--space-xl);
    }

    .hero-split {
      grid-template-columns: 1fr;
    }

    .hero-text {
      padding: var(--space-xl);
    }

    .hero-glyph {
      order: -1;
    }

    h1 {
      font-size: clamp(3rem, 16vw, 5rem);
    }

    .large h1 {
      font-size: clamp(4rem, 22vw, 7rem);
    }
  }
</style>
