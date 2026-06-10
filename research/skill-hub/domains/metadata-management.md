---
title: "Domain Research: Metadata Management"
robots: noindex
sitemap: false
---

# Metadata Management

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from metadata cataloging, lineage tracking, and data discovery?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [DAMA-DMBOK 2nd Edition](https://dama.org/content/body-knowledge) (src-001) | 1 | Official body of knowledge for data management | Metadata frameworks, governance |
| [Microsoft Purview Data Governance](https://learn.microsoft.com/en-us/purview/governance-solutions) (src-003) | 1 | Microsoft official documentation | RBAC, metadata management |
| [DataHub Documentation](https://datahubproject.io/docs/) (src-006) | 2 | Open-source metadata platform | Ingestion, lineage, governance workflows |
| [OpenLineage Specification](https://openlineage.io/docs/) (src-007) | 1 | Open standard for data lineage | Job, Run, Dataset event models |
| [Databricks Unity Catalog](https://docs.databricks.com/en/data-governance/unity-catalog/index.html) (src-011) | 1 | Databricks official documentation | Data catalog, discovery |

## Key practical patterns

- Catalog business, technical, and operational metadata separately.
- Verify technical metadata against actual systems; do not trust documentation alone.
- Use open standards (OpenLineage) for lineage collection across orchestrators.
- Move from batch to real-time streaming ingestion when metadata is stale.
- Link metadata gaps to governance and ownership problems.

## Artifacts found

- Metadata Inventory with business, technical, and operational metadata
- Metadata Gap Report
- AI Readiness Assessment
- Lineage Hop Log
- Lineage Gap Report

## Decision rules found

- If metadata is stale, then move from batch to real-time streaming ingestion.
- If a field has no business definition, do not use it in a report or integration until documented.
- If documentation contradicts actual data, trust the data and flag documentation as stale.
- If a dataset has no documented consumers, question whether it should be maintained.

## Quality gates found

- Metadata freshness check (last ingestion timestamp).
- Connector health and failure monitoring.
- Coverage audit for tier-1 pipelines.
- Every data element has a business definition in plain language.

## Common failure modes

- Cataloging only technical metadata without business meaning.
- Trusting outdated documentation without sampling actual data.
- Letting technical teams define business meanings without validation.
- Trying to catalog everything at once.
- Producing a catalog with no maintenance plan.

## Candidate skills

- `metadata-platform-architecture`
- `openlineage-integration-and-instrumentation`
- `data-catalog-governance`
- `ai-readiness-assessment`

## Source-backed notes

- DataHub covers ingestion, lineage, and governance workflows (src-006).
- OpenLineage defines Job, Run, and Dataset event models (src-007).
- Databricks Unity Catalog covers data catalog and discovery (src-011).

## Gaps / further research needed

- Automated metadata extraction tools and graph-based lineage databases are not covered.
- Real-time lineage tracking for streaming data needs more research.
