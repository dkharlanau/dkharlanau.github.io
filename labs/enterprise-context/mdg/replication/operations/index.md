---
layout: default
title: "SAP MDG DRF Operations & Replay — Enterprise Context Lab"
description: "How to operate MDG replication through DRF selection, payload, transport, key mapping, target acceptance, replay and reconciliation."
permalink: /labs/enterprise-context/mdg/replication/operations/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-03
last_reviewed: 2026-09-03
publication_wave: "sap-mdg-review-2026-09"
review_method: "SAP S/4HANA 2025 FPS01 DRF/key-mapping primary sources + SAP BP replication KBA evidence + operational safety review"
search_intent: "SAP MDG DRF operations replay Business Partner replication locks key mapping DRFOUT reconciliation"
structured_data:
  type: TechArticle
primary_topic: "sap-mdg-drf-operations"
hide_global_cta: true
tags: [sap, mdg, drf, replication, integration, operations]
career_impact: mapped
career_skills:
  - logistics-mdg
  - integration-recovery
source_links:
  - title: "SAP MDG Data Replication — S/4HANA 2025 FPS01"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/ef0a1e74ff9044df9e43d28021900335.html"
  - title: "SAP MDG Key Mapping — S/4HANA 2025 FPS01"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/8f3d0f8274e642b5aed793f4f4f8e5a4.html"
  - title: "SAP KBA 3730533 — System Performance Issues and Deadlocks During BP Replications"
    url: "https://userapps.support.sap.com/sap/support/knowledge/en/3730533"
  - title: "SAP KBA 3637764 — FAQ Business Partner Integration via Web Service"
    url: "https://userapps.support.sap.com/sap/support/knowledge/en/3637764"
---

# SAP MDG DRF Operations & Replay

A replication incident is not solved when the message becomes green. The useful trace is longer:

```text
Active source
→ DRF selection
→ Outbound payload
→ Transport
→ Identity mapping
→ Target validation
→ Persistence
→ Business consumer
```

SAP DRF configuration connects replication models, outbound implementations and receiving business systems. Key mapping is relevant when source and target IDs are not the same. Those are configuration facts. Operations needs an additional contract for recovery and proof.

## Error classes

| Failure | First evidence | Typical response |
|---|---|---|
| Not selected | Replication model + filter population | Correct selection logic and assess affected population |
| Payload wrong | Outbound payload / mapping trace | Correct source or mapping and rebuild from the intended source state |
| Transport failed | Correlation ID + delivery log | Restore transport and decide whether retry is safe |
| Target rejected | Target application error | Fix semantic contract; do not resend unchanged data forever |
| Key mapping failed | Source key + target key + mapping state | Repair identity mapping only after checking collisions and target existence |
| Persisted but not used | Target record + consumer trace | Continue diagnosis in the consuming process |

## Replay decision

Before replaying anything, answer six questions:

1. Is the source still in the state represented by the failed message?
2. Did the target receive or partially persist the previous attempt?
3. Is the operation duplicate-safe or idempotent?
4. Can replay overwrite a newer valid target state?
5. Does ordering matter relative to later changes?
6. Is the problem one object, one target or a population?

Then choose one of four actions:

```text
Safe replay
Rebuild from current active truth
Manual controlled resolution
Stop and reconcile population
```

Blind replay is attractive because it makes graphs go down. Unfortunately, graphs are not the business process.

## Initial load to ongoing changes

The handover between initial replication and ongoing change processing deserves its own control:

```text
Baseline population
→ source selected count
→ sent count
→ target accepted count
→ persisted count
→ key mapping coverage
→ cut-off / reconciliation point
→ first ongoing change cycle
→ no-gap proof
```

Do not assume every outbound implementation provides the same delta mechanism. The supported replication/output modes are business-object-specific.

## High-volume BP replication can create lock and capacity pressure

SAP KBA 3730533 documents S/4HANA and Private Edition incidents where large Business Partner changes combined with BP web-service replication led to occupied update work processes, `RECORD_LOCK`, `SAPLBS_SOA_INAPPSEQ_UPD`, `BSSOA_IAS_SEQ`, tRFC backlog and wider system-performance impact. This is a concrete failure pattern, not a statement that every BP mass change will behave this way.

For a planned high-volume change, treat source update and replication as one capacity-and-recovery design:

1. Estimate the changed BP and relationship population before execution.
2. Confirm whether the concrete outbound implementation uses direct, pooled, manual or scheduled processing and which options are supported.
3. Decide with the MDG/BP, Basis and integration owners whether replication should remain immediate or be controlled through an approved batch/runbook. Do not switch output behavior ad hoc in production.
4. If controlled DRFOUT processing is part of the approved design, start with a measured package size and observe update processes, locks, web-service processing and receiver throughput before increasing it.
5. Reconcile selected, sent, accepted and persisted populations before declaring the backlog complete.
6. Restore the normal operating mode only through the documented change procedure and after confirming there is no remaining population gap.

There is no useful universal package size or server-group setting. Capacity, message structure, target speed, relationship volume and current workload differ by landscape.

Typical technical clues from SAP's BP replication KBA include update processes in wait/on-hold status, `RECORD_LOCK`, `SAPLBS_SOA_INAPPSEQ_UPD`, `BSSOA_IAS_SEQ` and tRFC entries involving `MDG_BS_BP_OUTBOUND_DRF_CALL`. Use these clues to focus the investigation; do not treat the presence of one program name as proof of the root cause.

**Lead takeaway:** the risk is not “MDG cannot handle mass BP change”. The design problem is how high-volume source change, replication mode, receiver throughput, locks, update capacity and reconciliation interact.

## Operational metrics

I would monitor:

- selected objects;
- payloads built;
- target accepted and rejected;
- mapping failures;
- oldest unresolved object;
- replay volume;
- source/target reconciliation gap;
- business-consumer success after replication.

A useful alert is not only “transport failed”. Another high-value signal is “transport is green while target acceptance falls”. That catches semantic contract drift earlier.

## Runbook

```text
Freeze object + target + source version
→ prove active source
→ prove DRF selection
→ capture payload + correlation ID
→ inspect transport
→ inspect target acceptance
→ inspect key mapping
→ choose replay/rebuild/manual resolution
→ reconcile
→ prove business use
```

For BP web-service incidents, SAP's current support material also explicitly covers cases where the message monitor is green while the BP was not actually created or updated. That is exactly why the runbook ends at target and business proof rather than transport status.

## Machine-readable model

The structured operating model is in `_data/labs/enterprise_context/topics/mdg_drf_operations_control.yml`.

Use it with the main [replication architecture](/labs/enterprise-context/mdg/replication/), [MDG lineage](/labs/enterprise-context/mdg/lineage/) and [logistics cases](/labs/enterprise-context/mdg/logistics/cases/).
