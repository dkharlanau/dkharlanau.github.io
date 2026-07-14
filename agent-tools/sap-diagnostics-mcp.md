---
layout: default
title: SAP Diagnostics MCP
description: A local-first, read-only MCP server that retrieves public SAP Atlas knowledge.
permalink: /agent-tools/sap-diagnostics-mcp/
robots: noindex,follow
sitemap: false
status: needs_verification
verified: false
last_reviewed: 2026-07-14
---
<section class="section note-detail"><p class="eyebrow">Local package</p><h1>SAP Diagnostics MCP</h1><p class="lead">A deterministic stdio server for public Atlas records. It is local-first, credential-free, and read-only.</p><div class="note-body"><h2>What it does</h2><p>The package searches reviewed diagnostics, retrieves an Atlas record, follows related topics, produces evidence checklists and incident briefs, and searches the static tool registry. It does not connect to SAP or make remote calls.</p><h2>Incident Lab loop</h2><p>The package can also retrieve a synthetic case, evaluate an agent response against required evidence and sources, then return a revision step. The loop is a quality check, not a root-cause engine or operational approval. Use the browser-based <a href="/agent-tools/incident-lab/">SAP Incident Lab</a> to inspect the same public cases.</p><h2>Install</h2><p>The source package is in <code>mcp/sap-diagnostics-mcp</code>. From that directory, run <code>npm install .</code>, then use its README and <code>examples/mcp.json</code> to configure a local stdio client. Verify client-specific syntax against the client’s official documentation.</p><h2>Response contract</h2><p>Each diagnostic response includes a stable record ID, canonical URL, review state, review date, public evidence references, limitations, and related topics. The server has no write tool and no SAP credential setting.</p><h2>Example</h2><pre><code>get_incident_case({"case_id":"idoc-status-51-vendor-master"})
run_incident_loop({"case_id":"idoc-status-51-vendor-master", "response":{"hypotheses":["application posting error"]}})</code></pre></div></section>
