---
layout: default
title: "Ownership, SLAs &amp; Accountability: Who Is Responsible for the Agent"
description: "Understand how to assign clear ownership and service expectations so agents can be operated like real systems, not experiments."
permalink: /datasets/view/agentic-bytes/agentic_dev_020/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Ownership, SLAs &amp; Accountability: Who Is Responsible for the Agent</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">agentic-bytes</span>
    <span class="pill pill--type">agentic_byte</span>
    <span class="pill">agentic_dev_020</span>
    <span class="pill">ownership</span> <span class="pill">sla</span> <span class="pill">accountability</span> <span class="pill">operations</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/agentic-bytes/agentic_dev_020.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/agentic-bytes/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Understand how to assign clear ownership and service expectations so agents can be operated like real systems, not experiments.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_020.json">https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_020.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Ownership, SLAs & Accountability: Who Is Responsible for the Agent",
  "description": "Understand how to assign clear ownership and service expectations so agents can be operated like real systems, not experiments.",
  "url": "https://dkharlanau.github.io/datasets/view/agentic-bytes/agentic_dev_020/",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_020.json"
    }
  ],
  "keywords": [
    "ownership",
    "sla",
    "accountability",
    "operations"
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "byte_id": "agentic_dev_020",
  "title": "Ownership, SLAs &amp; Accountability: Who Is Responsible for the Agent",
  "level": "applied",
  "domain": [
    "agentic-development",
    "operations",
    "governance"
  ],
  "intent": "Understand how to assign clear ownership and service expectations so agents can be operated like real systems, not experiments.",
  "core_idea": {
    "one_liner": "If nobody owns the agent, nobody is responsible for its mistakes.",
    "why_it_matters": [
      "Agents affect real decisions and systems.",
      "Incidents require clear escalation paths.",
      "Without SLAs, quality degrades silently."
    ]
  },
  "definition": {
    "agent_ownership": "Explicit assignment of responsibility for an agent’s behavior, quality, and lifecycle.",
    "sla": "Agreed expectations for availability, accuracy, latency, and escalation."
  },
  "ownership_roles": [
    {
      "role": "Product owner",
      "responsibility": "Defines agent scope, value, and success criteria."
    },
    {
      "role": "Technical owner",
      "responsibility": "Ensures reliability, observability, and cost control."
    },
    {
      "role": "Domain owner",
      "responsibility": "Validates knowledge correctness and updates."
    }
  ],
  "agent_sla_dimensions": [
    {
      "dimension": "Availability",
      "example": "99.5% uptime for support hours"
    },
    {
      "dimension": "Latency",
      "example": "P95 response time &lt; 5 seconds"
    },
    {
      "dimension": "Accuracy",
      "example": "≥ 90% correct classification on golden set"
    },
    {
      "dimension": "Escalation",
      "example": "Human handoff within 10 minutes for critical cases"
    }
  ],
  "incident_handling": [
    "Detect via metrics or user report",
    "Identify agent version and knowledge set",
    "Trigger fallback or disable capability",
    "Notify owner and stakeholders",
    "Post-incident review and update evals"
  ],
  "micro_example": {
    "scenario": "Agent gives wrong recommendation in production",
    "response": {
      "owner_identified": "Technical owner",
      "action": "Disable affected decision path",
      "follow_up": "Update knowledge version and rerun evals"
    }
  },
  "failure_modes": [
    "Shared ownership (everyone and no one)",
    "No SLA for accuracy",
    "Incidents treated as 'AI quirks'",
    "No post-incident learning"
  ],
  "guards": [
    "Every agent must have named owners.",
    "SLAs must be measurable.",
    "Incidents must lead to changes."
  ],
  "teach_it_in_english": {
    "simple_explanation": "Agents need owners just like services do.",
    "one_sentence_definition": "Ownership turns AI from a toy into a system."
  },
  "practical_checklist": [
    "Who is on call for this agent?",
    "What does 'good enough' mean?",
    "How do we escalate failures?",
    "Do incidents improve the agent?"
  ],
  "tags": [
    "ownership",
    "sla",
    "accountability",
    "operations"
  ],
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "agentic-bytes",
    "source_project": "cv-ai",
    "source_path": "agentic-bytes/agentic_dev_020.json",
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
    "canonical_url": "https://dkharlanau.github.io/datasets/agentic-bytes/agentic_dev_020.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "agentic_byte",
    "entity_subtype": "level:applied",
    "summary": "Understand how to assign clear ownership and service expectations so agents can be operated like real systems, not experiments."
  }
}
</code></pre>

</details>
</div>
