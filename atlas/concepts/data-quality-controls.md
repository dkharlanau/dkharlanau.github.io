---
layout: default
title: "Data Quality Controls"
permalink: /atlas/concepts/data-quality-controls/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/data-mesh-architecture-map/
  - /atlas/maps/sap-data-products-map/
  - /atlas/concepts/data-mesh-for-sap-landscapes/
  - /atlas/concepts/data-lineage/
  - /atlas/concepts/data-product/
  - /atlas/sap/sap-mdg/
  - /atlas/sap/sap-datasphere/
  - /atlas/sap/sap-s4hana/
---

# Data Quality Controls

> **Status**: Skeleton — under review.  
> **Scope**: Data quality dimensions, rules, and monitoring for SAP landscapes.

## What it is

Data quality controls enforce and monitor dimensions of data fitness for use: accuracy, completeness, consistency, timeliness, validity, and uniqueness. In SAP landscapes, they span MDG validation rules, Datasphere metrics, and operational process controls.

## When to use it

- Master data governance via SAP MDG
- Analytical data product quality commitments
- Operational process validation (e.g., three-way match, credit check)
- Compliance and audit requirements for data provenance

## When not to use it

- One-off extracts where quality is verified by consumer
- Rapid prototyping where formal quality rules are premature
- Legacy systems where quality rule configuration is prohibitively complex

## SAP landscape fit

- **SAP MDG**: Validation rules, derivation rules, duplicate checks, and workflow-based approval
- **SAP Datasphere**: Data quality metrics and scorecards for analytical data
- **SAP Data Intelligence**: Rulebooks, profiling, and metadata explorer for broader landscapes
- **S/4HANA**: Incompletion procedures, field status, and document parking for operational quality

## Quality dimensions

| Dimension | Definition | SAP Control |
|-----------|-----------|-------------|
| Accuracy | Correctness against reality | MDG validation, external reference checks |
| Completeness | Presence of required elements | Incompletion procedure, mandatory fields |
| Consistency | Absence of contradictions | Cross-field validation, matching rules |
| Timeliness | Freshness for intended use | Replication latency monitoring, delta extraction |
| Validity | Conformance to syntax/rules | Domain checks, format validation, regex |
| Uniqueness | No unexpected duplicates | MDG duplicate check, number range validation |

## Design decisions

| Decision | Recommendation |
|----------|---------------|
| Shift-left | Enforce quality at point of authorship (MDG, S/4HANA) rather than downstream cleansing |
| Automation | Automated quality scorecards with alerting for threshold breaches |
| Ownership | Domain team owns quality rules for their data products |
| Monitoring | Dashboard with trends, not just point-in-time snapshots |

## Operational failure modes

- Accuracy requires "true" reference that may not exist; hardest dimension to validate automatically
- MDG rules domain-specific; out-of-the-box rules rarely cover all requirements
- Timeliness expectations vary by use case (real-time vs monthly)
- Quality degradation often discovered by downstream consumer complaint

## Monitoring/support model

- MDG data quality scorecards and duplicate check reports
- Datasphere data quality metrics for analytical pipelines
- Automated alerting for quality threshold breaches
- Regular data quality audits with business stakeholder review

## AI/agent opportunity

- Suggest quality rules from historical error patterns
- Predict quality degradation from source system changes
- Auto-classify data quality issues by dimension and severity
- Generate remediation recommendations from quality rule violations

## Related Atlas pages

- [Data Lineage](/atlas/concepts/data-lineage/)
- [Data Mesh for SAP Landscapes](/atlas/concepts/data-mesh-for-sap-landscapes/)
- [SAP MDG](/atlas/sap/sap-mdg/)
- [SAP Datasphere](/atlas/sap/sap-datasphere/)

## Source references

- [SAP Datasphere documentation](https://help.sap.com/docs/datasphere)
- [Academic reference on data quality dimensions](https://arxiv.org/pdf/2401.12011)

## Verification limitations

- Quality rule implementation varies by domain and organizational maturity.
- Content is synthesized from public SAP documentation and academic references.
- No private implementation details are included.
