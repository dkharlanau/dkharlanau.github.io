---
layout: default
title: "Periodic Action"
description: "Replace continuous or one-time actions with periodic ones to reduce load, cost, and risk while maintaining effectiveness."
permalink: /datasets/view/TRIZ-bytes/TRIZ-19/
sitemap: true
last_modified_at: 2026-04-13T08:37:04+00:00
dataset_detail_page: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Periodic Action</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-19</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-19.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Replace continuous or one-time actions with periodic ones to reduce load, cost, and risk while maintaining effectiveness.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-19.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-19.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial only, attribution with source link required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Periodic Action” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-19.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Periodic Action",
  "description": "Replace continuous or one-time actions with periodic ones to reduce load, cost, and risk while maintaining effectiveness.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-19/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Periodic Action” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-19.json",
  "identifier": "https://doi.org/10.5281/zenodo.18862098",
  "sameAs": [
    "https://doi.org/10.5281/zenodo.18862098",
    "https://github.com/dkharlanau/dkharlanau-datasets"
  ],
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-19.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-19",
  "title": "Periodic Action",
  "intent": "Replace continuous or one-time actions with periodic ones to reduce load, cost, and risk while maintaining effectiveness.",
  "triz_principle": {
    "number": 19,
    "name": "Periodic Action",
    "definition": "Instead of continuous action, use periodic or pulsed actions; adjust frequency as needed."
  },
  "problem_understanding": {
    "core_contradiction": "We want constant control and availability, but continuous operation is expensive and fragile.",
    "why_this_hurts": "Always-on processes consume resources, amplify noise, and make systems harder to stabilize and reason about.",
    "typical_signals": [
      "continuous polling or checks",
      "high baseline system load",
      "alerts firing too often",
      "processes running even when nothing changes"
    ]
  },
  "solution_logic": {
    "core_idea": "Act at meaningful intervals instead of continuously.",
    "key_rule": "Choose frequency based on business impact, not technical convenience.",
    "how_it_resolves_the_contradiction": "The system stays responsive where it matters while reducing unnecessary work and noise."
  },
  "application_patterns": {
    "consulting": [
      "scheduled decision checkpoints instead of constant reviews",
      "periodic steering meetings with clear agendas",
      "time-boxed audits instead of continuous scrutiny"
    ],
    "software_engineering": [
      "batch processing instead of constant polling",
      "scheduled jobs triggered by change volume",
      "debounced or throttled events"
    ],
    "architecture": [
      "event batching",
      "scheduled reconciliation instead of real-time syncing",
      "time-windowed processing pipelines"
    ],
    "enterprise_sap": [
      "periodic data synchronization instead of continuous replication",
      "scheduled data quality checks",
      "batch-based mass changes with controlled windows"
    ]
  },
  "anti_patterns": [
    "periodic actions without clear triggers",
    "intervals chosen arbitrarily",
    "batch sizes that grow without limits"
  ],
  "usage_guidance": {
    "use_when": [
      "continuous processing brings little added value",
      "system load is unnecessarily high",
      "real-time is not a true business requirement"
    ],
    "do_not_use_when": [
      "real-time response is critical",
      "delays cause irreversible damage"
    ]
  },
  "diagnostic_questions": [
    "Which actions truly require real-time execution?",
    "What is the acceptable delay for business value?",
    "Where could batching reduce noise and cost?"
  ],
  "example": {
    "before": "System continuously polls downstream systems for changes.",
    "after": "Changes are collected and processed in controlled periodic batches."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-19.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Periodic Action” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-19.json"
    },
    "license": {
      "name": "Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)",
      "spdx": "CC-BY-NC-4.0",
      "url": "https://creativecommons.org/licenses/by-nc/4.0/"
    },
    "links": {
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau",
      "repository": "https://github.com/dkharlanau/dkharlanau-datasets"
    },
    "contact": {
      "preferred": "linkedin",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-19.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-04-13T08:37:04+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Replace continuous or one-time actions with periodic ones to reduce load, cost, and risk while maintaining effectiveness.",
    "doi": {
      "concept": "10.5281/zenodo.18862098",
      "version": "10.5281/zenodo.18862097",
      "repository": "https://github.com/dkharlanau/dkharlanau-datasets"
    }
  }
}
</code></pre>

</details>
</div>
