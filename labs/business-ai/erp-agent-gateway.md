---
layout: default
title: "ERP Agent Gateway Pilot — Safe AI Tool Access to Enterprise Systems"
description: "A vendor-neutral Enterprise AI pilot for controlled agent access to ERP data and actions through MCP, APIs, policy checks, approvals, and audit trails."
permalink: /labs/business-ai/erp-agent-gateway/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-24
last_reviewed: 2026-09-24
hide_global_cta: true
publication_wave: "public-business-ai-pilots-01"
review_method: "current MCP, SAP, and Microsoft primary sources + adjacent Labs review + full editorial pass"
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
source_links:
  - title: "Model Context Protocol Specification — 2026-07-28"
    url: "https://modelcontextprotocol.io/specification/2026-07-28"
  - title: "SAP Help — Add MCP Servers to Your Joule Agent"
    url: "https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/3d9dfad0bc39468292d508f0808a12fe.html"
  - title: "SAP Architecture Center — Integration, Security, Ethics & Governance"
    url: "https://architecture.learning.sap.com/docs/ai-native-north-star-architecture/integration-security-ethics-governance"
  - title: "Microsoft Learn — Security for Dynamics 365 ERP MCP"
    url: "https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/mcp/mcp-security"
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
  - type: "same_domain"
    title: "Business AI Glossary — Plain Language for Discovery, Architecture, Governance and Delivery"
    url: "/labs/business-ai/glossary/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li><a href="/labs/business-ai/pilots/">Pilots</a></li><li aria-current="page">ERP Agent Gateway</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Pilot 02 / agents → ERP tools</p>
      <h1>A model can choose a tool.<br />It should not choose its own authority.</h1>
      <p>An ERP agent becomes operationally interesting at the moment it can do more than explain data. Once it can call a business capability, the design has to connect model reasoning with identity, current ERP state, business authorization, approval, transaction semantics, and recovery. This pilot focuses on that execution boundary.</p>
      <a class="research-canvas__button" href="#gateway-design">Open the gateway design <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Gateway execution sequence">
      <p>Execution boundary</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Propose</strong><small>Interpret the requested business action</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Authorize</strong><small>Check identity, scope, state, and approval</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Execute</strong><small>Call a supported enterprise interface</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>Reconcile</strong><small>Prove the final business state</small></div>
      <em>Connectivity gives the agent a route. It does not give the agent business authority.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal aria-label="Gateway principle">
    <span class="material-symbols-outlined" aria-hidden="true">policy</span>
    <div>
      <p><strong>The useful boundary:</strong> the model may select or prepare an action, but deterministic controls decide whether that action is available for this identity, object, business state, and risk level.</p>
      <p>The gateway should add a narrow control layer around enterprise capabilities. It should not replace the ERP application's own authorization, validation, workflow, or transaction logic, and it should never turn a broad technical credential into broader user access.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="gateway-design" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Reference architecture</p>
      <h2>Follow one action from intent to proven ERP state.</h2>
      <p>The gateway is easier to reason about when each stage has one job. The model handles interpretation. The control plane handles authority. The ERP remains the system that owns business state.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Stage</th><th scope="col">What must be established</th><th scope="col">Typical evidence</th></tr></thead>
        <tbody>
          <tr><th scope="row">1. Identity and context</th><td>Who is asking, which agent is acting, which tenant or company context applies, and whether the call is delegated or autonomous.</td><td>User or workload identity, role context, organizational scope, correlation ID.</td></tr>
          <tr><th scope="row">2. Capability contract</th><td>Which narrow business capability is available, which inputs it accepts, whether it reads or changes state, and which outcomes it can return.</td><td>Tool schema, version, side-effect class, input and output contract.</td></tr>
          <tr><th scope="row">3. Policy and state validation</th><td>Whether this identity may perform this action on this object now, and whether the proposal still matches current ERP state.</td><td>Authorization result, business rules, current object status, scope and risk checks.</td></tr>
          <tr><th scope="row">4. Approval</th><td>Whether execution is already allowed or an accountable person must approve the exact proposed change.</td><td>Approver identity, proposal version, object, intended field changes, approval result.</td></tr>
          <tr><th scope="row">5. Execution</th><td>Which supported API, workflow, service, event, or other enterprise interface performs the operation and how duplicate execution is prevented.</td><td>Request identifier, adapter version, backend response, transaction or object identifier.</td></tr>
          <tr><th scope="row">6. Reconciliation</th><td>Whether the intended business state actually exists after the call, including cases where the technical response was ambiguous.</td><td>Fresh read of the object, final status, changed values, warnings, exception or recovery state.</td></tr>
        </tbody>
      </table>
    </div>

    <p>This is deliberately narrower than a complete enterprise-agent architecture. Agent planning, memory, orchestration, A2A, lifecycle, and broader governance belong in the <a href="/labs/enterprise-context/business-ai/agents/">Enterprise Agent Architecture</a> and <a href="/labs/business-ai/governance-data-boundaries/">Governance and Data Boundaries</a> pages. Here the question is simpler: when an agent wants to touch ERP state, what has to be true before and after the call?</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Concrete flow</p>
      <h2>Bind approval to the change, not to the conversation.</h2>
      <p>Suppose a user asks an agent to move the requested delivery date on a sales order. The model can interpret the request and prepare a precise proposal, but that proposal is not yet authority to execute.</p>
    </header>

    <div class="research-route-list">
      <a href="#gateway-design"><span>01</span><strong>Read the current object</strong><small>Resolve the order in the permitted organizational scope and retrieve only the state required for the decision.</small><i class="material-symbols-outlined" aria-hidden="true">search</i></a>
      <a href="#gateway-design"><span>02</span><strong>Prepare an exact delta</strong><small>Represent the intended change as object + field + old value + proposed value, not as vague conversational intent.</small><i class="material-symbols-outlined" aria-hidden="true">difference</i></a>
      <a href="#gateway-design"><span>03</span><strong>Validate the current state</strong><small>Check whether the user, object status, field, business scope, and configured risk policy allow the change.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="#gateway-design"><span>04</span><strong>Approve when required</strong><small>If policy requires human approval, show the exact proposed delta and bind the approval to that version of the proposal.</small><i class="material-symbols-outlined" aria-hidden="true">approval</i></a>
      <a href="#gateway-design"><span>05</span><strong>Execute and re-read</strong><small>Call the supported enterprise interface, then retrieve the object again so the workflow proves the business result instead of trusting a generic success message.</small><i class="material-symbols-outlined" aria-hidden="true">published_with_changes</i></a>
    </div>
  </section>

  <section class="research-canvas__method" id="authority" data-reveal>
    <div><p class="research-canvas__eyebrow">Authority model</p><h2>Autonomy belongs to the action, not to the agent name.</h2></div>
    <ol>
      <li><span>01</span><strong>Read</strong><p>The agent may retrieve approved business data. Source-system authorization and data scope still apply.</p></li>
      <li><span>02</span><strong>Draft or propose</strong><p>The agent may prepare a change, simulation, or next step, but no enterprise state changes yet.</p></li>
      <li><span>03</span><strong>Approved write</strong><p>The workflow may execute a narrow side effect after an accountable person approves the exact proposal against fresh state.</p></li>
      <li><span>04</span><strong>Bounded autonomous write</strong><p>A pre-approved class of low-risk actions may execute without a person in every loop when scope, validation, recovery, and monitoring are strong enough.</p></li>
      <li><span>05</span><strong>Excluded</strong><p>Broad administration, uncontrolled mass changes, permission changes, arbitrary code execution, or bypass of segregation-of-duties controls should not be exposed just because the agent can technically call them.</p></li>
    </ol>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Protocol versus authority</p>
      <h2>MCP gives the tool call a common shape. It does not make the business action safe.</h2>
      <p>The current MCP specification, dated 2026-07-28, standardizes how clients and servers expose tools, resources, prompts, and related protocol capabilities. Its security guidance is equally important: tool behavior descriptions can be untrusted, users need control over data and operations, and the protocol itself cannot enforce the application security principles around a tool.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Keep protocol concerns in the protocol layer</h3>
        <p>Discovery, tool schemas, requests, responses, authorization flows, transport, errors, and capability negotiation make integrations more portable. They are valuable, but they do not define who may change a sales order or release a financial document.</p>
      </div>
      <div>
        <h3>Keep business control close to the system of record</h3>
        <p>Application roles, object-level authorization, business validation, workflows, and supported APIs should remain part of the execution path. The gateway can add narrower policy; it should not create a shortcut around those controls.</p>
      </div>
      <div>
        <h3>Treat tools and retrieved content as data</h3>
        <p>A tool description, document note, attachment, or returned text can influence model reasoning, but it should not be able to rewrite authorization policy or grant itself a stronger action.</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Current enterprise examples</p>
      <h2>Good platform integrations preserve existing application controls.</h2>
      <p>Different products expose different MCP and agent capabilities, so implementation details must be checked per platform. Two current examples illustrate the boundary well.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/3d9dfad0bc39468292d508f0808a12fe.html"><span>SAP</span><strong>Joule Studio MCP connections</strong><small>SAP documents external MCP server connections and explicitly cautions teams to use trusted, verified, authorized endpoints, secure authentication, and access restricted to required information.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://architecture.learning.sap.com/docs/ai-native-north-star-architecture/integration-security-ethics-governance"><span>SAP</span><strong>Governed agent integration</strong><small>SAP's 2026 architecture guidance describes governed gateways, fine-grained tool policies, scoped agent identity, and human routing for critical decisions.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/mcp/mcp-security"><span>D365</span><strong>Dynamics 365 ERP MCP security</strong><small>Microsoft documents that ERP MCP requests use the authenticated security context, do not elevate privilege, and continue through the application's standard APIs, validation, workflows, and business rules.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://modelcontextprotocol.io/specification/2026-07-28"><span>MCP</span><strong>Model Context Protocol 2026-07-28</strong><small>The current specification defines the protocol contract and its security principles. It is the transport and capability layer, not an ERP authorization model.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal aria-label="Ambiguous execution result">
    <span class="material-symbols-outlined" aria-hidden="true">sync_problem</span>
    <div>
      <p><strong>One operational rule matters more than it first appears:</strong> a timeout does not prove that the ERP action failed. The backend may have committed the transaction after the caller lost the response.</p>
      <p>Represent that case as an <strong>unknown outcome</strong>, not as an automatic retry. Reconcile by request or business key first. Where the backend supports idempotency or concurrency controls, use them. Where it does not, the gateway needs operation-specific duplicate protection and a deliberate recovery path.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="tests" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Failure lab</p>
      <h2>Test the control boundary, not only the happy tool call.</h2>
      <p>A useful pilot should deliberately create states where the model's preferred action is unsafe, stale, unauthorized, duplicated, or impossible to confirm.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Test</th><th scope="col">Risk</th><th scope="col">Expected gateway behavior</th></tr></thead>
        <tbody>
          <tr><th scope="row">Wrong company or object scope</th><td>The model finds a real object outside the caller's permitted business context.</td><td>Block before execution and return a scoped, non-sensitive explanation.</td></tr>
          <tr><th scope="row">State changed after proposal</th><td>An approval was based on data that is no longer current.</td><td>Re-read the object, invalidate or re-evaluate the proposal, and require fresh approval when the material change affects the decision.</td></tr>
          <tr><th scope="row">Timeout after write</th><td>The transaction may have committed although the client received no success response.</td><td>Move to unknown outcome, reconcile first, and prevent blind duplicate replay.</td></tr>
          <tr><th scope="row">Untrusted instruction in enterprise data</th><td>A note, attachment, tool result, or tool description tries to alter workflow rules.</td><td>Treat it as business data, not policy; keep authorization and control instructions outside retrieved content.</td></tr>
          <tr><th scope="row">Privilege mismatch</th><td>The runtime credential can technically do more than the end user or approved agent role should do.</td><td>Enforce the narrower effective business scope and reject privilege expansion.</td></tr>
          <tr><th scope="row">Backend validation rejects the action</th><td>The model produced a plausible request that conflicts with current application rules.</td><td>Preserve the backend error, return a structured business exception, and do not reinterpret rejection as success.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Evaluation</p><h2>Prove that the gateway makes better execution decisions.</h2></div>
    <ol>
      <li><span>01</span><strong>Authority decision correctness</strong><p>Across representative cases, did the control layer correctly allow, deny, or require approval for the proposed action?</p></li>
      <li><span>02</span><strong>Business-result correctness</strong><p>When a write was allowed, did the intended ERP state exist afterward, with no hidden or extra side effect?</p></li>
      <li><span>03</span><strong>Duplicate-free recovery</strong><p>Did retries, timeouts, and repeated requests avoid duplicate business transactions or uncontrolled replay?</p></li>
      <li><span>04</span><strong>Authorization invariants</strong><p>Could any prompt, tool choice, retrieved content, or technical identity widen the business scope that policy allowed?</p></li>
      <li><span>05</span><strong>Reconstructability</strong><p>Can an operator later connect the caller, proposal, policy decision, approval, tool version, backend result, and final business state without logging unnecessary sensitive content?</p></li>
    </ol>
    <p>For write-enabled tools, zero known unauthorized or duplicate writes should be a release condition, not a metric that can be averaged away by high success elsewhere. Broader evaluation, staged release, monitoring, and rollback belong in <a href="/labs/business-ai/implementation-readiness/">AI Implementation Readiness</a>.</p>
  </section>

  <section class="research-canvas__boundary" data-reveal aria-label="Reference output">
    <span class="material-symbols-outlined" aria-hidden="true">architecture</span>
    <div>
      <p><strong>A useful pilot output:</strong> a small gateway with two or three narrow ERP capabilities, explicit authority levels, deterministic policy checks, one approval path, safe handling of ambiguous outcomes, a mock or sandbox backend, and a failure-focused evaluation set.</p>
      <p><strong>What the pilot should prove:</strong> an agent can remain flexible in how it interprets work while enterprise execution stays narrow, attributable, recoverable, and owned.</p>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
