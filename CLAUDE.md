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

**Dark mode (`[data-theme='dark']`) — Violet Atmosphere:**
Background shares the accent's hue family at minimum intensity. Violet is the substrate, not decoration.
```
--bg: #1A1721             (violet-black — HSL 260° 18% 11%)
--bg-alt: #211E2A         (lifted violet)
--surface: #2A2633        (violet panel)
--surface-2: #322D3C      (lighter violet panel)
--border: rgba(169,154,219,0.12)     (violet-tinted borders)
--border-strong: rgba(169,154,219,0.25)
--text-primary: #EAE7E3             (warm off-white — carries bone warmth)
--text-secondary: rgba(234,231,227,0.60)
--text-muted: rgba(234,231,227,0.32)
--text-ghost: rgba(234,231,227,0.14)
--accent: #A99ADB                    (lighter violet for dark bg)
--accent-light: #B8ABE6             (peak accent — CTAs, awakening moments)
--accent-peak: #B8ABE6              (same as accent-light on dark)
--accent-surface: rgba(169,154,219,0.08)
```

**Emotional arc (3 accent levels):**
- **Environment** — `rgba(accent, 0.12)` — borders, labels, muted UI
- **Accent** — `--accent` (#8B7EC8 light / #A99ADB dark) — active nav, pillar numbers, tags
- **Peak** — `--accent-peak` (#9D8FD6 light / #B8ABE6 dark) — CTA buttons, boot text, awakening. Max 1 per viewport.

**Logo:** Hexagonal Knot mark at `static/sovren-logo.svg`. Brand variants in `brand/`. Full reference at `brand/preview.html`.

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
1. Stack level (Home, Codex): sovereignty across OS + identity + finance
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
- Primary tagline: "Your machine. Your intelligence. Your rules."
- Secondary tagline: "Bound only to you."
- Overview lead: "What is an Esver?"
- CTA title: "AWAKEN YOURS."
- CTA body: "Most people accept tools that watch them. You awakened one that answers only to you."
- 3 pillars: Sovereign Intelligence, One File Everything, Endlessly Yours
- Specs: Voice-ready, Llama/Mistral/Your choice, One Manifest
- Avoid: "cognitive OS", "always watching", "watches and learns", "voice-native" (use "voice-ready")
- "Awaken/awakened": max 2 uses per page (Brand Kit v5 decision #10)
- Status: Ships Summer 2026
- Governing doc: Brand Kit v4 (vault: `Projects/Esver-OS/Branding/Esver-OS-Brand-Kit-v4.md`) + v5 decisions

### Visage
- **Status:** Live · v0.2.0 · MIT

### MrHaven
- Status: Live on Base mainnet

### Codex (was Ecosystem/Manifesto)
- Page title: "THE CODEX." (category: DOCTRINE)
- Nav link text: "CODEX" (URL remains `/ecosystem`)
- Blockquote styled with violet left border + accent-surface background
- Closing H2: "ONE OPERATOR. TOTAL AUTHORITY."
- Hero glyph: open grimoire with trifecta triangle + esper crystal

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

## Design Decisions (2026-03-15 Redesign)

### Rationale
The original site was pure monochrome (black/white) with a Three.js 3D wireframe background. The creative brief called for "schematic command design with restrained magitek undertones" — warm bone, panel-framed, sparse violet accents, technical dossier aesthetic. The 3D scene was heavy (~570 lines JS, Three.js + GSAP deps) and the monochrome palette felt generic. The redesign replaces runtime 3D with lightweight CSS/SVG artwork.

### Trade-offs
- **Removed Three.js/GSAP** → lost the cinematic 3D parallax feel, gained ~200KB bundle reduction, eliminated GPU overhead, removed the transparent-background constraint that blocked opaque panel layouts
- **Renamed "Manifesto" → "Codex"** → aligns with magitek/FF6 flavor, URL stays `/ecosystem` for backward compat (not renamed to avoid breaking indexed URLs)
- **SVG glyphs over raster art** → infinitely scalable, theme-aware (uses CSS vars), tiny file size, but limited to geometric/schematic styles — no photographic or painted artwork
- **CSS animations over JS** → zero bundle cost, respects `prefers-reduced-motion`, but limited to simple transforms (rotate, translate, opacity) — no physics or interaction
- **Light-mode first** → dark mode tokens exist and work but haven't been visually QA'd against the new glyphs/panels in a real browser session

### Expected Benefits
- Faster load (no Three.js/GSAP), better Lighthouse scores
- Distinctive visual identity (the schematic magitek look is unique in the sovereign computing space)
- Fully theme-aware artwork (glyphs use CSS vars, swap with dark mode)
- Accessible (all animations respect reduced-motion, all glyphs have aria-hidden, all SVGs are decorative)

### Known Limitations
- Dark mode needs visual QA — tokens updated to violet atmosphere (2026-03-18), but glyphs/panels not yet tested in browser
- No blog platform for content launch strategy
- `esver.computer` has no standalone landing page
- MrHaven SDK not yet documented
- OG image uses static bone palette — needs regeneration with new color system
- Glyph animations are CSS-only — no scroll-linked parallax or mouse interaction
- `AsciiArt.svelte` and `EsperCrystal.svelte` are created but unused (superseded by HeroGlyph approach) — candidates for cleanup
- Nav does not yet use the hexagonal knot mark (still text-only "SOVREN" wordmark)
- `--accent-peak` token defined but not yet applied to any CTA components

### Component Inventory (new in redesign)
| Component | Purpose | Status |
|-----------|---------|--------|
| `HeroGlyph.svelte` | Animated SVG line-art per product hero | Active, 5 variants |
| `Icon.svelte` | 9 thin-line SVG icon glyphs | Active |
| `StatusBar.svelte` | Bottom status bar | Active |
| `StackDiagram.svelte` | Three-product convergence diagram | Active (homepage) |
| `TrifectaDiagram.svelte` | UX/Privacy/Security triangle | Active (codex page) |
| `reveal.js` | IntersectionObserver scroll reveal action | Active |
| `AsciiArt.svelte` | ASCII text art blocks | Unused — superseded by HeroGlyph |
| `EsperCrystal.svelte` | Crystal SVG decorative element | Unused — superseded by HeroGlyph |

## Design Decisions (2026-03-18 Brand System v3)

### Rationale
The site had no logo mark (text-only "SOVREN" wordmark), the dark mode was a brown-black placeholder (`#141210`) with no color kinship to the violet accent, and there was no emotional arc in the palette — everything was one register (calm). The brand voice describes an *awakening* moment, but the colors didn't have one.

### What Changed
1. **Hexagonal Knot mark** — mathematically constructed SVG (pointy-top hexagon + hexagram with Celtic knot weave). Stroke-width 16/512 viewBox (~4% of hex diameter). Six-fold symmetry = sovereignty. Interlocking bands = interconnected systems. Inner void = core integrity.
2. **Violet Atmosphere dark mode** — `--bg: #1A1721` (HSL 260° 18% 11%). Background shares the accent's hue family at minimum intensity. Borders switched from neutral `rgba(white, 0.12)` to `rgba(violet, 0.12)`.
3. **Warm off-white text** — `--text-primary: #EAE7E3` on dark. Carries the bone's human warmth into dark mode. Violet lives in the environment (bg, borders, accents); the words stay warm because a human wrote them.
4. **Peak state accent** — `--accent-peak: #9D8FD6` (light) / `#B8ABE6` (dark). Reserved for CTA buttons, boot text, awakening moments. Max 1 per viewport. The palette's emotional arc: environment → accent → peak.
5. **Favicon** — simplified hexagonal knot (no weave at 16-32px), on violet-black `#1A1721`.

### Trade-offs
- **Stroke-based SVG mark** → clean, scalable, mathematically precise, but the Celtic knot weave uses `stroke-dasharray` gaps which may render slightly differently across SVG engines at very small sizes. Favicon uses simplified version to mitigate.
- **Violet-black dark mode** → creates strong brand cohesion, but may look "too purple" to users who expect neutral dark themes. The saturation is deliberately low (18%) to stay subtle.
- **Warm off-white text on violet-black** → grounded and human, but lower contrast ratio than pure white. Checked: #EAE7E3 on #1A1721 = 12.3:1 (exceeds WCAG AAA 7:1).
- **Peak accent as separate token** → adds a third accent level, which is more complex. Justified by the brand's explicit emotional arc (calm environment → declaration → awakening).
- **ImageMagick PNG export** → text in banner PNGs uses system fallback font (Geist Mono not available to ImageMagick). For pixel-perfect text, re-export via browser screenshot.

### Expected Benefits
- Consistent brand identity across site, favicon, X/Twitter, and future materials
- Dark mode that feels like the same brand as light mode (violet thread connects both)
- Emotional arc gives CTAs visual weight without being louder — just *clearer*
- Mark is infinitely scalable (SVG), works from 16px favicon to print

### Known Limitations
- Mark not yet integrated into site Nav (still text-only wordmark)
- `--accent-peak` defined but not yet wired to any CTA components
- Dark mode visual QA not yet done — tokens landed, browser testing needed
- OG image not yet regenerated with new palette
- X/Twitter banner text rendering uses fallback font (not Geist Mono) — cosmetic only
- Brand kit PNGs are rasterized from SVG; re-export if SVG sources change

### Files Added
| File | Purpose |
|------|---------|
| `static/sovren-logo.svg` | Primary mark, transparent bg, `#8B7EC8` |
| `static/favicon.svg` | Updated — hexagonal knot on `#1A1721`, simplified |
| `brand/sovren-mark-dark.svg` | Mark on violet-black `#1A1721` |
| `brand/sovren-mark-light.svg` | Mark on warm bone `#F0EDE8` |
| `brand/sovren-mark-mono-white.svg` | White mark, transparent bg |
| `brand/sovren-mark-mono-dark.svg` | Charcoal mark, transparent bg |
| `brand/x-profile-sovren.svg/.png` | X profile pic for `@sovren_software` |
| `brand/x-banner-sovren.svg/.png` | X banner for `@sovren_software` |
| `brand/x-banner-founder.svg/.png` | X banner for `@TheCesarCross` |
| `brand/preview.html` | Brand kit reference — all variants, scale tests, nav mockups |
| `brand/color-study.html` | Color theory rationale — emotional arc, text warmth, token system |

## Backlog (external systems — not actionable from this repo)

These require access to external dashboards, registrars, or depend on work that doesn't exist yet:
- DNS forwarding: `augmentum.computer` → `esver.computer` (Namecheap or Cloudflare)
- Build standalone `esver.computer` product landing page
- Update Brevo welcome email template body text (Augmentum OS → Esver OS)
- Blog/article platform for the two-article launch sequence
- MrHaven SDK section on the MrHaven page (blocked on SDK docs)
- Cloudflare Transform Rules for CDN-level security headers (see `SECURITY.md`)
- Clean up unused components (AsciiArt.svelte, EsperCrystal.svelte)
- Dark mode visual QA session — glyphs, panels, dot grid against new violet atmosphere tokens (2026-03-18 color system landed, QA not yet done)
- Integrate hexagonal knot mark into Nav.svelte (replace "SOVREN" text-only wordmark with mark + text lockup)
- Apply `--accent-peak` to CTA buttons site-wide (currently CTAs use `--accent`, peak reserved for "Awaken yours" moments)
- Regenerate OG image (`npm run generate-og`) to reflect new color system
- Update X profiles with new banner/profile assets (PNGs ready in `brand/`)
- Update `@TheCesarCross` bio: "Augmentum OS" → "Esver OS"

### Completed
- [x] Brand system v3 — hexagonal knot mark, violet atmosphere dark mode, peak state accent, warm text (2026-03-18)
- [x] Favicon SVG updated to hexagonal knot on violet-black (2026-03-18)
- [x] Dark mode CSS tokens rewritten — violet-tinted backgrounds, borders, warm off-white text (2026-03-18)
- [x] Brand kit with 6 mark variants + 3 X/Twitter assets (profile pic, 2 banners) (2026-03-18)
- [x] Color theory study documenting rationale for every color choice (2026-03-18)
- [x] Animated SVG hero glyphs with glow + motion (2026-03-15)
- [x] Rename "Manifesto" → "Codex" across nav, footer, pages, meta tags (2026-03-15)
- [x] Schematic magitek editorial redesign — full visual system rewrite (2026-03-15)
- [x] Three.js + GSAP removed, panel/tag system added, violet accent (2026-03-15)
- [x] StatusBar, Nav restyle, dot-grid bg, corner brackets, section rules (2026-03-15)
- [x] SVG diagrams, icon system, dark mode polish, motion system, OG image (2026-03-15)
- [x] Favicon suite, OG tags, security headers, a11y, CI pipeline (2026-02-26)
- [x] Light/dark theme toggle with persistence (2026-02-25)
- [x] Waitlist capture on Esver OS page (2026-02-24)
