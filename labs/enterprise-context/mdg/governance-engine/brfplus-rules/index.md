---
layout: default
title: "SAP MDG BRFplus Rule Catalog — Enterprise Context Lab"
description: "A practical MDG rule catalog that separates workflow routing, validation, derivation, authorization and duplicate decisions."
permalink: /labs/enterprise-context/mdg/governance-engine/brfplus-rules/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, brfplus, workflow, validation, derivation]
---

# SAP MDG BRFplus Rule Catalog

BRFplus is powerful, which is exactly why I do not put every business rule into one heroic decision table.

For MDG rule-based workflow, SAP uses BRFplus decisions to determine change-request status, the next step and expected agents. That is a workflow responsibility. Data validation and derivation have different responsibilities and should stay visible as separate rule classes.

## Five rule classes

| Rule class | Question | Typical output |
|---|---|---|
| Workflow routing | Where does the CR go next and who owns the step? | Status, next step, agent |
| Validation | Is this business state allowed? | Error, warning, pass |
| Derivation | What value can be calculated from trusted inputs? | Derived value |
| Authorization / scope | Is this actor allowed to change this grain? | Allow / deny / scope |
| Duplicate / identity | Is this probably the same real-world object? | Candidates and match decision |

The first class can be driven by BRFplus workflow decision tables. The others may use BRFplus or other MDG mechanisms, but I still catalog them separately because they answer different questions.

## Rule record

Every important rule should have a compact contract:

```text
Rule ID
Business statement
Domain + grain
Rule class
CR types
Inputs
Output / message
Execution point
Severity
Business owner
Technical owner
Source of authority
Positive test
Negative test
Monitoring signal
Change history
```

Without a business statement, a decision table quickly becomes archaeology with columns.

## Example: Material plant validation

```text
Rule: MAT-PLANT-MRP-001
Grain: Material + Plant
Intent: planning-relevant extension must be complete
Type: validation
Owner: Plant Planning
Execution: before final check / activation
Positive test: complete MRP slice
Negative test: required planning value missing
```

The approver reviews the business decision. They should not be expected to notice that a deterministic mandatory combination is impossible.

## Example: supplier bank change

```text
Change classification
→ detect sensitive bank-data scope
→ route into stronger approval path
→ preserve old/new evidence
→ final validation
→ activation
→ payment-side proof
```

Here workflow routing and data validation are connected, but they are not the same rule.

## Workflow regression pack

For every high-impact change to workflow decision logic I would test at least:

- normal approval;
- rejection;
- revision;
- no-agent / invalid-agent condition;
- parallel branch where used;
- final check;
- activation error;
- emergency path where supported.

A rule change is a production behavior change even when it is “only Customizing”.

## Anti-patterns

- One table mixes routing, validation and derivation.
- Usernames are hard-coded instead of durable responsibility.
- A warning is used for a state that must never activate.
- The same derivation is reimplemented in UI, backend and interface mapping.
- IT owns a rule only because IT configured it.

## Machine-readable model

The structured catalog is in `_data/labs/enterprise_context/topics/mdg_brfplus_rule_catalog.yml`.

Use it with the [Change Request Type Matrix](/labs/enterprise-context/mdg/governance-engine/change-request-matrix/), [governance engine](/labs/enterprise-context/mdg/governance-engine/) and [Business Partner entity map](/labs/enterprise-context/mdg/domains/business-partner/entity-map/).
