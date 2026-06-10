---
title: "Domain Research: Master Data Management"
robots: noindex
sitemap: false
---

# Master Data Management

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from master data mapping, deduplication, golden record design, and replication governance?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [DAMA-DMBOK 2nd Edition](https://dama.org/content/body-knowledge) (src-001) | 1 | Official body of knowledge for data management | Master data frameworks, governance |
| [SAP Master Data Governance (MDG)](https://help.sap.com/docs/SAP_MASTER_DATA_GOVERNANCE) (src-012) | 1 | Official SAP MDG help documentation | Governance workflows, golden record logic |

## Key practical patterns

- Map master data domains before proposing MDM/MDG tools.
- Define golden record logic at the attribute level, not the record level.
- Measure duplication rate before deduplication campaigns.
- Design replication governance with direction, frequency, trigger, and failure handling.
- Include survivorship rules for conflicting values.

## Artifacts found

- Master Data Domain Map
- Duplication and Fragmentation Analysis
- Golden Record Definition
- Replication Governance Model
- Master Data Governance Plan

## Decision rules found

- If a master data attribute is created in one system and never changed elsewhere, that system is the source of truth.
- If an attribute is updated in multiple systems, designate a hub or winning system.
- If duplication rate exceeds 10%, prioritize deduplication before new integration.
- If no one accepts ownership of a master data domain, do not proceed with tooling.

## Quality gates found

- Every master data domain has a named business owner and data steward.
- Every key attribute has a defined source of truth and conflict resolution rule.
- Duplication rate has been measured and documented.
- Replication paths are documented with direction, frequency, trigger, and owner.

## Common failure modes

- Buying an MDM tool before defining golden record logic.
- Treating all attributes as if they have the same source of truth.
- Deduplicating without survivorship rules.
- Ignoring manual corrections in downstream systems.
- Mapping codes during a merger without deciding the target standard.

## Candidate skills

- `master-data-domain-mapping`
- `golden-record-design`
- `deduplication-strategy`
- `replication-governance`

## Source-backed notes

- DAMA-DMBOK defines master data frameworks and governance (src-001).
- SAP MDG covers governance workflows and golden record logic (src-012).

## Gaps / further research needed

- Advanced probabilistic matching and entity resolution algorithms are not covered.
- MDM platform selection guidance is outside scope.
