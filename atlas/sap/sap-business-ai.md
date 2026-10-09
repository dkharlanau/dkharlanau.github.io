---
layout: default
title: "SAP Business AI"
description: "Separate embedded SAP AI capabilities, Joule interactions, and custom AI services to identify the owner, controls, and limits of an implementation."
permalink: /atlas/sap/sap-business-ai/
atlas_section: sap
domain: SAP operations
subdomain: AI and agentic technologies
concept_type: technology
sap_area: "SAP Business AI"
business_process: "AI-assisted operations"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
last_modified_at: 2026-10-07
author: Dzmitryi Kharlanau

tags:
  - sap-business-ai
  - generative-ai
  - btp-ai
related:
  - /atlas/sap/sap-joule/
  - /atlas/sap/ai-agents/
  - /atlas/sap/rag/
  - /atlas/sap/sap-btp/
  - /atlas/sap/sap-s4hana/
  - /atlas/ai-operations/ai-agent-for-sap-support/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Business AI</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>SAP Business AI</h1>
    <p class="note-subtitle">The SAP AI portfolio: embedded capabilities, Joule and agents, plus services for building and governing AI.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>AI-assisted operations</dd></div>
      <div><dt>SAP area</dt><dd>SAP Business AI</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until verified against current SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>“We use SAP Business AI” does not identify an implementation. Name the capability, the application or service that owns it, and the business task it supports before choosing an architecture.</p>

    <h2>Separate three responsibilities</h2>
    <ol>
      <li><strong>Embedded business capability:</strong> an SAP application provides a specific AI feature. Check its business objects, permissions, release scope, and operational behavior.</li>
      <li><strong>User interaction and agent behavior:</strong> <a href="/atlas/sap/sap-joule/">Joule capabilities</a> provide supported ways to ask, navigate, or perform tasks. The visible assistant does not reveal every service or permission behind it.</li>
      <li><strong>Custom AI services:</strong> SAP AI Core and the <a href="https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/generative-ai-hub-in-sap-ai-core">generative AI hub</a> provide building blocks for AI applications. The implementation team still owns the business integration and controls.</li>
    </ol>
    <p>This is a responsibility map, not a licensing model. In its <a href="https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/">May 12, 2026 announcement</a>, SAP introduced SAP Business AI Platform as a foundation bringing SAP BTP, SAP Business Data Cloud, and SAP Business AI together. That portfolio statement does not establish availability or entitlement for a particular capability in a particular tenant.</p>

    <h2>Compare a delivered feature with a custom extension</h2>
    <p>Start with the documented feature if it matches the task. Check its limits before assuming that a custom agent is needed. A custom extension gives the team more design choices but also makes it responsible for grounding, tool access, evaluation, logging, approval, and recovery.</p>
    <p><strong>Synthetic example:</strong> a team wants help investigating blocked orders. If an available application capability answers the required question within the right access boundary, evaluate that contract first. If the task needs evidence from several systems, define which system owns each fact, how it is retrieved, and who owns the final action. Model access alone does not solve those integration questions.</p>

    <h2>Write a concrete architecture statement</h2>
    <p>Record the business task, owning product and capability, system of record, data interface, execution identity, allowed effects, and acceptance test. Mark unknowns, including edition, region, entitlement, and release availability.</p>
    <p>For example: “The assistant retrieves approved diagnostic guidance and current order status, proposes a next check, and sends any business change through the existing controlled workflow.” This describes the intended boundary; it is not evidence that the design has been implemented or tested.</p>
    <p>Use <a href="/atlas/sap/evaluation-guardrails/">Evaluation and Guardrails</a> for quality and control design, and <a href="/atlas/sap/agent-workflows/">Agent Workflows</a> when the task needs several steps. Retrieval can supply context, but stale or irrelevant evidence can still produce a wrong answer. Keep a testable result and an accountable owner for the decision.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-joule/">SAP Joule</a></li>
      <li><a href="/atlas/sap/ai-agents/">AI Agents</a></li>
      <li><a href="/atlas/sap/rag/">RAG</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
