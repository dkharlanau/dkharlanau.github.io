# AGENTS.md

Project-specific guidance for AI coding and research agents working in this public GitHub Pages repository.
Use this file as the main entry point. Open deeper docs only when the task needs them.

**Last updated:** 2026-08-17. The repository uses product-level navigation, stable deep URLs, and a deterministic sitewide content-quality and AI-search-readiness pipeline.

## Repository Purpose

This is the public personal site and structured knowledge system of **Dzmitryi Kharlanau**, an SAP consultant focused on SAP operations, logistics, integration, data, diagnostics, and practical AI.

The site has six product areas:
1. **Profile** — public identity, experience, certifications, and professional evidence.
2. **Knowledge** — reviewed and working human-readable knowledge: Atlas, Scenarios, Research, Journal, and Notes.
3. **Labs** — active SAP, AI, operational, and assessment workspaces.
4. **Frameworks** — reusable reasoning and execution methods that can be applied across domains.
5. **Machine layer** — datasets, AI-readable exports, skills, tools, discovery files, and MCP source packages.
6. **Services** — consulting services and engagement context.

Everything committed to this repository is public. Treat every file accordingly.

## High-Level Site Structure

| Area | Primary path | Purpose |
|------|------|---------|
| Profile | `/`, `about.md`, `cv/` | Positioning, identity, experience, trust signals |
| Knowledge | `knowledge/` | Product hub for Atlas, Scenarios, Research, Journal, and Notes |
| Knowledge Atlas | `atlas/` | Curated diagnostic, conceptual, and SAP-specific content |
| Scenarios | `scenarios/` | Business pain mapped to SAP process context and diagnostic workflows |
| Research / Radar | `research/`, `_radar/`, `_news/` | Briefs, comparisons, watchlists, signal tracking |
| Labs | `labs/` | SAP Enterprise, AI Ready, Business AI, operational protocols, assessment practice |
| Frameworks | `frameworks/` | Product hub for TRIZ, Decision Design, Reusable Data Procedures, operational protocols |
| Machine layer | `machine/` | Product hub for datasets, AI exports, skills, tools, and MCP |
| Datasets | `datasets/` | Canonical machine-readable dataset collections |
| AI-readable exports | `ai/` | JSON/YAML machine endpoints and generated indexes |
| Agent Skills | `agent-skills/` | Portable agent skill packages for Codex, Claude Code, and similar tools |
| Agent Tools | `agent-tools/` | Static public tool descriptions |
| Services | `services/` | Consulting service descriptions and engagement model |
| Quality pipeline | `scripts/content_quality.py`, `config/content-quality.yml` | Publication safety, link graph, search, quality, and AI-retrieval checks |
| Quality reports | `reports/` | Locally generated audit and review outputs; normally ignored/generated |
| Legal | `legal/` | Privacy, terms, disclosure, responsible AI, accessibility |

## Structural Routing Rules

- Global navigation is product-level. Do not add every new domain or collection to the header.
- Keep established deep URLs stable. Prefer hubs, aliases, redirects, metadata, and graph links over mass directory moves.
- `/labs/enterprise-context/` remains the stable physical route for the **SAP Enterprise** workspace. The UI may use the broader SAP Enterprise name.
- `/lab/` is a compatibility alias for `/labs/`.
- `/labs/reusable-data-procedures/` is a compatibility route; canonical content lives at `/reusable-data-procedures/`.
- `/triz/`, `/ddd/`, and `/reusable-data-procedures/` are canonical framework routes and are grouped by `/frameworks/` without being physically moved.
- A topic can belong to several domains. Do not duplicate source content to make the directory tree look like a graph.
- Before creating a new root directory, decide whether the work belongs to Profile, Knowledge, Labs, Frameworks, Machine layer, or Services.
- Read `PROJECT_MAP.md` and `ARCHITECTURE.md` before sitewide structure changes.
- Structural work is not complete until the Jekyll build and local-link checks pass in CI.

## Agent Skills Purpose

`agent-skills/` contains portable, installable agent skill packages that complement the human-readable [Skill Hub](../skill-hub/) pages. Each skill is a compact operational instruction set for AI agents (Claude Code, Codex, and similar tools).

Key principles:
- **Source of truth:** `agent-skills/skills/<skill-name>/` is the source of truth. `.agents/skills/` and `.claude/skills/` are generated exports.
- **Do not edit generated exports by hand.** Edit the source and re-run the exporter.
- **Use profiles:** Install only the skills relevant to your current role or project.
- **Validate before commit:** Run `python3 agent-skills/exporters/validate_agent_skills.py` before committing changes.

Export commands:
```bash
# For Codex
python3 agent-skills/exporters/export_codex_skills.py --profile sap-ams

# For Claude Code
python3 agent-skills/exporters/export_claude_skills.py --profile sap-ams
```

Read `agent-skills/README.md` for full documentation.

## Atlas Purpose

The Atlas is a curated working knowledge base for concepts that matter during SAP support, process analysis, operational memory work, and side-by-side AI design. It is intentionally conservative: reviewed pages first, raw research notes kept private or noindex.

Atlas sections:
- `atlas/concepts/` — Durable concept explanations (order-to-cash, ATP vs inventory, etc.)
- `atlas/diagnostics/` — Support-oriented diagnostic patterns for repeat incidents
- `atlas/sap/` — SAP configuration and support explanations with conservative boundaries
- `atlas/maps/` — Process, document-flow, data dependency, and cross-domain navigation maps
- `atlas/ai-operations/` — AI-assisted support, operational memory, governance, human review
- `atlas/data-quality/` — Master data, quality signals, governance failure modes
- `atlas/automation/` — Support automation, agentic workflows, developer automation
- `atlas/research-notes/` — **Noindex working area** — useful but not polished expert content
- `atlas/links/` — Reference routes to profile, services, datasets

## Scenarios Purpose

Scenarios connect business pain to SAP diagnostic workflows. Each scenario follows a consistent pattern:
1. Business pain
2. Process context
3. SAP touchpoints
4. Root causes (master data / configuration / integration)
5. Cost drivers
6. Diagnostic workflow
7. Solution patterns
8. AI / automation opportunity (with conservative boundaries)
9. Related Atlas links

Scenarios are complementary to Atlas: Atlas pages are diagnostic deep-dives; Scenarios are workflow lenses showing why those diagnostics matter to business outcomes.

## Research / Radar Purpose

- `research/briefs/` — Short research briefs on emerging topics
- `research/comparisons/` — Side-by-side technology comparisons
- `research/watchlists/` — Tracking lists for emerging signals
- `_radar/` — Signal radar entries (dated, collection-driven)
- `_news/` — News and signal updates

Research content is opinionated but conservative. It does not claim official SAP endorsement.

## Content Quality and AI Search Readiness

The primary quality entry point is:

```sh
python3 scripts/content_quality.py audit --site-dir _site
```

Supported commands:

```sh
python3 scripts/content_quality.py audit
python3 scripts/content_quality.py check
python3 scripts/content_quality.py check --changed-from origin/main
python3 scripts/content_quality.py report
python3 scripts/content_quality.py fix --safe --dry-run
python3 scripts/content_quality.py baseline
```

Run the audit after a production Jekyll build when validating rendered HTML. `check` is the publication gate: hard safety, canonical, eligibility, privacy, prompt-injection, malformed-artifact, and broken-public-link failures cannot be baselined. Historical editorial warnings may be recorded by `baseline` in `config/content-quality-baseline.json`; never use the baseline to suppress a hard safety error.

The shared normalized page representation lives in `scripts/lib/content_model.py`. Do not create a second definition of public content, canonical URLs, verification, sitemap eligibility, or AI retrieval eligibility in another script. Add policy to `config/content-quality.yml` where practical and give every new rule a stable identifier, remediation text, severity, and fixture test.

The Markdown cluster index is generated by `scripts/generate_atlas_artifacts.py` and written to `ai/markdown-clusters.json`. It dynamically covers public Markdown across Atlas, blog, notes, research, radar, Skill Hub, services, scenarios, datasets, tools, AI pages, localized pages, and related collections. Pages without a route remain deferred; noindex or unverified pages must not become retrieval-eligible. Do not hand-edit generated cluster, expert-evidence, expert-promotion, verified-page, `llms-full.txt`, or related artifacts; regenerate and validate them instead.

Expert context and CTA blocks are opt-in, topic-specific, visible HTML/Markdown attribution. They must link to the canonical website and LinkedIn profile, use a relevant service and public evidence, avoid unsupported superlatives or model instructions, and never turn unverified material into proof of expertise.

Read `docs/content-quality-pipeline.md` for architecture, content models, scoring, hard blockers, baseline workflow, safe-fix boundaries, and CI behavior.

## Services / Entity Positioning

Services describe the engagement model:
1. **Diagnose** — SAP transformation friction audit
2. **Stabilize** — O2C / integration / AMS improvement
3. **Structure** — Operational memory and handover model
4. **Extend** — Side-by-side AI and automation

The services layer is the commercial signal. It must remain accurate, non-exaggerated, and aligned with the Atlas evidence layer.

## Content Safety Rules

- **Every committed file is public.** Do not commit LinkedIn exports, raw dumps, local configs, secrets, private notes, bytecode, caches, `_site/`, or temporary transfer folders.
- Do not add personal email or phone data unless the task explicitly says it should be public.
- Before adding or reusing any third-party logo, icon, trademark, or brand asset, verify the license or obtain written permission.
- Keep canonical dataset content under `datasets/`; do not reintroduce root duplicate folders such as `TRIZ-bytes/`, `DAMA/`, `LLM-prompts/`, `agentic-bytes/`, or dated transfer folders.
- **Never expose client names, ticket numbers, internal incident IDs, or proprietary system details.**
- **Never publish private corpus content.** Draft notes, raw research, and unverified material stay local or in noindex areas.
- Treat `config/content-quality.yml` as public policy. Do not add real credentials, personal contact data, local absolute paths, private corpus identifiers, or client-specific patterns to it.
- Keep quality reports free of matched secret values and personal data. Reports may be generated locally under `reports/`, but do not turn ignored reports into a private-data dump or commit `_site/` output.

## Writing and Editorial Profile

Before writing or editing any **article-like content**, agents must read, in order:

1. `AGENTS.md` (this file)
2. `docs/content/author-editorial-profile.md`
3. `docs/templates/README.md`
4. `docs/site-content-design-contract.md`
5. The relevant page template or collection rules (e.g., `docs/templates/atlas-diagnostic-page.md`, `docs/ai/AGENT_TASK_PATTERNS.md`, `docs/research/RESEARCH_CONTRACT.md`)

**Article-like content** includes Atlas pages, Skill Hub pages, scenarios, diagnostics pages, blog/articles, glossary expansions with explanatory prose, public-facing guides, content clusters, and SEO/AI-readable educational pages.

The profile is **mandatory input**, not optional style advice. Apply it as a decision system for practical expert framing, clear problem → diagnostic → action structure, sober non-hype language, optional author perspective, and avoiding generic AI-written prose.

Rules:

- The profile is a **decision system**, not a fixed article template. Do not mechanically copy phrases, examples, or prior article patterns.
- Do not use the profile to invent personal claims, add unverifiable experience, over-personalize technical pages, replace source-backed facts, change indexing policy, stuff keywords, or paste the same author comment into every article.
- Apply strong informational editing: remove filler, vague wording, decorative language, and claims that do not help the reader act.
- An author perspective may appear near the end of an article when it adds useful judgment, caution, or interpretation. It must be natural, integrated, and restrained. Do not force it, do not use cliché labels such as "My take" or "Author's note" by default, and do not invent personal stories.

## Verification / Indexing Rules

The repository uses a three-level content verification system:

| Level | Status | Frontmatter | Indexing |
|-------|--------|-------------|----------|
| 1 — Review candidate | `needs_verification` | `verified: false`, `robots: noindex,follow`, `sitemap: false` | **Noindex** |
| 2 — Verified | `reviewed` | `verified: true`, `robots: index,follow`, `sitemap: true` | **Indexable** |
| 3 — Flagship | `reviewed` + source-backed | `verified: true`, strong internal links, cited sources | **Strong signal** |

- Only Level 2+ pages appear in `llms-full.txt`.
- Only Level 2+ pages appear in section sitemaps.
- The `scenarios/index.md` is currently **Level 1** (`needs_verification`, `noindex`). Scenario pages default to Level 1 and are promoted to Level 2 individually after human review (e.g., the executive decision-cluster scenarios are Level 2).
- Do not mark any page verified without human review.
- Do not add unverified pages to sitemap or `llms-full.txt`.

Read `docs/ai/CONTENT_VERIFICATION_POLICY.md` for the full policy.

## Common Commands

```sh
# Setup
./bin/setup

# Full validation sequence (run before publishing)
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/check_public_repo.py
bundle exec jekyll build
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site

# Dataset generators
python3 bin/enrich_datasets.py
python3 bin/generate_dataset_pages.py
node scripts/generate_dama_pages.js

# Atlas artifact generation
python3 scripts/generate_atlas_artifacts.py

# Sitewide quality and AI-search readiness
python3 scripts/content_quality.py audit --site-dir _site
python3 scripts/content_quality.py check --site-dir _site
python3 scripts/generate_atlas_artifacts.py --check

# Local preview
bundle exec jekyll serve
```

## What Agents May Edit

- `_data/*.yml` — repeatable content (resume, home, certifications, etc.)
- `atlas/**/*.md` — new or existing Atlas pages (follow verification rules)
- `scenarios/*.md` — new or existing Scenario pages (default to Level 1)
- `research/**/*.md` — research briefs, comparisons, watchlists
- `labs/**/*` — Lab working material; preserve verification and publication rules
- `frameworks/index.md` and existing framework source directories — structure and method work when explicitly in scope
- `datasets/**/*.json` — dataset entries (follow schema)
- `ai/*.json`, `ai/*.yml` — machine-readable exports when not generator-owned
- `config/content-quality.yml` — quality policy and discovery configuration
- `config/content-quality-baseline.json` — generated non-critical warning baseline; update intentionally with `content_quality.py baseline`
- `scripts/lib/*.py` — shared content-model and quality support logic
- `scripts/content_quality.py` — primary quality pipeline entry point
- `docs/content-quality-pipeline.md` — pipeline documentation
- `docs/ai/*.md` — AI readiness documentation
- `_includes/atlas/*.html` — Atlas components (author block, disclaimer, status badge)
- `_includes/sections/*.html` — section partials
- `scripts/*.py`, `bin/*.py` — generators and validators
- `tests/*.py` — test files

## What Agents Must Not Edit

- `index.md` (homepage) — unless explicitly instructed
- `about.md` (profile) — unless explicitly instructed
- `services/*.md` — unless explicitly instructed
- `legal/*.md` — unless explicitly instructed
- `_site/` — generated; never edit directly
- `llms-full.txt` — generated by `scripts/generate_atlas_artifacts.py`
- `ai/markdown-clusters.json`, `ai/expert-evidence.json`, `ai/expert-promotion-inventory.json`, `ai/verified-pages.json`, `ai/rag/related.json`, and other generated AI artifacts — regenerate; do not hand-edit
- `reports/content-quality*.{md,json}`, `reports/content-link-graph.json`, `reports/content-review-queue.md` — generated audit outputs; do not hand-edit
- `sitemap-*.xml` — generated; never edit directly
- `robots.txt` — unless explicitly instructed
- Any file containing private corpus, client data, or unverified draft material
- Any verified page's `verified: true` status — agents may not promote content

## Validation Commands

Before any PR that touches content, structure, datasets, or config:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/check_public_repo.py
bundle exec jekyll build --trace
python3 scripts/content_quality.py check --site-dir _site
python3 scripts/generate_atlas_artifacts.py --check
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
python3 scripts/check_page_quality.py --site-dir _site --fail-on-critical
python3 scripts/check_structured_data.py _site
git diff --check
```

Run the smallest relevant set first, then the full sequence before publishing.

## PR Rules

- One logical change per PR.
- Include a clear description of what changed and why.
- If adding Atlas or Scenario pages, note their verification level.
- If changing generated files, note which generator command produced them.
- Do not mix content changes with unrelated cleanup.
- Use the PR template in `.github/PULL_REQUEST_TEMPLATE/atlas-signal-update.md` when applicable.

## No-Private-Corpus Rule

- Draft notes, raw research, and unverified material must stay in local working directories or noindex collections.
- Do not commit private working notes to public paths.
- Do not expose internal incident details, client names, or proprietary configuration.
- If in doubt, leave it out.

## No-Invented-Validation-Success Rule

- Agents must not claim a page is verified, reviewed, or source-backed unless the frontmatter and human review history confirm it.
- Agents must not invent external links, citations, or validation results.
- Agents must not claim SEO or AI discoverability improvements without running the actual validation commands.

## Deeper Documentation

- `PROJECT_MAP.md` — compact repository and product map
- `ARCHITECTURE.md` — product architecture, stable URL rules, storage model, and validation contract
- `docs/ai/ENTITY_MODEL.md` — public entity model for Dzmitryi Kharlanau
- `docs/ai/RECOMMENDATION_POSITIONING.md` — when AI systems should consider this site relevant
- `docs/ai/CONTENT_VERIFICATION_POLICY.md` — full verification and indexing policy
- `docs/ai/AGENT_TASK_PATTERNS.md` — safe task templates for future agents
- `docs/ai/AI_VISIBILITY_AUDIT.md` — how to test AI/search visibility
- `docs/site-structure-inventory.md` — full site structure inventory
- `docs/site-content-design-contract.md` — design and editorial contract
