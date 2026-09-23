---
layout: default
title: "Data Contracts"
description: "A data contract defines the data a producer promises to provide, what it means, how reliable it should be, and how consumers can depend on it as the interface evolves."
tags:
  - concept
  - sap-master-data
  - sap-s4hana
  - sap-datasphere
  - data-quality
  - ai-operations
  - integration
permalink: /atlas/concepts/data-contracts/
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

> **Status**: Needs verification.  
> **Scope**: Producer-consumer agreements for shared data in SAP landscapes.

A data contract is the part of a shared dataset that consumers are allowed to rely on. It describes not only the fields that exist, but also what the data represents, how it is produced, what quality and freshness consumers can expect, who owns it, and how changes are handled.

That makes a data contract different from a database schema. A schema can tell us that `SalesOrder` is a character field and `NetAmount` is numeric. It does not tell us whether one row represents an order, an item, or a daily aggregate; which currency the amount uses; whether cancelled orders are included; how late the data may arrive; or whether a field can disappear without notice.

The useful question is therefore not “do we have a YAML file?” It is: **what promise exists at the boundary between the producer and the consumers, and can both sides tell when that promise has been broken?**

## Start with the consumer-visible boundary

Contracts work best around a stable consumption boundary rather than around every internal table. In an SAP landscape, that boundary might be a released CDS view, an API, a governed Datasphere model, a published data product, or a replicated dataset exposed to several downstream consumers.

Consider an analytical sales dataset sourced from SAP S/4HANA and consumed in SAP Datasphere. A useful contract could state that one row represents one sales-order item, identify the business keys, define the meaning and currency of value fields, describe which document states are included, and set an expected freshness window. It could also state which fields are stable for consumers and which are implementation details that may change.

Without those statements, a technically successful pipeline can still deliver incorrect business meaning. The rows arrive, the types match, and the dashboard refreshes — but a change in filtering or aggregation silently changes the KPI.

## What the contract should make explicit

The exact format can vary, but six parts usually matter:

| Contract concern | What consumers need to know |
|---|---|
| **Identity and grain** | What one record represents and which fields identify it |
| **Schema** | Fields, data types, nullability, allowed values, and structural constraints |
| **Semantics** | Business definitions, units, currencies, filters, status meaning, and calculation rules |
| **Quality and service levels** | Expectations for completeness, validity, freshness, delivery frequency, or retention where these matter |
| **Ownership and access** | Who owns the data, who supports it, and which access or policy boundaries apply |
| **Lifecycle** | How changes are announced, which changes are compatible, and how consumers migrate from a breaking change |

Open standards such as the Open Data Contract Standard model many of these concerns explicitly, including schema, quality rules, service-level properties, ownership, and authoritative definitions. The standard can be useful when teams want a portable machine-readable contract. It is not a requirement for the architectural idea itself: a contract is useful only if its promises match the real data path and are maintained with it.

## How this fits SAP rather than replacing SAP objects

SAP does not need a new “data contract object” for every interface. Existing SAP artifacts can provide parts of the contract, but they should not be confused with the complete agreement.

A released CDS view or another released ABAP API can provide a stronger technical boundary than reading an internal table directly. SAP's ABAP Cloud model restricts consumers to repository objects released under defined release contracts, which is specifically intended to provide stability across upgrades. That is valuable contract evidence: the producer has deliberately exposed an interface for reuse. It still does not define every consumer-specific quality or freshness promise.

SAP Datasphere adds another layer. Its Catalog can expose technical and business metadata, glossary terms, tags, and impact/lineage information so consumers can understand and evaluate an asset before using it. Datasphere data products also have an explicit lifecycle: products move through states such as Draft, Listed, Delisted, and Deactivated. Those capabilities improve discoverability and lifecycle governance, but listing a data product does not automatically prove that its semantics, quality thresholds, or compatibility policy are complete.

SAP MDG sits at a different boundary. Validation, derivation, duplicate handling, workflow, and activation rules can improve the quality of governed master data before it leaves the source process. Those rules are important upstream controls, not a substitute for the downstream contract. A consumer may still need promises about replication scope, freshness, identifiers, field semantics, and change handling after the master data is activated.

This distinction prevents a common design mistake: treating one technical artifact as if it covered the whole producer-consumer relationship.

## Compatibility is about consumer behavior, not only field changes

Schema evolution is the most visible contract problem, but semantic changes are often more dangerous. Removing a field or changing its type is clearly risky. Adding a field is usually easier for tolerant consumers. Yet even an apparently additive change can break a consumer if, for example, a new enum value reaches code that assumes the previous set was exhaustive.

The same is true for business meaning. Keeping a field called `NetAmount` while changing its calculation, currency handling, document scope, or aggregation level preserves the schema while breaking the contract that matters to the business.

For that reason, versioning should follow actual compatibility rather than a mechanical rule such as “every additive change is minor.” Before changing a shared dataset, we need to know which consumers use the affected field or rule, whether old and new versions must coexist, and how the migration will work. Lineage and catalog metadata help with that impact analysis, but they do not replace communication with important consumers.

## Make the promises testable where possible

The strongest contracts combine human-readable meaning with checks that can run automatically. Schema existence and types can be compared in CI. Quality rules can test nulls, uniqueness, allowed ranges, or referential expectations. Freshness can be measured from timestamps or delivery events. Contract versions can be compared before a deployment reaches consumers.

Automation has a boundary, though. A test can confirm that `Currency` is populated; it cannot prove that every consumer interprets a business amount correctly. It can detect that a column disappeared; it may not detect that a filter changed the population behind the same column set.

A practical contract therefore has two layers: **machine-checkable guarantees for what software can verify, and precise business definitions for what still requires human agreement**. Keeping those layers together is what turns a schema into a dependable data interface.

## Related Atlas pages

- [API Contracts](/atlas/concepts/api-contracts/)
- [Event Contracts](/atlas/concepts/event-contracts/)
- [Data Product](/atlas/concepts/data-product/)
- [SAP Data Product](/atlas/concepts/sap-data-product/)
- [Data Quality Controls](/atlas/concepts/data-quality-controls/)
- [Data Lineage](/atlas/concepts/data-lineage/)
- [SAP Datasphere](/atlas/sap/sap-datasphere/)

## Source references

- SAP Help Portal — [Cloud-Optimized ABAP Language and released APIs](https://help.sap.com/docs/abap-cloud/abap-cloud/abap-language)
- SAP Help Portal — [Governing and Publishing Data in the SAP Datasphere Catalog](https://help.sap.com/docs/SAP_DATASPHERE/aca3ccb4b2f84eb8b6154e8fd2812c0e/ca5e1d2f6c9b47578751ac65da9d895a.html)
- SAP Help Portal — [Managing your Data Product's Lifecycle](https://help.sap.com/docs/SAP_DATASPHERE/e4059f908d16406492956e5dbcf142dc/c400001264094f8c89da104db72514ad.html)
- Linux Foundation AI & Data / Bitol — [Open Data Contract Standard](https://bitol-io.github.io/open-data-contract-standard/)

## Verification limitations

Data-contract implementation is an architecture and governance choice, not one universal SAP feature. The exact enforcement model depends on the interface, product release, data platform, and tooling used in a landscape. This page keeps that distinction explicit and does not assume that a catalog entry, CDS view, MDG rule, or data product is a complete contract by itself.
