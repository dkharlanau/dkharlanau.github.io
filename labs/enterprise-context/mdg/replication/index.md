---
layout: default
title: "SAP MDG Replication & Distribution — Enterprise Context Lab"
description: "DRF, replication models, outbound implementations, filters, targets, key mapping, monitoring and reconciliation."
permalink: /labs/enterprise-context/mdg/replication/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, drf, replication, integration, key-mapping]
---

# Replication and Distribution

Activation and replication are two different proofs.

```text
Approved change
→ Active master data
→ Replication model
→ Outbound implementation
→ Filter
→ Business system
→ Message / service
→ Key mapping
→ Target persistence
→ Business consumer
```

SAP documents DRF around replication models, outbound implementations and assigned business systems. MDG replication reads **active** master data; inactive staged values are not the distribution truth. [SAP Help: Data Replication](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/ef0a1e74ff9044df9e43d28021900335.html) and [Configuring Data Replication](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/22d76454004f2357e10000000a44176d.html).

## Design contract

For every consumer define:

1. Business object and population.
2. Replication model and outbound implementation.
3. Filters and organizational scope.
4. Target business system.
5. Payload/service/message contract.
6. Identity and key mapping.
7. Target validation and persistence.
8. Monitoring, replay and reconciliation.

## Troubleshooting order

Do not begin with middleware logs. First ask whether the expected value is active.

```text
Active source?
→ selected by DRF?
→ payload correct?
→ transport delivered?
→ identity resolved?
→ target accepted?
→ target committed?
→ business process used it?
```

This isolates the first failing boundary. A successful HTTP call or outbound message is only transport evidence.

## Initialization and delta

An initial distribution creates a baseline. Ongoing changes create the delta stream. The cut-off between them needs an explicit watermark and reconciliation. Otherwise both jobs can be green while some changes fall into the gap.

## Lead-level risk list

- filter excludes a required organization;
- target requires a field not governed centrally;
- key mapping points to the wrong local object;
- retry creates duplicate side effects;
- local repair hides a central mapping defect;
- monitoring checks transport but not business acceptance.
