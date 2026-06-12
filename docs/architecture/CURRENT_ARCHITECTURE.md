---
published: false
robots: noindex,follow
sitemap: false
---

# Current Architecture — dkharlanau.github.io

Status: draft — internal documentation for maintainers and AI agents.  
Last updated: 2026-06-12

## Executive summary

`dkharlanau.github.io` is a public personal site and structured knowledge base built as a native GitHub Pages Jekyll site. The core is intentionally conservative (Ruby/Jekyll 3.10, GitHub Pages gem, Minima theme) so that `main` branch builds publish automatically with zero custom deployment. Modern tooling is layered around that core: Python validation scripts, pytest tests, generated Atlas discovery artifacts, dataset generators, and GitHub Actions CI.

This document describes how the repository works today. It is the source-of-truth reference for the workflow and agent guides that accompany it.

## Repository purpose

The site serves three purposes:

1. **Public entity signal** — who Dzmitryi Kharlanau is, what he works on, and where his expertise lies.
2. **Knowledge Atlas** — curated, conservative diagnostic and conceptual content for SAP support and operations.
3. **Scenarios / Research / Skill Hub** — business-pain-to-workflow mappings, source-backed research signals, and practical working skills.

Read `README.md` and `AGENTS.md` for the human and agent-facing summaries.

## Core publishing model

- **Platform:** GitHub Pages (native, not a custom Actions deployment).
- **Branch:** `main` is the production branch.
- **Build trigger:** GitHub Pages builds automatically on every push to `main`.
- **Local parity:** `bundle exec jekyll build` uses the same `github-pages` gem versions that GitHub Pages runs in production.
- **Output directory:** `_site/` — generated, never committed, never edited by hand.

## Technology stack

| Layer | Technology | Version / choice | File |
|---|---|---|---|
| Static site generator | Jekyll | 3.10.0 (pinned by `github-pages` gem) | `Gemfile.lock` |
| GitHub Pages integration | `github-pages` gem | 232 | `Gemfile` |
| Ruby runtime | Ruby | 3.3.4 | `.ruby-version` |
| Bundler | Bundler | 2.5.22 | `Gemfile.lock` |
| Theme | `minima` | 2.5.1 | `Gemfile.lock` |
| Plugins | `jekyll-seo-tag`, `jekyll-sitemap`, `jekyll-feed` | versions pinned by `github-pages` gem | `_config.yml` |
| Validation / generation | Python | 3.12 in CI; scripts are stdlib-first, only `pytest` + `PyYAML` required | `scripts/*.py`, `bin/*.py` |
| Test runner | pytest | latest stable | `.github/workflows/ci.yml` |
| Dataset page generation | Node.js | 22 LTS; one script using only `fs`/`path` | `scripts/generate_dama_pages.js` |
| Hosting | GitHub Pages | native | repository settings |

## GitHub Pages / Jekyll build model

- `Gemfile` declares `gem "github-pages"` and `webrick` (Ruby 3.x no longer bundles it). `faraday-retry` is present because newer `faraday` versions need it.
- `Gemfile.lock` is tracked so every environment resolves the same Jekyll/plugin versions.
- `.ruby-version` pins `3.3.4` to match the GitHub Pages production runtime.
- `_config.yml` configures the `minima` theme, site URL (`https://dkharlanau.github.io`), `permalink: pretty`, collections (`notes`, `blog`, `radar`, `news`), default layouts per collection, and plugin list.
- `_config.yml` also excludes a specific set of paths from the build: `_site`, `scripts`, `tests`, `docs/templates/`, `docs/routing-contract.md`, `docs/content-taxonomy.md`, `docs/classification-rules.md`, private/local folders (`TRIZ-bytes`, `DAMA`, `LLM-prompts`, `agentic-bytes`, LinkedIn exports, etc.).
- `bundle exec jekyll build` writes the rendered site to `_site/`. `bundle exec jekyll serve` runs a local preview server.

## Content architecture

| Public section | Source path | Output URL | Layout / notes |
|---|---|---|---|
| Home | `index.md` | `/` | `_layouts/default.html`, sections driven by `_data/home.yml` + `_includes/page-builder.html` |
| About / profile | `about.md` | `/about/` | `default`, `profile_page: true` |
| Services | `services/index.md`, `services/*.md` | `/services/`, `/services/<slug>/` | `default`, service detail pages reuse `note-detail` patterns |
| Knowledge Atlas | `atlas/index.md`, `atlas/*/*.md` | `/atlas/`, `/atlas/<section>/<slug>/` | `default` |
| Scenarios | `scenarios/index.md`, `scenarios/*.md` | `/scenarios/`, `/scenarios/<slug>/` | `default` |
| Research | `research/index.md`, `research/**/*.md` | `/research/`, `/research/<area>/<slug>/` | `default`, all draft/noindex |
| Skill Hub | `skill-hub/index.md`, `skill-hub/**/*.md` | `/skill-hub/`, `/skill-hub/<group>/<slug>/` | `default` |
| Blog | `blog/index.md`, `_blog/*.md` | `/blog/`, `/blog/<slug>/` | `blog` layout |
| Notes | `notes/index.md`, `_notes/*.md` | `/notes/`, `/notes/<slug>/` | `note` layout |
| Radar | `_radar/*.md` | `/radar/<slug>/` | `note` layout |
| News | `_news/*.md` | `/news/<slug>/` | `note` layout |
| Datasets | `datasets/index.md`, `datasets/<collection>/*.json`, generated pages | `/datasets/`, `/datasets/<collection>/`, `/datasets/view/...` | `default`, generated by `bin/generate_dataset_pages.py` |
| AI sources | `ai/index.md`, `ai/*.{json,yml}` | `/ai/`, `/ai/<file>` | `layout: null` for machine-readable files |
| Legal | `legal/*.md` | `/legal/<slug>/` | `default` |
| Changelog | `changelog.md` | `/changelog/` | driven by `_data/changelog.yml` |
| CV | `cv/index.html` | `/cv/` | static HTML |

## Atlas architecture

- Atlas lives in `atlas/<section>/<slug>.md`.
- Sections: `ai-operations`, `automation`, `concepts`, `data-quality`, `diagnostics`, `links`, `maps`, `research-notes`, `sap`.
- Each Atlas article has required frontmatter: `title`, `description`, `permalink` under `/atlas/`, `atlas_section`, `status`, `verified`, `tags`, `related`, `robots`, `sitemap`.
- Verification levels:
  - **Level 1** — `status: needs_verification`, `verified: false`, `robots: noindex,follow`, `sitemap: false`.
  - **Level 2** — `status: reviewed`, `verified: true`, `robots: index,follow`, `sitemap: true`.
  - **Level 3** — Level 2 plus source citations, strong internal links, recent `last_reviewed`.
- `scripts/generate_atlas_artifacts.py` reads Atlas pages and regenerates:
  - `atlas/manifest.json`
  - `llms-full.txt`
  - `ai/rag/related.json`
  - `ai/atlas-compact-index.json`
- Only Level 2+ pages are included in `llms-full.txt` and the Atlas sitemap.
- `atlas/research-notes/` is a noindex working area for useful but unpolished notes.

## Skill Hub architecture

- Skill Hub lives in `skill-hub/<group>/<slug>.md` plus foundation pages at `skill-hub/` root.
- Groups: `dama-dmbok`, `business-analysis`, `architecture`, `integration-architecture`, `sap-ams`.
- Skill pages are human-readable working-skill instructions.
- Agent-facing counterpart: `agent-skills/skills/<skill-name>/SKILL.md`.
- `agent-skills/skill-index.yml` is the source-of-truth index.
- `agent-skills/profiles/*.yml` define role-based skill collections.
- Exporter scripts copy selected skills to `.agents/skills/` (Codex) or `.claude/skills/` (Claude Code). Generated exports are **not** committed.
- Validate skills with `python3 agent-skills/exporters/validate_agent_skills.py`.

## Research / reports architecture

- `research/index.md` is the public research landing; it is draft/noindex.
- `research/briefs/`, `research/comparisons/`, `research/watchlists/` hold dated, cited signals.
- `research/skill-hub/` is the structured research base behind Skill Hub: `source-registry.yml`, `source-quality-rules.md`, domain notes, and synthesis files.
- Research material graduates to Atlas only after verification; it is never submitted to IndexNow and is excluded from sitemaps.
- Internal reports and contracts live under `docs/research/`, `docs/atlas/`, `docs/scenarios/`, `docs/maintenance/`.

## Layouts and includes

### Layouts (`_layouts/`)

- `default.html` — master layout. Includes `head.html`, conditionally includes `header.html`, renders `{{ content }}`, includes `cta-global.html`, includes `footer.html`, includes `seo/structured-data.html`.
- `note.html` — article layout for notes with backlink, eyebrow, title, metadata, body.
- `blog.html` — same as `note.html` but backlink goes to `/blog/`.
- `radar.html` — for radar entries.

### Key includes (`_includes/`)

- `head.html` — `<head>` content: title, meta description, robots, canonical, `og:*`, Twitter cards, JSON-LD WebSite, favicons, stylesheets, scripts, alternate links for AI endpoints.
- `page-builder.html` — routes a `sections` array to `_includes/sections/<key>.html` partials.
- `header.html`, `footer.html` — site chrome.
- `cta-global.html` — global CTA (currently blank).
- `seo/structured-data.html` — JSON-LD for Person, WebPage, Article, TechArticle, BreadcrumbList, DataCatalog, FAQPage.
- `atlas/author-block.html`, `atlas/disclaimer.html`, `atlas/status-badge.html` — Atlas components.
- `llms-manifest.txt` — source for `/llms.txt`.

## CSS / JavaScript architecture

- Three CSS files loaded in this order in `head.html`:
  1. `assets/material3.css` — Material 3 token layer.
  2. `assets/main.css` — base/component styles.
  3. `assets/site.css` — final overrides (source of truth for the live homepage look).
- No CSS build step; plain static CSS.
- `assets/dataset-render.js` — client-side dataset rendering, loaded with `defer`.
- `scripts/generate_dama_pages.js` emits standalone `docs/dama/assets/dama.css` for the DAMA decision-block pages.

## Generated artifacts

| Artifact | Generator | Source | Notes |
|---|---|---|---|
| `_site/` | `bundle exec jekyll build` | All source files | Build output — never edit or commit. |
| `llms-full.txt` | `scripts/generate_atlas_artifacts.py` | Verified Atlas pages | Excludes unverified pages and source paths. |
| `atlas/manifest.json` | `scripts/generate_atlas_artifacts.py` | Atlas frontmatter | Includes verified/unverified counts and section list. |
| `ai/rag/related.json` | `scripts/generate_atlas_artifacts.py` | Atlas `related` frontmatter | Edges + broken-link warnings. |
| `ai/atlas-compact-index.json` | `scripts/generate_atlas_artifacts.py` | Atlas frontmatter + headings | Signal-matching index. |
| `datasets/manifest.json` | `bin/enrich_datasets.py` | `datasets/**/*.json` | Machine-readable dataset index. |
| `datasets/README.md` | `bin/enrich_datasets.py` | `datasets/**/*.json` | Human-readable dataset landing readme. |
| `datasets/index.md`, `datasets/search.md`, `datasets/types/**`, `datasets/view/**` | `bin/generate_dataset_pages.py` | `datasets/manifest.json` | GitHub Pages-friendly dataset pages. |
| `docs/dama/*.html`, `docs/dama/tags/*.html`, `docs/dama/assets/dama.css` | `scripts/generate_dama_pages.js` | `datasets/DAMA/*.json` | Standalone decision-block pages. |
| `sitemap.xml`, `sitemap-pages.xml`, `sitemap-atlas.xml`, `sitemap-data.xml` | Jekyll (Liquid pages) | Site structure + frontmatter | Filter by `robots`, `sitemap`, Atlas verification status. |
| `feed.xml` | `jekyll-feed` plugin | `site.posts`, collections | RSS/Atom feed. |

## SEO / discovery architecture

- `robots.txt` allows generic crawlers, explicitly allows OAI-SearchBot / ChatGPT-User / Claude-SearchBot / Claude-User / PerplexityBot / CCBot / FacebookBot, and disallows GPTBot / ClaudeBot / Google-Extended for training. It also signals `ai-train=no, search=yes, ai-input=yes`.
- Sitemaps are split into an index plus section sitemaps to keep Atlas filtering explicit:
  - `sitemap.xml` — index referencing `sitemap-pages.xml`, `sitemap-data.xml`, `sitemap-atlas.xml`.
  - `sitemap-pages.xml` — non-Atlas, non-research pages with `sitemap != false` and no `noindex`.
  - `sitemap-atlas.xml` — only Atlas pages with `status: reviewed` and `verified: true`.
  - `sitemap-data.xml` — AI/data endpoints (`ai/resume.yml`, `ai/resume.json`, etc.) and `datasets/manifest.json`.
- `head.html` emits canonical, `og:url`, alternate links for AI endpoints (`ai:catalog`, `llms.txt`, `LLM.txt`, datasets manifest, agent skills index).
- `_includes/seo/structured-data.html` emits schema.org JSON-LD: Person (via `_data/resume.yml`), WebSite, WebPage/ProfilePage/CollectionPage/TechArticle/Article, BreadcrumbList, DataCatalog, FAQPage.
- `llms.txt` is generated from `_includes/llms-manifest.txt` and points crawlers to machine endpoints.
- `scripts/audit_discovery_outputs.py` audits the built `_site/` for sitemap/robots/llms/JSON-LD correctness and private-path leaks. CI runs it in `--warn-only` mode with a baseline.
- `scripts/indexnow_submit.py` submits canonical URLs to IndexNow; default is dry-run. Real submission is gated behind a manual `workflow_dispatch` with `INDEXNOW_KEY`.

## Safety rules

- Every committed file is public.
- Do not commit LinkedIn exports, raw dumps, local configs, secrets, private notes, bytecode, caches, `_site/`, or temporary transfer folders.
- Never expose client names, ticket numbers, internal incident IDs, or proprietary system details.
- Draft notes and unverified material stay local or in noindex areas (`atlas/research-notes/`, `research/`).
- Agents may not change `verified: false` to `verified: true`.
- Do not edit generated files by hand; regenerate them with the documented scripts.
- Do not add unverified pages to sitemaps or `llms-full.txt`.

## Known risks and limitations

- **Ruby drift:** Local Ruby must match `.ruby-version` (3.3.4). Environments with older Ruby cannot run Jekyll or post-build checks.
- **Jekyll 3.x:** GitHub Pages pins Jekyll 3.10. Some modern Jekyll 4 features are unavailable without a custom deployment pipeline.
- **Generated artifact staleness:** `atlas/manifest.json`, `llms-full.txt`, and related JSON files can become stale if content changes without running `scripts/generate_atlas_artifacts.py`. CI checks this with `--check`.
- **Sitemap leakage risk:** Custom sitemap templates rely on frontmatter `robots`/`sitemap`/`verified` fields. Missing or inconsistent frontmatter can leak noindex pages into sitemaps; `audit_discovery_outputs.py` catches this.
- **IndexNow bulk submission:** Real IndexNow submission is manual, but `--all` could still submit many URLs. The script caps batches (`--max-urls`) and skips research/unverified/private paths.
- **Skill Hub / Agent Skills drift:** Generated exports (`.agents/`, `.claude/`) must be regenerated after source changes; they are gitignored and easy to forget.

## What should stay stable

- GitHub Pages native publishing model.
- `github-pages` gem and pinned Jekyll/plugin versions.
- Ruby 3.3.4 / Bundler 2.5.22 pins.
- `_config.yml` core settings (URL, baseurl, collections, defaults, plugins, excludes).
- The three-level Atlas verification model and the generated-artifact pipeline.
- `robots.txt` crawler policy.
- Custom sitemap structure and filtering rules.
- Public-safety rules in `scripts/check_public_repo.py`.

## What can be modernized safely

- **Tooling around the core:** additional Python validators, new pytest tests, improved dataset generators, richer JSON-LD, and enhanced agent-skill exporters.
- **CI workflows:** adding caching, matrix jobs, or new read-only checks, as long as the GitHub Pages build remains native.
- **Content:** new Atlas, Scenario, Skill Hub, and Research pages following the existing frontmatter and verification rules.
- **Datasets:** new JSON entries and collection pages, provided attribution metadata is maintained.
- **AI endpoints:** new JSON/YAML exports in `ai/` and `.well-known/` for agent discovery.

Defer unless a concrete limitation forces it: Jekyll 4 migration, Astro/Vite/React rebuild, custom GitHub Pages deployment pipeline, major Ruby upgrade beyond GitHub Pages runtime. See `docs/technology/technology-policy.md` for the full rationale.
