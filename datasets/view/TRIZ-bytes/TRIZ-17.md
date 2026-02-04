---
layout: default
title: "Another Dimension"
description: "Unlock new solution space by moving the problem into an additional dimension instead of optimizing within the same plane."
permalink: /datasets/view/TRIZ-bytes/TRIZ-17/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Another Dimension</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-17</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-17.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Unlock new solution space by moving the problem into an additional dimension instead of optimizing within the same plane.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-17.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-17.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Another Dimension",
  "description": "Unlock new solution space by moving the problem into an additional dimension instead of optimizing within the same plane.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-17/",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-17.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-17",
  "title": "Another Dimension",
  "intent": "Unlock new solution space by moving the problem into an additional dimension instead of optimizing within the same plane.",
  "triz_principle": {
    "number": 17,
    "name": "Another Dimension",
    "definition": "Move an object or system into a new dimension, or use multi-dimensional arrangements instead of flat ones."
  },
  "problem_understanding": {
    "core_contradiction": "We keep optimizing within the same constraints, but improvements are marginal or blocked.",
    "why_this_hurts": "When all solutions live in the same dimension (time, org, data, process), trade-offs become zero-sum.",
    "typical_signals": [
      "endless prioritization conflicts",
      "performance vs quality trade-offs with no winners",
      "process tuning that yields minimal gains",
      "teams arguing because all changes compete for the same slot"
    ]
  },
  "solution_logic": {
    "core_idea": "Introduce an additional dimension to separate concerns that currently compete.",
    "key_rule": "When trade-offs are stuck, add a dimension instead of refining the plane.",
    "how_it_resolves_the_contradiction": "Previously conflicting requirements are separated across dimensions and no longer block each other."
  },
  "application_patterns": {
    "consulting": [
      "separate strategic, tactical, and operational decision timelines",
      "introduce parallel workstreams instead of sequential prioritization",
      "use scenarios instead of single forecasts"
    ],
    "software_engineering": [
      "async processing instead of synchronous flows",
      "temporal versioning instead of in-place updates",
      "multi-tenant designs instead of single shared state"
    ],
    "architecture": [
      "read/write separation (CQRS)",
      "event sourcing to add time as a dimension",
      "sidecar patterns to extend behavior without touching core"
    ],
    "enterprise_sap": [
      "time-dependent master data instead of overwriting values",
      "parallel validation paths for different risk classes",
      "simulation layers alongside productive processing"
    ]
  },
  "anti_patterns": [
    "adding dimensions without clear ownership",
    "introducing parallelism that increases confusion",
    "using new dimensions to avoid hard decisions"
  ],
  "usage_guidance": {
    "use_when": [
      "trade-offs are consistently zero-sum",
      "prioritization conflicts dominate discussions",
      "optimization within current structure is exhausted"
    ],
    "do_not_use_when": [
      "problem is simple and can be solved directly",
      "team cannot reason about added complexity"
    ]
  },
  "diagnostic_questions": [
    "What dimensions are we currently optimizing in?",
    "Which concern could be moved to a separate timeline, layer, or model?",
    "What new axis would reduce conflict instead of increasing it?"
  ],
  "example": {
    "before": "All changes compete for the same release window and approval path.",
    "after": "Low-risk changes flow continuously, while high-risk ones follow a separate, slower dimension."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-17.json",
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-17.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Unlock new solution space by moving the problem into an additional dimension instead of optimizing within the same plane."
  }
}
</code></pre>

</details>
</div>
