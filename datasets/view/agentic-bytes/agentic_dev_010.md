---
layout: default
title: "Human-in-the-Loop: Where Agents Must Stop and Ask"
description: "Understand where and why an agent must defer to a human, and how to design clear handoff points."
permalink: /datasets/view/agentic-bytes/agentic_dev_010/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Human-in-the-Loop: Where Agents Must Stop and Ask</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">agentic-bytes</span>
    <span class="pill pill--type">agentic_byte</span>
    <span class="pill">agentic_dev_010</span>
    <span class="pill">human-in-the-loop</span> <span class="pill">governance</span> <span class="pill">agent-autonomy</span> <span class="pill">trust</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/agentic-bytes/agentic_dev_010.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/agentic-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Understand where and why an agent must defer to a human, and how to design clear handoff points.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_010.json">https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_010.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Human-in-the-Loop: Where Agents Must Stop and Ask",
  "description": "Understand where and why an agent must defer to a human, and how to design clear handoff points.",
  "url": "https://dkharlanau.github.io/datasets/view/agentic-bytes/agentic_dev_010/",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_010.json"
    }
  ],
  "keywords": [
    "human-in-the-loop",
    "governance",
    "agent-autonomy",
    "trust"
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "byte_id": "agentic_dev_010",
  "title": "Human-in-the-Loop: Where Agents Must Stop and Ask",
  "level": "foundation",
  "domain": [
    "agentic-development",
    "governance",
    "human-in-the-loop"
  ],
  "intent": "Understand where and why an agent must defer to a human, and how to design clear handoff points.",
  "core_idea": {
    "one_liner": "Autonomy without checkpoints is a liability.",
    "why_it_matters": [
      "Some decisions are contextual, political, or risky.",
      "Humans provide accountability, not just intelligence.",
      "Well-placed handoffs increase trust and adoption."
    ]
  },
  "definition": {
    "human_in_the_loop": "A mandatory pause where the agent presents its findings or plan and waits for human approval or input."
  },
  "when_humans_are_required": [
    "Actions that modify production data",
    "High-risk or irreversible decisions",
    "Ambiguous requirements or conflicting goals",
    "Low-confidence outputs",
    "Legal, financial, or compliance-sensitive areas"
  ],
  "handoff_patterns": [
    {
      "pattern": "Plan approval",
      "description": "Agent proposes a plan and waits for approval before execution."
    },
    {
      "pattern": "Decision confirmation",
      "description": "Agent suggests a decision with pros/cons; human selects."
    },
    {
      "pattern": "Exception escalation",
      "description": "Agent stops when encountering undefined or forbidden cases."
    }
  ],
  "what_the_agent_must_present": [
    "Context summary",
    "Proposed action or decision",
    "Alternatives",
    "Risks and trade-offs",
    "Confidence level"
  ],
  "micro_example": {
    "scenario": "Agent identifies need to correct master data values.",
    "agent_output": {
      "proposal": "Apply value mapping fix to 1,200 records.",
      "risk": "May affect downstream billing.",
      "confidence": 0.74,
      "request": "Approve execution or request changes."
    }
  },
  "failure_modes": [
    "No clear handoff point",
    "Human approval requested too late",
    "Overusing humans for trivial steps",
    "Ignoring human feedback"
  ],
  "guards": [
    "Handoff points must be explicit.",
    "Agent must not proceed without approval.",
    "Human feedback must be recorded."
  ],
  "teach_it_in_english": {
    "simple_explanation": "The agent knows when to stop and ask for permission.",
    "one_sentence_definition": "Human-in-the-loop is how responsibility stays human."
  },
  "practical_checklist": [
    "Where can this go wrong?",
    "Who is accountable?",
    "Is the handoff early enough?",
    "Does the agent resume correctly after approval?"
  ],
  "tags": [
    "human-in-the-loop",
    "governance",
    "agent-autonomy",
    "trust"
  ],
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "agentic-bytes",
    "source_project": "cv-ai",
    "source_path": "agentic-bytes/agentic_dev_010.json",
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
    "canonical_url": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_010.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "agentic_byte",
    "entity_subtype": "level:foundation",
    "summary": "Understand where and why an agent must defer to a human, and how to design clear handoff points."
  }
}
</code></pre>

</details>
</div>
