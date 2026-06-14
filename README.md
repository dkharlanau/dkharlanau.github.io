# SAP AMS Consultant, SAP Support Diagnostics, SD/MM, Master Data & AI Agents — Dzmitryi Kharlanau

## What this repository is

This repository powers the public professional website for **Dzmitryi Kharlanau**, a Senior SAP Consultant focused on SAP AMS diagnostics, SAP support improvement, SAP SD/MM process issues, master data, integration troubleshooting, and AI-ready support knowledge systems.

The site is a controlled public profile layer, a structured knowledge base, and a machine-readable discovery surface for search engines, retrieval systems, and AI agents.

- **Live site:** https://dkharlanau.github.io
- **About:** https://dkharlanau.github.io/about/
- **Services:** https://dkharlanau.github.io/services/
- **Sitemap:** https://dkharlanau.github.io/sitemap.xml
- **robots.txt:** https://dkharlanau.github.io/robots.txt
- **llms.txt:** https://dkharlanau.github.io/llms.txt

## Professional focus

- SAP AMS and production support improvement
- SAP SD/MM diagnostics across sales, procurement, logistics, inventory, billing, pricing, and delivery flows
- Business partner, customer, vendor, MDG, and master data issue analysis
- IDoc, API, middleware, and interface monitoring diagnostics
- Incident triage, root-cause analysis, support knowledge reuse, and handover quality
- Practical AI-assisted workflows for documentation, retrieval, diagnostics, and operational memory

## Why this site exists

LinkedIn is useful, but it is not enough as the only professional source.

This site gives the professional profile a canonical, citable, structured, and machine-readable home. It helps humans and AI systems understand the same context: what Dzmitryi works on, which knowledge areas are public, which materials are verified, and how the public content should be used.

The goal is professional transparency, safer discovery, and better routing for relevant SAP AMS, enterprise support, and AI-assisted operations conversations.

## Main site areas

- **Home** — positioning and trust signals
- **About** — professional profile and public identity anchor
- **Services** — consulting model for diagnose, stabilize, structure, and extend work
- **Atlas** — SAP diagnostics, concepts, maps, AI operations, data quality, and automation notes
- **Scenarios** — business-pain-to-diagnostic-workflow mappings
- **Skill Hub** — practical workflows for consultants, analysts, and AI agents
- **Research / Radar** — source-backed monitoring, comparisons, and watchlists
- **Datasets** — structured public data collections
- **AI endpoints** — `llms.txt`, `llms-full.txt`, resume exports, compact indexes, and agent-skill routing
- **Legal / Citation** — usage, attribution, disclosure, accessibility, and responsible AI boundaries

Useful entry points:

- https://dkharlanau.github.io/atlas/
- https://dkharlanau.github.io/skill-hub/
- https://dkharlanau.github.io/datasets/
- https://dkharlanau.github.io/ai/
- https://dkharlanau.github.io/legal/professional-disclosure/
- https://dkharlanau.github.io/CITATION/

## What is ready for AI agents

The repository is designed for controlled public retrieval, not unrestricted scraping or exposure of private material.

Available discovery surfaces include:

- `robots.txt` with crawler and AI-crawler policy
- `sitemap.xml` plus section sitemaps for pages, datasets, and verified Atlas content
- `llms.txt` as the AI-readable entry manifest
- `llms-full.txt` with reviewed Atlas content only
- `.well-known/agent-skills/` for topic routing and agent discovery
- `agent-skills/` source packages for portable agent workflows
- `datasets/manifest.json` and dataset schema files
- `atlas/manifest.json` and `ai/atlas-compact-index.json` for structured Atlas discovery
- validation scripts that check public hygiene, indexing policy, links, SEO metadata, and AI-readable endpoints

Only public, intentionally committed content belongs here. Private client information, ticket numbers, internal incident IDs, secrets, local exports, and raw private corpus material must not be committed.

## Knowledge areas covered

The public content is organized around practical enterprise support work:

- SAP AMS operations and support model improvement
- SAP SD/MM support, including order-to-cash and procure-to-pay issue patterns
- Procurement, inventory, billing, pricing, delivery, and account-determination diagnostics
- Business partner, customer, vendor, MDG, and master data governance issues
- IDoc, API, middleware, and interface monitoring ownership
- Clean-core and side-by-side automation boundaries
- AI-assisted documentation, retrieval, analysis, and support workflows
- Operational memory, reusable runbooks, and knowledge systems for enterprise teams

## Networking and collaboration

Dzmitryi is open to relevant professional conversations around:

- SAP AMS improvement
- support model modernization
- SAP consulting, delivery, and practical automation
- AI-assisted support operations
- knowledge systems for enterprise teams
- agentic workflows for diagnostics, documentation, and operational memory

LinkedIn: https://www.linkedin.com/in/dkharlanau/

## Trust, citation, and independence

This is a personal independent site. It is not an official employer, client, SAP, or vendor website.

The repository contains public materials only. Content uses controlled verification levels, and unverified pages are kept out of indexing surfaces until reviewed. Citation and license files are included for attribution and reuse boundaries:

- `CITATION.md`
- `CITATION.cff`
- `LICENSE`
- `LICENSE-DATA`
- `AGENTS.md`

Public SAP-related notes are practical diagnostic material, not official SAP documentation. Validate any SAP process, configuration, or automation decision in the relevant landscape before acting on it.

## Local validation

Use the smallest relevant checks while editing, then run the full sequence before publishing a public-ready change.

```sh
./bin/setup
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/check_public_repo.py
python3 scripts/generate_atlas_artifacts.py --check
bundle exec jekyll build
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
python3 scripts/check_indexing_policy.py --site-dir _site --fail-on-critical
python3 scripts/check_sitemap_policy.py --site-dir _site --repo-dir . --fail-on-critical
python3 scripts/check_date_consistency.py --site-dir _site --repo-dir . --fail-on-critical
python3 scripts/check_content_quality.py --fail-on-critical
python3 scripts/check_page_quality.py --site-dir _site --fail-on-critical
python3 scripts/audit_indexability.py --site-dir _site --fail-on-critical --output-dir /tmp/cv-ai-validation-reports
python3 scripts/audit_internal_links.py --site-dir _site --output-dir /tmp/cv-ai-validation-reports
python3 scripts/accessibility_audit.py --site-dir _site --fail-on-critical
python3 scripts/validate_ai_endpoints.py _site
git diff --check
```
