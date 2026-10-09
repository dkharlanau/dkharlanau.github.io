---
layout: default
title: "Agent Workflows"
description: "Design a controlled agent workflow with authorization before side effects, confirmed business results, and safe recovery after uncertain outcomes."
permalink: /atlas/sap/agent-workflows/
atlas_section: sap
domain: SAP operations
subdomain: Developer and platform technologies
concept_type: technology
sap_area: "Agent Workflows"
business_process: "Application development"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
last_modified_at: 2026-10-07
author: Dzmitryi Kharlanau

tags:
  - agent-workflows
  - ai-agents
  - orchestration
related:
  - /atlas/sap/ai-agents/
  - /atlas/sap/human-approval-workflows/
  - /atlas/sap/evaluation-guardrails/
  - /atlas/sap/cap/
  - /atlas/sap/python-automation/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Agent Workflows</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>Agent Workflows</h1>
    <p class="note-subtitle">How to combine agent decisions with deterministic execution, validation, approvals, and recovery.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Application development</dd></div>
      <div><dt>SAP area</dt><dd>Agent Workflows</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>An agent workflow gives model decisions a controlled execution path. Use it when a task needs interpretation but must still preserve business authorization, durable state, and a recoverable outcome.</p>

    <h2>Choose who owns the process</h2>
    <ul>
      <li><strong>Agent inside a workflow:</strong> a fixed process owns the lifecycle and asks the agent to handle a bounded interpretive step.</li>
      <li><strong>Workflow as an agent tool:</strong> the agent selects a business operation; the workflow owns its validation, execution, and result.</li>
      <li><strong>Several specialist agents:</strong> use only when separate responsibilities justify the extra coordination, latency, and failure paths.</li>
    </ul>
    <p>The <a href="/atlas/sap/ai-agents/">agent selection guide</a> covers whether the task needs model-driven choices at all.</p>

    <h2>Keep inspection separate from a business change</h2>
    <ol>
      <li><strong>Accept:</strong> validate the request, supported scope, and requester identity.</li>
      <li><strong>Inspect:</strong> check access before retrieving evidence or calling read-only tools. Treat returned content as data, not new authority.</li>
      <li><strong>Propose:</strong> select a bounded operation and record its inputs, evidence, and expected effect.</li>
      <li><strong>Authorize:</strong> validate parameters, business rules, and execution permissions. Obtain any required approval and recheck relevant state before a side effect.</li>
      <li><strong>Execute:</strong> use the controlled operation with duplicate protection and a durable execution record.</li>
      <li><strong>Confirm:</strong> check the resulting business state, then complete, recover, or escalate.</li>
    </ol>
    <p>Limit diagnostic loops by time, actions, or evidence requirements. Stop when further steps cannot resolve the uncertainty within the allowed scope.</p>

    <h2>A timeout leaves a question, not permission to retry</h2>
    <p><strong>Synthetic example:</strong> a backend creates a document, but the response is lost. The workflow knows that the call timed out; it does not yet know whether creation failed. Repeating the request may create a duplicate.</p>
    <p>Record a request identifier and the known result of each side effect. After an uncertain response, query the supported status or reconciliation interface before retrying. Use idempotency where the business API supports it; otherwise define explicit duplicate detection and a manual recovery path. Resume from confirmed state rather than replaying every successful step.</p>
    <p>Some changes need compensation rather than rollback. Name the owner and allowed recovery action before enabling the write path.</p>

    <h2>Implementation boundary</h2>
    <p>In SAP Build Process Automation, a completed user task can have a distinct business outcome such as Approved or Rejected. The <a href="https://help.sap.com/docs/build-process-automation/sap-build-process-automation/configure-step-outcomes">step-outcome documentation</a> illustrates why technical completion alone does not establish the business result.</p>
    <p>The review output should identify each step's input, execution identity, side effect, result check, and recovery path. This pattern does not select a runtime or promise that every SAP API supports idempotency. For the approval payload and recipient rules, use <a href="/atlas/sap/human-approval-workflows/">Human Approval Workflows</a>.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/ai-agents/">AI Agents</a></li>
      <li><a href="/atlas/sap/human-approval-workflows/">Human Approval Workflows</a></li>
      <li><a href="/atlas/sap/evaluation-guardrails/">Evaluation and Guardrails</a></li>
      <li><a href="/atlas/sap/python-automation/">Python Automation</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
