---
layout: default
title: "SAP MDG Business Partner Entity Map — Enterprise Context Lab"
description: "A practical map from BP technical entities to shared identity, customer and supplier roles, organizational grains and ownership."
permalink: /labs/enterprise-context/mdg/domains/business-partner/entity-map/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, business-partner, customer, supplier, entity-model]
---

# SAP MDG Business Partner Entity Map

I separate three layers:

```text
Shared party identity
→ Customer / Supplier capability
→ Organizational behavior
```

That separation is visible in the technical model too. SAP documentation uses entities such as `BP_HEADER`, `BP_CENTRL`, `BP_ADDR`, `BP_BKDTL`, `BP_IDNUM`, `BP_TAXNUM`, `BP_ROLE`, `BP_VENGEN`, `BP_CMPNY`, `BP_PORG` and `BP_SALES`.

## Core map

| Grain | Representative entity | Meaning |
|---|---|---|
| Business Partner | `BP_HEADER` | Root identity, grouping and BP category |
| Business Partner | `BP_CENTRL` | Central/general party data |
| Business Partner + Address | `BP_ADDR` | Address instances |
| Business Partner + Bank Detail | `BP_BKDTL` | Bank-detail records |
| Business Partner + Identifier | `BP_IDNUM` | External/legal identifiers |
| Business Partner + Role | `BP_ROLE` | Roles attached to the same identity |
| Supplier | `BP_VENGEN` | Supplier-general behavior |
| Supplier + Company Code | `BP_CMPNY` | Accounting and payment context |
| Supplier + Purchasing Org | `BP_PORG` | Procurement behavior |
| Customer + Sales Area | `BP_SALES` | Sales-area-dependent customer behavior |

The important point is not that these names exist. The important point is that the architecture has different grains and therefore different decision rights.

## Ownership collisions

### Sales requests an address change

A sales user may need the change, but that does not automatically make Sales the owner of a shared BP address. If the address is used by Finance, Procurement, Tax and integrations, proposal rights and approval rights should be separated.

### Supplier bank data changes

This can be a high-risk change even when the technical record looks small. I would use a narrow CR scope, stronger approval, old/new evidence and downstream payment validation.

### Same company is customer and supplier

The default design should not create two real-world identities simply because two business processes exist. Govern one party identity, then add explicit customer and supplier roles and organizational slices.

## A practical trace

For a supplier that exists but cannot be used in purchasing:

```text
BP_HEADER
→ BP_ROLE
→ BP_VENGEN
→ BP_PORG
→ BP_CMPNY where required
→ activation / CVI
→ distribution
→ purchase order proof
```

For a customer that exists but sales processing is incomplete:

```text
BP_HEADER
→ customer role
→ BP_SALES
→ company-code / other required customer slices
→ activation
→ distribution
→ sales order / delivery proof
```

## Design rule

Do not let technical synchronization decide semantic ownership. CVI can keep technical objects aligned. It cannot answer who has authority to change legal name, payment terms, sales-area shipping behavior or purchasing-organization controls.

## Machine-readable model

The structured model is in `_data/labs/enterprise_context/topics/mdg_bp_entity_reference.yml`. Use it with the broader [Business Partner domain](/labs/enterprise-context/mdg/domains/business-partner/), [change-request design](/labs/enterprise-context/mdg/governance-engine/change-request-matrix/) and [consolidation survivorship](/labs/enterprise-context/mdg/consolidation/survivorship/).
