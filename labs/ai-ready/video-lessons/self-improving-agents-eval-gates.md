---
layout: default
title: "Can an Agent Improve Itself Without Breaking Production?"
description: "Practical AI Engineer lesson: GEPA, self-improvement, replay, holdout, approvals. Includes source limitations, SAP decisions and measurable exercises."
permalink: /labs/ai-ready/video-lessons/self-improving-agents-eval-gates/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, video-learning, architecture, sap, evaluation]
career_impact: mapped
career_skills: [ai-evaluation, delivery-cicd, ai-security]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# Can an Agent Improve Itself Without Breaking Production?

A support agent repeatedly misclassifies an integration timeout. Someone says: "Let the agent edit its own prompt until the problem disappears." That may help—or optimize the agent into a new failure mode.

In [An Agent That Fixes Its Own Mistakes](https://aietalks.com/talks/an-agent-that-fixes-its-own-mistakes), LinkedIn engineers Saloni Gandhi and Ziwei Guo describe an iterative loop that inspects agent traces, identifies causes, proposes changes with GEPA-style prompt optimization and validates candidates on held-out cases. Their production account includes **human review**, not unlimited autonomous modification.

## Self-improvement is a controlled release pipeline

~~~text
Production trace
   -> classify failure and evidence gap
   -> create or update a regression case
   -> propose one prompt / tool / workflow change
   -> run visible training tests
   -> run hidden holdout and safety tests
   -> compare to baseline
   -> human release decision
   -> monitor new version
~~~

A trace is **not automatically a correct label**. A bad user answer, a wrong system observation or an inaccurate judge can contaminate the feedback loop. Before changing prompts, decide whether the failure came from retrieval, tool authorization, incorrect mapping, stale context, model reasoning or process design.

## Where to use a model and where not to

| Step | Good tool | Why |
| --- | --- | --- |
| Capture actions | Observability/event store | Exact trace and timestamps |
| Detect hard contract violation | Code / schemas | Predictable result |
| Group messy failure descriptions | LLM or classifier | Semantic patterns |
| Suggest prompt/skill edit | Model + evidence | Generates candidate improvement |
| Verify safety and template format | Deterministic tests | Must not be negotiated |
| Evaluate nuanced explanation | Calibrated human/LLM rubric | Quality is partly subjective |
| Release changed behavior | Change control and human approval | Accountability remains explicit |

For a synthetic SAP case, the regression could say: when a message retry times out after the target has accepted it, the system must return **unknown/reconcile**, not **retry immediately**. A prompt that learns to answer those words but still invokes a second write has not fixed the problem.

## Avoid the overfitting trap

A self-improving system can see every failure in the development set and optimize specifically for them. Keep a stable **holdout** whose contents the revising agent cannot inspect; preserve adversarial examples and realistic recent production cases. Compare success, severity-weighted misses, cost, latency and number of required human corrections.

GEPA is a technique for optimizing prompts and instructions through feedback. It is not a substitute for governance of a live system, nor a reason to give the revising agent write access to its own production deployment.

## Build one useful loop in 45 minutes

Start with 20 synthetic incidents. Intentionally make one classifier confuse **missing configuration** with **failed replication**. Capture the wrong trace and its expected evidence. Ask a model to propose *one narrow change*. Run all tests, then compare previously unseen cases.

Only create a PR with the exact diff and test evidence; never auto-merge based only on the same LLM's self-assessment. Record a rollback revision.

**Architect question:** Your agent becomes 10% better on its train set, unchanged on holdout, but faster. Is that a production improvement? What business metric would confirm it?

Related: [Evidence-backed PRs](/labs/ai-ready/video-lessons/evidence-backed-ai-prs/) · [Agent Architecture](/labs/ai-ready/agent-architecture/) · [Speaker talk](https://aietalks.com/talks/an-agent-that-fixes-its-own-mistakes).

**Source boundary:** LinkedIn's system and reported improvements are speaker accounts. SAP incidents, safeguards and tests are independent recommendations.

*Editorial status: working study material, pending human review; noindex. All SAP scenarios are synthetic.*
