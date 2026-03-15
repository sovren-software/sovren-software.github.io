<!-- Trifecta SVG diagram: UX / Privacy / Security as a reinforcing triangle -->
<div class="diagram-wrap">
  <svg viewBox="0 0 400 360" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Trifecta diagram: UX, Privacy, and Security reinforce each other" role="img">
    <!-- Triangle edges -->
    <line x1="200" y1="40" x2="60" y2="300" class="edge" />
    <line x1="60" y1="300" x2="340" y2="300" class="edge" />
    <line x1="340" y1="300" x2="200" y2="40" class="edge" />

    <!-- Inner connecting lines (reinforcement) -->
    <line x1="200" y1="40" x2="200" y2="300" class="inner" />
    <line x1="60" y1="300" x2="270" y2="170" class="inner" />
    <line x1="340" y1="300" x2="130" y2="170" class="inner" />

    <!-- Vertex nodes -->
    <circle cx="200" cy="40" r="6" class="node" />
    <circle cx="60" cy="300" r="6" class="node" />
    <circle cx="340" cy="300" r="6" class="node" />

    <!-- Center node -->
    <circle cx="200" cy="213" r="4" class="node-accent" />

    <!-- Labels -->
    <text x="200" y="20" class="label" text-anchor="middle">UX</text>
    <text x="40" y="330" class="label" text-anchor="middle">PRIVACY</text>
    <text x="360" y="330" class="label" text-anchor="middle">SECURITY</text>

    <!-- Reinforcement arrows (small chevrons on inner lines) -->
    <text x="200" y="200" class="arrow" text-anchor="middle">///</text>
  </svg>
</div>

<style>
  .diagram-wrap {
    max-width: 320px;
    margin: 0 auto;
  }

  svg {
    width: 100%;
    height: auto;
  }

  .edge {
    stroke: var(--text-primary);
    stroke-width: 1.5;
    opacity: 0.8;
  }

  .inner {
    stroke: var(--accent);
    stroke-width: 0.75;
    opacity: 0.3;
    stroke-dasharray: 4 4;
  }

  .node {
    fill: var(--text-primary);
  }

  .node-accent {
    fill: var(--accent);
  }

  .label {
    fill: var(--text-muted);
    font-family: var(--font-mono);
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
  }

  .arrow {
    fill: var(--accent);
    font-family: var(--font-mono);
    font-size: 10px;
    opacity: 0.5;
  }
</style>
