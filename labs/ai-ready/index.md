---
layout: default
title: "AI Ready — Practical AI Architecture Lab"
description: "A practical learning area for using and building AI systems: models, prompting, retrieval, tools, MCP, agents, evals, security, observability, and deployment."
permalink: /labs/ai-ready/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, engineering, architecture, mcp, agents, rag, evals, security, automation]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li aria-current="page">AI Ready</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Labs / AI Ready</p>
      <h1>Learn AI by<br />building the layers.</h1>
      <p>A general-purpose handbook for using models in real systems. Start from the job, choose the smallest useful architecture, build it, test it, and learn how it fails.</p>
      <a class="research-canvas__button" href="/labs/ai-ready/engineering/">Open the engineering handbook <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Learning map">
      <p>Engineering path</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>13</strong><small>Engineering steps</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>5</strong><small>Runnable examples</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>4</strong><small>Hands-on labs</small></div>
      <em>Core material is general-purpose. No SAP system or vendor product is required.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">architecture</span>
    <p><strong>Main rule:</strong> use the model for uncertainty. Keep exact rules, permissions, durable state, validation, and side effects in normal software.</p>
    <p><strong>Build rule:</strong> prompt and schema first. Add retrieval, tools, MCP, or agents only when the simpler shape cannot meet the evals.</p>
    <a href="/labs/ai-ready/data/engineering-map.json">Open machine-readable engineering map <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Two entry points</p><h2>Start from work or start from engineering.</h2><p>Use cases tell you what shape usually fits a job. The handbook explains each technical layer in build order.</p></header>
    <div class="research-route-list">
      <a href="/labs/ai-ready/use-cases/"><span>USE</span><strong>Practical Use Cases</strong><small>Research, private knowledge, coding, data analysis, automation, and operations.</small><i class="material-symbols-outlined" aria-hidden="true">workspaces</i></a>
      <a href="/labs/ai-ready/engineering/"><span>ENG</span><strong>Engineering Handbook</strong><small>Models → prompt/context → structured output → embeddings → RAG → tools → MCP → agents → state → evals → observability → security → deployment.</small><i class="material-symbols-outlined" aria-hidden="true">construction</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="engineering-path" data-reveal>
    <header><p class="research-canvas__eyebrow">Engineering path</p><h2>Build the system in layers.</h2><p>You do not need every layer. The order helps you understand what each extra component is buying you.</p></header>
    <div class="research-route-list">
      <a href="/labs/ai-ready/engineering/models/"><span>01</span><strong>Models</strong><small>Choose profiles by task, quality, latency, cost, modality, privacy, and evals.</small><i class="material-symbols-outlined" aria-hidden="true">neurology</i></a>
      <a href="/labs/ai-ready/engineering/prompt-context/"><span>02</span><strong>Prompt and Context</strong><small>Separate instructions, examples, history, and untrusted evidence. Context is a budget.</small><i class="material-symbols-outlined" aria-hidden="true">memory</i></a>
      <a href="/labs/ai-ready/engineering/structured-output/"><span>03</span><strong>Structured Output</strong><small>Turn model output into schemas, enums, IDs, and validated software contracts.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/labs/ai-ready/engineering/embeddings-vector-search/"><span>04</span><strong>Embeddings and Vector Search</strong><small>Learn semantic similarity, metadata filters, lexical baselines, and hybrid retrieval.</small><i class="material-symbols-outlined" aria-hidden="true">scatter_plot</i></a>
      <a href="/labs/ai-ready/data-rag/"><span>05</span><strong>RAG</strong><small>Retrieve current or private evidence with provenance, permissions, and citations.</small><i class="material-symbols-outlined" aria-hidden="true">search</i></a>
      <a href="/labs/ai-ready/tools-mcp/"><span>06–07</span><strong>Tool Calling and MCP</strong><small>Read facts and perform actions through typed tools. Add MCP when shared reuse creates value.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="/labs/ai-ready/agent-architecture/"><span>08</span><strong>Agents</strong><small>Use bounded loops only when the next useful step depends on changing evidence.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/ai-ready/engineering/memory-state/"><span>09</span><strong>Memory and State</strong><small>Separate request context, history, user preferences, application state, and cache.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="/labs/ai-ready/evals-reliability/"><span>10</span><strong>Evals</strong><small>Build golden cases and regression gates before tuning by intuition.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="/labs/ai-ready/engineering/observability/"><span>11</span><strong>Observability</strong><small>Trace models, retrieval, tools, agent steps, versions, latency, and cost.</small><i class="material-symbols-outlined" aria-hidden="true">timeline</i></a>
      <a href="/labs/ai-ready/security-governance/"><span>12</span><strong>Security and Governance</strong><small>Treat content as untrusted. Keep permissions, secrets, policy, and approvals outside the model.</small><i class="material-symbols-outlined" aria-hidden="true">shield</i></a>
      <a href="/labs/ai-ready/build-operate/"><span>13</span><strong>Deployment</strong><small>Version behavior, set budgets, design degraded modes, observe production, and roll back.</small><i class="material-symbols-outlined" aria-hidden="true">rocket_launch</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="examples" data-reveal>
    <header><p class="research-canvas__eyebrow">Runnable mechanics</p><h2>Five small Python examples.</h2><p>No AI SDK is required. The examples expose the application boundaries that stay useful when a real model is plugged in later.</p></header>
    <div class="research-route-list">
      <a href="/labs/ai-ready/examples/structured_output_validation.py"><span>PY</span><strong>Structured output validation</strong><small>Parse JSON, validate schema-like rules, then apply separate business validation.</small><i class="material-symbols-outlined" aria-hidden="true">code</i></a>
      <a href="/labs/ai-ready/examples/lexical_retrieval.py"><span>PY</span><strong>Lexical retrieval baseline</strong><small>Use a small TF-IDF style score before reaching for semantic search infrastructure.</small><i class="material-symbols-outlined" aria-hidden="true">code</i></a>
      <a href="/labs/ai-ready/examples/tool_loop.py"><span>PY</span><strong>Bounded tool loop</strong><small>Tool allowlist, step budget, duplicate-call detection, evidence, and stop state.</small><i class="material-symbols-outlined" aria-hidden="true">code</i></a>
      <a href="/labs/ai-ready/examples/eval_runner.py"><span>PY</span><strong>Deterministic eval runner</strong><small>Run a small golden set and fail on routing regressions.</small><i class="material-symbols-outlined" aria-hidden="true">code</i></a>
      <a href="/labs/ai-ready/examples/approval_state.py"><span>PY</span><strong>Approval state</strong><small>Bind approval to an exact prepared change, version precondition, and idempotency key.</small><i class="material-symbols-outlined" aria-hidden="true">code</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="labs" data-reveal>
    <header><p class="research-canvas__eyebrow">Hands-on track</p><h2>Then build four complete mini-systems.</h2><p>The examples teach mechanics. The labs combine the layers into a small working architecture.</p></header>
    <div class="research-route-list">
      <a href="/labs/ai-ready/labs/mcp-readonly/"><span>01</span><strong>Read-only MCP Workspace</strong><small>Projects, tasks, and notes through narrow tools and resources.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="/labs/ai-ready/labs/rag-evals/"><span>02</span><strong>RAG with Evals</strong><small>Knowledge corpus, retrieval baselines, citations, and regression cases.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="/labs/ai-ready/labs/agent-approval/"><span>03</span><strong>Agent with Approval</strong><small>Read-first investigation, prepared change, approval, safe execution.</small><i class="material-symbols-outlined" aria-hidden="true">approval</i></a>
      <a href="/labs/ai-ready/labs/production-readiness/"><span>04</span><strong>Production Readiness</strong><small>Versions, traces, eval gates, budgets, degraded mode, and rollback.</small><i class="material-symbols-outlined" aria-hidden="true">rocket_launch</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Architecture defaults</p><h2>Short rules to remember.</h2></header>
    <div class="research-route-list">
      <a href="/labs/ai-ready/engineering/prompt-context/"><span>TXT</span><strong>Transform text → prompt + schema</strong><small>Do not add retrieval or agents when the task is already self-contained.</small><i class="material-symbols-outlined" aria-hidden="true">edit_note</i></a>
      <a href="/labs/ai-ready/data-rag/"><span>RAG</span><strong>Changing knowledge → retrieval</strong><small>Use current evidence, provenance, and a no-evidence state.</small><i class="material-symbols-outlined" aria-hidden="true">search</i></a>
      <a href="/labs/ai-ready/tools-mcp/"><span>API</span><strong>Current fact/action → typed tool</strong><small>Validate inputs, outputs, permissions, errors, and side effects in code.</small><i class="material-symbols-outlined" aria-hidden="true">build</i></a>
      <a href="/labs/ai-ready/agent-architecture/"><span>WF</span><strong>Known steps → workflow</strong><small>Use an agent only when evidence changes the next useful action.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/labs/ai-ready/evals-reliability/"><span>EV</span><strong>Change behavior → run evals</strong><small>Model, prompt, retrieval, tool, and agent changes all need regression evidence.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Machine-readable layer</p><h2>The handbook is data too.</h2></header>
    <div class="research-route-list">
      <a href="/labs/ai-ready/data/engineering-map.json"><span>MAP</span><strong>Engineering Map</strong><small>13-step learning path, decisions, practice tasks, and runnable examples.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/labs/ai-ready/data/catalog.json"><span>CAT</span><strong>Architecture Catalog</strong><small>Use cases, architecture tracks, labs, production rules, and source metadata.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/labs/ai-ready/data/architecture-patterns.json"><span>GRF</span><strong>Architecture Patterns</strong><small>Use conditions, controls, failure modes, and graph links.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/ai-ready/data/eval-sample.jsonl"><span>EVAL</span><strong>Eval Cases</strong><small>General-purpose architecture decisions and failure paths.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Deep dives</p><h2>Architecture after the basics.</h2><p>Use these when a small example becomes a real system.</p></header>
    <div class="research-route-list">
      <a href="/labs/ai-ready/system-boundaries/"><span>SYS</span><strong>System Boundaries</strong><small>Model vs deterministic application responsibilities.</small><i class="material-symbols-outlined" aria-hidden="true">foundation</i></a>
      <a href="/labs/ai-ready/deep-dives/"><span>ALL</span><strong>Architecture Deep Dives</strong><small>RAG, tools/MCP, agents, evals, security, and production.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
