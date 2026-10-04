---
layout: default
title: "AI Ready — Practical AI Architecture Lab"
description: "A practical learning area for using AI in real systems: research, knowledge, coding, data, tools, MCP, agents, evals, security, and deployment."
permalink: /labs/ai-ready/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-10-04
hide_global_cta: true
tags: [ai, architecture, mcp, agents, rag, evals, security, automation]
last_reviewed: 2026-08-16
publication_wave: "public-framework-search-wave-04"
review_method: "selective external evidence + page-level editorial review + authored heuristic boundary"
evidence_review_mode: "selective_or_heuristic"
search_intent: "practical AI architecture for RAG, tools, MCP, agents, evals and security"
# ai-discovery-managed:start
structured_data:
  type: TechArticle
primary_topic: "ai-architecture"
ai_sidecar: "/ai/pages/labs--ai-ready.json"
semantic_links:
  - type: "related_topic"
    title: "ERP Agent Gateway Pilot — Safe AI Tool Access to Enterprise Systems"
    url: "/labs/business-ai/erp-agent-gateway/"
  - type: "related_topic"
    title: "Which SAP Logistics Decisions Should AI Not Own? — Decision Card"
    url: "/labs/enterprise-context/decisions/ai-logistics-boundary/"
  - type: "related_topic"
    title: "Business AI Glossary — Plain Language for Discovery, Architecture, Governance and Delivery"
    url: "/labs/business-ai/glossary/"
  - type: "parent_context"
    title: "Labs — SAP Enterprise, Assurance, AI, Interview and Assessment"
    url: "/labs/"
  - type: "integrates_with"
    title: "IDoc, API, or Event? — SAP Integration Decision Card"
    url: "/labs/enterprise-context/decisions/idoc-api-event/"
  - type: "integrates_with"
    title: "SAP EWM — Warehouse Execution, Objects and Integration Boundaries"
    url: "/labs/enterprise-context/ewm/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li aria-current="page">AI Ready</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Labs / AI Ready</p>
      <h1>Use AI.<br />Build the system around it.</h1>
      <p>This lab is technology-first, not industry-first. Learn how to use models for research, knowledge work, coding, data analysis, automation, tool use, and agents. Then learn how to make those systems testable, secure, and deployable.</p>
      <a class="research-canvas__button" href="/labs/ai-ready/use-cases/">Start from a use case <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
    </div>
    <figure class="system-opening-visual">
      <img src="/assets/img/systems/ai-evidence-boundary-journal.webp" alt="Heterogeneous evidence entering a bounded AI synthesis layer, then separating into approved action, human review, and a retained audit trail." width="1728" height="1081" decoding="async" fetchpriority="high" />
      <figcaption>The model handles uncertainty; normal software keeps authority, state, and evidence.</figcaption>
    </figure>
    <div class="research-canvas__signal" aria-label="Review status">
      <p>Current baseline</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>7</strong><small>Architecture areas</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>4</strong><small>Hands-on labs</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>2026-07-28</strong><small>MCP revision tracked</small></div>
      <em>Reviewed 15 Aug 2026. Fast-moving protocol details are dated.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">architecture</span>
    <p><strong>Problem:</strong> Teams often start with a model demo before defining data, tools, controls, evaluation, deployment, and failure handling.</p>
    <p><strong>Main rule:</strong> use the model for uncertainty. Keep identity, permissions, exact rules, durable state, and side effects in normal software.</p>
    <p><strong>Learning rule:</strong> build the smallest useful version first, create eval cases, then add retrieval, tools, agents, or fine-tuning only when a measured gap needs them.</p>
    <a href="/labs/ai-ready/deep-dives/">Open architecture deep dives <span class="material-symbols-outlined" aria-hidden="true">menu_book</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Use it for real work</p>
      <h2>Start from the job, not the buzzword.</h2>
      <p>The same model can sit inside very different systems. The useful architecture depends on what must be correct, fresh, private, repeatable, or reversible.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/ai-ready/use-cases/#research"><span>01</span><strong>Research and synthesis</strong><small>Search, compare sources, extract evidence, summarize, and keep citations.</small><i class="material-symbols-outlined" aria-hidden="true">travel_explore</i></a>
      <a href="/labs/ai-ready/use-cases/#knowledge"><span>02</span><strong>Knowledge assistant</strong><small>Answer from private or changing documents using retrieval, metadata, and permissions.</small><i class="material-symbols-outlined" aria-hidden="true">library_books</i></a>
      <a href="/labs/ai-ready/use-cases/#coding"><span>03</span><strong>Coding and engineering</strong><small>Read repositories, explain code, propose patches, run tests, and use tools with bounded write access.</small><i class="material-symbols-outlined" aria-hidden="true">code</i></a>
      <a href="/labs/ai-ready/use-cases/#data"><span>04</span><strong>Data analysis</strong><small>Translate questions into deterministic calculations, SQL, Python, charts, and checked outputs.</small><i class="material-symbols-outlined" aria-hidden="true">analytics</i></a>
      <a href="/labs/ai-ready/use-cases/#automation"><span>05</span><strong>Automation and integrations</strong><small>Connect models to APIs and applications through typed tools, workflows, events, and MCP.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="/labs/ai-ready/use-cases/#agents"><span>06</span><strong>Agents and operations</strong><small>Use bounded loops when the next useful action depends on evidence found during the task.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="architecture-map" data-reveal>
    <header><p class="research-canvas__eyebrow">Architecture map</p><h2>Learn the system in layers.</h2><p>You do not need every layer for every product. Learn what each layer solves and what it can break.</p></header>
    <div class="research-route-list">
      <a href="/labs/ai-ready/system-boundaries/"><span>01</span><strong>System Boundaries</strong><small>Model vs application, structured output, state, memory, deterministic rules.</small><i class="material-symbols-outlined" aria-hidden="true">foundation</i></a>
      <a href="/labs/ai-ready/data-rag/"><span>02</span><strong>Data and RAG</strong><small>Sources, metadata, lexical/vector/hybrid retrieval, reranking, citations, permissions.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="/labs/ai-ready/tools-mcp/"><span>03</span><strong>Tools and MCP</strong><small>Typed tools, resources, prompts, transport, authorization, write safety, reuse.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="/labs/ai-ready/agent-architecture/"><span>04</span><strong>Agent Architecture</strong><small>Workflow, router, bounded tool loop, workers, budgets, termination, approval.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/ai-ready/evals-reliability/"><span>05</span><strong>Evals and Reliability</strong><small>Golden cases, deterministic graders, model graders, trajectory tests, regressions.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="/labs/ai-ready/security-governance/"><span>06</span><strong>Security and Governance</strong><small>Prompt injection, least privilege, secrets, sensitive data, approvals, audit.</small><i class="material-symbols-outlined" aria-hidden="true">shield</i></a>
      <a href="/labs/ai-ready/build-operate/"><span>07</span><strong>Build and Operate</strong><small>Versions, deployment, traces, budgets, token economics, retries, degraded modes, rollback.</small><i class="material-symbols-outlined" aria-hidden="true">rocket_launch</i></a>
    </div>
  </section>


  <section class="research-canvas__inventory" id="support-agent-production-pattern" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Case / AI support agent</p>
      <h2>Design for resolution, not only for answers.</h2>
      <p>A useful support agent must do more than retrieve text. It needs current context, controlled tools, clear stop conditions, safe escalation, and evidence that the issue was actually resolved.</p>
    </header>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">support_agent</span>
      <div>
        <p><strong>Case claim:</strong> the AssemblyAI video uses an 80% ticket-resolution result. Treat this as a case-specific outcome, not as a general target.</p>
        <p><strong>Lead question:</strong> before accepting the number, define what <em>resolved</em> means, which ticket classes are in scope, when a human takes over, and how wrong actions or reopened tickets are counted.</p>
      </div>
    </div>

    <div class="ecg-decision-columns">
      <div>
        <h3>Production pattern</h3>
        <ol>
          <li><strong>Understand the request.</strong> Classify intent, urgency, identity, and the business object involved.</li>
          <li><strong>Retrieve approved knowledge.</strong> Use current product guidance, runbooks, policies, and solved cases as evidence.</li>
          <li><strong>Read live facts through tools.</strong> Account status, order state, ticket history, or system evidence should come from the source system, not from model memory.</li>
          <li><strong>Act through typed functions.</strong> Validate parameters, permissions, policy, retries, and idempotency before any side effect.</li>
          <li><strong>Check the result.</strong> Confirm that the business state changed as expected instead of assuming a successful API response means the problem is solved.</li>
          <li><strong>Escalate with context.</strong> When confidence, authority, or policy is insufficient, pass the evidence, attempted steps, and open question to a human.</li>
          <li><strong>Evaluate the full trajectory.</strong> Measure answer quality, tool selection, action correctness, escalation quality, latency, cost, and final resolution.</li>
        </ol>
      </div>
      <div>
        <h3>What changes for voice</h3>
        <p>Voice adds an input-quality dependency before the model can reason or call a tool. Names, order IDs, email addresses, phone numbers, and codes must be captured correctly.</p>
        <p>If the input entity is wrong, a correct tool call can still query the wrong object. The system therefore needs confirmation rules for important identifiers and a safe path when the value is uncertain.</p>
        <p>Latency also becomes part of the experience. A long silent tool call can look like a failed call, so the interaction design needs an explicit transition or hold state while the lookup runs.</p>
      </div>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Failure modes a Lead should test</h3>
      <table>
        <thead><tr><th scope="col">Failure</th><th scope="col">What goes wrong</th><th scope="col">Control</th></tr></thead>
        <tbody>
          <tr><th scope="row">Wrong retrieval</th><td>The agent answers from stale or irrelevant knowledge.</td><td>Approved sources, metadata, retrieval evals, citations, and freshness rules.</td></tr>
          <tr><th scope="row">Wrong entity</th><td>An ID, email, name, or code is misunderstood and the tool queries the wrong object.</td><td>Entity validation, read-back confirmation, schema checks, and safe retry.</td></tr>
          <tr><th scope="row">Answer without action</th><td>The agent explains the policy but cannot complete the customer job.</td><td>Typed tools for the allowed action, with explicit authority boundaries.</td></tr>
          <tr><th scope="row">Unsafe action</th><td>A plausible model decision triggers a side effect that policy or authorization should block.</td><td>Deterministic policy checks, least privilege, approval for high-risk actions, and audit logs.</td></tr>
          <tr><th scope="row">Duplicate side effect</th><td>A retry creates the same refund, change, or update twice.</td><td>Idempotency keys, durable action state, and reconciliation.</td></tr>
          <tr><th scope="row">Bad escalation</th><td>The human receives the ticket but must restart the investigation.</td><td>Transfer the summary, evidence, attempted actions, confidence gap, and next question.</td></tr>
          <tr><th scope="row">Inflated resolution metric</th><td>The system counts deflection, abandonment, or temporary answers as success.</td><td>Define resolution before the pilot and track reopen rate, correction rate, CSAT, and human takeover.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="ecg-decision-columns">
      <div>
        <h3>Translate the pattern to SAP support</h3>
        <p>For SAP operations, a safe first scope is not autonomous Customizing. The agent can retrieve approved runbooks, classify the incident, read allowed system evidence, compare a good and bad business object, propose the next diagnostic step, and prepare a handoff.</p>
        <p>Examples include a blocked sales order, a failed IDoc, a PO/GR/IR mismatch, or a recurring master-data defect. The SAP system remains the owner of durable state and authorization. Material changes stay behind normal SAP controls and human accountability.</p>
      </div>
      <div>
        <h3>Lead decision</h3>
        <p>Use an agent when the next useful step depends on evidence discovered during the task. Keep a normal workflow when the sequence is already known. Keep exact policy, authorization, financial controls, and irreversible actions outside model discretion.</p>
        <p>The architecture is complete only when we can explain the normal path, the failure path, the human takeover, and the evidence that proves the final business outcome.</p>
      </div>
    </div>

    <p><strong>Case source:</strong> <a href="https://youtu.be/pyvRID_CZZU?si=jNbxDcPl9lMMhNnD" target="_blank" rel="noopener">AssemblyAI — “We Built an AI Support Agent That Resolves 80% of Tickets”</a>. Supporting technical reference: <a href="https://www.assemblyai.com/blog/build-ai-voice-agent-for-customer-support" target="_blank" rel="noopener">AssemblyAI — Build an AI voice agent for customer support that can look up orders</a>, published 30 Sep 2026. The 80% figure is kept as a case claim and is not used as a general benchmark.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Decision defaults</p><h2>Choose the simplest useful shape.</h2><p>Architecture gets easier when each extra layer has to prove why it is needed.</p></header>
    <div class="research-route-list">
      <a href="/labs/ai-ready/data-rag/"><span>RAG</span><strong>Changing knowledge → retrieval</strong><small>Retrieve current evidence. Fine-tuning is not a database refresh mechanism.</small><i class="material-symbols-outlined" aria-hidden="true">search</i></a>
      <a href="/labs/ai-ready/tools-mcp/"><span>API</span><strong>External fact or action → typed tool</strong><small>Use code to validate inputs, outputs, permissions, and errors.</small><i class="material-symbols-outlined" aria-hidden="true">build</i></a>
      <a href="/labs/ai-ready/tools-mcp/"><span>MCP</span><strong>Shared AI integration → consider MCP</strong><small>Use MCP when several clients benefit from one governed capability surface.</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
      <a href="/labs/ai-ready/agent-architecture/"><span>WF</span><strong>Known sequence → workflow</strong><small>Keep fixed steps fixed. Put the model only where interpretation is useful.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/labs/ai-ready/agent-architecture/"><span>AG</span><strong>Unknown next step → bounded agent</strong><small>Add hard budgets, allowed tools, stop states, and traces.</small><i class="material-symbols-outlined" aria-hidden="true">sync</i></a>
      <a href="/labs/ai-ready/evals-reliability/"><span>FT</span><strong>Behavior gap → prompt/schema/eval first</strong><small>Fine-tune only after a stable measured gap remains.</small><i class="material-symbols-outlined" aria-hidden="true">tune</i></a>
      <a href="/labs/ai-ready/build-operate/#token-economics"><span>COST</span><strong>Growing spend → optimize task economics</strong><small>Measure cost per successful task, then reduce wasted calls, repeated context, excess output, retries, and unnecessary premium-model use.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="labs" data-reveal>
    <header><p class="research-canvas__eyebrow">Hands-on track</p><h2>Build four small systems.</h2><p>All core labs use synthetic general-purpose data. No SAP system, client data, or vendor product is required.</p></header>
    <div class="research-route-list">
      <a href="/labs/ai-ready/labs/mcp-readonly/"><span>01</span><strong>Read-only MCP workspace</strong><small>Expose projects, notes, and tasks through narrow tools and resources.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="/labs/ai-ready/labs/rag-evals/"><span>02</span><strong>RAG with evals</strong><small>Build a small knowledge corpus, retrieve with citations, and measure quality.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="/labs/ai-ready/labs/agent-approval/"><span>03</span><strong>Agent with approval</strong><small>Investigate with read tools, prepare a change, and execute only after approval.</small><i class="material-symbols-outlined" aria-hidden="true">approval</i></a>
      <a href="/labs/ai-ready/labs/production-readiness/"><span>04</span><strong>Production readiness</strong><small>Add versioning, traces, eval gates, budgets, failure policy, and rollback.</small><i class="material-symbols-outlined" aria-hidden="true">rocket_launch</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Machine-readable layer</p><h2>Use the material as data too.</h2><p>The pages explain the ideas. The data files keep reusable patterns and eval cases in a form that can later feed retrieval or an architecture assistant.</p></header>
    <div class="research-route-list">
      <a href="/labs/ai-ready/data/catalog.json"><span>CAT</span><strong>Architecture catalog</strong><small>Tracks, decision rules, use cases, labs, and production rules.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/labs/ai-ready/data/architecture-patterns.json"><span>GRF</span><strong>Architecture patterns</strong><small>Use conditions, controls, failure modes, and graph links.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/ai-ready/data/eval-sample.jsonl"><span>EVAL</span><strong>Eval cases</strong><small>General-purpose architecture decisions and failure-path examples.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Source baseline</p><h2>Date the moving parts.</h2><p>Durable architecture rules live separately from protocol and platform details that change quickly.</p></header>
    <div class="research-route-list">
      <a href="https://blog.modelcontextprotocol.io/posts/2026-07-28/" target="_blank" rel="noopener"><span>MCP</span><strong>Model Context Protocol</strong><small>Official 2026-07-28 release notes. Reviewed 15 Aug 2026.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://platform.openai.com/docs/" target="_blank" rel="noopener"><span>API</span><strong>OpenAI developer documentation</strong><small>Model, tool, MCP, agent, and eval reference. Reviewed 15 Aug 2026.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://www.nist.gov/itl/ai-risk-management-framework" target="_blank" rel="noopener"><span>NIST</span><strong>AI Risk Management Framework</strong><small>Lifecycle risk-management baseline. Reviewed 15 Aug 2026.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://genai.owasp.org/" target="_blank" rel="noopener"><span>OWASP</span><strong>GenAI Security Project</strong><small>Security risks and defensive guidance. Reviewed 15 Aug 2026.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
