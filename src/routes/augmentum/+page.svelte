<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  import { browser } from '$app/environment';

  onMount(() => {
    if (browser) {
      goto('/esver', { replaceState: true });
    }
  });
</script>

<svelte:head>
  <title>Redirecting to Esver OS | Sovren Software</title>
  <meta http-equiv="refresh" content="0;url=/esver" />
  <link rel="canonical" href="https://sovren.software/esver" />
</svelte:head>

<main>
  <p style="padding: 2rem; font-family: monospace; letter-spacing: 0.1em;">
    Redirecting to <a href="/esver">/esver</a>...
  </p>
</main>
