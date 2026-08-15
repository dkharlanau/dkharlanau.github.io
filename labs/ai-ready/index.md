---
layout: default
title: "AI Ready — Practical Architecture Lab"
description: "A practical architecture map for AI systems: data, retrieval, tools, MCP, agents, evals, security, deployment, and production rules."
permalink: /labs/ai-ready/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags:
  - ai
  - architecture
  - mcp
  - agents
  - rag
  - evals
  - security
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li aria-current="page">AI Ready</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Labs / AI Ready</p>
      <h1>Build AI systems.<br />Not AI demos.</h1>
      <p>A practical map for choosing data, retrieval, tools, MCP, agents, evaluations, controls, and deployment patterns. Start with the problem. Add autonomy only where it earns its place.</p>
      <a class="research-canvas__button" href="#architecture-map">Open the architecture map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Review status">
      <p>Current baseline</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>8</strong><small>Architecture areas</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>4</strong><small>Hands-on labs</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>2026-07-28</strong><small>MCP revision tracked</small></div>
      <em>Reviewed 15 Aug 2026. Fast-moving items are dated on purpose.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">architecture</span>
    <p><strong>Architecture rule:</strong> the model is one component. Data quality, permissions, deterministic code, APIs, observability, and operations still belong to the application.</p>
    <p><strong>Default:</strong> use the least autonomous design that solves the problem well.</p>
    <a href="/labs/ai-ready/data/catalog.json">Open machine-readable catalog <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
  </section>

  <section class="research-canvas__inventory" id="architecture-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architecture map</p>
      <h2>Learn the system in layers.</h2>
      <p>The useful question is not “which model is best?”. It is “where does uncertainty belong, and where must behavior stay deterministic?”.</p>
    </header>
    <div class="research-route-list">
      <a href="#foundations"><span>01</span><strong>Foundations</strong><small>Context, instructions, structured output, embeddings, tool calls, state, memory, workflow vs agent.</small><i class="material-symbols-outlined" aria-hidden="true">foundation</i></a>
      <a href="#data"><span>02</span><strong>Data and Retrieval</strong><small>Sources of truth, datasets, chunking, metadata, hybrid search, reranking, grounding, provenance.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="#mcp"><span>03</span><strong>Tools and MCP</strong><small>Typed tool contracts, resources, prompts, transport, authorization, approvals, idempotency.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="#agents"><span>04</span><strong>Agent Architecture</strong><small>Tool loops, routing, planning, workers, supervisors, budgets, termination rules, human approval.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#evals"><span>05</span><strong>Evals and Reliability</strong><small>Golden cases, graders, regressions, traces, latency, cost, retries, fallbacks.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#security"><span>06</span><strong>Security and Governance</strong><small>Prompt injection, exfiltration, least privilege, secrets, audit, PII, sandboxing.</small><i class="material-symbols-outlined" aria-hidden="true">shield</i></a>
      <a href="#deploy"><span>07</span><strong>Build and Deploy</strong><small>Environments, configuration, containers, serverless, CI/CD, observability, rate limits, rollback.</small><i class="material-symbols-outlined" aria-hidden="true">rocket_launch</i></a>
      <a href="#decisions"><span>08</span><strong>Decision Matrix</strong><small>RAG or fine-tune? Tool or MCP? Workflow or agent? A short default for each architecture choice.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="foundations" data-reveal>
    <header><p class="research-canvas__eyebrow">01 / Foundations</p><h2>Know what belongs to the model.</h2><p>Language models are good at interpretation, synthesis, classification, planning, and working with uncertain input. They are poor substitutes for permissions, transaction rules, exact calculations, and durable state.</p></header>
    <div class="research-route-list">
      <a href="#foundations"><span>CTX</span><strong>Context is a budget</strong><small>Do not dump everything into the prompt. Select useful context, keep provenance, and measure whether more context actually improves answers.</small><i class="material-symbols-outlined" aria-hidden="true">memory</i></a>
      <a href="#foundations"><span>OUT</span><strong>Structured output is an interface</strong><small>When another component consumes the answer, use a schema and validate it. Natural language is for people; contracts are for software.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="#foundations"><span>MEM</span><strong>State is not memory</strong><small>Conversation state, user memory, application records, cache, and model context have different lifecycles. Store each one deliberately.</small><i class="material-symbols-outlined" aria-hidden="true">storage</i></a>
      <a href="#decisions"><span>WF</span><strong>Workflow before agent</strong><small>If the next step is known, code it. Use model decisions only where the next step depends on messy or variable evidence.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="data" data-reveal>
    <header><p class="research-canvas__eyebrow">02 / Data and Retrieval</p><h2>AI quality starts before the prompt.</h2><p>For enterprise work, the difficult part is usually finding the right source, version, scope, and permission. RAG does not repair weak master data or unclear ownership.</p></header>
    <div class="research-route-list">
      <a href="#data"><span>SRC</span><strong>Source of truth</strong><small>Define which system or document owns the fact. Carry source ID, effective date, owner, classification, and access rules as metadata.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
      <a href="#data"><span>RET</span><strong>Retrieval pipeline</strong><small>Start with lexical or filtered search when it is enough. Add vector search and reranking when semantic matching creates measurable value.</small><i class="material-symbols-outlined" aria-hidden="true">search</i></a>
      <a href="#evals"><span>DS</span><strong>Datasets have different jobs</strong><small>Keep source data, retrieval corpus, synthetic test data, golden eval cases, and fine-tuning data separate. Version them.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
      <a href="#security"><span>PII</span><strong>Classify before indexing</strong><small>Decide what may be embedded, cached, logged, sent to a model, or returned to a user. Retrieval permissions must follow the source.</small><i class="material-symbols-outlined" aria-hidden="true">policy</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="mcp" data-reveal>
    <header><p class="research-canvas__eyebrow">03 / Tools and MCP</p><h2>A protocol is not an architecture strategy.</h2><p>MCP is useful when several AI clients need a reusable way to discover and call capabilities. A normal API or direct function tool is still simpler when reuse is not needed.</p></header>
    <div class="research-route-list">
      <a href="https://modelcontextprotocol.io/" target="_blank" rel="noopener"><span>MCP</span><strong>Current MCP baseline</strong><small>The 2026-07-28 protocol revision moved the core to stateless request/response behavior. Check the current specification before implementing a server.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://modelcontextprotocol.io/" target="_blank" rel="noopener"><span>3</span><strong>Tools, resources, prompts</strong><small>Tools perform actions or retrieval, resources expose context, and prompts provide reusable interaction templates. Keep each contract small and clear.</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
      <a href="#security"><span>AUTH</span><strong>Authorization stays outside the model</strong><small>The model may propose a call. Your application decides whether the caller is allowed to make it. Tool descriptions are not security controls.</small><i class="material-symbols-outlined" aria-hidden="true">lock</i></a>
      <a href="#labs"><span>IDEM</span><strong>Design writes for retries</strong><small>Use request IDs, business keys, preconditions, dry-run modes, and approval when duplicate or high-impact writes are possible.</small><i class="material-symbols-outlined" aria-hidden="true">repeat</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="agents" data-reveal>
    <header><p class="research-canvas__eyebrow">04 / Agent Architecture</p><h2>Autonomy needs boundaries.</h2><p>An agent is useful when the system must choose the next action from changing evidence. More loops do not create more intelligence; sometimes they just create a larger invoice and a stranger incident report.</p></header>
    <div class="research-route-list">
      <a href="#agents"><span>LOOP</span><strong>Tool loop</strong><small>Model selects a tool, application validates the request, tool runs, result returns to the model, and the loop stops on a clear condition.</small><i class="material-symbols-outlined" aria-hidden="true">sync</i></a>
      <a href="#agents"><span>RTR</span><strong>Router</strong><small>Use one decision to select a workflow, specialist, model, or tool set. Good when the space of paths is known.</small><i class="material-symbols-outlined" aria-hidden="true">call_split</i></a>
      <a href="#agents"><span>WRK</span><strong>Orchestrator and workers</strong><small>Split independent tasks when parallel work creates value. Merge results with explicit acceptance rules.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#security"><span>STOP</span><strong>Budget and termination</strong><small>Limit steps, time, cost, tools, data scope, and retries. Escalate or stop when evidence is weak or a risky action is required.</small><i class="material-symbols-outlined" aria-hidden="true">stop_circle</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="evals" data-reveal>
    <header><p class="research-canvas__eyebrow">05 / Evals and Reliability</p><h2>Make quality testable.</h2><p>Before changing a prompt, model, retrieval method, or tool schema, keep cases that tell you whether the change helped or broke something else.</p></header>
    <div class="research-route-list">
      <a href="/labs/ai-ready/data/eval-sample.jsonl"><span>DATA</span><strong>Sample eval dataset</strong><small>Eight architecture cases with expected patterns, controls, and failure signals. Small on purpose; extend it from real failures.</small><i class="material-symbols-outlined" aria-hidden="true">download</i></a>
      <a href="#evals"><span>GOLD</span><strong>Golden set</strong><small>Keep representative easy, hard, ambiguous, unsafe, and failure-path cases. Store expected facts, tool choice, required controls, or outcome.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#evals"><span>GRD</span><strong>Use the simplest grader</strong><small>Exact values and schemas should use deterministic checks. Use model graders for qualities that cannot be expressed reliably as code.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="#deploy"><span>OBS</span><strong>Trace the whole request</strong><small>Capture retrieval, model calls, tool calls, approvals, latency, errors, and versions. Logs without correlation IDs are archaeology.</small><i class="material-symbols-outlined" aria-hidden="true">timeline</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="security" data-reveal>
    <header><p class="research-canvas__eyebrow">06 / Security and Governance</p><h2>Treat content as data, not authority.</h2><p>Prompt injection can arrive through a user, file, webpage, ticket, email, or retrieved document. The safe design assumes external content may be hostile.</p></header>
    <div class="research-route-list">
      <a href="https://genai.owasp.org/llmrisk/llm01-prompt-injection/" target="_blank" rel="noopener"><span>INJ</span><strong>Prompt injection</strong><small>Retrieved instructions must not override system policy, permissions, or approval rules. RAG and fine-tuning do not remove this risk.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="#security"><span>LP</span><strong>Least privilege</strong><small>Give each tool the minimum data and action scope it needs. Separate read tools from write tools and high-impact actions.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>
      <a href="#security"><span>SEC</span><strong>Secrets stay outside context</strong><small>Use secret stores and short-lived credentials. Never rely on “do not reveal this” instructions to protect a credential placed in model context.</small><i class="material-symbols-outlined" aria-hidden="true">password</i></a>
      <a href="https://www.nist.gov/itl/ai-risk-management-framework" target="_blank" rel="noopener"><span>RMF</span><strong>Govern the lifecycle</strong><small>Record ownership, intended use, risk, evaluation, monitoring, change control, and retirement. Governance is an operating process, not a PDF at project end.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="deploy" data-reveal>
    <header><p class="research-canvas__eyebrow">07 / Build and Deploy</p><h2>A local success is only the first environment.</h2><p>Production AI needs the same boring disciplines as other software, plus model, prompt, retrieval, and eval versioning.</p></header>
    <div class="research-route-list">
      <a href="#deploy"><span>ENV</span><strong>Separate environments</strong><small>Keep development, test, and production data, credentials, tools, quotas, and endpoints separate.</small><i class="material-symbols-outlined" aria-hidden="true">lan</i></a>
      <a href="#deploy"><span>VER</span><strong>Version the behavior</strong><small>Track model, prompt, tool schemas, retrieval settings, datasets, and evals with the application release.</small><i class="material-symbols-outlined" aria-hidden="true">commit</i></a>
      <a href="#deploy"><span>SLO</span><strong>Define budgets</strong><small>Set targets for answer quality, latency, availability, token or request cost, and tool failure rate. Optimize against a target, not a feeling.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
      <a href="#deploy"><span>FAIL</span><strong>Engineer failure paths</strong><small>Handle timeouts, malformed output, stale retrieval, denied permissions, partial tool results, duplicate requests, rate limits, and model fallback.</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="decisions" data-reveal>
    <header><p class="research-canvas__eyebrow">08 / Decision matrix</p><h2>Start with these defaults.</h2><p>Architecture becomes easier when every new technology has to prove why the simpler option is not enough.</p></header>
    <div class="research-route-list">
      <a href="#data"><span>RAG</span><strong>Fresh or private knowledge → retrieval</strong><small>Retrieve from the source of truth and carry provenance. Fine-tuning is not a database update mechanism.</small><i class="material-symbols-outlined" aria-hidden="true">search</i></a>
      <a href="#mcp"><span>TOOL</span><strong>External deterministic action → typed tool</strong><small>Validate inputs and outputs in code. Use MCP when standard reuse across clients is useful, not as ceremony.</small><i class="material-symbols-outlined" aria-hidden="true">build</i></a>
      <a href="#agents"><span>WF</span><strong>Known sequence → workflow</strong><small>Keep fixed steps fixed. Add an agent only when the system must adapt its next action to evidence.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="#evals"><span>FT</span><strong>Behavior gap → prompt and eval first</strong><small>Try clearer instructions, examples, schemas, retrieval, or tools. Fine-tune after tests show a stable gap worth training for.</small><i class="material-symbols-outlined" aria-hidden="true">tune</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="labs" data-reveal>
    <header><p class="research-canvas__eyebrow">Hands-on track</p><h2>Build four small systems.</h2><p>The goal is not another tutorial clone. Each lab adds one production concern and leaves a testable artifact.</p></header>
    <div class="research-route-list">
      <a href="/mcp/sap-diagnostics-mcp/"><span>01</span><strong>Read-only MCP server</strong><small>Expose a narrow SAP-like diagnostic capability. Focus on tool contracts, boundaries, transport, authorization, and traces.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="/labs/ai-ready/data/eval-sample.jsonl"><span>02</span><strong>RAG plus evals</strong><small>Build a small retrieval corpus with citations, then test retrieval and answer behavior with a golden dataset.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#agents"><span>03</span><strong>Agent with approval</strong><small>Investigate with read tools, prepare a change, and require explicit approval before a risky write.</small><i class="material-symbols-outlined" aria-hidden="true">approval</i></a>
      <a href="#deploy"><span>04</span><strong>Production readiness</strong><small>Add tracing, eval gates, retry rules, cost and latency budgets, secrets, rate limits, deployment, and rollback.</small><i class="material-symbols-outlined" aria-hidden="true">rocket_launch</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Production checklist</p><h2>Before a real user gets access.</h2><p>A short checklist catches more problems than a long architecture deck nobody opens after the workshop.</p></header>
    <div class="research-route-list">
      <a href="#security"><span>01</span><strong>Identity and permissions</strong><small>User identity reaches the tool boundary. Reads and writes use least privilege. High-impact actions have approval.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a href="#evals"><span>02</span><strong>Quality and regression</strong><small>Representative evals exist, failure cases are included, and a release can be compared with the previous version.</small><i class="material-symbols-outlined" aria-hidden="true">checklist</i></a>
      <a href="#deploy"><span>03</span><strong>Observability and recovery</strong><small>Trace IDs, sanitized logs, metrics, rate limits, retries, fallback behavior, and rollback are defined.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
      <a href="#data"><span>04</span><strong>Data lifecycle</strong><small>Sources, freshness, retention, PII, caches, embeddings, logs, and deletion behavior have owners.</small><i class="material-symbols-outlined" aria-hidden="true">cycle</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Source baseline</p><h2>Date the moving parts.</h2><p>AI platform details change quickly. This lab separates durable architecture rules from dated protocol and product facts.</p></header>
    <div class="research-route-list">
      <a href="https://blog.modelcontextprotocol.io/posts/2026-07-28/" target="_blank" rel="noopener"><span>MCP</span><strong>Model Context Protocol</strong><small>Official 2026-07-28 release notes. Reviewed 15 Aug 2026.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://platform.openai.com/docs/" target="_blank" rel="noopener"><span>API</span><strong>OpenAI developer documentation</strong><small>Current reference for Responses, tools, remote MCP, agents, and eval capabilities. Reviewed 15 Aug 2026.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://www.nist.gov/itl/ai-risk-management-framework" target="_blank" rel="noopener"><span>NIST</span><strong>AI Risk Management Framework</strong><small>Risk management baseline and Generative AI profile. Reviewed 15 Aug 2026.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://genai.owasp.org/" target="_blank" rel="noopener"><span>OWASP</span><strong>GenAI Security Project</strong><small>Security risks and practical defensive guidance. Reviewed 15 Aug 2026.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
