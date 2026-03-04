---
layout: default
title: "X-Operator (Exaggeration / Extremes)"
description: "Force breakthrough ideas by pushing a system parameter to an extreme and observing what must change to make it work."
permalink: /datasets/view/TRIZ-bytes/TRIZ-TECH-04/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">X-Operator (Exaggeration / Extremes)</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_technique</span>
    <span class="pill">TRIZ-TECH-04</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-TECH-04.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Force breakthrough ideas by pushing a system parameter to an extreme and observing what must change to make it work.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-04.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-04.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial only, attribution with source link required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “X-Operator (Exaggeration / Extremes)” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-04.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "X-Operator (Exaggeration / Extremes)",
  "description": "Force breakthrough ideas by pushing a system parameter to an extreme and observing what must change to make it work.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-TECH-04/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “X-Operator (Exaggeration / Extremes)” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-04.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-04.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-TECH-04",
  "title": "X-Operator (Exaggeration / Extremes)",
  "intent": "Force breakthrough ideas by pushing a system parameter to an extreme and observing what must change to make it work.",
  "technique": {
    "name": "Exaggeration / Extremes (often used in OTSM-TRIZ trainings)",
    "definition": "Deliberately exaggerate a parameter (very high/very low) to reveal hidden constraints and new solution paths."
  },
  "inputs": {
    "target_parameter": "The variable tied to the contradiction (e.g., 'lead time', 'validation strictness', 'cost').",
    "extreme_directions": [
      "make it 10× bigger",
      "make it near-zero"
    ]
  },
  "procedure": [
    "Pick one parameter that matters most.",
    "Run two extremes:",
    "  - Extreme A: 'What if this parameter is 10× bigger?'",
    "  - Extreme B: 'What if this parameter is ~0 (almost eliminated)?'",
    "For each extreme, answer:",
    "  - What breaks first?",
    "  - What must be removed or added to survive?",
    "  - What new constraints appear?",
    "Translate extreme insights back into realistic solutions (often these become Separation-on-Condition or new architecture boundaries)."
  ],
  "outputs": {
    "extreme_A_breakpoints": [],
    "extreme_B_breakpoints": [],
    "solution_hypotheses": [
      "introduce fast/slow lanes",
      "automate the expensive checks",
      "move checks to boundary",
      "change the contract with the environment"
    ]
  },
  "common_mistakes": [
    "Staying realistic too early (kills the point)",
    "Not translating insights back to implementable steps",
    "Picking a parameter that is not the real bottleneck"
  ],
  "example": {
    "consulting": {
      "parameter": "Approval lead time",
      "extreme_A": "If approvals take 30 days, what must be pre-approved?",
      "insight": "Standard cases should be auto-approved; humans handle exceptions only."
    }
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-TECH-04.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “X-Operator (Exaggeration / Extremes)” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-04.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-04.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-03-04T11:23:27+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_technique",
    "entity_subtype": "",
    "summary": "Force breakthrough ideas by pushing a system parameter to an extreme and observing what must change to make it work.",
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
