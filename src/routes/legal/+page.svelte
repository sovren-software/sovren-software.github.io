<svelte:head>
  <title>Legal — Sovren Software</title>
  <meta name="description" content="Privacy policy and terms of service for Sovren Software. Zero data collection. No tracking. No telemetry." />
  <link rel="canonical" href="https://sovren.software/legal" />
  <meta property="og:title" content="Legal — Sovren Software" />
  <meta property="og:description" content="Privacy policy and terms of service. Zero data collection. No tracking." />
  <meta property="og:url" content="https://sovren.software/legal" />
  <meta name="twitter:title" content="Legal — Sovren Software" />
  <meta name="twitter:description" content="Privacy policy and terms of service. Zero data collection. No tracking." />
</svelte:head>

<section class="legal-hero">
  <span class="category-rule">// LEGAL</span>
  <h1>PRIVACY &amp; TERMS.</h1>
  <p class="tagline">Last updated April 3, 2026</p>
</section>

<section class="legal-content">

  <div class="legal-block">
    <h2>// PRIVACY POLICY</h2>

    <h3>The short version</h3>
    <p>We do not collect, store, process, sell, or share your personal data. There is no tracking. There is no telemetry. There are no analytics scripts on this website. There are no cookies.</p>

    <h3>What we collect</h3>
    <p>Nothing. This website is a static site served via GitHub Pages and Cloudflare. We do not run analytics, pixel trackers, session recorders, or fingerprinting scripts. We do not use cookies. We do not embed third-party scripts that collect data on our behalf.</p>

    <h3>Email collection</h3>
    <p>If you voluntarily submit your email address through our launch notification form, it is stored by Brevo (formerly Sendinblue), our email delivery provider, solely for the purpose of sending you the notification you requested. We do not share this list with anyone. You can unsubscribe at any time via the link in any email.</p>

    <h3>Product philosophy</h3>
    <p>Our products are designed to operate entirely on hardware you own. Esver OS runs local inference with no cloud telemetry. Visage performs biometric authentication on-device with encrypted embeddings that never leave your machine. Mr. Haven operates through non-custodial smart contracts where you hold the keys. This privacy policy reflects the same principle applied to our website: your data stays with you because we never ask for it.</p>

    <h3>Server logs</h3>
    <p>Our hosting providers (GitHub Pages, Cloudflare) may collect standard server access logs (IP address, timestamp, page requested) as part of their infrastructure. We do not access, analyze, or retain these logs. Refer to <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noreferrer">GitHub's privacy statement</a> and <a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noreferrer">Cloudflare's privacy policy</a> for their respective data handling practices.</p>

    <h3>Third-party services</h3>
    <p>This site does not use Google Analytics, Facebook Pixel, Hotjar, Intercom, or any equivalent. The only third-party integration is the Brevo email form, which loads only on the Esver OS page when you interact with it.</p>

    <h3>Children</h3>
    <p>We do not knowingly collect data from anyone, including children under 13.</p>

    <h3>Changes</h3>
    <p>If this policy changes, the "last updated" date at the top of this page will reflect it. We will not introduce tracking or data collection without updating this policy first.</p>

    <h3>Contact</h3>
    <p>Questions about this policy: <a href="mailto:hello@sovren.software">hello@sovren.software</a></p>
  </div>

  <div class="legal-rule"></div>

  <div class="legal-block">
    <h2>// TERMS OF SERVICE</h2>

    <h3>Acceptance</h3>
    <p>By accessing sovren.software, you agree to these terms. If you do not agree, do not use the site.</p>

    <h3>What this site is</h3>
    <p>This is an informational website for Sovren Software and its products (Esver OS, Visage, Mr. Haven). Content is provided for informational purposes. Product specifications, timelines, and capabilities described on this site reflect current development status and may change.</p>

    <h3>Intellectual property</h3>
    <p>All content, design, code, and branding on this site is the property of Sovren Software unless otherwise noted. The Sovren name, hexagonal knot mark, and product names (Esver, Visage) are trademarks of Sovren Software. Open-source components are governed by their respective licenses (MIT, Apache 2.0) as indicated in their repositories.</p>

    <h3>No warranty</h3>
    <p>This site and its content are provided "as is" without warranty of any kind. We do not guarantee uninterrupted availability, accuracy of all content, or fitness for any particular purpose.</p>

    <h3>Limitation of liability</h3>
    <p>Sovren Software is not liable for any damages arising from your use of this site or reliance on its content. This includes but is not limited to direct, indirect, incidental, or consequential damages.</p>

    <h3>Product-specific terms</h3>
    <p>Individual products have their own terms. Mr. Haven smart contracts operate on Base L2 and are governed by their on-chain behavior. Esver OS is distributed under its own license. These product-level terms supersede this page where applicable.</p>

    <h3>Governing law</h3>
    <p>These terms are governed by the laws of the State of Wyoming, United States.</p>

    <h3>Contact</h3>
    <p>Questions about these terms: <a href="mailto:hello@sovren.software">hello@sovren.software</a></p>
  </div>

</section>

<style>
  .legal-hero {
    padding: var(--pad-hero);
    max-width: var(--max-w);
    margin: 0 auto;
  }

  .category-rule {
    display: block;
    font-size: var(--fs-label-sm);
    letter-spacing: var(--ls-ultra);
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: var(--space-lg);
  }

  .legal-hero h1 {
    font-size: clamp(2.5rem, 6vw, 5rem);
    font-weight: var(--fw-bold);
    line-height: var(--lh-tight);
    letter-spacing: var(--ls-tight);
    color: var(--text-primary);
    margin: 0;
  }

  .tagline {
    font-size: var(--fs-body-sm);
    color: var(--text-secondary);
    margin-top: var(--space-md);
  }

  .legal-content {
    padding: var(--pad-section);
    max-width: var(--max-w-prose);
    margin: 0 auto;
  }

  .legal-block h2 {
    font-size: var(--fs-label-sm);
    letter-spacing: var(--ls-ultra);
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: var(--space-xl);
    padding-bottom: var(--space-sm);
    border-bottom: var(--panel-border);
  }

  .legal-block h3 {
    font-size: var(--fs-body);
    font-weight: var(--fw-semibold);
    color: var(--text-primary);
    margin-top: var(--space-xl);
    margin-bottom: var(--space-sm);
  }

  .legal-block p {
    font-size: var(--fs-body-sm);
    line-height: var(--lh-relaxed);
    color: var(--text-secondary);
    margin-bottom: var(--space-lg);
  }

  .legal-block a {
    color: var(--accent);
    text-decoration: none;
  }

  .legal-block a:hover {
    text-decoration: underline;
  }

  .legal-rule {
    border-top: var(--panel-border);
    margin: var(--space-5xl) 0;
  }
</style>
