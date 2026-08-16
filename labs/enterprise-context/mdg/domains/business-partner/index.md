---
layout: default
title: "SAP MDG Business Partner, Customer & Supplier — Enterprise Context Lab"
description: "Deep domain engineering for shared Business Partner identity and customer/supplier organizational extensions."
permalink: /labs/enterprise-context/mdg/domains/business-partner/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, business-partner, customer, supplier, cvi]
---

# Business Partner, Customer and Supplier

A customer and a supplier can represent the same real-world party. That is why I separate **identity** from **business role** and then from **organizational behavior**.

```text
Real-world party
      ↓
Business Partner core
      ↓
Roles
 ┌────┴────┐
Customer  Supplier
  ↓          ↓
Sales Area  Purchasing Org
Company Code Company Code
```

SAP's current MDG documentation exposes separate Business Partner, Customer and Supplier data models in the Manage Business Partners scope. SAP S/4HANA also separates general BP data from company-code, sales and purchasing organization contexts. [SAP Help: BP data models](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/5fe9935ef5974d379de0d90cd94b3102.html) and [BP master data structure](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/776fbd534f22b44ce10000000a174cb4.html).

## Design rules

**Core BP data** answers “who is this party?” Names, addresses, identifiers, tax numbers, bank details and relationships can belong here depending on governance scope.

**Customer data** answers “how can we sell to this party?” The required company-code and sales-area slices must be explicit.

**Supplier data** answers “how can we buy from and pay this party?” Purchasing-organization and finance slices have different business owners.

CVI/synchronization is important technically, but it does not decide who owns a business meaning. Ownership must be defined before implementation.

## Hard cases

### The same company is customer and supplier
Do not create two enterprise identities by default. Govern one party identity and explicit roles, then control role-specific attributes.

### Address change requested by Sales
Ask whether Sales owns that address or only consumes it. Shared identity changes can affect procurement, finance, tax, credit, logistics and integrations.

### Supplier exists but PO creation is incomplete
Trace BP core → supplier role → purchasing organization → company code → target replication → procurement document. A green BP approval is not enough.

### Customer exists but delivery fails
Trace BP core → customer role → sales area → shipping/billing-relevant customer data → replicated target → sales/delivery determination.

## Lead answer

I would describe BP governance as:

```text
Party identity → Role → Organizational slice → Owner → Rule → Approval → Activation → Distribution → O2C/P2P proof
```

That explains both data model and operating model, which is more useful than reciting transactions.
