<script>
  import { page } from '$app/stores';

  export let theme = 'light';
  export let onToggleTheme = () => {};

  let menuOpen = false;
  function close() { menuOpen = false; }

  function isActive(path) {
    if (path === '/') return $page.url.pathname === '/';
    return $page.url.pathname.startsWith(path);
  }
</script>

<nav aria-label="Primary">
  <div class="nav-inner">
    <a href="/" class="wordmark" on:click={close}>SOVREN</a>

    <div class="nav-links" class:open={menuOpen}>
      <span class="sep">//</span>
      <a href="/esver" on:click={close} class:active={isActive('/esver')}>ESVER</a>
      <span class="sep">//</span>
      <a href="/visage" on:click={close} class:active={isActive('/visage')}>VISAGE</a>
      <span class="sep">//</span>
      <a href="/mrhaven" on:click={close} class:active={isActive('/mrhaven')}>MR_HAVEN</a>
      <span class="sep">//</span>
      <a href="/ecosystem" on:click={close} class:active={isActive('/ecosystem')}>ECOSYSTEM</a>
    </div>

    <div class="nav-actions">
      <button class="theme-toggle" on:click={onToggleTheme} aria-label="Toggle theme">
        {theme === 'light' ? 'SYS:DARK' : 'SYS:LIGHT'}
      </button>

      <button
        class="hamburger"
        class:open={menuOpen}
        on:click={() => (menuOpen = !menuOpen)}
        aria-label="Toggle menu"
      >
        {menuOpen ? '[ CLOSE ]' : '[ MENU ]'}
      </button>
    </div>
  </div>
</nav>

<style>
  nav {
    position: sticky;
    top: 0;
    z-index: var(--z-nav);
    background: var(--bg);
    border-bottom: var(--panel-border);
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

  .nav-actions {
    display: flex;
    align-items: center;
    gap: var(--space-xl);
  }

  .theme-toggle {
    background: none;
    border: 1px solid var(--border);
    color: var(--text-muted);
    font-family: var(--font-mono);
    font-size: var(--fs-label);
    letter-spacing: var(--ls-wider);
    cursor: pointer;
    transition: color var(--transition-fast), border-color var(--transition-fast);
    padding: var(--space-xs) var(--space-sm);
  }

  .theme-toggle:hover {
    color: var(--accent);
    border-color: var(--accent);
  }

  .nav-links {
    display: flex;
    gap: var(--space-lg);
    align-items: center;
  }

  .sep {
    color: var(--text-ghost);
    font-size: var(--fs-label);
    letter-spacing: 0;
    user-select: none;
  }

  .nav-links a {
    font-size: var(--fs-nav);
    letter-spacing: var(--ls-wider);
    color: var(--text-muted);
    text-decoration: none;
    text-transform: uppercase;
    transition: color var(--transition-fast);
    padding-bottom: 2px;
    border-bottom: 2px solid transparent;
  }

  .nav-links a:hover {
    color: var(--text-primary);
  }

  .nav-links a.active {
    color: var(--accent);
    border-bottom-color: var(--accent);
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
      border: var(--panel-border-strong);
      border-top: none;
      flex-direction: column;
      align-items: flex-start;
      padding: var(--space-xl) var(--space-3xl);
      gap: var(--space-xl);
    }

    .nav-links.open {
      display: flex;
    }

    .sep {
      display: none;
    }

    .nav-links a {
      font-size: 0.75rem;
      border-bottom: none;
    }
  }
</style>
