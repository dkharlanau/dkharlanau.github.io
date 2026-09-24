---
layout: default
title: "AI Agents"
description: "AI agents combine models, tools, state, and control logic to pursue a goal across multiple steps; in SAP they must remain bounded by business authorization and process controls."
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
    <p>An AI agent is software that can work toward a goal across several steps instead of returning one model response and stopping. A useful agent typically combines a model with tools, state, instructions, and control logic. It can inspect the current situation, choose an allowed action, observe the result, and continue until it reaches a stopping condition or hands the task to a person.</p>

    <p>The word <em>agent</em> is often used too loosely. A chatbot is not automatically an agent, and a workflow is not automatically agentic. The important difference is decision freedom: a deterministic workflow follows a predefined path, while an agent can choose among permitted actions based on the context it sees.</p>

    <h2>The agent is only one part of the system</h2>

    <p>For enterprise work, the model itself is rarely the hardest part. The surrounding system decides what the agent is allowed to know and do. We normally need at least four boundaries:</p>

    <ul>
      <li><strong>context</strong> — the data, documents, events, or conversation state available for the task;</li>
      <li><strong>tools</strong> — the APIs, searches, calculations, or workflow actions the agent may call;</li>
      <li><strong>authority</strong> — the identity and business permissions under which those tools execute;</li>
      <li><strong>control</strong> — validation, evaluation, stopping rules, approvals, and escalation.</li>
    </ul>

    <p>If these boundaries are vague, the design is unsafe even when the model performs well in a demo. A tool that exposes an unrestricted update API, for example, gives the agent a much larger risk surface than a tool that accepts one validated business action with explicit authorization checks.</p>

    <h2>Agents are now a real SAP product pattern</h2>

    <p>SAP's current Joule documentation includes content-based agents that run as part of Joule capabilities. SAP describes these agents as suitable for complex, non-deterministic business processes; during execution they can exchange messages with Joule and request user input or human approval. SAP also ships specialized Joule Agents for business scenarios.</p>

    <p>This means an older rule such as “AI in SAP may only suggest, never act” is no longer accurate. The better rule is narrower: an agent may act only through the tools, identities, and process controls that the solution deliberately exposes. Whether a human approval is required depends on the specific process, risk, and product behavior.</p>

    <h2>Agent versus workflow</h2>

    <p>Many productive designs combine the two. A workflow can establish a reliable outer process—receive a request, collect required data, wait for approval, execute a transaction, record the result—while an agent handles the part that benefits from interpretation, such as classifying an incident or deciding which diagnostic tool to call next.</p>

    <p>The opposite pattern also exists: an agent can call a deterministic workflow as one of its tools. That is often safer than giving it many low-level APIs. The workflow becomes a controlled business capability with known inputs, outputs, authorization checks, and rollback behavior.</p>

    <h2>What changes when the agent can write</h2>

    <p>Read-only assistance mainly risks incorrect information. A write-capable agent adds operational risk: it can create a business object, change a status, trigger a downstream process, or consume a limited resource. The control model therefore has to match the effect of the action.</p>

    <p>Before exposing a write tool, we should know which identity executes it, which business authorization is checked, whether the request is idempotent, how duplicate execution is prevented, what evidence is logged, and what happens if the agent stops halfway through a multi-step task. Human approval can be one control, but it is not a substitute for these engineering controls.</p>

    <h2>How to evaluate an agent</h2>

    <p>Do not evaluate only the final prose. Measure whether the agent completes the business task correctly and safely. Useful tests can include tool-selection accuracy, task completion, invalid-action rate, escalation quality, latency, and the proportion of runs that require manual correction. The right metric depends on the task; there is no universal “agent accuracy” score.</p>

    <p>For SAP scenarios, the most useful test cases usually include realistic authorization differences, stale or incomplete master data, backend errors, duplicate requests, ambiguous user intent, and process states in which an otherwise valid action is not allowed.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/joule">Joule documentation and development guidance</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/6b0a25c11bc54daf84c29a5f9b82c87d.html">Manage Joule skills and agents across environments</a>.</li>
      <li>SAP News Center — <a href="https://news.sap.com/2026/04/sap-business-ai-release-highlights-q1-2026/">SAP Business AI release highlights Q1 2026</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/btp/sap-business-technology-platform/access-joule">Joule authorization example in SAP BTP cockpit</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Agent capabilities, supported tools, and product availability change quickly. Treat “agent” as an architectural pattern first, then verify the exact SAP product capability, release, region, entitlement, and authorization model before implementation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
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
