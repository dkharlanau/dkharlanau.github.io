---
layout: default
title: "Contradiction Formulation (Engineering Contradiction)"
description: "Turn a messy situation into a solvable TRIZ problem by expressing it as a trade-off between two parameters."
permalink: /datasets/view/TRIZ-bytes/TRIZ-TECH-01/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Contradiction Formulation (Engineering Contradiction)</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_technique</span>
    <span class="pill">TRIZ-TECH-01</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-TECH-01.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Turn a messy situation into a solvable TRIZ problem by expressing it as a trade-off between two parameters.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-01.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-01.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial, attribution required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Contradiction Formulation (Engineering Contradiction)” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-01.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Contradiction Formulation (Engineering Contradiction)",
  "description": "Turn a messy situation into a solvable TRIZ problem by expressing it as a trade-off between two parameters.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-TECH-01/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Contradiction Formulation (Engineering Contradiction)” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-01.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-01.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-TECH-01",
  "title": "Contradiction Formulation (Engineering Contradiction)",
  "intent": "Turn a messy situation into a solvable TRIZ problem by expressing it as a trade-off between two parameters.",
  "technique": {
    "name": "Engineering (Technical) Contradiction",
    "definition": "Improve one characteristic of a system, but another characteristic worsens as a result."
  },
  "inputs": {
    "problem_statement": "Plain-language description of the pain (symptoms, constraints, stakeholders).",
    "improving_parameter": "What you want to improve (speed, quality, cost, reliability, maintainability, etc.).",
    "worsening_parameter": "What gets worse when you push improvement (complexity, risk, latency, cost, etc.)."
  },
  "procedure": [
    "Write the problem in one sentence: 'We need to improve X, but then Y gets worse.'",
    "Confirm both sides are measurable (even roughly). Replace vague words with proxy metrics.",
    "Create 2–3 alternative contradictions using the same parameters but different framing (more 'physics', less opinion).",
    "Select the contradiction that, if resolved, would remove the biggest bottleneck."
  ],
  "outputs": {
    "contradiction": "We must improve &lt;X&gt; but it worsens &lt;Y&gt;.",
    "candidate_metrics": [
      "metric_for_X",
      "metric_for_Y"
    ],
    "variants": [
      "variant_1",
      "variant_2"
    ]
  },
  "how_it_connects_to_solution": {
    "next_step_options": [
      "Use Contradiction Matrix → Inventive Principles",
      "Reformulate into a Physical Contradiction (one parameter must be both high and low)",
      "Run System Operator (9 windows) to discover missing system-level contradictions"
    ]
  },
  "common_mistakes": [
    "Using opinions instead of parameters ('team is slow')",
    "Mixing causes and symptoms in X/Y",
    "Choosing contradictions that are not the real bottleneck"
  ],
  "example": {
    "consulting": {
      "contradiction": "We must increase governance strictness to reduce data errors, but it increases lead time and user resistance."
    },
    "software": {
      "contradiction": "We must increase validation to reduce incidents, but it increases latency and complexity."
    }
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-TECH-01.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Contradiction Formulation (Engineering Contradiction)” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-01.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-01.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-03-04T11:23:27+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_technique",
    "entity_subtype": "",
    "summary": "Turn a messy situation into a solvable TRIZ problem by expressing it as a trade-off between two parameters.",
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
