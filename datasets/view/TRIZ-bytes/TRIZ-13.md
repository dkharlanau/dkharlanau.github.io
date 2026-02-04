---
layout: default
title: "The Other Way Around (Inversion)"
description: "Solve a problem by reversing actions, relationships, or assumptions instead of optimizing the existing direction."
permalink: /datasets/view/TRIZ-bytes/TRIZ-13/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">The Other Way Around (Inversion)</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-13</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-13.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Solve a problem by reversing actions, relationships, or assumptions instead of optimizing the existing direction.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-13.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-13.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "The Other Way Around (Inversion)",
  "description": "Solve a problem by reversing actions, relationships, or assumptions instead of optimizing the existing direction.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-13/",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-13.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-13",
  "title": "The Other Way Around (Inversion)",
  "intent": "Solve a problem by reversing actions, relationships, or assumptions instead of optimizing the existing direction.",
  "triz_principle": {
    "number": 13,
    "name": "The Other Way Around",
    "definition": "Invert the action, the system structure, or the problem perspective to achieve the desired effect."
  },
  "problem_understanding": {
    "core_contradiction": "We keep optimizing the current approach, but results do not improve or get worse.",
    "why_this_hurts": "Incremental optimization reinforces a flawed direction; effort increases while impact stays flat.",
    "typical_signals": [
      "repeated optimizations with diminishing returns",
      "more controls but lower throughput",
      "processes that exist mainly to fix problems they create",
      "teams exhausted by constant tuning"
    ]
  },
  "solution_logic": {
    "core_idea": "Reverse the flow, responsibility, or logic instead of refining it.",
    "key_rule": "If improvement stalls, question the direction, not the speed.",
    "how_it_resolves_the_contradiction": "Inversion exposes hidden assumptions and unlocks simpler or more robust solution paths."
  },
  "application_patterns": {
    "consulting": [
      "start from desired outcome and work backwards",
      "replace approval-driven processes with exception-driven ones",
      "shift from pushing work to pulling demand"
    ],
    "software_engineering": [
      "event-driven instead of request-driven architectures",
      "pull-based processing instead of scheduled batch jobs",
      "consumer-controlled retries instead of producer retries"
    ],
    "architecture": [
      "CQRS: queries pull state instead of being updated synchronously",
      "reverse dependencies using dependency inversion",
      "policy-as-code instead of manual enforcement"
    ],
    "enterprise_sap": [
      "exception-based MDG workflows instead of mandatory approvals",
      "downstream-triggered replication instead of central push",
      "derive data on read instead of precomputing everything"
    ]
  },
  "anti_patterns": [
    "inverting without understanding the original goal",
    "creating symmetrical complexity in the opposite direction",
    "mixing old and inverted logic inconsistently"
  ],
  "usage_guidance": {
    "use_when": [
      "optimization no longer yields results",
      "controls keep increasing but quality drops",
      "process exists mainly to manage its own side effects"
    ],
    "do_not_use_when": [
      "current direction is fundamentally correct and under-optimized",
      "inversion would violate safety or compliance constraints"
    ]
  },
  "diagnostic_questions": [
    "What if we did the opposite of our current approach?",
    "Which assumptions would break if flow direction changed?",
    "Who should really control this interaction?"
  ],
  "example": {
    "before": "Central team pushes frequent mandatory updates to all systems.",
    "after": "Systems pull updates when ready, based on explicit contracts and readiness checks."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-13.json",
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-13.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Solve a problem by reversing actions, relationships, or assumptions instead of optimizing the existing direction."
  }
}
</code></pre>

</details>
</div>
