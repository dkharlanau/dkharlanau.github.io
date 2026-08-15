---
layout: default
title: "AI Ready — Engineering Practice"
description: "Runnable mini-projects for model selection, context design, retrieval, and a local assistant with controlled actions."
permalink: /labs/ai-ready/practice/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, engineering, practice, models, retrieval, agents, evals]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li aria-current="page">Engineering Practice</li></ol>
</nav>

# AI Engineering Practice

Reading architecture is useful. Changing a system and watching the result is better.

Use the same loop for every project:

```text
predict
-> run
-> inspect output and trace
-> change one constraint
-> run again
-> compare
-> write down the decision
```

The projects use synthetic data and Python standard library only. No API key or industry platform is required.

## Project 01 · Model Selection Benchmark

[Open the project](/labs/ai-ready/practice/model-benchmark/)

Compare two model profiles against the same cases and a quality floor. Learn why “best model” is incomplete without task-level evals, latency, and cost.

Build result: a repeatable selection harness.

## Project 02 · Context Experiment

[Open the project](/labs/ai-ready/practice/context-experiment/)

Compare full-context stuffing with small trust-filtered context. Measure evidence precision, recall, context size, and hostile-content exposure.

Build result: a context-selection experiment you can extend with real retrieval.

## Project 03 · Retrieval Benchmark

[Open the project](/labs/ai-ready/practice/retrieval-benchmark/)

Compare lexical, semantic-style vector, and hybrid ranking on the same relevance labels.

Build result: a retrieval benchmark where the embedding layer can later be replaced without changing the eval harness.

## Project 04 · Local Operations Assistant

[Open the project](/labs/ai-ready/practice/local-assistant/)

Join retrieval, read tools, state, a bounded workflow, a prepared write, approval, optimistic concurrency, idempotency, and traces.

Build result: a small application skeleton that remains useful when a real model is added later.

## Run everything

```bash
python3 labs/ai-ready/practice/run_all.py
```

The runner executes every project self-test. The repository CI also runs dedicated tests for the practice layer.

## Learning record

After each project, keep five notes:

1. **baseline** — what the simple version did;
2. **failure** — which case broke it;
3. **change** — what layer you added;
4. **measurement** — what improved or became worse;
5. **decision** — whether the extra complexity earned its place.

That record is more valuable than a screenshot of a chatbot answering one friendly question.

## Machine-readable map

[`practice-map.json`](/labs/ai-ready/data/practice-map.json) lists the projects, commands, inputs, controls, and expected learning outcomes.

Continue with: [Engineering Handbook](/labs/ai-ready/engineering/) · [Architecture Deep Dives](/labs/ai-ready/deep-dives/)
