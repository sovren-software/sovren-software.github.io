<script>
  import Router from 'svelte-spa-router'
  import Nav from './components/Nav.svelte'
  import Home from './pages/Home.svelte'
  import Augmentum from './pages/Augmentum.svelte'
  import Visage from './pages/Visage.svelte'
  import MrHaven from './pages/MrHaven.svelte'
  import Ecosystem from './pages/Ecosystem.svelte'

  const routes = {
    '/': Home,
    '/augmentum': Augmentum,
    '/visage': Visage,
    '/mrhaven': MrHaven,
    '/ecosystem': Ecosystem,
  }
</script>

<Nav />
<Router {routes} />

<footer>
  <div class="footer-inner">
    <div class="footer-top">
      <a href="#/" class="footer-wordmark">SOVREN</a>
      <nav class="footer-nav">
        <a href="#/augmentum">AUGMENTUM</a>
        <a href="#/visage">VISAGE</a>
        <a href="#/mrhaven">MR. HAVEN</a>
        <a href="#/ecosystem">ECOSYSTEM</a>
        <a href="https://twitter.com/sovren_software" target="_blank" rel="noreferrer">TWITTER</a>
        <a href="https://github.com/sovren-software" target="_blank" rel="noreferrer">GITHUB</a>
        <a href="mailto:hello@sovren.software" class="muted">CONTACT</a>
        <a href="#" class="muted">PRIVACY</a>
        <a href="#" class="muted">LEGAL</a>
      </nav>
    </div>
    <div class="footer-copy">© 2026 SOVREN SOFTWARE. BUILT FOR AUTONOMY.</div>
  </div>
</footer>

<style>
  footer {
    background: var(--bg);
    border-top: 1px solid var(--border);
    padding: 3.5rem 2.5rem;
  }

  .footer-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }

  .footer-top {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 2rem;
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
    flex-wrap: wrap;
    gap: 0.75rem 2rem;
    font-size: 0.65rem;
    letter-spacing: 0.14em;
  }

  .footer-nav a {
    color: var(--text-secondary);
    text-decoration: none;
  }

  .footer-nav a.muted {
    color: var(--text-muted);
  }

  .footer-nav a:hover {
    color: var(--text-primary);
  }

  .footer-copy {
    font-size: 0.6rem;
    letter-spacing: 0.12em;
    color: var(--text-muted);
  }
</style>
