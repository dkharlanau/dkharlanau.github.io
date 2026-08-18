# PROJECT_MAP.md

Compact map of `dkharlanau.github.io`.
Last updated: 2026-08-18.

## Product Architecture

The public repository has many physical directories, but the site is organised around six product areas. Do not mirror every directory in the global navigation.

| Product area | Primary route | Purpose |
|---|---|---|
| Profile | `/`, `/about/`, `/cv/` | Identity, experience, certifications, public profile |
| Knowledge | `/knowledge/` | Human knowledge entry point for Atlas, Scenarios, Research, Journal, and Notes |
| Labs | `/labs/` | Active workspaces for SAP Enterprise, AI architecture, Business AI, operational protocols, interview readiness, and assessment practice |
| Frameworks | `/frameworks/` | Reusable methods: TRIZ Digital, Decision Design, Reusable Data Procedures, operational protocols |
| Machine layer | `/machine/` | Technical map for datasets, AI-readable exports, skills, tools, and MCP packages |
| Services | `/services/` | Consulting services and commercial signal |

The global navigation should stay product-level. Deep domain navigation belongs inside the relevant product.

### Decision Lab foundation

The six product areas are connected by the canonical [SAP Enterprise & Business AI Decision Lab thesis](docs/decision-lab-product-thesis.md). Its north-star chain links a business problem to process, decision, evidence, architecture/control, outcome, and a reusable Lead recommendation.

Business AI graph and data work must use `_data/labs/business_ai/contract.yml`, explained in [`docs/business-ai-data-contract.md`](docs/business-ai-data-contract.md). New graph artifacts, analytics, and agent context are views over this contract, not new sources of truth.

## Canonical Route Rules

- Keep established deep URLs stable unless there is a strong technical reason to move them.
- Prefer a hub or alias over a mass directory move. A clean taxonomy is not worth breaking external references.
- `/labs/enterprise-context/` remains the canonical physical route for the SAP Enterprise workspace. In UI copy, call the workspace **SAP Enterprise** because its scope now covers far more than context.
- `/lab/` is a compatibility route that redirects to `/labs/`.
- `/labs/reusable-data-procedures/` is a compatibility route that redirects to the canonical `/reusable-data-procedures/` workspace.
- `/triz/`, `/ddd/`, and `/reusable-data-procedures/` remain canonical framework routes even though they are grouped under `/frameworks/` in navigation.
- Generated artifacts, sitemaps, and AI exports must not be hand-edited when a generator owns them.

## Knowledge

| Section | Path | Role |
|---|---|---|
| Knowledge hub | `knowledge/index.md` | Routes users to the correct knowledge maturity and format |
| Atlas | `atlas/` | Curated concepts, diagnostics, SAP notes, maps, data quality, automation, AI operations |
| Scenarios | `scenarios/` | Business pain mapped to process context and diagnostic workflow |
| Research | `research/` | Briefs, comparisons, watchlists, working evidence |
| Journal | `_blog/`, `blog/` | Long-form analysis |
| Notes | `_notes/`, `notes/` | Short-form working observations |
| Radar / News | `_radar/`, `_news/`, `radar/`, `news/` | Dated signals and updates |

## Labs

`labs/` is for active exploration and practice, not for every reusable method.

| Workspace | Physical path | Scope |
|---|---|---|
| SAP Enterprise | `labs/enterprise-context/` | SAP business domains, processes, logistics, data, integration, development, analytics, industries |
| AI Ready | `labs/ai-ready/` | Data, RAG, MCP, agents, evals, security, deployment, production decisions |
| Business AI | `labs/business-ai/` | Process → AI job → pattern → technology → control → outcome → evidence |
| Operational Protocols | `labs/templates/` | RCA, incident response, integration failures, runbooks, cutover, hypercare |
| Interview Readiness | `labs/interview-readiness/` | Interview roadmap, questions, project stories, mixed practice, and browser-local progress across SAP Lead domains |
| SAP Lead Assessment | `labs/assessment/` | Cases, mocks, review, reasoning levels, evidence coverage, progress |

### Interview Readiness relationship

Interview Readiness is a preparation layer over existing Labs. It does not duplicate SAP or AI source material.

- `roadmap/` records four topic states: Not reviewed, Refreshed, Can explain, Can defend.
- `questions/` provides explain, trace, diagnose, design, challenge, and Lead-level prompts.
- `stories/` stores browser-local interview stories structured around context, role, decision, trade-off, result, and lesson.
- `practice/` mixes Sales, Logistics, Integration, AI, and Lead judgment into a balanced session.
- `progress/` combines roadmap depth, practice history, and story coverage.
- Browser-local Interview Readiness state is separate from the scored attempt history used by `labs/assessment/`.

### SAP Enterprise domain map

The existing `labs/enterprise-context/` tree is intentionally not mass-moved. Treat it as a graph with several domain families:

- **Core context:** `domains/`, `model/`, `frameworks/`, `industries/`, `deployment-models/`
- **Sales:** `sales-processes/`, `sales-order/`, `pricing/`, `atp/`, `shipping/`, `billing/`, `credit/`, `tax/`, `condition-contract-management/`, `sales-analytics/`, `sales-diagnostics/`
- **Procurement and logistics:** `procurement/`, `inventory-management/`, `material-behavior/`, `ewm/`, `transportation-management/`, `production/`, `quality-management/`
- **Master data:** `master-data/`, `mdg/`, `data-governance/`, `data/`
- **Technology:** `integrations/`, `integration-operations/`, `development/`, `business-ai/`, `end-to-end-analytics/`, `iot-devices/`
- **Cross-functional / industry:** `automotive-jit/`, `finance-logistics/`, `logistics-capabilities/`

A topic may belong to several families. Do not duplicate it only to satisfy the directory tree. Express cross-domain meaning through links, metadata, and graph relationships.

## Frameworks

| Framework | Canonical path | Purpose |
|---|---|---|
| TRIZ for Digital Systems | `triz/` | Contradictions, separation operators, resource scan, digital patterns, cases, workbench |
| Decision Design | `ddd/` | Decision canvas, structured decision model, schemas, examples, agent context |
| Reusable Data Procedures | `reusable-data-procedures/` | Repeatable file discovery, mapping, validation, procedure execution and governance |
| Operational Protocols | `labs/templates/` | Reusable operational analysis and execution protocols |

Frameworks must remain reusable across SAP, AI, data, and general digital-system cases.

## Machine Layer

| Area | Path | Purpose |
|---|---|---|
| Datasets | `datasets/` | Canonical machine-readable data collections |
| AI-readable exports | `ai/` | JSON/YAML indexes, discovery maps, evidence, generated exports |
| Skill Hub | `skill-hub/` | Human-readable capability map |
| Agent Skills | `agent-skills/` | Portable installable agent skill packages |
| Agent Tools | `agent-tools/` | Static public tool descriptions |
| MCP | `mcp/` | Source and documentation for local MCP packages; GitHub Pages does not execute them |
| Discovery | `.well-known/` | Machine discovery and agent skill manifests |
| Search | `search/` | Human search surface |

## Services and Profile

- `services/` contains consulting service descriptions.
- `about.md`, `cv/`, `certifications.md`, `education.md`, and `publications.md` form the public profile layer.
- Localised home/profile routes live under `de/`, `fr/`, `es/`, `it/`, `nl/`, `pl/`, `pt-br/`, `ar/`, and `zh-cn/`.

## Platform and Build Directories

| Directory | Purpose |
|---|---|
| `_data/` | Jekyll data and structured content inputs |
| `_includes/` | Shared components, navigation, SEO, product partials |
| `_layouts/` | Shared page structure |
| `assets/` | CSS, JavaScript, images, icons |
| `config/` | Content-quality and discovery policy |
| `docs/` | Internal project documentation and contracts |
| `scripts/`, `bin/` | Generators, validators, maintenance tools |
| `tests/` | Automated test suite |
| `.github/` | CI workflows and PR templates |
| `legal/` | Public policies |

## Generated Artifacts

Common generated files include `_site/`, `llms-full.txt`, Atlas manifests and AI indexes, sitemap files, quality reports, and other outputs named by their generators. Never edit generated output to fix the source problem. Fix the source or generator, regenerate, and validate.

## Link Integrity

Structural changes must preserve link integrity.

Minimum validation before merge:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/check_public_repo.py
bundle exec jekyll build --trace
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
python3 scripts/content_quality.py check --site-dir _site
python3 scripts/generate_atlas_artifacts.py --check
```

CI contains additional indexing, sitemap, date, accessibility, AI-endpoint, and Lab publication checks. A structural PR is not ready while required CI checks are failing.

## Where New Work Goes

Use the problem type, not the technology name, to choose the home:

- Durable reviewed explanation → `atlas/`
- Business problem / diagnostic workflow → `scenarios/`
- Fast-moving cited evidence → `research/`
- Active SAP / AI exploration, interview preparation, or assessment practice → `labs/`
- Reusable reasoning or execution method → existing framework under `/frameworks/`
- Canonical structured data → `datasets/`
- Generated or curated machine endpoint → `ai/`
- Portable agent capability → `agent-skills/` or `agent-tools/`

Do not create a new root directory simply because a topic has become large. First decide whether it is a domain inside an existing product, a reusable framework, or a machine-facing representation of existing knowledge.
