---
layout: default
title: "Continuity of Useful Action"
description: "Maximize value creation by ensuring the system is always performing useful work instead of waiting or idling."
permalink: /datasets/view/TRIZ-bytes/TRIZ-20/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Continuity of Useful Action</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-20</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-20.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Maximize value creation by ensuring the system is always performing useful work instead of waiting or idling.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-20.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-20.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Continuity of Useful Action",
  "description": "Maximize value creation by ensuring the system is always performing useful work instead of waiting or idling.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-20/",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-20.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-20",
  "title": "Continuity of Useful Action",
  "intent": "Maximize value creation by ensuring the system is always performing useful work instead of waiting or idling.",
  "triz_principle": {
    "number": 20,
    "name": "Continuity of Useful Action",
    "definition": "Carry on work continuously so that all parts of the system are always performing useful functions."
  },
  "problem_understanding": {
    "core_contradiction": "We want efficiency, but systems spend large amounts of time waiting, blocked, or idle.",
    "why_this_hurts": "Idle time hides bottlenecks, inflates lead time, and creates the illusion of progress while value is not produced.",
    "typical_signals": [
      "waiting for approvals or dependencies",
      "queues growing while resources are idle",
      "stop-and-go processes",
      "work started but not finished"
    ]
  },
  "solution_logic": {
    "core_idea": "Redesign flow so that useful work continues even when the main path is blocked.",
    "key_rule": "Optimize for flow of value, not utilization of steps.",
    "how_it_resolves_the_contradiction": "Through parallelization, pre-work, or alternative tasks, the system keeps producing value instead of stalling."
  },
  "application_patterns": {
    "consulting": [
      "prepare decision options while approvals are pending",
      "parallelize analysis streams",
      "keep a ready backlog of value-adding tasks"
    ],
    "software_engineering": [
      "async workflows to avoid blocking",
      "background processing for non-critical tasks",
      "work stealing and dynamic task queues"
    ],
    "architecture": [
      "non-blocking I/O",
      "message-driven architectures",
      "separation of critical and non-critical paths"
    ],
    "enterprise_sap": [
      "parallel data preparation while approvals run in MDG",
      "non-blocking replication queues",
      "decoupled follow-up processes after master data changes"
    ]
  },
  "anti_patterns": [
    "busy work that does not create value",
    "parallelism that increases coordination overhead",
    "masking true bottlenecks with side activities"
  ],
  "usage_guidance": {
    "use_when": [
      "lead time is dominated by waiting",
      "teams are blocked by external dependencies",
      "system throughput is low despite high effort"
    ],
    "do_not_use_when": [
      "parallel work would cause rework or conflicts",
      "strict sequencing is required for correctness"
    ]
  },
  "diagnostic_questions": [
    "Where does work wait most of the time?",
    "What useful work could continue while waiting?",
    "Which dependencies unnecessarily block progress?"
  ],
  "example": {
    "before": "Development stops completely while waiting for final approval.",
    "after": "Non-critical improvements and preparation continue while approvals are pending."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-20.json",
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-20.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Maximize value creation by ensuring the system is always performing useful work instead of waiting or idling."
  }
}
</code></pre>

</details>
</div>
