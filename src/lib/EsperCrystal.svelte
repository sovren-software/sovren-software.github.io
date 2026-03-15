<!-- Esper crystal SVG — decorative magitek element -->
<script>
  /** @type {number} */
  export let size = 120;
</script>

<svg
  width={size}
  height={size * 1.4}
  viewBox="0 0 100 140"
  fill="none"
  xmlns="http://www.w3.org/2000/svg"
  aria-hidden="true"
  class="crystal"
>
  <!-- Outer crystal shape -->
  <polygon
    points="50,5 85,40 85,100 50,135 15,100 15,40"
    stroke="var(--accent)"
    stroke-width="1"
    fill="none"
    opacity="0.3"
  />
  <!-- Inner crystal facets -->
  <polygon
    points="50,20 72,45 72,95 50,120 28,95 28,45"
    stroke="var(--accent)"
    stroke-width="0.75"
    fill="var(--accent-surface)"
    opacity="0.5"
  />
  <!-- Center line -->
  <line x1="50" y1="20" x2="50" y2="120" stroke="var(--accent)" stroke-width="0.5" opacity="0.3" />
  <!-- Cross facets -->
  <line x1="28" y1="45" x2="72" y2="45" stroke="var(--accent)" stroke-width="0.5" opacity="0.2" />
  <line x1="28" y1="95" x2="72" y2="95" stroke="var(--accent)" stroke-width="0.5" opacity="0.2" />
  <!-- Diagonal facets -->
  <line x1="50" y1="20" x2="72" y2="45" stroke="var(--accent)" stroke-width="0.5" opacity="0.2" />
  <line x1="50" y1="20" x2="28" y2="45" stroke="var(--accent)" stroke-width="0.5" opacity="0.2" />
  <line x1="50" y1="120" x2="72" y2="95" stroke="var(--accent)" stroke-width="0.5" opacity="0.2" />
  <line x1="50" y1="120" x2="28" y2="95" stroke="var(--accent)" stroke-width="0.5" opacity="0.2" />
  <!-- Center glow point -->
  <circle cx="50" cy="70" r="3" fill="var(--accent)" opacity="0.6" />
  <circle cx="50" cy="70" r="8" fill="var(--accent)" opacity="0.08" />
</svg>

<style>
  .crystal {
    display: block;
  }
</style>
