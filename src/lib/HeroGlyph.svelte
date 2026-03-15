<!--
  Large SVG line-art glyphs for hero sections.
  Visible, animated, with violet glow effects.
-->
<script>
  /** @type {string} */
  export let id;
</script>

<div class="glyph-container">
{#if id === 'sovren'}
  <svg viewBox="0 0 600 500" fill="none" class="glyph glyph--drift">
    <defs>
      <filter id="glow-s" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="4" result="blur" />
        <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
      </filter>
    </defs>

    <!-- Outer hex — slow rotate -->
    <g class="spin-slow" style="transform-origin:300px 250px">
      <polygon points="300,30 540,170 540,330 300,470 60,330 60,170" stroke="var(--accent)" stroke-width="1" opacity="0.3" />
    </g>
    <g class="spin-slow-reverse" style="transform-origin:300px 250px">
      <polygon points="300,70 500,185 500,315 300,430 100,315 100,185" stroke="var(--accent)" stroke-width="0.75" opacity="0.2" />
    </g>

    <!-- Convergence lines -->
    <line x1="300" y1="80" x2="300" y2="210" stroke="var(--text-primary)" stroke-width="1.5" opacity="0.25" />
    <line x1="130" y1="370" x2="250" y2="270" stroke="var(--text-primary)" stroke-width="1.5" opacity="0.25" />
    <line x1="470" y1="370" x2="350" y2="270" stroke="var(--text-primary)" stroke-width="1.5" opacity="0.25" />

    <!-- Central node — pulsing glow -->
    <circle cx="300" cy="250" r="40" stroke="var(--accent)" stroke-width="2" opacity="0.4" filter="url(#glow-s)" />
    <circle cx="300" cy="250" r="20" stroke="var(--accent)" stroke-width="1.5" opacity="0.35" class="pulse" />
    <circle cx="300" cy="250" r="5" fill="var(--accent)" opacity="0.7" class="pulse" filter="url(#glow-s)" />

    <!-- Domain nodes -->
    <circle cx="300" cy="80" r="28" stroke="var(--text-primary)" stroke-width="1.5" opacity="0.35" />
    <rect x="285" y="68" width="30" height="24" rx="2" stroke="var(--accent)" stroke-width="1" opacity="0.35" />
    <line x1="290" y1="78" x2="305" y2="78" stroke="var(--accent)" stroke-width="1" opacity="0.5" />
    <line x1="290" y1="82" x2="300" y2="82" stroke="var(--accent)" stroke-width="1" opacity="0.35" />

    <circle cx="130" cy="370" r="28" stroke="var(--text-primary)" stroke-width="1.5" opacity="0.35" />
    <circle cx="130" cy="365" r="10" stroke="var(--accent)" stroke-width="1" opacity="0.35" />
    <path d="M113,382 Q130,376 147,382" stroke="var(--text-primary)" stroke-width="1" opacity="0.3" fill="none" />

    <circle cx="470" cy="370" r="28" stroke="var(--text-primary)" stroke-width="1.5" opacity="0.35" />
    <rect x="455" y="356" width="30" height="28" rx="0" stroke="var(--accent)" stroke-width="1" opacity="0.35" />
    <circle cx="470" cy="367" r="4" stroke="var(--accent)" stroke-width="1" opacity="0.4" fill="none" />
    <line x1="470" y1="371" x2="470" y2="378" stroke="var(--accent)" stroke-width="1" opacity="0.4" />

    <!-- Signal paths -->
    <line x1="300" y1="108" x2="300" y2="210" stroke="var(--accent)" stroke-width="1" stroke-dasharray="6 6" opacity="0.3" />
    <line x1="148" y1="352" x2="265" y2="268" stroke="var(--accent)" stroke-width="1" stroke-dasharray="6 6" opacity="0.3" />
    <line x1="452" y1="352" x2="335" y2="268" stroke="var(--accent)" stroke-width="1" stroke-dasharray="6 6" opacity="0.3" />

    <text x="300" y="40" text-anchor="middle" class="glyph-label">COMPUTE</text>
    <text x="80" y="415" text-anchor="middle" class="glyph-label">IDENTITY</text>
    <text x="520" y="415" text-anchor="middle" class="glyph-label">CAPITAL</text>
  </svg>

{:else if id === 'esver'}
  <svg viewBox="0 0 500 420" fill="none" class="glyph glyph--drift">
    <defs>
      <filter id="glow-e" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="3" result="blur" />
        <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
      </filter>
    </defs>

    <!-- Monitor frame -->
    <rect x="80" y="40" width="340" height="260" rx="0" stroke="var(--text-primary)" stroke-width="2" opacity="0.35" />
    <rect x="92" y="52" width="316" height="236" rx="0" stroke="var(--text-primary)" stroke-width="0.75" opacity="0.2" />

    <!-- Command lines -->
    <line x1="112" y1="82" x2="148" y2="82" stroke="var(--accent)" stroke-width="1.5" opacity="0.6" filter="url(#glow-e)" />
    <line x1="155" y1="82" x2="290" y2="82" stroke="var(--text-primary)" stroke-width="1" opacity="0.2" />
    <line x1="112" y1="105" x2="148" y2="105" stroke="var(--accent)" stroke-width="1.5" opacity="0.5" filter="url(#glow-e)" />
    <line x1="155" y1="105" x2="320" y2="105" stroke="var(--text-primary)" stroke-width="1" opacity="0.2" />
    <line x1="112" y1="128" x2="148" y2="128" stroke="var(--accent)" stroke-width="1.5" opacity="0.45" />
    <line x1="155" y1="128" x2="270" y2="128" stroke="var(--text-primary)" stroke-width="1" opacity="0.15" />
    <line x1="112" y1="151" x2="148" y2="151" stroke="var(--accent)" stroke-width="1.5" opacity="0.35" />
    <line x1="155" y1="151" x2="245" y2="151" stroke="var(--text-primary)" stroke-width="1" opacity="0.12" />
    <line x1="112" y1="174" x2="148" y2="174" stroke="var(--accent)" stroke-width="1.5" opacity="0.3" />
    <line x1="155" y1="174" x2="220" y2="174" stroke="var(--text-primary)" stroke-width="1" opacity="0.1" />

    <!-- Cursor -->
    <rect x="112" y="198" width="10" height="16" fill="var(--accent)" opacity="0.5" class="blink" />

    <!-- Status bar -->
    <line x1="92" y1="260" x2="408" y2="260" stroke="var(--text-primary)" stroke-width="0.75" opacity="0.2" />
    <circle cx="108" cy="275" r="4" fill="var(--accent)" opacity="0.6" class="pulse" filter="url(#glow-e)" />
    <line x1="120" y1="275" x2="210" y2="275" stroke="var(--text-primary)" stroke-width="0.75" opacity="0.15" />

    <!-- Stand -->
    <line x1="250" y1="300" x2="250" y2="345" stroke="var(--text-primary)" stroke-width="1.5" opacity="0.3" />
    <line x1="195" y1="345" x2="305" y2="345" stroke="var(--text-primary)" stroke-width="2" opacity="0.35" />

    <!-- Voice waves -->
    <path d="M345,365 Q380,342 345,320" stroke="var(--accent)" stroke-width="1" opacity="0.3" fill="none" class="pulse" />
    <path d="M355,375 Q400,342 355,310" stroke="var(--accent)" stroke-width="1" opacity="0.2" fill="none" class="pulse-delay" />
    <path d="M365,385 Q420,342 365,300" stroke="var(--accent)" stroke-width="1" opacity="0.12" fill="none" />

    <!-- Shield -->
    <path d="M155,355 L155,385 Q155,402 175,410 Q195,402 195,385 L195,355 Z" stroke="var(--text-primary)" stroke-width="1" opacity="0.3" fill="none" />
    <line x1="175" y1="370" x2="175" y2="390" stroke="var(--accent)" stroke-width="0.75" opacity="0.3" />

    <text x="250" y="405" text-anchor="middle" class="glyph-label">ESPER_LINK: BOUND</text>
  </svg>

{:else if id === 'visage'}
  <svg viewBox="0 0 400 440" fill="none" class="glyph glyph--drift">
    <defs>
      <filter id="glow-v" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="3" result="blur" />
        <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
      </filter>
    </defs>

    <!-- Scan frame -->
    <rect x="100" y="40" width="200" height="280" rx="0" stroke="var(--text-primary)" stroke-width="1.5" opacity="0.3" />

    <!-- Corner brackets -->
    <line x1="100" y1="40" x2="135" y2="40" stroke="var(--accent)" stroke-width="2.5" opacity="0.6" filter="url(#glow-v)" />
    <line x1="100" y1="40" x2="100" y2="75" stroke="var(--accent)" stroke-width="2.5" opacity="0.6" filter="url(#glow-v)" />
    <line x1="300" y1="40" x2="265" y2="40" stroke="var(--accent)" stroke-width="2.5" opacity="0.6" filter="url(#glow-v)" />
    <line x1="300" y1="40" x2="300" y2="75" stroke="var(--accent)" stroke-width="2.5" opacity="0.6" filter="url(#glow-v)" />
    <line x1="100" y1="320" x2="135" y2="320" stroke="var(--accent)" stroke-width="2.5" opacity="0.6" filter="url(#glow-v)" />
    <line x1="100" y1="320" x2="100" y2="285" stroke="var(--accent)" stroke-width="2.5" opacity="0.6" filter="url(#glow-v)" />
    <line x1="300" y1="320" x2="265" y2="320" stroke="var(--accent)" stroke-width="2.5" opacity="0.6" filter="url(#glow-v)" />
    <line x1="300" y1="320" x2="300" y2="285" stroke="var(--accent)" stroke-width="2.5" opacity="0.6" filter="url(#glow-v)" />

    <!-- Face outline -->
    <ellipse cx="200" cy="160" rx="58" ry="72" stroke="var(--text-primary)" stroke-width="1.5" opacity="0.35" fill="none" />

    <!-- Eyes -->
    <ellipse cx="178" cy="145" rx="12" ry="6" stroke="var(--text-primary)" stroke-width="1" opacity="0.35" fill="none" />
    <ellipse cx="222" cy="145" rx="12" ry="6" stroke="var(--text-primary)" stroke-width="1" opacity="0.35" fill="none" />
    <circle cx="178" cy="145" r="3" fill="var(--accent)" opacity="0.6" filter="url(#glow-v)" />
    <circle cx="222" cy="145" r="3" fill="var(--accent)" opacity="0.6" filter="url(#glow-v)" />

    <!-- Nose + mouth -->
    <line x1="200" y1="158" x2="200" y2="178" stroke="var(--text-primary)" stroke-width="0.75" opacity="0.2" />
    <line x1="183" y1="192" x2="217" y2="192" stroke="var(--text-primary)" stroke-width="1" opacity="0.2" />

    <!-- Animated scan line -->
    <line x1="105" y1="180" x2="295" y2="180" stroke="var(--accent)" stroke-width="1.5" opacity="0.4" class="scan-sweep" filter="url(#glow-v)" />

    <!-- Scan grid lines -->
    <line x1="110" y1="100" x2="290" y2="100" stroke="var(--accent)" stroke-width="0.75" stroke-dasharray="3 5" opacity="0.2" />
    <line x1="110" y1="140" x2="290" y2="140" stroke="var(--accent)" stroke-width="0.75" stroke-dasharray="3 5" opacity="0.18" />
    <line x1="110" y1="220" x2="290" y2="220" stroke="var(--accent)" stroke-width="0.75" stroke-dasharray="3 5" opacity="0.18" />
    <line x1="110" y1="260" x2="290" y2="260" stroke="var(--accent)" stroke-width="0.75" stroke-dasharray="3 5" opacity="0.2" />

    <!-- Data points -->
    <circle cx="165" cy="130" r="3" stroke="var(--accent)" stroke-width="1" opacity="0.4" fill="none" />
    <circle cx="235" cy="130" r="3" stroke="var(--accent)" stroke-width="1" opacity="0.4" fill="none" />
    <circle cx="200" cy="205" r="3" stroke="var(--accent)" stroke-width="1" opacity="0.4" fill="none" />
    <circle cx="168" cy="178" r="3" stroke="var(--accent)" stroke-width="1" opacity="0.4" fill="none" />
    <circle cx="232" cy="178" r="3" stroke="var(--accent)" stroke-width="1" opacity="0.4" fill="none" />

    <!-- Data point connections -->
    <line x1="165" y1="130" x2="235" y2="130" stroke="var(--accent)" stroke-width="0.75" stroke-dasharray="4 4" opacity="0.25" />
    <line x1="168" y1="178" x2="232" y2="178" stroke="var(--accent)" stroke-width="0.75" stroke-dasharray="4 4" opacity="0.25" />
    <line x1="165" y1="130" x2="168" y2="178" stroke="var(--accent)" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.15" />
    <line x1="235" y1="130" x2="232" y2="178" stroke="var(--accent)" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.15" />

    <!-- Match bar -->
    <rect x="120" y="350" width="160" height="8" rx="0" stroke="var(--text-primary)" stroke-width="0.75" opacity="0.2" fill="none" />
    <rect x="120" y="350" width="152" height="8" rx="0" fill="var(--accent)" opacity="0.25" />

    <text x="200" y="382" text-anchor="middle" class="glyph-label">MATCH_CONFIDENCE: 99.7%</text>
    <text x="200" y="402" text-anchor="middle" class="glyph-label">LIVENESS: VERIFIED</text>
  </svg>

{:else if id === 'mrhaven'}
  <svg viewBox="0 0 440 440" fill="none" class="glyph glyph--drift">
    <defs>
      <filter id="glow-m" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="4" result="blur" />
        <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
      </filter>
    </defs>

    <!-- Outer hex — slow rotate -->
    <g class="spin-slow" style="transform-origin:220px 210px">
      <polygon points="220,30 390,120 390,300 220,390 50,300 50,120" stroke="var(--text-primary)" stroke-width="1.5" opacity="0.3" fill="none" />
    </g>
    <g class="spin-slow-reverse" style="transform-origin:220px 210px">
      <polygon points="220,55 370,132 370,288 220,365 70,288 70,132" stroke="var(--text-primary)" stroke-width="1" opacity="0.2" fill="none" />
    </g>

    <!-- Vault door -->
    <circle cx="220" cy="210" r="80" stroke="var(--text-primary)" stroke-width="2" opacity="0.35" fill="none" />
    <circle cx="220" cy="210" r="65" stroke="var(--text-primary)" stroke-width="1" opacity="0.25" fill="none" />

    <!-- Lock — glowing -->
    <circle cx="220" cy="195" r="14" stroke="var(--accent)" stroke-width="1.5" opacity="0.6" fill="none" filter="url(#glow-m)" class="pulse" />
    <line x1="220" y1="209" x2="220" y2="235" stroke="var(--accent)" stroke-width="1.5" opacity="0.5" />
    <rect x="208" y="228" width="24" height="18" rx="0" stroke="var(--accent)" stroke-width="1" opacity="0.4" fill="none" />

    <!-- Vault bolts -->
    <circle cx="220" cy="130" r="5" stroke="var(--text-primary)" stroke-width="1" opacity="0.3" fill="none" />
    <circle cx="289" cy="170" r="5" stroke="var(--text-primary)" stroke-width="1" opacity="0.3" fill="none" />
    <circle cx="289" cy="250" r="5" stroke="var(--text-primary)" stroke-width="1" opacity="0.3" fill="none" />
    <circle cx="220" cy="290" r="5" stroke="var(--text-primary)" stroke-width="1" opacity="0.3" fill="none" />
    <circle cx="151" cy="250" r="5" stroke="var(--text-primary)" stroke-width="1" opacity="0.3" fill="none" />
    <circle cx="151" cy="170" r="5" stroke="var(--text-primary)" stroke-width="1" opacity="0.3" fill="none" />

    <!-- Radial lines -->
    <line x1="220" y1="145" x2="220" y2="135" stroke="var(--accent)" stroke-width="0.75" opacity="0.2" />
    <line x1="275" y1="173" x2="284" y2="170" stroke="var(--accent)" stroke-width="0.75" opacity="0.2" />
    <line x1="275" y1="247" x2="284" y2="250" stroke="var(--accent)" stroke-width="0.75" opacity="0.2" />
    <line x1="220" y1="275" x2="220" y2="285" stroke="var(--accent)" stroke-width="0.75" opacity="0.2" />
    <line x1="165" y1="247" x2="156" y2="250" stroke="var(--accent)" stroke-width="0.75" opacity="0.2" />
    <line x1="165" y1="173" x2="156" y2="170" stroke="var(--accent)" stroke-width="0.75" opacity="0.2" />

    <!-- Timer bar -->
    <rect x="130" y="400" width="180" height="6" rx="0" stroke="var(--text-primary)" stroke-width="0.75" opacity="0.25" fill="none" />
    <rect x="130" y="400" width="90" height="6" rx="0" fill="var(--accent)" opacity="0.35" />

    <text x="220" y="428" text-anchor="middle" class="glyph-label">VAULT_SEAL: IMMUTABLE</text>
  </svg>

{:else if id === 'codex'}
  <svg viewBox="0 0 520 420" fill="none" class="glyph glyph--drift">
    <defs>
      <filter id="glow-c" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="4" result="blur" />
        <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
      </filter>
    </defs>

    <!-- Book spine -->
    <line x1="260" y1="50" x2="260" y2="340" stroke="var(--text-primary)" stroke-width="2" opacity="0.35" />

    <!-- Pages -->
    <path d="M260,50 Q175,44 70,62 L70,330 Q175,318 260,340 Z" stroke="var(--text-primary)" stroke-width="1.5" opacity="0.3" fill="none" />
    <path d="M260,50 Q345,44 450,62 L450,330 Q345,318 260,340 Z" stroke="var(--text-primary)" stroke-width="1.5" opacity="0.3" fill="none" />

    <!-- Left: trifecta -->
    <polygon points="165,120 125,195 205,195" stroke="var(--accent)" stroke-width="1.5" opacity="0.45" fill="none" filter="url(#glow-c)" />
    <circle cx="165" cy="120" r="4" fill="var(--accent)" opacity="0.5" class="pulse" />
    <circle cx="125" cy="195" r="4" fill="var(--accent)" opacity="0.5" class="pulse-delay" />
    <circle cx="205" cy="195" r="4" fill="var(--accent)" opacity="0.5" />
    <circle cx="165" cy="170" r="3" fill="var(--accent)" opacity="0.6" filter="url(#glow-c)" class="pulse" />

    <!-- Left text lines -->
    <line x1="100" y1="235" x2="230" y2="235" stroke="var(--text-primary)" stroke-width="0.75" opacity="0.15" />
    <line x1="100" y1="252" x2="210" y2="252" stroke="var(--text-primary)" stroke-width="0.75" opacity="0.12" />
    <line x1="100" y1="269" x2="225" y2="269" stroke="var(--text-primary)" stroke-width="0.75" opacity="0.12" />
    <line x1="100" y1="286" x2="190" y2="286" stroke="var(--text-primary)" stroke-width="0.75" opacity="0.1" />

    <!-- Right: esper crystal -->
    <polygon points="350,110 385,155 385,225 350,270 315,225 315,155" stroke="var(--accent)" stroke-width="1.5" opacity="0.4" fill="none" />
    <polygon points="350,130 372,160 372,220 350,250 328,220 328,160" stroke="var(--accent)" stroke-width="1" fill="var(--accent-surface)" opacity="0.5" />
    <line x1="350" y1="130" x2="350" y2="250" stroke="var(--accent)" stroke-width="0.75" opacity="0.25" />
    <line x1="315" y1="155" x2="385" y2="155" stroke="var(--accent)" stroke-width="0.5" opacity="0.15" />
    <line x1="315" y1="225" x2="385" y2="225" stroke="var(--accent)" stroke-width="0.5" opacity="0.15" />
    <circle cx="350" cy="190" r="5" fill="var(--accent)" opacity="0.6" filter="url(#glow-c)" class="pulse" />

    <!-- Right text lines -->
    <line x1="300" y1="285" x2="425" y2="285" stroke="var(--text-primary)" stroke-width="0.75" opacity="0.12" />
    <line x1="300" y1="302" x2="405" y2="302" stroke="var(--text-primary)" stroke-width="0.75" opacity="0.1" />

    <!-- Binding marks -->
    <circle cx="260" cy="50" r="8" stroke="var(--accent)" stroke-width="1.5" opacity="0.45" fill="none" filter="url(#glow-c)" />
    <circle cx="260" cy="340" r="8" stroke="var(--accent)" stroke-width="1.5" opacity="0.45" fill="none" filter="url(#glow-c)" />

    <text x="260" y="378" text-anchor="middle" class="glyph-label">DOCTRINE: SOVEREIGNTY</text>
    <text x="260" y="398" text-anchor="middle" class="glyph-label">REVISION: 0.8.2-ARCANE</text>
  </svg>
{/if}
</div>

<style>
  .glyph-container {
    display: flex;
    justify-content: center;
    align-items: center;
    pointer-events: none;
    user-select: none;
  }

  .glyph {
    width: 100%;
    height: auto;
    max-width: 520px;
  }

  /* Gentle floating drift */
  .glyph--drift {
    animation: drift 8s ease-in-out infinite;
  }

  @keyframes drift {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
  }

  /* Slow clockwise rotation */
  :global(.spin-slow) {
    animation: spinSlow 60s linear infinite;
  }

  @keyframes spinSlow {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }

  /* Slow counter-clockwise */
  :global(.spin-slow-reverse) {
    animation: spinSlowR 45s linear infinite;
  }

  @keyframes spinSlowR {
    from { transform: rotate(0deg); }
    to { transform: rotate(-360deg); }
  }

  /* Pulsing glow */
  :global(.pulse) {
    animation: pulse 3s ease-in-out infinite;
  }

  :global(.pulse-delay) {
    animation: pulse 3s ease-in-out 1s infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: inherit; }
    50% { opacity: 0.15; }
  }

  /* Cursor blink */
  :global(.blink) {
    animation: blink 1.2s step-end infinite;
  }

  @keyframes blink {
    0%, 100% { opacity: 0.5; }
    50% { opacity: 0; }
  }

  /* Scan sweep (Visage) */
  :global(.scan-sweep) {
    animation: scanSweep 4s ease-in-out infinite;
  }

  @keyframes scanSweep {
    0% { transform: translateY(-80px); opacity: 0; }
    15% { opacity: 0.4; }
    85% { opacity: 0.4; }
    100% { transform: translateY(120px); opacity: 0; }
  }

  :global(.glyph-label) {
    font-family: var(--font-mono);
    font-size: 10px;
    letter-spacing: 3px;
    fill: var(--text-muted);
    text-transform: uppercase;
  }

  @media (max-width: 768px) {
    .glyph {
      max-width: 300px;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .glyph--drift,
    :global(.spin-slow),
    :global(.spin-slow-reverse),
    :global(.pulse),
    :global(.pulse-delay),
    :global(.blink),
    :global(.scan-sweep) {
      animation: none !important;
    }
  }
</style>
