<svelte:head>
  <title>404 — Page Not Found | Sovren Software</title>
  <meta name="description" content="The page you were looking for doesn't exist. Return to the Sovren Software home page." />
  <meta name="robots" content="noindex" />
</svelte:head>

<script>
  import ProductHero from '$lib/ProductHero.svelte';
</script>

<main class="error-page">
  <ProductHero
    category="404"
    title="NOT<br />FOUND."
    tagline="This page doesn't exist."
    size="large"
  />
  <div class="actions">
    <a href="/" class="btn-primary">← BACK TO HOME</a>
  </div>
</main>

<style>
  .error-page {
    min-height: calc(100vh - var(--nav-h));
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .actions {
    max-width: var(--max-w);
    margin: 0 auto;
    width: 100%;
    padding: var(--space-2xl) var(--space-3xl);
    padding-bottom: var(--space-7xl);
  }

  @media (max-width: 768px) {
    .actions {
      padding: var(--space-2xl) var(--space-xl);
      padding-bottom: var(--space-5xl);
    }
  }
</style>
