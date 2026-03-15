<section class="status-bar" aria-label="System status">
  <div class="status-inner">
    <span class="status-left">SOVREN_SOFTWARE // V1.0</span>
    <span class="status-center">
      <span class="status-dot"></span>
      SIGNAL_STATUS: OPERATIONAL
    </span>
    <span class="status-right">© 2026</span>
  </div>
</section>

<style>
  .status-bar {
    width: 100%;
    height: var(--status-bar-h);
    border-top: var(--panel-border);
    background: var(--bg-alt);
    display: flex;
    align-items: center;
  }

  .status-inner {
    max-width: var(--max-w);
    margin: 0 auto;
    width: 100%;
    padding: 0 var(--space-3xl);
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: var(--fs-label-xs);
    letter-spacing: var(--ls-wider);
    color: var(--text-muted);
    text-transform: uppercase;
  }

  .status-center {
    display: flex;
    align-items: center;
    gap: var(--space-sm);
  }

  .status-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--accent);
  }

  @media (max-width: 768px) {
    .status-center {
      display: none;
    }

    .status-inner {
      padding: 0 var(--space-xl);
    }
  }
</style>
