---
layout: default
title: "SAP MDG Change Request Type Matrix — Enterprise Context Lab"
description: "How to design MDG change-request types by business purpose, scope, risk, authority, volume, activation and recovery behavior."
permalink: /labs/enterprise-context/mdg/governance-engine/change-request-matrix/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-03
last_reviewed: 2026-09-03
publication_wave: "sap-mdg-review-2026-09"
review_method: "SAP S/4HANA 2025 FPS01 change-request and workflow primary sources + authored design-matrix review"
search_intent: "SAP MDG change request type design matrix data model entity scope workflow activation error"
structured_data:
  type: TechArticle
primary_topic: "sap-mdg-change-request-design"
hide_global_cta: true
career_impact: mapped
career_skills:
  - logistics-mdg
  - logistics-master-data
  - lead-decision
tags: [sap, mdg, change-request, workflow, governance, architecture]
source_links:
  - title: "Configuration of the Change Request Process — SAP S/4HANA 2025 FPS01"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/12dcbc53d7865129e10000000a44176d.html"
  - title: "Rule-Based Workflow — SAP S/4HANA 2025 FPS01"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/1da96a56e1e8e65ae10000000a44147b.html"
  - title: "Creating a Basic Change Request Process"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/1253c4db3f52494b808d820af673fe8c.html"
# ai-discovery-managed:start
primary_topic: "sap-mdg-change-request-design"
ai_sidecar: "/ai/pages/labs--enterprise-context--mdg--governance-engine--change-request-matrix.json"
entity_mentions:
  - "sap-mdg"
semantic_links:
  - type: "parent_context"
    title: "SAP MDG Governance Engine — Enterprise Context Lab"
    url: "/labs/enterprise-context/mdg/governance-engine/"
  - type: "parent_context"
    title: "SAP Master Data Governance — Enterprise Context Lab"
    url: "/labs/enterprise-context/mdg/"
  - type: "related_topic"
    title: "Which SAP Logistics Decisions Should AI Not Own? — Decision Card"
    url: "/labs/enterprise-context/decisions/ai-logistics-boundary/"
  - type: "related_topic"
    title: "Where Should Master-Data Validation Live? — SAP Decision Card"
    url: "/labs/enterprise-context/decisions/master-data-validation/"
  - type: "related_topic"
    title: "SAP MDG Lead Assessment Drills — Enterprise Context Lab"
    url: "/labs/enterprise-context/mdg/assessment/"
  - type: "integrates_with"
    title: "IDoc, API, or Event? — SAP Integration Decision Card"
    url: "/labs/enterprise-context/decisions/idoc-api-event/"
# ai-discovery-managed:end
---
# SAP MDG Change Request Type Matrix

A change-request type is a **governance contract**. I would not create one workflow for every possible change and then hope that authorizations save the design later.

SAP S/4HANA 2025 FPS01 defines a change-request type against one MDG data model and allows it to control which entity types can be processed. The process flow can use workflow templates or rule-based workflow, depending on the configured process. The matrix below is an architecture design aid, not a list of SAP-delivered mandatory CR types. [Change Request Process](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/12dcbc53d7865129e10000000a44176d.html).

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

The risk labels and authority model above are authored governance choices. They should be adapted to the customer's control model rather than copied as SAP defaults.

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

The plant extension should not accidentally expose unrelated global identity fields only because one generic CR type is convenient.

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

SAP's current basic change-request documentation explicitly separates successful activation from rollback/error behavior after activation failure. The recovery path should therefore preserve the difference between a business decision and a technical/data activation problem. [Creating a Basic Change Request Process](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/1253c4db3f52494b808d820af673fe8c.html).

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
9. Replication timing/trigger where relevant.
10. Audit evidence and owner.

## Machine-readable model

The structured matrix is in `_data/labs/enterprise_context/topics/mdg_change_request_design_matrix.yml`.

Continue with [BRFplus rule design](/labs/enterprise-context/mdg/governance-engine/brfplus-rules/), the broader [governance engine](/labs/enterprise-context/mdg/governance-engine/) and the [Material domain](/labs/enterprise-context/mdg/domains/material/).
