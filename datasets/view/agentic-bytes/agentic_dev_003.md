---
layout: default
title: "Output Contracts: Why Agents Must Speak JSON"
description: "Understand why strict output formats (JSON schemas) are critical for building agents you can trust, debug, and automate."
permalink: /datasets/view/agentic-bytes/agentic_dev_003/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Output Contracts: Why Agents Must Speak JSON</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">agentic-bytes</span>
    <span class="pill pill--type">agentic_byte</span>
    <span class="pill">agentic_dev_003</span>
    <span class="pill">json-schema</span> <span class="pill">output-contracts</span> <span class="pill">agent-reliability</span> <span class="pill">automation</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/agentic-bytes/agentic_dev_003.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/agentic-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Understand why strict output formats (JSON schemas) are critical for building agents you can trust, debug, and automate.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_003.json">https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_003.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Output Contracts: Why Agents Must Speak JSON",
  "description": "Understand why strict output formats (JSON schemas) are critical for building agents you can trust, debug, and automate.",
  "url": "https://dkharlanau.github.io/datasets/view/agentic-bytes/agentic_dev_003/",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_003.json"
    }
  ],
  "keywords": [
    "json-schema",
    "output-contracts",
    "agent-reliability",
    "automation"
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "byte_id": "agentic_dev_003",
  "title": "Output Contracts: Why Agents Must Speak JSON",
  "level": "foundation",
  "domain": [
    "agentic-development",
    "output-contracts",
    "reliability"
  ],
  "intent": "Understand why strict output formats (JSON schemas) are critical for building agents you can trust, debug, and automate.",
  "core_idea": {
    "one_liner": "If an agent’s output is not structured and validated, it is not reliable.",
    "why_it_matters": [
      "Humans can tolerate vague text; systems cannot.",
      "JSON turns an agent from a narrator into a component.",
      "Validation prevents silent failures and misinterpretation."
    ]
  },
  "definition": {
    "output_contract": "A predefined, machine-readable structure that the agent must follow when producing results (usually JSON with a schema)."
  },
  "why_free_text_fails": [
    "Ambiguity: different readers interpret it differently.",
    "Parsing errors: downstream systems break.",
    "Hidden mistakes: errors are buried in prose.",
    "No guarantees: you cannot assert correctness."
  ],
  "what_a_good_contract_contains": [
    "Fixed field names",
    "Explicit data types",
    "Required vs optional fields",
    "Enumerations for allowed values",
    "Clear semantics for each field"
  ],
  "typical_use_cases": [
    "Classification (ticket type, severity, domain)",
    "Decision outputs (approve/reject/defer)",
    "Plans and step lists",
    "Diagnostics (root cause candidates)",
    "Mappings and translations"
  ],
  "example_contract": {
    "schema_description": "Ticket triage result",
    "json_schema_like": {
      "ticket_id": "string",
      "category": "one of [replication, data_quality, authorization, configuration]",
      "severity": "one of [low, medium, high, critical]",
      "confidence": "number between 0 and 1",
      "next_actions": [
        "string"
      ],
      "needs_human_review": "boolean"
    }
  },
  "agent_rules": [
    "The agent must not add extra fields.",
    "The agent must not change field meanings.",
    "If required data is missing, the agent must set a flag or return an explicit error object.",
    "No explanations outside the contract unless explicitly requested."
  ],
  "micro_example": {
    "scenario": "UAT defect classification",
    "bad_output": "This looks like a replication issue and is probably high priority.",
    "good_output": {
      "ticket_id": "UAT-431",
      "category": "replication",
      "severity": "high",
      "confidence": 0.82,
      "next_actions": [
        "Check DRF queue backlog",
        "Review recent replication errors"
      ],
      "needs_human_review": true
    }
  },
  "failure_modes": [
    "Schema drift (agent slowly changes structure)",
    "Overloaded fields (one field used for many meanings)",
    "False precision (fake confidence numbers)",
    "Mixing explanation text into structured output"
  ],
  "guards": [
    "Validate every output against schema.",
    "Reject or retry on validation failure.",
    "Version schemas explicitly (v1, v2)."
  ],
  "teach_it_in_english": {
    "simple_explanation": "JSON is a contract. It tells the agent: this is how you are allowed to speak.",
    "one_sentence_definition": "An output contract makes AI behavior predictable and safe."
  },
  "practical_checklist": [
    "Is the output machine-readable?",
    "Can I validate it automatically?",
    "Would two agents produce comparable outputs?",
    "Can I safely feed this into another system?"
  ],
  "tags": [
    "json-schema",
    "output-contracts",
    "agent-reliability",
    "automation"
  ],
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "agentic-bytes",
    "source_project": "cv-ai",
    "source_path": "agentic-bytes/agentic_dev_003.json",
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
    "canonical_url": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_003.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "agentic_byte",
    "entity_subtype": "level:foundation",
    "summary": "Understand why strict output formats (JSON schemas) are critical for building agents you can trust, debug, and automate."
  }
}
</code></pre>

</details>
</div>
