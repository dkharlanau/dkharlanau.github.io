# Dzmitryi Kharlanau — SAP Transformation, Enterprise Operations & Agentic AI

This repository powers the public professional website and knowledge base of **Dzmitryi Kharlanau**, an SAP consultant and system analyst working across SAP transformation, enterprise operations, SD/MM, MDG, integrations, data governance, AMS, and practical agentic AI.

The site is designed as three things at once: a human-readable professional profile, a source-backed enterprise knowledge base, and a machine-readable discovery surface for search engines, retrieval systems, and AI agents.

- **Live site:** https://dkharlanau.github.io/
- **Open-source products:** https://dkharlanau.github.io/products/
- **LinkedIn:** https://www.linkedin.com/in/dkharlanau/
- **About:** https://dkharlanau.github.io/about/
- **Services:** https://dkharlanau.github.io/services/
- **SAP / enterprise knowledge:** https://dkharlanau.github.io/atlas/
- **Datasets:** https://dkharlanau.github.io/datasets/
- **AI discovery:** https://dkharlanau.github.io/ai/
- **llms.txt:** https://dkharlanau.github.io/llms.txt

## Professional focus

- SAP transformation and enterprise delivery
- SAP SD/MM, order-to-cash, procure-to-pay, logistics, pricing, billing, delivery, and inventory issues
- Business partner, customer, vendor, MDG, master data governance, and migration
- IDoc, API, middleware, interface monitoring, and cross-system diagnostics
- SAP AMS, incident triage, root-cause analysis, operational handover, and support-model improvement
- Data quality, reusable runbooks, operational memory, and enterprise knowledge systems
- AI-assisted diagnostics, retrieval, documentation, automation, and agentic workflows
- Safe boundaries between deterministic enterprise processes and autonomous/agentic behavior

## Open-source product system

The public repositories form a composable **Enterprise Transformation Toolkit**. Each product has one bounded job and can be adopted independently; cross-product composition is based on explicit ownership, stable references, deterministic projections, and retained evidence.

Start from the problem rather than from the portfolio:

| Need | Product |
| --- | --- |
| Describe and govern a business process | [Process as Code](https://github.com/dkharlanau/process-as-code) |
| Make business rules executable and reviewable | [Decision Tables as Code](https://github.com/dkharlanau/decision-tables-as-code) |
| Govern source-to-target mappings | [Mapping as Code](https://github.com/dkharlanau/mapping-as-code) |
| Make enterprise integrations operable and reviewable | [Interface as Code](https://github.com/dkharlanau/interface-as-code) |
| Prove migration or replication state | [Reconciliation as Code](https://github.com/dkharlanau/reconciliation-as-code) |
| Analyze transformation dependencies | [Transformation Graph](https://github.com/dkharlanau/transformation-graph) |
| Analyze the blast radius of a concrete change | [Enterprise Change Graph](https://github.com/dkharlanau/enterprise-change-graph) |
| Coordinate cutover readiness and contingency | [Cutover Graph](https://github.com/dkharlanau/cutover-graph) |
| Connect project claims to fresh evidence | [Project Evidence Graph](https://github.com/dkharlanau/project-evidence-graph) |
| Diagnose SAP-heavy operations from bounded evidence | [SAP Agentic Operations](https://github.com/dkharlanau/sap-agentic-operations) |
| Generate business-readable visuals from semantic models | [Visual Workbench](https://github.com/dkharlanau/visual-workbench) |
| Turn sources into evidence-backed cumulative learning | [Signal to Insight](https://github.com/dkharlanau/signal-to-insight) |
| Resolve public web interfaces for agent/tool use | [Agent-Ready Web Profile](https://github.com/dkharlanau/agent-ready-web-profile) |

The canonical portfolio map, product boundaries, and interoperability contracts live at **https://dkharlanau.github.io/products/** and in [`products/manifest.json`](products/manifest.json). The portfolio deliberately avoids a universal writable enterprise graph: domain semantics remain owned by their source products and are referenced or projected into analysis layers.

## Public knowledge system

The repository contains reviewed public material organized around practical enterprise work rather than generic AI demos. Main areas include:

- **Atlas** — SAP diagnostics, concepts, maps, data quality, AI operations, and automation notes
- **Scenarios** — business-problem-to-diagnostic-workflow mappings
- **Skill Hub** — reusable workflows for consultants, analysts, and AI agents
- **Research / Radar** — source-backed monitoring and comparisons
- **Datasets** — structured public data collections and schemas
- **AI endpoints** — machine-readable manifests, indexes, structured identity, and agent-routing surfaces

## Agent-ready surfaces

The site exposes controlled public interfaces intended to make the same verified knowledge understandable to humans and machines:

- `robots.txt` and sitemaps
- `llms.txt` and reviewed Markdown resources
- Agent Skills / `SKILL.md` packages
- JSON/NDJSON datasets and schemas
- structured Atlas manifests and compact retrieval indexes
- provenance, citation, licensing, and verification metadata
- an Agent-Ready Web Profile reference implementation

This is complementary to normal SEO and public web publishing. It is not presented as a ranking shortcut.

## Why this repository exists

Professional expertise increasingly needs more than a platform profile. This repository provides a canonical, citable, version-controlled source that connects **Dzmitryi Kharlanau** with concrete SAP, enterprise-operations, data-governance, and agentic-AI work.

The goal is to make professional capability inspectable: architecture, research, datasets, reusable methods, and working interoperability experiments are public where they can safely be public.

## Supporting and earlier projects

- **Dataset repository:** https://github.com/dkharlanau/dkharlanau-datasets
- **AI-Ready CV Builder:** https://github.com/dkharlanau/ai-cv-builder — an earlier experimental professional-identity prototype; the main site and ARWP now cover the broader use cases.

## Trust and boundaries

This is an independent personal project. It is not an official SAP, employer, or client repository.

Only intentionally public material belongs here. Client information, internal ticket numbers, private incident data, secrets, credentials, and proprietary exports must not be committed.

SAP-related material is practical diagnostic and research content, not official SAP documentation. Any configuration, process, integration, or automation decision must be validated in the relevant system landscape.

See `CITATION.md`, `CITATION.cff`, `LICENSE`, `LICENSE-DATA`, and `AGENTS.md` for attribution, licensing, and usage boundaries.
