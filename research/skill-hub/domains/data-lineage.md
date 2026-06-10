---
title: "Domain Research: Data Lineage"
robots: noindex
sitemap: false
---

# Data Lineage

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from data lineage tracing, transformation documentation, and lineage gap analysis?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [OpenLineage Specification](https://openlineage.io/docs/) (src-007) | 1 | Open standard for data lineage | Job, Run, Dataset event models |
| [DataHub Documentation](https://datahubproject.io/docs/) (src-006) | 2 | Open-source metadata platform | Lineage ingestion, governance |
| [Confluent Schema Registry](https://docs.confluent.io/platform/current/schema-registry/develop/api.html) (src-004) | 1 | API and compatibility mechanics | Compatibility modes, ruleSet attachments |

## Key practical patterns

- Trace from consumer backward to original source.
- Document every hop: system, component, transformation, owner, trust level.
- Label trust levels: verified, inferred, claimed.
- Flag manual steps (spreadsheets, email, manual upload) as high-risk hops.
- Use open standards (OpenLineage) for lineage collection.

## Artifacts found

- Data Lineage Map (source-to-consumer path)
- Lineage Gap Report
- Gap Closure Plan
- Lineage Hop Log

## Decision rules found

- If multiple orchestrators are used, then standardize lineage collection on an open standard.
- If a hop is claimed by an expert but not verified in system logs, label it "inferred."
- If a transformation changes business meaning, document it as a semantic transformation.
- If a lineage path includes a manual step, treat it as a high-risk hop.
- If a hop owner is missing, assign a new owner before closing the gap.

## Quality gates found

- Coverage audit for tier-1 pipelines.
- Every hop has a named system, component, and owner.
- Every transformation is documented with logic and business reason.
- Parallel or alternate paths are documented.

## Common failure modes

- Trusting a single expert's memory without verifying in code or logs.
- Documenting only the happy path and ignoring error handling.
- Treating lineage as a one-time documentation exercise.
- Focusing on technical hops and ignoring business ownership.
- Producing a visual diagram without a tabular backup.

## Candidate skills

- `openlineage-integration-and-instrumentation`
- `lineage-gap-analysis`
- `transformation-documentation`
- `lineage-map-design`

## Source-backed notes

- OpenLineage defines Job, Run, and Dataset event models (src-007).
- DataHub covers lineage ingestion and governance (src-006).
- Confluent Schema Registry defines compatibility modes (src-004).

## Gaps / further research needed

- Automated lineage extraction tools and graph-based lineage databases are not covered.
- Real-time lineage tracking for streaming data needs more research.
