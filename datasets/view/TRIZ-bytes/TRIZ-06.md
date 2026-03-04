---
layout: default
title: "Universality"
description: "Reduce system complexity by making one element perform multiple functions instead of introducing new specialized components."
permalink: /datasets/view/TRIZ-bytes/TRIZ-06/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Universality</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-06</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-06.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Reduce system complexity by making one element perform multiple functions instead of introducing new specialized components.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-06.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-06.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial only, attribution with source link required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Universality” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-06.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Universality",
  "description": "Reduce system complexity by making one element perform multiple functions instead of introducing new specialized components.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-06/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Universality” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-06.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-06.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-06",
  "title": "Universality",
  "intent": "Reduce system complexity by making one element perform multiple functions instead of introducing new specialized components.",
  "triz_principle": {
    "number": 6,
    "name": "Universality",
    "definition": "Make an object or system perform multiple functions, eliminating the need for other parts."
  },
  "problem_understanding": {
    "core_contradiction": "We want richer functionality, but adding new components increases complexity, cost, and maintenance burden.",
    "why_this_hurts": "Each new specialized element adds integration points, failure modes, documentation, and cognitive load for teams.",
    "typical_signals": [
      "many small tools doing similar things",
      "overlapping services or frameworks",
      "high integration and maintenance cost",
      "teams struggling to understand the full landscape"
    ]
  },
  "solution_logic": {
    "core_idea": "Reuse and extend existing elements to cover multiple related needs.",
    "key_rule": "Prefer extending a stable, well-understood component over introducing a new specialized one.",
    "how_it_resolves_the_contradiction": "Functionality grows while the number of moving parts stays limited, reducing coordination and operational risk."
  },
  "application_patterns": {
    "consulting": [
      "use one decision forum to handle related topics instead of many committees",
      "define roles that cover multiple adjacent responsibilities",
      "reuse a single framework for analysis, design, and evaluation"
    ],
    "software_engineering": [
      "reuse a common pipeline for validation, transformation, and logging",
      "extend existing services with configuration instead of new microservices",
      "use shared libraries instead of duplicating logic"
    ],
    "architecture": [
      "platform components providing multiple capabilities (auth, audit, config)",
      "shared event backbone instead of point-to-point integrations",
      "common domain services reused across contexts"
    ],
    "enterprise_sap": [
      "use MDG as a single governance entry point for multiple master data objects",
      "reuse BRF+ rules across validation, derivation, and decision logic",
      "leverage standard SAP frameworks instead of parallel custom tools"
    ]
  },
  "anti_patterns": [
    "overloading a component beyond its natural responsibility",
    "creating a god object that knows too much",
    "forcing universality where specialization is required"
  ],
  "usage_guidance": {
    "use_when": [
      "multiple components solve closely related problems",
      "integration and maintenance costs dominate",
      "a stable core component already exists"
    ],
    "do_not_use_when": [
      "responsibilities are fundamentally different",
      "scaling or performance needs diverge strongly",
      "the component would become a single point of failure"
    ]
  },
  "diagnostic_questions": [
    "Which tools or services overlap in purpose?",
    "What functionality could be absorbed by an existing stable component?",
    "Where does adding a new component create more cost than value?"
  ],
  "example": {
    "before": "Separate services handle validation, auditing, and routing, each with its own configuration and lifecycle.",
    "after": "A single configurable pipeline performs validation, auditing, and routing based on context."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-06.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Universality” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-06.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-06.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-03-04T11:23:27+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Reduce system complexity by making one element perform multiple functions instead of introducing new specialized components.",
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
