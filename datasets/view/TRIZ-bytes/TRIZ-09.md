---
layout: default
title: "Preliminary Anti-Action"
description: "Reduce risk and cost by performing preventive actions before a problem fully manifests."
permalink: /datasets/view/TRIZ-bytes/TRIZ-09/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Preliminary Anti-Action</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-09</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-09.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Reduce risk and cost by performing preventive actions before a problem fully manifests.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-09.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-09.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial only, attribution with source link required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Preliminary Anti-Action” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-09.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Preliminary Anti-Action",
  "description": "Reduce risk and cost by performing preventive actions before a problem fully manifests.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-09/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Preliminary Anti-Action” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-09.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-09.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-09",
  "title": "Preliminary Anti-Action",
  "intent": "Reduce risk and cost by performing preventive actions before a problem fully manifests.",
  "triz_principle": {
    "number": 9,
    "name": "Preliminary Anti-Action",
    "definition": "If an action is likely to cause harmful effects, introduce countermeasures in advance."
  },
  "problem_understanding": {
    "core_contradiction": "We need to move fast, but changes often introduce defects, incidents, or rework.",
    "why_this_hurts": "Fixing problems after they occur is more expensive and disruptive than preventing them early.",
    "typical_signals": [
      "recurring incidents after releases",
      "late discovery of data quality issues",
      "frequent rollback or hotfixes",
      "teams firefighting instead of building"
    ]
  },
  "solution_logic": {
    "core_idea": "Anticipate likely failure modes and neutralize them before execution.",
    "key_rule": "Prevent the most probable damage, not all theoretical risks.",
    "how_it_resolves_the_contradiction": "Speed is preserved while risk is reduced through targeted, early safeguards."
  },
  "application_patterns": {
    "consulting": [
      "risk pre-mortems before major decisions",
      "checklists for common failure points",
      "early stakeholder alignment to avoid late objections"
    ],
    "software_engineering": [
      "input validation before processing",
      "static analysis and linters before runtime",
      "contract tests before integration"
    ],
    "architecture": [
      "circuit breakers to prevent cascading failures",
      "schema validation before data ingestion",
      "canary releases to detect issues early"
    ],
    "enterprise_sap": [
      "pre-check reports before MDG change request submission",
      "data quality rules before replication",
      "simulation and test runs before cutover activities"
    ]
  },
  "anti_patterns": [
    "trying to prevent every imaginable risk",
    "heavy upfront processes that slow delivery",
    "preventive controls disconnected from real failure modes"
  ],
  "usage_guidance": {
    "use_when": [
      "the same problems repeat across releases or projects",
      "late fixes are very expensive",
      "failure modes are well known"
    ],
    "do_not_use_when": [
      "risks are unknown or highly exploratory",
      "prevention costs more than recovery"
    ]
  },
  "diagnostic_questions": [
    "What failures happen most often after changes?",
    "Which problems are cheap to prevent but expensive to fix?",
    "What signals could warn us earlier?"
  ],
  "example": {
    "before": "Data errors are discovered only after replication to downstream systems.",
    "after": "Pre-validation rules catch data issues before replication is triggered."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-09.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Preliminary Anti-Action” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-09.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-09.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-03-04T11:23:27+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Reduce risk and cost by performing preventive actions before a problem fully manifests.",
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
