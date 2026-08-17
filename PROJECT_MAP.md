# PROJECT_MAP.md

Compact map of `dkharlanau.github.io`.

Last updated: 2026-08-17

## Site model

The repository contains many physical directories, but the public information architecture is organized into six clusters. Existing public URLs remain stable; hub pages provide the simpler navigation layer.

| Cluster | Hub | Purpose |
|---|---|---|
| Profile | `/` | Professional profile, experience, certifications, publications |
| Knowledge | `/knowledge/` | Published explanations, Atlas, scenarios, research, journal, notes, radar |
| Labs | `/labs/` | Working models, SAP enterprise maps, AI architecture, Business AI, assessment practice |
| Frameworks | `/frameworks/` | TRIZ Digital, Decision-Driven Design, Reusable Data Procedures, reusable skills |
| Machine Layer | `/machine/` | Datasets, AI exports, schemas, entities, agent tools, discovery resources |
| Services | `/services/` | Consulting offers and commercial entry points |

The canonical machine-readable cluster registry is `_data/site_clusters.yml`.

## Public structure

```text
/
├── knowledge/
│   ├── atlas/
│   ├── scenarios/
│   ├── research/
│   ├── blog/
│   ├── notes/
│   └── radar/
│
├── labs/
│   ├── assessment/
│   ├── enterprise-context/
│   ├── ai-ready/
│   ├── business-ai/
│   └── templates/
│
├── frameworks/
│   ├── triz/                         # existing stable URL: /triz/
│   ├── ddd/                          # existing stable URL: /ddd/
│   ├── reusable-data-procedures/     # existing stable URL: /reusable-data-procedures/
│   └── skill-hub/                    # existing stable URL: /skill-hub/
│
├── machine/
│   ├── datasets/                     # existing stable URL: /datasets/
│   ├── ai/                           # existing stable URL: /ai/
│   ├── entities/                     # existing stable URL: /entities/
│   ├── agent-tools/                  # existing stable URL: /agent-tools/
│   ├── agent-skills/                 # existing stable URL: /agent-skills/
│   ├── .well-known/
│   └── mcp/
│
└── services/
```

The tree above is conceptual. Do not physically move established directories only to make the repository mirror the public navigation.

## Labs

### SAP Enterprise Lab

Physical root: `labs/enterprise-context/`

Main areas:

- `domains/`
- `deployment-models/`
- `industries/`
- `sales-processes/`, `sales-order/`, `pricing/`, `atp/`, `shipping/`, `billing/`, `credit/`, `tax/`
- `procurement/`, `inventory-management/`, `material-behavior/`
- `ewm/`, `transportation-management/`, `production/`, `quality-management/`
- `master-data/`, `mdg/`, `data-governance/`
- `integrations/`, `integration-operations/`
- `development/`, `end-to-end-analytics/`, `business-ai/`, `iot-devices/`
- `automotive-jit/`, `finance-logistics/`, `logistics-capabilities/`
- `model/`, `frameworks/`, `data/`

The UI may call this area **SAP Enterprise Lab**. The existing `/labs/enterprise-context/` URL remains stable.

### AI Ready Lab

Physical root: `labs/ai-ready/`

Main areas include agent architecture, data/RAG, MCP/tools, evals, security, system boundaries, engineering, coding agents, examples, practice, and machine-readable data.

### Business AI Lab

Physical root: `labs/business-ai/`

Main model:

`business process -> pattern -> technology -> control -> outcome -> evidence`

Key pages include domains, processes, patterns, technologies, scenarios, cases, practices, matrix, model, and data.

### SAP Lead Assessment Lab

Physical root: `labs/assessment/`

Key areas include core coverage, cross-process reasoning, mock assessment, practice engine, feedback, factual and semantic review, evidence coverage, reasoning coverage and gaps, progress, and promotion readiness.

### Operational Templates

Physical root: `labs/templates/`

Reusable protocols for RCA, incidents, integrations, deviations, runbooks, change impact, decisions, cutover, and hypercare.

## Frameworks

### TRIZ for Digital Systems

Physical root and stable URL: `triz/` -> `/triz/`

The framework includes contradiction analysis, operators, resources, patterns, business-process use, AI boundaries, evolution signals, failure modes, cases, drills, templates, and a workbench.

### Decision-Driven Design

Physical root and stable URL: `ddd/` -> `/ddd/`

Includes the decision canvas, schema, framework data, examples, and agent context.

### Reusable Data Procedures

Physical root and stable URL: `reusable-data-procedures/` -> `/reusable-data-procedures/`

Includes architecture, building blocks, execution model, procedure model, semantic registry, reference data, packs, governance, review inbox, testing, cases, decision memory, schemas, and roadmap.

`labs/reusable-data-procedures/` is a compatibility/entry page. Do not build a second independent content model there.

### Skill Hub

Physical root and stable URL: `skill-hub/` -> `/skill-hub/`

Reusable human and agent skills for architecture, business analysis, DAMA, integration, AI-assisted analysis and development, decision validation, operations, and execution control.

## Knowledge

### Atlas

Physical root: `atlas/`

Curated knowledge areas:

- `concepts/`
- `diagnostics/`
- `sap/`
- `maps/`
- `data-quality/`
- `automation/`
- `ai-operations/`
- `ai-tools/`
- `research-notes/`
- `links/`

New Atlas pages start as unverified/noindex material and move through the publication gates.

### Scenarios

Physical root: `scenarios/`

Business-pain-to-diagnostic-workflow cases across SAP processes, master data, integration, AMS, architecture, and AI.

### Research

Physical root: `research/`

- `briefs/`
- `comparisons/`
- `watchlists/`
- `skill-hub/`

Research is an evidence and exploration layer. Stable conclusions may later be promoted into Atlas, Labs, or Frameworks.

### Journal and notes

- `_blog/` + `blog/`
- `_notes/` + `notes/`
- `_radar/` + `radar/`
- `_news/` + `news/`

## Machine Layer

### Datasets

Physical root: `datasets/`

Includes DAMA, TRIZ datasets, agentic bytes, AI business signals, AMS, Automotive JIT, incident material, LLM prompts, schemas, manifests, and typed collections.

### AI exports

Physical root: `ai/`

Machine-readable catalogs, compact Atlas indexes, expert evidence, discovery maps, generated inventories, incident data, and related exports.

### Agent and discovery resources

- `agent-tools/`
- `agent-skills/`
- `.well-known/agent-skills/`
- `entities/`
- `mcp/`
- `search/`

These are machine and tool entry points, not duplicate human-facing knowledge sections.

## Services

Physical root: `services/`

Current service material covers SAP AMS, O2C, integration architecture and reliability, master data stability, planning and replenishment, AI/ML enablement, mini-apps, and related consulting work.

## Jekyll and platform directories

| Directory | Purpose |
|---|---|
| `_data/` | Jekyll data and registries |
| `_includes/` | Reusable components, navigation, SEO, page blocks |
| `_layouts/` | Page layouts |
| `_plugins/` | Jekyll plugins |
| `assets/` | CSS, JavaScript, images, fonts references |
| `docs/` | Internal project documentation |
| `scripts/` | Generators, validators, maintenance scripts |
| `bin/` | Setup and dataset generation helpers |
| `tests/` | Automated tests |
| `.github/` | Actions and pull request templates |
| `legal/` | Public policies |

## Generated artifacts

Do not edit generated artifacts directly when a source or generator exists.

Important generated outputs include:

- `_site/`
- `llms-full.txt`
- `sitemap.xml`
- `sitemap-pages.xml`
- `sitemap-atlas.xml`
- `sitemap-data.xml`
- `atlas/manifest.json`
- generated AI and dataset catalogs where documented by their generator

## Structural rules

1. Keep established public URLs stable unless there is a strong migration reason.
2. Prefer a hub page and metadata relationship over copying the same content into another root.
3. Knowledge explains. Labs model and exercise. Frameworks define reusable methods.
4. Machine Layer exposes structured access and contracts; it should point back to canonical human material.
5. Cross-cutting SAP entities belong to a graph of relationships, not to one folder hierarchy only.
6. New navigation groups should be registered in `_data/site_clusters.yml`.
7. Run link and content validation after structural changes.
8. Never publish client data, private corpora, credentials, or internal incident details.
