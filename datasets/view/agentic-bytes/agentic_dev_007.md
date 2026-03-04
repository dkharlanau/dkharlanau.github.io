---
layout: default
title: "Guardrails: What an Agent Is Never Allowed to Do"
description: "Learn how to define hard boundaries so an agent behaves safely, predictably, and does not overstep its authority."
permalink: /datasets/view/agentic-bytes/agentic_dev_007/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Guardrails: What an Agent Is Never Allowed to Do</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">agentic-bytes</span>
    <span class="pill pill--type">agentic_byte</span>
    <span class="pill">agentic_dev_007</span>
    <span class="pill">guardrails</span> <span class="pill">agent-safety</span> <span class="pill">control</span> <span class="pill">production-agents</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/agentic-bytes/agentic_dev_007.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/agentic-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Learn how to define hard boundaries so an agent behaves safely, predictably, and does not overstep its authority.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_007.json">https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_007.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial, attribution required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Guardrails: What an Agent Is Never Allowed to Do” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_007.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Guardrails: What an Agent Is Never Allowed to Do",
  "description": "Learn how to define hard boundaries so an agent behaves safely, predictably, and does not overstep its authority.",
  "url": "https://dkharlanau.github.io/datasets/view/agentic-bytes/agentic_dev_007/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Guardrails: What an Agent Is Never Allowed to Do” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_007.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_007.json"
    }
  ],
  "keywords": [
    "guardrails",
    "agent-safety",
    "control",
    "production-agents"
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "byte_id": "agentic_dev_007",
  "title": "Guardrails: What an Agent Is Never Allowed to Do",
  "level": "foundation",
  "domain": [
    "agentic-development",
    "safety",
    "reliability"
  ],
  "intent": "Learn how to define hard boundaries so an agent behaves safely, predictably, and does not overstep its authority.",
  "core_idea": {
    "one_liner": "Guardrails are not suggestions — they are hard limits on agent behavior.",
    "why_it_matters": [
      "LLMs optimize for helpfulness, not safety.",
      "Most real incidents happen because boundaries were implicit.",
      "Clear guardrails make agents trustworthy in production."
    ]
  },
  "definition": {
    "guardrail": "An explicit rule that restricts what an agent can say or do, regardless of user intent."
  },
  "core_guardrail_types": [
    {
      "type": "Action guardrails",
      "description": "Limit which tools can be used and in which situations.",
      "example": "Agent may read data but cannot write or delete records."
    },
    {
      "type": "Knowledge guardrails",
      "description": "Restrict answers to verified sources only.",
      "example": "If information is not found in RAG, the agent must say it does not know."
    },
    {
      "type": "Authority guardrails",
      "description": "Define when human approval is mandatory.",
      "example": "Any change affecting production requires human confirmation."
    },
    {
      "type": "Output guardrails",
      "description": "Enforce strict output formats and tone.",
      "example": "Agent must return valid JSON and no free text."
    }
  ],
  "common_guardrail_rules": [
    "Do not invent facts or tool results.",
    "Do not act outside assigned tools.",
    "Do not bypass required human approval.",
    "Do not answer outside defined domain or context.",
    "If uncertain, stop and ask or refuse."
  ],
  "micro_example": {
    "scenario": "User asks the agent to 'quickly fix production data'.",
    "agent_decision": {
      "guardrail_triggered": "Authority + Action guardrail",
      "response": "I cannot modify production data without explicit human approval. I can propose a fix plan instead."
    }
  },
  "failure_modes": [
    "Implicit guardrails (not written anywhere)",
    "Overly soft language ('try to avoid')",
    "Too many exceptions",
    "Guardrails enforced only in prompts, not in code"
  ],
  "implementation_levels": [
    {
      "level": "Prompt-level",
      "notes": "Useful but weakest; can be bypassed."
    },
    {
      "level": "Policy / middleware",
      "notes": "Checks inputs, outputs, and tool calls."
    },
    {
      "level": "System-level",
      "notes": "Hard enforcement (permissions, API scopes)."
    }
  ],
  "guards": [
    "Every critical action must map to an explicit guardrail.",
    "Guardrails must be testable.",
    "Violations must be logged."
  ],
  "teach_it_in_english": {
    "simple_explanation": "Guardrails tell the agent where the cliff is, so it never needs to find out by falling.",
    "one_sentence_definition": "Guardrails are the rules that protect users, systems, and the agent itself."
  },
  "practical_checklist": [
    "What actions are strictly forbidden?",
    "When must a human be involved?",
    "What should the agent do when unsure?",
    "Are guardrails enforced outside the prompt?"
  ],
  "tags": [
    "guardrails",
    "agent-safety",
    "control",
    "production-agents"
  ],
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "agentic-bytes",
    "source_project": "cv-ai",
    "source_path": "agentic-bytes/agentic_dev_007.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Guardrails: What an Agent Is Never Allowed to Do” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_007.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_007.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-03-04T11:23:27+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "agentic_byte",
    "entity_subtype": "level:foundation",
    "summary": "Learn how to define hard boundaries so an agent behaves safely, predictably, and does not overstep its authority.",
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
