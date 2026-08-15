---
layout: default
title: "AI Ready Practice — Context Experiment"
description: "Measure what changes when an AI system selects useful evidence instead of sending every available document."
permalink: /labs/ai-ready/practice/context-experiment/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, practice, context, prompting, retrieval, security]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/practice/">Practice</a></li><li aria-current="page">Context Experiment</li></ol>
</nav>

# Context Experiment

More context is not automatically better context. This project compares two deliberately simple strategies:

- **all context** sends every document;
- **selected context** retrieves a small trusted subset.

The experiment measures evidence recall, evidence precision, context size, no-evidence behavior, and exposure to untrusted text.

## Run it

```bash
python3 labs/ai-ready/practice/context-experiment/context_experiment.py
python3 labs/ai-ready/practice/context-experiment/context_experiment.py --self-test
```

One document contains a prompt-injection-style instruction. The full-context strategy includes it because it includes everything. The selected strategy treats trust as an application rule and filters it before the model would see it.

## Architecture lesson

```text
available data
  -> access and trust filter
  -> retrieval
  -> context selection
  -> model
```

Prompt engineering starts before the prompt. The application decides which information earns a place in the context window.

## Experiments to try

1. increase `top_k` from 2 to 5;
2. remove the trust filter and watch the exposure metric;
3. add a long irrelevant document with many common words;
4. add a paraphrase that lexical search misses;
5. connect the next project and use hybrid retrieval for selection.

A production version should also measure answer quality. This small project isolates context selection first, because debugging five moving layers at once is a hobby humans invented despite having finite lifespans.

Related: [Prompt and Context](/labs/ai-ready/engineering/prompt-context/) · [Security](/labs/ai-ready/security-governance/)
