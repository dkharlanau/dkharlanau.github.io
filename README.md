# CV AI site

Personal brand site for Dzmitryi Kharlanau, built on Jekyll with a light Neubrutalist design system.

## Quick start

1. Ensure Ruby/Bundler are installed, then add a Gemfile (see GitHub Pages defaults) and run `bundle install`.
2. Serve locally with `bundle exec jekyll serve`.
3. Deploy via GitHub Pages (repository already follows the expected structure).

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
- Static sitemap: run `python bin/build_static_sitemap.py` to regenerate `sitemap-static.xml` for search-console submissions.

See `ARCHITECTURE.md` for deeper guidance on extending the system.
