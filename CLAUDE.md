# sovren-website

Marketing site for Sovren Software at `sovren.software`.

---

## Stack

- **Framework**: SvelteKit + `@sveltejs/adapter-static` (prerendered static site)
- **Font**: Geist Mono Variable (self-hosted, `static/fonts/GeistMono-Variable.woff2`)
- **Deploy**: GitHub Actions → `sovren-software.github.io`, CNAME `sovren.software`
- **CDN**: Cloudflare proxy in front of GitHub Pages (enables crawler access, hides Fastly)
- **Search**: Bing Webmaster Tools verified, sitemap submitted

## Design System

Centralized in `src/app.css` with 60+ design tokens. All styles reference tokens — no magic numbers in components.

### Colors

**Dark mode (default):**
```
--bg: #000000
--surface: #080808
--surface-2: #111111
--border: rgba(255,255,255,0.1)
--text-primary: #ffffff
--text-secondary: rgba(255,255,255,0.55)
--text-muted: rgba(255,255,255,0.25)
--text-ghost: rgba(255,255,255,0.12)
```

**Light sections (overview/CTA blocks):**
```
--light-bg: #ffffff
--light-border: #e5e5e5
--light-text-primary: #000000
--light-text-body: #333333
--light-text-secondary: #555555
--light-text-muted: #999999
--light-text-dim: #888888
```

### Typography

| Token | Size | Usage |
|-------|------|-------|
| `--fs-hero` | clamp(3.5rem, 11vw, 8rem) | Home hero H1 |
| `--fs-hero-product` | clamp(4rem, 12vw, 9rem) | Product hero H1 (Augmentum) |
| `--fs-hero-large` | clamp(5rem, 18vw, 12rem) | Product hero H1 (Visage, MrHaven) |
| `--fs-h2` | clamp(2rem, 5vw, 4rem) | CTA section headings |
| `--fs-h2-large` | clamp(2.5rem, 6vw, 5rem) | Ecosystem closing H2 |
| `--fs-thesis` | clamp(1.75rem, 3.5vw, 3.25rem) | Home thesis statement |
| `--fs-lead` | clamp(1.3rem, 2.5vw, 1.7rem) | Overview lead paragraph |
| `--fs-tagline` | clamp(0.95rem, 2vw, 1.1rem) | Hero taglines |
| `--fs-pillar-title` | clamp(0.95rem, 1.5vw, 1.15rem) | Pillar labels |
| `--fs-body` | 0.9rem | Body text |
| `--fs-body-sm` | 0.875rem | Compact body |
| `--fs-body-xs` | 0.85rem | Footnotes, small text |
| `--fs-spec` | 0.72rem | Spec table values |
| `--fs-label` | 0.65rem | Category labels |
| `--fs-label-sm` | 0.62rem | Section labels |
| `--fs-label-xs` | 0.58rem | Footer column labels |
| `--fs-btn` | 0.7rem | Buttons |
| `--fs-nav` | 0.65rem | Navigation links |
| `--fs-wordmark` | 0.875rem | Logo/wordmark |

**Line-height tokens:** `--lh-tight`, `--lh-heading`, `--lh-default`, `--lh-relaxed`, `--lh-loose`

**Letter-spacing tokens:** `--ls-tight`, `--ls-default`, `--ls-moderate`, `--ls-wide`, `--ls-wider`, `--ls-widest`

**Font-weight tokens:** `--fw-normal`, `--fw-medium`, `--fw-semibold`, `--fw-bold`

### Spacing

| Token | Value |
|-------|-------|
| `--space-xs` | 0.25rem |
| `--space-sm` | 0.5rem |
| `--space-md` | 0.75rem |
| `--space-lg` | 1rem |
| `--space-xl` | 1.5rem |
| `--space-2xl` | 2rem |
| `--space-3xl` | 2.5rem |
| `--space-4xl` | 3rem |
| `--space-5xl` | 4rem |
| `--space-6xl` | 6rem |
| `--space-7xl` | 7rem |

**Section padding:** `--pad-section` (6rem 2.5rem), `--pad-section-lg` (7rem 2.5rem), `--pad-hero` (5rem 2.5rem)

### Layout

```
--max-w: 1200px           /* Container max-width */
--max-w-prose: 760px      /* Prose blocks (manifesto) */
--max-w-body: 480px       /* Body paragraphs */
--max-w-tagline: 600px    /* Tagline blocks */
--nav-h: 60px             /* Navigation height */
--z-nav: 100              /* Navigation z-index */
```

### Shared Components

Reusable Svelte components in `src/lib/`:

| Component | Props | Purpose |
|-----------|-------|---------|
| `ProductHero.svelte` | title, category, status, tagline, size | Product page hero section |
| `Overview.svelte` | lead, specs[], stackNote, slot | White-background overview with spec table |
| `PillarList.svelte` | label, pillars[] | Numbered feature list ("HOW IT WORKS") |
| `CtaSection.svelte` | title, body, actions[] | White-background CTA with buttons |

**Product pages** use all four components with zero local CSS. **Home/Ecosystem** retain unique layouts but use design tokens throughout.

### Rules

- Never add a second typeface
- Never use color for emphasis — use weight and letter-spacing only
- White contrast sections use light tokens, never hardcoded values
- All transitions: `var(--transition-fast)` (0.15s)

## Routing

SvelteKit file-based routing. All routes prerendered via `+layout.js` (`export const prerender = true`).

| URL | File |
|---|---|
| `/` | `src/routes/+page.svelte` |
| `/augmentum` | `src/routes/augmentum/+page.svelte` |
| `/visage` | `src/routes/visage/+page.svelte` |
| `/mrhaven` | `src/routes/mrhaven/+page.svelte` |
| `/ecosystem` | `src/routes/ecosystem/+page.svelte` |
| `*` | `src/routes/+error.svelte` |

Active nav state: `import { page } from '$app/stores'` → `$page.url.pathname.startsWith(path)` in `src/lib/Nav.svelte`.

Page transitions: `{#key $page.url.pathname}` with `in:fade`/`out:fade` in `src/routes/+layout.svelte`.

## Static Assets

All static files live in `static/` (NOT `public/` — SvelteKit convention). Copied verbatim to `dist/` at build time.

| File | Purpose |
|---|---|
| `static/CNAME` | GitHub Pages custom domain — do not delete |
| `static/robots.txt` | Crawler access — allows all, points to sitemap |
| `static/sitemap.xml` | All 5 routes with clean URLs |
| `static/llms.txt` | AI crawler context (ChatGPT, Perplexity, Claude) |
| `static/BingSiteAuth.xml` | Bing Webmaster Tools verification |
| `static/fonts/GeistMono-Variable.woff2` | Self-hosted font |

## SEO / AI Discoverability

- `src/app.html` — global JSON-LD (Organization + WebSite schemas)
- Each `+page.svelte` — `<svelte:head>` with unique title, description, og:title, og:description, og:url
- `static/llms.txt` — full product descriptions for AI crawlers
- Cloudflare proxy — prevents GitHub/Fastly from blocking ChatGPT Browse proxy IPs
- Bing Webmaster Tools — verified, sitemap submitted

## Copy Philosophy

**The Sovren Stack is the umbrella.** It is not a product — it is the collection of three products: Augmentum OS (computing), Visage (identity), MrHaven (finance). The hero sub on the home page describes all three layers, not any individual product.

**The x10 thesis lives on individual product pages.** "The infrastructure that multiplies what one person can do" belongs to Augmentum OS. The stack-level copy describes what the stack IS (three layers), not what any one layer does.

**Thesis hierarchy:**
1. Stack level (Home, Ecosystem): sovereignty across OS + identity + finance
2. Product level: each product surfaces the founder-as-proof / capability-multiplication angle
3. Feature level: technical specifics, no thesis language needed

**Tone:** Declarative. Terse. No hedging. No "we believe" or "we think." State things as facts.

## Product Copy Reference

### Home
- Hero H1: `THE SOVREN STACK.`
- Hero sub: `Sovereign OS. Local identity. Programmable assets.`
- Thesis statement: "Privacy is not a feature. Control is not an option. Sovereignty is the baseline..."
- Thesis body: "We build tools for those who want more of themselves — more capacity, more control, more surface area."

### Augmentum OS
- Tagline: "The operating system built for people who refuse to be owned by their software vendor."
- Key angle: AI-native OS layer multiplies what one person can do
- Status: Ships Summer 2026

### Visage
- Tagline: "Linux face authentication via PAM. Your face is your key — processed locally, never broadcast to the cloud."
- Key angle: Open source identity layer; integrates natively with Augmentum OS
- Status: Live · v0.1.0 · MIT

### MrHaven
- Tagline: "Programmable asset control for humans and autonomous agents — no custodian, no intermediary, no exceptions."
- Key angle: Protocol designed for humans AND AI agents as users
- Status: Live on Base mainnet

### Ecosystem (Manifesto)
- Frame: extraction is the default state → we reject that premise → one person with the right stack outbuilds a team
- Closing: "The Sovren Stack...form the infrastructure for one person to operate at the scale of a team."

## Deploy Process

```bash
npm run build        # verify build passes before pushing
git push             # GitHub Actions auto-deploys from main branch
```

CNAME file at `static/CNAME` contains `sovren.software`. Do not delete it.

DNS: 4 A records (185.199.108-111.153) + www CNAME → `sovren-software.github.io`. All proxied through Cloudflare.

## Known Limitations

- No blog platform for the content launch strategy (teaser article, X thread)
- `augmentum.computer` has no landing page yet (CTA now uses mailto:hello@sovren.software)
- MrHaven SDK not yet documented on the site (removed SDK mention from CTA until ready)
- No visual that shows the three products converging (convergence story is text-only, now stronger)

## Remaining Work

- [ ] `augmentum.computer` holding page or redirect
- [ ] Blog/article platform for the two-article launch sequence
- [ ] MrHaven SDK section on the MrHaven page (when SDK docs exist)
- [ ] Visual convergence diagram on Ecosystem page
- [ ] X profile update (currently MrHaven-branded)
- [x] Waitlist capture on Augmentum OS page — mailto:hello@sovren.software (2026-02-24)
- [x] Visage version updated to v0.2.0 (2026-02-24)
- [x] AI agent angle surfaced on MrHaven page (2026-02-24)
- [x] Convergence story strengthened across Augmentum OS, Ecosystem pages (2026-02-24)
- [x] Visage v2/Augmentum OS integration callout added (2026-02-24)
