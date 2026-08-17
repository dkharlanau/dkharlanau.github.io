---
layout: default
title: "ERP Agent Gateway Pilot — Safe AI Tool Access to Enterprise Systems"
description: "A vendor-neutral Enterprise AI pilot for controlled agent access to ERP data and actions through MCP, APIs, policy checks, approvals, and audit trails."
permalink: /labs/business-ai/erp-agent-gateway/
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
search_intent: "ERP AI agent gateway, MCP ERP agent architecture, safe agent access to SAP Dynamics Oracle ERP"
structured_data:
  type: TechArticle
tags:
  - business-ai
  - enterprise-ai
  - erp
  - mcp
  - agents
  - security
  - integration
# ai-discovery-managed:start
primary_topic: "business-ai"
ai_sidecar: "/ai/pages/labs--business-ai--erp-agent-gateway.json"
entity_mentions:
  - "sap-integration"
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
    title: "Open Enterprise AI Pilots — ERP, Documents, Agents, and Controls"
    url: "/labs/business-ai/pilots/"
  - type: "related_topic"
    title: "Document-to-ERP AI Pilot — From PDF to Controlled Transaction"
    url: "/labs/business-ai/document-to-erp-ai/"
  - type: "related_topic"
    title: "Open Enterprise AI Research — ERP Evidence, Safety, and Readiness"
    url: "/labs/business-ai/open-research/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li><a href="/labs/business-ai/pilots/">Pilots</a></li><li aria-current="page">ERP Agent Gateway</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Pilot 02 / agents → ERP tools</p>
      <h1>The dangerous part<br />is the permission behind the tool.</h1>
      <p>An agent that can explain an order is useful. An agent that can change an order is an architecture decision. This pilot explores the layer between AI reasoning and enterprise execution: identity, tools, policy, confirmation, transaction safety, and audit.</p>
      <a class="research-canvas__button" href="#gateway-design">Open the gateway design <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Agent authority levels">
      <p>Authority ladder</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Read</strong><small>Retrieve and explain</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Plan</strong><small>Prepare an action</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Write</strong><small>Execute under policy</small></div>
      <em>Autonomy is not one switch. It should be assigned per tool, process, risk, user, and business context.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal aria-label="Gateway principle">
    <span class="material-symbols-outlined" aria-hidden="true">policy</span>
    <p><strong>Problem.</strong> An agent can cross from useful reasoning into an unsafe ERP action unless identity, policy, confirmation, and transaction controls are explicit.</p>
    <p><strong>Core rule.</strong> The agent never receives broad ERP power just because the user has it. It receives a narrow set of tools with explicit input schemas, policy checks, and observable results.</p>
    <p><strong>Another rule.</strong> A tool description is not a security control. Authorization must live outside the model prompt.</p>
  </section>

  <section class="research-canvas__inventory" id="gateway-design" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Reference architecture</p>
      <h2>Put a policy boundary between reasoning and execution.</h2>
      <p>The agent can decide which capability may help. The gateway decides whether that capability is available, whether the request is valid, and whether a human must approve the action.</p>
    </header>
    <div class="research-route-list">
      <a href="#gateway-design"><span>01</span><strong>User and agent identity</strong><small>Resolve who is asking, which agent is acting, the tenant or company context, roles, and delegated permissions.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a href="#gateway-design"><span>02</span><strong>Tool catalog</strong><small>Expose small business capabilities such as get order, check stock, simulate price, create draft, or release blocked document.</small><i class="material-symbols-outlined" aria-hidden="true">construction</i></a>
      <a href="#gateway-design"><span>03</span><strong>Policy gateway</strong><small>Validate tool, scope, object, amount, process status, business role, environment, and required approval before execution.</small><i class="material-symbols-outlined" aria-hidden="true">gavel</i></a>
      <a href="#gateway-design"><span>04</span><strong>ERP adapters</strong><small>Translate the approved capability call into MCP, REST, OData, BAPI, IDoc, workflow, event, or another controlled system interface.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="#gateway-design"><span>05</span><strong>Structured result</strong><small>Return business result, warnings, transaction identifiers, changed fields, and machine-readable errors instead of vague success text.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="#gateway-design"><span>06</span><strong>Audit and replay</strong><small>Record request, user, agent, policy result, approval, tool version, ERP response, and final business state for later review.</small><i class="material-symbols-outlined" aria-hidden="true">history</i></a>
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Authority model</p><h2>Read, plan, write. Do not mix them casually.</h2></div>
    <ol>
      <li><span>01</span><strong>Read</strong><p>The agent can query approved business data and explain it. Sensitive fields, companies, and objects remain filtered by user and tool policy.</p></li>
      <li><span>02</span><strong>Plan</strong><p>The agent can prepare a change, simulation, draft, or proposed sequence of actions, but the ERP state does not change.</p></li>
      <li><span>03</span><strong>Write</strong><p>A narrow tool may change ERP state after deterministic validation and, where required, explicit human confirmation.</p></li>
      <li><span>04</span><strong>Never</strong><p>Some actions should stay outside the agent surface: broad administration, unrestricted code execution, mass changes without review, or bypass of segregation-of-duties controls.</p></li>
    </ol>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Cross-ERP direction</p>
      <h2>The interface layer is starting to standardize. The business controls are not.</h2>
      <p>MCP makes tool connection more portable, but an ERP tool still has business meaning. “createOrder” is not safe because it has a JSON schema. It is safe only when the business context, permissions, validation, and transaction behaviour are correct.</p>
    </header>
    <div class="research-route-list">
      <a href="https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp"><span>D365</span><strong>Dynamics 365 ERP MCP</strong><small>Microsoft documents a dynamic ERP MCP server for access to finance and operations data and business logic, including existing permissions and auditability.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/joule-studio-classic/joule-studio-classic-edition/add-mcp-servers-to-your-joule-agent"><span>SAP</span><strong>Joule Agent MCP Connections</strong><small>SAP documents external MCP server connections for Joule agents and warns that endpoints must be trusted, verified, authorized, and restricted to required information.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://modelcontextprotocol.io/specification/2025-11-25"><span>MCP</span><strong>MCP Specification</strong><small>The specification defines protocol-level tool use and explicitly discusses consent, access control, privacy, and tool safety.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="/labs/enterprise-context/integrations/"><span>SAP+</span><strong>Existing enterprise interfaces</strong><small>MCP is another interface option, not a reason to throw away APIs, events, IDocs, workflows, or integration middleware that already own important semantics.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="tests" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Failure lab</p>
      <h2>Test the bad day before the boardroom demo.</h2>
      <p>The gateway is valuable only if it blocks or contains the requests we do not want. The benchmark should deliberately create confusing, unsafe, and contradictory situations.</p>
    </header>
    <div class="research-route-list">
      <a href="#tests"><span>F1</span><strong>Wrong company or plant</strong><small>The user asks a valid question but the agent selects an object from a different organizational context.</small><i class="material-symbols-outlined" aria-hidden="true">domain_disabled</i></a>
      <a href="#tests"><span>F2</span><strong>Stale business context</strong><small>The agent planned a change using data that was valid seconds ago but no longer matches current ERP state.</small><i class="material-symbols-outlined" aria-hidden="true">update_disabled</i></a>
      <a href="#tests"><span>F3</span><strong>Duplicate action</strong><small>A timeout causes retry and the same transaction is executed twice unless idempotency is enforced.</small><i class="material-symbols-outlined" aria-hidden="true">content_copy</i></a>
      <a href="#tests"><span>F4</span><strong>Prompt injection through enterprise data</strong><small>A note, attachment, description, or external document tries to convince the agent to ignore the expected workflow.</small><i class="material-symbols-outlined" aria-hidden="true">security</i></a>
      <a href="#tests"><span>F5</span><strong>Permission mismatch</strong><small>The model selects a tool that the current user, role, process, or environment is not allowed to execute.</small><i class="material-symbols-outlined" aria-hidden="true">lock</i></a>
      <a href="#tests"><span>F6</span><strong>High-risk write</strong><small>The action is technically permitted but exceeds an amount, scope, or risk threshold that requires stronger approval.</small><i class="material-symbols-outlined" aria-hidden="true">priority_high</i></a>
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Evaluation</p><h2>Measure control quality, not agent confidence.</h2></div>
    <ol>
      <li><span>01</span><strong>Correct tool rate</strong><p>Did the agent choose the right capability for the business request?</p></li>
      <li><span>02</span><strong>Policy decision accuracy</strong><p>Did the gateway allow, deny, or escalate the action correctly?</p></li>
      <li><span>03</span><strong>Unsafe execution rate</strong><p>How many actions changed ERP state when they should have been blocked? The target is zero.</p></li>
      <li><span>04</span><strong>Recovery quality</strong><p>When a call failed or state changed, did the workflow retry safely, re-read context, or stop with a clear exception?</p></li>
      <li><span>05</span><strong>Audit completeness</strong><p>Can an operator reconstruct who asked, what the agent planned, which policy applied, what tool ran, and what changed?</p></li>
    </ol>
  </section>

  <section class="research-canvas__boundary" data-reveal aria-label="Reference output">
    <span class="material-symbols-outlined" aria-hidden="true">architecture</span>
    <p><strong>Public output.</strong> The pilot should produce a small gateway service, a tool contract, policy examples, a mock ERP, MCP/API adapters, a failure-test pack, and an evaluation report.</p>
    <p><strong>What this proves.</strong> Agent architecture is not just orchestration. It connects security, integration, process ownership, ERP semantics, error handling, and operations. That is exactly why it is interesting.</p>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
