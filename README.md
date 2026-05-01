# Sovren Software — sovren.software

Marketing site for **Sovren Software**, the company behind customer-owned infrastructure for reliable agentic work: Esver OS for verified workflows, Visage for local identity, and Mr. Haven for programmable capital.

Live at **[sovren.software](https://sovren.software)**

---

## What Is the Sovren Stack?

The Sovren Stack is three products that keep work, identity, and assets under owner control:

| Product | Layer | Status |
|---------|-------|--------|
| **Esver OS** | Work — verified executable skills on customer-owned infrastructure | Private development |
| **Visage** | Identity — local face auth via PAM + ONNX | Live · v0.2.0 · MIT |
| **MrHaven** | Finance — non-custodial USDC time vault on Base L2 | Live on mainnet |

This website is the public face of all three products and the ecosystem manifesto.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | SvelteKit 2.x + `@sveltejs/adapter-static` |
| 3D Scene | Three.js (wireframe cube, grid, particles, product monoliths) |
| Animation | GSAP 3.x |
| Font | Geist Mono Variable (self-hosted) |
| Build | Vite 7.x |
| Deploy | GitHub Actions → GitHub Pages → Cloudflare proxy |
| Domain | `sovren.software` (CNAME in `static/CNAME`) |

---

## Quick Start

```bash
npm install
npm run dev          # http://localhost:5173
npm run build        # static output → dist/
npm run preview      # preview production build
npm run check        # svelte-check type validation
npm run lint         # ESLint
npm run format       # Prettier
npm run generate-og  # regenerate static/og-image.png
```

**Requirements:** Node.js 20+ (see `.nvmrc`)

---

## Project Structure

```
src/
├── app.css                          # Global design tokens + theme definitions
├── app.html                         # HTML shell with JSON-LD structured data
├── lib/
│   ├── Nav.svelte                   # Navigation with theme toggle
│   ├── ProductHero.svelte           # Reusable hero section
│   ├── Overview.svelte              # Reusable overview + spec table
│   ├── PillarList.svelte            # Reusable numbered feature list
│   ├── CtaSection.svelte            # Reusable call-to-action section
│   └── three/
│       ├── Scene.svelte             # Svelte wrapper for Three.js canvas lifecycle
│       ├── SceneManager.js          # Core 3D scene: camera, renderer, animation loop, theme colors
│       └── ProductMonoliths.svelte  # Interactive 3D product panels on home page
├── routes/
│   ├── +layout.svelte               # Global layout: Scene, Nav, footer, theme logic
│   ├── +layout.js                   # Prerender flag (static site generation)
│   ├── +page.svelte                 # Home page: hero, product grid, thesis
│   ├── +error.svelte                # 404 error page
│   ├── esver/+page.svelte       # Esver OS product page
│   ├── visage/+page.svelte          # Visage product page
│   ├── mrhaven/+page.svelte         # MrHaven product page
│   └── ecosystem/+page.svelte       # Ecosystem manifesto page
static/
├── CNAME                            # GitHub Pages custom domain
├── _headers                         # Security headers (Cloudflare Pages / reference for CF Transform Rules)
├── fonts/GeistMono-Variable.woff2   # Self-hosted font
├── favicon.ico                      # 32×32 ICO
├── favicon.svg                      # SVG favicon (wireframe cube mark)
├── favicon-32x32.png                # 32×32 PNG
├── favicon-16x16.png                # 16×16 PNG
├── apple-touch-icon.png             # 180×180 for iOS
├── icon-192.png                     # PWA icon
├── icon-512.png                     # PWA icon
├── manifest.webmanifest             # Web app manifest (PWA)
├── og-image.png                     # 1200×630 OG image (Geist Mono rendered via Satori)
├── robots.txt                       # Crawler access rules
├── sitemap.xml                      # All routes with lastmod dates
├── llms.txt                         # AI crawler context file
└── BingSiteAuth.xml                 # Bing Webmaster verification
scripts/
└── generate-og.js                   # OG image generator (Satori + Resvg, uses Geist Mono TTF)
```

---

## Architecture

### Theme System (Light / Dark)

The site supports light and dark modes with a cinematic toggle in the navigation.

- **Default:** Light mode (`:root` / `[data-theme='light']`)
- **Toggle:** Button in `Nav.svelte` calls `toggleTheme()` in `+layout.svelte`
- **Persistence:** `localStorage.getItem('theme')` with system preference fallback via `prefers-color-scheme`
- **Mechanism:** `data-theme` attribute on `<html>` drives CSS variable swaps
- **3D sync:** `SceneManager.js` observes `data-theme` via `MutationObserver` and updates fog, wireframe, grid, and particle colors in real time

All colors use CSS custom properties — no hardcoded color values in components.

### 3D Scene (Three.js)

A full-viewport 3D background renders behind all page content:

- **Canvas:** `position: fixed`, `z-index: -1`, `pointer-events: none` — sits behind all UI
- **Elements:** Rotating wireframe cube, inner octahedron, infinite grid, volumetric dust particles
- **Interaction:** Mouse parallax on cube rotation, scroll-linked grid drift
- **Theme-aware:** Materials, fog color/density, and particle opacity adapt to light/dark mode
- **Lifecycle:** `Scene.svelte` mounts/unmounts the canvas; `SceneManager.js` handles the animation loop and cleanup
- **Accessibility:** Animations fully disabled when `prefers-reduced-motion: reduce` is set — checked at runtime and via CSS media query
- **Memory:** `destroy()` correctly removes all event listeners using stored bound references, disposes all Three.js geometries and materials

`ProductMonoliths.svelte` exists as an interactive wireframe panel component but is currently unused — it was removed from the home page to reduce visual clutter.

### Shared Components

Product pages (Esver, Visage, MrHaven) share four components with zero local CSS:

| Component | Props | Purpose |
|-----------|-------|---------|
| `ProductHero.svelte` | title, category, status, tagline, size | Hero section |
| `Overview.svelte` | lead, specs[], stackNote, slot | Overview with spec table |
| `PillarList.svelte` | label, pillars[] | Numbered feature list |
| `CtaSection.svelte` | title, body, actions[] | Call-to-action with buttons |

### Design System

Centralized in `src/app.css` with 60+ design tokens covering:

- **Colors** — Theme-aware via `--bg`, `--surface`, `--border`, `--text-primary/secondary/muted/ghost`
- **Typography** — Fluid `clamp()` scale from `--fs-hero` down to `--fs-label-xs`
- **Spacing** — `--space-xs` through `--space-7xl`
- **Layout** — `--max-w`, `--max-w-prose`, `--nav-h`, `--z-nav`
- **Transitions** — `--transition-fast`, `--transition-slow`

Rules: one typeface only, no color for emphasis (use weight/spacing), all values via tokens.

---

## Deployment

```bash
npm run check        # must pass before pushing
npm run lint         # must pass before pushing
npm run build        # verify build passes
git push             # GitHub Actions auto-deploys from main
```

- Output: `dist/` directory (static adapter)
- DNS: 4 GitHub Pages A records + `www` CNAME → `sovren-software.github.io`, proxied via Cloudflare
- `static/CNAME` contains `sovren.software` — do not delete
- CI runs `check → lint → build` in sequence before deploying

### Security Headers

GitHub Pages cannot set HTTP response headers. Security is enforced at two levels:

1. **Browser-level (active now):** `Content-Security-Policy`, `Referrer-Policy`, and `X-Content-Type-Options` are set via `<meta http-equiv>` in `app.html`
2. **CDN-level (manual):** `X-Frame-Options`, `HSTS`, `COOP`, `CORP`, and `Permissions-Policy` must be configured as Cloudflare Transform Rules — see `SECURITY.md` for exact steps

The `static/_headers` file is the authoritative record of all required headers and will be auto-enforced if the site ever migrates to Cloudflare Pages.

---

## SEO & AI Discoverability

- `app.html` — JSON-LD structured data (Organization + WebSite schemas), favicon suite, manifest, OG/Twitter defaults
- Each page — `<svelte:head>` with unique title, description, Open Graph meta, Twitter Card tags, and canonical URL
- `static/og-image.png` — 1200×630 social preview image rendered with actual Geist Mono font via Satori
- `static/llms.txt` — full product descriptions for AI crawlers (ChatGPT, Perplexity, Claude)
- `static/sitemap.xml` — all 5 routes with `<lastmod>` dates
- Cloudflare proxy prevents GitHub/Fastly from blocking AI crawler IPs
- Bing Webmaster Tools verified

## Code Quality

- **Linting:** ESLint with `eslint-plugin-svelte` — run via `npm run lint`
- **Type checking:** `svelte-check` — run via `npm run check`
- **Formatting:** Prettier with `prettier-plugin-svelte` — run via `npm run format`
- **CI:** GitHub Actions runs `check → lint → build` on every push to `main`
- **Dependencies:** Dependabot configured for weekly npm dependency PRs

---

## Email Signup + Funnel (Brevo)

The site now routes the Esver CTA through a configurable marketing URL in `src/lib/marketing.js`.

### 1) Wire the signup link

Edit `src/lib/marketing.js` and set:

```js
export const BREVO_SIGNUP_URL = '__SET_BREVO_SIGNUP_URL__';
```

to your Brevo hosted signup form URL (example format: `https://xxxx.sibforms.com/serve/...`).

If not set, the CTA falls back to `mailto:` so the button still functions.

### 2) Brevo dashboard setup (minimal)

1. Create list: `MAIN_NEWSLETTER`
2. Create a sign-up form (Marketing → Forms)
3. Enable double opt-in
4. Set destination list to `MAIN_NEWSLETTER`
5. Copy hosted form URL into `src/lib/marketing.js`
6. Create automation: trigger on contact added to `MAIN_NEWSLETTER`
7. Add one email step (delay 1–2 minutes), then activate

### 2.5) Phase 2 cohesive UX behavior

- The Esver page now includes a native launch briefing section with an embedded Brevo form iframe.
- If the signup URL is not an embeddable `http(s)` URL, the page automatically falls back to a direct CTA link.
- The closing CTA now routes users deeper into the ecosystem (`/ecosystem` + `/visage`) to avoid duplicate signup prompts.

### 3) Single welcome email template (v1)

Use this as the first and only automation email for now:

**Subject:** Welcome to Sovren — launch briefing subscribed  
**Preview:** You are in. We will send one launch briefing and occasional high-signal updates.

**Body:**

```text
You are subscribed to the Sovren launch briefing.

What you should expect:
- One operational briefing when Esver OS goes live
- Occasional high-signal updates across the Sovren Stack (OS, identity, programmable finance)
- No spam. No feed noise. No growth-hack sequences.

Why this exists:
Sovren builds software for operators who want leverage without surrendering control.
Privacy is not a feature. Sovereignty is the baseline.

Explore the stack:
- Esver OS: https://sovren.software/esver
- Visage: https://sovren.software/visage
- MrHaven: https://sovren.software/mrhaven

— Sovren Software
https://sovren.software
```

### 4) Verification checklist

1. Open `/esver` and verify the launch briefing section renders.
2. Confirm iframe form loads (or fallback button appears if embed unavailable).
3. Submit a test email and confirm contact lands in `MAIN_NEWSLETTER`.
4. Confirm the single welcome automation email is sent.
5. Confirm `/ecosystem` and `/visage` links in final CTA work.

---

## IDE Setup

[VS Code](https://code.visualstudio.com/) + [Svelte for VS Code](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode)

For AI-assisted development, see `CLAUDE.md` for the full design system reference, copy guidelines, and product context.

## License

Proprietary — © 2025–2026 Sovren Software. All rights reserved. See `LICENSE`.

Exception: [Visage](https://github.com/sovren-software/visage) is MIT-licensed and open source.
