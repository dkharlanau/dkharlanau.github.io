# Prompt for Kimi Code — apply Martenweave design language to cv-ai site

## Role and context

You are working in the Jekyll repository at `/Users/dzmitryikharlanau/Developments/cv-ai` — the public personal site of an SAP consultant (GitHub Pages). A second local repository, `/Users/dzmitryikharlanau/Developments/martenweave.github.io`, contains a mature, distinctive design that the site owner wants to adapt for cv-ai.

A design brief already exists in this repo at `docs/design/martenweave-style-adoption-brief.md` — read it first. Also read `AGENTS.md` and `DESIGN-SYSTEM.md` in the repo root and follow them strictly.

## Goal

Restyle the cv-ai site by adopting Martenweave's **structural design grammar** — hairline ruled grids, monospace metadata layer, oversized tight-tracked headlines, hard offset "paper" shadows, process rails — while **keeping the cv-ai cool neutral palette** (navy-charcoal ink, light grey-blue surfaces). The result must read as the same restrained editorial B2B publication described in `DESIGN-SYSTEM.md`, not as a copy of the Martenweave product site.

## Source material to study before editing

- `/Users/dzmitryikharlanau/Developments/martenweave.github.io/styles.css` — tokens, ruled-grid sections, docs/blog shells, responsive rules, reduced-motion handling.
- `/Users/dzmitryikharlanau/Developments/martenweave.github.io/home.css` — hero, proof-strip, workflow-rail, use-case-list, faq-list, conversion sections, offset shadows.
- `/Users/dzmitryikharlanau/Developments/martenweave.github.io/index.html` — how sections are composed in markup.
- In this repo: `assets/site.css` (loaded last — your main working layer), `assets/main.css`, `_layouts/default.html`, `_includes/page-builder.html`, `_includes/sections/*.html`.

## Design decisions (already made — do not reopen)

1. **Palette**: keep cv-ai's `--color-page: #f6f7f9`, `--color-ink: #111827`, `--color-accent: #152033` and border greys. Introduce exactly one warm accent: `--color-signal: #d98d12` (amber), used ONLY for kickers/eyebrows, numeric indices, focus outlines, and small status markers. No aubergine/purple anywhere.
2. **Shape**: replace all border radii (currently 10–18px) with 2–4px. Remove all drop shadows; the only allowed shadow is the offset paper shadow `box-shadow: 14px 14px 0 <soft-tint>` on dark terminal/code blocks and screenshots.
3. **Surfaces**: replace rounded shadow cards with hairline grids — cells share 1px borders (`--color-border`), no gaps, no elevation. Hover = background tint (`--color-accent-soft`) or accent fill inversion, never scale/shadow lifts.
4. **Typography**: keep Inter + Source Serif 4. Headlines get Martenweave treatment: `clamp()` sizes, `letter-spacing: -0.04…-0.055em`, `max-width` in `ch`, `text-wrap: balance`. Add a monospace metadata layer: kickers (`text-transform: uppercase`, letter-spacing ~0.1em, amber), trust lines, indices `01 / 02 / 03`, footer line.
5. **Accessibility**: keep/improve skip-link, `:focus-visible` 3px amber outline, `prefers-reduced-motion: reduce` disabling all animation, AA contrast for amber on light backgrounds (use it on ink or large text only).

## Component work (homepage first, then shared templates)

Implement as reusable CSS classes in `assets/site.css` (or a new `assets/design-tokens.css` loaded after `site.css` — update `_layouts/default.html` accordingly) plus minimal markup changes in `_includes/sections/`:

1. **Hero** (`hero.html`) → Martenweave `atlas-hero` structure: amber mono eyebrow, h1 max ~14ch, subhead, two buttons (primary = accent fill, secondary = 1px outline, radius 2px, no shadow), monospace trust line with amber separators.
2. **Credibility** (`credibility.html`) → `proof-strip`: 3–4 columns divided by hairlines, bold claim + small muted explanation, no cards.
3. **Analysis problem** (`analysis-problem.html`) → `pillars`/`distinction` pattern: shared-border grid, generous whitespace, mono indices.
4. **Engagement framework** (`engagement-framework.html`) → `workflow-rail`: numbered horizontal steps with a connecting hairline, mono step numbers, amber active marker; collapses to vertical hairline list on mobile.
5. **Explore site** (`explore-site.html`) → `docs-grid`/`use-case-list`: bordered cell grid, mono kicker per cell, hover tint.
6. **FAQ** (`faq.html`) → `faq-list`: hairline top/bottom rows, no card chrome.
7. **Contact / CTA** (`contact.html`) → `conversion-section`: single-row grid (headline + text + button), hairline separation.
8. **Header/footer**: nav links get the `scaleX` underline hover animation; footer gets a monospace tagline line.
9. **Atlas/doc pages**: apply the shared classes so `atlas/` and `datasets/` pages get the same hairline treatment (sticky sidebar shell, h2 with hairline top border, amber-labeled note blocks) — reuse, don't fork.

## Hard constraints

- Do NOT change any content, copy, claims, frontmatter, `verified:` flags, robots/sitemap fields, JSON-LD/Schema, or files listed under "What Agents Must Not Edit" in `AGENTS.md` (`index.md` frontmatter stays as is — only section includes may change).
- Do NOT touch `assets/main.css` or `assets/material3.css`; work in the layer loaded last.
- Do NOT copy Martenweave's hero image drift animation, product screenshots, or purple palette.
- Keep all changes in one feature branch; one logical change per commit group.

## Validation (must pass before you report done)

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/check_public_repo.py
bundle exec jekyll build
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
python3 scripts/check_page_quality.py --site-dir _site --fail-on-critical
```

## Acceptance criteria

- No element with border-radius > 4px; no drop shadows except the offset paper shadow.
- Every former card grid renders as a hairline shared-border grid.
- Kickers, indices, trust lines, footer tagline render in the monospace amber metadata style.
- Mobile breakpoints collapse grids into single-column hairline lists (mirror Martenweave's `@media` behavior).
- All validation commands above pass; accessibility (focus-visible, reduced motion, contrast) is preserved or improved.
- Report: files changed, before/after summary per component, validation output summary.
