---
layout: default
title: "SAP MDG Governance Engine — Enterprise Context Lab"
description: "Change Request, workflow, BRFplus, validation, derivation, authority and activation as one controlled MDG process."
permalink: /labs/enterprise-context/mdg/governance-engine/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-03
last_reviewed: 2026-09-03
publication_wave: "sap-mdg-review-2026-09"
review_method: "SAP S/4HANA 2025 FPS01 MDG workflow, change-request, validation and derivation primary sources + page-level factual review"
search_intent: "SAP MDG change request rule based workflow BRFplus validation derivation activation governance"
structured_data:
  type: TechArticle
primary_topic: "sap-mdg-governance-engine"
hide_global_cta: true
career_impact: mapped
career_skills:
  - logistics-mdg
  - logistics-master-data
  - lead-decision
tags: [sap, mdg, change-request, workflow, brfplus, validation, derivation]
source_links:
  - title: "Rule-Based Workflow — SAP S/4HANA 2025 FPS01"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/1da96a56e1e8e65ae10000000a44147b.html"
  - title: "Validation and Derivation — SAP S/4HANA 2025 FPS01"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/8395e68123e24177982795ca05e127e9.html"
  - title: "Configuration of the Change Request Process — SAP S/4HANA 2025 FPS01"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/12dcbc53d7865129e10000000a44176d.html"
---

# Change Request, Workflow and Rules

Three mechanisms are often mixed together:

- **Validation**: is this data state allowed?
- **Derivation**: what value can be calculated from trusted inputs?
- **Workflow**: who can decide, and where does the change go next?

Keeping these contracts separate makes MDG easier to test and support.

```text
Business intent
→ Change Request Type
→ Data Scope
→ Validate / Derive
→ Workflow Step
→ Agent / Authority
→ Decision
→ Final Check
→ Activation
→ Evidence
```

SAP S/4HANA 2025 FPS01 documents the MDG rule-based workflow as a BRFplus-driven process that determines change-request status, next step and expected agents from runtime inputs. The change request type controls which data can be processed, while validation and derivation have domain-specific implementation options. [Rule-Based Workflow](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/1da96a56e1e8e65ae10000000a44147b.html), [Change Request Process](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/12dcbc53d7865129e10000000a44176d.html), and [Validation and Derivation](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/8395e68123e24177982795ca05e127e9.html).

## How I design change-request types

I split CR types when the **business purpose, scope, risk, authority or lifecycle** is materially different. Creating a Material, extending it to one plant and changing a regulated attribute are not automatically the same governance process.

A good CR type has a clear answer for:

- which data can be changed;
- which checks run before approval;
- which decisions need human authority;
- who can approve them;
- what rejection means;
- what final completeness means;
- what happens after activation failure.

The exact predefined CR types, workflow steps and rule technology available depend on the MDG domain and release. Do not copy a domain-specific workflow template as a universal MDG standard.

## Rule catalog

Every important validation or derivation should record business statement, grain, inputs, output/message, execution point, owner, severity and positive/negative tests. A BRFplus object without a business owner is only technical debt with a nicer UI.

SAP's current documentation also recommends the dedicated validation-rule and derivation-scenario capabilities where available for the domain instead of assuming direct BRFplus is always the preferred implementation. This is a useful clean-design boundary: choose the supported rule mechanism for the domain, then keep the business rule itself explicit and testable.

## Workflow smell checklist

- One universal workflow for every domain change.
- Five approvals where only one person has a real decision right.
- Approver used as a manual data-quality engine.
- Derivation duplicated in UI, backend and integration mapping.
- Activation error routed as if the approver rejected the request.
- A warning used for a state that should never become active.

## Assessment example

If asked about a new rule, I explain **where the rule belongs, who owns it, what evidence proves it, and how the workflow reacts to failure**. That shows architecture rather than configuration memory.

A Lead-level answer should also separate a business rejection from a technical activation failure. SAP's current change-request process documentation includes dedicated activation and rollback/error steps; the operating model should preserve that distinction rather than sending every failure back to an approver.

## Design deep dives

- [Change Request Type Matrix](/labs/enterprise-context/mdg/governance-engine/change-request-matrix/) — select CR patterns by purpose, entity scope, risk, authority, volume and recovery path.
- [BRFplus Rule Catalog](/labs/enterprise-context/mdg/governance-engine/brfplus-rules/) — keep workflow routing, validation, derivation, authorization and duplicate rules explicit and testable.
- [Material entity map](/labs/enterprise-context/mdg/domains/material/entity-map/) and [Business Partner entity map](/labs/enterprise-context/mdg/domains/business-partner/entity-map/) — connect process scope back to real technical entities and business grains.
- [MDG Lead Assessment Drills](/labs/enterprise-context/mdg/assessment/) — apply these contracts under rollout and incident pressure.
