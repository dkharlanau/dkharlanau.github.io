---
layout: default
title: "Copying"
description: "Reduce cost, risk, or complexity by using copies, templates, or simplified representations instead of originals."
permalink: /datasets/view/TRIZ-bytes/TRIZ-26/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Copying</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-26</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-26.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Reduce cost, risk, or complexity by using copies, templates, or simplified representations instead of originals.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-26.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-26.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Copying",
  "description": "Reduce cost, risk, or complexity by using copies, templates, or simplified representations instead of originals.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-26/",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-26.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-26",
  "title": "Copying",
  "intent": "Reduce cost, risk, or complexity by using copies, templates, or simplified representations instead of originals.",
  "triz_principle": {
    "number": 26,
    "name": "Copying",
    "definition": "Use simple or inexpensive copies instead of complex, expensive, or fragile originals."
  },
  "problem_understanding": {
    "core_contradiction": "We need accuracy and reliability, but working with the original system or data is risky, slow, or costly.",
    "why_this_hurts": "Direct interaction with production assets increases failure impact, limits experimentation, and slows learning.",
    "typical_signals": [
      "fear of touching production",
      "testing blocked by data sensitivity",
      "experiments postponed due to risk",
      "high cost of environments and setups"
    ]
  },
  "solution_logic": {
    "core_idea": "Work on safe copies or abstractions instead of originals.",
    "key_rule": "Copy the behavior that matters, not the full complexity.",
    "how_it_resolves_the_contradiction": "Learning and change accelerate while risk to critical assets is minimized."
  },
  "application_patterns": {
    "consulting": [
      "use reference cases and archetypes instead of bespoke analysis",
      "simulate decisions using scenarios",
      "prototype recommendations before full rollout"
    ],
    "software_engineering": [
      "use mocks and stubs instead of live dependencies",
      "sandbox environments for experimentation",
      "golden templates for services and pipelines"
    ],
    "architecture": [
      "blueprints and reference architectures",
      "shadow traffic for testing changes",
      "digital twins for complex systems"
    ],
    "enterprise_sap": [
      "client copies for testing and training",
      "test data subsets instead of full datasets",
      "simulation runs before productive changes"
    ]
  },
  "anti_patterns": [
    "copies drifting away from reality",
    "false confidence from oversimplified models",
    "maintaining too many variants"
  ],
  "usage_guidance": {
    "use_when": [
      "risk of change is high",
      "learning or experimentation is needed",
      "production access is constrained"
    ],
    "do_not_use_when": [
      "exact real-time behavior is required",
      "copies are costly to maintain"
    ]
  },
  "diagnostic_questions": [
    "What part of the system is too risky to touch directly?",
    "Which behaviors must be preserved in the copy?",
    "How can we validate that the copy stays representative?"
  ],
  "example": {
    "before": "All testing and validation happen directly in the production-like environment.",
    "after": "Teams experiment safely on copies and promote only validated changes."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-26.json",
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-26.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Reduce cost, risk, or complexity by using copies, templates, or simplified representations instead of originals."
  }
}
</code></pre>

</details>
</div>
