---
layout: default
title: "AI Architecture Patterns — From Reusable Shapes to First-Pass Blueprints"
description: "A practical framework for choosing a simple AI solution shape, separating patterns from capabilities and controls, and turning it into a first-pass enterprise blueprint."
permalink: /labs/business-ai/architecture-patterns/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-24
last_reviewed: 2026-09-24
hide_global_cta: true
publication_wave: "business-ai-architecture-patterns-01"
review_method: "current SAP and Microsoft primary sources + adjacent Labs review + full editorial pass"
evidence_review_mode: "selective_or_heuristic"
search_intent: "AI architecture patterns lightweight first pass blueprint pressure test retrieval grounded generation agentic orchestration human review enterprise integration"
structured_data:
  type: TechArticle
tags:
  - business-ai
  - architecture-patterns
  - blueprint
  - retrieval
  - agentic-orchestration
  - human-in-the-loop
  - enterprise-integration
  - evaluation
career_impact: mapped
career_skills:
  - ai-readiness
  - ai-retrieval
  - ai-agents-mcp
  - ai-evaluation
  - delivery-lifecycle
source_links:
  - title: "SAP Cloud SDK for AI — Orchestration Service V2 API"
    url: "https://help.sap.com/doc/generative-ai-hub-sdk/CLOUD/en-US/_reference/orchestration-service2.html"
  - title: "SAP Cloud SDK for AI — Document Grounding"
    url: "https://help.sap.com/doc/generative-ai-hub-sdk/CLOUD/en-US/_reference/document-grounding.html"
  - title: "Microsoft Azure Architecture Center — AI Agent Orchestration Patterns"
    url: "https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns"
# ai-discovery-managed:start
primary_topic: "business-ai"
ai_sidecar: "/ai/pages/labs--business-ai--architecture-patterns.json"
semantic_links:
  - type: "same_domain"
    title: "AI Model Selection — Model Classes, Context, Latency, Cost and Evals"
    url: "/labs/business-ai/model-selection/"
  - type: "same_domain"
    title: "AI Platform Building Blocks — Capability Roles, Minimum Set and Control Boundaries"
    url: "/labs/business-ai/platform-building-blocks/"
  - type: "parent_context"
    title: "Business AI Lab — Processes, Patterns, Technologies, Evidence"
    url: "/labs/business-ai/"
  - type: "same_domain"
    title: "Business AI Glossary — Plain Language for Discovery, Architecture, Governance and Delivery"
    url: "/labs/business-ai/glossary/"
  - type: "same_domain"
    title: "Document-to-ERP AI Pilot — From PDF to Controlled Transaction"
    url: "/labs/business-ai/document-to-erp-ai/"
  - type: "same_domain"
    title: "ERP Agent Gateway Pilot — Safe AI Tool Access to Enterprise Systems"
    url: "/labs/business-ai/erp-agent-gateway/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li aria-current="page">Architecture Patterns</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / architecture patterns</p>
      <h1>Choose the smallest shape<br />that solves the workflow.</h1>
      <p>An AI architecture pattern is a reusable arrangement of model reasoning, business context, tools, workflow logic, and control points. It helps us decide how a solution should behave before we commit to products, APIs, deployment details, or a final security design.</p>
      <a class="research-canvas__button" href="#pattern-levels">Follow the architecture model <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Architecture reasoning sequence">
      <p>Architecture reasoning</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Work</strong><small>What must happen?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Pattern</strong><small>What solution shape fits?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Boundary</strong><small>What may it know and do?</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>Proof</strong><small>What still needs validation?</small></div>
      <em>Complexity should be earned by the workflow.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <div>
      <p><strong>Pattern is not capability.</strong> Retrieval, structured output, tool calling, multimodal input, filtering, evaluation, and monitoring are capabilities. Human approval is a control. They become part of an architecture pattern only when the workflow gives them a specific role and relationship.</p>
      <p>This distinction matters because a feature list does not explain a system. Architecture explains how information and authority move through it.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="pattern-levels" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Three levels</p>
      <h2>Separate the reusable pattern from the workflow blueprint and the final design.</h2>
      <p>The three levels carry different amounts of certainty. Keeping them separate prevents an early idea from looking more proven than it is.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Level</th><th scope="col">What it decides</th><th scope="col">Example</th></tr></thead>
        <tbody>
          <tr><th scope="row">Architecture pattern</th><td>The reusable relationship between model, context, tools, workflow logic, and people.</td><td>Retrieve approved policy content, generate an answer, and abstain when evidence is weak.</td></tr>
          <tr><th scope="row">First-pass blueprint</th><td>How that shape applies to one business workflow, including authority and open assumptions.</td><td>A sales user asks why an order is credit blocked; the workflow reads current SAP state, retrieves policy guidance, explains the result, and remains read-only.</td></tr>
          <tr><th scope="row">Final technical design</th><td>The validated implementation: interfaces, identity, data movement, platform configuration, controls, observability, release, and support.</td><td>The approved SAP interface, authorization model, runtime, error handling, evaluation thresholds, monitoring, and operating ownership are fixed and tested.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="pattern-families" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Working pattern families</p>
      <h2>Start with four shapes before combining anything.</h2>
      <p>This is a practical taxonomy, not a vendor standard. The point is to expose the main dependency that makes the workflow useful.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Pattern</th><th scope="col">Use it when</th><th scope="col">Main architectural question</th></tr></thead>
        <tbody>
          <tr><th scope="row">Bounded model transformation</th><td>The input already contains what the model needs and the task is mainly classification, summarization, extraction, translation, or structured transformation.</td><td>What output contract and validation make the result usable?</td></tr>
          <tr><th scope="row">Retrieval-grounded response</th><td>The answer depends on approved knowledge that is too specific, changeable, or extensive to rely on model memory.</td><td>Which sources are authoritative and permitted for this user and task?</td></tr>
          <tr><th scope="row">Tool-assisted workflow</th><td>The solution must read current system state, run a deterministic function, or prepare an action through an external capability.</td><td>What may the model request, and what business checks remain outside the model?</td></tr>
          <tr><th scope="row">Orchestrated workflow</th><td>The task needs several dependent steps, dynamic routing, retries, specialist handoffs, or coordinated tools.</td><td>Which decisions genuinely need model-led routing, and which should remain deterministic?</td></tr>
        </tbody>
      </table>
    </div>

    <p>Multimodal input, ranking, human review, guardrails, and observability can support any of these shapes. Treating them as separate top-level architectures usually hides the more important question: how does the business workflow actually move from request to evidence to result?</p>
  </section>

  <section class="research-canvas__inventory" id="blueprint-contract" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Blueprint contract</p>
      <h2>Draw the business path before the technology stack.</h2>
      <p>A first-pass blueprint should be specific enough to challenge. It does not need every product choice, but it should make the important boundaries visible.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Question</th><th scope="col">What the blueprint should show</th></tr></thead>
        <tbody>
          <tr><th scope="row">What starts the work?</th><td>User request, document arrival, business event, schedule, or another explicit trigger.</td></tr>
          <tr><th scope="row">What evidence is needed?</th><td>Prompt input, approved knowledge, current enterprise state, or deterministic calculations.</td></tr>
          <tr><th scope="row">What does the model decide?</th><td>The bounded interpretation, extraction, drafting, recommendation, or routing task that benefits from model judgment.</td></tr>
          <tr><th scope="row">What stays deterministic?</th><td>Business rules, schema checks, authorization, calculations, transaction validation, or workflow gates that should not depend on free-form model judgment.</td></tr>
          <tr><th scope="row">What may change business state?</th><td>Read-only access, draft/proposal creation, approved execution, or no system action at all.</td></tr>
          <tr><th scope="row">How is the result proven?</th><td>Evaluation evidence, source trace, tool result, final system state, review decision, and operational telemetry where relevant.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="blueprint-boundary" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Boundary</p>
      <h2>Do not solve design questions that have not been earned yet.</h2>
      <p>The first-pass blueprint is useful when it makes assumptions explicit. It becomes misleading when it chooses detailed technology before the team has proved the workflow, data, access, and authority model.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Decide now</h3>
        <ul>
          <li>The business result and user group</li>
          <li>The primary pattern and why it fits</li>
          <li>The authoritative evidence or system state</li>
          <li>The model's role</li>
          <li>The read, propose, approve, or execute boundary</li>
          <li>The main proof gaps</li>
        </ul>
      </div>
      <div>
        <h3>Leave open until validated</h3>
        <ul>
          <li>Exact model and runtime configuration</li>
          <li>Final integration and deployment topology</li>
          <li>Detailed security implementation</li>
          <li>Final retrieval or indexing design</li>
          <li>Production thresholds and support procedures</li>
          <li>Scale assumptions that have not been measured</li>
        </ul>
      </div>
    </div>
    <p>Use <a href="/labs/business-ai/platform-building-blocks/">Platform Building Blocks</a> when the question is which technical capabilities are needed, and <a href="/labs/business-ai/governance-data-boundaries/">Governance and Data Boundaries</a> when the question is who may see, approve, or change what.</p>
  </section>

  <section class="research-canvas__inventory" id="blueprint-pressure-test" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Pressure test</p>
      <h2>A useful blueprint survives six questions.</h2>
      <p>Before adding more boxes, ask whether the current shape can answer these questions in plain language.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Fit</h3>
        <p>What part of the workflow requires AI rather than normal application logic?</p>
        <h3>Evidence</h3>
        <p>Which information is authoritative, and how does it reach the workflow?</p>
        <h3>State</h3>
        <p>Does the answer depend on live enterprise state, static knowledge, or both?</p>
      </div>
      <div>
        <h3>Authority</h3>
        <p>Can the workflow only explain and propose, or may it create side effects?</p>
        <h3>Failure</h3>
        <p>What should happen when evidence is missing, tools fail, or the proposed route is unsafe?</p>
        <h3>Proof</h3>
        <p>What evidence would make us keep, change, or reject this architecture?</p>
      </div>
    </div>
    <p>If the team cannot answer one of these without naming a product feature, the architecture is probably still hiding an unresolved business or control decision.</p>
  </section>

  <span id="hr-blueprint"></span>
  <section class="research-canvas__inventory" id="sales-order-blueprint" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Worked blueprint</p>
      <h2>Explain a blocked sales order without giving the assistant release authority.</h2>
      <p>Suppose a sales user asks why an order is credit blocked and what can be done next. The useful architecture is not simply “RAG plus an agent.” The workflow needs two different kinds of evidence: current SAP state and explanatory business knowledge.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Blueprint element</th><th scope="col">First-pass decision</th></tr></thead>
        <tbody>
          <tr><th scope="row">Trigger</th><td>A sales user requests an explanation for one blocked order.</td></tr>
          <tr><th scope="row">Transactional evidence</th><td>Read current order and credit-related state through an approved SAP interface. Do not ask the model to infer live status from old text.</td></tr>
          <tr><th scope="row">Knowledge evidence</th><td>Retrieve approved credit-policy or operating guidance that explains what the status means and who owns the next step.</td></tr>
          <tr><th scope="row">Model role</th><td>Combine the two evidence types into a clear explanation and draft next-step options.</td></tr>
          <tr><th scope="row">Deterministic boundary</th><td>Authorization, business rules, calculations, and the actual SAP document state remain outside free-form model judgment.</td></tr>
          <tr><th scope="row">Action authority</th><td>Read-only in the first release. The assistant does not release the credit block.</td></tr>
          <tr><th scope="row">Escalation</th><td>Unsupported, conflicting, or exception cases go to the responsible credit specialist.</td></tr>
          <tr><th scope="row">Proof</th><td>Test correct state retrieval, grounded explanation, unsupported-case handling, authorization behavior, and absence of unauthorized side effects.</td></tr>
        </tbody>
      </table>
    </div>
    <p>The pattern is therefore a <strong>tool-assisted, retrieval-grounded response</strong>. Orchestration becomes necessary only if later scope adds several dependent steps or dynamic handoffs.</p>
  </section>

  <section class="research-canvas__inventory" id="retrieval-blueprint" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Retrieval boundary</p>
      <h2>Knowledge retrieval and transactional reads solve different problems.</h2>
      <p>Retrieval-augmented generation is useful when the model needs approved knowledge. It does not automatically provide current transactional truth. A policy document can explain what a credit block means; the current sales-order state still belongs to the system that owns that transaction.</p>
    </header>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">database</span>
      <div>
        <p><strong>Knowledge source:</strong> policy, procedure, product documentation, operating guidance, or other managed content.</p>
        <p><strong>Enterprise state:</strong> the current object, status, balance, document, authorization, or process state returned by the authoritative business system.</p>
        <p>A solution may need both, but it should not blur them into one generic “context” layer.</p>
      </div>
    </div>
    <p>SAP's current Document Grounding capability is a concrete example of the first case: it implements a RAG approach over configured knowledge sources. Tool or API access is a separate architectural decision when the workflow needs live business state.</p>
  </section>

  <section class="research-canvas__inventory" id="agentic-fit" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Orchestration fit</p>
      <h2>Do not turn a pipeline into an agent because the label sounds more advanced.</h2>
      <p>Start with the lowest level of coordination that reliably completes the work. A direct model call can solve bounded transformations. A single tool-assisted workflow can handle many enterprise tasks. Multi-step or multi-agent orchestration earns its place when the route itself must change at runtime.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Orchestration is justified when</h3>
        <ul>
          <li>Later steps depend on earlier tool results.</li>
          <li>The next specialist or tool cannot be chosen in advance.</li>
          <li>The workflow must recover from missing information or partial failure.</li>
          <li>Different security or capability boundaries require real delegation.</li>
        </ul>
      </div>
      <div>
        <h3>Keep it deterministic when</h3>
        <ul>
          <li>The sequence is known in advance.</li>
          <li>Rules, approvals, and calculations already have deterministic logic.</li>
          <li>One model call plus one or two bounded tools completes the task.</li>
          <li>The team cannot yet test or support dynamic routing safely.</li>
        </ul>
      </div>
    </div>
    <p>Microsoft's current Azure Architecture Center guidance makes the same complexity trade-off explicit: direct model calls, single agents with tools, and multi-agent orchestration sit on a spectrum, with added coordination bringing added latency, cost, and failure modes.</p>
  </section>

  <section class="research-canvas__inventory" id="pattern-risks" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Failure boundaries</p>
      <h2>Each added boundary creates a different kind of failure.</h2>
      <p>Architecture becomes easier to reason about when failures are attached to the component that can actually create them.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Boundary</th><th scope="col">Typical failure</th><th scope="col">Design response</th></tr></thead>
        <tbody>
          <tr><th scope="row">Model transformation</th><td>Wrong extraction, classification, reasoning, or format.</td><td>Representative evaluation cases and deterministic validation where possible.</td></tr>
          <tr><th scope="row">Retrieval</th><td>Wrong, stale, inaccessible, or insufficient evidence.</td><td>Source ownership, entitlement filtering, freshness rules, and abstention behavior.</td></tr>
          <tr><th scope="row">Tool access</th><td>Wrong arguments, stale state, unavailable interface, or unsafe side effect.</td><td>Typed contracts, authorization, business validation, idempotency or reconciliation where relevant.</td></tr>
          <tr><th scope="row">Orchestration</th><td>Wrong route, loops, lost state, duplicate actions, or failed handoff.</td><td>Bounded state, stop conditions, retries with clear semantics, and traceable transitions.</td></tr>
          <tr><th scope="row">Human review</th><td>The reviewer lacks evidence or the approval no longer matches current state.</td><td>Show the exact proposal and relevant evidence; revalidate before execution when state may have changed.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="assessment-language" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architecture language</p>
      <h2>Describe the flow before naming the stack.</h2>
      <p>“RAG agent with tools” is not an architecture. A stronger explanation names the evidence, model task, deterministic checks, authority boundary, and proof required.</p>
    </header>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span>
      <p><strong>Example:</strong> “The assistant reads the current SAP order state through an approved interface, retrieves the relevant credit-policy guidance, and uses the model only to explain those facts and draft next steps. It remains read-only. Credit release stays in the existing business process. We would add dynamic orchestration only if later scope introduces dependent tools or routing that cannot be expressed reliably with normal workflow logic.”</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sources" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary references</p>
      <h2>Current implementation examples behind the pattern model.</h2>
    </header>
    <ul>
      <li><a href="https://help.sap.com/doc/generative-ai-hub-sdk/CLOUD/en-US/_reference/orchestration-service2.html">SAP Cloud SDK for AI — Orchestration Service V2 API</a>: current SAP examples for structured response formats, orchestration modules, and tool calling.</li>
      <li><a href="https://help.sap.com/doc/generative-ai-hub-sdk/CLOUD/en-US/_reference/document-grounding.html">SAP Cloud SDK for AI — Document Grounding</a>: SAP's RAG/document-grounding implementation and knowledge-source model.</li>
      <li><a href="https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns">Microsoft Azure Architecture Center — AI Agent Orchestration Patterns</a>: current guidance on choosing the lowest useful orchestration complexity and on sequential, concurrent, handoff, and other agent coordination patterns.</li>
    </ul>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">route</span>
    <p><strong>Continue the reasoning:</strong> use <a href="/labs/business-ai/platform-building-blocks/">Platform Building Blocks</a> for capability selection, <a href="/labs/business-ai/governance-data-boundaries/">Governance and Data Boundaries</a> for ownership and authority, <a href="/labs/business-ai/model-selection/">AI Model Selection</a> for model/runtime trade-offs, and <a href="/labs/business-ai/implementation-readiness/">AI Implementation Readiness</a> when the blueprint is ready for release evidence and operating controls.</p>
  </section>
</div>
