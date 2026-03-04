---
layout: default
title: "Local Quality"
description: "Allow different parts of a system to have different properties instead of forcing uniformity everywhere."
permalink: /datasets/view/TRIZ-bytes/TRIZ-03/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Local Quality</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-03</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-03.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Allow different parts of a system to have different properties instead of forcing uniformity everywhere.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-03.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-03.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial only, attribution with source link required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Local Quality” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-03.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Local Quality",
  "description": "Allow different parts of a system to have different properties instead of forcing uniformity everywhere.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-03/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Local Quality” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-03.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-03.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-03",
  "title": "Local Quality",
  "intent": "Allow different parts of a system to have different properties instead of forcing uniformity everywhere.",
  "triz_principle": {
    "number": 3,
    "name": "Local Quality",
    "definition": "Transition from uniform structure or conditions to non-uniform ones, where each part performs under conditions best suited to it."
  },
  "problem_understanding": {
    "core_contradiction": "We want standardization to reduce complexity, but different parts of the system have fundamentally different needs.",
    "why_this_hurts": "When everything is treated the same, some parts become over-engineered while others are constrained, leading to inefficiency and hidden workarounds.",
    "typical_signals": [
      "one-size-fits-all process or architecture",
      "performance tuning in the wrong places",
      "excessive configuration just to fit special cases",
      "teams bypass standards to get work done"
    ]
  },
  "solution_logic": {
    "core_idea": "Optimize each part locally instead of globally enforcing the same rules everywhere.",
    "key_rule": "Standardize interfaces and outcomes, not internal implementation details.",
    "how_it_resolves_the_contradiction": "The system stays coherent at the boundaries, while each segment can use the most suitable approach internally."
  },
  "application_patterns": {
    "consulting": [
      "apply different governance intensity depending on risk and impact",
      "use lightweight processes for low-risk changes and strict controls for high-risk ones",
      "tailor KPIs to the nature of each domain, not one global metric set"
    ],
    "software_engineering": [
      "use different data storage or consistency models per component",
      "optimize hot paths separately from rarely used flows",
      "allow different coding styles or frameworks behind stable APIs"
    ],
    "architecture": [
      "polyglot persistence instead of one database for all use cases",
      "separate real-time transactional paths from batch or analytical paths",
      "different scalability strategies per subsystem"
    ],
    "enterprise_sap": [
      "apply stricter validation for financially critical master data and lighter rules for informational attributes",
      "allow local extensions in specific organizational units without changing global templates",
      "use different replication frequencies depending on business criticality"
    ]
  },
  "anti_patterns": [
    "local optimizations without clear boundaries",
    "breaking global consistency rules",
    "letting every team define its own standards without alignment"
  ],
  "usage_guidance": {
    "use_when": [
      "parts of the system have clearly different performance, risk, or compliance needs",
      "standardization causes friction and shadow processes",
      "optimization efforts are spread evenly instead of focused where it matters"
    ],
    "do_not_use_when": [
      "the system is small and uniform",
      "differences are cosmetic rather than structural"
    ]
  },
  "diagnostic_questions": [
    "Which parts of the system actually need the highest reliability or control?",
    "Where are we paying the cost of standards without getting value?",
    "Which components would benefit most from being treated differently?"
  ],
  "example": {
    "before": "All changes follow the same heavy approval and testing process regardless of impact.",
    "after": "High-risk financial changes use strict governance, while low-risk UI or reporting changes follow a lightweight fast-track."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-03.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Local Quality” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-03.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-03.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-03-04T11:23:27+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Allow different parts of a system to have different properties instead of forcing uniformity everywhere.",
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
