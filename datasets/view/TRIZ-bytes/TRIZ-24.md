---
layout: default
title: "Intermediary"
description: "Reduce coupling and conflict by introducing an intermediate element that manages interaction between parts."
permalink: /datasets/view/TRIZ-bytes/TRIZ-24/
sitemap: true
last_modified_at: 2026-04-13T08:37:04+00:00
dataset_detail_page: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Intermediary</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-24</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-24.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Reduce coupling and conflict by introducing an intermediate element that manages interaction between parts.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-24.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-24.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial only, attribution with source link required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Intermediary” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-24.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Intermediary",
  "description": "Reduce coupling and conflict by introducing an intermediate element that manages interaction between parts.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-24/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Intermediary” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-24.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-24.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-24",
  "title": "Intermediary",
  "intent": "Reduce coupling and conflict by introducing an intermediate element that manages interaction between parts.",
  "triz_principle": {
    "number": 24,
    "name": "Intermediary",
    "definition": "Use an intermediate carrier, mediator, or process to transfer or manage an action."
  },
  "problem_understanding": {
    "core_contradiction": "Direct interaction is fast, but it creates tight coupling, conflicts, and fragility.",
    "why_this_hurts": "When components interact directly, changes propagate uncontrollably and responsibilities blur.",
    "typical_signals": [
      "tight point-to-point integrations",
      "many direct dependencies",
      "changes in one system breaking others",
      "teams negotiating details instead of delivering"
    ]
  },
  "solution_logic": {
    "core_idea": "Insert a mediator that standardizes, buffers, or translates interactions.",
    "key_rule": "The intermediary owns the interaction contract, not the participants.",
    "how_it_resolves_the_contradiction": "Participants evolve independently while the intermediary absorbs variability and change."
  },
  "application_patterns": {
    "consulting": [
      "use a facilitator to mediate conflicting stakeholders",
      "introduce decision frameworks between strategy and execution",
      "centralize arbitration for cross-domain conflicts"
    ],
    "software_engineering": [
      "message brokers instead of direct calls",
      "API gateways managing contracts and policies",
      "workflow engines orchestrating steps"
    ],
    "architecture": [
      "event buses decoupling producers and consumers",
      "service meshes handling cross-cutting concerns",
      "anti-corruption layers between domains"
    ],
    "enterprise_sap": [
      "middleware for integration instead of direct RFCs",
      "MDG as governance intermediary between sources and consumers",
      "replication layers translating and validating data"
    ]
  },
  "anti_patterns": [
    "intermediary becoming a bottleneck",
    "opaque mediation with hidden logic",
    "adding intermediaries without removing direct coupling"
  ],
  "usage_guidance": {
    "use_when": [
      "direct coupling causes frequent breakage",
      "participants evolve at different speeds",
      "interaction logic is complex or volatile"
    ],
    "do_not_use_when": [
      "interaction is simple and stable",
      "latency must be minimal"
    ]
  },
  "diagnostic_questions": [
    "Where does direct interaction cause the most pain?",
    "Which variability could be absorbed by a mediator?",
    "What contract should be owned centrally?"
  ],
  "example": {
    "before": "Systems integrate directly with each other using custom logic.",
    "after": "A mediation layer standardizes and manages all interactions."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-24.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Intermediary” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-24.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-24.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-04-13T08:37:04+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Reduce coupling and conflict by introducing an intermediate element that manages interaction between parts.",
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
