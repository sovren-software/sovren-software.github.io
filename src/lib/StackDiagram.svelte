<!-- Sovren Stack architecture diagram: three layers converging -->
<div class="diagram-wrap">
  <svg viewBox="0 0 480 320" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Sovren Stack architecture: Esver OS, Visage, and Mr. Haven converging into one sovereign layer" role="img">
    <!-- Connection lines to center -->
    <line x1="80" y1="80" x2="240" y2="200" class="conn" />
    <line x1="240" y1="50" x2="240" y2="200" class="conn" />
    <line x1="400" y1="80" x2="240" y2="200" class="conn" />

    <!-- Layer boxes -->
    <!-- 01 — Esver OS -->
    <rect x="20" y="40" width="120" height="80" rx="0" class="layer-box" />
    <text x="80" y="62" class="layer-num" text-anchor="middle">01</text>
    <text x="80" y="80" class="layer-name" text-anchor="middle">ESVER OS</text>
    <text x="80" y="100" class="layer-domain" text-anchor="middle">COMPUTE</text>

    <!-- 02 — Visage -->
    <rect x="180" y="10" width="120" height="80" rx="0" class="layer-box" />
    <text x="240" y="32" class="layer-num" text-anchor="middle">02</text>
    <text x="240" y="50" class="layer-name" text-anchor="middle">VISAGE</text>
    <text x="240" y="70" class="layer-domain" text-anchor="middle">IDENTITY</text>

    <!-- 03 — Mr. Haven -->
    <rect x="340" y="40" width="120" height="80" rx="0" class="layer-box" />
    <text x="400" y="62" class="layer-num" text-anchor="middle">03</text>
    <text x="400" y="80" class="layer-name" text-anchor="middle">MR. HAVEN</text>
    <text x="400" y="100" class="layer-domain" text-anchor="middle">CAPITAL</text>

    <!-- Convergence node -->
    <circle cx="240" cy="200" r="8" class="node-accent" />

    <!-- Output line -->
    <line x1="240" y1="208" x2="240" y2="270" class="output" />

    <!-- Result label -->
    <rect x="140" y="270" width="200" height="40" rx="0" class="result-box" />
    <text x="240" y="296" class="result-label" text-anchor="middle">SOVEREIGN STACK</text>
  </svg>
</div>

<style>
  .diagram-wrap {
    max-width: 420px;
    margin: 0 auto;
  }

  svg {
    width: 100%;
    height: auto;
  }

  .conn {
    stroke: var(--accent);
    stroke-width: 2;
    opacity: 0.3;
    stroke-dasharray: 6 4;
  }

  .layer-box {
    fill: none;
    stroke: var(--text-primary);
    stroke-width: 1.5;
    opacity: 0.6;
  }

  .layer-num {
    fill: var(--accent);
    font-family: var(--font-mono);
    font-size: 9px;
    letter-spacing: 2px;
  }

  .layer-name {
    fill: var(--text-primary);
    font-family: var(--font-mono);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
  }

  .layer-domain {
    fill: var(--text-muted);
    font-family: var(--font-mono);
    font-size: 8px;
    letter-spacing: 3px;
  }

  .node-accent {
    fill: var(--accent);
    opacity: 0.8;
  }

  .output {
    stroke: var(--accent);
    stroke-width: 2.5;
    opacity: 0.5;
  }

  .result-box {
    fill: none;
    stroke: var(--accent);
    stroke-width: 2.5;
    opacity: 0.6;
  }

  .result-label {
    fill: var(--accent);
    font-family: var(--font-mono);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
  }
</style>
