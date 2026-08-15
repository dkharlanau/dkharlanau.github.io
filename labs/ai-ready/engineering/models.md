---
layout: default
title: "AI Ready — Models"
description: "A practical guide to selecting model profiles by task, reasoning depth, latency, cost, modality, privacy, and evaluation evidence."
permalink: /labs/ai-ready/engineering/models/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, models, model-selection, latency, cost, multimodal]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/engineering/">Engineering</a></li><li aria-current="page">Models</li></ol>
</nav>

# Models

A model is a runtime dependency, not the architecture. Select it from the task and the eval results.

## Think in model profiles

Do not begin with one permanent model name. Define a profile instead:

| Profile | Good fit | Main trade-off |
|---|---|---|
| fast | classification, extraction, routing, short transformations | lower reasoning depth |
| balanced | normal assistants, summaries, RAG answers, tool selection | middle latency and cost |
| reasoning | complex planning, difficult code, multi-source analysis | slower and more expensive |
| embedding | semantic similarity and retrieval | not a text generator |
| multimodal | images, documents, audio, mixed inputs | larger input and evaluation surface |
| local/private | strong data-control or offline needs | operations and model quality may be harder |

The names are yours. The point is to separate the application need from one provider SKU.

## Selection questions

Before testing a model, write down:

1. What task does it perform?
2. What does a correct answer look like?
3. How much reasoning is actually needed?
4. What latency can the user accept?
5. What is the cost budget per request or outcome?
6. Does it need text only, or other modalities?
7. What data may be sent to this runtime?
8. Does the output need a schema or tool call?
9. What happens if the model is unavailable?

## Route by task, not ego

One application can use several profiles:

```text
incoming request
  -> cheap intent route
  -> retrieval
  -> balanced answer model
  -> reasoning model only for difficult cases
```

A larger model for every request is easy to implement. It is also an efficient way to turn uncertain architecture into certain cost.

## Compare models with the same eval set

Keep prompts, tools, retrieval, and cases stable while comparing models. Track at least:

- critical-case pass rate;
- schema pass rate;
- tool-selection accuracy;
- unsupported claims;
- latency p50/p95;
- usage or cost;
- refusal/safety behavior where relevant.

A model that wins on average but fails a critical permission or action case is not the winner.

## Fallbacks

A fallback should preserve a known reduced capability.

Examples:

- reasoning profile unavailable -> balanced profile + smaller task scope;
- multimodal unavailable -> ask for text extraction or return unsupported input;
- generation unavailable -> deterministic lookup still works;
- preferred model over budget -> route low-risk simple tasks to a cheaper profile.

Do not silently swap models when the behavior difference matters.

## Fine-tuning is a separate decision

Select a base model first. Fine-tuning can make sense for a stable behavior pattern after prompt, examples, schema, retrieval, and tools have been tested. It is not how you refresh changing knowledge.

## Decision card

**Use a stronger model when:** eval failures need deeper reasoning or a required modality.

**Use a smaller/faster model when:** it meets critical evals and improves latency or cost.

**Do not change the model when:** the real problem is stale data, weak retrieval, vague tool schemas, missing validation, or a broken workflow.

## Practice

Take 20 eval cases. Define two imaginary profiles: `fast` and `reasoning`. Mark which cases really need deeper reasoning before you run anything. This forces task decomposition before benchmark shopping.

Next: [Prompt and Context](/labs/ai-ready/engineering/prompt-context/) · [Evals and Reliability](/labs/ai-ready/evals-reliability/)
