<script>
  import '../app.css';
  import Nav from '$lib/Nav.svelte';
  import StatusBar from '$lib/StatusBar.svelte';
  import { page } from '$app/stores';
  import { fade } from 'svelte/transition';
  import { onMount } from 'svelte';
  import { browser } from '$app/environment';

  let theme = 'light';

  onMount(() => {
    if (browser) {
      const storedTheme = localStorage.getItem('theme');
      if (storedTheme) {
        theme = storedTheme;
      } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        theme = 'dark';
      }
      document.documentElement.setAttribute('data-theme', theme);
    }
  });

  function toggleTheme() {
    theme = theme === 'light' ? 'dark' : 'light';
    if (browser) {
      document.documentElement.setAttribute('data-theme', theme);
      localStorage.setItem('theme', theme);
    }
  }
</script>

<a href="#main-content" class="skip-nav">Skip to main content</a>
<Nav {theme} onToggleTheme={toggleTheme} />

{#key $page.url.pathname}
  <div id="main-content" in:fade={{ duration: 150, delay: 50 }} out:fade={{ duration: 100 }}>
    <slot />
  </div>
{/key}

<footer>
  <div class="footer-inner">
    <div class="footer-top">
      <a href="/" class="footer-wordmark">SOVREN</a>
      <nav class="footer-nav" aria-label="Footer">
        <div class="footer-col">
          <span class="col-label">// PRODUCTS</span>
          <a href="/esver">ESVER</a>
          <a href="/visage">VISAGE</a>
          <a href="/mrhaven">MR. HAVEN</a>
        </div>
        <div class="footer-col">
          <span class="col-label">// COMPANY</span>
          <a href="/ecosystem">ECOSYSTEM</a>
          <a href="mailto:hello@sovren.software">CONTACT</a>
        </div>
        <div class="footer-col">
          <span class="col-label">// EXTERNAL</span>
          <a href="https://twitter.com/sovren_software" target="_blank" rel="noreferrer">TWITTER</a>
          <a href="https://github.com/sovren-software" target="_blank" rel="noreferrer">GITHUB</a>
          <a href="https://mrhaven.io" target="_blank" rel="noreferrer">MRHAVEN.IO</a>
          <a href="https://esver.computer" target="_blank" rel="noreferrer">ESVER.COMPUTER</a>
        </div>
      </nav>
    </div>
    <div class="footer-rule"></div>
    <div class="footer-bottom">
      <span class="footer-copy">© 2026 SOVREN SOFTWARE</span>
      <span class="footer-copy muted">BUILT FOR AUTONOMY.</span>
    </div>
  </div>
</footer>

<StatusBar />

<style>
  .skip-nav {
    position: absolute;
    top: -100%;
    left: var(--space-lg);
    z-index: calc(var(--z-nav) + 10);
    padding: var(--space-sm) var(--space-lg);
    background: var(--text-primary);
    color: var(--bg);
    font-family: var(--font-mono);
    font-size: var(--fs-label);
    letter-spacing: var(--ls-wider);
    text-decoration: none;
    text-transform: uppercase;
    transition: top 0.1s;
  }

  .skip-nav:focus {
    top: var(--space-sm);
  }

  footer {
    background: var(--bg);
    border-top: var(--panel-border-strong);
    padding: var(--space-5xl) var(--space-3xl) var(--space-4xl);
  }

  .footer-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: var(--space-3xl);
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
    border-left: var(--panel-border);
    padding-left: var(--space-xl);
  }

  .col-label {
    font-size: var(--fs-label-xs);
    letter-spacing: var(--ls-ultra);
    color: var(--text-ghost);
    margin-bottom: var(--space-xs);
    text-transform: uppercase;
  }

  .footer-col a {
    font-size: var(--fs-footer-link);
    letter-spacing: 0.12em;
    color: var(--text-secondary);
    text-decoration: none;
    transition: color var(--transition-fast);
  }

  .footer-col a:hover {
    color: var(--accent);
  }

  .footer-rule {
    height: 1px;
    background: var(--border);
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

    .footer-col {
      border-left: none;
      padding-left: 0;
    }
  }
</style>
