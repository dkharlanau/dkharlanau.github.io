---
layout: default
title: "Nested Doll"
description: "Manage complexity by placing systems or components inside others, creating clear containment and layered responsibility."
permalink: /datasets/view/TRIZ-bytes/TRIZ-07/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Nested Doll</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">TRIZ-bytes</span>
    <span class="pill pill--type">triz_byte</span>
    <span class="pill">TRIZ-07</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/TRIZ-bytes/TRIZ-07.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/TRIZ-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Manage complexity by placing systems or components inside others, creating clear containment and layered responsibility.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-07.json">https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-07.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial only, attribution with source link required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Nested Doll” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-07.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Nested Doll",
  "description": "Manage complexity by placing systems or components inside others, creating clear containment and layered responsibility.",
  "url": "https://dkharlanau.github.io/datasets/view/TRIZ-bytes/TRIZ-07/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Nested Doll” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-07.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-07.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "TRIZ-07",
  "title": "Nested Doll",
  "intent": "Manage complexity by placing systems or components inside others, creating clear containment and layered responsibility.",
  "triz_principle": {
    "number": 7,
    "name": "Nested Doll",
    "definition": "Place one object inside another; make a system of nested structures."
  },
  "problem_understanding": {
    "core_contradiction": "We need to handle growing complexity, but exposing everything at the same level overwhelms teams and systems.",
    "why_this_hurts": "Flat architectures force everyone to understand too much; changes ripple unpredictably across layers.",
    "typical_signals": [
      "everything is visible to everyone",
      "no clear abstraction levels",
      "developers must understand the whole system to change a part",
      "configuration and logic mixed together"
    ]
  },
  "solution_logic": {
    "core_idea": "Introduce containment and layers so each level deals only with its own concerns.",
    "key_rule": "Each layer exposes a simple interface and hides its internal complexity.",
    "how_it_resolves_the_contradiction": "Local reasoning becomes possible while the system still works as a coherent whole."
  },
  "application_patterns": {
    "consulting": [
      "embed local initiatives inside a global program framework",
      "define strategy → policy → execution layers",
      "package complex decisions into reusable playbooks"
    ],
    "software_engineering": [
      "wrap complex logic into modules with simple APIs",
      "use facades to hide internal workflows",
      "nest configurations: defaults → overrides → local tweaks"
    ],
    "architecture": [
      "layered architecture with clear responsibility per layer",
      "platform → product → feature nesting",
      "infrastructure abstractions over cloud/provider specifics"
    ],
    "enterprise_sap": [
      "global templates containing local extensions",
      "MDG change requests wrapping object-specific validations",
      "configuration hierarchies: global → company code → plant"
    ]
  },
  "anti_patterns": [
    "leaky abstractions between layers",
    "deep nesting with no clear ownership",
    "layers that only forward calls without adding value"
  ],
  "usage_guidance": {
    "use_when": [
      "system understanding requires too much context",
      "changes propagate unpredictably",
      "you need safe local variation within global rules"
    ],
    "do_not_use_when": [
      "nesting adds indirection without reducing complexity",
      "performance-critical paths cannot tolerate extra layers"
    ]
  },
  "diagnostic_questions": [
    "What complexity could be hidden behind a stable interface?",
    "Which responsibilities should belong to a higher or lower layer?",
    "Where do teams need protection from internal details?"
  ],
  "example": {
    "before": "Business rules, configuration, and technical logic are mixed in the same code paths.",
    "after": "Business rules are wrapped in a rule module, configuration is layered, and technical execution is hidden behind a facade."
  },
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "TRIZ-bytes",
    "source_project": "cv-ai",
    "source_path": "TRIZ-bytes/TRIZ-07.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Nested Doll” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-07.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/TRIZ-bytes/TRIZ-07.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-03-04T11:23:27+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "triz_byte",
    "entity_subtype": "",
    "summary": "Manage complexity by placing systems or components inside others, creating clear containment and layered responsibility.",
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
