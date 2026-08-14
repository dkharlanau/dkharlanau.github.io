# Enterprise Context Lab authoring rules

This file applies to `_data/labs/enterprise_context/**`.

The Lab is a structured knowledge graph first and a collection of pages second. Keep changes data-first, source-tracked, and reusable across topics.

## Read before editing

1. `schema.yml` — vocabulary and stable ID prefixes.
2. `model_contract.yml` — graph layers, integrity rules, and authoring sequence.
3. `manifest.yml` — Lab purpose, maturity gates, public views, and machine endpoints.
4. The nearest existing topic and relevant source registry files.

## Working model

Use three separate layers:

- **Ontology** — canonical identities and types. Reuse stable IDs for the same concept.
- **Topic graph** — bounded scenario, entities, directed typed relations, evidence, failures, tests, and reasoning.
- **Presentation** — human-readable grouping and narrative. Never create a competing semantic model only to make a page easier to render.

## Before adding an entity

Search all topic files for the concept and likely aliases. Reuse an existing ID when the semantic identity is the same. Create a new ID only when the concept is genuinely distinct.

Prefer the narrowest useful node type from `schema.yml`. Keep the ID stable and move wording changes into `title`, `summary`, aliases, or topic-specific explanation.

## Before adding a relation

Check that both endpoint IDs exist. Use only an edge type declared in `schema.yml`. Treat direction as meaningful. Do not duplicate the same `from/type/to` triple inside one topic.

Every material relation should answer a useful question such as:

- what contains or specializes this concept;
- what precedes or triggers it;
- what data it reads, writes, creates, or updates;
- what rule determines it;
- what integration connects it;
- what can fail and what can cause that failure;
- what measures, controls, tests, or validates it;
- what application, platform, deployment model, or business domain owns or supports it.

If a relationship is not obvious, add `rationale`. If it is an externally verifiable fact, attach registered `source_refs`.

## Evidence discipline

Do not blur SAP documentation, project experience, interpretation, and synthetic examples into one voice. Use the evidence classes defined in `schema.yml` and `model_contract.yml`.

For release-sensitive product claims, record the applicable product/release scope and verification date. Register sources under `sources/` before referencing them.

Never add client-confidential, employer-confidential, partner-only, licensed training, credential, or private incident material.

## Topic authoring sequence

1. Frame the business question and scope.
2. Inspect existing IDs and adjacent topics.
3. Add the minimum entities required to explain the problem.
4. Add typed relations that expose the useful structure.
5. Add failure modes, decisions, tests, and diagnostic heuristics where they improve reasoning.
6. Register and attach evidence.
7. Run `python3 scripts/validate_enterprise_context.py`.
8. Only then change presentation pages or graph views.

Depth is more valuable than catalog breadth. A useful topic should expose dependencies, trade-offs, failure paths, and diagnostic questions rather than merely list SAP products or features.

## Public-content boundary

Public content may explain the model, sources, trade-offs, and professional reasoning. Do not describe private authoring tools, assistant collaboration, prompt history, or internal drafting workflow on public Lab pages.

## Validation

Run the smallest check first:

```sh
python3 scripts/validate_enterprise_context.py
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_enterprise_context_model.py
```

Before publication, also follow the repository-wide validation sequence in the root `AGENTS.md`.
