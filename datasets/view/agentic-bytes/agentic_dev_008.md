---
layout: default
title: "Self-Check / Critic: Teaching Agents to Verify Themselves"
description: "Understand how to add an explicit self-check step so agents catch their own mistakes before users do."
permalink: /datasets/view/agentic-bytes/agentic_dev_008/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Self-Check / Critic: Teaching Agents to Verify Themselves</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">agentic-bytes</span>
    <span class="pill pill--type">agentic_byte</span>
    <span class="pill">agentic_dev_008</span>
    <span class="pill">self-check</span> <span class="pill">critic</span> <span class="pill">verification</span> <span class="pill">hallucination-control</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/agentic-bytes/agentic_dev_008.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/agentic-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Understand how to add an explicit self-check step so agents catch their own mistakes before users do.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_008.json">https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_008.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Self-Check / Critic: Teaching Agents to Verify Themselves",
  "description": "Understand how to add an explicit self-check step so agents catch their own mistakes before users do.",
  "url": "https://dkharlanau.github.io/datasets/view/agentic-bytes/agentic_dev_008/",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_008.json"
    }
  ],
  "keywords": [
    "self-check",
    "critic",
    "verification",
    "hallucination-control"
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "byte_id": "agentic_dev_008",
  "title": "Self-Check / Critic: Teaching Agents to Verify Themselves",
  "level": "foundation",
  "domain": [
    "agentic-development",
    "verification",
    "reliability"
  ],
  "intent": "Understand how to add an explicit self-check step so agents catch their own mistakes before users do.",
  "core_idea": {
    "one_liner": "A good agent does not trust its first answer.",
    "why_it_matters": [
      "LLMs are confident even when wrong.",
      "Most failures are obvious in hindsight but unchecked.",
      "A critic step dramatically reduces hallucinations."
    ]
  },
  "definition": {
    "self_check": "A deliberate verification step where the agent reviews its own output against rules, evidence, and constraints."
  },
  "self_check_patterns": [
    {
      "pattern": "Same-model critic",
      "description": "The same model reviews its own output using a different prompt.",
      "pros": [
        "Cheap",
        "Easy to implement"
      ],
      "cons": [
        "Limited independence"
      ]
    },
    {
      "pattern": "Role-based critic",
      "description": "The agent switches to a 'critic' role with strict evaluation criteria.",
      "pros": [
        "Clear separation of concerns"
      ],
      "cons": [
        "Still same model"
      ]
    },
    {
      "pattern": "Second-model critic",
      "description": "A different model reviews the output.",
      "pros": [
        "Higher independence"
      ],
      "cons": [
        "Higher cost"
      ]
    }
  ],
  "what_the_critic_checks": [
    "Did we actually answer the question?",
    "Are all claims supported by retrieved knowledge or tool outputs?",
    "Does the output follow the contract (schema, tone, scope)?",
    "Are there contradictions or unsupported assumptions?"
  ],
  "micro_example": {
    "scenario": "Agent generates RCA for slow replication.",
    "self_check_questions": [
      "Did I confirm the root cause or just list possibilities?",
      "Did I use real evidence from tools?",
      "Am I overstating confidence?"
    ],
    "critic_outcome": "Requests additional queue metrics before final answer."
  },
  "failure_modes": [
    "Fake self-check ('looks good')",
    "Critic ignored when inconvenient",
    "No action taken after failed check",
    "Critic allowed to invent new facts"
  ],
  "guards": [
    "Critic cannot add new facts, only flag issues.",
    "Failed self-check must block final answer.",
    "Self-check output must be structured."
  ],
  "teach_it_in_english": {
    "simple_explanation": "The agent pauses and asks: 'How could this be wrong?'",
    "one_sentence_definition": "A self-check turns confidence into reliability."
  },
  "practical_checklist": [
    "Is there an explicit verification step?",
    "Are claims tied to evidence?",
    "Can the agent say 'not enough data'?",
    "Is the critic allowed to stop the workflow?"
  ],
  "tags": [
    "self-check",
    "critic",
    "verification",
    "hallucination-control"
  ],
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "agentic-bytes",
    "source_project": "cv-ai",
    "source_path": "agentic-bytes/agentic_dev_008.json",
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
    "canonical_url": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_008.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "agentic_byte",
    "entity_subtype": "level:foundation",
    "summary": "Understand how to add an explicit self-check step so agents catch their own mistakes before users do."
  }
}
</code></pre>

</details>
</div>
