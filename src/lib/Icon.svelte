<!--
  Line-based icon/glyph system.
  Usage: <Icon name="compute" size={20} />
  All icons are thin-line SVGs that match the schematic aesthetic.
-->
<script>
  /** @type {string} */
  export let name;
  /** @type {number} */
  export let size = 20;
</script>

<svg
  width={size}
  height={size}
  viewBox="0 0 24 24"
  fill="none"
  stroke="currentColor"
  stroke-width="1.5"
  stroke-linecap="square"
  stroke-linejoin="miter"
  aria-hidden="true"
  class="icon"
>
  {#if name === 'compute'}
    <!-- Terminal/command: monitor with prompt -->
    <rect x="3" y="4" width="18" height="14" rx="0" />
    <line x1="3" y1="20" x2="21" y2="20" />
    <polyline points="8,10 10,12 8,14" />
    <line x1="12" y1="14" x2="16" y2="14" />
  {:else if name === 'identity'}
    <!-- Face/biometric: simplified face outline -->
    <circle cx="12" cy="10" r="6" />
    <path d="M4 20 C4 16 8 14 12 14 C16 14 20 16 20 20" />
  {:else if name === 'capital'}
    <!-- Vault/lock: safe with keyhole -->
    <rect x="4" y="4" width="16" height="16" rx="0" />
    <rect x="6" y="6" width="12" height="12" rx="0" />
    <circle cx="12" cy="11" r="2" />
    <line x1="12" y1="13" x2="12" y2="15" />
  {:else if name === 'shield'}
    <!-- Shield: security perimeter -->
    <path d="M12 3 L20 7 L20 13 C20 17 16 20 12 21 C8 20 4 17 4 13 L4 7 Z" />
  {:else if name === 'voice'}
    <!-- Microphone: voice interface -->
    <rect x="9" y="3" width="6" height="10" rx="0" />
    <path d="M5 11 C5 15 8 18 12 18 C16 18 19 15 19 11" />
    <line x1="12" y1="18" x2="12" y2="22" />
    <line x1="8" y1="22" x2="16" y2="22" />
  {:else if name === 'lock'}
    <!-- Lock: encrypted/secured -->
    <rect x="5" y="11" width="14" height="10" rx="0" />
    <path d="M8 11 L8 7 C8 4.5 9.8 3 12 3 C14.2 3 16 4.5 16 7 L16 11" />
    <circle cx="12" cy="16" r="1.5" />
  {:else if name === 'arrow-right'}
    <!-- Arrow right -->
    <line x1="4" y1="12" x2="20" y2="12" />
    <polyline points="14,6 20,12 14,18" />
  {:else if name === 'check'}
    <!-- Checkmark -->
    <polyline points="4,12 9,17 20,6" />
  {:else if name === 'signal'}
    <!-- Signal/operational: broadcast waves -->
    <circle cx="12" cy="12" r="2" />
    <path d="M8 8 A6 6 0 0 1 16 8" />
    <path d="M5 5 A10 10 0 0 1 19 5" />
  {/if}
</svg>

<style>
  .icon {
    display: inline-block;
    vertical-align: middle;
    flex-shrink: 0;
  }
</style>
