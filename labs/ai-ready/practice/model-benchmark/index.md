---
layout: default
title: "AI Ready Practice — Model Selection Benchmark"
description: "Compare model profiles on the same cases before choosing by reputation, size, or price."
permalink: /labs/ai-ready/practice/model-benchmark/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, practice, models, evals, benchmark]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/practice/">Practice</a></li><li aria-current="page">Model Benchmark</li></ol>
</nav>

# Model Selection Benchmark

A model name is not an architecture decision. A useful decision starts with **your cases, your quality floor, and your operating limits**.

This project uses recorded fixture outputs so it runs without API keys. The numbers are training fixtures, not claims about real models.

## What you build

```text
cases
  -> same output contract
  -> profile A
  -> profile B
  -> deterministic graders
  -> quality floor
  -> cheapest profile that passes
```

The dataset mixes classification, extraction, no-evidence behavior, routing, and permission handling.

## Run it

```bash
python3 labs/ai-ready/practice/model-benchmark/benchmark.py
python3 labs/ai-ready/practice/model-benchmark/benchmark.py --quality-floor 0.5
python3 labs/ai-ready/practice/model-benchmark/benchmark.py --self-test
```

At a high quality floor, the stronger fixture wins. Lower the floor and the cheaper fixture can become acceptable. That is the point: model choice depends on the product requirement, not a universal leaderboard.

## Experiment

Change one thing at a time:

1. add three hard cases;
2. break one output so it is invalid JSON;
3. increase the quality floor;
4. add a third profile;
5. replace fixture outputs with recorded outputs from real models.

Keep case IDs and the expected contract stable. Once real APIs are involved, record model/version, prompt version, latency, token use, and cost next to every result.

## What to learn

A fast model can be the correct production choice if it clears the release gate. A stronger model can be cheaper overall when weaker behavior creates retries, fallbacks, or human review.

Related: [Models](/labs/ai-ready/engineering/models/) · [Evals](/labs/ai-ready/evals-reliability/) · [Practice map](/labs/ai-ready/data/practice-map.json)
