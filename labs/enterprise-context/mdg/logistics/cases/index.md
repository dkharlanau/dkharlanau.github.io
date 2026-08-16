---
layout: default
title: "SAP MDG Logistics End-to-End Cases — Enterprise Context Lab"
description: "Assessment-ready MDG traces into Sales, Procurement, MRP, Quality and EWM."
permalink: /labs/enterprise-context/mdg/logistics/cases/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, logistics, sales, procurement, mrp, ewm, quality]
---

# MDG End-to-End Logistics Cases

The point of MDG is not a clean master-data screen. The point is predictable business execution.

```text
Business symptom
→ Required master-data grain
→ Governed value
→ Activation
→ Distribution
→ Consumer determination
→ Business document evidence
```

## Case 1: New Material for Order-to-Cash

Goal: sell and deliver an existing enterprise product in a new sales and plant context.

Trace:

```text
Material identity
→ Plant extension
→ Sales-area extension
→ valuation / units / tax context as required
→ approval
→ activation
→ replication
→ sales order
→ plant / ATP / scheduling
→ delivery
→ goods issue
```

Typical first failures: global material exists but sales area is missing; sales slice arrived but plant slice did not; target has the field but local determination interprets it differently.

## Case 2: New Supplier for Procure-to-Pay

```text
BP identity
→ Supplier role
→ Company Code
→ Purchasing Organization
→ duplicate/tax/bank checks
→ approval
→ activation
→ replication
→ purchase order
→ goods receipt
→ invoice verification
→ payment context
```

The important distinction is between shared BP identity and procurement-specific behavior.

## Case 3: Plant Extension for MRP

Do not create another Material. Extend the existing identity with the plant grain, validate planning parameters, activate and prove the planning run consumes the intended data.

## Case 4: Governed Product into EWM

Trace Material and warehouse-relevant data through replication and local identity into an inbound/outbound document, warehouse task and confirmation. A product existing in EWM is weaker evidence than a successful execution flow.

## Case 5: Quality-Relevant Material Change

Trace the changed quality-related value by plant, rule owner, approval, activation and inspection execution. Test that the change affects the intended plant and does not leak into another organizational slice.

## Lead diagnostic questions

1. Which exact grain drives the failed business decision?
2. Was the value entered, derived or mapped?
3. Who approved it?
4. Is it active?
5. Was it distributed to this consumer?
6. Did the target accept the semantic value?
7. Which document proves business use?

## Practice at Lead depth

The [MDG Lead Assessment Drills](/labs/enterprise-context/mdg/assessment/) add four larger cases: a 12-plant automotive rollout, an incomplete plant extension, duplicate-supplier consolidation and DRF recovery after a target outage.

Use the [Material entity map](/labs/enterprise-context/mdg/domains/material/entity-map/), [BP entity map](/labs/enterprise-context/mdg/domains/business-partner/entity-map/), [Change Request Type Matrix](/labs/enterprise-context/mdg/governance-engine/change-request-matrix/) and [DRF Operations & Replay](/labs/enterprise-context/mdg/replication/operations/) as evidence maps while answering them.
