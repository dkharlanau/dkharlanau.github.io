---
layout: default
title: "Evaluation and Guardrails"
description: "Define task-specific AI acceptance tests and runtime controls, then track failures and re-evaluate material system changes."
permalink: /atlas/sap/evaluation-guardrails/
atlas_section: sap
domain: SAP operations
subdomain: AI and agentic technologies
concept_type: technology
sap_area: "AI Guardrails"
business_process: "AI-assisted operations"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
last_modified_at: 2026-10-07
author: Dzmitryi Kharlanau

tags:
  - ai-guardrails
  - ai-evaluation
  - responsible-ai
related:
  - /atlas/sap/ai-agents/
  - /atlas/sap/sap-joule/
  - /atlas/sap/sap-business-ai/
  - /atlas/sap/human-approval-workflows/
  - /atlas/sap/rag/
  - /atlas/ai-operations/ai-agent-for-sap-support/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Evaluation and Guardrails</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>Evaluation and Guardrails</h1>
    <p class="note-subtitle">Measure AI quality separately from the controls that constrain runtime behavior.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>AI-assisted operations</dd></div>
      <div><dt>SAP area</dt><dd>AI Guardrails</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until verified against current SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p><strong>Evaluation</strong> tests whether an AI system performs a defined task well enough. <strong>Guardrails</strong> constrain what it can read, return, or do at runtime. Better answers do not remove authorization risk; stricter filters do not prove that answers are correct.</p>

    <h2>Define acceptance in business terms</h2>
    <p>For a support assistant, check the SAP object, diagnosis, evidence, and next action. For a write-capable agent, also check the resulting business state and whether forbidden operations were rejected. Choose thresholds for the task's consequences instead of reporting one undefined “accuracy” score.</p>
    <ul>
      <li><strong>Normal case:</strong> the expected task completes with relevant evidence.</li>
      <li><strong>Missing or stale data:</strong> the system explains the gap or escalates instead of inventing certainty.</li>
      <li><strong>Different permissions:</strong> retrieval and tools enforce the caller's allowed scope.</li>
      <li><strong>Ambiguous or hostile input:</strong> the system asks, refuses, or stays within the supported task.</li>
      <li><strong>Backend error or duplicate request:</strong> it preserves known state and avoids unsafe repetition.</li>
    </ul>
    <p><strong>Synthetic test:</strong> run the same diagnostic question under two roles with different plant access. A correct diagnosis still fails the test if the restricted role receives evidence it may not read.</p>

    <h2>Put each control where it can be enforced</h2>
    <ul>
      <li><strong>Input and retrieval:</strong> validate scope, limit data access, handle prompt injection, and mask data where needed.</li>
      <li><strong>Output:</strong> check schema, evidence, content, and business rules.</li>
      <li><strong>Tools:</strong> enforce allowed operations, parameters, authorization, rate limits, and duplicate protection.</li>
      <li><strong>Business actions:</strong> apply required approval, separation of duties, reconciliation, and recovery.</li>
    </ul>
    <p>SAP's <a href="https://help.sap.com/doc/generative-ai-hub-sdk/CLOUD/en-US/_reference/orchestration-service2.html">Orchestration Service V2 documentation</a> describes masking and content-filtering modules. These address specific model-call risks; they do not establish permission to change an ERP object. Use the <a href="/atlas/sap/human-approval-workflows/">approval pattern</a> for the human decision boundary.</p>

    <h2>Keep test evidence useful after release</h2>
    <p>Use fixed offline cases to compare changes, then monitor production corrections, escalations, and business results. Separate retrieval errors, tool failures, policy blocks, validation failures, and successful completion so each has a clear owner.</p>
    <p>Record the tested model, prompt, retrieval sources, tools, and backend assumptions. Re-run affected tests after a material change to any of them or to the work arriving in production. An unchanged prompt can still fail after an API or authorization change.</p>
    <p><a href="https://help.sap.com/docs/ai-launchpad/sap-ai-launchpad/view-evaluations?version=CLOUD">SAP AI Launchpad evaluation views</a> expose run details, metrics, and tags, subject to documented roles and service-plan prerequisites. They expose evaluation evidence; the team still defines acceptance criteria. Leave the review with test cases, expected results, failure owners, and a release decision. Product-specific features require current documentation and tenant checks.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/ai-agents/">AI Agents</a></li>
      <li><a href="/atlas/sap/agent-workflows/">Agent Workflows</a></li>
      <li><a href="/atlas/sap/human-approval-workflows/">Human Approval Workflows</a></li>
      <li><a href="/atlas/sap/rag/">RAG</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
