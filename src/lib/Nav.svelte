<script>
  import { page } from '$app/stores';

  let menuOpen = false;
  function close() { menuOpen = false; }

  function isActive(path) {
    if (path === '/') return $page.url.pathname === '/';
    return $page.url.pathname.startsWith(path);
  }
</script>

<nav>
  <div class="nav-inner">
    <a href="/" class="wordmark" on:click={close}>SOVREN</a>
    <button
      class="hamburger"
      class:open={menuOpen}
      on:click={() => (menuOpen = !menuOpen)}
      aria-label="Toggle menu"
    >
      {menuOpen ? '[ CLOSE ]' : '[ MENU ]'}
    </button>
    <div class="nav-links" class:open={menuOpen}>
      <a href="/augmentum" on:click={close} class:active={isActive('/augmentum')}>AUGMENTUM</a>
      <a href="/visage" on:click={close} class:active={isActive('/visage')}>VISAGE</a>
      <a href="/mrhaven" on:click={close} class:active={isActive('/mrhaven')}>MR. HAVEN</a>
      <a href="/ecosystem" on:click={close} class:active={isActive('/ecosystem')}>ECOSYSTEM</a>
    </div>
  </div>
</nav>

<style>
  nav {
    position: sticky;
    top: 0;
    z-index: var(--z-nav);
    background: var(--bg);
    border-bottom: 1px solid var(--border);
  }

  .nav-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    padding: 0 var(--space-3xl);
    height: var(--nav-h);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .wordmark {
    font-size: var(--fs-wordmark);
    font-weight: var(--fw-bold);
    letter-spacing: var(--ls-wider);
    color: var(--text-primary);
    text-decoration: none;
  }

  .nav-links {
    display: flex;
    gap: var(--space-3xl);
    align-items: center;
  }

  .nav-links a {
    font-size: var(--fs-nav);
    letter-spacing: var(--ls-wider);
    color: var(--text-muted);
    text-decoration: none;
    text-transform: uppercase;
    transition: color var(--transition-fast);
  }

  .nav-links a:hover,
  .nav-links a.active {
    color: var(--text-primary);
  }

  .hamburger {
    display: none;
    font-family: var(--font-mono);
    font-size: var(--fs-nav);
    letter-spacing: 0.12em;
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    padding: var(--space-sm);
  }

  @media (max-width: 768px) {
    .hamburger {
      display: block;
    }

    .nav-links {
      display: none;
      position: absolute;
      top: var(--nav-h);
      left: 0;
      right: 0;
      background: var(--bg);
      border-bottom: 1px solid var(--border);
      flex-direction: column;
      align-items: flex-start;
      padding: var(--space-xl) var(--space-3xl);
      gap: var(--space-xl);
    }

    .nav-links.open {
      display: flex;
    }

    .nav-links a {
      font-size: 0.75rem;
    }
  }
</style>
