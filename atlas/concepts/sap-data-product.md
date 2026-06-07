---
layout: atlas
title: "SAP Data Product"
permalink: /atlas/concepts/sap-data-product/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/data-mesh-architecture-map/
  - /atlas/maps/sap-data-products-map/
  - /atlas/concepts/data-mesh-for-sap-landscapes/
  - /atlas/concepts/data-product/
  - /atlas/concepts/data-contracts/
  - /atlas/concepts/data-quality-controls/
  - /atlas/concepts/data-lineage/
  - /atlas/concepts/semantic-layer/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-datasphere/
  - /atlas/sap/sap-mdg/
---

# SAP Data Product

> **Status**: Skeleton — under review.  
> **Scope**: Domain-oriented data products in SAP landscapes with owner, source, consumers, and quality risks.

## What it is

An SAP data product is a curated, governed, and versioned data asset derived from SAP systems (primarily S/4HANA) and exposed for cross-domain consumption. It includes schema, semantics, quality commitments, and ownership.

## SAP data product examples

| Data Product | Owner | Source System | Primary Consumers | Quality Risks | Integration Patterns |
|-------------|-------|---------------|-------------------|---------------|---------------------|
| **Customer** | Sales/CRM domain | SAP S/4HANA, SAP MDG | CRM, Analytics, E-commerce, Marketing | Duplicates, incomplete addresses, CVI sync errors | IDoc, OData, Replication |
| **Supplier** | Procurement domain | SAP S/4HANA, SAP MDG | Procurement, Finance, Risk, Ariba | Bank details, tax codes, duplicate vendors | IDoc, OData, Ariba Network, Events |
| **Material/Product** | Supply Chain domain | SAP S/4HANA, SAP MDG | Supply Chain, Sales, Manufacturing, E-commerce | Classification, units of measure, translation | IDoc, OData, Events, CDC |
| **Sales Order** | Sales domain | SAP S/4HANA | Fulfillment, Billing, Analytics, WMS | Pricing, availability, delivery blocks, incompletion | OData, Events, CDC |
| **Purchase Order** | Procurement domain | SAP S/4HANA | Procurement, Finance, EWM, GR/IR | Approval, incompletion, release strategy | IDoc, OData, Events |
| **Delivery** | Logistics domain | SAP S/4HANA, SAP EWM | Shipping, Billing, Tracking, WMS | Picking accuracy, serial numbers, batch management | IDoc, OData, Events |
| **Billing Document** | Finance domain | SAP S/4HANA | Finance, Tax, Analytics, Output Control | Split rules, output control, pricing | IDoc, OData, Batch |
| **Inventory Position** | Supply Chain domain | SAP S/4HANA, SAP EWM | Planning, Sales, Manufacturing, Analytics | ATP vs physical stock, reservations, in transit | OData, CDC, Events |
| **Financial Posting** | Finance domain | SAP S/4HANA | Consolidation, Tax, Analytics, Treasury | Cost object, profit center, segment | IDoc, OData, Batch |
| **Business Partner** | Master Data domain | SAP S/4HANA, SAP MDG | All domains | CVI sync, role assignment, duplicate check | IDoc, OData, Replication, Events |

## Design decisions

| Decision | Recommendation |
|----------|---------------|
| Source interface | CDS views with `@Analytics.dataExtraction.enabled` for extraction; OData for API |
| Quality enforcement | MDG validation rules for master data; Datasphere metrics for analytical |
| Consumption | Datasphere remote tables (federation) or replication flows (replication) |
| Analytics | SAC stories and planning models consuming Datasphere semantic models |
| Governance | Domain owner approves schema changes; central team owns catalog and platform |

## Operational failure modes

- Master data duplicate check false positive → blocked business process
- CDS view change removes field used by consumer → downstream pipeline failure
- Replication lag exceeds SLA → analytics based on stale data
- CVI synchronization error → customer/vendor mismatch between BP and customer master

## Monitoring/support model

- Datasphere Impact and Lineage Analysis for downstream dependency tracking
- MDG data quality scorecards and duplicate check reports
- Replication flow monitoring for latency and row counts
- SAC story validation for field existence and data freshness

## Ownership model

- **Domain owner**: owns data product definition, quality rules, and consumer relations
- **Master data team**: owns MDG configuration, validation rules, and consolidation
- **Data platform team**: owns Datasphere infrastructure, replication, and catalog
- **Consumer teams**: own integration testing and usage compliance

## AMS incident patterns

- Customer master not replicated to CRM → check IDoc status, partner profile, or BP relationship
- Sales order pricing incorrect in analytics → verify condition technique and pricing procedure
- Inventory position mismatch between S/4HANA and WMS → check movement types and goods receipt
- Financial posting missing in consolidation → verify posting period, cost object, and extractor delta

## AI/agent opportunity

- Auto-generate data product specifications from CDS view metadata
- Predict quality risks from historical error patterns and source system changes
- Detect downstream consumer impact from proposed schema changes
- Generate root cause analysis for replication lag from system metrics

## Related Atlas pages

- [Data Product](/atlas/concepts/data-product/)
- [Data Contracts](/atlas/concepts/data-contracts/)
- [Data Mesh for SAP Landscapes](/atlas/concepts/data-mesh-for-sap-landscapes/)
- [Data Quality Controls](/atlas/concepts/data-quality-controls/)
- [Data Lineage](/atlas/concepts/data-lineage/)
- [SAP Data Products Map](/atlas/maps/sap-data-products-map/)
- [SAP S/4HANA](/atlas/sap/sap-s4hana/)
- [SAP MDG](/atlas/sap/sap-mdg/)
- [SAP Datasphere](/atlas/sap/sap-datasphere/)

## Source references

- [SAP Datasphere documentation](https://help.sap.com/docs/datasphere)
- [SAP MDG documentation](https://help.sap.com/docs/sap-master-data-governance)
- [SAP Community — Datasphere Best Practices](https://community.sap.com/t5/technology-blog-posts-by-sap/sap-datasphere-space-data-integration-and-data-modeling-best-practices/ba-p/13651889)

## Verification limitations

- Data product boundaries vary by organization; this catalog provides common patterns.
- Content is synthesized from public SAP documentation and architecture practice.
- No private implementation details are included.
