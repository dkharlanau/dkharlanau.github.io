---
layout: default
title: "One Consultant Gets Faster. Why Does the Team Still Work the Same?"
description: "Practical AI Engineer lesson on AI adoption, standardized process, organizational outcomes. Source-based insights, SAP decisions and an exercise."
permalink: /labs/ai-ready/video-lessons/scaling-ai-beyond-the-power-user/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, video-learning, architecture, sap, evaluation]
career_impact: mapped
career_skills: [lead-team, ai-business-value, lead-stakeholders]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# One Consultant Gets Faster. Why Does the Team Still Work the Same?

A consultant uses AI to write code and documentation much faster. The rest of the project still waits for approvals, data extracts, inaccessible systems and unclear ownership. The individual gained speed; the delivery system did not.

[Why AI Makes You 100x Faster but Not Your Company](https://aietalks.com/talks/why-ai-makes-you-100x-faster-but-not-your-company) by Mitchell Troyanovsky (Basis) argues that individual productivity gains do not scale automatically. An organization needs repeatable ways of working, quality rules and shared trust—not a collection of private prompts.

The 100x phrase is a provocative talk title, **not** an improvement to plan into a business case.

## A systems-thinking diagnosis

A project follows a chain:

~~~text
Business request -> clarification -> design -> build -> review -> transport
                 -> tests -> data -> approval -> deployment -> support
~~~

Making *build* twice as fast does little if review, data readiness and approval dominate end-to-end cycle time. The bottleneck simply moves. AI can also create **more unfinished work** if it accelerates task generation faster than the organization can validate outcomes.

This is a classic constraint problem: optimize the **flow of completed value**, not one person's keystrokes.

## Three patterns that scale better than private prompts

| Pattern | What the team gets | Minimum control |
| --- | --- | --- |
| Shared task playbook | Same definition of done for repeat work | Owner, input contract, approved output |
| Evidence-backed review | Faster acceptance, fewer repeated questions | Tests, trace and exact artifact version |
| Reusable data / automation tool | Repeatable steps across people and projects | Access scope, eval fixtures, rollback |

For an SAP transformation team, a shared **data validation workflow** may provide more value than ten private assistants that each compare customer exports differently.

## The architecture is also an operating model

The speakers' message about **opinionated agents** is that users should not have to invent the process every time. In a complex project, "opinionated" means enforcing agreed quality and escalation paths while letting experts challenge exceptions. It must not become an excuse to hide decisions from users.

A useful AI job charter defines:
- Business outcome: e.g., reduce time from defect arrival to evidence-backed triage.
- Input contract: what data is allowed, fresh and authoritative.
- Output: recommendation, evidence, uncertainties and decision owner.
- Autonomy limit: read/prepare/write.
- Measurement: cycle time, accepted resolution, rework, incidents and total cost.

## A 30-day experiment

Choose **one repeated team problem**, not five AI products. For example, preparing a diagnostic response to a failed master-data replication.

Week 1: measure current time, sources and rework. Week 2: create a shared read-only playbook with synthetic test cases. Week 3: pilot with two consultants and human review. Week 4: measure accepted results, review time and new failure modes.

Do not extrapolate from a single enthusiastic power user. Compare outcomes across people and case difficulty.

**Lead-level question:** Your manager says "everyone has ChatGPT, so SAP delivery should be 50% faster." How would you challenge the assumption respectfully, propose an experiment and agree on a business metric?

Related: [Business AI](/labs/business-ai/) · [Decision Design](/ddd/) · [Talk source](https://aietalks.com/talks/why-ai-makes-you-100x-faster-but-not-your-company).

**Source boundary:** The organizational thesis is drawn from the talk. Quantified gains are not assumed. SAP scenarios and the experiment are proposals, not reported project results.

*Editorial status: working study material, pending human review; noindex. All SAP scenarios are synthetic.*
