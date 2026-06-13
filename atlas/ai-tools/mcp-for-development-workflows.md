---
layout: default
title: "MCP for Development Workflows"
description: "Use the Model Context Protocol safely for development workflows: read-only vs write-capable tools, permission boundaries, and audit gates."
permalink: /atlas/ai-tools/mcp-for-development-workflows/
atlas_section: ai-tools
domain: AI-assisted development
subdomain: Tool integration
concept_type: operating pattern
sap_area: Developer automation / support tooling
business_process: Knowledge work
status: needs_verification
verified: false
level: 1
robots: noindex,follow
sitemap: false
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau
tags:
  - ai-tools
  - mcp
  - model-context-protocol
  - tool-integration
  - developer-automation
  - security
related:
  - /atlas/ai-tools/ai-coding-agents-landscape/
  - /atlas/ai-tools/ai-code-review-agents/
  - /atlas/ai-tools/ai-security-for-generated-code/
  - /atlas/ai-operations/ai-agent-for-sap-support/
  - /skill-hub/ai-assisted-development/mcp-development-workflow/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/ai-tools/">AI Tools</a></li>
    <li aria-current="page">MCP for Development Workflows</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">

<header class="note-header">
  <p class="eyebrow">Knowledge Atlas</p>
  <h1>MCP for development workflows</h1>
  <p class="note-subtitle">The Model Context Protocol connects agents to tools. The security model is not automatic: you must decide what each server is allowed to read and write.</p>
  <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
</header>

<aside class="atlas-meta-panel">
  <dl>
    <div><dt>Domain</dt><dd>AI-assisted development</dd></div>
    <div><dt>Type</dt><dd>operating pattern</dd></div>
    <div><dt>Last reviewed</dt><dd>2026-06-13</dd></div>
  </dl>
</aside>

<div class="note-body">

<h2>What MCP is</h2>

<p>The <a href="https://modelcontextprotocol.io/">Model Context Protocol (MCP)</a> is an open specification for connecting AI hosts such as Claude Code, Cursor, and Codex CLI to external tools and data sources. It defines a standard way for a host to discover tools, invoke them, and receive results over stdio or HTTP.</p>

<p>The practical value is interoperability: a tool provider writes one server and any MCP-compatible host can use it. The protocol does not define security, scope, or approval; those remain the team's responsibility.</p>

<h2>When to use it</h2>

<ul>
  <li>You want an agent to query documentation, search code, or read observability data without custom integrations.</li>
  <li>You need the same tool to work across multiple agents such as Claude Code, Cursor, and Codex CLI.</li>
  <li>You are building a tool integration and want to avoid provider-specific function-call formats.</li>
</ul>

<h2>When not to use it</h2>

<ul>
  <li>The integration needs complex long-running tasks that exceed MCP's current request/response model.</li>
  <li>You cannot define clear read/write boundaries for the tool.</li>
  <li>The authentication and authorization model of the server is unclear or untrusted.</li>
</ul>

<h2>Core concepts</h2>

<table>
  <thead>
    <tr><th>Component</th><th>Role</th></tr>
  </thead>
  <tbody>
    <tr><td>Host</td><td>The AI application that connects to servers, such as Claude Code or Cursor.</td></tr>
    <tr><td>Client</td><td>A protocol client inside the host that manages one server connection.</td></tr>
    <tr><td>Server</td><td>A service that exposes tools, resources, and prompts to the host.</td></tr>
    <tr><td>Tools</td><td>Actions the model can invoke, such as reading a file or creating a GitHub issue.</td></tr>
    <tr><td>Resources</td><td>Read-only data sources the model can reference, such as documentation.</td></tr>
  </tbody>
</table>

<h2>Read-only vs write-capable tools</h2>

<p>The most important decision is whether a server can only read or can also change state.</p>

<table>
  <thead>
    <tr><th>Type</th><th>Examples</th><th>Risk level</th></tr>
  </thead>
  <tbody>
    <tr><td>Read-only</td><td>Documentation retrieval, code search, observability queries</td><td>Lower; main risk is data exposure</td></tr>
    <tr><td>Write-capable</td><td>GitHub issue creation, file writes, deployment triggers</td><td>Higher; every write needs approval and audit</td></tr>
  </tbody>
</table>

<h2>Permission boundaries</h2>

<ul>
  <li><strong>Filesystem:</strong> Restrict to specific directories. Avoid giving an agent access to your entire home directory or to repositories it does not need.</li>
  <li><strong>GitHub:</strong> Use fine-grained tokens with minimal scopes. Separate read tokens from write tokens. Never give an agent admin access.</li>
  <li><strong>Browser/search:</strong> Limit to allow-listed domains and query types. Unrestricted web access can leak context and fetch malicious content.</li>
  <li><strong>Database:</strong> Prefer read-only replicas or views. Require explicit approval for any write.</li>
</ul>

<h2>Security risks</h2>

<ul>
  <li><strong>Tool poisoning:</strong> A malicious or compromised MCP server can expose dangerous tools with misleading names. Vet servers before installing.</li>
  <li><strong>Prompt injection:</strong> Data fetched through MCP resources can contain instructions that manipulate the agent. Treat external content as untrusted.</li>
  <li><strong>Over-permissioning:</strong> A server with broad scopes can do more damage than the model intended. Apply least privilege.</li>
  <li><strong>Secret leakage:</strong> Tools may log arguments or return values. Do not pass secrets, tokens, or private data through tool calls unless the server is trusted and isolated.</li>
</ul>

<h2>Safe workflow pattern</h2>

<ol>
  <li><strong>Inventory servers.</strong> List every MCP server the agent can reach and classify each as read-only or write-capable.</li>
  <li><strong>Assign scopes.</strong> Give each server the minimum permissions needed for its job.</li>
  <li><strong>Require approval for writes.</strong> Configure the host to ask before any write or destructive action.</li>
  <li><strong>Audit tool calls.</strong> Keep logs of what tools were called, with what arguments, and what changed.</li>
  <li><strong>Review after the fact.</strong> Periodically check that server permissions still match actual usage.</li>
</ol>

<h2>Human-in-the-loop gates</h2>

<ul>
  <li>Never allow an MCP tool to merge code, delete resources, or deploy to production without human approval.</li>
  <li>Use dry-run modes where available.</li>
  <li>Require a second human review for any change made by an agent through a write-capable MCP tool.</li>
</ul>

<h2>Practical evaluation criteria</h2>

<ul>
  <li>Can you list every MCP server your agents use?</li>
  <li>Does each server have the minimum necessary scope?</li>
  <li>Are write operations gated by explicit approval?</li>
  <li>Do you audit tool calls and their outcomes?</li>
  <li>Have you tested what happens if a server returns malicious or misleading content?</li>
</ul>

<p>MCP is a promising interoperability layer, not a security model. The hard work is still defining read/write boundaries, scopes, and approval gates; the protocol only makes the integration less custom.</p>

<h2>Related Atlas pages</h2>

<ul>
  <li><a href="/atlas/ai-tools/ai-coding-agents-landscape/">AI Coding Agents Landscape</a></li>
  <li><a href="/atlas/ai-tools/ai-code-review-agents/">AI Code Review Agents</a></li>
  <li><a href="/atlas/ai-tools/ai-security-for-generated-code/">AI Security for Generated Code</a></li>
  <li><a href="/atlas/ai-operations/ai-agent-for-sap-support/">AI Agent for SAP Support</a></li>
</ul>

<h2>Related Skill Hub pages</h2>

<ul>
  <li><a href="/skill-hub/ai-assisted-development/mcp-development-workflow/">MCP Development Workflow</a></li>
  <li><a href="/skill-hub/ai-assisted-development/ai-generated-code-review/">AI-Generated Code Review</a></li>
</ul>

<h2>Sources and limitations</h2>

<p>Primary sources: modelcontextprotocol.io specification, Anthropic engineering blog, and public MCP server documentation. MCP's authorization specification is still evolving; treat current auth patterns as transitional. Security research from 2025–2026 has documented prompt-injection and tool-poisoning risks in MCP ecosystems; consult current advisories before deploying in production.</p>

</div>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}

</article>
