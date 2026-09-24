---
layout: default
title: "Evaluation and Guardrails"
description: "Evaluation measures whether an AI system performs acceptably; guardrails constrain what it may process, produce, or do at runtime. Enterprise AI needs both."
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
    <p>Evaluation and guardrails solve different problems. <strong>Evaluation</strong> asks whether an AI system performs well enough for a defined task. <strong>Guardrails</strong> constrain what the system may accept, return, or do while it is running. A system can pass an evaluation and still need strong runtime controls; a heavily filtered system can still be poor at the business task.</p>

    <p>Keeping the two concepts separate makes enterprise AI easier to reason about. We can improve model or prompt quality without pretending that better accuracy removes authorization risk, and we can add safety controls without claiming they prove the answers are correct.</p>

    <h2>Evaluate the task, not the model in isolation</h2>

    <p>For a support assistant, useful evaluation might ask whether the answer identifies the right SAP object, cites relevant evidence, and avoids inventing configuration. For an agent, it may ask whether the correct tool was selected, whether the task reached the intended business state, and whether unsafe or unsupported actions were rejected.</p>

    <p>There is no universal enterprise metric called “accuracy.” The evaluation set should represent the real task: normal cases, ambiguous requests, authorization differences, stale data, backend errors, and edge cases that are expensive when handled incorrectly. A benchmark with easy prompts can look excellent while the productive workflow remains unreliable.</p>

    <h2>Offline and production evaluation answer different questions</h2>

    <p>Offline evaluation is useful before a change is released. A fixed dataset lets us compare prompts, models, retrieval strategies, or tool logic against repeatable cases. Production evaluation shows what happens with real users and real system conditions: which requests fail, where people correct the output, how often the agent escalates, and whether backend behavior changes the result.</p>

    <p>SAP AI Launchpad currently supports evaluation runs for generative AI workloads and exposes run details, metrics, and tags. That is an evaluation facility, not a substitute for business acceptance criteria. The project still has to define what a successful result means.</p>

    <h2>Guardrails belong at several layers</h2>

    <p>One content filter is not a complete guardrail strategy. Enterprise controls can sit at several points:</p>

    <ul>
      <li><strong>before the model</strong> — input validation, prompt-injection defenses, data masking, and scope checks;</li>
      <li><strong>around model output</strong> — content filtering, schema validation, citation or evidence requirements, and business-rule checks;</li>
      <li><strong>around tools</strong> — allowlisted operations, parameter validation, authorization, rate or volume controls, and idempotency;</li>
      <li><strong>around business actions</strong> — approval, segregation of duties, reconciliation, and rollback or compensating logic.</li>
    </ul>

    <p>SAP's generative AI hub orchestration currently documents optional data masking and input/output content filtering. These controls can reduce specific risks, but they do not decide whether an SAP posting is valid, whether a user is authorized to change a business object, or whether a master-data change needs approval.</p>

    <h2>Guardrails should fail clearly</h2>

    <p>A blocked request is not necessarily an error. If a policy deliberately prevents the model from processing a category of data or a tool rejects an unauthorized operation, the workflow should preserve that distinction. Users and operators need to know whether the system failed technically, lacked evidence, hit a policy boundary, or escalated by design.</p>

    <p>This makes monitoring more useful. Instead of one generic failure rate, separate model or retrieval errors, tool failures, policy blocks, validation failures, human escalations, and successful completions. Each category has a different owner and a different remedy.</p>

    <h2>Human review is one guardrail, not the last defense</h2>

    <p>Human approval is appropriate for selected high-impact or uncertain actions, but it should not be used to compensate for an uncontrolled tool surface. The approver should see the exact proposed action and relevant evidence, while the execution path still enforces technical and business authorization.</p>

    <p>The strongest design is layered: evaluate whether the AI can do the task, constrain what it can access and call, validate the proposed result, and add a human decision where judgment or accountability genuinely requires one.</p>

    <h2>Re-evaluate when the system changes</h2>

    <p>Model versions, prompts, grounding sources, APIs, business rules, and user behavior all change. A previous test result therefore has a shelf life. The important trigger for re-evaluation is not a calendar date alone; it is a material change to the system or the distribution of work it receives.</p>

    <p>For SAP-facing AI, backend upgrades matter too. If an API changes, a field becomes unavailable, or an authorization model is redesigned, an unchanged agent can start failing even though the model itself did not change.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/ai-launchpad/sap-ai-launchpad-user-guide/view-evaluations">View evaluations in SAP AI Launchpad</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/ai-launchpad/sap-ai-launchpad/build-your-orchestration-workflow">Build an orchestration workflow</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/data-masking-d9a54d9ca54b40beacbd24e1663ec3b4">Data masking in SAP AI Core</a>.</li>
      <li>SAP Cloud SDK for AI — <a href="https://help.sap.com/doc/generative-ai-hub-sdk/CLOUD/en-US/_reference/orchestration-service2.html">Orchestration Service V2 modules and content filtering</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Evaluation features, filtering providers, model support, and orchestration options evolve quickly. Verify the current service plan and product documentation, and define task-specific acceptance criteria rather than relying on a generic AI quality score.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
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
