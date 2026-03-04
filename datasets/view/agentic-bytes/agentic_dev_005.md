---
layout: default
title: "Metadata: Teaching Agents What a Chunk Is About"
description: "Understand how metadata turns raw text chunks into navigable, filterable, and trustworthy knowledge for agents."
permalink: /datasets/view/agentic-bytes/agentic_dev_005/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Metadata: Teaching Agents What a Chunk Is About</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">agentic-bytes</span>
    <span class="pill pill--type">agentic_byte</span>
    <span class="pill">agentic_dev_005</span>
    <span class="pill">metadata</span> <span class="pill">rag</span> <span class="pill">knowledge-governance</span> <span class="pill">agent-control</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/agentic-bytes/agentic_dev_005.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/agentic-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Understand how metadata turns raw text chunks into navigable, filterable, and trustworthy knowledge for agents.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_005.json">https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_005.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial only, attribution with source link required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Metadata: Teaching Agents What a Chunk Is About” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_005.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Metadata: Teaching Agents What a Chunk Is About",
  "description": "Understand how metadata turns raw text chunks into navigable, filterable, and trustworthy knowledge for agents.",
  "url": "https://dkharlanau.github.io/datasets/view/agentic-bytes/agentic_dev_005/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Metadata: Teaching Agents What a Chunk Is About” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_005.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_005.json"
    }
  ],
  "keywords": [
    "metadata",
    "rag",
    "knowledge-governance",
    "agent-control"
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "byte_id": "agentic_dev_005",
  "title": "Metadata: Teaching Agents What a Chunk Is About",
  "level": "foundation",
  "domain": [
    "agentic-development",
    "rag",
    "metadata"
  ],
  "intent": "Understand how metadata turns raw text chunks into navigable, filterable, and trustworthy knowledge for agents.",
  "core_idea": {
    "one_liner": "Without metadata, RAG is blind; with metadata, it can reason.",
    "why_it_matters": [
      "Vectors give similarity, metadata gives control.",
      "Agents must know context, scope, and freshness.",
      "Good metadata reduces hallucinations and wrong retrieval."
    ]
  },
  "definition": {
    "metadata": "Structured attributes attached to a chunk that describe its meaning, scope, origin, and validity."
  },
  "must_have_metadata": [
    {
      "field": "domain",
      "purpose": "Logical area (e.g. SAP, MDG, agentic-dev, data-quality)."
    },
    {
      "field": "system_or_context",
      "purpose": "Which system or environment it applies to (S/4, MDG, BTP, generic)."
    },
    {
      "field": "type",
      "purpose": "Decision, checklist, anti-pattern, concept, RCA, mapping."
    },
    {
      "field": "version",
      "purpose": "Knowledge evolves; agents must prefer newer versions."
    },
    {
      "field": "validity",
      "purpose": "Is it current, deprecated, or conditional?"
    }
  ],
  "optional_but_powerful_metadata": [
    "process (O2C, P2P, MDG, UAT, Cutover)",
    "risk_level (low/medium/high)",
    "confidence (expert-verified vs heuristic)",
    "owner (who is responsible for this knowledge)",
    "last_reviewed_date"
  ],
  "how_agents_use_metadata": [
    "Filter chunks before vector search (reduce noise).",
    "Resolve conflicts (prefer higher version or confidence).",
    "Ask follow-up questions when validity is conditional.",
    "Explain answers with proper scope ('this applies to S/4 only')."
  ],
  "micro_example": {
    "chunk_title": "MDG BP Replication – Queue Backlog Diagnosis",
    "metadata_example": {
      "domain": "SAP",
      "system_or_context": "MDG-S/4",
      "type": "RCA",
      "process": "Master Data Replication",
      "version": "1.2",
      "validity": "current",
      "risk_level": "high"
    }
  },
  "failure_modes_without_metadata": [
    "Correct chunk retrieved in wrong context",
    "Outdated rules mixed with current ones",
    "Generic advice applied to regulated scenarios",
    "Agent overconfident in heuristic knowledge"
  ],
  "guards": [
    "Every chunk must have minimum metadata.",
    "Version bumps are mandatory on semantic change.",
    "Deprecated chunks must not be deleted silently."
  ],
  "teach_it_in_english": {
    "simple_explanation": "Metadata tells the agent when, where, and how a piece of knowledge is allowed to be used.",
    "one_sentence_definition": "Metadata is the difference between remembering and understanding."
  },
  "practical_checklist": [
    "Can the agent filter this chunk correctly?",
    "Is the scope explicit?",
    "Is the version and freshness clear?",
    "Would a wrong context make this advice dangerous?"
  ],
  "tags": [
    "metadata",
    "rag",
    "knowledge-governance",
    "agent-control"
  ],
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "agentic-bytes",
    "source_project": "cv-ai",
    "source_path": "agentic-bytes/agentic_dev_005.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Metadata: Teaching Agents What a Chunk Is About” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_005.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_005.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-03-04T19:03:44+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "agentic_byte",
    "entity_subtype": "level:foundation",
    "summary": "Understand how metadata turns raw text chunks into navigable, filterable, and trustworthy knowledge for agents.",
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
