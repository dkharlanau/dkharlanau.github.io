---
layout: default
title: "SAP MDG Domain Engineering — Enterprise Context Lab"
description: "Deep SAP MDG domain engineering for Material, Business Partner, Customer and Supplier, with governance, replication, consolidation and migration links."
permalink: /labs/enterprise-context/mdg/domains/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, material, business-partner, customer, supplier, data-model]
---

# SAP MDG Domain Engineering

MDG becomes useful when the data model matches the real business grain. A screen is not a grain. A table is not automatically a business object. The design starts with identity, organizational meaning, ownership and lifecycle.

```text
Business identity
→ Organizational grain
→ Entity / relationship
→ Ownership
→ Validation / derivation
→ Change request
→ Activation
→ Distribution
→ Business proof
```

## Domain maps

- [Material Domain](/labs/enterprise-context/mdg/domains/material/) — global product identity, plant, sales, purchasing, storage, valuation, warehouse and quality contexts.
- [Business Partner / Customer / Supplier](/labs/enterprise-context/mdg/domains/business-partner/) — shared party identity, roles and application-specific organizational slices.

## Governance mechanics

- [Change Request, Workflow & Rules](/labs/enterprise-context/mdg/governance-engine/)
- [Replication & Distribution](/labs/enterprise-context/mdg/replication/)
- [Consolidation & Golden Record](/labs/enterprise-context/mdg/consolidation/)
- [Migration & Load Strategy](/labs/enterprise-context/mdg/migration/)
- [Logistics End-to-End Cases](/labs/enterprise-context/mdg/logistics/cases/)

## Lead view

For every requirement, I want five answers before implementation starts:

1. What is the business identity and grain?
2. Who owns the value and who can approve a change?
3. Which deterministic rule validates or derives it?
4. Where does active truth live and how is it distributed?
5. Which business document proves the design works?

This keeps MDG out of the common trap where governance is designed around UI fields and the real process impact is discovered during integration testing.
