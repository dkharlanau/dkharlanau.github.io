---
layout: default
title: "Machine Layer — Data, Agent Tools, and AI-Readable Sources"
description: "Technical entry point for datasets, AI-readable exports, agent tools, MCP packages, professional intelligence, and SAP Lead drills."
permalink: /machine/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-10-10
agent_connection: true
hide_global_cta: true
hide_site_share: true
tags:
  - datasets
  - ai-agents
  - machine-readable
  - mcp
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li aria-current="page">Machine Layer</li></ol>
</nav>

<div class="research-canvas hub-canvas hub-canvas--machine">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Machine layer / structured access</p>
      <h1>Turn public knowledge into usable machine context.</h1>
      <p>Datasets, AI exports, skills, tool descriptions, and local MCP packages expose stable structure for retrieval and automation. Credentials and private context stay outside the public site.</p>
      <a class="research-canvas__button" href="#agent-setup">Connect your agent <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <figure class="hub-canvas__visual">
      <img src="/assets/img/systems/master-data-lineage-journal.webp" alt="Several public data sources passing through identity, validation, and governance gates into one structured core with controlled downstream routes." width="1728" height="1081" decoding="async" fetchpriority="high" />
      <figcaption>Public sources → validation and structure → controlled reuse</figcaption>
    </figure>
    <div class="research-canvas__signal" aria-label="Machine layer">
      <p>Access types</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Data</strong><small>Canonical datasets</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>AI</strong><small>Readable exports</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Tools</strong><small>Skills and MCP</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>Reasoning</strong><small>Decision and evidence contracts</small></div>
      <em>Public files only. Runtime credentials, private corpora, and browser-local practice state stay outside the repository.</em>
    </div>
  </header>

  <section class="agent-setup" id="agent-setup" aria-label="Agent connection guide">
    {% include agent-connection.html setup=true %}
    <div class="agent-setup__steps">
      <h3>1. Read the site with web access</h3>
      <p>Paste the prompt above into your agent, then ask a specific question — for example, “How should I trace an IDoc that arrived but did not create the expected business document?” Your agent needs a browsing or HTTP retrieval tool. A URL pasted into a chat does not provide its contents by itself.</p>
      <p>The <a href="/llms.txt">source manifest</a> points to the public knowledge. For a retrieval pipeline, use the <a href="/ai/site-profile.json">site profile</a> and <a href="/ai/markdown-clusters.json">page index</a> to inspect available sources and their retrieval eligibility. If your agent has no web access, provide the relevant page text or downloaded file directly.</p>
      <h3>2. Add local MCP tools</h3>
      <p>For an MCP client that supports local stdio servers, install Node.js 20 or newer and Git, then clone the public repository on your computer:</p>
      <pre><code>git clone https://github.com/dkharlanau/dkharlanau.github.io.git</code></pre>
      <p>Add the following generic stdio configuration to your client’s MCP settings. Replace both example paths with the absolute path to your checkout; the settings file and field names depend on your client.</p>
      <pre><code>{
  "mcpServers": {
    "sap-diagnostics": {
      "command": "node",
      "args": ["/path/to/dkharlanau.github.io/mcp/sap-diagnostics-mcp/src/server.js"],
      "env": {
        "SAP_ATLAS_DATA_DIR": "/path/to/dkharlanau.github.io"
      }
    }
  }
}</code></pre>
      <p>Restart or reconnect the client and check that <code>search_diagnostics</code> is available. Ask it to search for IDoc diagnostics and inspect the returned URLs and review state. See the <a href="/mcp/sap-diagnostics-mcp/">MCP package guide</a> for the tool list and checks.</p>
      <p>The MCP package runs locally and reads public files. This GitHub Pages site provides static sources; it has no hosted MCP endpoint. No site account or API key is required. Keep your checkout current with <code>git pull --ff-only</code>.</p>
      <h3>Check the first answer</h3>
      <p>Look for source URLs, review status, and a clear distinction between evidence and assumptions. Local retrieval provides public context; any later access to SAP needs its own authorization.</p>
      <p>For reusable agent workflows, browse the <a href="https://github.com/dkharlanau/dkharlanau.github.io/tree/main/agent-skills">Agent Skills installation guide</a>. Choose a role profile rather than installing every skill.</p>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal aria-label="Machine layer boundary">
    <span class="material-symbols-outlined" aria-hidden="true">schema</span>
    <p><strong>Problem:</strong> useful knowledge becomes hard for tools to retrieve when every source has a different format, route, or level of structure.</p>
    <p><strong>Context:</strong> this static layer exposes public datasets, indexes, schemas, skills, tool descriptions, and reasoning contracts for retrieval, evaluation, and local automation. It does not run agents or private services.</p>
  </section>

  <section class="research-canvas__inventory" id="machine-routes" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Technical routes</p>
      <h2>One map for machine-facing assets.</h2>
      <p>The source collections keep their existing URLs and schemas.</p>
    </header>
    <div class="research-route-list">
      <a href="/machine/portfolio/"><span>MAP</span><strong>Public Project Map</strong><small>Seventeen public repositories grouped into enterprise design, transformation assurance, and SAP and practical AI routes.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/datasets/"><span>DATA</span><strong>Datasets</strong><small>Canonical structured collections, manifests, schemas, and domain-specific data packages.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
      <a href="/ai/"><span>AI</span><strong>AI-readable sources</strong><small>Generated and curated JSON, YAML, discovery maps, indexes, and expert evidence surfaces.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/ai/professional-intelligence.json"><span>MODEL</span><strong>Professional Intelligence Contract</strong><small>Readiness dimensions, the Lead decision chain, evidence levels, pressure routes, and privacy boundaries.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/interview-readiness/drills/"><span>DRILL</span><strong>SAP Lead Drill Layer</strong><small>Human-facing Decision Cards, progressive diagnostics, Boss Battles, and project-evidence coverage connected to the Professional Intelligence model.</small><i class="material-symbols-outlined" aria-hidden="true">fitness_center</i></a>
      <a href="/skill-hub/"><span>SKILL</span><strong>Skill Hub</strong><small>Human-readable map of reusable analysis, architecture, development, and decision skills.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="/agent-tools/"><span>TOOL</span><strong>Agent Tools</strong><small>Static tool descriptions for SAP diagnostics, ABAP, integration, data analysis, evaluation, and related work.</small><i class="material-symbols-outlined" aria-hidden="true">construction</i></a>
      <a href="/machine/assessment/"><span>ASSESS</span><strong>SAP Lead Assessment Access</strong><small>Case manifest, schemas, practice contracts, JSONL case sets, and the local read-only assessment MCP route.</small><i class="material-symbols-outlined" aria-hidden="true">psychology_alt</i></a>
      <a href="/mcp/sap-diagnostics-mcp/"><span>MCP</span><strong>SAP Diagnostics MCP</strong><small>A local, read-only package that consumes committed public artifacts. GitHub Pages publishes it but does not execute it.</small><i class="material-symbols-outlined" aria-hidden="true">terminal</i></a>
      <a href="/ai/public-portfolio.json"><span>JSON</span><strong>Public Portfolio Endpoint</strong><small>Machine-readable tracks, project roles, repository links, public entry points, observation date, and claim boundaries.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
    </div>
  </section>
</div>
