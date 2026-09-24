---
layout: default
title: "Data Lineage"
description: "Data lineage shows where data comes from, how it changes, and which downstream objects depend on it across an SAP data landscape."
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
last_reviewed: 2026-09-23
related:
  - /atlas/maps/data-mesh-architecture-map/
  - /atlas/concepts/data-mesh-for-sap-landscapes/
  - /atlas/concepts/data-quality-controls/
  - /atlas/concepts/data-product/
  - /atlas/sap/sap-datasphere/
  - /atlas/sap/sap-s4hana/
---

# Data Lineage

> **Status**: Under review.  
> **Scope**: Data provenance and impact analysis for SAP landscapes.

Data lineage answers a simple question that becomes difficult in a large landscape: **where did this value come from?** It follows data from its source through transformations and models to the object that a report, API, data product, or analytical application consumes.

Impact analysis asks the opposite question: **what will be affected if we change this object?** The same dependency graph can therefore support two different jobs. Lineage looks upstream; impact analysis looks downstream.

## Why it matters in SAP work

In a small report, a consultant may still know the path from source table to output. In an S/4HANA, Datasphere, and analytics landscape, the path can cross CDS views, replicated tables, transformations, semantic models, and several consuming applications. At that point, memory and naming conventions are not enough.

We normally use lineage for three kinds of work:

- tracing a wrong analytical value back toward its source;
- checking downstream dependencies before changing a model or interface;
- documenting how important data is produced for governance, audit, or support.

Lineage is most useful when it records actual technical dependencies. A diagram that only says “S/4HANA → Datasphere → Analytics” is architecture documentation, not detailed lineage.

## SAP Datasphere: lineage and impact are different views of the same graph

SAP Datasphere provides **Impact and Lineage Analysis** for supported catalog and modeling assets. SAP defines lineage as the objects used as sources by the selected object, while impact shows objects that use the selected object as a source. The diagram can therefore help us move from a symptom toward an upstream cause, or from a planned change toward the objects that may be affected.

This does not mean that every relationship in a landscape is automatically visible. The current Datasphere documentation notes, for example, that associations are not shown in the impact and lineage diagram. Coverage also depends on which systems and assets are represented in the catalog. We should treat the diagram as evidence of known dependencies, not as proof that no other dependency exists.

A practical example is a sales analytic model with an unexpected net-value figure. We can start at the analytic asset, follow lineage into its views and source objects, and identify where the value was filtered, joined, or transformed. If we instead want to rename or remove a source field, the impact side of the graph helps identify models that depend on it before we make the change.

## Granularity changes the answer

Object-level lineage tells us that model A depends on table B. Column-level lineage tries to answer a harder question: which source fields contribute to this particular output field? The second is more useful for precise change impact, but it is also harder to capture across transformations, custom code, external tools, and older systems.

For that reason, we should not promise enterprise-wide column lineage simply because one platform offers detailed lineage inside its own scope. Cross-system lineage usually requires metadata from several products and, in some landscapes, a catalog or governance tool that can connect them.

## What good lineage needs

Useful lineage is maintained as part of the delivery process, not reconstructed only when an audit or incident starts. At minimum, we want stable object identities, source and target relationships, transformation context, ownership, and enough metadata to distinguish an active production path from an obsolete one.

The operational test is simple: if a model changes today, can we identify the important consumers before they fail? If a KPI is wrong tomorrow, can we trace the value far enough upstream to find the responsible transformation or source? If the answer is no, the lineage is not yet doing useful work.

## Related Atlas pages

- [Data Quality Controls](/atlas/concepts/data-quality-controls/)
- [Data Mesh for SAP Landscapes](/atlas/concepts/data-mesh-for-sap-landscapes/)
- [SAP Datasphere](/atlas/sap/sap-datasphere/)

## Source references

- SAP Help Portal — [Catalog Concepts: Impact and Lineage](https://help.sap.com/docs/SAP_DATASPHERE/aca3ccb4b2f84eb8b6154e8fd2812c0e/5772386034824e2ba7146fe7b3109d21.html)
- SAP Help Portal — [SAP Datasphere documentation](https://help.sap.com/docs/SAP_DATASPHERE)

## Verification limitations

Lineage coverage varies by product, connection, object type, and modeling technique. This page describes the concept and current SAP Datasphere behavior without assuming that one tool provides complete end-to-end lineage for every SAP and non-SAP system.
