---
layout: default
title: "SAP Data Products Map"
permalink: /atlas/maps/sap-data-products-map/
nav_order: 13
parent: Maps
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/concepts/sap-data-product/
  - /atlas/concepts/data-product/
  - /atlas/concepts/data-contracts/
  - /atlas/concepts/data-quality-controls/
  - /atlas/concepts/data-lineage/
  - /atlas/concepts/semantic-layer/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-datasphere/
  - /atlas/sap/sap-analytics-cloud/
  - /atlas/sap/sap-mdg/
  - /atlas/sap/cds-views/
  - /atlas/sap/cds-analytical-views/
  - /atlas/sap/odata/
  - /atlas/sap/data-quality-lineage/
---

# SAP Data Products Map

> **Status**: Skeleton — under review.  
> **Scope**: Domain-oriented data products in SAP landscapes — definitions, owners, consumers, and quality risks.

## What this map covers

This map catalogs common SAP data products, their source systems, consumers, quality risks, and integration patterns. It is designed for data architects and AMS teams managing master and transactional data.

## Core concepts

- [SAP Data Product](/atlas/concepts/sap-data-product/)
- [Data Product](/atlas/concepts/data-product/)
- [Data Contracts](/atlas/concepts/data-contracts/)
- [Data Quality Controls](/atlas/concepts/data-quality-controls/)
- [Data Lineage](/atlas/concepts/data-lineage/)
- [Semantic Layer](/atlas/concepts/semantic-layer/)

## Connected products

- [SAP S/4HANA](/atlas/sap/sap-s4hana/)
- [SAP Datasphere](/atlas/sap/sap-datasphere/)
- [SAP Analytics Cloud](/atlas/sap/sap-analytics-cloud/)
- [SAP MDG](/atlas/sap/sap-mdg/)

## Connected technologies

- [CDS Views](/atlas/sap/cds-views/)
- [CDS Analytical Views](/atlas/sap/cds-analytical-views/)
- [OData](/atlas/sap/odata/)
- [Data Quality and Lineage](/atlas/sap/data-quality-lineage/)

## SAP data product examples

| Data Product | Source System | Primary Consumers | Quality Risks | Integration Patterns |
|-------------|---------------|-------------------|---------------|---------------------|
| Customer | SAP S/4HANA, SAP MDG | CRM, Analytics, E-commerce | Duplicates, incomplete addresses | IDoc, OData, Replication |
| Supplier | SAP S/4HANA, SAP MDG | Procurement, Finance, Risk | Bank details, tax codes | IDoc, OData, Ariba |
| Material/Product | SAP S/4HANA, SAP MDG | Supply Chain, Sales, Manufacturing | Classification, units of measure | IDoc, OData, Events |
| Sales Order | SAP S/4HANA | Fulfillment, Billing, Analytics | Pricing, availability, blocks | OData, Events, CDC |
| Purchase Order | SAP S/4HANA | Procurement, Finance, EWM | Approval, incompletion | IDoc, OData, Events |
| Delivery | SAP S/4HANA, SAP EWM | Shipping, Billing, Tracking | Picking accuracy, serial numbers | IDoc, OData, Events |
| Billing Document | SAP S/4HANA | Finance, Tax, Analytics | Split rules, output control | IDoc, OData, Batch |
| Inventory Position | SAP S/4HANA, SAP EWM | Planning, Sales, Manufacturing | ATP vs physical stock | OData, CDC, Events |
| Financial Posting | SAP S/4HANA | Consolidation, Tax, Analytics | Cost object, profit center | IDoc, OData, Batch |
| Business Partner | SAP S/4HANA, SAP MDG | All domains | CVI sync, role assignment | IDoc, OData, Replication |

## Source references

- [SAP Datasphere documentation](https://help.sap.com/docs/datasphere)
- [SAP MDG documentation](https://help.sap.com/docs/sap-master-data-governance)
- [Data Mesh Principles — Martin Fowler](https://martinfowler.com/articles/data-monolith-to-mesh.html)

## Verification limitations

- Data product boundaries vary by organization; this catalog provides common patterns, not universal truth.
- Content is synthesized from public SAP documentation and architecture practice.
- No private implementation details are included.
