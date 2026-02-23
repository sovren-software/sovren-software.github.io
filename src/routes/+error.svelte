<svelte:head>
  <title>404 — Page Not Found | Sovren Software</title>
</svelte:head>

<main class="error-page">
  <div class="error-inner">
    <span class="error-code">404</span>
    <h1>NOT FOUND.</h1>
    <p>This page doesn't exist.</p>
    <a href="/" class="btn-back">← BACK TO HOME</a>
  </div>
</main>

<style>
  .error-page {
    min-height: calc(100vh - 60px);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .error-inner {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
    text-align: center;
    padding: 4rem 2rem;
  }

  .error-code {
    font-size: 0.65rem;
    letter-spacing: 0.25em;
    color: var(--text-muted);
  }

  h1 {
    font-size: clamp(3rem, 10vw, 7rem);
    font-weight: 700;
    letter-spacing: 0.08em;
    line-height: 1.0;
  }

  p {
    font-size: 0.85rem;
    color: var(--text-secondary);
    letter-spacing: 0.04em;
  }

  .btn-back {
    display: inline-block;
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    color: var(--text-muted);
    text-decoration: none;
    margin-top: 0.5rem;
    transition: color 0.15s;
  }

  .btn-back:hover {
    color: var(--text-primary);
  }
</style>
