---
layout: default
title: "Cheap Short-Living Objects"
description: "Reduce risk and cost by using temporary, disposable, or easily replaceable elements instead of durable ones."
permalink: /datasets/view/TRIZ-bytes/TRIZ-27/
sitemap: true
last_modified_at: 2026-04-13T08:37:04+00:00
dataset_detail_page: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Cheap Short-Living Objects</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-27</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-27.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Reduce risk and cost by using temporary, disposable, or easily replaceable elements instead of durable ones.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-27.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-27.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial only, attribution with source link required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Cheap Short-Living Objects” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-27.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Cheap Short-Living Objects",
  "description": "Reduce risk and cost by using temporary, disposable, or easily replaceable elements instead of durable ones.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-27/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Cheap Short-Living Objects” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-27.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-27.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-27",
  "title": "Cheap Short-Living Objects",
  "intent": "Reduce risk and cost by using temporary, disposable, or easily replaceable elements instead of durable ones.",
  "triz_principle": {
    "number": 27,
    "name": "Cheap Short-Living Objects",
    "definition": "Replace expensive, long-lasting objects with cheaper, short-lived ones."
  },
  "problem_understanding": {
    "core_contradiction": "We want reliability and control, but long-lived solutions accumulate risk, rigidity, and maintenance cost.",
    "why_this_hurts": "Permanent solutions attract hacks, exceptions, and hidden dependencies that are hard to remove later.",
    "typical_signals": [
      "temporary solutions that become permanent",
      "long-lived environments or configurations nobody dares to change",
      "high cost to clean up experiments",
      "fear of rollback because impact is too big"
    ]
  },
  "solution_logic": {
    "core_idea": "Design components and processes to be temporary and disposable by default.",
    "key_rule": "If something is likely to change or fail, make it cheap to replace.",
    "how_it_resolves_the_contradiction": "Risk is limited in time and scope, enabling faster experimentation and cleaner evolution."
  },
  "application_patterns": {
    "consulting": [
      "time-boxed initiatives instead of open-ended programs",
      "pilot decisions with automatic expiration dates",
      "temporary task forces instead of permanent committees"
    ],
    "software_engineering": [
      "ephemeral environments for testing",
      "short-lived feature branches",
      "throwaway prototypes instead of over-engineered PoCs"
    ],
    "architecture": [
      "immutable infrastructure with easy replacement",
      "stateless services that can be recreated anytime",
      "canary components with planned removal"
    ],
    "enterprise_sap": [
      "temporary MDG rules for migration phases",
      "short-lived workflows for exceptional periods",
      "sandbox systems instead of permanent special clients"
    ]
  },
  "anti_patterns": [
    "temporary solutions without clear expiration",
    "cheap components used in critical long-term paths",
    "lack of cleanup ownership"
  ],
  "usage_guidance": {
    "use_when": [
      "uncertainty is high",
      "experimentation is required",
      "long-term commitment is risky"
    ],
    "do_not_use_when": [
      "stability over long periods is required",
      "replacement cost is actually high"
    ]
  },
  "diagnostic_questions": [
    "Which elements are expected to change soon?",
    "What could be made disposable instead of permanent?",
    "How can replacement be automated?"
  ],
  "example": {
    "before": "A pilot solution becomes a long-term dependency with no clear owner.",
    "after": "The pilot is explicitly temporary and replaced or removed after evaluation."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-27.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Cheap Short-Living Objects” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-27.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-27.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-04-13T08:37:04+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Reduce risk and cost by using temporary, disposable, or easily replaceable elements instead of durable ones.",
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
