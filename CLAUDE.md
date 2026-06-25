# CLAUDE.md

Guidance for AI assistants working in this repository.

## What this project is

A marketing website for **ゆめハウス (Yume House)**, a real-estate office in
Kumamoto, Japan (operated by Blooo Inc.). The site is built as static HTML/CSS
and then **shipped through WordPress** using an Astra child theme that acts as a
"delivery box": WordPress provides URLs and the contact form backend, while the
visible page is the bundled static HTML rendered verbatim — Astra's header,
footer, and styles are deliberately bypassed.

The original Japanese design notes for this approach live in `instructions.md`.

## Repository layout

```
.
├── astra-child_0204/        # ★ The deliverable: WordPress Astra child theme
│   ├── style.css            # Theme header (declares Template: astra)
│   ├── functions.php        # Enqueues style.css, loads contact handler
│   ├── tpl-static-local.php  # ★ Core renderer (see below)
│   ├── front-page.php       # 1-liner → require tpl-static-local.php
│   ├── page-*.php           # 1-liner per page → require tpl-static-local.php
│   ├── inc/contact-submit.php # admin-post.php contact form handler
│   ├── assets/site/         # ★ Bundled static site (served verbatim)
│   │   ├── 1._home/code.html ... 11._privacy/code.html
│   │   ├── shared/          # base.css, tailwind-config.js, theme-init.js
│   │   ├── estate-images/   # generated hero/property/banner images
│   │   └── image2..4/, Image/  # logos, store photos
│   ├── scripts/zip-theme.sh # Packages the theme into ../astra-child_0204.zip
│   └── README.md            # Japanese deployment instructions
├── tools/
│   └── rebuild_yume_estate_site.py  # ★ Generator for the code.html pages
├── Html/                    # Reference / earlier static exports (NOT shipped)
│   ├── stitch_yume_site1New/  # Older "Stitch" export of the same pages
│   ├── Nagaoka/             # Separate static mirror of another site
│   ├── reports/             # Design audit / planning markdown
│   └── ゆめハウス　ロゴ・店舗写真/  # Raw logo & store photo assets
├── docs/codex-memos/        # Dated design/work memos (Japanese)
└── instructions.md          # Original architecture rationale (Japanese)
```

The starred (★) items are the active codebase. `Html/` holds reference material
and older exports — do not assume edits there affect the live site.

## How the theme works (read this before editing)

`astra-child_0204/tpl-static-local.php` is the heart of the project. The flow:

1. Every WordPress page uses it, either via the `Static Local (Theme Ignored)`
   page template or, more commonly, via the matching `page-{slug}.php` /
   `front-page.php` stub that simply does `require __DIR__ . '/tpl-static-local.php';`.
2. It maps the current page **slug** to a static file under `assets/site/`
   using the `astra_child_0204_static_local_routes()` table.
3. It reads that `code.html`, then rewrites it on the fly:
   - Injects `<base href=".../assets/site/{dir}/">` so relative `css/js/img`
     paths resolve against the theme directory.
   - Rewrites inter-page links (`../2._property_search/code.html`) to real
     WordPress URLs (`/property-search/`).
   - Rewrites bare `#fragment` links to absolute `permalink#fragment`.
   - On the `contact` page, rewrites the `<form>` to post to `admin-post.php`
     with a nonce + honeypot.
4. It echoes the HTML and `exit`s — it never calls `get_header`, `get_footer`,
   `wp_head`, or `wp_footer`, so the Astra parent theme contributes nothing.

### Slug → file map

| Page slug          | Static file                          |
| ------------------ | ------------------------------------ |
| `home` (+ front page) | `assets/site/1._home/code.html`   |
| `property-search`  | `assets/site/2._property_search/code.html` |
| `property-details` | `assets/site/3._property_details/code.html` |
| `guide-flow`       | `assets/site/4._guide_flow/code.html` |
| `our-strengths`    | `assets/site/5._our_strengths/code.html` |
| `testimonials`     | `assets/site/6._testimonials/code.html` |
| `company-info`     | `assets/site/7._company_info/code.html` |
| `contact`          | `assets/site/8._contact/code.html` |
| `rental-business`  | `assets/site/9._rental_business/code.html` |
| `faq`              | `assets/site/10._faq/code.html` |
| `privacy`          | `assets/site/11._privacy/code.html` |

When adding a page you must touch three places: the route table in
`tpl-static-local.php`, a `page-{slug}.php` stub, and the `PAGES` dict in the
generator (see below).

## The page generator (source of truth for content)

`tools/rebuild_yume_estate_site.py` **generates** the `code.html` files. It is a
zero-dependency Python script (stdlib only) where each page is a function
(`home_page()`, `contact_page()`, …) composed from shared helpers (`header()`,
`footer()`, `hero()`, `section()`, `card()`, `grid()`, `cta()`, etc.). Shared
constants near the top hold phone number, address, listing URLs (SUUMO / at
home), the asset-version string (`VERSION`), and the image path map (`IMAGES`).

**Treat the Python generator as the source of truth for page markup.** To change
copy, layout, images, or navigation, edit the relevant function in the script
and regenerate — do not hand-edit `code.html` (it will be overwritten):

```sh
python3 tools/rebuild_yume_estate_site.py
```

This writes directly into `astra-child_0204/assets/site/{slug}/code.html`.

Caveat: not every static page is necessarily produced by the generator in every
state of the repo, and `Html/stitch_yume_site1New/` is a separate older export
that differs from `assets/site/`. If a `code.html` looks generated (contains the
`estate-*` class names and the `?v={VERSION}` query strings), regenerate via the
script; if you're unsure, diff before and after to confirm your change is the
only delta.

## Styling

- All pages share `assets/site/shared/base.css` (~1400 lines, hand-written CSS
  with a `:root` token block and `estate-*` BEM-ish class names like
  `estate-header`, `estate-button`, `estate-card`). This is the real stylesheet.
- `shared/tailwind-config.js` and `shared/theme-init.js` are present from the
  original Stitch export; the production look comes from `base.css`.
- Fonts: Google Fonts (Plus Jakarta Sans, Noto Sans JP, Noto Serif JP).
- Brand color is a deep blue (`#16324f` / "strong blue" passes documented in
  `docs/codex-memos/`).
- Asset cache-busting uses a `?v={VERSION}` query string defined in the
  generator (e.g. `20260521-strongblue1`); bump `VERSION` when assets change.

## Contact form

`inc/contact-submit.php` registers an `admin-post.php` handler
(`astra_child_0204_contact_submit`) for both logged-in and anonymous users. It:

- verifies a WordPress nonce, checks a hidden `website` honeypot field,
- sanitizes `name / kana / tel / email / store / message` and requires all,
- sends mail via `wp_mail()` to `hiroto.shimokawa@blooo.co.jp`,
- redirects back with `?contact_sent=1` or `?contact_error=1`, which
  `tpl-static-local.php` turns into a success/error flash banner.

If you change form field names in the `8._contact` HTML, update the handler to
match.

## Common workflows

**Edit page content/layout** → edit `tools/rebuild_yume_estate_site.py` →
`python3 tools/rebuild_yume_estate_site.py` → verify the diff in
`astra-child_0204/assets/site/*/code.html`.

**Edit global styling** → edit `astra-child_0204/assets/site/shared/base.css`
directly (not generated).

**Add a new page** → add to the generator's `PAGES`/`NAV`, add a route in
`tpl-static-local.php`, add a `page-{slug}.php` stub, regenerate.

**Package for WordPress upload** →
`bash astra-child_0204/scripts/zip-theme.sh` (produces
`astra-child_0204.zip` in the repo root, which is gitignored). On the WP side:
install/activate Astra, upload & activate this child theme, create fixed pages
with the slugs above, and set the front page to `home` under
Settings → Reading.

**Preview locally** → there is no build server for the theme; open a
`code.html` in a browser, or serve `assets/site/` statically. The Astra link
rewriting only happens inside WordPress, so inter-page links use the relative
`../{n}._{name}/code.html` form when viewed as plain files.

## Conventions & guardrails

- **PHP**: theme functions are namespaced with the `astra_child_0204_` prefix;
  files use `declare(strict_types=1)`. Always escape output (`esc_url`,
  `esc_attr`, `esc_html`) and sanitize input (`sanitize_*`, `wp_unslash`),
  matching the existing code. Keep the "no Astra header/footer" rule intact.
- **Python generator**: stdlib only, no external dependencies. Keep HTML escaped
  via the `e()` / `escape()` helper.
- **Don't hand-edit generated `code.html`** — change the generator instead.
- **`Html/` and `docs/` are reference**, not the shipped site. Don't wire them
  into the theme.
- Generated/local artifacts are gitignored: `*.zip`, `.DS_Store`, `.vscode/`,
  `reference-sites/`, `related-assets/`, `Html_Copy/`.
- The site content and many docs/memos are in Japanese; preserve Japanese copy
  exactly and keep new user-facing strings in Japanese.

## Git / branching

- Active development branch for this work: `claude/claude-md-docs-7qaog4`.
- Push with `git push -u origin <branch>`. Do not open a pull request unless
  explicitly asked.
