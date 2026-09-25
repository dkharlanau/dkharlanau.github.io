---
layout: default
title: "Data Product"
description: "A data product is a managed data offering built for repeated consumption, with a clear purpose, interface, semantics, ownership, quality expectations, and lifecycle."
tags:
  - concept
  - sap-master-data
  - sap-s4hana
  - sap-datasphere
  - sap-integration
  - data-quality
  - ai-operations
permalink: /atlas/concepts/data-product/
parent: Concepts
status: needs_verification
robots: noindex, follow
sitemap: false
verified: false
last_reviewed: 2026-09-24
last_modified_at: 2026-09-24
author: Dzmitryi Kharlanau
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

> **Status**: Needs verification.  
> **Scope**: Data products as stable consumer-facing data offerings in enterprise and SAP landscapes.

A data product is not simply a table with a good name. It is a **managed data offering built for repeated consumption**. Consumers should be able to discover it, understand what it represents, access it through a defined interface, judge whether it is fit for their purpose, and survive normal change without reverse-engineering the producer's implementation.

The word *product* matters because the boundary is defined from the consumer side. A source team may own hundreds of tables, views, transformations, and jobs. Consumers should not need to understand all of them. They need a smaller, stable surface with clear semantics, quality expectations, ownership, and lifecycle rules.

## The product boundary

Suppose a company wants to expose sales-order data for analytics and planning. Publishing a raw order table is not enough. A useful product needs to answer questions such as:

- What does one record represent: order, item, schedule line, or another grain?
- Which business states are included or excluded?
- Which fields are stable for consumers, and what do their values mean?
- How is the data accessed, and how fresh can it be expected to be?
- Who owns the product when the source process or interface changes?

That boundary can be implemented in different ways. One product may expose analytical tables, another a governed semantic model, and another an API or share. The transport is not the defining feature. What matters is that the consumer receives a coherent, supported data capability rather than a collection of internal artifacts.

This also separates a data product from nearby concepts:

| Concept | Main question |
|---|---|
| **Data asset** | What data object exists? |
| **Data product** | What managed data offering can consumers use for a defined purpose? |
| **Data contract** | What does the producer promise at the consumer boundary? |
| **Data lineage** | Where did the data come from, and what depends on it? |
| **Semantic layer** | How are business concepts, measures, dimensions, and relationships represented for consumption? |

A product can contain or rely on all of these, but none of them is automatically a complete data product on its own.

## What consumers need from the product

A useful data product normally brings several concerns together.

**Purpose and grain.** The product should state what business question or reuse case it supports and what one record represents. Grain is especially important in SAP data because an apparently simple object such as a sales order has header, item, schedule-line, partner, pricing, status, and document-flow dimensions.

**Interface and semantics.** Consumers need a supported access path and definitions for important fields, measures, statuses, units, currencies, and business keys. Stable naming helps, but semantic stability matters more than naming alone.

**Quality and service expectations.** The product should make relevant expectations visible: for example completeness of required attributes, expected update frequency, acceptable delay, or known limitations. Not every product needs a formal SLA, but repeated consumers need enough information to decide whether the data is fit for their task.

**Ownership and support.** Someone must be responsible for the consumer-facing boundary. That does not mean one team owns every source system or pipeline. It means consumers know who can decide what the product means, approve incompatible changes, and coordinate fixes.

**Lifecycle.** Products change. Fields are added, business rules evolve, source systems are replaced, and interfaces are retired. The product therefore needs a way to communicate releases, breaking changes, deprecation, and eventual withdrawal.

These concerns are related but should not be collapsed into one metadata form. A catalog description can improve discovery; automated tests can check schema and freshness; a contract can state explicit guarantees; lineage can reveal dependencies. Product management is the work of keeping those pieces coherent over time.

## A concrete SAP example

Consider a cross-domain product called **Sales Order Item**. SAP S/4HANA may be the operational source, while SAP Datasphere or another governed data platform exposes the consumer-facing dataset.

The product boundary could define one row as one sales-order item, identify the business key, explain net value and currency semantics, state which document categories and statuses are included, and publish an expected freshness window. It could also expose relationships to customer, material, sales organization, and delivery data without forcing consumers to reconstruct those joins from internal source tables.

Behind that boundary, the implementation may use released extraction interfaces, replicated or federated data, transformations, semantic models, and quality checks. Those are important engineering choices, but they are not the product's public definition. We should be able to replace an internal replication mechanism without forcing every consumer to redesign, provided the consumer-facing contract remains compatible.

This distinction is useful in SAP landscapes because operational structures are often optimized for transaction processing rather than broad reuse. Turning every CDS view, remote table, or API into a “data product” simply moves internal complexity into a catalog.

## How SAP uses the term today

SAP also has product-specific implementations of the data-product idea. In SAP Datasphere, data products can be managed through an explicit lifecycle. Current documentation describes states such as **Draft**, **Listed**, **Delisted**, and **Deactivated**; listing makes a product available to consumers in the Catalog & Marketplace. SAP also exposes usage information and lifecycle actions around these products.

The Catalog & Marketplace provides discovery and evaluation capabilities around data products and other governed assets. Current SAP documentation describes search, metadata, impact and lineage information, access requests, and installation or consumption flows. In SAP Business Data Cloud, SAP also exposes version history for data products so consumers can review releases and assess the impact of updates.

These are useful concrete mechanisms, but they should not redefine the architecture principle too narrowly. A data product can exist outside SAP Datasphere, and a Datasphere object is not automatically a good product merely because it can be listed. The consumer still needs a meaningful boundary, trustworthy semantics, ownership, and managed change.

## Design from the consumer backwards

The easiest way to create a weak data product is to start with an existing table and ask how to publish it. A stronger sequence starts with the repeated consumer need.

For the Sales Order Item example, first decide which reusable business view consumers actually need. Then define the grain and semantic scope, choose the authoritative source, decide which interface should be stable, and set the quality and freshness expectations that matter to the use case. Only after that should the team choose whether the serving pattern is federation, replication, an API, a shared table, or another mechanism.

The same reasoning helps avoid oversized products. A “Customer 360” product that mixes master data, transactions, interactions, profitability, credit, and marketing attributes may sound attractive but can hide several different owners, update rhythms, access rules, and meanings. Smaller products with explicit relationships are often easier to operate and change.

There is no universal rule that one domain must own exactly one product. Product boundaries should follow coherent consumer value and accountable ownership, not the organization chart alone.

## Change is where the product model becomes real

A data product is easiest to describe on the day it is launched. The harder test comes six months later when a source field changes, a consumer depends on undocumented behavior, or the old interface needs to be retired.

That is why versioning should reflect compatibility rather than ceremony. A field can keep the same technical type while its business meaning changes; that may be more dangerous than adding a new column. Conversely, an internal transformation can change substantially without requiring a consumer migration if the product boundary remains stable.

Before an incompatible change, the owner should know which consumers matter, what they depend on, whether old and new versions need to coexist, and how the migration will be communicated. Lineage and catalog metadata help with impact analysis. A data contract can make the expected compatibility rules explicit. Neither replaces ownership.

A practical test for the product model is therefore straightforward: **can a new consumer understand and use the data without reverse-engineering the producer, and can an existing consumer survive normal evolution without being surprised?** If not, the organization may have published data, but it has not yet created a dependable data product.

## Related Atlas pages

- [SAP Data Product](/atlas/concepts/sap-data-product/)
- [Data Contracts](/atlas/concepts/data-contracts/)
- [Data Mesh for SAP Landscapes](/atlas/concepts/data-mesh-for-sap-landscapes/)
- [Data Quality Controls](/atlas/concepts/data-quality-controls/)
- [Data Lineage](/atlas/concepts/data-lineage/)
- [CDS Views](/atlas/sap/cds-views/)
- [SAP Datasphere](/atlas/sap/sap-datasphere/)

## Source references

- SAP Help Portal — [Managing your Data Product's Lifecycle](https://help.sap.com/docs/SAP_DATASPHERE/e4059f908d16406492956e5dbcf142dc/c400001264094f8c89da104db72514ad.html)
- SAP Help Portal — [Governing and Publishing Data in the Catalog](https://help.sap.com/docs/SAP_DATASPHERE/aca3ccb4b2f84eb8b6154e8fd2812c0e/ca5e1d2f6c9b47578751ac65da9d895a.html)
- SAP Help Portal — [Viewing Data Product Version History](https://help.sap.com/docs/business-data-cloud/governing-and-publishing-data-in-catalog/viewing-version-history)
- Martin Fowler / Zhamak Dehghani — [Data Mesh Principles and Logical Architecture](https://martinfowler.com/articles/data-mesh-principles.html)

## Verification limitations

“Data product” is an architectural and operating-model concept as well as a term used by specific SAP products. Implementations differ by platform and organization. This page keeps the generic product boundary separate from SAP Datasphere and SAP Business Data Cloud product features, and does not treat any individual CDS view, table, API, catalog entry, or semantic model as a complete data product by default.
