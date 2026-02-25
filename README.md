# Sovren Software — sovren.software

Marketing site for **Sovren Software**, the company behind the Sovren Stack: a sovereign computing platform spanning OS, identity, and programmable finance.

Live at **[sovren.software](https://sovren.software)**

---

## What Is the Sovren Stack?

The Sovren Stack is three products that together give individuals full-stack digital sovereignty:

| Product | Layer | Status |
|---------|-------|--------|
| **Augmentum OS** | Computing — declarative NixOS system | Ships Summer 2026 |
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
```

**Requirements:** Node.js 18+

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
│   ├── augmentum/+page.svelte       # Augmentum OS product page
│   ├── visage/+page.svelte          # Visage product page
│   ├── mrhaven/+page.svelte         # MrHaven product page
│   └── ecosystem/+page.svelte       # Ecosystem manifesto page
static/
├── CNAME                            # GitHub Pages custom domain
├── fonts/GeistMono-Variable.woff2   # Self-hosted font
├── robots.txt                       # Crawler access rules
├── sitemap.xml                      # All routes for search engines
├── llms.txt                         # AI crawler context file
└── BingSiteAuth.xml                 # Bing Webmaster verification
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
- **Elements:** Rotating wireframe cube, inner icosahedron, infinite grid, volumetric dust particles
- **Interaction:** Mouse parallax on cube rotation, scroll-linked grid drift
- **Theme-aware:** Materials, fog color/density, and particle opacity adapt to light/dark mode
- **Lifecycle:** `Scene.svelte` mounts/unmounts the canvas; `SceneManager.js` handles the animation loop and cleanup

The home page also renders `ProductMonoliths.svelte` — three interactive wireframe panels positioned behind the product cards that respond to hover with tilt, glow, and color transitions.

### Shared Components

Product pages (Augmentum, Visage, MrHaven) share four components with zero local CSS:

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
npm run build        # verify build passes
git push             # GitHub Actions auto-deploys from main
```

- Output: `dist/` directory (static adapter)
- DNS: 4 GitHub Pages A records + `www` CNAME → `sovren-software.github.io`, proxied via Cloudflare
- `static/CNAME` contains `sovren.software` — do not delete

---

## SEO & AI Discoverability

- `app.html` — JSON-LD structured data (Organization + WebSite schemas)
- Each page — `<svelte:head>` with unique title, description, and Open Graph meta
- `static/llms.txt` — full product descriptions for AI crawlers (ChatGPT, Perplexity, Claude)
- `static/sitemap.xml` — all 5 routes
- Cloudflare proxy prevents GitHub/Fastly from blocking AI crawler IPs
- Bing Webmaster Tools verified

---

## IDE Setup

[VS Code](https://code.visualstudio.com/) + [Svelte for VS Code](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode)

For AI-assisted development, see `CLAUDE.md` for the full design system reference, copy guidelines, and product context.
