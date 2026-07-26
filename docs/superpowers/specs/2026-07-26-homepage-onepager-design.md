# Homepage One-Pager Redesign — Design Spec

Date: 2026-07-26
Status: Approved by user (design phase)
Scope: EN homepage (`index.md`) only. All 9 localized homepages stay unchanged.

## Goal

Replace the current EN homepage with a minimalistic editorial one-pager that mirrors
the approved reference screenshot: oversized headline, interactive journey map,
interactive constraint canvas, photo strip, three-column row, and a bottom CTA bar.
Visual language follows the uncommitted "Evidence Atlas" layer (cool grey-white page,
navy ink, hairline rules, one amber signal) already used by the services page.

## Decisions (from brainstorming)

- Mirror the screenshot's **structure and style**, reusing existing site content where it fits.
- Both widgets (journey map, constraint canvas) are **interactive**, client-side JS only.
- **EN first** — locales keep the old sections until the EN result is reviewed.
- **Replace fully** — old EN homepage sections (analysis-problem, ai-costs-outcomes,
  strategic-context, credibility, faq, explore-site, contact) leave the homepage.
- Implementation via **new page-builder section partials** (Approach A), not a monolithic
  layout and not restyling shared partials (which would leak into locales).

Authorization note: `docs/site-content-design-contract.md` §3 protects the homepage
unless explicitly instructed; the user explicitly instructed this redesign.

## Architecture

- Six new partials in `_includes/sections/`, registered in the `page-builder.html`
  `case/when` dispatcher.
- `index.md`: `sections:` list replaced with the six new keys. Frontmatter otherwise
  unchanged (keeps `locale: en`, `home_locale: true` for the language switcher).
- One new stylesheet `assets/home-canvas.css`, loaded only for the EN homepage via the
  existing conditional pattern in `_includes/head.html`. It consumes `--ea-*` tokens
  from `assets/evidence-atlas.css` (loaded earlier in the cascade) and adds no new
  global tokens beyond a `--hc-*` namespace if needed.
- One new script `assets/home-canvas.js`, deferred, EN homepage only, for the two
  interactive widgets. No dependencies, no build step.
- New English-only data keys in `_data/home.yml`. Existing keys are untouched —
  the 9 locale homepages continue to resolve the old sections and keys.

## Sections (top to bottom)

1. **`hero-canvas`** — Eyebrow, oversized tight-tracked headline adapted from existing
   hero copy ("SAP operations that are easier to run — and easier to improve."),
   lead paragraph (existing hero lead), amber CTA button ("Start SAP analysis" →
   `/services/ams-cost-center-catalyst/`), muted microcopy line. Right column holds
   the journey map.
2. **`journey-map`** — Horizontal 5-node rail with connecting SVG line, reusing the
   services-page taxonomy: 01 AMS reliability, 02 Master data, 03 Logistics & planning,
   04 Integration & automation, 05 Practical AI. Hover/focus/click activates a node
   and swaps a detail card (statement + "typical work" bullets condensed from
   `focus_areas` in `_data/home.yml`). Default active node: 01.
3. **`constraint-canvas-home`** — Eyebrow "Constraint canvas", title "What needs
   attention first?", four native `<select>` controls (business impact, recurrence,
   manual work, change horizon) and a "Recommended next action" panel. A small JS
   rule table maps combinations to one of ~8 recommendations, each linking to the
   matching service page.
4. **`photo-strip`** — The three existing WebP photos in `assets/img/services/`
   (logistics-terminal, data-operations, collaborative-workshop) with hairline
   caption labels.
5. **`tri-columns`** — Three columns: "Clarity in 4 steps" (align → focus → act →
   sustain, condensed from `engagement_framework`), "Practical AI. Safe by design."
   (three principles with Material Symbols icons, from existing AI content), and
   "Ideas from practice" (3 latest posts via Liquid from `_blog`, dated, plus a
   "view all" link to `/blog/`).
6. **`cta-bar`** — "Ready to map your constraint?" + primary button (LinkedIn,
   matching the current site CTA) + email link, rendered above the existing footer.

## Data flow

New keys in `_data/home.yml` (English-only):

- `home_hero` — eyebrow, title, lead, CTA label/URL, microcopy.
- `home_journey` — 5 nodes × { number, title, statement, bullets[] }.
- `home_canvas` — 4 selects × { label, options[] }, and `rules[]` mapping
  option combinations → { recommendation, url }.
- `home_steps` — 4 steps × { number, title, detail }.
- `home_ai_principles` — 3 items × { icon, title, detail }.
- `home_cta` — title, primary action, email.

"Ideas from practice" needs no data: `site.blog | sort: 'date' | reverse | slice: 0, 3`.

## Error handling & accessibility

- No-JS degradation: journey map renders node 01's card server-side; constraint
  canvas shows a default recommendation. Both widgets enhance only when JS loads.
- Journey nodes are real `<button>` elements with `aria-pressed`; detail card uses
  `aria-live="polite"`. Selects are native form controls with visible `<label>`s.
- Mobile: journey rail becomes a vertical list with tap-to-expand cards; canvas
  selects stack; tri-column collapses to a single column; photo strip scrolls or stacks.
- Respect `prefers-reduced-motion`; no animated transitions required for function.
- All images keep meaningful `alt` text; captions are real text, not baked into images.

## Verification

Run before considering the work done:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/check_public_repo.py
bundle exec jekyll build
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
python3 scripts/check_page_quality.py --site-dir _site --fail-on-critical
```

Note: some tests may assert current homepage structure/content; fix or update them
where they legitimately encode the old homepage, and flag any that encode policy.
Then manual visual QA in the browser at `http://127.0.0.1:4000/` (desktop + mobile
widths), screenshots compared against the reference screenshot.

## Out of scope

- Localized homepages (de, ar, es, fr, it, nl, pl, pt-BR, zh-Hans) — later increment.
- Header/footer changes — the uncommitted header rewrite stays as-is.
- Changes to old section partials or old `home.yml` keys (still used by locales).
- SEO copy/positioning changes beyond condensing existing approved content.

---

## V2 Revision (2026-07-26, user-directed)

The user redirected the visual language after v1 implementation (Tasks 1–6):

- **Design language:** the homepage adopts the `/atlas/` page's layout and styles
  (Evidence Atlas layer: `atlas-hero`, `section-heading`, `eyebrow`, `lead`,
  `atlas-card-grid` with CSS-counter "ROUTE / 01" indices, `section-shell--flat`,
  `button` / `button--primary`).
- **Minimalistic landing fold:** identity line + eyebrow + headline + lead +
  actions. The journey-map rail and photo strip are removed.
- **No menu header on the homepage:** `hide_global_header: true` frontmatter,
  handled in `_layouts/default.html`; the hero carries a minimal identity line
  with locale links instead.
- **Better footer (global):** `_includes/footer.html` rewritten as a structured
  editorial footer (brand block + Explore/Legal link columns), styled by a new
  global stylesheet `assets/site-footer.css`.

### V2 section structure (EN homepage)

1. `hero-atlas` — identity line (name · descriptor · locale links) + `atlas-hero`
   (eyebrow kicker, headline, lead, primary + two secondary buttons).
2. `priorities-grid` — `section-heading` + `atlas-card-grid` with the 5 operating
   priorities (reuses `home_journey` data; cards get automatic "ROUTE / 0N" indices).
3. `constraint-canvas-home` — restyled into a `section-shell--flat`; keeps the
   interactive selects + recommendation (the only remaining widget).
4. `steps-ruled` — "Clarity in 4 steps" as a ruled mono-index list.
5. `ai-principles` — `section-shell--flat` with the 3 practical-AI principles.
6. `ideas-list` — ruled list of the 3 latest blog posts + "view all" button.
7. `cta-bar` — `section-shell--flat` CTA with primary/secondary buttons.

### V2 implementation notes

- Deleted partials: `hero-canvas.html`, `journey-map.html`, `photo-strip.html`,
  `tri-columns.html`. `constraint-canvas-home.html` and `cta-bar.html` are rewritten.
- `assets/home-canvas.js` trimmed to the constraint-canvas widget only.
- `assets/home-canvas.css` rewritten slim: identity line, canvas controls,
  ruled lists (steps/principles/ideas) — everything else comes from the
  Evidence Atlas layer.
- Data: `home_hero` gains `kicker` and `secondary_actions`; all other v1 keys
  are reused unchanged.
- Footer strings reuse `locale_data.ui.footer` with English defaults; one new
  "Atlas" link (default `'Atlas'`).
- Verification unchanged (v1 Task 7 commands + browser QA against `/atlas/`
  for visual consistency, no-header homepage, new footer on all pages).
