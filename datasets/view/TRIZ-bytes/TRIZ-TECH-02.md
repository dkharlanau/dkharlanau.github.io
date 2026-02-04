---
layout: default
title: "Physical Contradiction + Separation Principles"
description: "Break a deadlock where the same parameter must be simultaneously high and low by separating requirements across conditions."
permalink: /datasets/view/TRIZ-bytes/TRIZ-TECH-02/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Physical Contradiction + Separation Principles</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_technique</span>
    <span class="pill">TRIZ-TECH-02</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-TECH-02.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Break a deadlock where the same parameter must be simultaneously high and low by separating requirements across conditions.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-02.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-02.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Physical Contradiction + Separation Principles",
  "description": "Break a deadlock where the same parameter must be simultaneously high and low by separating requirements across conditions.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-TECH-02/",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-02.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-TECH-02",
  "title": "Physical Contradiction + Separation Principles",
  "intent": "Break a deadlock where the same parameter must be simultaneously high and low by separating requirements across conditions.",
  "technique": {
    "name": "Physical Contradiction",
    "definition": "One and the same parameter must have opposite values to satisfy different requirements."
  },
  "inputs": {
    "object_or_variable": "The thing that must be both A and not-A (e.g., 'validation strictness', 'release speed').",
    "requirement_A": "Why it must be high/strong/fast/etc.",
    "requirement_not_A": "Why it must be low/weak/slow/etc."
  },
  "procedure": [
    "Convert engineering contradiction into physical form: '&lt;variable&gt; must be HIGH to achieve..., and LOW to avoid...'.",
    "Choose a separation axis:",
    "  - Separation in time: high now, low later (or vice versa).",
    "  - Separation in space: high in one area, low in another.",
    "  - Separation on condition: high only under specific triggers/risk levels.",
    "  - Separation between whole and parts: strict globally, flexible locally (or reverse).",
    "Design a mechanism that enforces the separation (rules, routing, architecture boundary, workflow branching)."
  ],
  "outputs": {
    "physical_contradiction": "&lt;variable&gt; must be HIGH and LOW.",
    "separation_strategy": "time | space | condition | whole_vs_parts",
    "solution_candidates": [
      "branching workflow by risk",
      "strict validation at boundary, flexible internally",
      "fast path + slow path"
    ]
  },
  "common_mistakes": [
    "Trying to compromise (medium value) instead of separating",
    "Choosing a separation axis but not implementing an enforcement mechanism",
    "Applying separation everywhere instead of only where the contradiction lives"
  ],
  "example": {
    "enterprise": {
      "physical_contradiction": "Master data validation must be strict (to prevent financial errors) and flexible (to avoid blocking operations).",
      "separation_on_condition": "Strict rules for high-risk attributes; relaxed rules for low-risk attributes with monitoring."
    },
    "software": {
      "physical_contradiction": "Release process must be fast and slow.",
      "separation_in_time": "Fast canary releases first; full verification and rollout later."
    }
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-TECH-02.json",
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-02.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_technique",
    "entity_subtype": "",
    "summary": "Break a deadlock where the same parameter must be simultaneously high and low by separating requirements across conditions."
  }
}
</code></pre>

</details>
</div>
