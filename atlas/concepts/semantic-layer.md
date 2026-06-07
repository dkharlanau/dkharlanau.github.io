---
layout: default
title: "Semantic Layer"
permalink: /atlas/concepts/semantic-layer/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/data-mesh-architecture-map/
  - /atlas/maps/sap-data-products-map/
  - /atlas/concepts/data-mesh-for-sap-landscapes/
  - /atlas/concepts/data-product/
  - /atlas/concepts/sap-data-product/
  - /atlas/sap/sap-datasphere/
  - /atlas/sap/sap-analytics-cloud/
  - /atlas/sap/cds-views/
  - /atlas/sap/cds-analytical-views/
---

# Semantic Layer

> **Status**: Skeleton — under review.  
> **Scope**: Business-friendly data abstraction for SAP analytics.

## What it is

A semantic layer provides business-friendly abstractions over raw technical data, hiding schema complexity and exposing dimensions, measures, hierarchies, and calculations. It enables self-service analytics without requiring users to understand underlying table structures.

## When to use it

- Enabling business users to build reports without SQL knowledge
- Standardizing KPI definitions across multiple analytics tools
- Providing consistent business logic (calculated measures, time dependency) across consumers
- Migrating from direct table access to governed analytical models

## When not to use it

- Simple, single-purpose reports where direct query is sufficient
- Real-time operational dashboards where semantic layer overhead adds latency
- Scenarios requiring ad-hoc exploration of raw transactional data

## SAP landscape fit

- **SAP Datasphere Analytic Model**: Strategic "go-to analytic consumption entity" combining analytical datasets, fact models, and perspectives
- **S/4HANA Virtual Data Model (VDM)**: CDS views exposing business entities (SalesOrder, BusinessPartner) instead of raw tables
- **SAP Analytics Cloud**: Consumes Datasphere semantic models via live connections, preserving business definitions
- **BW Bridge**: Supports advanced BW semantics not yet available in pure Datasphere models

## Design decisions

| Decision | Recommendation |
|----------|---------------|
| Model type | Datasphere Analytic Model for new; BW Bridge for advanced BW semantics |
| Reusability | Design for multi-consumer use; avoid story-specific modeling |
| Time dependency | Leverage Datasphere time-dependency for slowly changing dimensions |
| Cross-space | Use linked dimensions for enterprise-wide consistency; note SAC live connection restrictions |

## Operational failure modes

- Datasphere Analytic Model does not yet support all BW semantics; some features require BW Bridge
- Field renaming in associations limited; may lead to confusing duplicate column names
- Cross-space associations restricted when consuming via SAC live connections
- Semantic layer drift: multiple teams create similar but inconsistent measures

## Monitoring/support model

- Track semantic model usage and consumer story dependencies
- Monitor query performance and source system impact
- Version semantic models with deprecation policy for breaking changes
- Business glossary integration for consistent terminology

## AI/agent opportunity

- Auto-generate semantic model suggestions from CDS view relationships
- Detect measure definition inconsistencies across models
- Recommend optimizations from query performance patterns
- Generate business glossary entries from model metadata

## Related Atlas pages

- [Data Mesh for SAP Landscapes](/atlas/concepts/data-mesh-for-sap-landscapes/)
- [Data Product](/atlas/concepts/data-product/)
- [SAP Datasphere](/atlas/sap/sap-datasphere/)
- [SAP Analytics Cloud](/atlas/sap/sap-analytics-cloud/)
- [CDS Analytical Views](/atlas/sap/cds-analytical-views/)

## Source references

- [SAP Community — Datasphere Analytic Model](https://community.sap.com/t5/technology-blog-posts-by-members/the-sap-datasphere-analytic-model/ba-p/13556451)
- [SAP Datasphere documentation](https://help.sap.com/docs/datasphere)

## Verification limitations

- Datasphere Analytic Model capabilities are evolving; verify current release features.
- Content is synthesized from public SAP documentation and community content.
- No private implementation details are included.
