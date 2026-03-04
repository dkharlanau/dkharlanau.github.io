---
layout: default
title: "Agent Interfaces &amp; Contracts: How Agents Communicate Safely"
description: "Understand how agents should communicate with other agents and systems using strict contracts instead of free text."
permalink: /datasets/view/agentic-bytes/agentic_dev_019/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Agent Interfaces &amp; Contracts: How Agents Communicate Safely</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">agentic-bytes</span>
    <span class="pill pill--type">agentic_byte</span>
    <span class="pill">agentic_dev_019</span>
    <span class="pill">agent-interfaces</span> <span class="pill">contracts</span> <span class="pill">multi-agent</span> <span class="pill">architecture</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/agentic-bytes/agentic_dev_019.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/agentic-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Understand how agents should communicate with other agents and systems using strict contracts instead of free text.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_019.json">https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_019.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial, attribution required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Agent Interfaces &amp; Contracts: How Agents Communicate Safely” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_019.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Agent Interfaces & Contracts: How Agents Communicate Safely",
  "description": "Understand how agents should communicate with other agents and systems using strict contracts instead of free text.",
  "url": "https://dkharlanau.github.io/datasets/view/agentic-bytes/agentic_dev_019/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Agent Interfaces & Contracts: How Agents Communicate Safely” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_019.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_019.json"
    }
  ],
  "keywords": [
    "agent-interfaces",
    "contracts",
    "multi-agent",
    "architecture"
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "byte_id": "agentic_dev_019",
  "title": "Agent Interfaces &amp; Contracts: How Agents Communicate Safely",
  "level": "applied",
  "domain": [
    "agentic-development",
    "architecture",
    "interfaces"
  ],
  "intent": "Understand how agents should communicate with other agents and systems using strict contracts instead of free text.",
  "core_idea": {
    "one_liner": "Agents must talk like APIs, not like humans.",
    "why_it_matters": [
      "Free text breaks coordination.",
      "Contracts make agent interactions debuggable.",
      "Clear interfaces prevent cascading failures."
    ]
  },
  "definition": {
    "agent_interface": "A formally defined input/output contract that governs how an agent receives requests and returns results."
  },
  "interface_principles": [
    "Structured inputs and outputs only",
    "Explicit success and failure states",
    "No hidden assumptions",
    "Backward compatibility where possible"
  ],
  "typical_interface_fields": [
    "request_id",
    "intent",
    "inputs",
    "constraints",
    "expected_output",
    "confidence",
    "status"
  ],
  "agent_to_agent_contract_example": {
    "request": {
      "request_id": "REQ-1021",
      "intent": "analyze_replication_issue",
      "inputs": {
        "system": "MDG-S4",
        "object": "BP",
        "symptom": "delay"
      },
      "constraints": {
        "read_only": true
      }
    },
    "response": {
      "request_id": "REQ-1021",
      "status": "completed",
      "result": {
        "root_cause": "queue_backlog",
        "confidence": 0.81
      }
    }
  },
  "micro_example": {
    "scenario": "Planner agent delegates to RCA agent",
    "bad": "Hey, can you check why this is slow?",
    "good": "Structured request with intent, scope, and constraints."
  },
  "failure_modes": [
    "Free-text delegation",
    "Implicit context sharing",
    "Changing contracts without versioning",
    "Overloading one interface with multiple meanings"
  ],
  "guards": [
    "All agent interactions must use contracts.",
    "Contracts must be versioned.",
    "Validation is mandatory before execution."
  ],
  "teach_it_in_english": {
    "simple_explanation": "Agents should communicate the same way services do.",
    "one_sentence_definition": "Agent interfaces turn cooperation into engineering."
  },
  "practical_checklist": [
    "Is the message machine-readable?",
    "Can it be validated automatically?",
    "Is failure explicitly represented?",
    "Can this interface evolve safely?"
  ],
  "tags": [
    "agent-interfaces",
    "contracts",
    "multi-agent",
    "architecture"
  ],
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "agentic-bytes",
    "source_project": "cv-ai",
    "source_path": "agentic-bytes/agentic_dev_019.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Agent Interfaces &amp; Contracts: How Agents Communicate Safely” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_019.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_019.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-03-04T11:23:27+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "agentic_byte",
    "entity_subtype": "level:applied",
    "summary": "Understand how agents should communicate with other agents and systems using strict contracts instead of free text.",
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
