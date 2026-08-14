# Enterprise Context Lab working state

Updated: 2026-08-14

This file records the current engineering baseline for the Enterprise Context Lab. Read it before redesigning the model or introducing parallel conventions.

## Current foundation

The Lab is treated as a structured knowledge graph with three distinct layers:

1. **Ontology** — canonical concepts, stable IDs, node types, and reusable semantic identity.
2. **Topic graph** — bounded SAP or enterprise subjects expressed through typed directed relations, evidence, confidence, failures, tests, and reasoning.
3. **Presentation** — human-readable pages, grouping, filtering, and visual graph views derived from structured data.

Do not collapse these layers into one topic-specific YAML format or duplicate the semantic model inside page markup.

## Control files already in place

- `schema.yml` — node types, edge vocabulary, statuses, evidence types, source contract, assertion contract, freshness fields, and stable ID rules.
- `manifest.yml` — Lab purpose, maturity gates, reference enterprise, human views, and machine endpoints.
- `model_contract.yml` — identity rules, relation rules, evidence discipline, quality gates, and the model-first authoring sequence.
- `AGENTS.md` — scoped authoring rules for this Lab data tree.

These files are the baseline. Extend them deliberately; do not create competing contracts unless a migration is intentional.

## Graph modeling capability already created

A reusable agent skill exists at:

`agent-skills/skills/enterprise-context-graph/`

It includes:

- `SKILL.md`
- `references/method.md`
- `references/templates.md`
- `references/examples.md`

The skill is indexed in `agent-skills/skill-index.yml` and included in the `solution-architecture` and `full-professional` profiles.

Use this skill for new Lab subjects such as sales, ATP, pricing, master data, MDG, procurement, automotive JIT/JIS, integration architecture, SAP development models, AI capabilities, and cross-domain scenarios.

## Validation already created

`python3 scripts/validate_enterprise_context.py`

The validator checks structural graph integrity, including:

- YAML parsing;
- required topic and source fields;
- valid topic status;
- canonical entity type/prefix consistency;
- conflicting reuse of an entity ID;
- known edge types;
- resolved `from` and `to` relation endpoints;
- valid evidence and confidence values;
- duplicate relation triples inside a topic;
- registered `source_refs`;
- documented relations without evidence references;
- self-relations without rationale;
- topic tags.

Repository tests exist in `tests/test_enterprise_context_model.py`, including a repository-wide integrity test and focused negative cases.

## CI integration already created

Changes under `agent-skills/**` trigger the existing Agent tools validation workflow.

The graph foundation was introduced through branch `agent/lab-graph-foundation` and draft PR `#244`.

At the time this state was recorded:

- Agent tools validation passed, including agent-skill validation, npm tests, and smoke tests.
- Repository Python tests with the Enterprise Context validator passed on the implemented graph foundation.
- Full site CI remained part of the normal Jekyll and site-quality publication pipeline.

Treat CI state as historical here; check the current PR or branch before claiming present validation success.

## Existing modeling rules to preserve

- Reuse canonical IDs across topics when the semantic concept is the same.
- Titles may change; semantic IDs normally should not.
- A relationship is directional: `from -> type -> to`.
- Prefer typed edges for important dependencies instead of hiding them only in prose.
- Register sources before referencing them.
- Separate documented facts, professional experience, expert heuristics, interpretation, inference, and synthetic examples.
- Keep release-sensitive claims scoped and dated.
- Prefer a deep bounded vertical over a broad product catalogue.
- Add failures, root causes, tests, controls, KPIs, integrations, and diagnostic heuristics when they improve architectural reasoning.
- Validate the structured model before changing graph presentation.

## Public boundary

Public Lab pages should show the knowledge, model, evidence, architecture reasoning, and useful examples. Keep private tooling and internal authoring workflow out of the public presentation.

Everything committed to this repository is public. Never store confidential client, employer, partner-only, credential, restricted training, or private incident material here.

## Default continuation protocol

When expanding the Lab:

1. Read this file, `AGENTS.md`, `schema.yml`, `model_contract.yml`, and `manifest.yml`.
2. Inspect adjacent topics and search for reusable IDs.
3. Frame the business or architecture question and scope.
4. Model the minimum useful canonical entity set.
5. Add typed relations and evidence.
6. Add decision logic, failures, tests, and heuristics where useful.
7. Run `python3 scripts/validate_enterprise_context.py`.
8. Run focused tests.
9. Update or create human views only after the graph is coherent.

Do not restart the architecture from scratch merely because a new topic is large. New domains should extend the existing graph contract unless a concrete limitation justifies a controlled schema change.
