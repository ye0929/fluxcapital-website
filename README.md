# Flux Capital Ltd — static website

Pure HTML/CSS/JS, no backend, no build step, no external CDNs. Open `index.html` locally or upload to any static host.

## Files
- `index.html` — single page: hero, About, Business Scope (with "no client funds / no advice" note), Contact (mailto info@fluxcapital.info), footer disclaimer.
- `styles.css` — dark navy theme with gold accent, responsive (mobile nav collapses to logo + language button).
- `i18n.js` — EN/简体中文 dictionary and language switcher.
- `404.html` — bilingual not-found page (uses root-absolute paths `/styles.css`, so it renders properly once hosted).
- `favicon.svg` — logo/icon.
- `robots.txt` — allows all crawlers.
- `preview-en.png`, `preview-zh.png` — screenshots (not needed on the server).

## Language switching
Elements carry `data-i18n="key"`; `i18n.js` replaces their text from the dictionary.
Priority: `?lang=zh|en` URL parameter → saved choice in `localStorage` (`fluxcapital-lang`) → browser language (zh* → Chinese, else English).
The 中文/EN button toggles and saves the choice.

## Uploading to GoDaddy later
1. GoDaddy cPanel/Web Hosting: open File Manager → `public_html/`, upload all files (except README/previews if you like). For a custom 404, add to `.htaccess`: `ErrorDocument 404 /404.html`.
2. Or host free on GitHub Pages / Cloudflare Pages / Netlify and in GoDaddy DNS point `fluxcapital.info` (A/CNAME records) to that host as its docs describe.
3. Visit https://fluxcapital.info and check both `?lang=en` and `?lang=zh`.
