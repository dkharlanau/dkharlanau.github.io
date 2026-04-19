---
layout: default
title: "Parameter Changes"
description: "Improve outcomes by changing key parameters instead of redesigning the entire system."
permalink: /datasets/view/TRIZ-bytes/TRIZ-35/
sitemap: true
last_modified_at: 2026-04-13T08:37:04+00:00
dataset_detail_page: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Parameter Changes</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-35</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-35.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Improve outcomes by changing key parameters instead of redesigning the entire system.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-35.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-35.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial only, attribution with source link required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Parameter Changes” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-35.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Parameter Changes",
  "description": "Improve outcomes by changing key parameters instead of redesigning the entire system.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-35/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Parameter Changes” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-35.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-35.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-35",
  "title": "Parameter Changes",
  "intent": "Improve outcomes by changing key parameters instead of redesigning the entire system.",
  "triz_principle": {
    "number": 35,
    "name": "Parameter Changes",
    "definition": "Change an object’s physical state, concentration, flexibility, or other parameters to achieve the desired effect."
  },
  "problem_understanding": {
    "core_contradiction": "We want better performance or quality, but structural changes are expensive and risky.",
    "why_this_hurts": "Teams jump to redesigns when many problems are caused by poorly tuned parameters rather than wrong architecture.",
    "typical_signals": [
      "talk about replatforming too early",
      "performance issues under specific conditions only",
      "rules that are correct in logic but wrong in thresholds",
      "systems that work but feel unnecessarily rigid"
    ]
  },
  "solution_logic": {
    "core_idea": "Tune parameters before changing structure.",
    "key_rule": "Exhaust parameter space before redesigning the system.",
    "how_it_resolves_the_contradiction": "Small, low-risk adjustments unlock large improvements without destabilizing the system."
  },
  "application_patterns": {
    "consulting": [
      "adjust decision thresholds instead of changing governance model",
      "change escalation limits before reorganizing teams",
      "tune KPIs rather than redefining strategy"
    ],
    "software_engineering": [
      "tune timeouts, batch sizes, and retry limits",
      "adjust cache TTLs and consistency levels",
      "feature flags to vary behavior by context"
    ],
    "architecture": [
      "scaling parameters instead of topology changes",
      "circuit breaker thresholds tuning",
      "config-driven resilience policies"
    ],
    "enterprise_sap": [
      "adjust MDG validation strictness by object or phase",
      "tune workflow thresholds for auto-approval",
      "modify replication frequency instead of redesigning integration"
    ]
  },
  "anti_patterns": [
    "random tuning without measurement",
    "hard-coding parameters",
    "over-tuning one area while ignoring system effects"
  ],
  "usage_guidance": {
    "use_when": [
      "system is mostly correct but poorly tuned",
      "issues appear only under certain conditions",
      "fast improvement is needed with low risk"
    ],
    "do_not_use_when": [
      "fundamental design is wrong",
      "parameters are already well optimized"
    ]
  },
  "diagnostic_questions": [
    "Which parameters most influence behavior?",
    "What ranges have never been tested?",
    "Which change would be reversible and cheap?"
  ],
  "example": {
    "before": "System is redesigned due to performance issues under peak load.",
    "after": "Timeouts, batch sizes, and caching parameters are tuned to handle peaks without redesign."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-35.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Parameter Changes” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-35.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-35.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-04-13T08:37:04+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Improve outcomes by changing key parameters instead of redesigning the entire system.",
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
