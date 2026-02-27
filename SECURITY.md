# Security Headers — Cloudflare Configuration

The site is served from GitHub Pages (which cannot set HTTP response headers) proxied
through Cloudflare. The `static/_headers` file in this repo is the authoritative source
of truth for all security headers. It will be enforced automatically if the site ever
migrates to Cloudflare Pages.

Until then, configure the following directly in Cloudflare.

---

## Setup: Cloudflare Transform Rules

**Location:** Cloudflare Dashboard → `sovren.software` → Rules → Transform Rules → Modify Response Header → Create Rule

**Rule name:** `Security Headers`

**When incoming requests match:** `(hostname eq "sovren.software" or hostname eq "www.sovren.software")`

**Then:** Add the following **Set** operations (static values):

| Header | Value |
|--------|-------|
| `X-Frame-Options` | `DENY` |
| `X-Content-Type-Options` | `nosniff` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=()` |
| `Cross-Origin-Opener-Policy` | `same-origin` |
| `Cross-Origin-Resource-Policy` | `same-origin` |
| `Content-Security-Policy` | `default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; font-src 'self'; img-src 'self' data: https:; connect-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self' mailto:` |

**Note:** Do not configure `Strict-Transport-Security` (HSTS) here — Cloudflare manages
HSTS automatically when "Always Use HTTPS" is enabled. Enable it under:
SSL/TLS → Edge Certificates → HTTP Strict Transport Security (HSTS) → Enable with
`max-age=63072000`, `includeSubDomains`, and `preload` checked.

---

## Verification

After saving the rule, verify headers are present:

```bash
curl -sI https://sovren.software | grep -E "x-frame|x-content|referrer|permissions|csp|cross-origin"
```

Expected output should include all headers listed above.

---

## Future Migration

Migrating to **Cloudflare Pages** (instead of GitHub Pages) will enforce these headers
automatically via `static/_headers` without any dashboard configuration. Steps:

1. Create a Cloudflare Pages project pointing to this repo
2. Set build command: `npm run build`, output dir: `dist`
3. Add custom domain `sovren.software` in Cloudflare Pages settings
4. Update DNS: replace the 4 GitHub Pages A records with Cloudflare Pages CNAME
5. Remove `static/CNAME` (Cloudflare Pages does not use it)
6. Update `deploy.yml` to use `cloudflare/wrangler-action@v3` with
   `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` repository secrets
7. Disable GitHub Pages in repository settings
