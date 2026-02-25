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
    min-height: calc(100vh - var(--nav-h));
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .error-inner {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--space-xl);
    text-align: center;
    padding: var(--space-5xl) var(--space-2xl);
  }

  .error-code {
    font-size: var(--fs-label);
    letter-spacing: var(--ls-widest);
    color: var(--text-muted);
  }

  h1 {
    font-size: clamp(3rem, 10vw, 7rem);
    font-weight: var(--fw-bold);
    letter-spacing: 0.08em;
    line-height: 1.0;
  }

  p {
    font-size: var(--fs-body-xs);
    color: var(--text-secondary);
    letter-spacing: var(--ls-moderate);
  }

  .btn-back {
    display: inline-block;
    font-size: var(--fs-label);
    letter-spacing: var(--ls-wider);
    color: var(--text-muted);
    text-decoration: none;
    margin-top: var(--space-sm);
    transition: color var(--transition-fast);
  }

  .btn-back:hover {
    color: var(--text-primary);
  }
</style>
