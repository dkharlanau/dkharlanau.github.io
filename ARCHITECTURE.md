# Site Architecture

This repository is a public Jekyll site, knowledge system, and machine-readable source layer. The physical directory tree is intentionally richer than the global navigation. Product architecture and storage architecture are related, but they are not the same thing.

## Product model

The site has six top-level product areas:

1. **Profile** — identity, experience, certifications, and public professional context.
2. **Knowledge** — Atlas, Scenarios, Research, Journal, and Notes.
3. **Labs** — active SAP, AI, operational, interview, and assessment workspaces.
4. **Frameworks** — reusable reasoning and execution methods.
5. **Machine layer** — datasets, AI-readable exports, skills, tools, and MCP source packages.
6. **Services** — consulting offers and engagement context.

The global header should navigate products, not expose every content collection. Deep links belong inside their product hub.

Canonical product hubs:

- `/knowledge/`
- `/labs/`
- `/frameworks/`
- `/machine/`
- `/services/`

Profile is reached through `/`, `/about/`, and `/cv/`.

### Decision Lab thesis

The six product areas work together as one evidence-backed SAP Enterprise and Business AI Decision Lab. The canonical product thesis, evidence chain, authority themes, and non-goals are defined in [`docs/decision-lab-product-thesis.md`](docs/decision-lab-product-thesis.md).

Business AI structured data follows the canonical contract in [`_data/labs/business_ai/contract.yml`](_data/labs/business_ai/contract.yml), with implementation guidance in [`docs/business-ai-data-contract.md`](docs/business-ai-data-contract.md). New graph, agent, analysis, and evidence views must extend or consume that contract instead of creating a parallel source model.

## Stable URL principle

Do not mass-move established content only to make the directory tree look like the product taxonomy. Existing external and internal links are part of the architecture.

Use these rules:

- Keep mature deep routes stable.
- Add hubs, aliases, or redirects when the information architecture changes.
- Use canonical links on compatibility pages.
- Run the built-site link checker after every structural change.
- Change a canonical deep route only when there is a concrete benefit that justifies redirect and link-migration work.

Examples:

- `/lab/` is a compatibility alias for `/labs/`.
- `/labs/reusable-data-procedures/` redirects to canonical `/reusable-data-procedures/`.
- The UI calls `/labs/enterprise-context/` **SAP Enterprise**, while the established physical URL remains stable.
- `/triz/`, `/ddd/`, and `/reusable-data-procedures/` remain canonical routes but are grouped under the Frameworks product.

## Knowledge architecture

`/knowledge/` is the human entry point for content with different purposes and maturity levels.

- `atlas/` — curated concepts, diagnostics, SAP notes, maps, data quality, automation, and AI operations.
- `scenarios/` — business problems connected to SAP context and diagnostic workflows.
- `research/` — briefs, comparisons, watchlists, and changing evidence.
- `_blog/` + `blog/` — long-form analysis.
- `_notes/` + `notes/` — shorter working notes.
- `_radar/`, `_news/` — dated signals.

A topic can appear in several views, but its primary source should not be duplicated. Use links and metadata to express relationships.

## Lab architecture

`/labs/` contains active workspaces, not every method or dataset.

### SAP Enterprise

Physical path: `labs/enterprise-context/`.

The workspace covers:

- business domains and deployment context;
- Sales, pricing, ATP, shipping, billing, credit, tax, and diagnostics;
- Procurement, inventory, EWM, transportation, production, and quality;
- master data, MDG, and data governance;
- integration, development, analytics, and AI touchpoints;
- industry and cross-functional capabilities.

Directory placement is not the knowledge graph. Cross-domain relationships should be expressed in structured metadata and links.

### AI Ready

`labs/ai-ready/` covers data, retrieval, MCP, agents, tools, evaluations, security, deployment, and production boundaries.

### Business AI

`labs/business-ai/` connects business process, AI job, reusable pattern, technology family, control, outcome, and evidence.

### Interview Readiness

`labs/interview-readiness/` is a preparation layer over the existing SAP, AI, and Assessment material. It does not create a second source of truth for SAP topics.

The workspace has five views:

- `roadmap/` — browser-local topic states: Not reviewed, Refreshed, Can explain, Can defend;
- `questions/` — interview prompts across explanation, tracing, diagnosis, design, challenge, and Lead judgment;
- `stories/` — browser-local project evidence structured as context, role, decision, trade-off, result, and lesson;
- `practice/` — a balanced mixed interview session across Sales, Procurement and Logistics, Integration and Architecture, AI and Data, and Lead judgment;
- `progress/` — combined roadmap depth, practice history, and story coverage.

Interview Readiness stores only preparation state in browser localStorage. It remains separate from Assessment attempt history so self-reported topic depth is not confused with scored case evidence.

### Assessment

`labs/assessment/` is a practice and evaluation layer. It reuses Lab and Knowledge material instead of copying it. It covers explanation, tracing, diagnosis, design, challenge, mocks, review, evidence coverage, and progress.

Interview Readiness answers “what should I repeat and can I discuss it in an interview?”. Assessment answers “can I reason through a case under pressure?”. The two layers may link to the same source material but should not merge their scoring models.

### Operational Protocols

`labs/templates/` contains reusable operational protocols such as RCA, integration failure analysis, runbooks, change impact, cutover, and hypercare. It is exposed from both Labs and Frameworks because it is used for practice and as a reusable method.

## Framework architecture

`/frameworks/` groups reusable methods that should travel across domains:

- `triz/` — TRIZ for Digital Systems;
- `ddd/` — structured decision design;
- `reusable-data-procedures/` — governed repeatable data work;
- `labs/templates/` — operational analysis and execution protocols.

A framework should not be copied under SAP, AI, or data merely because a case uses it.

## Machine layer

`/machine/` is a human-readable map to machine-facing assets.

- `datasets/` — canonical structured datasets.
- `ai/` — JSON/YAML exports, generated indexes, discovery maps, evidence surfaces.
- `skill-hub/` — human-readable capability map.
- `agent-skills/` — portable installable agent skill packages.
- `agent-tools/` — static public tool descriptions.
- `mcp/` — source and documentation for local MCP packages.
- `.well-known/` — discovery manifests.

GitHub Pages remains a static host. It does not execute MCP, agents, databases, authentication services, or private runtime components.

## Jekyll and rendering

- **Static site generator:** Jekyll 4.
- **Content inputs:** Markdown, HTML, JSON/YAML, and Jekyll `_data/`.
- **Shared UI:** `_includes/` and `_layouts/`.
- **Design system:** `assets/main.css` and shared component classes.
- **Collections:** `_blog/`, `_notes/`, `_radar/`, `_news/`, `_glossary/` and configured Jekyll collections.

The homepage uses `index.md`, `_data/home.yml`, and section includes. Resume/profile views reuse structured profile data where possible.

## Generated and AI-readable artifacts

Generated output must be treated as output, not source.

Examples include:

- `_site/`;
- `llms-full.txt`;
- Atlas manifests and compact indexes;
- expert evidence and promotion inventories;
- related-page indexes;
- sitemap files;
- content-quality reports.

Fix the source or generator, regenerate, and validate. Do not patch generated files by hand.

## Link and publication validation

The structural safety contract is enforced through CI. A normal validation sequence is:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/check_public_repo.py
bundle exec jekyll build --trace
python3 scripts/content_quality.py check --site-dir _site
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
python3 scripts/generate_atlas_artifacts.py --check
```

CI also checks indexing policy, sitemap policy, date consistency, content quality, accessibility, AI-readable endpoints, Lab publication policy, and other repository contracts.

A structural change is not complete if required CI checks fail.

## Design rule for future growth

Before adding a new root directory, classify the work:

- durable explanation → Knowledge;
- active exploration, interview preparation, or practice → Lab;
- reusable reasoning/execution method → Framework;
- structured representation for tools → Machine layer;
- commercial offer → Services;
- identity/evidence → Profile.

When a topic becomes large, first deepen its domain model. Do not automatically promote it to a new top-level product. The filesystem has no shortage of folders; the reader has a finite attention span.
