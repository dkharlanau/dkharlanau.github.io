---
layout: default
title: "SAP MDG DRF Operations & Replay — Enterprise Context Lab"
description: "How to operate MDG replication through DRF selection, payload, transport, key mapping, target acceptance, replay and reconciliation."
permalink: /labs/enterprise-context/mdg/replication/operations/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, drf, replication, integration, operations]
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
| Payload wrong | Outbound payload / mapping trace | Correct source or mapping and rebuild |
| Transport failed | Correlation ID + delivery log | Restore transport and decide safe retry |
| Target rejected | Target application error | Fix semantic contract; do not resend unchanged data forever |
| Key mapping failed | Source key + target key + mapping state | Repair identity mapping and check collisions |
| Persisted but not used | Target record + consumer trace | Continue diagnosis in consuming process |

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

## Initial load to delta

The handover between initial replication and ongoing delta deserves its own control:

```text
Baseline population
→ source selected count
→ sent count
→ target accepted count
→ persisted count
→ key mapping coverage
→ cut-off watermark
→ first delta
→ no-gap proof
```

If two teams own baseline and delta without one shared cut-off, the gap becomes a small time machine where changes disappear.

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

## Machine-readable model

The structured operating model is in `_data/labs/enterprise_context/topics/mdg_drf_operations_control.yml`.

Use it with the main [replication architecture](/labs/enterprise-context/mdg/replication/), [MDG lineage](/labs/enterprise-context/mdg/lineage/) and [logistics cases](/labs/enterprise-context/mdg/logistics/cases/).
