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
    <a href="/" class="wordmark" on:click={close}>
      <svg class="nav-mark" viewBox="0 0 512 512" aria-hidden="true">
        <g fill="none" stroke="currentColor" stroke-width="16" stroke-linecap="butt">
          <line x1="256" y1="56" x2="429.21" y2="356" stroke-dasharray="218.94 24 103.47"/>
          <line x1="429.21" y1="356" x2="82.79" y2="356" stroke-dasharray="218.94 24 103.47"/>
          <line x1="82.79" y1="356" x2="256" y2="56" stroke-dasharray="218.94 24 103.47"/>
          <line x1="429.21" y1="156" x2="256" y2="456" stroke-dasharray="218.94 24 103.47"/>
          <line x1="256" y1="456" x2="82.79" y2="156" stroke-dasharray="218.94 24 103.47"/>
          <line x1="82.79" y1="156" x2="429.21" y2="156" stroke-dasharray="218.94 24 103.47"/>
        </g>
        <polygon points="256,56 429.21,156 429.21,356 256,456 82.79,356 82.79,156"
                 fill="none" stroke="currentColor" stroke-width="16"
                 stroke-linejoin="miter" stroke-miterlimit="4"/>
        <g fill="none" stroke="currentColor" stroke-width="16" stroke-linecap="butt">
          <line x1="298.74" y1="130.01" x2="328.75" y2="181.97"/>
          <line x1="343.75" y1="356" x2="283.74" y2="356"/>
          <line x1="125.53" y1="281.99" x2="155.54" y2="230.03"/>
          <line x1="386.47" y1="230.01" x2="356.46" y2="281.97"/>
          <line x1="213.26" y1="381.99" x2="183.25" y2="330.03"/>
          <line x1="168.25" y1="156" x2="228.26" y2="156"/>
        </g>
      </svg>
      SOVREN
    </a>

    <div class="nav-links" class:open={menuOpen}>
      <span class="sep">//</span>
      <a href="/esver" on:click={close} class:active={isActive('/esver')}>ESVER</a>
      <span class="sep">//</span>
      <a href="/visage" on:click={close} class:active={isActive('/visage')}>VISAGE</a>
      <span class="sep">//</span>
      <a href="/mrhaven" on:click={close} class:active={isActive('/mrhaven')}>MR_HAVEN</a>
      <span class="sep">//</span>
      <a href="/ecosystem" on:click={close} class:active={isActive('/ecosystem')}>CODEX</a>
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
    display: flex;
    align-items: center;
    gap: var(--space-sm);
    font-size: var(--fs-wordmark);
    font-weight: var(--fw-bold);
    letter-spacing: var(--ls-wider);
    color: var(--text-primary);
    text-decoration: none;
  }

  .nav-mark {
    width: 20px;
    height: 20px;
    color: var(--accent);
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
