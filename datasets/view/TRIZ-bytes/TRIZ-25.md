---
layout: default
title: "Self-Service"
description: "Reduce coordination cost and delays by letting a system or user perform needed actions independently."
permalink: /datasets/view/TRIZ-bytes/TRIZ-25/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Self-Service</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-25</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-25.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Reduce coordination cost and delays by letting a system or user perform needed actions independently.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-25.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-25.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial, attribution required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Self-Service” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-25.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Self-Service",
  "description": "Reduce coordination cost and delays by letting a system or user perform needed actions independently.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-25/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Self-Service” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-25.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-25.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-25",
  "title": "Self-Service",
  "intent": "Reduce coordination cost and delays by letting a system or user perform needed actions independently.",
  "triz_principle": {
    "number": 25,
    "name": "Self-Service",
    "definition": "Make an object serve itself by performing auxiliary functions independently."
  },
  "problem_understanding": {
    "core_contradiction": "Centralized control ensures quality, but it creates queues, delays, and dependency on gatekeepers.",
    "why_this_hurts": "Every request waiting for approval or execution by another team increases lead time and frustration.",
    "typical_signals": [
      "tickets waiting in queues",
      "teams blocked by other teams",
      "manual interventions for routine tasks",
      "high coordination overhead for simple changes"
    ]
  },
  "solution_logic": {
    "core_idea": "Move routine actions closer to where the need arises.",
    "key_rule": "Centralize rules and guardrails, decentralize execution.",
    "how_it_resolves_the_contradiction": "Quality is preserved by constraints, while speed improves through autonomy."
  },
  "application_patterns": {
    "consulting": [
      "self-service analytics instead of central reporting teams",
      "decision playbooks enabling teams to act without escalation",
      "clear guardrails instead of case-by-case approvals"
    ],
    "software_engineering": [
      "self-service environment provisioning",
      "config-driven behavior changes",
      "developer portals for APIs and tooling"
    ],
    "architecture": [
      "platforms exposing self-service capabilities",
      "policy enforcement at the edges",
      "automation replacing manual coordination"
    ],
    "enterprise_sap": [
      "self-service master data requests with built-in validation",
      "business user–driven configuration within limits",
      "automated approvals for standard cases"
    ]
  },
  "anti_patterns": [
    "self-service without guardrails",
    "pushing complexity to users",
    "lack of auditability or rollback"
  ],
  "usage_guidance": {
    "use_when": [
      "requests are frequent and routine",
      "central teams are bottlenecks",
      "rules are well understood"
    ],
    "do_not_use_when": [
      "actions are rare but high-risk",
      "users lack necessary context or training"
    ]
  },
  "diagnostic_questions": [
    "Which requests are repetitive and predictable?",
    "What rules could replace manual approval?",
    "Where does waiting add no value?"
  ],
  "example": {
    "before": "Teams submit tickets for every small configuration change.",
    "after": "Teams adjust configurations themselves within predefined limits."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-25.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Self-Service” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-25.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-25.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-03-04T11:23:27+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Reduce coordination cost and delays by letting a system or user perform needed actions independently.",
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
