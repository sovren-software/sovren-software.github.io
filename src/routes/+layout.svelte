<script>
  import '../app.css';
  import Nav from '$lib/Nav.svelte';
  import { page } from '$app/stores';
  import { fade } from 'svelte/transition';
</script>

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
    padding: 4rem 2.5rem 3rem;
  }

  .footer-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 3rem;
  }

  .footer-top {
    display: flex;
    justify-content: space-between;
    gap: 4rem;
    flex-wrap: wrap;
  }

  .footer-wordmark {
    font-size: 0.875rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    color: var(--text-primary);
    text-decoration: none;
  }

  .footer-nav {
    display: flex;
    gap: 4rem;
    flex-wrap: wrap;
  }

  .footer-col {
    display: flex;
    flex-direction: column;
    gap: 0.9rem;
  }

  .col-label {
    font-size: 0.58rem;
    letter-spacing: 0.2em;
    color: var(--text-muted);
    margin-bottom: 0.25rem;
  }

  .footer-col a {
    font-size: 0.68rem;
    letter-spacing: 0.12em;
    color: var(--text-secondary);
    text-decoration: none;
    transition: color 0.15s;
  }

  .footer-col a:hover {
    color: var(--text-primary);
  }

  .footer-bottom {
    display: flex;
    gap: 1.5rem;
    align-items: center;
    flex-wrap: wrap;
  }

  .footer-copy {
    font-size: 0.6rem;
    letter-spacing: 0.12em;
    color: var(--text-muted);
  }

  .footer-copy.muted {
    color: rgba(255, 255, 255, 0.12);
  }

  @media (max-width: 768px) {
    .footer-nav {
      gap: 2.5rem;
    }
  }
</style>
