# Dzmitryi Kharlanau — Professional Website

This is my public professional website and profile repository.

I use it as a controlled, transparent, and AI-readable layer around my professional background, public references, certificates, publications, and selected structured profile data.

## About me

I am **Dzmitryi Kharlanau**, a Senior SAP Consultant working across SAP AMS support, logistics, migration, master data, operational analysis, and process optimization.

My SAP path started in 2014 through SAP University Alliances, TERP10, and SAP SD certification.

Over the years, I have worked on multiple SAP projects in different roles: consultant, team lead / coordinator, developer, and operational analyst. This gave me a practical view of how SAP work really happens — across business processes, support pressure, migration activities, master data, integrations, custom logic, and delivery constraints.

Today, my focus is SAP AMS, support knowledge, incident analysis, SD/MM issues, master data problems, process optimization, and practical AI-assisted support workflows.

I actively work with modern AI tools and AI-assisted development workflows. I use them to explore how support knowledge, diagnostics, retrieval, automation, documentation, and side-by-side tools can improve enterprise operations.

I try to keep developing across SAP, architecture, practical AI, and product thinking.

## Why this site exists

LinkedIn is useful, but it is not enough as the only professional source.

This site gives me one canonical public profile that I can control, structure, reference, and keep machine-readable for search engines and AI systems.

It exists to make my background easier to understand and verify.

- **Live URL:** https://dkharlanau.github.io
- **Generated with:** Jekyll + GitHub Pages
- **Sitemap:** https://dkharlanau.github.io/sitemap.xml
- **robots.txt:** https://dkharlanau.github.io/robots.txt

## What this site is about

The site focuses on practical SAP AMS, support, and process optimization topics:

- SAP AMS improvement
- SAP support and process optimization
- change-to-run handover
- support knowledge reuse
- master data and process reliability
- integration and operational complexity
- clean-core boundaries
- practical AI-assisted SAP support
- side-by-side automation and support workflows

The main idea is that SAP support quality depends on practical handover, clean data, reliable integrations, clear ownership, support readiness, and daily operating discipline.

## Site structure

- **Home** — Positioning and trust signals
- **About / Profile** — Canonical human-readable and machine-readable profile
- **Services** — Consulting engagement model (diagnose, stabilize, structure, extend)
- **Knowledge Atlas** — Curated SAP diagnostics, concepts, and process maps
- **Scenarios** — Business-pain-to-diagnostic-workflow mappings
- **Skill Hub** — Practical working skills for enterprise consultants and AI agents
- **Research / Radar** — Signal tracking and source-backed briefs
- **Datasets** — Canonical machine-readable dataset collections
- **AI endpoints** — `llms.txt`, `resume.json`, `resume.yml`, and agent-skill discovery via `.well-known/`

## What this repository contains

This repository may include:

- website source files
- structured résumé / profile data
- public certificate and badge references
- publication and note references
- AI-readable files such as `llms.txt`, `resume.json`, or `resume.yml`

## Build and validation

```sh
# Local preview
bundle exec jekyll serve

# Full validation sequence (run before publishing)
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/check_public_repo.py
bundle exec jekyll build
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
python3 scripts/check_indexing_policy.py --site-dir _site
python3 scripts/check_content_quality.py
python3 scripts/audit_indexability.py --site-dir _site
python3 scripts/audit_internal_links.py --site-dir _site
```

All committed content is public. The repository uses a three-level verification system for content quality and indexing control.

## Networking

I am open to relevant professional networking, SAP AMS improvement topics, SAP support discussions, and practical AI / automation topics around support operations.

You can reach me on LinkedIn:

[Dzmitryi Kharlanau](https://uk.linkedin.com/in/dkharlanau)

## Independence

The views and materials on this site are personal and independent.

This is not an official employer, vendor, or client website.

## AI and search transparency

This site is designed to be machine-readable for search engines and AI retrieval systems. It includes:

- A detailed `robots.txt` with per-crawler policies and sitemap references
- Section-level sitemaps (`sitemap-atlas.xml`, `sitemap-data.xml`, `sitemap-pages.xml`)
- AI-readable files (`llms.txt`, `resume.json`, `resume.yml`)
- `.well-known/agent-skills/` for AI agent discovery and topic routing
- A three-level content verification system that controls which pages are indexed
