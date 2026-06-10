---
title: "Domain Research: Data Governance"
robots: noindex
sitemap: false
---

# Data Governance

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from data governance, ownership models, and policy enforcement?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [DAMA-DMBOK 2nd Edition](https://dama.org/content/body-knowledge) (src-001) | 1 | Official body of knowledge for data management | Governance frameworks, stewardship models, data quality dimensions |
| [AWS Well-Architected Data Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/welcome.html) (src-002) | 1 | AWS official guidance for data analytics architecture | Classification, lineage, quality patterns |
| [Microsoft Purview Data Governance](https://learn.microsoft.com/en-us/purview/governance-solutions) (src-003) | 1 | Microsoft official documentation for Purview | RBAC, access control, metadata management |
| [Data Mesh Principles](https://martinfowler.com/articles/data-mesh-principles.html) (src-010) | 2 | Foundational article on Data Mesh architecture | Federated governance, domain-oriented ownership |
| [Databricks Unity Catalog](https://docs.databricks.com/en/data-governance/unity-catalog/index.html) (src-011) | 1 | Databricks official documentation | Governance, data catalog, access control |
| [SAP Master Data Governance (MDG)](https://help.sap.com/docs/SAP_MASTER_DATA_GOVERNANCE) (src-012) | 1 | Official SAP MDG help documentation | Governance workflows, data quality rules, stewardship |

## Key practical patterns

- Start with ownership before proposing tools or automation.
- Use a three-role model: business owner (accountable), technical owner (systems), data steward (day-to-day).
- Classify data at ingestion and propagate tags through lineage.
- Federate governance for autonomous domains rather than centralizing all decisions.
- Policy-as-code: implement classification and access rules in version-controlled configuration.

## Artifacts found

- Data Ownership Matrix
- Rule Catalog with enforcement points and failure actions
- Governance Action Plan with priorities and owners
- Decision Rights Charter
- Data classification taxonomy

## Decision rules found

- If data is a strategic asset, then establish a formal governance program with executive sponsorship.
- If multiple autonomous domains exist, then federate governance rather than centralizing all decisions.
- If sensitive data is present, then classify at ingestion and propagate tags through lineage.
- If ownership is unclear, produce an ownership matrix before proposing automation.
- If a rule exists only in a policy document and is not enforced technically, classify it as "process-dependent" and flag the risk.

## Quality gates found

- Classification coverage audit for all tier-1 data assets.
- Periodic access review and recertification cycle.
- Policy compliance scan against metadata catalog.
- Stewardship accountability check (ownership assigned and active).

## Common failure modes

- Proposing a data governance tool before ownership is defined.
- Naming a business unit as owner without naming a specific person.
- Treating a policy document as governance without enforcement.
- Defining governance for all data at once, causing scope collapse.
- Ignoring informal data caretakers who already do the work.

## Candidate skills

- `federated-governance-operating-model`
- `data-stewardship-ownership-mapping`
- `classification-taxonomy-architecture`
- `policy-as-code-design`

## Source-backed notes

- DAMA-DMBOK defines governance frameworks, stewardship models, and data quality dimensions (src-001).
- AWS Data Analytics Lens provides classification, lineage, and quality patterns (src-002).
- Microsoft Purview documents RBAC, access control, and metadata management (src-003).
- Data Mesh defines domain-oriented decentralized data ownership (src-010).
- Databricks Unity Catalog covers governance and data discovery (src-011).
- SAP MDG covers governance workflows and stewardship (src-012).

## Gaps / further research needed

- Public ADR repositories from enterprise SAP contexts are very few.
- Modern trade-off analysis templates for cloud architecture are scattered across blogs.
