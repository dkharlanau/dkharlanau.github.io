---
layout: default
title: "Asymmetry"
description: "Break false symmetry to reduce complexity, cost, or risk by assigning different roles or properties to similar-looking parts."
permalink: /datasets/view/TRIZ-bytes/TRIZ-04/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Asymmetry</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-04</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-04.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Break false symmetry to reduce complexity, cost, or risk by assigning different roles or properties to similar-looking parts.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-04.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-04.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Asymmetry",
  "description": "Break false symmetry to reduce complexity, cost, or risk by assigning different roles or properties to similar-looking parts.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-04/",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-04.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-04",
  "title": "Asymmetry",
  "intent": "Break false symmetry to reduce complexity, cost, or risk by assigning different roles or properties to similar-looking parts.",
  "triz_principle": {
    "number": 4,
    "name": "Asymmetry",
    "definition": "Replace symmetrical structures or interactions with asymmetrical ones where roles and responsibilities differ."
  },
  "problem_understanding": {
    "core_contradiction": "We want fairness and uniformity, but equal treatment creates inefficiency, duplication, or deadlocks.",
    "why_this_hurts": "Symmetry often hides decision paralysis: everyone waits for everyone else, or the same heavy rules apply where they are not needed.",
    "typical_signals": [
      "bidirectional dependencies",
      "mutual approvals and endless coordination",
      "mirror systems doing the same work",
      "conflicts over ownership because roles are unclear"
    ]
  },
  "solution_logic": {
    "core_idea": "Intentionally assign different roles, authority, or behavior to similar elements.",
    "key_rule": "Make responsibility asymmetric even if structure looks similar.",
    "how_it_resolves_the_contradiction": "Clear direction replaces negotiation; decisions flow in one direction, reducing coordination cost and risk."
  },
  "application_patterns": {
    "consulting": [
      "define a single decision owner instead of consensus bodies",
      "use one-way escalation paths",
      "assign one party as rule-setter and others as rule-consumers"
    ],
    "software_engineering": [
      "unidirectional data flow instead of bidirectional syncing",
      "single-writer, multiple-reader models",
      "command-query separation (CQS)"
    ],
    "architecture": [
      "master–replica instead of peer-to-peer",
      "event producers vs event consumers (no symmetry)",
      "northbound vs southbound interfaces"
    ],
    "enterprise_sap": [
      "MDG as single source of truth; S/4 as consumer only",
      "one-way replication with clear ownership",
      "asymmetric authorization: create/change vs view-only roles"
    ]
  },
  "anti_patterns": [
    "pretending symmetry while hiding power elsewhere",
    "creating asymmetry without communicating ownership",
    "mixing symmetric data ownership with asymmetric processes"
  ],
  "usage_guidance": {
    "use_when": [
      "coordination cost is higher than execution cost",
      "decisions are slow due to consensus requirements",
      "systems or teams block each other"
    ],
    "do_not_use_when": [
      "true peer collaboration is required",
      "load or responsibility must be evenly distributed for resilience"
    ]
  },
  "diagnostic_questions": [
    "Where do we require mutual agreement when one owner would be enough?",
    "Which interactions could become one-directional?",
    "Who should be the clear authority in this flow?"
  ],
  "example": {
    "before": "Two systems synchronize master data bidirectionally and constantly conflict.",
    "after": "One system is the authoritative source; the other only consumes updates via one-way replication."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-04.json",
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-04.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Break false symmetry to reduce complexity, cost, or risk by assigning different roles or properties to similar-looking parts."
  }
}
</code></pre>

</details>
</div>
