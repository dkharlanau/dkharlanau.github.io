---
layout: default
title: "AI Agents"
description: "Decide when a task needs an AI agent, define its tools and authority, and set evidence, stopping, and review requirements."
permalink: /atlas/sap/ai-agents/
atlas_section: sap
domain: SAP operations
subdomain: AI and agentic technologies
concept_type: technology
sap_area: "AI Agents"
business_process: "AI-assisted operations"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
last_modified_at: 2026-10-07
author: Dzmitryi Kharlanau

tags:
  - ai-agents
  - autonomous-systems
  - sap-ams
related:
  - /atlas/sap/sap-joule/
  - /atlas/sap/sap-business-ai/
  - /atlas/sap/rag/
  - /atlas/sap/evaluation-guardrails/
  - /atlas/sap/human-approval-workflows/
  - /atlas/ai-operations/ai-agent-for-sap-support/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">AI Agents</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>AI Agents</h1>
    <p class="note-subtitle">Goal-directed AI systems that combine models, tools, state, and control logic across multiple steps.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>AI-assisted operations</dd></div>
      <div><dt>SAP area</dt><dd>AI Agents</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until verified against current SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>Consider an agent when choosing the next useful step requires interpretation of new evidence. An agent combines a model, tools, state, and control logic: it observes a result, selects an allowed next action, and stops or escalates when it reaches a defined limit.</p>

    <h2>First decide whether the task needs that freedom</h2>
    <ul>
      <li><strong>Known rule and known path:</strong> use a rule, script, or workflow. An extra model decision adds uncertainty without helping.</li>
      <li><strong>One interpretation step:</strong> use a model inside a fixed workflow, for example to classify an incident before routing it.</li>
      <li><strong>The next check depends on earlier findings:</strong> consider an agent with a small set of diagnostic tools.</li>
    </ul>
    <p>A conversational interface does not tell you which design is underneath. For SAP-delivered capabilities, check the specific <a href="/atlas/sap/sap-joule/">Joule capability and its authorization boundary</a>.</p>

    <h2>Define the operating scope before choosing the model</h2>
    <p>Write down the goal, allowed evidence, available tools, execution identity, and stopping condition. These define the agent's operating boundary. Instructions alone cannot enforce it; the retrieval and tool layers must check access and reject unsupported actions.</p>
    <p><strong>Synthetic example:</strong> an assistant investigates a failed delivery interface. It may read the relevant message status and approved diagnostic guidance, then choose another read-only check. Its output is a likely failure area, supporting evidence, and a next action for the operator. Reprocessing a message is a separate business action with its own permission and duplicate-execution checks.</p>
    <p>Keep the tool narrow. “Read this message's processing status” is easier to control than arbitrary database access. A write tool should expose a validated business operation rather than unrestricted field updates.</p>

    <h2>What changes when tools can write?</h2>
    <p>Read-only agents can disclose restricted data or produce misleading advice. Retrieved text can also contain malicious instructions. Write access adds effects such as creating documents, changing status, or triggering downstream work. Match controls to the effect: identity, business authorization, input validation, duplicate protection, execution evidence, and recovery.</p>
    <p>Human approval may be required by the process or risk policy. It does not replace these controls. Define what the agent must do when evidence is missing, a tool fails, the request is ambiguous, or its time or action limit is reached.</p>

    <h2>Output of the design review</h2>
    <p>Produce a bounded task contract and test cases, not only a prompt. Measure task completion, tool choice, invalid actions, escalation, latency, and manual correction for that task. Continue with <a href="/atlas/sap/agent-workflows/">execution and recovery</a> and <a href="/atlas/sap/evaluation-guardrails/">acceptance tests and runtime controls</a>.</p>
    <p>This is a reusable design pattern, not a tested SAP implementation. Product availability and supported tools need separate checks.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-joule/">SAP Joule</a></li>
      <li><a href="/atlas/sap/agent-workflows/">Agent Workflows</a></li>
      <li><a href="/atlas/sap/evaluation-guardrails/">Evaluation and Guardrails</a></li>
      <li><a href="/atlas/sap/human-approval-workflows/">Human Approval Workflows</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
