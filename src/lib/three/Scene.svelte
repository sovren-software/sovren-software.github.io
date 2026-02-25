<script>
  import { onMount, onDestroy } from 'svelte';
  import { browser } from '$app/environment';

  let canvas;
  let manager;

  onMount(async () => {
    if (browser) {
      const { SceneManager } = await import('./SceneManager.js');
      manager = new SceneManager(canvas);
    }
  });

  onDestroy(() => {
    if (manager) {
      manager.destroy();
    }
  });
</script>

<canvas bind:this={canvas} class="webgl-canvas"></canvas>

<style>
  .webgl-canvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: -1;
    pointer-events: none;
    background: #000000;
  }
</style>
