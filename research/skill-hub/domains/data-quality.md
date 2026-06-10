---
title: "Domain Research: Data Quality"
robots: noindex
sitemap: false
---

# Data Quality

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from data quality validation, root cause analysis, and pipeline testing?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [DAMA-DMBOK 2nd Edition](https://dama.org/content/body-knowledge) (src-001) | 1 | Official body of knowledge for data management | Data quality dimensions, governance frameworks |
| [AWS Well-Architected Data Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/welcome.html) (src-002) | 1 | AWS official guidance for data analytics architecture | Quality patterns, classification |
| [Great Expectations Documentation](https://docs.greatexpectations.io/docs/) (src-008) | 2 | Open-source data validation framework | Expectation Suites, Checkpoints, Data Docs |
| [dbt Documentation](https://docs.getdbt.com/) (src-009) | 2 | Official dbt documentation | Tests, snapshots, documentation generation |
| [SAP Master Data Governance (MDG)](https://help.sap.com/docs/SAP_MASTER_DATA_GOVERNANCE) (src-012) | 1 | Official SAP MDG help documentation | Data quality rules, stewardship |

## Key practical patterns

- Validate data at ingestion before downstream consumption.
- Use declarative tests (Great Expectations, dbt) in version control.
- Update quality rules simultaneously when schema evolves.
- Classify root causes: missing rule, unenforced rule, wrong rule, upstream error, integration error, reference mismatch, user error without guardrail, system bug.
- Separate correction from prevention.

## Artifacts found

- Expectation Suite (JSON/YAML)
- Data quality scorecard
- Root Cause Analysis Note
- Remediation Backlog Item
- Data Quality Rule definition

## Decision rules found

- If data enters a pipeline, then validate at ingestion before downstream consumption.
- If schema evolves, then update quality rules in version control simultaneously.
- If the defect recurs, the root cause is not the symptom; trace further upstream.
- If no validation rule exists for a data element, the root cause is "missing rule."
- If a rule exists but is bypassed by a specific path, the root cause is "unenforced rule."

## Quality gates found

- Not-null and uniqueness constraints on primary keys.
- Accepted-values checks for categorical fields.
- Freshness thresholds for time-sensitive data.
- Relationship integrity between fact and dimension tables.

## Common failure modes

- Treating the symptom as the root cause.
- Mass-correcting records before fixing the source or mapping.
- Blaming "user error" without investigating why the system allowed it.
- Skipping scope assessment, turning a "small" correction into multi-system remediation.
- Proposing prevention controls that are not enforceable.

## Candidate skills

- `expectation-suite-design-and-maintenance`
- `pipeline-quality-gate-engineering`
- `data-quality-root-cause-analysis`
- `master-data-quality-assessment`

## Source-backed notes

- DAMA-DMBOK defines data quality dimensions and governance frameworks (src-001).
- Great Expectations defines Expectation Suites, Checkpoints, and Data Docs (src-008).
- dbt covers tests, snapshots, and documentation generation (src-009).
- SAP MDG covers data quality rules and stewardship (src-012).

## Gaps / further research needed

- Statistical process control and automated anomaly detection are not covered.
- Real-time streaming data quality patterns need more research.
