# CV AI site

Personal brand site for Dzmitryi Kharlanau, built on Jekyll with a light Neubrutalist design system.

## Datasets: license & citation

- Dataset bytes live under `/datasets/` and are licensed **CC BY-NC 4.0** (non-commercial, attribution required).
- Citation + license details: `/legal/datasets/` (site) and `LICENSE-DATA` (repo).
- GitHub “Cite this repository” support: `CITATION.cff`.

## Logos, brands, and trademarks

- Third-party company logos, product marks, and brand assets are **not** covered by the dataset or repository content license unless a file explicitly says otherwise.
- Before adding or reusing any third-party logo or icon, verify the applicable license, public brand-guidelines, or obtain written permission from the rights holder.
- If permission is unclear, do not commit the asset. Link to the company website or use plain text instead.
- Keep any approved third-party logo use narrow and referential only. Do not imply endorsement, partnership, certification, or affiliation unless that relationship is real and can be stated publicly.
- When a third-party asset is added, record its source and usage basis in the relevant data file or commit context so provenance is clear.
- Repository maintainers and contributors are responsible for securing any required permissions before publishing branded assets.
- Nothing in this repository should be treated as legal advice or as a substitute for brand approval from the rights holder.

## Quick start

This repo targets Ruby `>= 3.2.3` (see `.ruby-version`).

1. Ensure Ruby is installed and active (`ruby -v` should be `>=` the version in `.ruby-version`).
2. Install gems with `./bin/setup` (or `bundle install`).
3. Serve locally with `bundle exec jekyll serve`.
4. Deploy via GitHub Pages (repository already follows the expected structure).

## Content model

- Homepage copy lives in `_data/home.yml` and renders through `_includes/sections/*` via `index.md`.
- Resume data is centralised in `_data/resume.yml` and powers both `cv/index.html` and `ai/resume.json`.
- Notes sit inside `_notes/` and use the `_layouts/note.html` template; the listing is published at `/notes/`.
- AI-friendly mirrors exist in `/ai`, currently `resume.json`, `resume.yml`, and `home.json`.
- Changelog page (`/changelog/`) pulls from `_data/changelog.yml` via the `changelog` section partial.
- Legal policies live under `/legal/` as standalone Markdown pages (code of conduct, terms, privacy, professional disclosure, responsible AI, accessibility).
- The homepage `llm-profiles` section surfaces quick links to `/ai/resume.json`, `/ai/resume.yml`, and `/LLM.txt` for copilot handoff.
- Social channels are defined in `_data/social.yml` and rendered through the reusable `_includes/components/social-line.html` component used across sections and the footer.
- Structured data scripts live in `_includes/seo/structured-data.html`, wiring Person, WebSite, Breadcrumb, and Article metadata automatically.
- Sitemaps: `sitemap.xml` indexes `sitemap-pages.xml` (pages, notes, blog) and `sitemap-data.xml` (JSON/YAML assets); `ai/sitemap.xml` exposes the `ai/home.json` snapshot.

See `ARCHITECTURE.md` for deeper guidance on extending the system.
