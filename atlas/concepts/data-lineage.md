---
layout: default
title: "Data Lineage"
description: "Data lineage tracks the flow of data from origin to destination, showing transformations, dependencies, and impacts across the data lifecycle."
tags:
  - concept
  - sap-s4hana
  - sap-datasphere
  - data-quality
  - ai-operations
  - automation
  - integration
permalink: /atlas/concepts/data-lineage/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/data-mesh-architecture-map/
  - /atlas/concepts/data-mesh-for-sap-landscapes/
  - /atlas/concepts/data-quality-controls/
  - /atlas/concepts/data-product/
  - /atlas/sap/sap-datasphere/
  - /atlas/sap/sap-s4hana/
---


# Data Lineage

> **Status**: Skeleton — under review.  
> **Scope**: Data provenance and impact analysis for SAP landscapes.

## What it is

Data lineage tracks the flow of data from origin to destination, showing transformations, dependencies, and impacts across the data lifecycle. It enables change impact analysis, debugging, and compliance.

## When to use it

- Impact analysis before changing a CDS view or extractor
- Debugging data quality issues by tracing transformations
- Compliance audits requiring provenance documentation
- Root cause analysis for analytics report discrepancies

## When not to use it

- Simple, direct table-to-report flows where manual documentation suffices
- Rapid prototyping where lineage tooling overhead exceeds value
- Legacy systems without metadata extraction capabilities

## SAP landscape fit

- **SAP Datasphere**: Built-in Impact and Lineage Analysis for tables, views, and analytic models
- **Column-level lineage**: Supported for tables, graphical/SQL views, and analytic models
- **Dependency Analysis**: Reveals associations and data access controls linked to an object
- **Third-party tools**: Collibra, Manta, OvalEdge for cross-system landscapes

## Design decisions

| Decision | Recommendation |
|----------|---------------|
| Native vs third-party | Datasphere native for SAP-centric; third-party for multi-vendor landscapes |
| Granularity | Column-level for precise impact analysis; table-level for overview |
| Automation | Extract metadata from CDS views, Datasphere models, and SAC stories |
| Documentation | Layer business meaning on top of technical lineage via catalog |

## Operational failure modes

- Datasphere lineage scoped to tenant; cross-system lineage requires manual stitching
- Column analysis gaps for data flows and transformation flows
- Legacy systems (ECC, BW) lack native lineage metadata
- Lineage decays without automated metadata extraction

## Monitoring/support model

- Regular lineage audits for critical data products
- Impact analysis before schema changes or deprecation
- Integration with data catalog for business glossary overlay
- Third-party augmentation for non-SAP sources

## AI/agent opportunity

- Auto-discover lineage from query logs and metadata
- Predict impact of schema changes from lineage graphs
- Generate compliance documentation from lineage metadata
- Detect lineage gaps and recommend manual documentation

## Related Atlas pages

- [Data Quality Controls](/atlas/concepts/data-quality-controls/)
- [Data Mesh for SAP Landscapes](/atlas/concepts/data-mesh-for-sap-landscapes/)
- [SAP Datasphere](/atlas/sap/sap-datasphere/)

## Source references

- [SAP Docs GitHub — Datasphere Lineage](https://github.com/SAP-docs/sap-datasphere/blob/main/docs/Acquiring-Preparing-Modeling-Data/impact-and-lineage-analysis-9da4892.md)
- [SAP Datasphere documentation](https://help.sap.com/docs/datasphere)

## Verification limitations

- Cross-system lineage requires manual stitching or third-party tools.
- Content is synthesized from public SAP documentation.
- No private implementation details are included.
