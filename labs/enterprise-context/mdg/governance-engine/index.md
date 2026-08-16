---
layout: default
title: "SAP MDG Governance Engine — Enterprise Context Lab"
description: "Change Request, workflow, BRFplus, validation, derivation, authority and activation as one controlled MDG process."
permalink: /labs/enterprise-context/mdg/governance-engine/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, change-request, workflow, brfplus, validation, derivation]
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

SAP's rule-based workflow uses BRFplus decision tables to determine change-request status, the next step and expected agents based on runtime inputs. [SAP Help: Rule-Based Workflow](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/14772ca8c6d743da94ebe163d80fb15d.html).

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

## Rule catalog

Every important validation or derivation should record business statement, grain, inputs, output/message, execution point, owner, severity and positive/negative tests. A BRFplus object without a business owner is only technical debt with a nicer UI.

## Workflow smell checklist

- One universal workflow for every domain change.
- Five approvals where only one person has a real decision right.
- Approver used as a manual data-quality engine.
- Derivation duplicated in UI, backend and integration mapping.
- Activation error routed as if the approver rejected the request.
- A warning used for a state that should never become active.

## Assessment example

If asked about a new rule, I explain **where the rule belongs, who owns it, what evidence proves it, and how the workflow reacts to failure**. That shows architecture rather than configuration memory.
