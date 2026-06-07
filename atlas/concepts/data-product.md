---
layout: default
title: "Data Product"
permalink: /atlas/concepts/data-product/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/data-mesh-architecture-map/
  - /atlas/maps/sap-data-products-map/
  - /atlas/concepts/data-mesh-for-sap-landscapes/
  - /atlas/concepts/sap-data-product/
  - /atlas/concepts/data-contracts/
  - /atlas/concepts/data-quality-controls/
  - /atlas/concepts/data-lineage/
  - /atlas/sap/sap-datasphere/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/cds-views/
---

# Data Product

> **Status**: Skeleton — under review.  
> **Scope**: Data product definition, interface, and quality attributes for enterprise architecture.

## What it is

A data product is a self-contained, versioned, discoverable asset that makes explicit commitments to consumers about quality, freshness, schema stability, and availability. It shifts responsibility upstream: the domain team that generates the data owns its quality and interface.

## When to use it

- Publishing curated datasets for cross-domain consumption
- Replacing ad-hoc extracts with governed, documented interfaces
- Establishing SLAs for analytics and operational reporting
- Migrating from centralized ETL to domain-oriented data ownership

## When not to use it

- One-off, exploratory analysis with no repeat consumers
- Internal debugging or troubleshooting extracts
- Scenarios where the overhead of versioning and documentation exceeds value

## Quality attributes

| Attribute | Definition | Example |
|-----------|-----------|---------|
| Discoverable | Listed in catalog with search and metadata | Datasphere Catalog entry |
| Addressable | Stable endpoint or query interface | CDS view entity, Datasphere remote table |
| Trustworthy | Quality rules, lineage, and SLA documented | MDG validation + Datasphere metrics |
| Self-describing | Schema, semantics, and constraints documented | CDS annotations + business glossary |
| Interoperable | Standard formats and protocols | OData, SQL, Parquet |
| Natively accessible | Queryable without transformation | Live connection, API, or SQL view |
| Secure | Access controlled and audited | SAC roles, Datasphere permissions |
| Versioned | Breaking changes managed with migration path | Semantic versioning |

## SAP landscape fit

- **CDS Views**: Operational data products with built-in semantics and OData exposure
- **Datasphere Analytic Models**: Analytical data products with measures, dimensions, and hierarchies
- **SAP MDG**: Master data products with governance, validation, and distribution
- **API Business Hub**: Discoverability and specification download for API-based products

## Design decisions

| Decision | Recommendation |
|----------|---------------|
| Interface type | API (OData/REST) for operational; SQL/view for analytical |
| Schema evolution | Additive changes in minor versions; breaking changes in major versions |
| Quality metrics | Completeness, freshness, uniqueness documented and monitored |
| SLA | Availability target, max latency, freshness threshold |
| Documentation | Consumer guide with examples, constraints, and contact |

## Operational failure modes

- Schema change without notice breaks consumer pipelines
- Quality degradation undetected until downstream report is wrong
- SLA breach discovered by consumer complaint, not monitoring
- Documentation drifts out of sync with actual schema

## Monitoring/support model

- Automated quality scorecards (completeness, freshness, uniqueness)
- Consumer usage tracking and feedback collection
- Schema change detection and consumer impact analysis
- SLA dashboard with alerting for breaches

## Ownership model

- **Data product owner (domain)**: owns schema, quality, documentation, SLA, and consumer relations
- **Data platform team**: owns catalog, infrastructure, and governance tooling
- **Consumer domains**: own integration, testing, and migration planning

## AMS incident patterns

- Consumer reports missing data → verify source system availability and replication flow
- Schema change breaks downstream → check versioning policy and consumer notification
- Quality score drops → investigate source system changes or validation rule issues
- SLA breach → review infrastructure capacity and source system load

## AI/agent opportunity

- Auto-generate data product documentation from metadata
- Detect schema changes and predict consumer impact
- Recommend quality rules from historical error patterns
- Generate consumer onboarding examples from schema and sample data

## Related Atlas pages

- [SAP Data Product](/atlas/concepts/sap-data-product/)
- [Data Contracts](/atlas/concepts/data-contracts/)
- [Data Mesh for SAP Landscapes](/atlas/concepts/data-mesh-for-sap-landscapes/)
- [Data Quality Controls](/atlas/concepts/data-quality-controls/)
- [Data Lineage](/atlas/concepts/data-lineage/)
- [CDS Views](/atlas/sap/cds-views/)
- [SAP Datasphere](/atlas/sap/sap-datasphere/)

## Source references

- [Data Mesh Principles — Martin Fowler](https://martinfowler.com/articles/data-monolith-to-mesh.html)
- [SAP Datasphere documentation](https://help.sap.com/docs/datasphere)

## Verification limitations

- Data product implementation varies by organization and platform.
- Content is synthesized from public architecture literature and SAP documentation.
- No private implementation details are included.
