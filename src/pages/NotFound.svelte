<script>
  import { onMount } from 'svelte'
  onMount(() => window.scrollTo(0, 0))
</script>

<main>
  <section class="hero">
    <div class="hero-inner">
      <span class="code">404</span>
      <h1>SIGNAL<br />LOST.</h1>
      <p class="tagline">This page doesn't exist. Maybe it never did.</p>
      <a href="#/" class="btn-home">RETURN TO BASE →</a>
    </div>
  </section>
</main>

<style>
  .hero {
    min-height: calc(100vh - 60px);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .hero-inner {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 1.5rem;
    padding: 4rem 2.5rem;
    max-width: var(--max-w);
    width: 100%;
    margin: 0 auto;
  }

  .code {
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    color: var(--text-muted);
  }

  h1 {
    font-size: clamp(4rem, 14vw, 10rem);
    font-weight: 700;
    letter-spacing: 0.06em;
    line-height: 0.95;
  }

  .tagline {
    font-size: clamp(0.9rem, 2vw, 1rem);
    color: var(--text-secondary);
    letter-spacing: 0.04em;
    margin-top: 0.5rem;
  }

  .btn-home {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    padding: 0.85rem 1.75rem;
    border: 1px solid var(--border);
    background: transparent;
    color: var(--text-secondary);
    text-decoration: none;
    transition: border-color 0.15s, color 0.15s;
    margin-top: 1rem;
  }

  .btn-home:hover {
    border-color: var(--text-primary);
    color: var(--text-primary);
  }
</style>
