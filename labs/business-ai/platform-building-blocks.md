---
layout: default
title: "AI Platform Building Blocks — Capability Roles, Minimum Set and Control Boundaries"
description: "A practical framework for selecting reusable AI platform capabilities by workflow role, dependency, control boundary, and implementation evidence rather than by feature list."
permalink: /labs/business-ai/platform-building-blocks/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-08-19
last_reviewed: 2026-08-19
hide_global_cta: true
publication_wave: "business-ai-platform-building-blocks-01"
review_method: "user-supplied platform capability framework + official OpenAI primary-source verification + editorial synthesis"
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
# ai-discovery-managed:start
primary_topic: "business-ai"
semantic_links:
  - type: "parent_context"
    title: "Business AI Lab — Processes, Patterns, Technologies, Evidence"
    url: "/labs/business-ai/"
  - type: "previous_step"
    title: "AI Fluency: Early Technical Judgment, Confidence and Tradeoffs"
    url: "/labs/ai-fluency/"
  - type: "next_step"
    title: "AI Model Selection — Model Classes, Context, Latency, Cost and Evals"
    url: "/labs/business-ai/model-selection/"
  - type: "next_step"
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
      <h1>Choose capabilities by role.<br />Not by feature count.</h1>
      <p>A platform capability is a reusable technical building block that helps a solution perform one part of the work. It becomes useful only when it is connected to a clear workflow requirement, boundary, dependency, and evidence need.</p>
      <a class="research-canvas__button" href="#capability-roles">Open the capability map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Capability selection sequence">
      <p>Capability selection</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Role</strong><small>What work does it support?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Boundary</strong><small>What access or authority changes?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Evidence</strong><small>What must be tested?</small></div>
      <em>The smallest responsible capability set is usually easier to validate, operate, and hand over.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">view_in_ar</span>
    <p><strong>Platform building block.</strong> A reusable capability that performs one technical role inside a larger workflow, such as retrieval, structured output, tool use, orchestration, evaluation, or monitoring.</p>
    <p><strong>Working rule.</strong> Do not add a capability because it exists. Add it because the workflow needs the role it performs and the team can support the dependency and control it introduces.</p>
  </section>

  <section class="research-canvas__inventory" id="feature-first" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Feature-first risk</p>
      <h2>Feature-first thinking creates weak recommendations.</h2>
      <p>Adding capabilities before the workflow is clear often increases complexity before the team has confirmed the user need, source content, output contract, action boundary, risk level, or evidence required.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Before adding a capability</h3>
        <ul>
          <li>What role does this capability play in the workflow?</li>
          <li>What dependency or control does it introduce?</li>
          <li>What would happen if we left it out of the first version?</li>
          <li>What must be validated before recommending it?</li>
        </ul>
      </div>
      <div>
        <h3>Common result of feature-first design</h3>
        <ul>
          <li>Overbuilt first releases</li>
          <li>More permissions than the workflow needs</li>
          <li>Harder evaluation and failure diagnosis</li>
          <li>Unclear ownership across platform, data, security, and integration teams</li>
          <li>Expensive handover and support</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="capability-roles" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Capability roles</p>
      <h2>Group capabilities by the job they perform.</h2>
      <p>The same product feature can be useful in one workflow and unnecessary in another. Capability roles make the reasoning more stable than a product checklist.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Role</th><th scope="col">What it does</th><th scope="col">Example</th><th scope="col">Main design question</th></tr></thead>
        <tbody>
          <tr><th scope="row">Interaction</th><td>Defines how a user or system asks for work and receives a result.</td><td>A sales user requests an account brief through an internal application or workflow.</td><td>What input and output contract does the workflow need?</td></tr>
          <tr><th scope="row">Context</th><td>Provides the business information required to produce a useful result.</td><td>Approved account notes, opportunity data, call summaries, policies, or product information.</td><td>Which sources are trustworthy, current, permitted, and relevant?</td></tr>
          <tr><th scope="row">Action</th><td>Uses tools or affects another system.</td><td>Check CRM status, run a calculation, create a draft task, or prepare an update for approval.</td><td>Is the capability read-only, recommending, or changing business state?</td></tr>
          <tr><th scope="row">Orchestration</th><td>Coordinates multi-step work and handoffs.</td><td>Collect request, retrieve context, check missing fields, draft, review, then prepare a next step.</td><td>Which steps are deterministic, model-led, tool-led, or human-led?</td></tr>
          <tr><th scope="row">Evaluation</th><td>Tests quality and reliability.</td><td>Check completeness, source grounding, required format, tool correctness, and workflow usefulness.</td><td>What evidence changes the release decision?</td></tr>
          <tr><th scope="row">Developer workflow</th><td>Supports builders who implement, test, review, and maintain the solution.</td><td>Coding agents and development tooling can help implement changes, add tests, and review code.</td><td>How are generated changes reviewed, tested, and owned?</td></tr>
          <tr><th scope="row">Governance and observability</th><td>Controls access and creates evidence about real operation.</td><td>Permissions, approval points, traces, logs, usage signals, quality checks, and escalation paths.</td><td>Can the team explain who may do what, what happened, and who responds when it fails?</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="minimum-set" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Minimum viable capability set</p>
      <h2>Start with the smallest responsible combination.</h2>
      <p>A minimum viable capability set is the smallest set of capabilities needed for the workflow to succeed responsibly. Minimum does not mean uncontrolled. It means no extra architecture without a justified role.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Decision</th><th scope="col">Question</th></tr></thead>
        <tbody>
          <tr><th scope="row">Required now</th><td>Which capabilities are necessary for the first useful workflow?</td></tr>
          <tr><th scope="row">Later</th><td>Which capabilities can wait until value and operating evidence are stronger?</td></tr>
          <tr><th scope="row">Added burden</th><td>Which capabilities add risk, complexity, cost, latency, or support effort?</td></tr>
          <tr><th scope="row">Dependencies</th><td>Which capabilities depend on source quality, permissions, integration readiness, or environment maturity?</td></tr>
          <tr><th scope="row">Validation owner</th><td>Which choices need product, security, data, integration, architecture, or implementation review?</td></tr>
        </tbody>
      </table>
      <p><strong>Lead test:</strong> if removing a capability does not materially weaken the first workflow, it probably does not belong in the first version.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="interaction-layer" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Interaction layer</p>
      <h2>Design the handoff, not only the prompt.</h2>
      <p>The interaction layer is where an application, workflow, or system asks AI to perform work and receives an output it can use.</p>
    </header>

    <section class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span>
      <p><strong>Workflow handoff:</strong> Request → Instructions → Inputs → Context → Output → Review or action.</p>
    </section>

    <div class="research-canvas__table-wrap">
      <h3>Design outputs for downstream use</h3>
      <table>
        <thead><tr><th scope="col">Need</th><th scope="col">Capability signal</th><th scope="col">Control question</th></tr></thead>
        <tbody>
          <tr><th scope="row">Consistent machine-readable output</th><td>Structured output with a defined schema can create a stronger contract for downstream systems.</td><td>Is schema compliance enough, or must business rules validate the values too?</td></tr>
          <tr><th scope="row">Source evidence</th><td>Retrieval evidence or source references may be required.</td><td>Which sources are approved and how is missing evidence handled?</td></tr>
          <tr><th scope="row">Human review</th><td>Add an explicit review point before customer-facing or material use.</td><td>What exactly must the reviewer decide?</td></tr>
          <tr><th scope="row">System update</th><td>Tool use may be needed to prepare or execute an action.</td><td>Does the tool only read, propose, or change business state?</td></tr>
        </tbody>
      </table>
    </div>

    <div class="ecg-decision-columns">
      <div>
        <h3>Modality questions</h3>
        <ul>
          <li>What modality does the user provide?</li>
          <li>What modality should the system return?</li>
          <li>How quickly does the response need to happen?</li>
          <li>Can the workflow tolerate delay?</li>
        </ul>
      </div>
      <div>
        <h3>Operating questions</h3>
        <ul>
          <li>What data is captured, stored, or reviewed?</li>
          <li>What privacy, consent, or accessibility needs apply?</li>
          <li>What happens when the system misreads, mishears, or lacks confidence?</li>
          <li>How will quality be evaluated?</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="context-layer" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Context layer</p>
      <h2>Retrieval only helps when useful sources exist.</h2>
      <p>Many workflows need business-specific context such as approved documents, policies, knowledge bases, support content, customer records, product information, workflow history, or previous outputs.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Retrieval fit</h3>
        <p>Retrieval or File Search-style support is useful when the workflow has source content that can materially support the answer or output.</p>
        <ul>
          <li>Are there trustworthy source documents or records?</li>
          <li>Is ownership clear?</li>
          <li>Are access permissions suitable for the requesting user?</li>
          <li>Is the content current enough for the task?</li>
        </ul>
      </div>
      <div>
        <h3>Retrieval readiness</h3>
        <p>Do not treat retrieval as a box that automatically creates grounding.</p>
        <ul>
          <li>Can the team test whether the right information is found?</li>
          <li>Can missing or conflicting evidence be detected?</li>
          <li>Can source access be filtered correctly?</li>
          <li>Who updates or retires weak sources?</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="tools" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Action layer</p>
      <h2>Separate information access from business authority.</h2>
      <p>Tools let an AI-supported workflow call functions, services, APIs, or external systems. The most important early distinction is whether a tool only reads information or can change something.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Tool boundary</th><th scope="col">Example</th><th scope="col">What changes</th></tr></thead>
        <tbody>
          <tr><th scope="row">Read-only</th><td>Look up vendor status, policy status, stock, account information, or contract metadata.</td><td>The main risks are access, privacy, relevance, and incorrect interpretation.</td></tr>
          <tr><th scope="row">Prepare or recommend</th><td>Draft a CRM update, proposed purchase request, or next action for review.</td><td>Review quality and evidence become part of the workflow.</td></tr>
          <tr><th scope="row">Action-taking</th><td>Update a field, create a task, submit a transaction, or trigger another process.</td><td>Authorization, validation, approval, idempotency, audit, and recovery become stronger requirements.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Before recommending tool use</h3>
      <table>
        <thead><tr><th scope="col">Question</th><th scope="col">Why it matters</th></tr></thead>
        <tbody>
          <tr><th scope="row">Which tools are needed?</th><td>Avoid broad tool access when the workflow needs only a small set.</td></tr>
          <tr><th scope="row">Which tools are read-only or action-taking?</th><td>Authority changes the control model.</td></tr>
          <tr><th scope="row">What actions are allowed or restricted?</th><td>Tool availability is not the same as business authorization.</td></tr>
          <tr><th scope="row">What requires human approval?</th><td>Approval should sit before material business state changes where required.</td></tr>
          <tr><th scope="row">What happens if a call fails?</th><td>Failure handling, retries, fallback, and duplicate protection may be needed.</td></tr>
          <tr><th scope="row">What should be logged?</th><td>Operations need enough evidence to reconstruct what happened.</td></tr>
          <tr><th scope="row">Who owns the integration?</th><td>Someone must maintain contracts, credentials, changes, and recovery.</td></tr>
          <tr><th scope="row">What should be tested?</th><td>Correct tool choice, valid arguments, authorization, failure behavior, and side effects all need evidence.</td></tr>
        </tbody>
      </table>
    </div>

    <section class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">hub</span>
      <p><strong>MCP-style connections.</strong> MCP can be relevant when a workflow needs repeatable access to external tools or context. Treat it as a connection and tool-governance mechanism, not as permission to bypass identity, authorization, approval, logging, or recovery design.</p>
    </section>
  </section>

  <section class="research-canvas__inventory" id="evaluation-observability" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Evaluation and observability</p>
      <h2>Every capability creates a new proof obligation.</h2>
      <p>The capability set determines what must be evaluated and what must be visible in operation.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Capability</th><th scope="col">What should be evaluated</th><th scope="col">What should be observable</th></tr></thead>
        <tbody>
          <tr><th scope="row">Retrieval</th><td>Source relevance, permission filtering, groundedness, missing evidence.</td><td>Which sources were retrieved and used.</td></tr>
          <tr><th scope="row">Structured output</th><td>Schema compliance plus task-specific field correctness.</td><td>Validation failures and downstream rejection.</td></tr>
          <tr><th scope="row">Tool use</th><td>Tool selection, arguments, permissions, failure handling, side effects.</td><td>Tool calls, results, errors, approvals, and business outcome.</td></tr>
          <tr><th scope="row">Orchestration</th><td>Step sequence, routing, handoffs, state, fallback.</td><td>Trace across model, tool, rule, and human steps.</td></tr>
          <tr><th scope="row">Human review</th><td>Whether review catches meaningful errors and supports a clear decision.</td><td>Approval, rejection, correction, escalation, and ownership.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sap-example" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SAP Lead example</p>
      <h2>Build a procurement assistant from the minimum set.</h2>
      <p>A procurement assistant may need to check vendor status before helping a business user prepare an intake request. Start with the smallest useful version and add authority only when evidence supports it.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Version</th><th scope="col">Capability set</th><th scope="col">Why</th></tr></thead>
        <tbody>
          <tr><th scope="row">V1: read and summarize</th><td>Interaction + approved context + read-only vendor lookup + structured summary + evals.</td><td>Useful without changing SAP or another business system.</td></tr>
          <tr><th scope="row">V2: prepare next step</th><td>Add orchestration and a tool that prepares a request or update for human review.</td><td>Reduces manual work while keeping business authority with a person.</td></tr>
          <tr><th scope="row">V3: controlled action</th><td>Add action-taking tools only after permissions, approval rules, business validation, logging, failure handling, and recovery are validated.</td><td>Higher automation now has a matching control and evidence model.</td></tr>
        </tbody>
      </table>
      <p><strong>Lead point:</strong> the platform decision follows the workflow maturity. V1 does not need every capability that V3 may eventually require.</p>
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Assessment shortcut</p><h2>Use six questions before naming a platform feature.</h2></div>
    <ol>
      <li><span>01</span><strong>Workflow</strong><p>What work must the solution support?</p></li>
      <li><span>02</span><strong>Role</strong><p>Which capability role is actually missing?</p></li>
      <li><span>03</span><strong>Minimum</strong><p>What is the smallest responsible set for the first version?</p></li>
      <li><span>04</span><strong>Boundary</strong><p>What new data, permission, tool, or action boundary appears?</p></li>
      <li><span>05</span><strong>Proof</strong><p>What must be evaluated and observed?</p></li>
      <li><span>06</span><strong>Owner</strong><p>Who maintains the capability and responds when it changes or fails?</p></li>
    </ol>
  </section>

  <section class="research-canvas__inventory" id="verified-platform-notes" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Current platform examples</p>
      <h2>Examples are implementation options, not the framework itself.</h2>
      <p>Current OpenAI platform documentation includes built-in File Search, function calling, remote MCP tools, and structured JSON Schema outputs. Codex is positioned as a coding agent for codebase understanding, implementation, testing, and review. Product details change faster than the workflow roles above, so verify current availability before making a customer-specific recommendation.</p>
    </header>
    <ul>
      <li><a href="https://platform.openai.com/docs/quickstart/make-your-first-api-request">OpenAI API quickstart and tools</a></li>
      <li><a href="https://platform.openai.com/docs/api-reference/evals/deleteRun?lang=python">OpenAI API reference — Structured Outputs example</a></li>
      <li><a href="https://platform.openai.com/docs/api-reference/realtime-client-events/session?lang=node.js">OpenAI API reference — remote MCP tool fields</a></li>
      <li><a href="https://developers.openai.com/">OpenAI Developers — Codex developer workflow</a></li>
    </ul>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span>
    <p><strong>Continue the reasoning:</strong> start with <a href="/labs/ai-fluency/">AI Fluency</a> to define the workflow, confidence, and tradeoffs. Use this capability map to build the minimum responsible technical set. Then use <a href="/labs/business-ai/model-selection/">AI Model Selection</a> and <a href="/labs/business-ai/implementation-readiness/">AI Implementation Readiness</a> to validate the model, controls, release evidence, and operating plan.</p>
  </section>
</div>
