# PROJECT_MAP.md

Compact map of the `dkharlanau.github.io` repository.
Last updated: 2026-06-09

## Important Directories

| Directory | Purpose |
|-----------|---------|
| `atlas/` | Knowledge Atlas — curated diagnostic, conceptual, and SAP-specific content |
| `scenarios/` | Business-pain-to-diagnostic-workflow scenarios |
| `services/` | Consulting service descriptions |
| `research/` | Research briefs, comparisons, watchlists |
| `datasets/` | Canonical machine-readable dataset collections |
| `ai/` | Machine-readable exports (JSON/YAML) for AI agents and search systems |
| `_data/` | Jekyll data files (resume, home, certifications, changelog, etc.) |
| `_includes/` | Jekyll partials (sections, components, SEO, Atlas blocks) |
| `_layouts/` | Jekyll layouts (default, blog, note, radar) |
| `_blog/` | Blog post collection |
| `_notes/` | Notes collection |
| `_radar/` | Radar signal collection |
| `_news/` | News signal collection |
| `legal/` | Policies (privacy, terms, disclosure, responsible AI, accessibility, datasets) |
| `docs/` | Internal documentation (Atlas backlog, SEO, content contracts, AI readiness) |
| `docs/ai/` | AI-agent-readiness documentation |
| `scripts/` | Python generators, validators, and maintenance scripts |
| `bin/` | Setup and dataset generation scripts |
| `tests/` | pytest test suite |
| `.github/` | GitHub Actions workflows and PR templates |
| `.well-known/` | Agent skills and machine-readable discovery files |
| `_site/` | **Generated Jekyll build output — never edit directly** |

## Public Content Sections

| Section | Path | Type |
|---------|------|------|
| Home | `index.md` | Landing |
| About | `about.md` | Profile |
| Services | `services/index.md`, `services/*.md` | Commercial signal |
| Atlas | `atlas/index.md`, `atlas/*/*.md` | Knowledge base |
| Scenarios | `scenarios/index.md`, `scenarios/*.md` | Business pain workflows |
| Research | `research/index.md`, `research/**/*.md` | Research briefs |
| Blog | `blog/index.md`, `_blog/*.md` | Long-form essays |
| Notes | `notes/index.md`, `_notes/*.md` | Short-form notes |
| Datasets | `datasets/index.md`, `datasets/*/` | Data collections |
| AI Sources | `ai/index.md`, `ai/*.{json,yml}` | Machine-readable exports |
| Legal | `legal/*.md` | Policies |
| Changelog | `changelog.md` | Release history |

## Generated Artifacts

| Artifact | Source | Generator |
|----------|--------|-----------|
| `_site/` | All source files | `bundle exec jekyll build` |
| `llms-full.txt` | Verified Atlas pages | `scripts/generate_atlas_artifacts.py` |
| `sitemap.xml` | Site structure | Jekyll + `jekyll-sitemap` plugin |
| `sitemap-pages.xml` | Page sitemap | Jekyll |
| `sitemap-atlas.xml` | Atlas sitemap | Jekyll |
| `sitemap-data.xml` | Dataset sitemap | Jekyll |
| `atlas/manifest.json` | Atlas page registry | `scripts/generate_atlas_artifacts.py` |
| `ai/catalog.json` | Dataset catalog | `bin/enrich_datasets.py` |
| `docs/dama/*.html` | DAMA dataset pages | `scripts/generate_dama_pages.js` |

## Scripts

| Script | Purpose |
|--------|---------|
| `bin/setup` | Environment setup |
| `bin/enrich_datasets.py` | Dataset metadata enrichment |
| `bin/generate_dataset_pages.py` | Dataset page generation |
| `scripts/check_public_repo.py` | Public-safety check |
| `scripts/check_links.py` | Link validation |
| `scripts/check_seo.py` | SEO validation |
| `scripts/generate_atlas_artifacts.py` | Atlas manifest and llms-full generation |
| `scripts/generate_dama_pages.js` | DAMA HTML page generation |
| `scripts/validate_site_content.py` | Content validation |
| `scripts/content_maintenance_scan.py` | Content maintenance scan |
| `scripts/propose_atlas_update.py` | Atlas update proposal |
| `scripts/match_atlas_signal.py` | Signal-to-Atlas matching |
| `scripts/build_site_index.py` | Site index generation |
| `scripts/indexnow_submit.py` | IndexNow submission |

## Tests

| Test File | Coverage |
|-----------|----------|
| `tests/test_atlas_artifacts.py` | Atlas artifact generation |
| `tests/test_atlas_backlog_pipeline.py` | Atlas backlog pipeline |
| `tests/test_atlas_pr_workflow.py` | Atlas PR workflow |
| `tests/test_atlas_proposal_quality.py` | Atlas proposal quality |
| `tests/test_atlas_rag_evaluation.py` | Atlas RAG evaluation |
| `tests/test_atlas_signal_matcher.py` | Signal matching |
| `tests/test_atlas_update_proposals.py` | Update proposals |
| `tests/test_content_maintenance.py` | Content maintenance |
| `tests/test_discovery_outputs.py` | Discovery outputs |
| `tests/test_indexnow_hardening.py` | IndexNow hardening |
| `tests/test_li2resume.py` | Resume generation |
| `tests/test_research_atlas_proposals.py` | Research proposals |
| `tests/test_seo_discovery.py` | SEO discovery |
| `tests/test_signal_to_atlas_schema.py` | Signal-to-Atlas schema |

## SEO / Sitemap / LLMs Files

| File | Purpose |
|------|---------|
| `robots.txt` | Crawler policy with AI-specific rules |
| `sitemap.xml` | Sitemap index |
| `sitemap-pages.xml` | Page-level sitemap |
| `sitemap-atlas.xml` | Atlas page sitemap |
| `sitemap-data.xml` | Dataset sitemap |
| `llms.txt` | LLM access manifest (Jekyll-generated from `_includes/llms-manifest.txt`) |
| `llms-full.txt` | Full-text verified Atlas content |
| `_includes/llms-manifest.txt` | Source manifest for `llms.txt` |
| `_includes/seo/structured-data.html` | JSON-LD structured data |

## Where to Add Atlas Pages

- **Concepts**: `atlas/concepts/<slug>.md` — durable explanations
- **Diagnostics**: `atlas/diagnostics/<slug>.md` — diagnostic patterns
- **SAP notes**: `atlas/sap/<slug>.md` — SAP-specific configuration/support
- **Maps**: `atlas/maps/<slug>.md` — process and dependency maps
- **AI operations**: `atlas/ai-operations/<slug>.md` — AI-assisted support patterns
- **Data quality**: `atlas/data-quality/<slug>.md` — master data and governance
- **Automation**: `atlas/automation/<slug>.md` — support automation patterns

All new Atlas pages must start at **Level 1** (`status: needs_verification`, `verified: false`, `robots: noindex,follow`, `sitemap: false`).

## Where to Add Scenario Pages

- `scenarios/<slug>.md` — business pain scenarios

All new Scenario pages must start at **Level 1** (`status: needs_verification`, `verified: false`, `robots: noindex,follow`, `sitemap: false`).

## Where to Add Docs

- `docs/ai/*.md` — AI-agent-readiness documentation
- `docs/atlas/*.md` — Atlas backlog, pipeline, and editorial docs
- `docs/seo/*.md` — SEO and discovery docs
- `docs/templates/*.md` — Content templates
- `docs/research/*.md` — Research contracts
- `docs/scenarios/*.md` — Scenarios backlog

## Where Not to Add Content

- `_site/` — generated build output
- `llms-full.txt` — generated artifact
- `sitemap-*.xml` — generated artifacts
- Root-level duplicate folders (`TRIZ-bytes/`, `DAMA/`, `LLM-prompts/`, `agentic-bytes/`) — keep under `datasets/`
- Any path containing private corpus, client data, or internal incident details
- Any path that would expose unverified draft material as indexable
