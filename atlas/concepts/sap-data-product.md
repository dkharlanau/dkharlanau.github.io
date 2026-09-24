---
layout: default
title: "SAP Data Product"
description: "SAP data products explained: how SAP Business Data Cloud and SAP Datasphere package, publish, activate, share, version, and operate reusable business datasets."
tags:
  - concept
  - sap-sd
  - sap-mm
  - sap-master-data
  - sap-wm
  - sap-s4hana
  - sap-datasphere
permalink: /atlas/concepts/sap-data-product/
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

> **Status**: Needs verification.  
> **Scope**: SAP-specific data-product mechanisms, especially SAP Business Data Cloud and SAP Datasphere.

In SAP architecture discussions, **data product** can mean two related things. The first is the general architecture idea: a managed dataset with a clear purpose, semantics, ownership, quality expectations, and lifecycle. The second is a concrete product object delivered or published through SAP data platforms.

This page focuses on the second meaning and connects it back to the first. That distinction matters because a CDS view, table, extractor, API, IDoc, or replication flow is not automatically an SAP data product. Any of those artifacts can contribute to a product, but the consumer-facing boundary has to be managed as a product rather than exposed as another internal technical object.

## From an SAP application to a reusable product

SAP Business Data Cloud (BDC) currently uses data products as self-contained datasets that expose application data for consumption outside the producing application or service. SAP-managed products can originate from applications such as SAP S/4HANA Cloud and are grouped into **data packages** for activation and consumption.

That creates a useful separation of responsibilities:

| Boundary | What it answers |
|---|---|
| **Source application** | Which business data and semantics are authoritative? |
| **Data product** | Which reusable dataset is exposed outside that application? |
| **Data package** | Which related SAP-managed products are delivered together? |
| **Catalog** | How can consumers discover, understand, and request the product? |
| **Delivery target** | Where is the product installed or shared for use? |
| **Consumer model** | How is the data combined, modeled, and presented for a specific use case? |

The distinction prevents a common shortcut: treating whatever leaves SAP S/4HANA as the data product. A source interface may only be an implementation mechanism. The product is the supported dataset and its managed lifecycle as seen by consumers.

Current SAP Business Data Cloud documentation describes SAP-managed data products that can be installed in SAP Datasphere or shared with supported target services such as SAP Databricks and SAP HANA Cloud. The available targets depend on the product, landscape, and current feature scope, so the architecture should name the actual consumption path rather than assuming every product can be delivered everywhere.

## Activation is not the same as consumption

A product has to become available before a consumer can use it. In SAP Business Data Cloud, administrators activate the relevant data product or data package. The activated product can then appear in the catalog, where consumers can evaluate it and, depending on the supported scenario, install it into SAP Datasphere or share it to another target.

Those are separate stages:

**Activation** makes the managed product available in the BDC landscape.  
**Discovery** lets consumers find and understand it.  
**Installation or sharing** places an accessible representation in the target environment.  
**Modeling** turns that data into the dimensions, measures, relationships, and business views required by a use case.

This last step is easy to miss. Installing a data product into Datasphere does not mean that every analytical question is already modeled. SAP Business Data Cloud intelligent content, for example, can add SAP Datasphere preparation and analytic models and then SAP Analytics Cloud stories on top of the underlying data products. The product supplies reusable business data; the analytical experience is another layer.

That also gives us a better way to troubleshoot. If a value is wrong in a dashboard, we should identify whether the problem belongs to the source application, the product delivery pipeline, a Datasphere transformation or analytic model, or the final SAC story. “The data product is wrong” is too broad to be a useful diagnosis.

## SAP-managed products and custom products are different cases

SAP Business Data Cloud is not limited to SAP-delivered products. SAP Datasphere can also act as a provider. In a Datasphere tenant that belongs to a BDC formation, the Data Sharing Cockpit can create a custom data product for SAP Business Data Cloud on a Delta Share runtime. Once the product is listed, it is synchronized into the catalog and can be consumed through the supported installation or sharing paths.

This is a different responsibility from activating an SAP-managed package. With an SAP-managed product, SAP controls the delivered product and its lifecycle. With a custom product, the customer or provider has to decide what the product means, which tables belong together, how it should be described, and how change will be managed for consumers.

The generic [Data Product](/atlas/concepts/data-product/) page covers those design questions in more detail. The SAP platform does not remove them. A technically listable dataset can still be a poor product if its grain, semantics, ownership, or change expectations are unclear.

## Lifecycle is part of the interface

SAP Datasphere gives provider-side data products an explicit lifecycle. Current documentation includes states such as **Draft**, **Listed**, **Delisted**, and **Deactivated**. Listing makes a product discoverable to consumers; delisting removes it from new discovery while existing consumers may continue to use it; deactivation stops normal update behavior for installed consumers.

The important architectural point is not the status names themselves. It is that publication and retirement are controlled events. A shared dataset should not disappear simply because an internal table or pipeline was renamed.

SAP Business Data Cloud also exposes version history for its data products. Consumers can review current, previous, and available versions and inspect release information before updating. This supports impact analysis, but it does not remove the need to understand downstream dependencies. A technically compatible product update can still affect a calculation, filter, or semantic assumption in a consumer model.

That is where [Data Contracts](/atlas/concepts/data-contracts/) and [Data Lineage](/atlas/concepts/data-lineage/) become useful companions: the product defines the managed offering, the contract defines what consumers can rely on, and lineage shows what depends on it.

## Operate the pipeline, not only the catalog entry

A catalog entry can look healthy while data delivery is not. Current SAP Business Data Cloud monitoring separates product availability from the health of the pipeline that populates it. The Monitoring app can expose source connectivity, activation or installation progress, and high-level processing information for recent refreshes.

The support boundary is also important. SAP documents that source-data issues can require correction in the source system, while failures inside SAP-managed BDC data pipelines may require SAP Support. That is different from a customer-owned Datasphere transformation, where the customer controls the model and can change its logic directly.

For an operational investigation, a useful sequence is therefore:

1. Is the expected product activated and available?
2. Is the source system connected and supplying data?
3. Did the managed delivery or replication pipeline complete?
4. Is the product installed or shared to the expected target?
5. Did downstream transformations preserve the intended grain and semantics?
6. Is the consumer reading the correct version and model?

This sequence keeps product lifecycle, transport, and business meaning separate instead of treating them as one platform status.

## Example: an S/4HANA product used for analytics

Suppose a team needs reusable SAP S/4HANA order data for several analytical products. With a managed data-product approach, the consumer should not start by joining internal application tables independently.

The source application remains authoritative for order semantics. An SAP-provided or customer-created data product exposes a defined external dataset. After activation, the product is installed into Datasphere or shared to another supported target. The analytics team can then build a consumer model that adds the exact measures, dimensions, filters, and cross-domain relationships needed for its purpose.

If the same product is later used by planning, AI, or another analytical application, those consumers can build on the same managed source boundary without copying the original extraction logic into every project.

This does **not** make the data product the right interface for every integration. If another application needs to create or change an order, confirm a business transaction, or react immediately to an operational event, a released API, business event, message, or another transactional integration pattern may be the correct boundary. Data products are primarily about reusable data consumption, not a replacement for application integration.

## What to verify before designing around a product

SAP's data-product capabilities are moving quickly, especially across SAP Business Data Cloud, Datasphere, SAP HANA Cloud, SAP Databricks, and BDC Connect scenarios. Before using a product in a solution design, verify four things in the current documentation and tenant:

- the exact source application and product or package that is available;
- the supported target and whether the product is installed, replicated, or shared;
- the lifecycle and version-update process for that product;
- which parts of the pipeline are SAP-managed and which are customer-owned.

That check is more valuable than assuming that “SAP data product” describes one universal delivery technology.

## Related Atlas pages

- [Data Product](/atlas/concepts/data-product/)
- [Data Contracts](/atlas/concepts/data-contracts/)
- [Data Mesh for SAP Landscapes](/atlas/concepts/data-mesh-for-sap-landscapes/)
- [Data Quality Controls](/atlas/concepts/data-quality-controls/)
- [Data Lineage](/atlas/concepts/data-lineage/)
- [Semantic Layer](/atlas/concepts/semantic-layer/)
- [SAP Data Products Map](/atlas/maps/sap-data-products-map/)
- [SAP S/4HANA](/atlas/sap/sap-s4hana/)
- [SAP Datasphere](/atlas/sap/sap-datasphere/)

## Source references

- SAP Help Portal — [Working with Data Products](https://help.sap.com/docs/SAP_BUSINESS_DATA_CLOUD/f7acf8c9dad54e99b5ce5ebc633ed8e1/fcf9975b49ea4adeb837e4be16116175.html)
- SAP Help Portal — [Creating Data Products for SAP Business Data Cloud](https://help.sap.com/docs/SAP_DATASPHERE/e4059f908d16406492956e5dbcf142dc/b07e95d07a1e4569b87d9bb57b732bcf.html)
- SAP Help Portal — [Managing your Data Product's Lifecycle](https://help.sap.com/docs/SAP_DATASPHERE/e4059f908d16406492956e5dbcf142dc/c400001264094f8c89da104db72514ad.html)
- SAP Help Portal — [Viewing Data Product Version History](https://help.sap.com/docs/business-data-cloud/governing-and-publishing-data-in-catalog/viewing-version-history)
- SAP Help Portal — [Monitoring Data and Pipeline Health in SAP Business Data Cloud](https://help.sap.com/docs/business-data-cloud/administering-sap-business-data-cloud/data-monitoring)

## Verification limitations

SAP Business Data Cloud and SAP Datasphere data-product features, supported source applications, delivery targets, lifecycle behavior, and administration flows can change between releases. This page describes the current architectural boundary and avoids treating any CDS view, table, API, extractor, or catalog object as a complete data product by default.
