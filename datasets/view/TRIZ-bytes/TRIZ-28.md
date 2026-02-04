---
layout: default
title: "Mechanics Substitution"
description: "Replace rigid, manual, or mechanical approaches with more flexible, informational, or automated ones."
permalink: /datasets/view/TRIZ-bytes/TRIZ-28/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Mechanics Substitution</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-28</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-28.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Replace rigid, manual, or mechanical approaches with more flexible, informational, or automated ones.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-28.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-28.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Mechanics Substitution",
  "description": "Replace rigid, manual, or mechanical approaches with more flexible, informational, or automated ones.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-28/",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-28.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-28",
  "title": "Mechanics Substitution",
  "intent": "Replace rigid, manual, or mechanical approaches with more flexible, informational, or automated ones.",
  "triz_principle": {
    "number": 28,
    "name": "Mechanics Substitution",
    "definition": "Replace a mechanical means with sensory, informational, or automated means."
  },
  "problem_understanding": {
    "core_contradiction": "We need control and reliability, but manual or rigid mechanisms are slow, error-prone, and hard to scale.",
    "why_this_hurts": "Human-driven or hard-coded control does not adapt well to complexity, volume, or change.",
    "typical_signals": [
      "manual approvals and checks",
      "hard-coded rules instead of configurable logic",
      "human monitoring instead of metrics",
      "operational overload as scale increases"
    ]
  },
  "solution_logic": {
    "core_idea": "Substitute manual or rigid control with information-driven or automated mechanisms.",
    "key_rule": "Automate decisions that are rule-based and observable.",
    "how_it_resolves_the_contradiction": "Control improves while speed and scalability increase through automation and information feedback."
  },
  "application_patterns": {
    "consulting": [
      "replace manual reporting with dashboards",
      "use metrics-driven governance instead of meetings",
      "automate compliance checks where possible"
    ],
    "software_engineering": [
      "policy-as-code instead of manual enforcement",
      "automated quality gates in CI/CD",
      "rule engines instead of nested conditionals"
    ],
    "architecture": [
      "event-driven monitoring instead of manual supervision",
      "automated scaling and recovery",
      "declarative configuration over imperative scripts"
    ],
    "enterprise_sap": [
      "BRF+ rules instead of custom ABAP checks",
      "automated DQ monitoring instead of manual reviews",
      "workflow conditions driven by data, not roles"
    ]
  },
  "anti_patterns": [
    "automating poorly understood processes",
    "black-box automation with no transparency",
    "automation without override or fallback"
  ],
  "usage_guidance": {
    "use_when": [
      "decisions are repetitive and rule-based",
      "volume or speed exceeds human capacity",
      "signals can be measured reliably"
    ],
    "do_not_use_when": [
      "judgment and context are critical",
      "rules are unstable or unclear"
    ]
  },
  "diagnostic_questions": [
    "Which manual steps are purely rule-based?",
    "What signals could replace human judgment here?",
    "How can automation be monitored and overridden?"
  ],
  "example": {
    "before": "Manual checks and approvals are required for every standard change.",
    "after": "Automated rules validate and approve standard changes, with humans handling exceptions only."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-28.json",
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-28.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Replace rigid, manual, or mechanical approaches with more flexible, informational, or automated ones."
  }
}
</code></pre>

</details>
</div>
