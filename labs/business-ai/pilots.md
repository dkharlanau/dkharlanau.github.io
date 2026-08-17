---
layout: default
title: "Open Enterprise AI Pilots — ERP, Documents, Agents, and Controls"
description: "A practical portfolio of vendor-neutral Enterprise AI pilots around ERP, document processing, agent access, controls, evaluation, and open research."
permalink: /labs/business-ai/pilots/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-08-17
last_reviewed: 2026-08-17
hide_global_cta: true
publication_wave: "public-business-ai-pilots-01"
review_method: "author-designed pilot architecture + cross-vendor primary-source review"
evidence_review_mode: "selective_or_heuristic"
search_intent: "enterprise AI ERP pilots, document to ERP AI, ERP agents, MCP, AI governance and open research"
structured_data:
  type: TechArticle
tags:
  - business-ai
  - enterprise-ai
  - erp
  - mcp
  - agents
  - document-ai
  - ai-governance
# ai-discovery-managed:start
primary_topic: "business-ai"
ai_sidecar: "/ai/pages/labs--business-ai--pilots.json"
semantic_links:
  - type: "parent_context"
    title: "Business AI Lab — Processes, Patterns, Technologies, Evidence"
    url: "/labs/business-ai/"
  - type: "related_topic"
    title: "AI Ready — Practical AI Architecture Lab"
    url: "/labs/ai-ready/"
  - type: "integrates_with"
    title: "Enterprise Agent Architecture — Tools, Identity, Autonomy and Governance"
    url: "/labs/enterprise-context/business-ai/agents/"
  - type: "related_topic"
    title: "Document-to-ERP AI Pilot — From PDF to Controlled Transaction"
    url: "/labs/business-ai/document-to-erp-ai/"
  - type: "related_topic"
    title: "ERP Agent Gateway Pilot — Safe AI Tool Access to Enterprise Systems"
    url: "/labs/business-ai/erp-agent-gateway/"
  - type: "related_topic"
    title: "Open Enterprise AI Research — ERP Evidence, Safety, and Readiness"
    url: "/labs/business-ai/open-research/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li aria-current="page">Open Enterprise AI Pilots</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / open pilots</p>
      <h1>Stop debating AI.<br />Give it a process and a failure case.</h1>
      <p>I am building small Enterprise AI pilots around ERP systems, documents, agents, and controls. The goal is not to make a chatbot look clever for five minutes. The goal is to find where AI can enter a real business process without making the process harder to trust.</p>
      <a class="research-canvas__button" href="#pilot-map">Open the pilot map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Pilot programme status">
      <p>Current programme</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>2</strong><small>Flagship pilots</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>3</strong><small>Open research tracks</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>0</strong><small>Required vendor locks</small></div>
      <em>SAP is a primary context, not a prison. The same questions matter in Dynamics 365, Oracle, and other ERP landscapes.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal aria-label="Pilot boundary">
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>A pilot is not a demo.</strong> Every pilot must define the business step, system of record, authority boundary, measurable result, failure condition, and exit criteria before the model gets a chance to impress anyone.</p>
    <p><strong>A pilot is allowed to fail.</strong> A failed test with a clear reason is useful. A polished demo with no audit trail is mostly theatre with better lighting.</p>
  </section>

  <section class="research-canvas__inventory" id="pilot-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Flagship pilots</p>
      <h2>Two places where AI meets enterprise reality quickly.</h2>
      <p>Both pilots start vendor-neutral. Adapters can target SAP, Microsoft Dynamics 365, Oracle Fusion, a mock ERP, or a small reference API. The interesting part is the boundary between uncertain AI output and deterministic business execution.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/business-ai/document-to-erp-ai/"><span>01</span><strong>Document-to-ERP AI</strong><small>Turn a business document into a validated ERP proposal with master-data checks, confidence, human approval, transaction control, and a complete audit trail.</small><i class="material-symbols-outlined" aria-hidden="true">description</i></a>
      <a href="/labs/business-ai/erp-agent-gateway/"><span>02</span><strong>ERP Agent Gateway</strong><small>Let an AI agent use ERP tools through a controlled gateway with read, plan, and write modes, policy checks, confirmations, and traceable actions.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Open research</p>
      <h2>Build evidence that survives the vendor slide.</h2>
      <p>The research tracks are designed to be useful even when the platform names change. They focus on safety, readiness, and evidence.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/business-ai/open-research/#evidence-registry"><span>R1</span><strong>Enterprise AI Evidence Registry</strong><small>Track claims, primary sources, measured results, missing evidence, limitations, and what can actually be reused.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="/labs/business-ai/open-research/#safety-benchmark"><span>R2</span><strong>ERP Agent Safety Benchmark</strong><small>Test permissions, wrong-tool selection, prompt injection, duplicate actions, stale context, confirmation, and recovery.</small><i class="material-symbols-outlined" aria-hidden="true">shield</i></a>
      <a href="/labs/business-ai/open-research/#readiness"><span>R3</span><strong>ERP AI Readiness Assessment</strong><small>Score process, data, documents, integration, security, observability, governance, and system authority before choosing a pilot.</small><i class="material-symbols-outlined" aria-hidden="true">checklist</i></a>
      <a href="/labs/business-ai/open-research/"><span>OPEN</span><strong>Open Research Programme</strong><small>Research rules, contribution options, question backlog, and a simple way to collaborate without sharing confidential production data.</small><i class="material-symbols-outlined" aria-hidden="true">groups</i></a>
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Pilot contract</p><h2>Every experiment answers the same seven questions.</h2></div>
    <ol>
      <li><span>01</span><strong>Process</strong><p>Which real business step becomes faster, safer, or easier to operate?</p></li>
      <li><span>02</span><strong>Source of truth</strong><p>Which ERP, document store, database, or service owns the final business state?</p></li>
      <li><span>03</span><strong>Uncertainty</strong><p>Which part may be probabilistic, and which part must remain deterministic?</p></li>
      <li><span>04</span><strong>Authority</strong><p>What can the AI read, propose, execute, or never touch?</p></li>
      <li><span>05</span><strong>Control</strong><p>Where are validation, confirmation, fallback, rollback, and audit enforced?</p></li>
      <li><span>06</span><strong>Metric</strong><p>What result is measured beyond model accuracy?</p></li>
      <li><span>07</span><strong>Failure</strong><p>Which bad outcome would make the pilot unacceptable even if the average result looks good?</p></li>
    </ol>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Why now</p>
      <h2>Agent access to ERP is becoming a real architecture problem.</h2>
      <p>In 2026, this is no longer only a research topic. Microsoft documents a Dynamics 365 ERP MCP server for access to ERP data and business logic. SAP documents MCP server connections for Joule agents. Oracle lists agentic ERP features across areas such as ledgers, expenses, collections, and payables. The MCP specification itself puts consent, authorization, and tool safety close to the centre of the protocol.</p>
    </header>
    <div class="research-route-list">
      <a href="https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp"><span>MS</span><strong>Dynamics 365 ERP MCP</strong><small>Primary documentation for agent access to finance and operations data and business logic.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/joule-studio-classic/joule-studio-classic-edition/add-mcp-servers-to-your-joule-agent"><span>SAP</span><strong>Joule Agent + MCP Servers</strong><small>SAP guidance for connecting Joule agents to external applications through MCP servers, including explicit security warnings.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://docs.oracle.com/en/cloud/saas/fusion-ai/aiafl/ai-erp.html"><span>ORA</span><strong>Oracle Fusion ERP AI Features</strong><small>Primary catalogue of AI and agentic ERP features across finance processes.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://modelcontextprotocol.io/specification/2025-11-25"><span>MCP</span><strong>Model Context Protocol Specification</strong><small>Open protocol specification covering context, tools, consent, authorization, and tool safety.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal aria-label="Portfolio value">
    <span class="material-symbols-outlined" aria-hidden="true">work</span>
    <p><strong>Why publish the work?</strong> A serious pilot can show process knowledge, architecture, integration thinking, data controls, evaluation, and operational judgment in one place. That is more useful than adding another line that says “AI experience” to a CV.</p>
    <p><strong>What I want to prove.</strong> Enterprise AI is not mainly a model-selection problem. It is a system-design problem with business consequences.</p>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
