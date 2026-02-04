---
layout: default
title: "Plan → Execute: Separating Thinking from Doing"
description: "Learn why agents must separate planning from execution to stay controllable, debuggable, and safe."
permalink: /datasets/view/agentic-bytes/agentic_dev_009/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Plan → Execute: Separating Thinking from Doing</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">agentic-bytes</span>
    <span class="pill pill--type">agentic_byte</span>
    <span class="pill">agentic_dev_009</span>
    <span class="pill">plan-execute</span> <span class="pill">agent-control</span> <span class="pill">workflow</span> <span class="pill">reliability</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/agentic-bytes/agentic_dev_009.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/agentic-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Learn why agents must separate planning from execution to stay controllable, debuggable, and safe.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_009.json">https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_009.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Plan → Execute: Separating Thinking from Doing",
  "description": "Learn why agents must separate planning from execution to stay controllable, debuggable, and safe.",
  "url": "https://dkharlanau.github.io/datasets/view/agentic-bytes/agentic_dev_009/",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_009.json"
    }
  ],
  "keywords": [
    "plan-execute",
    "agent-control",
    "workflow",
    "reliability"
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "byte_id": "agentic_dev_009",
  "title": "Plan → Execute: Separating Thinking from Doing",
  "level": "foundation",
  "domain": [
    "agentic-development",
    "planning",
    "execution"
  ],
  "intent": "Learn why agents must separate planning from execution to stay controllable, debuggable, and safe.",
  "core_idea": {
    "one_liner": "If an agent plans and acts at the same time, you cannot trust or debug it.",
    "why_it_matters": [
      "Planning clarifies intent; execution changes state.",
      "Separation prevents accidental actions.",
      "You can review and approve plans before damage is done."
    ]
  },
  "definition": {
    "plan_execute_pattern": "An agent first produces an explicit plan, then executes it step by step, with checks in between."
  },
  "plan_phase": {
    "purpose": "Decide what to do without touching the real world.",
    "contains": [
      "Goal statement",
      "Ordered steps",
      "Required tools",
      "Expected outputs",
      "Decision points"
    ],
    "rules": [
      "No tool calls during planning.",
      "Plan must be short and reviewable.",
      "Plan must define what 'success' means."
    ]
  },
  "execute_phase": {
    "purpose": "Carry out the approved plan using tools.",
    "contains": [
      "Tool calls",
      "Intermediate results",
      "Error handling",
      "Progress tracking"
    ],
    "rules": [
      "Follow the plan strictly.",
      "Stop if assumptions are violated.",
      "Log every action."
    ]
  },
  "micro_example": {
    "scenario": "Investigate data mismatch after migration.",
    "plan": [
      "Identify affected objects and scope",
      "Compare source vs target key fields",
      "Check transformation rules",
      "Report root cause and fix options"
    ],
    "execute": [
      "Run comparison query",
      "Fetch transformation logs",
      "Generate discrepancy report"
    ]
  },
  "failure_modes": [
    "Implicit planning hidden in text",
    "Agent changing plan mid-execution without notice",
    "Executing without approval",
    "No clear stop condition"
  ],
  "guards": [
    "Plans must be explicit and reviewable.",
    "Execution without a plan is forbidden.",
    "Plan changes require re-approval."
  ],
  "teach_it_in_english": {
    "simple_explanation": "First decide what you will do. Only then do it.",
    "one_sentence_definition": "Plan–Execute separates intention from action."
  },
  "practical_checklist": [
    "Is the plan explicit?",
    "Can a human review it?",
    "Are tools only used in execution?",
    "Is success clearly defined?"
  ],
  "tags": [
    "plan-execute",
    "agent-control",
    "workflow",
    "reliability"
  ],
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "agentic-bytes",
    "source_project": "cv-ai",
    "source_path": "agentic-bytes/agentic_dev_009.json",
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
    "canonical_url": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_009.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "agentic_byte",
    "entity_subtype": "level:foundation",
    "summary": "Learn why agents must separate planning from execution to stay controllable, debuggable, and safe."
  }
}
</code></pre>

</details>
</div>
