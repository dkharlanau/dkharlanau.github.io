---
layout: atlas
title: "Data Contracts"
permalink: /atlas/concepts/data-contracts/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/data-mesh-architecture-map/
  - /atlas/concepts/api-contracts/
  - /atlas/concepts/event-contracts/
  - /atlas/concepts/data-product/
  - /atlas/concepts/sap-data-product/
  - /atlas/concepts/data-mesh-for-sap-landscapes/
  - /atlas/sap/cds-views/
  - /atlas/sap/sap-datasphere/
  - /atlas/sap/sap-mdg/
---

# Data Contracts

> **Status**: Skeleton — under review.  
> **Scope**: Formal agreements between data producers and consumers in SAP landscapes.

## What it is

A data contract is a formal agreement between data producers and consumers that defines schema, semantics, quality expectations, SLAs, access policies, and versioning. It shifts data quality responsibility left to producers.

## When to use it

- Defining CDS view interfaces for cross-domain consumption
- Publishing data products from S/4HANA to Datasphere or SAC
- Establishing master data replication quality guarantees
- Migrating from ad-hoc extracts to governed data products

## When not to use it

- One-off, exploratory analytics where schema stability is not required
- Internal debugging extracts with no downstream consumers
- Legacy systems where schema changes are controlled by external vendors

## SAP landscape fit

- **CDS Views**: Schema contract defined by CDS entity; annotations add semantics
- **SAP Datasphere**: Spaces and remote tables enforce access boundaries; data flows define transformation contracts
- **SAP MDG**: Validation and derivation rules embed quality contracts in change request processing
- **ODP/CDC**: Extractor contracts define delta-enabled fields and primary key requirements

## Design decisions

| Component | SAP Implementation |
|-----------|-------------------|
| Schema | CDS entity, Datasphere table, or OpenAPI/JSON Schema |
| Semantics | CDS annotations, business glossary in Datasphere Catalog |
| Quality rules | MDG validation rules, Datasphere data quality metrics |
| SLA | Documented freshness, availability, and latency commitments |
| Access | Datasphere space permissions, SAC role-based access |
| Versioning | Semantic versioning; breaking changes require consumer notification |

## Operational failure modes

- Producer adds non-nullable field without notice → consumer ETL breaks
- Quality rule change rejects previously valid records → downstream data gaps
- SLA breach (stale data) → analytics decisions based on outdated information
- Access policy change → consumer query failures or unauthorized access errors

## Monitoring/support model

- Datasphere Impact and Lineage Analysis for downstream dependency tracking
- MDG data quality scorecards and duplicate check reports
- Data catalog for contract discoverability and ownership
- Automated CI checks for schema changes against registered consumers

## Ownership model

- **Data product owner (domain)**: owns schema, quality rules, SLA, and documentation
- **Data platform team**: owns infrastructure, catalog, and governance tooling
- **Consumer domains**: own integration testing and migration planning

## AMS incident patterns

- CDS view change breaks SAC story → check column removal or type change
- Replication lag exceeds SLA → check SLT performance, network, or source system load
- MDG duplicate check false positive → review matching rule weights and thresholds
- Data product consumer reports missing records → verify CDC delta enablement and primary key

## AI/agent opportunity

- Auto-generate data contract drafts from CDS view metadata
- Detect schema changes that break registered consumer contracts
- Predict SLA breaches from replication lag trends
- Generate data quality rule suggestions from historical error patterns

## Related Atlas pages

- [API Contracts](/atlas/concepts/api-contracts/)
- [Event Contracts](/atlas/concepts/event-contracts/)
- [Data Product](/atlas/concepts/data-product/)
- [SAP Data Product](/atlas/concepts/sap-data-product/)
- [Data Mesh for SAP Landscapes](/atlas/concepts/data-mesh-for-sap-landscapes/)
- [CDS Views](/atlas/sap/cds-views/)
- [SAP Datasphere](/atlas/sap/sap-datasphere/)
- [SAP MDG](/atlas/sap/sap-mdg/)

## Source references

- [SAP Datasphere documentation](https://help.sap.com/docs/datasphere)
- [Data Mesh Principles — Martin Fowler](https://martinfowler.com/articles/data-monolith-to-mesh.html)

## Verification limitations

- Data contract enforcement tooling in SAP landscapes is evolving.
- Content is synthesized from public SAP documentation and data mesh literature.
- No private implementation details are included.
