---
name: enterprise-context-graph
description: Extend the Enterprise Context Lab with consistent entities, typed relationships, evidence, reasoning, and validation.
---
# Enterprise Context Graph Modeling

Use this skill when adding or restructuring Lab topics, SAP process models, application landscapes, master-data models, integration maps, failure paths, or assessment-oriented knowledge graphs.

## Purpose

Turn a subject into a reusable graph instead of a standalone article. The result should support human learning, architecture discussion, diagnostics, and machine retrieval from the same structured source.

## Required inputs

- the business or architecture question;
- scope and exclusions;
- relevant SAP/business domain;
- existing adjacent Lab topics;
- evidence requirements and freshness sensitivity.

## Workflow

1. Read `_data/labs/enterprise_context/schema.yml`, `model_contract.yml`, and `manifest.yml`.
2. Search existing topics for canonical IDs, aliases, and overlapping concepts.
3. Define the smallest useful entity set. Reuse identities before creating new ones.
4. Separate ontology, topic graph, and presentation concerns.
5. Add directed relations from the controlled edge vocabulary. Prefer relationships that expose sequence, dependency, determination, integration, causality, ownership, control, testing, or measurement.
6. Separate documented facts from professional experience, expert heuristics, interpretations, and synthetic examples.
7. Register source metadata before attaching `source_refs`.
8. Add failure modes, root causes, tests, diagnostic questions, and decision trade-offs when they make the topic more useful for lead-level reasoning.
9. Run `python3 scripts/validate_enterprise_context.py` before changing public presentation.
10. Render pages as views over structured data. Do not duplicate the semantic model in page prose or UI configuration.

## Decision rules

- Stable identity beats convenient duplication.
- A title can change; a semantic ID normally should not.
- Prefer a typed edge over burying an important dependency inside prose.
- Prefer a bounded topic graph over an exhaustive product catalogue.
- A documented claim without traceable evidence is incomplete.
- A heuristic should be useful even when no product name is present.
- A synthetic scenario must remain visibly synthetic.
- Release-sensitive claims need a product/release boundary and a recent verification date.
- If a graph relation cannot be explained in one sentence, add a rationale or reconsider the edge.

## Output format

A strong change normally contains:

- topic metadata and scope;
- canonical entities with stable IDs;
- typed directed relations;
- evidence references and confidence;
- decision drivers or heuristics;
- relevant failure modes and tests;
- a synthetic example only when it adds explanatory value;
- passing graph validation.

## Quality gates

Reject or fix the change when it introduces:

- unresolved relation endpoints;
- unknown edge types;
- unknown source references;
- duplicate relation triples within a topic;
- conflicting reuse of an entity ID;
- invented project history or confidential context;
- a public page that exposes private authoring workflow instead of the knowledge itself.

## References

- `_data/labs/enterprise_context/AGENTS.md`
- `_data/labs/enterprise_context/schema.yml`
- `_data/labs/enterprise_context/model_contract.yml`
- `_data/labs/enterprise_context/manifest.yml`
