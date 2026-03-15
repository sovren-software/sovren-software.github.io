<!--
  ASCII art blocks for product hero sections.
  Each product gets a unique schematic readout.
  Usage: <AsciiArt id="esver" />
-->
<script>
  /** @type {string} */
  export let id;
</script>

<div class="ascii-wrap">
{#if id === 'sovren'}
<pre class="ascii" aria-hidden="true">{`
     ╔════════════════════════════════════╗
     ║         ◆  SOVREN_CORE  ◆         ║
     ╠════════════════════════════════════╣
     ║                                    ║
     ║   ┌──────────┐    ┌──────────┐    ║
     ║   │ COMPUTE  │────│ IDENTITY │    ║
     ║   │ esver.os │    │ visage   │    ║
     ║   └────┬─────┘    └────┬─────┘    ║
     ║        └──────◆───────┘           ║
     ║               │                    ║
     ║         ┌─────┴──────┐            ║
     ║         │  CAPITAL   │            ║
     ║         │  mr.haven  │            ║
     ║         └────────────┘            ║
     ║                                    ║
     ║  SIGNAL_STATUS: ████████░░ 82%    ║
     ║  AETHERIC_FLUX: NOMINAL           ║
     ╚════════════════════════════════════╝
`}</pre>
{:else if id === 'esver'}
<pre class="ascii" aria-hidden="true">{`
  ┌─────────────────────────────┐
  │  > SYSTEM_INIT              │
  │  > VOICE_ENGINE: ████ LIVE  │
  │  > BIOMETRIC_GATE: LOCKED   │
  │  > AI_COPILOT: STANDBY      │
  │  > AUTHORITY: OPERATOR       │
  │  > TELEMETRY: NONE           │
  │                              │
  │  ┌────────────────────────┐  │
  │  │  ◆ ESPER_LINK: BOUND  │  │
  │  │    kernel → operator   │  │
  │  │    flux_rate: 0.98     │  │
  │  └────────────────────────┘  │
  │                              │
  │  STATUS: ALL_SYSTEMS_GO      │
  └─────────────────────────────┘
`}</pre>
{:else if id === 'visage'}
<pre class="ascii" aria-hidden="true">{`
  ┌───────────────────────┐
  │                       │
  │     ┌───────────┐     │
  │     │  ◎    ◎  │     │
  │     │    ╲╱     │     │
  │     │   ════    │     │
  │     └───────────┘     │
  │                       │
  │  SCAN_MODE: ACTIVE    │
  │  INFERENCE: ON_DEVICE │
  │  MODEL: ONNX_v2       │
  │  MATCH: ██████░ 99.7% │
  │  LIVENESS: VERIFIED   │
  │                       │
  │  ◆ BIOMETRIC_SEALED   │
  └───────────────────────┘
`}</pre>
{:else if id === 'mrhaven'}
<pre class="ascii" aria-hidden="true">{`
  ╔═══════════════════════════╗
  ║     ◆ VAULT_PRIME_001    ║
  ╠═══════════════════════════╣
  ║                           ║
  ║  ASSET:    USDC           ║
  ║  CHAIN:    BASE_L2        ║
  ║  CUSTODY:  NON_CUSTODIAL  ║
  ║                           ║
  ║  ┌───────────────────┐    ║
  ║  │ LOCK:  ████ ARMED │    ║
  ║  │ HEIR:  ████ SET   │    ║
  ║  │ AGENT: ████ BOUND │    ║
  ║  └───────────────────┘    ║
  ║                           ║
  ║  DEAD_SWITCH: 90_DAYS     ║
  ║  CONTRACT: IMMUTABLE      ║
  ╚═══════════════════════════╝
`}</pre>
{:else if id === 'codex'}
<pre class="ascii" aria-hidden="true">{`
  ┌─────────────────────────────┐
  │  ◆◆◆  THE SOVREN CODEX  ◆◆◆│
  ├─────────────────────────────┤
  │                             │
  │  AETHER_NET ──── GRIMOIRE   │
  │       │              │      │
  │       ▼              ▼      │
  │  ┌─────────┐  ┌──────────┐ │
  │  │ LEYLINES│  │INCANTATION│ │
  │  │ ◆◆◆◆◆◆ │  │   _CRD   │ │
  │  └─────────┘  └──────────┘ │
  │                             │
  │  DOCTRINE: SOVEREIGNTY      │
  │  REVISION: 0.8.2-ARCANE     │
  │  SEAL: ████████████ BOUND   │
  └─────────────────────────────┘
`}</pre>
{/if}
</div>

<style>
  .ascii-wrap {
    display: flex;
    justify-content: center;
  }

  .ascii {
    font-family: var(--font-mono);
    font-size: 11px;
    line-height: 1.4;
    color: var(--accent);
    opacity: 0.35;
    white-space: pre;
    margin: 0;
    user-select: none;
    pointer-events: none;
  }

  @media (max-width: 768px) {
    .ascii {
      font-size: 8px;
      line-height: 1.3;
    }
  }
</style>
