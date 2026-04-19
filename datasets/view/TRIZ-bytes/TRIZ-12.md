---
layout: default
title: "Equipotentiality"
description: "Reduce unnecessary effort by aligning conditions so work does not have to fight against artificial differences."
permalink: /datasets/view/TRIZ-bytes/TRIZ-12/
sitemap: true
last_modified_at: 2026-04-13T08:37:04+00:00
dataset_detail_page: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Equipotentiality</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-12</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-12.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Reduce unnecessary effort by aligning conditions so work does not have to fight against artificial differences.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-12.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-12.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial only, attribution with source link required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Equipotentiality” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-12.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Equipotentiality",
  "description": "Reduce unnecessary effort by aligning conditions so work does not have to fight against artificial differences.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-12/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Equipotentiality” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-12.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-12.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-12",
  "title": "Equipotentiality",
  "intent": "Reduce unnecessary effort by aligning conditions so work does not have to fight against artificial differences.",
  "triz_principle": {
    "number": 12,
    "name": "Equipotentiality",
    "definition": "Change working conditions so that an object is neither raised nor lowered; eliminate unnecessary potential differences."
  },
  "problem_understanding": {
    "core_contradiction": "We want efficient flow, but the system forces work to constantly move uphill through friction, approvals, or transformations.",
    "why_this_hurts": "Energy is wasted not on value creation, but on overcoming artificial barriers created by mismatched standards, environments, or formats.",
    "typical_signals": [
      "constant data transformations between systems",
      "manual alignment of formats, rules, or environments",
      "rework caused by incompatible assumptions",
      "teams spending time 'adapting' instead of building"
    ]
  },
  "solution_logic": {
    "core_idea": "Align conditions so work can flow naturally without resistance.",
    "key_rule": "Remove artificial differences before adding automation or tooling.",
    "how_it_resolves_the_contradiction": "By equalizing conditions, effort drops and throughput increases without adding complexity."
  },
  "application_patterns": {
    "consulting": [
      "align definitions and terminology before process design",
      "harmonize decision criteria across forums",
      "use shared templates and vocabularies"
    ],
    "software_engineering": [
      "standardize data formats and schemas early",
      "align dev/test/prod environments",
      "use common error and logging models"
    ],
    "architecture": [
      "canonical data models at integration boundaries",
      "uniform API standards across services",
      "shared identity and authorization mechanisms"
    ],
    "enterprise_sap": [
      "harmonized master data definitions across systems",
      "aligned number ranges and key mappings",
      "common validation logic before replication"
    ]
  },
  "anti_patterns": [
    "automating over misalignment",
    "adding adapters everywhere instead of fixing root causes",
    "forcing alignment where diversity is required"
  ],
  "usage_guidance": {
    "use_when": [
      "most effort goes into translation and alignment",
      "errors are caused by mismatched assumptions",
      "work slows down at system or team boundaries"
    ],
    "do_not_use_when": [
      "differences are intentional and valuable",
      "alignment cost exceeds efficiency gains"
    ]
  },
  "diagnostic_questions": [
    "Where do we constantly translate or adapt?",
    "Which differences add no real value?",
    "What could be aligned once instead of fixed repeatedly?"
  ],
  "example": {
    "before": "Each system uses its own master data definitions, requiring constant mapping and correction.",
    "after": "A shared canonical model removes the need for repeated transformations."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-12.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Equipotentiality” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-12.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-12.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-04-13T08:37:04+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Reduce unnecessary effort by aligning conditions so work does not have to fight against artificial differences.",
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
