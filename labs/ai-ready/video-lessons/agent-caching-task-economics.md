---
layout: default
title: "A Cheap Model Can Still Run an Expensive Agent"
description: "Practical AI Engineer lesson: prompt caching, model selection, task economics. Includes source limitations, SAP decisions and measurable exercises."
permalink: /labs/ai-ready/video-lessons/agent-caching-task-economics/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, video-learning, architecture, sap, evaluation]
career_impact: mapped
career_skills: [ai-business-value, ai-evaluation, delivery-observability]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# A Cheap Model Can Still Run an Expensive Agent

**The cost problem:** A low token price can hide repeated context, unnecessary model turns and human rework. Compare total cost per accepted task, not price per call.

A model's advertised price per million tokens is a poor answer to "How much does my agent cost?" The agent may call the model dozens of times, repeat most of its context, invoke tools, fail, retry, and need a human to check its work.

In [Without Caching, Your AI Agent Costs 10x More](https://aietalks.com/talks/without-caching-your-ai-agent-costs-10x-more), George Cameron (Artificial Analysis) discusses task-level benchmarks and prompt-cache effects. A reported benchmark task costing over $200 without effective caching versus around $21 with caching is a **particular workload observation**, not a normal multiplier for every agent.

## Count the completed job, not the individual token

For one accepted case, separate:

| Cost driver | What you must observe | How to improve |
| --- | --- | --- |
| Repeated stable prompt/context | Cache read vs regular input tokens | Keep stable tool and policy definitions in a shared prefix |
| Changing case evidence | New input tokens per step | Retrieve just relevant fields and passages |
| Model reasoning and output | Total output tokens | Put deterministic checks in code, stop when evidence suffices |
| Repeated failed attempts | Retry count and cause | Fix tool errors, add budgets and honest stop states |
| Tool and infrastructure cost | API, storage, search, sandbox, compute | Choose simpler read paths and shared infrastructure where safe |
| Human correction | Minutes per case | Improve grounding, UI and acceptance criteria |

**Working formula:** cost per accepted case = (model + tools + hosting + rework cost) / accepted cases. State the period and dataset. Do not divide by all calls if most calls did not produce an accepted business result.

## Understand the prompt-cache boundary

Many providers reuse a sufficiently stable **prefix** of a repeated prompt. Their match rules, minimum eligible size, price and expiration differ. A stable prefix helps only when the serving provider actually supports caching for your configuration.

~~~text
Stable: tool contracts + system policy + domain definitions
Variable: user request + current SAP facts + retrieved messages
  -> cache the stable part where supported
  -> validate or minimize the variable part
~~~

Avoid putting volatile timestamps or case IDs at the beginning of the stable section; this may destroy reuse. Conversely, do not cache secrets or cross-tenant data in an unsafe shared scope. The provider's isolation guarantees and data policy matter more than a cache-hit percentage.

## The failure of "choose the cheapest model"

**Synthetic SAP diagnostic benchmark:**

- Model A costs less per call but needs many retries and regularly misses one required source.
- Model B costs more per call but needs fewer steps and consistently returns an evidence-backed result.
- Model C is excellent at classification but weak at final causal explanations.

You may use A for extraction, C for a narrow routing decision and B for uncertain cross-system diagnosis. That composition is justified **only if** its measured quality, latency and end-to-end cost beat the simpler baseline. Complex routing also increases operating risk.

## A 45-minute spreadsheet exercise

Record for 20 synthetic cases: model ID, cached input tokens, uncached input, output, number of turns, tool fees, wall time, accepted/rejected outcome and minutes of human intervention. Use actual provider prices from the date of your evaluation; do not paste an old tariff into a permanent design.

Compare four configurations: original prompt, stable prefix, smaller retrieved evidence, and smaller model for exact classification. Re-run the same golden set after each change.

Publish three charts: **cost per accepted result**, **correctness by failure category**, and **P95 time to accepted result**. Reject any cost optimization that passes fewer high-severity incidents.

**Architect challenge:** A prompt-cache change reduces model spend by 60%, but cached context is accidentally reused across customers. Is it a success? Which boundary failed?

Related: [Token Economics](/labs/ai-ready/build-operate/#token-economics) · [Agent Architecture](/labs/ai-ready/agent-architecture/) · [Talk source](https://aietalks.com/talks/without-caching-your-ai-agent-costs-10x-more).

**Source boundary:** The headline cost comparison is reported by Artificial Analysis; formulas and SAP experiments are independent teaching proposals.

*Editorial status: working study material, pending human review; noindex. All SAP scenarios are synthetic.*
