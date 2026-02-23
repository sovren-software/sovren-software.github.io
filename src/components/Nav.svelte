<script>
  import { location } from 'svelte-spa-router'

  let menuOpen = false
  function close() { menuOpen = false }

  function isActive(path) {
    if (path === '/') return $location === '/'
    return $location.startsWith(path)
  }
</script>

<nav>
  <div class="nav-inner">
    <a href="#/" class="wordmark" on:click={close}>SOVREN</a>
    <button
      class="hamburger"
      class:open={menuOpen}
      on:click={() => (menuOpen = !menuOpen)}
      aria-label="Toggle menu"
    >
      {menuOpen ? '[ CLOSE ]' : '[ MENU ]'}
    </button>
    <div class="nav-links" class:open={menuOpen}>
      <a href="#/augmentum" on:click={close} class:active={isActive('/augmentum')}>AUGMENTUM</a>
      <a href="#/visage" on:click={close} class:active={isActive('/visage')}>VISAGE</a>
      <a href="#/mrhaven" on:click={close} class:active={isActive('/mrhaven')}>MR. HAVEN</a>
      <a href="#/ecosystem" on:click={close} class:active={isActive('/ecosystem')}>ECOSYSTEM</a>
    </div>
  </div>
</nav>

<style>
  nav {
    position: sticky;
    top: 0;
    z-index: 100;
    background: var(--bg);
    border-bottom: 1px solid var(--border);
  }

  .nav-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    padding: 0 2.5rem;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .wordmark {
    font-size: 0.875rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    color: var(--text-primary);
    text-decoration: none;
  }

  .nav-links {
    display: flex;
    gap: 2.5rem;
    font-size: 0.7rem;
    letter-spacing: 0.14em;
  }

  .nav-links a {
    color: var(--text-muted);
    text-decoration: none;
    transition: color 0.15s;
    white-space: nowrap;
  }

  .nav-links a:hover,
  .nav-links a.active {
    color: var(--text-primary);
  }

  .hamburger {
    display: none;
    font-family: var(--font-mono);
    font-size: 0.62rem;
    letter-spacing: 0.15em;
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    padding: 0;
    transition: color 0.15s;
  }

  .hamburger.open {
    color: var(--text-primary);
  }

  @media (max-width: 640px) {
    .hamburger {
      display: block;
    }

    .nav-links {
      display: none;
      position: fixed;
      top: 60px;
      left: 0;
      right: 0;
      background: var(--bg);
      border-bottom: 1px solid var(--border);
      flex-direction: column;
      padding: 2rem 2.5rem;
      gap: 2rem;
      font-size: 0.8rem;
    }

    .nav-links.open {
      display: flex;
    }
  }
</style>
