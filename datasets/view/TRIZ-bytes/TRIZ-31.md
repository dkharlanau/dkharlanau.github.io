---
layout: default
title: "Porous Materials"
description: "Increase adaptability and resilience by allowing controlled permeability instead of enforcing total isolation."
permalink: /datasets/view/TRIZ-bytes/TRIZ-31/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Porous Materials</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-31</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-31.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Increase adaptability and resilience by allowing controlled permeability instead of enforcing total isolation.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-31.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-31.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Porous Materials",
  "description": "Increase adaptability and resilience by allowing controlled permeability instead of enforcing total isolation.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-31/",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-31.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-31",
  "title": "Porous Materials",
  "intent": "Increase adaptability and resilience by allowing controlled permeability instead of enforcing total isolation.",
  "triz_principle": {
    "number": 31,
    "name": "Porous Materials",
    "definition": "Make an object porous or add porous elements to allow controlled passage of substances or signals."
  },
  "problem_understanding": {
    "core_contradiction": "We want strong boundaries for safety and clarity, but rigid isolation blocks learning, flow, and adaptation.",
    "why_this_hurts": "Over-isolated systems and teams lose feedback, duplicate work, and become slow to respond to change.",
    "typical_signals": [
      "hard silos between teams or systems",
      "information available only through formal escalation",
      "shadow integrations and data copies",
      "slow response to cross-domain issues"
    ]
  },
  "solution_logic": {
    "core_idea": "Design boundaries that are selective, not absolute.",
    "key_rule": "Let signals and learning pass through, while keeping control and ownership intact.",
    "how_it_resolves_the_contradiction": "The system stays protected but remains responsive and informed through controlled permeability."
  },
  "application_patterns": {
    "consulting": [
      "cross-domain sync points with clear agendas",
      "shared metrics dashboards across teams",
      "communities of practice alongside formal structures"
    ],
    "software_engineering": [
      "read-only access to shared data instead of full integration",
      "event subscriptions for visibility without control",
      "feature usage telemetry exposed across teams"
    ],
    "architecture": [
      "event streams for observability across domains",
      "API access with scoped permissions",
      "shared monitoring without shared ownership"
    ],
    "enterprise_sap": [
      "read-only replication for analytics and monitoring",
      "shared data quality dashboards across domains",
      "controlled access to master data attributes"
    ]
  },
  "anti_patterns": [
    "leaky boundaries with no control",
    "exposing internals instead of signals",
    "porosity without accountability"
  ],
  "usage_guidance": {
    "use_when": [
      "silos block visibility and learning",
      "teams need awareness without control",
      "coordination cost is high due to isolation"
    ],
    "do_not_use_when": [
      "data sensitivity forbids exposure",
      "boundaries are required for legal or safety reasons"
    ]
  },
  "diagnostic_questions": [
    "Which boundaries block useful signals?",
    "What information could be shared safely?",
    "How can visibility improve decisions without breaking ownership?"
  ],
  "example": {
    "before": "Each domain operates in isolation with no visibility into others.",
    "after": "Domains expose metrics and events while keeping control over their own data."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-31.json",
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-31.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Increase adaptability and resilience by allowing controlled permeability instead of enforcing total isolation."
  }
}
</code></pre>

</details>
</div>
