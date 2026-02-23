# sovren-website

Marketing site for Sovren Software at `sovren.software`.

---

## Stack

- **Framework**: Vite + Svelte 5
- **Router**: svelte-spa-router (hash-based — required for GitHub Pages static hosting)
- **Font**: Geist Mono Variable (self-hosted, `public/fonts/GeistMono-Variable.woff2`)
- **Deploy**: GitHub Actions → `sovren-software.github.io`, CNAME `sovren.software`

## Design System

```
--bg: #000000
--text-primary: #ffffff
--text-secondary: rgba(255,255,255,0.6)
--text-muted: rgba(255,255,255,0.25)
--border: rgba(255,255,255,0.1)
--max-w: 1200px
--font-mono: 'Geist Mono Variable', monospace
```

White `#ffffff` contrast sections are used for overview/CTA blocks within product pages. Never add a second typeface. Never use color for emphasis — use weight and letter-spacing only.

## Routing

| Hash route | Page |
|---|---|
| `#/` | Home |
| `#/augmentum` | Augmentum.svelte |
| `#/visage` | Visage.svelte |
| `#/mrhaven` | MrHaven.svelte |
| `#/ecosystem` | Ecosystem.svelte |
| `*` | NotFound.svelte |

Active nav state: `import { location } from 'svelte-spa-router'` → `$location.startsWith(path)` in Nav.svelte.

Page transitions: `{#key routeKey}<div in:fade={{ duration: 150, delay: 50 }} out:fade={{ duration: 100 }}><Router {routes}/></div>{/key}` in App.svelte.

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

CNAME file at `public/CNAME` contains `sovren.software` — Vite copies it to `dist/` at build time. Do not delete it.

GitHub Pages custom domain is set via API (`gh api repos/sovren-software/sovren-software.github.io/pages`). DNS is 4 A records (185.199.108-111.153) + www CNAME at Namecheap.

## Known Limitations

- No email capture / waitlist on Augmentum OS page (external link to `augmentum.computer` only)
- No blog platform for the content launch strategy (teaser article, X thread)
- `augmentum.computer` has no landing page yet
- MrHaven SDK not yet documented on the site
- No visual that shows the three products converging (convergence story is text-only)

## Remaining Work

- [ ] `augmentum.computer` holding page or redirect
- [ ] Waitlist capture on Augmentum OS page
- [ ] Blog/article platform for the two-article launch sequence
- [ ] MrHaven SDK section on the MrHaven page
- [ ] Visual convergence diagram on Ecosystem page
- [ ] X profile update (currently MrHaven-branded)
