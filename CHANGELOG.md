# Changelog

All notable changes to the Sovren Software website are documented here.

---

## [1.0.0] — 2026-02-26

### Added
- Favicon suite: `favicon.svg` (wireframe cube mark), `favicon.ico`, `favicon-32x32.png`, `favicon-16x16.png`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`
- Web app manifest (`manifest.webmanifest`) with PWA metadata, icon references, `theme_color`, and `background_color`
- OG image (`og-image.png`, 1200×630) generated via Satori with actual Geist Mono TTF font — consistent rendering across all social platforms
- OG image generator script (`scripts/generate-og.js`) — run with `npm run generate-og`
- Open Graph `og:image`, `og:type`, `og:site_name` tags in `app.html` as global defaults; per-page `og:url` and `og:title`/`og:description` already present
- Twitter Card meta tags (`twitter:card`, `twitter:site`, `twitter:title`, `twitter:description`, `twitter:image`) on all pages
- `<link rel="canonical">` on all five routes
- `<meta name="robots" content="noindex">` on 404 error page
- `<meta name="description">` on 404 error page
- Security headers file (`static/_headers`): authoritative reference for `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`, `Strict-Transport-Security`, `Content-Security-Policy`, `Cross-Origin-Opener-Policy`, `Cross-Origin-Resource-Policy`
- `Content-Security-Policy`, `Referrer-Policy`, `X-Content-Type-Options` enforced at browser level via `<meta http-equiv>` in `app.html`
- `SECURITY.md` — exact Cloudflare Transform Rules to configure CDN-level headers; verification command; future migration steps
- Font preload `<link rel="preload">` for `GeistMono-Variable.woff2` in `app.html` (eliminates FOUT, improves LCP)
- `<meta name="theme-color" content="#000000">` in `app.html`
- `--fs-footer-link` and `--fs-footer-copy` CSS custom properties in `app.css` (live bug fix — were undefined, footer font sizes were indeterminate)
- `@media (prefers-reduced-motion: reduce)` global CSS rule in `app.css`
- `prefers-reduced-motion` runtime check in `SceneManager.js` — all animations halt for users with vestibular/motion sensitivity; respects dynamic changes via `MediaQueryList` event listener
- `<h2 id="products-heading" class="sr-only">` on home page products section (heading hierarchy fix for screen readers and SEO)
- `aria-labelledby="products-heading"` on home page products `<section>`
- Skip navigation link (`<a href="#main-content">`) in `+layout.svelte` — appears on keyboard focus (WCAG 2.4.1 Level A)
- `id="main-content"` on layout slot wrapper — valid skip-link target for all pages
- `aria-label="Primary"` on `<nav>` in `Nav.svelte`
- `aria-label="Footer"` on `<nav>` in footer (`+layout.svelte`)
- `LICENSE` — proprietary, all rights reserved, © 2025–2026 Sovren Software
- `CHANGELOG.md`
- `.nvmrc` — Node 20
- `engines: { "node": ">=20" }` in `package.json`
- ESLint (`eslint`, `eslint-plugin-svelte`, `globals`) — `npm run lint`
- Prettier (`prettier`, `prettier-plugin-svelte`) — `npm run format`
- `svelte-check` — `npm run check`
- `eslint.config.js` and `.prettierrc` configuration files
- Dependabot config (`.github/dependabot.yml`) — weekly npm dependency PRs
- `vite.config.js` `chunkSizeWarningLimit: 600` to suppress Three.js bundle size warning
- Satori + `@resvg/resvg-js` as devDependencies for OG image generation

### Fixed
- `SceneManager.destroy()` memory leak — event listeners now use stored bound references (`_onResize`, `_onScroll`, `_onMouseMove`) and are correctly removed on component unmount
- `SceneManager` Three.js geometry and material disposal in `destroy()` — GPU memory no longer accumulates across page navigations
- `SceneManager` `powerPreference` changed from `"high-performance"` to `"default"` — prevents forcing discrete GPU on battery-powered devices
- `SceneManager` `getDelta()` removed — was called after `getElapsedTime()`, always returned near-zero, was unused
- `SceneManager` catch block changed from `catch (e)` to bare `catch {}` (unused variable)
- `ProductHero.svelte` — added `// @ts-nocheck` to suppress pre-existing Three.js 0.183 type incompatibilities (not regressions)
- `ProductMonoliths.svelte` — same `// @ts-nocheck` fix
- Mr. Haven naming: `MrHaven` → `Mr. Haven` in all `stackNote` props (Augmentum OS and Mr. Haven pages)
- Visage version: `v0.1.0` → `v0.2.0` in `llms.txt`
- `llms.txt` Augmentum OS GitHub link: removed dead `aegis-os` repo reference, replaced with org URL
- Removed dead `asciiArt` variable from `+page.svelte`
- Removed unused `CtaSection` import from `ecosystem/+page.svelte`
- CLAUDE.md token values synced to match `app.css`: `--space-7xl` (8rem), `--nav-h` (80px), `--max-w-prose` (800px), `--max-w-body` (520px), `--max-w-tagline` (640px)
- CLAUDE.md 3D scene description: "inner icosahedron" → "inner octahedron" (matches actual `OctahedronGeometry` in code)
- CLAUDE.md Visage version: `v0.1.0` → `v0.2.0`
- Sitemap: added `<lastmod>2026-02-26</lastmod>` to all five URLs

### Changed
- `package.json` version: `0.0.0` → `1.0.0`
- `Overview.svelte` `stackNote` prop renders via `{@html}` instead of plain text — enables anchor links in stack notes
- All three product page `stackNote` props now contain working internal anchor links to the other two products in the stack
- CI pipeline (`deploy.yml`) now runs `npm run check` and `npm run lint` before `npm run build`
- README updated: Node requirement (18+ → 20+), all new scripts, static asset inventory, deployment security header guidance, code quality section, license section

---

## 2026-02-25

### Added
- 3D cinematic scene — wireframe cube, grid, particles
- Light/dark theme toggle with localStorage persistence and 3D sync
- Theme-aware CSS variables — all hardcoded colors removed

## 2026-02-24

### Added
- Waitlist capture on Augmentum OS page (mailto)
- AI agent angle on MrHaven page
- Convergence story across Augmentum OS and Ecosystem pages

### Changed
- Visage version updated to v0.2.0
- Visage v2/Augmentum OS integration callout added
