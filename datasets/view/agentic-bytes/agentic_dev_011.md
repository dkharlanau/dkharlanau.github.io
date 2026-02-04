---
layout: default
title: "Golden Set &amp; Evals: How to Know Your Agent Works"
description: "Learn how to evaluate agents systematically so improvements do not break existing behavior."
permalink: /datasets/view/agentic-bytes/agentic_dev_011/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Golden Set &amp; Evals: How to Know Your Agent Works</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">agentic-bytes</span>
    <span class="pill pill--type">agentic_byte</span>
    <span class="pill">agentic_dev_011</span>
    <span class="pill">evaluation</span> <span class="pill">golden-set</span> <span class="pill">regression</span> <span class="pill">agent-quality</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/agentic-bytes/agentic_dev_011.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/agentic-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Learn how to evaluate agents systematically so improvements do not break existing behavior.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_011.json">https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_011.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Golden Set & Evals: How to Know Your Agent Works",
  "description": "Learn how to evaluate agents systematically so improvements do not break existing behavior.",
  "url": "https://dkharlanau.github.io/datasets/view/agentic-bytes/agentic_dev_011/",
  "isAccessibleForFree": true,
  "creator": {
    "@type": "Person",
    "@id": "https://dkharlanau.github.io/#dkharlanau",
    "name": "Dzmitryi Kharlanau",
    "url": "https://dkharlanau.github.io/"
  },
  "distribution": [
    {
      "@type": "DataDownload",
      "encodingFormat": "application/json",
      "contentUrl": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_011.json"
    }
  ],
  "keywords": [
    "evaluation",
    "golden-set",
    "regression",
    "agent-quality"
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "byte_id": "agentic_dev_011",
  "title": "Golden Set &amp; Evals: How to Know Your Agent Works",
  "level": "foundation",
  "domain": [
    "agentic-development",
    "evaluation",
    "quality"
  ],
  "intent": "Learn how to evaluate agents systematically so improvements do not break existing behavior.",
  "core_idea": {
    "one_liner": "If you cannot measure agent quality, you cannot improve it.",
    "why_it_matters": [
      "Agents regress silently after prompt or knowledge changes.",
      "Human impressions are inconsistent.",
      "Evaluation turns agent development into engineering."
    ]
  },
  "definition": {
    "golden_set": "A curated set of representative questions and tasks with expected outcomes used for repeatable evaluation.",
    "eval": "A process that compares agent outputs against expectations using clear criteria."
  },
  "what_a_good_golden_set_contains": [
    "Easy, medium, and hard cases",
    "Edge cases and failure scenarios",
    "Ambiguous inputs",
    "Previously broken cases (regressions)"
  ],
  "eval_dimensions": [
    {
      "dimension": "Correctness",
      "question": "Is the answer factually and logically correct?"
    },
    {
      "dimension": "Grounding",
      "question": "Are claims supported by retrieved knowledge or tools?"
    },
    {
      "dimension": "Safety",
      "question": "Did the agent respect guardrails?"
    },
    {
      "dimension": "Usefulness",
      "question": "Would a real user consider this helpful?"
    },
    {
      "dimension": "Cost &amp; latency",
      "question": "Is the quality acceptable for the time and cost?"
    }
  ],
  "eval_patterns": [
    {
      "pattern": "Offline eval",
      "description": "Run the agent against the golden set after any change."
    },
    {
      "pattern": "Regression eval",
      "description": "Ensure old correct answers stay correct."
    },
    {
      "pattern": "Shadow eval",
      "description": "Test a new version in parallel without affecting users."
    }
  ],
  "micro_example": {
    "scenario": "MDG replication troubleshooting agent",
    "golden_case": {
      "input": "Replication delayed for only one business partner type",
      "expected": "Agent asks for object-specific filters and mapping checks",
      "failure_signal": "Agent suggests generic system performance issues"
    }
  },
  "failure_modes": [
    "Golden set too small or too clean",
    "Evaluating only happy paths",
    "Changing expectations without versioning",
    "Ignoring eval failures under time pressure"
  ],
  "guards": [
    "Every agent change must run evals.",
    "Eval results must be stored and compared over time.",
    "Failing evals block release."
  ],
  "teach_it_in_english": {
    "simple_explanation": "A golden set is a test exam your agent must pass every time.",
    "one_sentence_definition": "Evals turn agent behavior into something you can trust."
  },
  "practical_checklist": [
    "Do we have representative test cases?",
    "Are failures actionable?",
    "Do evals run automatically?",
    "Can we detect regressions early?"
  ],
  "tags": [
    "evaluation",
    "golden-set",
    "regression",
    "agent-quality"
  ],
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "agentic-bytes",
    "source_project": "cv-ai",
    "source_path": "agentic-bytes/agentic_dev_011.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau (SAP Lead). Dataset bytes: https://dkharlanau.github.io"
    },
    "license": {
      "name": "",
      "spdx": "",
      "url": ""
    },
    "links": {
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "contact": {
      "preferred": "linkedin",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "canonical_url": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_011.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "agentic_byte",
    "entity_subtype": "level:foundation",
    "summary": "Learn how to evaluate agents systematically so improvements do not break existing behavior."
  }
}
</code></pre>

</details>
</div>
