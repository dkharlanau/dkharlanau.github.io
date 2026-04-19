---
layout: default
title: "Enterprise AI Deployment Is Real, but Data Complexity Still Blocks Scale"
description: "Use current enterprise survey data to anchor conversations about AI rollout, skills gaps, and data readiness in large organizations."
permalink: /datasets/view/ai-business-signals/aibs-001/
sitemap: true
last_modified_at: 2026-04-13T08:37:04+00:00
dataset_detail_page: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Enterprise AI Deployment Is Real, but Data Complexity Still Blocks Scale</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">ai-business-signals</span>
    <span class="pill pill--type">ai_business_signal</span>
    <span class="pill">aibs-001</span>
    <span class="pill">enterprise-ai</span> <span class="pill">adoption</span> <span class="pill">data-complexity</span> <span class="pill">skills-gap</span> <span class="pill">governance</span> <span class="pill">sap-relevance</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/ai-business-signals/aibs-001.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/ai-business-signals/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Use current enterprise survey data to anchor conversations about AI rollout, skills gaps, and data readiness in large organizations.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/ai-business-signals/aibs-001.json">https://dkharlanau.github.io/datasets/ai-business-signals/aibs-001.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial only, attribution with source link required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Enterprise AI Deployment Is Real, but Data Complexity Still Blocks Scale” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/ai-business-signals/aibs-001.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Enterprise AI Deployment Is Real, but Data Complexity Still Blocks Scale",
  "description": "Use current enterprise survey data to anchor conversations about AI rollout, skills gaps, and data readiness in large organizations.",
  "url": "https://dkharlanau.github.io/datasets/view/ai-business-signals/aibs-001/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Enterprise AI Deployment Is Real, but Data Complexity Still Blocks Scale” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/ai-business-signals/aibs-001.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/ai-business-signals/aibs-001.json"
    }
  ],
  "keywords": [
    "enterprise-ai",
    "adoption",
    "data-complexity",
    "skills-gap",
    "governance",
    "sap-relevance"
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "aibs-001",
  "title": "Enterprise AI Deployment Is Real, but Data Complexity Still Blocks Scale",
  "type": "ai_business_signal",
  "theme": "enterprise-adoption",
  "intent": "Use current enterprise survey data to anchor conversations about AI rollout, skills gaps, and data readiness in large organizations.",
  "published_on": "2024-01-10",
  "coverage_period": "Survey fielded in November 2023",
  "source": {
    "organization": "IBM",
    "title": "Data Suggests Growth in Enterprise Adoption of AI is Due to Widespread Deployment by Early Adopters, But Barriers Keep 40% in the Exploration and Experimentation Phases",
    "url": "https://newsroom.ibm.com/2024-01-10-Data-Suggests-Growth-in-Enterprise-Adoption-of-AI-is-Due-to-Widespread-Deployment-by-Early-Adopters",
    "publisher_type": "primary",
    "methodology": "Morning Consult survey commissioned by IBM; 8,584 IT professionals across multiple markets."
  },
  "fact": {
    "primary_stat": "42% of enterprise-scale organizations reported AI actively in use.",
    "supporting_stats": [
      "40% were still exploring or experimenting.",
      "59% of organizations already exploring or deploying AI said they accelerated rollout or investment in the prior 24 months.",
      "Top deployment barriers were limited AI skills and expertise (33%), too much data complexity (25%), and ethical concerns (23%)."
    ]
  },
  "business_relevance": [
    "The enterprise conversation has moved beyond whether AI is real; the bottleneck is operational scale.",
    "Data complexity is a board-level delivery problem, not just a platform problem."
  ],
  "dzmitryi_commentary": "For SAP-heavy environments this matters because the barrier profile is familiar: fragmented master data, weak ownership, and integration noise. If 25% of large organizations cite data complexity as a blocker, then MDG, interface governance, and operational memory are part of the AI business case, not side work.",
  "focus_fit": [
    "sap-ams",
    "data-governance",
    "operational-continuity",
    "practical-ai"
  ],
  "tags": [
    "enterprise-ai",
    "adoption",
    "data-complexity",
    "skills-gap",
    "governance",
    "sap-relevance"
  ],
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "ai-business-signals",
    "source_project": "cv-ai",
    "source_path": "ai-business-signals/aibs-001.json",
    "canonical_url": "https://dkharlanau.github.io/datasets/ai-business-signals/aibs-001.json",
    "created_at_utc": "2026-04-13T08:03:03+00:00",
    "updated_at_utc": "2026-04-13T08:37:04+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
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
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "ai_business_signal",
    "entity_subtype": "",
    "summary": "Use current enterprise survey data to anchor conversations about AI rollout, skills gaps, and data readiness in large organizations.",
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Enterprise AI Deployment Is Real, but Data Complexity Still Blocks Scale” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/ai-business-signals/aibs-001.json"
    },
    "doi": {
      "concept": "10.5281/zenodo.18862098",
      "version": "10.5281/zenodo.18862097",
      "repository": "https://github.com/dkharlanau/dkharlanau-datasets"
    },
    "license": {
      "name": "Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)",
      "spdx": "CC-BY-NC-4.0",
      "url": "https://creativecommons.org/licenses/by-nc/4.0/"
    }
  }
}
</code></pre>

</details>
</div>
