---
layout: default
title: "Thermal Expansion"
description: "Exploit expansion, contraction, or elasticity effects to adapt to changing conditions without redesign."
permalink: /datasets/view/TRIZ-bytes/TRIZ-37/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Thermal Expansion</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-37</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-37.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Exploit expansion, contraction, or elasticity effects to adapt to changing conditions without redesign.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-37.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-37.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Thermal Expansion",
  "description": "Exploit expansion, contraction, or elasticity effects to adapt to changing conditions without redesign.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-37/",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-37.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-37",
  "title": "Thermal Expansion",
  "intent": "Exploit expansion, contraction, or elasticity effects to adapt to changing conditions without redesign.",
  "triz_principle": {
    "number": 37,
    "name": "Thermal Expansion",
    "definition": "Use expansion or contraction of materials or systems caused by changes in conditions."
  },
  "problem_understanding": {
    "core_contradiction": "We need stability, but demand, load, or scope fluctuates constantly.",
    "why_this_hurts": "Fixed-size solutions either waste resources when load is low or fail when load increases.",
    "typical_signals": [
      "over-provisioned systems most of the time",
      "emergency scaling under peak load",
      "rigid capacity planning cycles",
      "manual intervention to handle spikes"
    ]
  },
  "solution_logic": {
    "core_idea": "Design the system to expand and contract naturally with demand.",
    "key_rule": "Elasticity should be inherent, not an afterthought.",
    "how_it_resolves_the_contradiction": "The system adapts to real conditions, maintaining efficiency and resilience across load ranges."
  },
  "application_patterns": {
    "consulting": [
      "variable staffing models",
      "scope elasticity instead of fixed commitments",
      "budget ranges instead of single numbers"
    ],
    "software_engineering": [
      "auto-scaling services",
      "dynamic thread pools",
      "adaptive batch sizes"
    ],
    "architecture": [
      "elastic cloud infrastructure",
      "scale-out instead of scale-up designs",
      "load-based routing"
    ],
    "enterprise_sap": [
      "dynamic background job scheduling",
      "volume-based workflow routing",
      "adaptive replication throttling"
    ]
  },
  "anti_patterns": [
    "elasticity without cost controls",
    "scaling core stateful components blindly",
    "reactive scaling without signals"
  ],
  "usage_guidance": {
    "use_when": [
      "load or demand is highly variable",
      "peak handling drives design complexity",
      "manual scaling is common"
    ],
    "do_not_use_when": [
      "load is stable and predictable",
      "elasticity adds unacceptable latency"
    ]
  },
  "diagnostic_questions": [
    "Where do we overpay for idle capacity?",
    "What signals should trigger expansion or contraction?",
    "Which parts can safely scale elastically?"
  ],
  "example": {
    "before": "System capacity is fixed for peak load and underutilized most of the time.",
    "after": "Services expand during peaks and contract automatically when demand drops."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-37.json",
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-37.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Exploit expansion, contraction, or elasticity effects to adapt to changing conditions without redesign."
  }
}
</code></pre>

</details>
</div>
