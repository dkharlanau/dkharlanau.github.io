---
name: enterprise-context-graph
description: Use when adding, extending, or restructuring Enterprise Context Lab topics, SAP process models, application landscapes, master-data models, integration maps, failure paths, or other knowledge-graph content. Produces canonical entities, typed relationships, evidence links, reasoning structures, and a validated graph. Do not use for prose-only edits that do not change the Lab model.
---

# Enterprise Context Graph Modeling

## Purpose

Turn a subject into a reusable graph instead of a standalone article. The result should support human learning, architecture discussion, diagnostics, assessment preparation, and machine retrieval from the same structured source.

## Use when

- Adding a new SAP or enterprise topic to `_data/labs/enterprise_context/topics/`.
- Extending an existing topic with processes, business objects, master data, applications, integrations, rules, failures, KPIs, tests, scenarios, or AI assets.
- Connecting concepts across sales, procurement, manufacturing, logistics, master data, integration, development, or industry overlays.
- Restructuring duplicated or inconsistent IDs and relationships into a stable graph model.
- Preparing a topic that must support both a compact human page and machine-readable retrieval.
- Modeling architecture trade-offs, diagnostic paths, or assessment questions where the relationships matter as much as the entities.

## Do not use when

- Editing wording, spelling, CSS, layout, or navigation without changing the Lab semantic model.
- Writing an unrelated Atlas, blog, service, or research page that is not backed by Enterprise Context data.
- Capturing client-confidential, employer-confidential, partner-only, licensed training, credential, or private incident information.
- Inventing project history, delivery outcomes, metrics, or personal experience to make a topic appear more authoritative.
- Creating a second ontology solely for one page when the concept can reuse an existing canonical ID.

## Required inputs

- The business, diagnostic, or architecture question.
- Scope and explicit exclusions.
- Relevant SAP or business domain.
- Existing adjacent Lab topics and likely canonical IDs.
- Evidence requirements and freshness sensitivity.
- The intended reasoning value: dependency, decision, failure path, process flow, integration, test, or other relationship that the graph should expose.

## Workflow

1. **Read the contract.** Read `_data/labs/enterprise_context/schema.yml`, `model_contract.yml`, `manifest.yml`, and the scoped `AGENTS.md`.
2. **Search before creating.** Search existing topics for canonical IDs, aliases, and overlapping concepts. Resolve identity before adding a duplicate.
3. **Frame the boundary.** State the business question, scope, exclusions, and what decision or explanation the model must support.
4. **Model the minimum entity set.** Add only the entities needed to explain the topic. Reuse stable IDs where semantic identity is the same.
5. **Connect the graph.** Add directed relations from the controlled edge vocabulary. Prefer relationships that expose sequence, dependency, determination, integration, causality, ownership, control, testing, or measurement.
6. **Separate claims.** Keep documented facts distinct from professional experience, expert heuristics, interpretations, inferences, and synthetic examples.
7. **Register evidence.** Add source metadata under `sources/` before attaching `source_refs`. Include product/release scope for time-sensitive claims.
8. **Add lead-level reasoning.** Capture relevant failure modes, root causes, tests, diagnostic questions, design decisions, and trade-offs rather than stopping at a product catalogue.
9. **Validate the graph.** Run `python3 scripts/validate_enterprise_context.py` and the focused pytest file. Fix integrity errors before presentation work.
10. **Render from data.** Treat Lab pages and graph views as presentation over the structured model. Do not build a competing semantic model in prose or UI configuration.

## Decision rules

- Stable identity beats convenient duplication.
- A title can change; a semantic ID normally should not.
- Prefer a typed edge over burying an important dependency inside prose.
- Prefer a bounded topic graph over an exhaustive product catalogue.
- A documented claim without traceable evidence is incomplete.
- A heuristic should remain useful even when no product name is present.
- A synthetic scenario must remain visibly synthetic.
- Release-sensitive claims need a product/release boundary and a recent verification date.
- If a graph relation cannot be explained in one sentence, add a rationale or reconsider the edge.
- If two topics use the same concept, prefer one canonical ID and topic-specific explanation over two near-duplicate nodes.
- If a new relation type is required, first check whether an existing edge expresses the meaning. Extend `schema.yml` only when the semantic distinction is durable and useful across topics.

## Output format

A strong change normally contains:

- topic metadata, business question, scope, and exclusions;
- canonical entities with stable IDs and controlled types;
- typed directed relations with evidence class and confidence;
- registered source references for externally verifiable facts;
- decision drivers or expert heuristics where useful;
- relevant failure modes, root causes, controls, KPIs, and tests;
- a synthetic example only when it adds explanatory value;
- passing graph-integrity validation;
- presentation changes only after the structured model is coherent.

## Quality gates

- [ ] Existing canonical IDs and aliases were searched before new IDs were created.
- [ ] Entity IDs use the node-type prefixes defined in `schema.yml`.
- [ ] Relation endpoints resolve to known entities.
- [ ] Relation types exist in the controlled edge vocabulary.
- [ ] No duplicate `from/type/to` triple exists inside a topic.
- [ ] Documented claims use registered source IDs where evidence is expected.
- [ ] Facts, heuristics, interpretation, and synthetic content are clearly separated.
- [ ] No confidential or invented project context is present.
- [ ] The topic exposes useful dependencies, trade-offs, failure paths, or diagnostic questions rather than only listing products.
- [ ] `python3 scripts/validate_enterprise_context.py` passes before presentation work is considered complete.

## References

- `references/method.md` — Identity resolution, relation modeling, evidence separation, and validation method.
- `references/templates.md` — Copy-ready YAML patterns for topics, entities, relations, and sources.
- `references/examples.md` — Good and bad examples for SAP process, integration, and master-data graph modeling.
- `_data/labs/enterprise_context/AGENTS.md` — Scoped repository rules.
- `_data/labs/enterprise_context/schema.yml` — Controlled vocabulary.
- `_data/labs/enterprise_context/model_contract.yml` — Lab modeling contract.
- `_data/labs/enterprise_context/manifest.yml` — Lab purpose and maturity model.

## Safety rules

- Treat every committed file as public.
- Keep private tooling and internal authoring workflow out of public Lab pages.
- Never expose client names, internal system identifiers, proprietary configuration, credentials, or restricted source material.
- Do not claim human review, verification, project experience, or delivery outcomes unless repository evidence and user-provided facts support them.
- Prefer primary public documentation for product behavior and release-sensitive claims; do not mirror source text into the repository.
