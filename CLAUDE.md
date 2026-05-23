# Star City Roofing — Claude Code Project Rules

## Project Overview
This is the website for **Star City Roofing**, a locally owned roofing contractor in El Paso, TX.
- **Phone:** (915) 740-5961
- **Address:** 11115 Dyer St, El Paso, TX 79934
- **Google Rating:** 4.9★ with 181+ reviews
- **Tagline:** God. Family. Roofing.

---

## Brand Colors
- **Primary Accent:** `#D1B394` (warm bronze/tan — matches logo)
- **Dark Background:** `#1A1A1A` (charcoal)
- **Mid Dark:** `#2D2D2D`
- **Light Background:** `#F0EEE9`
- **Off White:** `#FAFAF7`
- **Text Gray:** `#5A5A5A`
- **White:** `#FFFFFF`

Use `#D1B394` wherever red (`#C8181F`) currently appears — buttons, borders, accents, hover states, highlights.

---

## Typography
- **Headers:** `Barlow Condensed` — weights 700, 800, 900
- **Body:** `Barlow` — weights 400, 500, 600
- Always load from Google Fonts
- Headers always UPPERCASE with letter-spacing
- Never use Inter, Roboto, Arial, or system fonts

---

## Site Structure
All pages are flat HTML files in the root directory. Do NOT restructure or rename any files.

### Pages
- `index.html` — Homepage
- `about.html` — About page
- `contact.html` — Contact page
- `thank-you.html` — Post form submission
- `roof-replacement-el-paso.html` — Primary service page
- `roof-repair-el-paso.html` — Service page
- `storm-damage-roof-repair-el-paso.html` — Service page
- `flat-roof-coating-el-paso.html` — Service page
- `service-areas.html` — Service area hub
- `roofing-northeast-el-paso.html` — Area page
- `roofing-east-el-paso.html` — Area page
- `roofing-west-el-paso.html` — Area page
- `roofing-upper-valley-el-paso.html` — Area page
- `roofing-horizon-city.html` — Area page
- `roofing-socorro-tx.html` — Area page

### Assets
- All images are in the `/images/` folder — always use real photos, never placeholders
- `style.css` — main stylesheet
- `main.js` — nav toggle and FAQ accordion

---

## SEO Rules — Never Break These
- Every page must have a unique `<title>` tag with location keyword
- Every page must have a unique `<meta name="description">` tag
- Every page must have a `<link rel="canonical">` tag
- Internal links must always use relative paths (e.g. `href="roof-replacement-el-paso.html"`)
- Service pages must link to related area pages
- Area pages must link back to all service pages
- Never remove schema markup (JSON-LD) from pages that have it
- Page URLs (filenames) must never change — they are indexed by Google

---

## Design Rules
- Always mobile responsive — test at 375px, 768px, and 1180px
- Navigation must always include all pages with dropdowns
- Every page must have the sticky header with phone number CTA
- Every page must have the full footer with all links
- Every page must have a quote/lead form
- Never use placeholder text (lorem ipsum)
- All copy must reference El Paso, TX and specific neighborhoods
- Before/after gallery pairs always use `before` + `after` labeled images

---

## Performance Rules
- No external JS libraries unless absolutely necessary
- Images use lazy loading where possible
- CSS variables for all colors — never hardcode hex values in individual rules
- Keep all CSS in `style.css` — no inline styles except for background-image URLs

---

## When Making Changes
1. Always read this CLAUDE.md file first
2. Invoke the frontend-design skill before writing any frontend code
3. Make changes to local files first
4. Preview in browser before pushing to GitHub
5. Only push to GitHub when explicitly told to
6. After pushing to GitHub, Vercel auto-deploys — no extra steps needed

---

## Git & Deployment
- **GitHub repo:** `https://github.com/Milolameraverga/starcity-roofing`
- **Live site:** Vercel auto-deploys from GitHub main branch
- **Commit message format:** short description of what changed (e.g. "update hero color to brand bronze")
- Never commit the `starcity-roofing-website.zip` file
- Never commit the `build_pages.py` file to production

---

## Business Context
Star City Roofing dominates Northeast El Paso (79934) but needs to expand visibility to:
- West El Paso (79912, 79922, 79932) — currently zero GBP ranking there
- Upper Valley (79932)
- All copy and new pages should reinforce service in these areas
