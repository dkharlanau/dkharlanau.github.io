---
layout: default
title: "Composite Materials"
description: "Combine different elements to achieve properties that none of them provide alone."
permalink: /datasets/view/TRIZ-bytes/TRIZ-40/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Composite Materials</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-40</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-40.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Combine different elements to achieve properties that none of them provide alone.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-40.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-40.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial, attribution required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Composite Materials” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-40.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Composite Materials",
  "description": "Combine different elements to achieve properties that none of them provide alone.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-40/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Composite Materials” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-40.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-40.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-40",
  "title": "Composite Materials",
  "intent": "Combine different elements to achieve properties that none of them provide alone.",
  "triz_principle": {
    "number": 40,
    "name": "Composite Materials",
    "definition": "Use composite structures made of different materials to obtain combined advantages."
  },
  "problem_understanding": {
    "core_contradiction": "We want simplicity, but single approaches cannot satisfy all competing requirements.",
    "why_this_hurts": "Pure solutions force trade-offs: speed vs control, flexibility vs stability, autonomy vs governance.",
    "typical_signals": [
      "either-or architectural debates",
      "solutions optimized for one dimension only",
      "frequent exceptions to rigid standards",
      "workarounds combining tools informally"
    ]
  },
  "solution_logic": {
    "core_idea": "Deliberately combine different approaches, each covering the other's weaknesses.",
    "key_rule": "Design the composition explicitly, not accidentally.",
    "how_it_resolves_the_contradiction": "The composite delivers balanced properties without forcing a single extreme."
  },
  "application_patterns": {
    "consulting": [
      "hybrid governance models (central + local)",
      "mixed delivery models (standard + custom)",
      "portfolio approaches instead of single bets"
    ],
    "software_engineering": [
      "modular monoliths (monolith + modularity)",
      "hybrid consistency models",
      "combining sync and async processing"
    ],
    "architecture": [
      "core platforms with extension layers",
      "hybrid cloud architectures",
      "event-driven core with synchronous edges"
    ],
    "enterprise_sap": [
      "SAP core with external side services",
      "MDG governance plus local extensions",
      "standard processes augmented by flexible tooling"
    ]
  },
  "anti_patterns": [
    "accidental complexity from ad-hoc mixing",
    "unclear ownership between combined elements",
    "composites without integration strategy"
  ],
  "usage_guidance": {
    "use_when": [
      "requirements conflict but both are essential",
      "pure approaches have failed",
      "system must serve diverse needs"
    ],
    "do_not_use_when": [
      "simplicity alone is the dominant goal",
      "team cannot manage hybrid complexity"
    ]
  },
  "diagnostic_questions": [
    "Which properties are in conflict?",
    "What combination could cover both?",
    "Where should boundaries between elements lie?"
  ],
  "example": {
    "before": "Either strict centralized governance or uncontrolled local freedom.",
    "after": "Central rules with controlled local extensions form a balanced composite."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-40.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Composite Materials” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-40.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-40.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-03-04T11:23:27+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Combine different elements to achieve properties that none of them provide alone.",
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
