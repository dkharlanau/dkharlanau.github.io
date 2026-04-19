---
layout: default
title: "Phase Transitions"
description: "Achieve step-change improvements by moving the system into a different operating state instead of incremental optimization."
permalink: /datasets/view/TRIZ-bytes/TRIZ-36/
sitemap: true
last_modified_at: 2026-04-13T08:37:04+00:00
dataset_detail_page: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Phase Transitions</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-36</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-36.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Achieve step-change improvements by moving the system into a different operating state instead of incremental optimization.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-36.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-36.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial only, attribution with source link required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Phase Transitions” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-36.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Phase Transitions",
  "description": "Achieve step-change improvements by moving the system into a different operating state instead of incremental optimization.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-36/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Phase Transitions” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-36.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-36.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-36",
  "title": "Phase Transitions",
  "intent": "Achieve step-change improvements by moving the system into a different operating state instead of incremental optimization.",
  "triz_principle": {
    "number": 36,
    "name": "Phase Transitions",
    "definition": "Use phase changes (state transitions) to obtain new properties or behavior."
  },
  "problem_understanding": {
    "core_contradiction": "Incremental improvements are not enough, but radical redesign seems too risky.",
    "why_this_hurts": "Teams keep polishing within the same mode of operation, hitting a ceiling where effort no longer translates into results.",
    "typical_signals": [
      "diminishing returns from optimization",
      "systems behaving well until a sudden collapse",
      "processes that fail only beyond certain scale or volume",
      "performance cliffs instead of smooth degradation"
    ]
  },
  "solution_logic": {
    "core_idea": "Change the operating state of the system so new properties emerge.",
    "key_rule": "Do not optimize inside a phase that has reached its limits.",
    "how_it_resolves_the_contradiction": "A phase change unlocks fundamentally different behavior instead of marginal gains."
  },
  "application_patterns": {
    "consulting": [
      "switch from project mode to product mode",
      "move from manual decision-making to rule-based governance",
      "introduce outcome-based funding instead of activity-based budgeting"
    ],
    "software_engineering": [
      "switch from synchronous to asynchronous processing",
      "move from monolith to modular monolith",
      "introduce streaming instead of batch at scale thresholds"
    ],
    "architecture": [
      "event-driven transition after scale threshold",
      "read/write separation when contention appears",
      "introduce eventual consistency instead of strict ACID everywhere"
    ],
    "enterprise_sap": [
      "move from manual master data maintenance to MDG",
      "switch from project-specific rules to reusable governance frameworks",
      "transition from migration mode to steady-state governance"
    ]
  },
  "anti_patterns": [
    "triggering phase change too early",
    "mixing phases without clear boundaries",
    "ignoring readiness for the new state"
  ],
  "usage_guidance": {
    "use_when": [
      "incremental optimization no longer works",
      "system behavior changes abruptly at scale",
      "constraints are inherent to the current mode"
    ],
    "do_not_use_when": [
      "problem can still be solved by tuning parameters",
      "organization is not ready for a new operating model"
    ]
  },
  "diagnostic_questions": [
    "What mode is the system currently operating in?",
    "Where do we see sharp behavioral changes?",
    "What new properties would a different mode unlock?"
  ],
  "example": {
    "before": "Manual master data processes struggle as volume grows.",
    "after": "MDG introduces a new governance phase with automated workflows and rules."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-36.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Phase Transitions” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-36.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-36.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-04-13T08:37:04+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Achieve step-change improvements by moving the system into a different operating state instead of incremental optimization.",
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
