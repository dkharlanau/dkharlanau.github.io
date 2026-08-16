---
layout: default
title: "SAP MDG Migration & Load Strategy — Enterprise Context Lab"
description: "Migration into MDG with profiling, mapping, matching, load, reconciliation, delta control, cutover and business proof."
permalink: /labs/enterprise-context/mdg/migration/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, migration, data-load, reconciliation, cutover]
---

# Migration and Load Strategy

A load job finishing successfully is not a migration acceptance criterion. The hard problem is preserving identity, organizational completeness and business meaning.

```text
Discover
→ Profile
→ Map
→ Clean
→ Match
→ Load
→ Validate
→ Activate
→ Reconcile
→ Delta
→ Cutover
→ Operate
```

SAP MDG provides several supported data-transfer and mass/consolidation paths depending on domain and scenario, including file upload and consolidation imports. [SAP Help: File Upload](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/50f230eee73e485c8afcdff84f62b391.html), [Import Master Data - Business Partners](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/2a84422a36aa47968fcddf86e90d31bd.html), and [Mass Processing](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/18d97d57fb883925e10000000a4450e5.html).

## Migration controls

### Population
Define exactly what is in scope, including organizational slices. “100k materials” is incomplete if nobody counts required plant and sales-area extensions.

### Identity
Define source key, target key, duplicate policy, number ranges and key mapping before loading.

### Mapping
Every target field needs one of: direct map, code map, default, derivation, intentional blank or rejection rule.

### Quality
Profile nulls, invalid codes, duplicates, cross-field rules and referential integrity before the first productive rehearsal.

### Reconciliation
At minimum compare source population, target population, source-only keys, target-only keys, matched keys, rejected rows and critical control totals.

### Delta
Define watermark, timezone, overlap/gap policy, late-arrival handling and freeze. Baseline plus delta must form one continuous population.

### Business proof
Use representative migrated records in real O2C, P2P, planning, quality and warehouse scenarios.

## Cutover decision

I would not give GO because “the load is 99.8% complete”. I want to know **which 0.2%**, whether they are critical, whether identity is clean, whether delta is complete and whether core business journeys work.
