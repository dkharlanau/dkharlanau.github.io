---
layout: default
title: "System Operator (9 Windows)"
description: "Escape tunnel vision by analyzing the problem across time (past/present/future) and hierarchy (subsystem/system/supersystem)."
permalink: /datasets/view/TRIZ-bytes/TRIZ-TECH-03/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">System Operator (9 Windows)</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_technique</span>
    <span class="pill">TRIZ-TECH-03</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-TECH-03.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Escape tunnel vision by analyzing the problem across time (past/present/future) and hierarchy (subsystem/system/supersystem).</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-03.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-03.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "System Operator (9 Windows)",
  "description": "Escape tunnel vision by analyzing the problem across time (past/present/future) and hierarchy (subsystem/system/supersystem).",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-TECH-03/",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-03.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-TECH-03",
  "title": "System Operator (9 Windows)",
  "intent": "Escape tunnel vision by analyzing the problem across time (past/present/future) and hierarchy (subsystem/system/supersystem).",
  "technique": {
    "name": "System Operator / Multi-Screen / 9 Windows",
    "definition": "A 3×3 view: subsystem/system/supersystem × past/present/future, used to reveal hidden factors and solution directions."
  },
  "inputs": {
    "system_of_interest": "The product/process/service you are solving for.",
    "current_problem": "The issue in the 'system-present' window."
  },
  "procedure": [
    "Fill the 9 windows (write short bullet facts, not theories):",
    "  - Subsystem: parts/components; Supersystem: environment, stakeholders, adjacent systems.",
    "  - Past: how it worked before; Future: what it must become / trends / constraints.",
    "Ask 3 forcing questions:",
    "  1) What changed from past→present that created the problem?",
    "  2) If the future is forced (scale/regulation/AI), what breaks first?",
    "  3) Which window contains a lever that avoids changing the core system?",
    "Extract contradictions from windows (often the real contradiction is in supersystem or subsystem, not in the present system)."
  ],
  "outputs": {
    "nine_windows": {
      "subsystem_past": [],
      "subsystem_present": [],
      "subsystem_future": [],
      "system_past": [],
      "system_present": [],
      "system_future": [],
      "supersystem_past": [],
      "supersystem_present": [],
      "supersystem_future": []
    },
    "new_contradictions_found": [],
    "lever_candidates": [
      "change environment/contract instead of core logic",
      "change subsystem boundary instead of whole system"
    ]
  },
  "common_mistakes": [
    "Filling windows with opinions instead of observable facts",
    "Skipping supersystem (where many real constraints live)",
    "Treating it as documentation instead of a contradiction generator"
  ],
  "example": {
    "software": {
      "system_present": "API is slow under peak load.",
      "supersystem_present": "Downstream vendor rate-limits requests.",
      "lever_candidate": "Move to async queue + backpressure instead of optimizing core API."
    }
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-TECH-03.json",
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-TECH-03.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_technique",
    "entity_subtype": "",
    "summary": "Escape tunnel vision by analyzing the problem across time (past/present/future) and hierarchy (subsystem/system/supersystem)."
  }
}
</code></pre>

</details>
</div>
