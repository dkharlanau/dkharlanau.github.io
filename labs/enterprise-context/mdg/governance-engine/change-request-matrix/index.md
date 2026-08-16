---
layout: default
title: "SAP MDG Change Request Type Matrix — Enterprise Context Lab"
description: "How to design MDG change-request types by business purpose, scope, risk, authority, volume, activation and recovery behavior."
permalink: /labs/enterprise-context/mdg/governance-engine/change-request-matrix/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, change-request, workflow, governance, architecture]
---

# SAP MDG Change Request Type Matrix

A change-request type is a **governance contract**. I would not create one workflow for every possible change and then hope that authorizations save the design later.

SAP defines a change-request type for one MDG data model and lets it restrict the entity types that can be processed. The process flow can use standard/custom workflow or rule-based workflow.

## Design matrix

| Pattern | Typical scope | Risk | Main authority |
|---|---|---:|---|
| Create new identity | Root + mandatory starting segments | High | Enterprise identity owner + domain owners |
| Organizational extension | Existing identity + one organizational grain | Medium | Owner of the target plant/sales area/purchasing org |
| Sensitive attribute change | Narrow high-impact fields | High | Named owner with explicit approval |
| Low-risk correction | Narrow low-risk fields | Low | Steward or delegated owner |
| Block / unblock / deletion | Lifecycle state | High | Business owner aware of transactional impact |
| Mass change | Many objects or grains | High | Owner of rule + population |
| Emergency correction | Minimum required scope | High | Predefined emergency authority |

## When I split CR types

I create a separate CR pattern when at least one of these changes materially:

- business purpose;
- allowed entity scope;
- decision authority;
- risk level;
- single-object versus population processing;
- validation/final-check logic;
- activation or recovery behavior.

A different screen alone is not enough reason.

## Example: Material

`Create Material` and `Extend Material to Plant` can look similar from a UI perspective, but they have different governance meaning.

```text
Create
→ new enterprise identity
→ duplicate / number controls
→ global + mandatory starting scope

Plant extension
→ existing identity
→ plant grain only
→ plant completeness
→ plant owner
→ MRP / production / procurement proof
```

The plant extension should not accidentally expose unrelated global identity fields just because one generic CR type is convenient.

## Example: BP / Supplier

A new supplier, supplier bank change and supplier block are not the same decision:

```text
New supplier      = identity + role + org completeness
Bank change       = sensitive attribute + stronger evidence
Block / unblock   = lifecycle decision + transaction impact
```

The risk and approvers differ. The workflow should show that difference instead of burying it in a long list of steps.

## Separate rejection from activation failure

This is important in interviews and in real support.

```text
Business rejection
= an authorized person decided not to accept the change

Activation failure
= the approved change could not become active truth
```

The second one needs technical/data recovery. Sending it back as if the approver changed their mind produces confusing audit history and miserable support tickets.

## CR contract checklist

For each type, define:

1. Business purpose.
2. Data model and allowed entity types.
3. Single or multi-object scope.
4. Initial status and processing actions.
5. Workflow pattern and step model.
6. Agent determination.
7. Validation points and final check.
8. Activation and activation-error handling.
9. Replication trigger.
10. Audit evidence and owner.

## Machine-readable model

The structured matrix is in `_data/labs/enterprise_context/topics/mdg_change_request_design_matrix.yml`.

Continue with [BRFplus rule design](/labs/enterprise-context/mdg/governance-engine/brfplus-rules/), the broader [governance engine](/labs/enterprise-context/mdg/governance-engine/) and the [Material entity map](/labs/enterprise-context/mdg/domains/material/entity-map/).
