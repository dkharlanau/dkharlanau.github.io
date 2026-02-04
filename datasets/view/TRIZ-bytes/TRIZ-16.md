---
layout: default
title: "Partial or Excessive Actions"
description: "Achieve better results by deliberately doing less or more than the nominal requirement instead of aiming for exactness."
permalink: /datasets/view/TRIZ-bytes/TRIZ-16/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Partial or Excessive Actions</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-16</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-16.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Achieve better results by deliberately doing less or more than the nominal requirement instead of aiming for exactness.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-16.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-16.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Partial or Excessive Actions",
  "description": "Achieve better results by deliberately doing less or more than the nominal requirement instead of aiming for exactness.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-16/",
  "isAccessibleForFree": true,
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-16.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-16",
  "title": "Partial or Excessive Actions",
  "intent": "Achieve better results by deliberately doing less or more than the nominal requirement instead of aiming for exactness.",
  "triz_principle": {
    "number": 16,
    "name": "Partial or Excessive Actions",
    "definition": "If an exact action is difficult, achieve the required effect by doing slightly less or slightly more."
  },
  "problem_understanding": {
    "core_contradiction": "We aim for exact correctness, but precision is expensive, slow, or unrealistic under constraints.",
    "why_this_hurts": "Chasing perfect accuracy increases cost and delays, while most value could be delivered earlier with approximation.",
    "typical_signals": [
      "long cycles to reach perfect data quality",
      "over-engineering for rare edge cases",
      "projects blocked waiting for full completeness",
      "high cost to close the last 5–10% gap"
    ]
  },
  "solution_logic": {
    "core_idea": "Intentionally choose approximation over exactness where it delivers faster or cheaper value.",
    "key_rule": "Optimize for impact, not mathematical perfection.",
    "how_it_resolves_the_contradiction": "Most benefits are realized early, while cost and time are kept under control."
  },
  "application_patterns": {
    "consulting": [
      "80/20 analysis instead of exhaustive studies",
      "phased recommendations with increasing precision",
      "decision-making with confidence ranges instead of exact numbers"
    ],
    "software_engineering": [
      "eventual consistency instead of strict immediate consistency",
      "best-effort processing with retries",
      "heuristics instead of complex optimization algorithms"
    ],
    "architecture": [
      "approximate caching strategies",
      "sampling instead of full data scans",
      "graceful degradation under load"
    ],
    "enterprise_sap": [
      "tolerance-based validations instead of exact matches",
      "phased data cleansing with priority attributes first",
      "allowing temporary inconsistencies resolved later by governance"
    ]
  },
  "anti_patterns": [
    "approximations without clear limits",
    "normalizing poor quality as acceptable forever",
    "lack of transparency about reduced precision"
  ],
  "usage_guidance": {
    "use_when": [
      "exact precision is costly but low-value",
      "speed matters more than completeness",
      "errors are reversible or low impact"
    ],
    "do_not_use_when": [
      "safety, finance, or legal correctness is mandatory",
      "errors are irreversible or catastrophic"
    ]
  },
  "diagnostic_questions": [
    "Where does the last 10% of effort bring little additional value?",
    "Which approximations would users accept?",
    "What precision level is actually required for decisions?"
  ],
  "example": {
    "before": "Project waits months to achieve 100% data correctness before go-live.",
    "after": "Critical data is corrected first; remaining issues are resolved incrementally post go-live."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-16.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau (SAP Lead). Dataset bytes: https://dkharlanau.github.io"
    },
    "license": {
      "name": "",
      "spdx": "",
      "url": ""
    },
    "links": {
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "contact": {
      "preferred": "linkedin",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-16.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Achieve better results by deliberately doing less or more than the nominal requirement instead of aiming for exactness."
  }
}
</code></pre>

</details>
</div>
