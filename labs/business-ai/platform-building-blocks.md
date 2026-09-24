---
layout: default
title: "AI Platform Building Blocks — Capability Roles, Minimum Set and Control Boundaries"
description: "A practical framework for selecting reusable AI platform capabilities by workflow role, dependency, control boundary, and implementation evidence rather than by feature list."
permalink: /labs/business-ai/platform-building-blocks/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-24
last_reviewed: 2026-09-24
hide_global_cta: true
publication_wave: "business-ai-platform-building-blocks-01"
review_method: "current SAP, OpenAI and MCP primary documentation + adjacent Labs review + full editorial rewrite"
evidence_review_mode: "selective_or_heuristic"
search_intent: "AI platform building blocks capability roles interaction context retrieval tools orchestration evaluation governance MCP"
structured_data:
  type: TechArticle
tags:
  - business-ai
  - ai-fluency
  - platform-capabilities
  - retrieval
  - tools
  - orchestration
  - evaluation
  - governance
  - mcp
career_impact: mapped
career_skills:
  - ai-readiness
  - ai-retrieval
  - ai-agents-mcp
  - ai-evaluation
  - ai-security
source_links:
  - title: "SAP Cloud SDK for AI — Orchestration Service V2 API"
    url: "https://help.sap.com/doc/generative-ai-hub-sdk/CLOUD/en-US/_reference/orchestration-service2.html"
  - title: "SAP Cloud SDK for AI — Document Grounding"
    url: "https://help.sap.com/doc/generative-ai-hub-sdk/CLOUD/en-US/_reference/document-grounding.html"
  - title: "OpenAI API — File Search"
    url: "https://developers.openai.com/api/docs/guides/tools-file-search"
  - title: "OpenAI API — Function Calling"
    url: "https://developers.openai.com/api/docs/guides/function-calling"
  - title: "Model Context Protocol — 2026-07-28 specification release"
    url: "https://blog.modelcontextprotocol.io/posts/2026-07-28/"
# ai-discovery-managed:start
primary_topic: "business-ai"
ai_sidecar: "/ai/pages/labs--business-ai--platform-building-blocks.json"
semantic_links:
  - type: "same_domain"
    title: "Business AI Glossary — Plain Language for Discovery, Architecture, Governance and Delivery"
    url: "/labs/business-ai/glossary/"
  - type: "same_domain"
    title: "AI Architecture Patterns — From Reusable Shapes to First-Pass Blueprints"
    url: "/labs/business-ai/architecture-patterns/"
  - type: "same_domain"
    title: "AI Model Selection — Model Classes, Context, Latency, Cost and Evals"
    url: "/labs/business-ai/model-selection/"
  - type: "parent_context"
    title: "Business AI Lab — Processes, Patterns, Technologies, Evidence"
    url: "/labs/business-ai/"
  - type: "same_domain"
    title: "ERP Agent Gateway Pilot — Safe AI Tool Access to Enterprise Systems"
    url: "/labs/business-ai/erp-agent-gateway/"
  - type: "same_domain"
    title: "AI Implementation Readiness — Evals, Safeguards, Observability, Release and Rollback"
    url: "/labs/business-ai/implementation-readiness/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li aria-current="page">Platform Building Blocks</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / platform building blocks</p>
      <h1>Build only the capabilities<br />the workflow earns.</h1>
      <p>An enterprise AI platform is easy to over-design because almost every capability looks useful in isolation. The better question is narrower: what must this workflow know, decide, call, remember, prove, and control? The platform should supply those roles with as little extra machinery as possible.</p>
      <a class="research-canvas__button" href="#capability-roles">Open the capability map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Capability selection sequence">
      <p>Capability selection</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Work</strong><small>What must happen?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Role</strong><small>What capability is missing?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Boundary</strong><small>What access or authority changes?</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>Proof</strong><small>How will we know it works?</small></div>
      <em>A smaller platform surface is usually easier to secure, test, operate, and hand over.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">view_in_ar</span>
    <div>
      <p><strong>A building block is not an architecture pattern.</strong> Retrieval, tool calling, structured output, model access, workflow state, tracing, and filtering are reusable capabilities. An architecture pattern explains how selected capabilities work together in one business flow.</p>
      <p>This distinction keeps platform design honest. A feature can be technically impressive and still have no job in the first release.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="feature-first" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Feature-first risk</p>
      <h2>A capability should enter the design because a workflow needs it.</h2>
      <p>Starting from a platform catalogue reverses the reasoning. Teams end up adding retrieval before they know the source of truth, agents before they know why several steps need model-led coordination, or write tools before the approval and recovery model is ready.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Useful reason to add something</h3>
        <p>The workflow has a concrete gap: missing business context, a required external action, a machine-readable output contract, several dependent steps, or evidence that operations must capture.</p>
      </div>
      <div>
        <h3>Weak reason</h3>
        <p>The product supports it, a demo used it, or it sounds like part of a modern AI stack. Those facts may justify exploration, but they do not justify production complexity.</p>
      </div>
      <div>
        <h3>The practical test</h3>
        <p>Remove the capability from the first design. If the useful business outcome is still achievable with acceptable risk and effort, the capability can probably wait.</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="capability-roles" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Capability roles</p>
      <h2>Map the platform to six jobs.</h2>
      <p>Products package these jobs differently, but the roles stay relatively stable. They are a better design vocabulary than a permanent list of product features.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Role</th><th scope="col">What it contributes</th><th scope="col">Main design question</th></tr></thead>
        <tbody>
          <tr><th scope="row">Interaction and contract</th><td>Accepts a request and returns text, structured data, audio, a tool request, or another usable result.</td><td>What must the consumer receive, and how strict is that contract?</td></tr>
          <tr><th scope="row">Context and evidence</th><td>Supplies knowledge, documents, live enterprise state, conversation history, or other information the model needs.</td><td>Which source is authoritative for this question, and is the user allowed to see it?</td></tr>
          <tr><th scope="row">Model and inference</th><td>Performs the probabilistic work: interpretation, extraction, drafting, classification, reasoning, or routing.</td><td>Which capability and configuration meet the quality, latency, cost, and modality requirement?</td></tr>
          <tr><th scope="row">Tools and actions</th><td>Lets the workflow read from or act on external systems through explicit functions, APIs, or services.</td><td>What may be requested, what may actually execute, and where is business authorization enforced?</td></tr>
          <tr><th scope="row">Orchestration and state</th><td>Coordinates dependent steps, deterministic logic, model calls, tools, retries, handoffs, and durable workflow state.</td><td>Which steps need coordination, and which decisions should remain deterministic?</td></tr>
          <tr><th scope="row">Assurance</th><td>Provides evaluation, policy enforcement, observability, audit evidence, release controls, and operational ownership.</td><td>How do we prove the workflow behaves acceptably and reconstruct what happened when it does not?</td></tr>
        </tbody>
      </table>
    </div>

    <p>Developer tooling supports the lifecycle around these runtime roles. Coding agents, test tools, deployment automation, and review systems can accelerate implementation, but they are not automatically part of the production AI path used by the business user.</p>
  </section>

  <section class="research-canvas__inventory" id="minimum-set" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Minimum capability set</p>
      <h2>Add the next block only when the simpler path stops being enough.</h2>
      <p>The first useful version often needs fewer AI-specific components than expected. Start from the business input and output, then add capabilities in response to a real dependency.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">If the workflow needs...</th><th scope="col">Add...</th><th scope="col">Do not confuse it with...</th></tr></thead>
        <tbody>
          <tr><th scope="row">A bounded transformation of provided input</th><td>Model access plus a clear input/output contract.</td><td>Retrieval or an agent merely because the task uses AI.</td></tr>
          <tr><th scope="row">Approved knowledge not present in the request</th><td>Retrieval or another governed context source.</td><td>A replacement for current transactional truth.</td></tr>
          <tr><th scope="row">Current enterprise state or a deterministic calculation</th><td>A read tool or approved application/API call.</td><td>Document retrieval from an old snapshot.</td></tr>
          <tr><th scope="row">A business side effect</th><td>A narrow action tool plus authorization, validation, approval where required, and recovery.</td><td>The model's decision to call the tool.</td></tr>
          <tr><th scope="row">Several dependent steps or handoffs</th><td>Orchestration and explicit workflow state.</td><td>Dynamic agent routing when a fixed sequence is sufficient.</td></tr>
          <tr><th scope="row">Production operation</th><td>Evaluation and observability proportional to the consequence of failure.</td><td>A dashboard with no release or support decision attached to it.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="interaction-layer" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Interaction and contract</p>
      <h2>The handoff matters more than the prompt.</h2>
      <p>The model sits inside a larger interface. What matters downstream is not whether the answer looks fluent, but whether the next user or system can use it safely and predictably.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Human-facing result</h3>
        <p>A narrative answer can stay flexible when a person is expected to interpret it. The workflow still needs clear source boundaries, uncertainty handling, and escalation when the answer is material.</p>
      </div>
      <div>
        <h3>Machine-facing result</h3>
        <p>Structured output can enforce a stronger syntactic contract for downstream processing. Schema validity does not prove that a supplier number, amount, date, or business decision is correct, so semantic and business validation remain separate.</p>
      </div>
      <div>
        <h3>Action request</h3>
        <p>A tool call is a request from the model to perform a defined operation. The application or tool runtime still decides how that request is validated, authorized, executed, recorded, and returned.</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="context-layer" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Context and evidence</p>
      <h2>Knowledge retrieval and enterprise state are different evidence problems.</h2>
      <p>This is one of the most important distinctions in SAP-oriented AI design. Policies and manuals are often good retrieval material. A current delivery block, supplier status, credit exposure, or purchase-order value normally belongs to a live business-system query.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Evidence type</th><th scope="col">Typical source</th><th scope="col">Design concern</th></tr></thead>
        <tbody>
          <tr><th scope="row">Static or slowly changing knowledge</th><td>Policies, procedures, product documentation, support knowledge, approved guidance.</td><td>Retrieval quality, source ownership, freshness, access filtering, and conflicting documents.</td></tr>
          <tr><th scope="row">Current enterprise state</th><td>SAP or another system of record through an approved interface.</td><td>Identity, authorization, transaction freshness, field semantics, and business-object scope.</td></tr>
          <tr><th scope="row">Session or workflow state</th><td>Conversation history or explicit workflow storage.</td><td>What must persist, for how long, and whether stale state can change the next decision.</td></tr>
        </tbody>
      </table>
    </div>

    <p>SAP's current Document Grounding capability is a concrete RAG implementation for retrieving context from configured document sources. That is useful for knowledge evidence. It does not remove the need for a live SAP interface when the answer depends on the current state of a business object.</p>
  </section>

  <section class="research-canvas__inventory" id="tools" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Tools and authority</p>
      <h2>Tool connectivity expands capability; it does not grant business authority.</h2>
      <p>Function calling and MCP-style connections make external operations available to a model-driven workflow. The security boundary still belongs to the surrounding system: identity, scopes, application roles, allowed objects, validation, approval, transaction handling, and audit.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Tool level</th><th scope="col">Example</th><th scope="col">What the platform must add</th></tr></thead>
        <tbody>
          <tr><th scope="row">Read</th><td>Read current supplier, order, inventory, or account state.</td><td>Scoped identity, authorization, input validation, source semantics, and traceable results.</td></tr>
          <tr><th scope="row">Prepare</th><td>Create a draft payload or proposed update for review.</td><td>Business-rule validation, evidence for the proposal, and a clear approval decision.</td></tr>
          <tr><th scope="row">Execute</th><td>Post or update enterprise state.</td><td>All of the above plus transaction controls, duplicate protection, outcome reconciliation, audit, and recovery.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">hub</span>
      <div>
        <p><strong>MCP is an integration protocol, not an enterprise permission model.</strong> The current 2026-07-28 specification improves transport, discovery, routing, and authorization mechanics, but a connected tool still needs the application's business-level access and execution controls.</p>
        <p>The same rule applies to native function calling. OpenAI's current function-calling flow explicitly leaves function execution to application code after the model emits a tool request. SAP AI Core Orchestration V2 likewise supports tool calling while leaving the caller responsible for executing tools and continuing the loop.</p>
      </div>
    </div>

    <p>For a deeper execution design, use the <a href="/labs/business-ai/erp-agent-gateway/">ERP Agent Gateway</a> guide. It covers the propose → authorize → execute → reconcile boundary in more detail.</p>
  </section>

  <section class="research-canvas__inventory" id="evaluation-observability" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Assurance</p>
      <h2>Each new capability creates a new thing that can fail.</h2>
      <p>Evaluation and observability should follow the workflow's actual composition. Adding retrieval, tools, or orchestration increases both the possible value and the proof burden.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Capability</th><th scope="col">What to prove before release</th><th scope="col">What to reconstruct in operation</th></tr></thead>
        <tbody>
          <tr><th scope="row">Model and output contract</th><td>Task quality, critical failures, schema or format reliability.</td><td>Model/configuration version, relevant request context, validation result.</td></tr>
          <tr><th scope="row">Retrieval</th><td>Relevant source selection, access filtering, missing/conflicting evidence behavior.</td><td>Which evidence was retrieved and which source governed the answer.</td></tr>
          <tr><th scope="row">Tools</th><td>Correct tool choice, arguments, authorization behavior, expected side effects, failure recovery.</td><td>Requested operation, validation, approval, execution result, and final business state where material.</td></tr>
          <tr><th scope="row">Orchestration</th><td>Step ordering, handoffs, retries, state transitions, and fallback.</td><td>The path across deterministic logic, model calls, tools, and human decisions.</td></tr>
        </tbody>
      </table>
    </div>

    <p>The release and operating model belongs in <a href="/labs/business-ai/implementation-readiness/">AI Implementation Readiness</a>. The important point here is simpler: a platform feature is not complete when it can be called; it is complete when the team can test, observe, own, and recover it in the intended workflow.</p>
  </section>

  <section class="research-canvas__inventory" id="sap-example" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SAP example</p>
      <h2>Design a supplier assistant without turning every capability on.</h2>
      <p>Suppose a buyer asks whether a supplier can be used for a planned purchase and what to do next. That sounds like one question, but it contains two evidence types and potentially one action boundary.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Need</th><th scope="col">Capability</th><th scope="col">Boundary</th></tr></thead>
        <tbody>
          <tr><th scope="row">Understand the request</th><td>Model plus a clear interaction/output contract.</td><td>The model interprets the request; it does not invent missing organizational context.</td></tr>
          <tr><th scope="row">Explain procurement policy</th><td>Retrieval over approved policy or operating guidance.</td><td>Retrieved text is explanatory knowledge, not proof of the supplier's current SAP state.</td></tr>
          <tr><th scope="row">Check current supplier state</th><td>Read-only call through an approved SAP interface.</td><td>The user's identity and SAP authorization determine what may be read.</td></tr>
          <tr><th scope="row">Combine the evidence</th><td>Model generates a concise explanation and structured next-step proposal.</td><td>Deterministic checks validate required fields and allowed values.</td></tr>
          <tr><th scope="row">First release</th><td>No write tool.</td><td>The assistant remains read-only. A buyer performs the business action through the normal process.</td></tr>
          <tr><th scope="row">Later automation</th><td>Add a narrow prepare or execute tool only when the workflow, authorization, approval, transaction, and recovery model are proven.</td><td>More automation is an authority decision, not merely a platform upgrade.</td></tr>
        </tbody>
      </table>
    </div>

    <p>This example does not require an autonomous agent to be useful. A fixed sequence — interpret → retrieve policy → read SAP state → explain — may be easier to validate and support. Orchestration becomes more valuable when the workflow truly needs branching, retries, several tools, durable state, or specialist handoffs.</p>
  </section>

  <section class="research-canvas__inventory" id="verified-platform-notes" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Current implementation examples</p>
      <h2>The same capability roles appear in different platform products.</h2>
      <p>Use product documentation to confirm the implementation option, but keep the workflow reasoning above vendor-neutral enough to survive product changes.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Capability role</th><th scope="col">Current example</th><th scope="col">What the documentation establishes</th></tr></thead>
        <tbody>
          <tr><th scope="row">Model orchestration</th><td><a href="https://help.sap.com/doc/generative-ai-hub-sdk/CLOUD/en-US/_reference/orchestration-service2.html">SAP AI Core Orchestration Service V2</a></td><td>Provides model orchestration modules including templating, content filtering, data masking, and tool calling.</td></tr>
          <tr><th scope="row">Knowledge retrieval</th><td><a href="https://help.sap.com/doc/generative-ai-hub-sdk/CLOUD/en-US/_reference/document-grounding.html">SAP Document Grounding</a></td><td>Implements retrieval-augmented generation over configured document knowledge sources.</td></tr>
          <tr><th scope="row">Hosted file retrieval</th><td><a href="https://developers.openai.com/api/docs/guides/tools-file-search">OpenAI File Search</a></td><td>Lets Responses API models search uploaded knowledge bases through a hosted semantic and keyword retrieval tool.</td></tr>
          <tr><th scope="row">Application tools</th><td><a href="https://developers.openai.com/api/docs/guides/function-calling">OpenAI Function Calling</a></td><td>The model requests a function; application code executes it and returns the result to the model.</td></tr>
          <tr><th scope="row">Standardized tool connection</th><td><a href="https://blog.modelcontextprotocol.io/posts/2026-07-28/">Model Context Protocol 2026-07-28</a></td><td>Defines current protocol mechanics for connecting AI applications to tools and context, including updated discovery, routing, and authorization behavior.</td></tr>
        </tbody>
      </table>
    </div>

    <p>These are examples, not a mandatory stack. A SAP-centric workflow may use SAP AI Core capabilities, another model platform, normal application APIs, or a combination. The design question stays the same: which capability has a justified role, and which system remains authoritative for the business decision?</p>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span>
    <div>
      <p><strong>Continue the reasoning:</strong> use <a href="/labs/business-ai/architecture-patterns/">Architecture Patterns</a> when the question is how these capabilities should fit together. Use <a href="/labs/business-ai/model-selection/">AI Model Selection</a> for the inference choice, and <a href="/labs/business-ai/implementation-readiness/">AI Implementation Readiness</a> for release evidence, observability, and recovery.</p>
    </div>
  </section>
</div>
