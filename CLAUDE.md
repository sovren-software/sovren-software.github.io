# sovren-website

Marketing site for Sovren Software at `sovren.software`.

---

## Stack

- **Framework**: SvelteKit 2.x + `@sveltejs/adapter-static` (prerendered static site)
- **3D Scene**: Three.js 0.183 (wireframe cube, grid, particles, product monoliths)
- **Animation**: GSAP 3.x
- **Font**: Geist Mono Variable (self-hosted, `static/fonts/GeistMono-Variable.woff2`)
- **Build**: Vite 7.x
- **Deploy**: GitHub Actions → `sovren-software.github.io`, CNAME `sovren.software`
- **CDN**: Cloudflare proxy in front of GitHub Pages (enables crawler access, hides Fastly)
- **Search**: Bing Webmaster Tools verified, sitemap submitted

## Design System

Centralized in `src/app.css` with 60+ design tokens. All styles reference tokens — no magic numbers in components.

### Colors

The site uses a `data-theme` attribute on `<html>` to switch between light and dark mode. CSS custom properties swap automatically.

**Light mode (default — `:root` / `[data-theme='light']`):**
```
--bg: #ffffff
--surface: rgba(230,230,230,0.4)
--surface-2: rgba(210,210,210,0.5)
--border: rgba(0,0,0,0.15)
--border-glow: rgba(0,0,0,0.8)
--text-primary: #000000
--text-secondary: rgba(0,0,0,0.65)
--text-muted: rgba(0,0,0,0.35)
--text-ghost: rgba(0,0,0,0.15)
```

**Dark mode (`[data-theme='dark']`):**
```
--bg: #000000
--surface: rgba(25,25,25,0.4)
--surface-2: rgba(40,40,40,0.5)
--border: rgba(255,255,255,0.15)
--border-glow: rgba(255,255,255,0.8)
--text-primary: #ffffff
--text-secondary: rgba(255,255,255,0.65)
--text-muted: rgba(255,255,255,0.35)
--text-ghost: rgba(255,255,255,0.15)
```

**Important:** Both themes are pure monochrome. No accent colors, no brand colors. Emphasis is achieved through weight and spacing, never color.

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
- All color values must use theme-aware CSS variables — never hardcode `rgba(255,...)` or `rgba(0,...)`
- All transitions: `var(--transition-fast)` (0.15s) or `var(--transition-slow)` (0.4s)

## Theme System

Light/dark mode toggle with persistence and system preference fallback.

### How It Works

1. **`+layout.svelte`** owns the theme state and provides `toggleTheme()` to `Nav.svelte`
2. On mount: checks `localStorage('theme')` → falls back to `prefers-color-scheme` → defaults to light
3. Sets `document.documentElement.setAttribute('data-theme', theme)`
4. CSS variables in `app.css` swap via `:root` / `[data-theme='light']` and `[data-theme='dark']` selectors
5. 3D scene reacts via `MutationObserver` on `data-theme` attribute changes

### Theme Flow

```
User clicks toggle → +layout.svelte toggleTheme()
  → sets data-theme on <html>
  → saves to localStorage
  → CSS variables swap instantly
  → MutationObserver in SceneManager.js fires
  → updateThemeColors() adjusts fog, wireframes, grid, particles
  → MutationObserver in ProductMonoliths.svelte fires
  → monolith wireframe colors update
```

### Adding Theme-Aware Styles

Always use CSS variables. Never hardcode colors:
```css
/* ✓ Correct */
color: var(--text-primary);
background: var(--surface);
border-color: var(--border);

/* ✗ Wrong */
color: #ffffff;
background: rgba(255, 255, 255, 0.1);
```

## 3D Scene System

A cinematic Three.js background renders behind all page content on every route.

### Architecture

```
+layout.svelte
  └── <Scene />                    # Svelte lifecycle wrapper
       └── SceneManager.js         # Core Three.js logic
            ├── Camera (z=15)
            ├── Renderer (alpha: true, transparent canvas)
            ├── FogExp2 (theme-aware color + density)
            ├── Wireframe cube (rotating, mouse-reactive)
            ├── Inner icosahedron (counter-rotating)
            ├── GridHelper (100×100, scroll-linked drift)
            └── Particle system (500 dust particles)

ProductMonoliths.svelte exists but is currently unused (removed for visual clarity).
```

### Key Files

| File | Responsibility |
|------|---------------|
| `src/lib/three/Scene.svelte` | Canvas element creation, SceneManager lifecycle (mount/destroy) |
| `src/lib/three/SceneManager.js` | Camera, renderer, scene objects, animation loop, resize/scroll/mouse handlers, theme color updates, cleanup |
| `src/lib/three/ProductMonoliths.svelte` | Interactive wireframe panels with hover effects — currently unused, removed from home page for visual clarity |

### CSS Layering

The 3D canvas must remain visible behind all content. This requires:

```
Canvas:  position: fixed; z-index: -1; pointer-events: none;
Body:    background: transparent;
Nav:     background: transparent; backdrop-filter: blur(10px);
Footer:  background: transparent;
```

All page sections must have transparent backgrounds. Do **not** add `background-color` to `main`, `section`, or generic `div` elements — this will occlude the 3D canvas.

### Theme Color Mapping (3D)

| Element | Light Mode | Dark Mode |
|---------|-----------|-----------|
| Fog color | `0xffffff` | `0x000000` |
| Fog density | `0.015` | `0.02` |
| Wireframe color | `0x000000` | `0xffffff` |
| Grid primary | `0x888888` | `0x444444` |
| Grid secondary | `0xcccccc` | `0x222222` |
| Particle color | `0x000000` (opacity 0.2) | `0xffffff` (opacity 0.4) |
| Monolith wireframe | `0x333333` | `0xffffff` | *(unused — monoliths removed)* |

### Modifying the 3D Scene

- All scene setup is in `SceneManager.js` constructor
- Animation loop is `tick()` — called via `requestAnimationFrame`
- Theme updates go in `updateThemeColors()` — called by the `MutationObserver`
- Always clean up resources in `destroy()` (geometries, materials, observers, event listeners)
- The renderer uses `alpha: true` — the CSS `background: var(--bg)` on the canvas provides the background color

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
- [x] 3D cinematic scene — wireframe cube, grid, particles, product monoliths (2026-02-25)
- [x] Light/dark theme toggle with persistence and 3D sync (2026-02-25)
- [x] Theme-aware CSS variables — all hardcoded colors removed (2026-02-25)
- [x] Waitlist capture on Augmentum OS page — mailto:hello@sovren.software (2026-02-24)
- [x] Visage version updated to v0.2.0 (2026-02-24)
- [x] AI agent angle surfaced on MrHaven page (2026-02-24)
- [x] Convergence story strengthened across Augmentum OS, Ecosystem pages (2026-02-24)
- [x] Visage v2/Augmentum OS integration callout added (2026-02-24)
