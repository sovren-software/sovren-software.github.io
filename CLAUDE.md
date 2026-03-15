# sovren-website

Marketing site for Sovren Software at `sovren.software`.

---

## Stack

- **Framework**: SvelteKit 2.x + `@sveltejs/adapter-static` (prerendered static site)
- **Font**: Geist Mono Variable (self-hosted, `static/fonts/GeistMono-Variable.woff2`)
- **Build**: Vite 7.x
- **Deploy**: GitHub Actions → `sovren-software.github.io`, CNAME `sovren.software`
- **CDN**: Cloudflare proxy in front of GitHub Pages (enables crawler access, hides Fastly)
- **Search**: Bing Webmaster Tools verified, sitemap submitted

Note: Three.js and GSAP were removed in the schematic magitek redesign (2026-03-15). No 3D scene or animation library.

## Design System — Schematic Magitek

Visual language: schematic command design with restrained magitek undertones. Warm bone backgrounds, panel-framed layouts, thin border rules, sparse violet accents, and a technical dossier aesthetic.

Centralized in `src/app.css` with 70+ design tokens. All styles reference tokens — no magic numbers in components.

### Colors

The site uses a `data-theme` attribute on `<html>` to switch between light and dark mode. CSS custom properties swap automatically. **Light-mode first** — dark mode tokens are present but unpolished.

**Light mode (default — `:root` / `[data-theme='light']`):**
```
--bg: #F0EDE8             (warm bone)
--bg-alt: #E8E4DF         (darker bone for alternating panels)
--surface: #FFFFFF         (white panel surface)
--surface-2: #F7F5F2      (off-white surface)
--border: rgba(0,0,0,0.12)        (thin rules)
--border-strong: rgba(0,0,0,0.25)  (panel frames)
--text-primary: #1A1A1A            (charcoal)
--text-secondary: rgba(26,26,26,0.65)
--text-muted: rgba(26,26,26,0.35)
--text-ghost: rgba(26,26,26,0.15)
--accent: #8B7EC8                  (soft violet)
--accent-light: #A99ADB           (lighter violet)
--accent-surface: rgba(139,126,200,0.08) (violet tint)
```

**Dark mode (`[data-theme='dark']`) — placeholder:**
```
--bg: #141210
--bg-alt: #1A1816
--accent: #A99ADB
(rest follows inverse pattern)
```

### Panel System

The panel system provides the technical dossier framing:
```css
.panel        { border: var(--panel-border); padding: var(--panel-pad); }
.panel--strong { border: var(--panel-border-strong); }
.panel--alt   { background: var(--bg-alt); }
.panel-header { fs: label-sm, ls: ultra, uppercase, border-bottom, muted }
```

### Tag System

Inline metadata badges:
```css
.tag          { inline-block, fs: label-sm, ls: wider, uppercase, bordered }
.tag--accent  { border-color + color: var(--accent) }
```

### Typography

| Token | Size | Usage |
|-------|------|-------|
| `--fs-hero` | clamp(4rem, 12vw, 10rem) | Home hero H1 |
| `--fs-hero-product` | clamp(4rem, 12vw, 9rem) | Product hero H1 (Esver) |
| `--fs-hero-large` | clamp(5rem, 18vw, 12rem) | Product hero H1 (Visage, MrHaven) |
| `--fs-h2` | clamp(2rem, 5vw, 4rem) | CTA section headings |
| `--fs-h2-large` | clamp(2.5rem, 6vw, 5rem) | Ecosystem closing H2 |
| `--fs-thesis` | clamp(2rem, 4vw, 4rem) | Home thesis statement |
| `--fs-lead` | clamp(1.3rem, 2.5vw, 1.7rem) | Overview lead paragraph |
| `--fs-tagline` | clamp(0.95rem, 2vw, 1.1rem) | Hero taglines |
| `--fs-pillar-title` | clamp(0.95rem, 1.5vw, 1.15rem) | Pillar labels |
| `--fs-body` | 0.95rem | Body text |
| `--fs-body-sm` | 0.875rem | Compact body |
| `--fs-body-xs` | 0.85rem | Footnotes, small text |
| `--fs-spec` | 0.75rem | Spec table values |
| `--fs-label` | 0.7rem | Category labels |
| `--fs-label-sm` | 0.65rem | Section labels |
| `--fs-label-xs` | 0.6rem | Footer column labels, status bar |
| `--fs-label-lg` | 0.8rem | Large labels |
| `--fs-btn` | 0.75rem | Buttons |
| `--fs-nav` | 0.7rem | Navigation links |
| `--fs-wordmark` | 0.9rem | Logo/wordmark |

**Line-height tokens:** `--lh-tight`, `--lh-heading`, `--lh-default`, `--lh-relaxed`, `--lh-loose`

**Letter-spacing tokens:** `--ls-tight`, `--ls-default`, `--ls-moderate`, `--ls-wide`, `--ls-wider`, `--ls-widest`, `--ls-ultra` (0.35em)

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
| `--space-7xl` | 8rem |

**Section padding:** `--pad-section` (6rem 2.5rem), `--pad-section-lg` (8rem 2.5rem), `--pad-hero` (5rem 2.5rem)

### Layout

```
--max-w: 1200px           /* Container max-width */
--max-w-prose: 800px      /* Prose blocks (manifesto) */
--max-w-body: 520px       /* Body paragraphs */
--max-w-tagline: 640px    /* Tagline blocks */
--nav-h: 60px             /* Navigation height */
--status-bar-h: 36px      /* Bottom status bar */
--z-nav: 100              /* Navigation z-index */
```

### Shared Components

Reusable Svelte components in `src/lib/`:

| Component | Props | Purpose |
|-----------|-------|---------|
| `ProductHero.svelte` | title, category, status, tagline, size | Panel-framed product hero with category rule |
| `Overview.svelte` | lead, specs[], stackNote, slot | Overview with `// SPECIFICATIONS` panel header |
| `PillarList.svelte` | label, pillars[] | Panel-bordered pillars with violet number badges |
| `CtaSection.svelte` | title, body, actions[] | Panel-framed CTA section |
| `StatusBar.svelte` | (none) | Bottom status bar: version, operational status, copyright |
| `Nav.svelte` | theme, onToggleTheme | Top nav with `//` separators, `SYS:LIGHT`/`SYS:DARK` toggle |

**Product pages** use all four main components with zero local CSS (except Esver's launch briefing form). **Home/Ecosystem** retain unique layouts but use design tokens and panel classes throughout.

### Rules

- Never add a second typeface
- Violet accent (`--accent`) is used sparingly: active nav state, pillar numbers, tags, blockquote borders, hover states, status dot
- All color values must use theme-aware CSS variables — never hardcode colors
- All transitions: `var(--transition-fast)` (0.15s) or `var(--transition-slow)` (0.4s)
- All sections have opaque `var(--bg)` backgrounds (no transparent backgrounds)
- Panel borders use `var(--panel-border)` or `var(--panel-border-strong)` — not raw border declarations
- Section labels use `// PREFIX` format (e.g., `// SPECIFICATIONS`, `// DOCTRINE`, `// THE THREE PILLARS`)

## Theme System

Light/dark mode toggle with persistence and system preference fallback.

### How It Works

1. **`+layout.svelte`** owns the theme state and provides `toggleTheme()` to `Nav.svelte`
2. On mount: checks `localStorage('theme')` → falls back to `prefers-color-scheme` → defaults to light
3. Sets `document.documentElement.setAttribute('data-theme', theme)`
4. CSS variables in `app.css` swap via `:root` / `[data-theme='light']` and `[data-theme='dark']` selectors

### Theme Flow

```
User clicks toggle → +layout.svelte toggleTheme()
  → sets data-theme on <html>
  → saves to localStorage
  → CSS variables swap instantly (all tokens theme-aware)
```

### Adding Theme-Aware Styles

Always use CSS variables. Never hardcode colors:
```css
/* Correct */
color: var(--text-primary);
background: var(--surface);
border-color: var(--border);
border: var(--panel-border);

/* Wrong */
color: #ffffff;
background: rgba(255, 255, 255, 0.1);
border: 1px solid rgba(0,0,0,0.12);
```

## Routing

SvelteKit file-based routing. All routes prerendered via `+layout.js` (`export const prerender = true`).

| URL | File |
|---|---|
| `/` | `src/routes/+page.svelte` |
| `/esver` | `src/routes/esver/+page.svelte` |
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

**The Sovren Stack is the umbrella.** It is not a product — it is the collection of three products: Esver OS (computing), Visage (identity), MrHaven (finance). The hero sub on the home page describes all three layers, not any individual product.

**The x10 thesis lives on individual product pages.** "The infrastructure that multiplies what one person can do" belongs to Esver OS. The stack-level copy describes what the stack IS (three layers), not what any one layer does.

**Thesis hierarchy:**
1. Stack level (Home, Ecosystem): sovereignty across OS + identity + finance
2. Product level: each product surfaces the founder-as-proof / capability-multiplication angle
3. Feature level: technical specifics, no thesis language needed

**Tone:** Declarative. Terse. No hedging. No "we believe" or "we think." State things as facts.

## Product Copy Reference

### Home
- Hero H1: `THE SOVREN STACK.`
- Hero sub: `> Sovereign compute. Local identity. Programmable capital.`
- Hero frame labels: `// 001` (top-left), `V1.0` (top-right)
- Thesis panel header: `// DOCTRINE`

### Esver OS
- Tagline: "One operator. Total authority. UX, privacy, and security — none sacrificed."
- Hero lead: "Your command center. Built without compromise."
- CTA title: "BUILT WITHOUT COMPROMISE."
- Avoid: "cognitive OS", "always watching", "watches and learns" framing
- Status: Ships Summer 2026

### Visage
- **Status:** Live · v0.2.0 · MIT

### MrHaven
- Status: Live on Base mainnet

### Ecosystem (Manifesto)
- Blockquote styled with violet left border + accent-surface background
- Closing H2: "ONE OPERATOR. TOTAL AUTHORITY."

## Deploy Process

```bash
npm run check        # svelte-check — must pass
npm run lint         # ESLint — must pass
npm run build        # verify build passes before pushing
git push             # GitHub Actions auto-deploys from main branch
```

CI pipeline runs `check → lint → build` in sequence. All three must pass before deployment.

CNAME file at `static/CNAME` contains `sovren.software`. Do not delete it.

DNS: 4 A records (185.199.108-111.153) + www CNAME → `sovren-software.github.io`. All proxied through Cloudflare.

### Security Headers

Two-level enforcement on GitHub Pages + Cloudflare:
- **Active (meta):** CSP, Referrer-Policy, X-Content-Type-Options via `<meta http-equiv>` in `app.html`
- **Requires Cloudflare dashboard:** X-Frame-Options, HSTS, COOP, CORP, Permissions-Policy — see `SECURITY.md`
- `static/_headers` is authoritative source; auto-enforced if migrated to Cloudflare Pages

### OG Image

```bash
npm run generate-og  # rewrites static/og-image.png
```

Script is at `scripts/generate-og.js`. Run it after any brand or copy changes that should be reflected in social previews.

## Known Limitations

- No blog platform for the content launch strategy (teaser article, X thread)
- `esver.computer` has no standalone landing page — product page lives at `sovren.software/esver`
- MrHaven SDK not yet documented on the site (removed SDK mention from CTA until ready)
- No visual that shows the three products converging (convergence story is text-only)
- `augmentum.computer` → `esver.computer` DNS redirect not yet configured (Namecheap/Cloudflare)
- Brevo welcome email template still references Augmentum OS in body text — update in Brevo dashboard

## Remaining Work

### External / Blocked (cannot complete from this repo)
- [ ] DNS forwarding: `augmentum.computer` → `esver.computer` (Namecheap or Cloudflare forwarding)
- [ ] Build standalone `esver.computer` product landing page
- [ ] Update Brevo welcome email template body text (Augmentum OS → Esver OS)
- [ ] Blog/article platform for the two-article launch sequence
- [ ] MrHaven SDK section on the MrHaven page (when SDK docs exist)
- [ ] X profile update (currently MrHaven-branded)
- [ ] Cloudflare Transform Rules for CDN-level security headers (see `SECURITY.md`)

### Completed
- [x] Schematic magitek editorial redesign — full visual system rewrite (2026-03-15)
- [x] Three.js + GSAP removed, panel/tag system added, violet accent (2026-03-15)
- [x] StatusBar component, Nav restyled (2026-03-15)
- [x] SVG diagrams: StackDiagram + TrifectaDiagram (2026-03-15)
- [x] Line-based icon/glyph system: Icon.svelte with 9 glyphs (2026-03-15)
- [x] Dark mode polish: refined token tuning (2026-03-15)
- [x] Motion system: reveal.js + CSS scroll reveals (2026-03-15)
- [x] OG image regenerated with schematic magitek palette (2026-03-15)
- [x] Visual convergence diagram on homepage (2026-03-15)
- [x] manifest.webmanifest theme-color updated (2026-03-15)
- [x] Favicon suite, Web app manifest, OG image (2026-02-26)
- [x] Open Graph + Twitter Card + Canonical URLs on all pages (2026-02-26)
- [x] Security headers, skip-nav, aria-labels, prefers-reduced-motion (2026-02-26)
- [x] ESLint + Prettier + svelte-check, CI pipeline, Dependabot (2026-02-26)
- [x] LICENSE, CHANGELOG, SECURITY.md (2026-02-26)
- [x] Light/dark theme toggle with persistence (2026-02-25)
- [x] Waitlist capture on Esver OS page (2026-02-24)
