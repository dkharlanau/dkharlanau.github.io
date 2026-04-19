---
layout: default
title: "Chunking: How Knowledge Must Be Cut for RAG"
description: "Learn how to structure knowledge so an agent can reliably retrieve and use it without confusion or hallucination."
permalink: /datasets/view/agentic-bytes/agentic_dev_004/
sitemap: true
last_modified_at: 2026-04-13T08:37:04+00:00
dataset_detail_page: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Chunking: How Knowledge Must Be Cut for RAG</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">agentic-bytes</span>
    <span class="pill pill--type">agentic_byte</span>
    <span class="pill">agentic_dev_004</span>
    <span class="pill">rag</span> <span class="pill">chunking</span> <span class="pill">knowledge-design</span> <span class="pill">retrieval-quality</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/agentic-bytes/agentic_dev_004.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/agentic-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Learn how to structure knowledge so an agent can reliably retrieve and use it without confusion or hallucination.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_004.json">https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_004.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial only, attribution with source link required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Chunking: How Knowledge Must Be Cut for RAG” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_004.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Chunking: How Knowledge Must Be Cut for RAG",
  "description": "Learn how to structure knowledge so an agent can reliably retrieve and use it without confusion or hallucination.",
  "url": "https://dkharlanau.github.io/datasets/view/agentic-bytes/agentic_dev_004/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Chunking: How Knowledge Must Be Cut for RAG” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_004.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_004.json"
    }
  ],
  "keywords": [
    "rag",
    "chunking",
    "knowledge-design",
    "retrieval-quality"
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "byte_id": "agentic_dev_004",
  "title": "Chunking: How Knowledge Must Be Cut for RAG",
  "level": "foundation",
  "domain": [
    "agentic-development",
    "rag",
    "knowledge-engineering"
  ],
  "intent": "Learn how to structure knowledge so an agent can reliably retrieve and use it without confusion or hallucination.",
  "core_idea": {
    "one_liner": "RAG does not fail because of models — it fails because of bad chunking.",
    "why_it_matters": [
      "The model can only reason over what it retrieves.",
      "Poor chunking causes partial context and wrong conclusions.",
      "Good chunks turn documents into reusable knowledge units."
    ]
  },
  "definition": {
    "chunk": "A self-contained unit of knowledge that can be retrieved and understood independently."
  },
  "golden_rules": [
    "One chunk = one idea.",
    "A chunk must make sense without neighboring text.",
    "If you cannot explain a chunk in 30 seconds, it is too big."
  ],
  "recommended_chunk_sizes": {
    "concepts": "150–300 tokens",
    "procedures_checklists": "200–400 tokens",
    "decision_rules": "100–250 tokens",
    "reference_tables": "as rows, not prose blocks"
  },
  "bad_chunking_patterns": [
    "Splitting by fixed token size only",
    "Cutting mid-sentence or mid-idea",
    "One chunk covering multiple decisions",
    "Large narrative documents with no internal structure"
  ],
  "good_chunking_patterns": [
    "Semantic boundaries (concept, rule, checklist, example)",
    "Stable templates (same fields every time)",
    "Explicit titles and summaries per chunk"
  ],
  "agent_friendly_templates": [
    "Decision Byte",
    "Anti-pattern Byte",
    "Checklist Byte",
    "Mapping Byte",
    "RCA Byte"
  ],
  "micro_example": {
    "scenario": "MDG replication troubleshooting guide",
    "bad_chunk": "10 pages covering queues, errors, mappings, governance mixed together.",
    "good_chunks": [
      "Queue backlog diagnosis",
      "Web service error patterns",
      "Value mapping failures",
      "Authorization-related replication blocks"
    ]
  },
  "retrieval_failure_modes": [
    "Right document, wrong chunk",
    "Partial rule without conditions",
    "Example retrieved without explanation",
    "Conflicting chunks retrieved together"
  ],
  "guards": [
    "Each chunk must have a title and intent.",
    "Chunks must be versioned when meaning changes.",
    "Never mix procedures and opinions in the same chunk."
  ],
  "teach_it_in_english": {
    "simple_explanation": "Chunking is like cutting a book into index cards that still make sense on their own.",
    "one_sentence_definition": "A good chunk is the smallest unit of knowledge that still tells the whole truth."
  },
  "practical_checklist": [
    "Does this chunk answer one clear question?",
    "Can it stand alone without other chunks?",
    "Is its size appropriate for retrieval?",
    "Would I reuse this chunk in another agent?"
  ],
  "tags": [
    "rag",
    "chunking",
    "knowledge-design",
    "retrieval-quality"
  ],
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "agentic-bytes",
    "source_project": "cv-ai",
    "source_path": "agentic-bytes/agentic_dev_004.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Chunking: How Knowledge Must Be Cut for RAG” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_004.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_004.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-04-13T08:37:04+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "agentic_byte",
    "entity_subtype": "level:foundation",
    "summary": "Learn how to structure knowledge so an agent can reliably retrieve and use it without confusion or hallucination.",
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
