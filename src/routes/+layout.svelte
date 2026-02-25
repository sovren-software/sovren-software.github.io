<script>
  import '../app.css';
  import Nav from '$lib/Nav.svelte';
  import Scene from '$lib/three/Scene.svelte';
  import { page } from '$app/stores';
  import { fade } from 'svelte/transition';
</script>

<Scene />
<Nav />

{#key $page.url.pathname}
  <div in:fade={{ duration: 150, delay: 50 }} out:fade={{ duration: 100 }}>
    <slot />
  </div>
{/key}

<footer>
  <div class="footer-inner">
    <div class="footer-top">
      <a href="/" class="footer-wordmark">SOVREN</a>
      <nav class="footer-nav">
        <div class="footer-col">
          <span class="col-label">PRODUCTS</span>
          <a href="/augmentum">AUGMENTUM</a>
          <a href="/visage">VISAGE</a>
          <a href="/mrhaven">MR. HAVEN</a>
        </div>
        <div class="footer-col">
          <span class="col-label">COMPANY</span>
          <a href="/ecosystem">ECOSYSTEM</a>
          <a href="mailto:hello@sovren.software">CONTACT</a>
        </div>
        <div class="footer-col">
          <span class="col-label">EXTERNAL</span>
          <a href="https://twitter.com/sovren_software" target="_blank" rel="noreferrer">TWITTER</a>
          <a href="https://github.com/sovren-software" target="_blank" rel="noreferrer">GITHUB</a>
          <a href="https://mrhaven.io" target="_blank" rel="noreferrer">MRHAVEN.IO</a>
          <a href="https://augmentum.computer" target="_blank" rel="noreferrer">AUGMENTUM.COMPUTER</a>
        </div>
      </nav>
    </div>
    <div class="footer-bottom">
      <span class="footer-copy">© 2026 SOVREN SOFTWARE</span>
      <span class="footer-copy muted">BUILT FOR AUTONOMY.</span>
    </div>
  </div>
</footer>

<style>
  footer {
    background: var(--bg);
    border-top: 1px solid var(--border);
    padding: var(--space-5xl) var(--space-3xl) var(--space-4xl);
  }

  .footer-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: var(--space-4xl);
  }

  .footer-top {
    display: flex;
    justify-content: space-between;
    gap: var(--space-5xl);
    flex-wrap: wrap;
  }

  .footer-wordmark {
    font-size: var(--fs-wordmark);
    font-weight: var(--fw-bold);
    letter-spacing: var(--ls-wider);
    color: var(--text-primary);
    text-decoration: none;
  }

  .footer-nav {
    display: flex;
    gap: var(--space-5xl);
    flex-wrap: wrap;
  }

  .footer-col {
    display: flex;
    flex-direction: column;
    gap: 0.9rem;
  }

  .col-label {
    font-size: var(--fs-label-xs);
    letter-spacing: 0.2em;
    color: var(--text-muted);
    margin-bottom: var(--space-xs);
  }

  .footer-col a {
    font-size: var(--fs-footer-link);
    letter-spacing: 0.12em;
    color: var(--text-secondary);
    text-decoration: none;
    transition: color var(--transition-fast);
  }

  .footer-col a:hover {
    color: var(--text-primary);
  }

  .footer-bottom {
    display: flex;
    gap: var(--space-xl);
    align-items: center;
    flex-wrap: wrap;
  }

  .footer-copy {
    font-size: var(--fs-footer-copy);
    letter-spacing: 0.12em;
    color: var(--text-muted);
  }

  .footer-copy.muted {
    color: var(--text-ghost);
  }

  @media (max-width: 768px) {
    .footer-nav {
      gap: var(--space-3xl);
    }
  }
</style>
