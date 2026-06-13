---
layout: default
title: "MCP Development Workflow"
description: "Use MCP and tool servers safely for development workflows: read-only vs write-capable tools, permission boundaries, local filesystem risks, GitHub write risks, and audit logging."
permalink: /skill-hub/ai-assisted-development/mcp-development-workflow/
last_modified_at: 2026-06-13
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/ai-assisted-development/">AI-Assisted Development</a></li>
    <li aria-current="page">MCP Development Workflow</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — AI-Assisted Development</p>
  <h1>MCP development workflow</h1>
  <p class="lead">Use MCP and tool servers safely for development workflows: read-only vs write-capable tools, permission boundaries, local filesystem risks, GitHub write risks, and audit logging.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you connect MCP servers to coding agents without over-privileging them. The output is an MCP server inventory with classification, scopes, approval rules, and audit steps.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>You want an agent to read documentation, search code, or query observability data through MCP.</li>
      <li>You are considering an MCP server that can write to GitHub, the filesystem, or a deployment pipeline.</li>
      <li>You need to audit which tools your agents can invoke.</li>
      <li>You are building or deploying an MCP server for your team.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Connect a documentation MCP server</h3>
    <p>You add an MCP server that fetches internal docs. You classify it as read-only, restrict it to HTTPS, and verify it cannot write. The agent can now answer questions without gaining filesystem access.</p>
    <h3>Connect a GitHub MCP server</h3>
    <p>You add a GitHub MCP server so an agent can read issues. You use a fine-grained token with read-only issue access, not a token that can write code or merge PRs. Write access is reserved for explicit human approval.</p>
    <h3>Build a custom MCP server</h3>
    <p>You build an MCP server that wraps an internal API. You declare exactly which tools it exposes, use capability attestation where possible, and log every invocation for audit.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li><strong>MCP server list</strong> — every server the agent can reach.</li>
      <li><strong>Tool inventory</strong> — tools, resources, and prompts each server exposes.</li>
      <li><strong>Classification</strong> — read-only or write-capable for each tool.</li>
      <li><strong>Scope definitions</strong> — directories, repositories, domains, or API endpoints the tool may access.</li>
      <li><strong>Host configuration</strong> — approval settings, logging, and transport details.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What can each MCP server read and write?</li>
      <li>Does the server need broad access, or can it be scoped to one repo or directory?</li>
      <li>Who wrote the server, and can it be compromised or poisoned?</li>
      <li>Are tool calls logged for audit?</li>
      <li>What happens if a tool returns malicious instructions?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Inventory servers.</strong> List every MCP server configured in the agent host.</li>
      <li><strong>Map tools and resources.</strong> Document what each server exposes.</li>
      <li><strong>Classify risk.</strong> Mark each tool as read-only or write-capable.</li>
      <li><strong>Assign scopes.</strong> Restrict filesystem, GitHub, browser, and API access to the minimum needed.</li>
      <li><strong>Configure approval gates.</strong> Require explicit approval for every write or destructive action.</li>
      <li><strong>Enable logging.</strong> Record tool calls, arguments, and outcomes.</li>
      <li><strong>Review periodically.</strong> Check that permissions still match actual usage.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a server can write, it needs explicit approval for each write.</li>
      <li>If a server is from an untrusted source, do not install it.</li>
      <li>If a server requests broad filesystem access, deny or restrict it to a specific directory.</li>
      <li>If a server fetches web content, limit it to allow-listed domains.</li>
      <li>If a tool call can affect production, require a second human review.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>MCP inventory</strong> — server, tools, classification, scope, and owner.</li>
      <li><strong>Approval policy</strong> — which actions require human approval.</li>
      <li><strong>Audit log configuration</strong> — how tool calls are recorded.</li>
      <li><strong>Incident response note</strong> — what to do if a server is compromised.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>MCP inventory entry</h3>
    <pre><code>Server: [name]
Source: [official/community/internal]
Transport: [stdio/sse/http]
Tools:
- [tool name]: [read-only/write-capable]
- [tool name]: [read-only/write-capable]
Scope: [directories/repos/domains allowed]
Approval policy: [auto / prompt / block]
Owner: [team or individual]
Last reviewed: [date]
</code></pre>

    <h3>Approval policy</h3>
    <pre><code>Auto-allowed:
- Read-only documentation retrieval
- Read-only code search within allowed directories

Prompt-required:
- Any filesystem write
- Any GitHub issue/PR/comment creation
- Any deployment or CI trigger

Blocked:
- Repository deletion
- Secret or credential access
- Production data writes
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every MCP server is inventoried and classified.</li>
      <li>Write-capable tools require explicit approval.</li>
      <li>Scopes are restricted to the minimum necessary.</li>
      <li>Tool calls are logged and reviewable.</li>
      <li>Untrusted servers are not installed.</li>
      <li>The team knows the incident response path.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Installing servers without inventory.</strong> Consequence: unknown tools can be invoked.</li>
      <li><strong>Granting write access by default.</strong> Consequence: agents make unreviewed changes.</li>
      <li><strong>Ignoring prompt injection.</strong> Consequence: fetched content manipulates the agent.</li>
      <li><strong>Disabling logging.</strong> Consequence: no audit trail when something goes wrong.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, start by listing every MCP server available to the agent. Document each tool, its classification, and its scope before using it. Never assume a server is read-only; verify. Apply least privilege. If a tool request exceeds its declared scope, reject it and report. Keep logs of all tool invocations.</p>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/ai-assisted-development/ai-generated-code-review/">AI-Generated Code Review</a></li>
      <li><a href="/skill-hub/ai-assisted-development/ai-tool-selection-for-development/">AI Tool Selection for Development</a></li>
      <li><a href="/skill-hub/ai-assisted-analysis/ai-accountability-working-skill/">AI Accountability</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/ai-tools/mcp-for-development-workflows/">MCP for Development Workflows</a></li>
      <li><a href="/atlas/ai-tools/ai-security-for-generated-code/">AI Security for Generated Code</a></li>
      <li><a href="/atlas/ai-tools/ai-coding-agents-landscape/">AI Coding Agents Landscape</a></li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of MCP security practice. The MCP specification and authorization model are evolving; verify current guidance on modelcontextprotocol.io and follow current security advisories.</p>
  </section>

</article>
