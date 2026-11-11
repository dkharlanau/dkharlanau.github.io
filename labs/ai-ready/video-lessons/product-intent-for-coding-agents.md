---
layout: default
title: "The Code Is Correct. Is It the Right Change?"
description: "Practical AI Engineer lesson on product intent, code agents, design history, review. Source-based insights, SAP decisions and an exercise."
permalink: /labs/ai-ready/video-lessons/product-intent-for-coding-agents/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, video-learning, architecture, sap, evaluation]
career_impact: mapped
career_skills: [lead-decision, delivery-cicd, delivery-memory]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# The Code Is Correct. Is It the Right Change?

A coding agent adds a new option to a screen. All tests pass. Yet the team removed the same option six months earlier because it confused users. The code has no way to tell the agent **why the earlier decision existed**.

Tom Moor (Linear) focuses on that gap in [What Your Coding Agent Can't See in the Code](https://aietalks.com/talks/what-your-coding-agent-cant-see-in-the-code). A change can be technically correct and still violate product intent, historical decisions or existing ownership. This is especially relevant in long-lived ERP implementations.

## Context is more than the repository

| Context source | What it tells the agent | Risk if missing |
| --- | --- | --- |
| Requirement or incident | Business pain and expected outcome | Solves the wrong problem |
| Architecture decision | Why one option was accepted | Reintroduces rejected design |
| Runbook / ownership map | Who operates and approves the behavior | No accountable owner |
| Past PR, revert or defect | Which approach failed before | Repeats a known mistake |
| Test and monitoring trace | Whether change works now | Concludes success from code alone |
| User research | What the UI must actually support | Adds confusing functionality |

The speaker describes a workflow: triage enriches a request, coding agents implement, reviewers inspect related history and team decisions, and selected lessons from comments/reverts are distilled back into instructions. Distillation is not the same as copying every old chat into a memory file.

## SAP example: a one-field change with hidden consequences

**Synthetic case:** A developer proposes automatically setting a shipping-related field whenever a customer is changed. The technical solution works in a unit test.

Before approval, the reviewer should ask:
- Was this field intentionally left under order-level control for some process variants?
- Does the change affect mass migration, UAT data or productive data?
- Are there previous defects or reversals showing why a global default was rejected?
- Who owns the rule: SD configuration, master data governance or an integration mapping?
- Is the new behavior standard, customization or landscape-specific?

A model may surface relevant past design records. It must **not** infer an undocumented business rule from one PR comment. Preserve source links and dates.

## Compact decision record

~~~yaml
decision_id: SYN-DESIGN-042
problem: Missing shipping input on a subset of orders
options:
  - global_customer_default
  - order_level_control
recommended: order_level_control
why: Multiple process variants require different values
evidence:
  - synthetic-process-matrix-v2
risk_if_changed: Existing special processes may behave differently
owner: sales-solution-lead
review_when: New process variant or proven business gap
~~~

This record is synthetic. A useful decision history holds only **current** design choices and important rejected options, with links to proof. Old rules should have expiry or supersession metadata.

## A 40-minute practice loop

Choose one real **public** PR in a project you own. Compare its description with the original issue, previous related PRs and any documented decision. Add a five-line "why this is the right change" section—not a generic AI summary.

Then give a coding agent the same task with and without the decision history. Evaluate which version respects the product boundary and which introduces unnecessary functionality. The agent's final answer is not sufficient; inspect the diff and tests.

**Lead question:** When the best code implementation conflicts with a previously approved architecture decision, who can authorize the exception? What evidence would justify reopening that decision?

Related: [Evidence-backed PRs](/labs/ai-ready/video-lessons/evidence-backed-ai-prs/) · [Decision Design](/ddd/) · [Source talk](https://aietalks.com/talks/what-your-coding-agent-cant-see-in-the-code).

**Source boundary:** Linear workflow details are drawn from the speaker's account. The SAP scenario and decision record are synthetic.

*Editorial status: working study material, pending human review; noindex. All SAP scenarios are synthetic.*
