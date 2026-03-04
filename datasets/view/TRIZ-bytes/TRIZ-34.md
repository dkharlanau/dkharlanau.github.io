---
layout: default
title: "Discarding and Recovering"
description: "Improve flow and resilience by intentionally removing elements when they are no longer useful, while keeping the ability to restore them if needed."
permalink: /datasets/view/TRIZ-bytes/TRIZ-34/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Discarding and Recovering</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-34</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-34.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Improve flow and resilience by intentionally removing elements when they are no longer useful, while keeping the ability to restore them if needed.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-34.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-34.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial, attribution required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Discarding and Recovering” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-34.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Discarding and Recovering",
  "description": "Improve flow and resilience by intentionally removing elements when they are no longer useful, while keeping the ability to restore them if needed.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-34/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Discarding and Recovering” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-34.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-34.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-34",
  "title": "Discarding and Recovering",
  "intent": "Improve flow and resilience by intentionally removing elements when they are no longer useful, while keeping the ability to restore them if needed.",
  "triz_principle": {
    "number": 34,
    "name": "Discarding and Recovering",
    "definition": "Make parts of an object or system disappear after completing their function, or restore them when required."
  },
  "problem_understanding": {
    "core_contradiction": "We want stability and traceability, but keeping everything forever creates clutter, cost, and rigidity.",
    "why_this_hurts": "Unused artifacts, data, rules, and processes accumulate and slowly strangle system evolution.",
    "typical_signals": [
      "obsolete rules still active",
      "dead configuration nobody dares to remove",
      "historical data slowing systems",
      "fear of cleanup because rollback is unclear"
    ]
  },
  "solution_logic": {
    "core_idea": "Design explicit lifecycle: create → use → discard → optionally recover.",
    "key_rule": "Nothing is permanent unless it proves long-term value.",
    "how_it_resolves_the_contradiction": "The system stays lean while retaining the ability to recover knowledge or functionality when needed."
  },
  "application_patterns": {
    "consulting": [
      "sunset plans for initiatives and policies",
      "decision logs with expiry dates",
      "regular portfolio cleanup cycles"
    ],
    "software_engineering": [
      "feature flags with automatic expiration",
      "data retention and archival strategies",
      "deprecate-and-remove workflows"
    ],
    "architecture": [
      "soft deletes with recovery windows",
      "versioned APIs with retirement plans",
      "time-based cleanup jobs"
    ],
    "enterprise_sap": [
      "temporary MDG rules removed after migration phases",
      "archiving obsolete master data",
      "cleanup of unused workflows and replication settings"
    ]
  },
  "anti_patterns": [
    "deleting without recovery strategy",
    "never removing anything 'just in case'",
    "cleanup driven by crisis instead of policy"
  ],
  "usage_guidance": {
    "use_when": [
      "system complexity grows over time",
      "many elements have unclear purpose",
      "change is blocked by legacy clutter"
    ],
    "do_not_use_when": [
      "regulatory rules require permanent retention",
      "recovery cost would be unacceptable"
    ]
  },
  "diagnostic_questions": [
    "Which elements no longer deliver value?",
    "What could safely expire by default?",
    "How can recovery be made cheap and reliable?"
  ],
  "example": {
    "before": "Old validation rules and workflows remain active long after their original purpose is gone.",
    "after": "Rules expire automatically and can be restored from versioned history if needed."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-34.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Discarding and Recovering” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-34.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-34.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-03-04T11:23:27+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Improve flow and resilience by intentionally removing elements when they are no longer useful, while keeping the ability to restore them if needed.",
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
