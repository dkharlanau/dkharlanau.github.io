---
layout: default
title: "AI Coding Agents Landscape"
description: "Terminal agents, IDE agents, and autonomous engineering agents: how they differ, when to use each, and how to choose without losing engineering control."
permalink: /atlas/ai-tools/ai-coding-agents-landscape/
atlas_section: ai-tools
domain: AI-assisted development
subdomain: Coding agents
concept_type: decision framework
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
  - coding-agents
  - claude-code
  - codex
  - cursor
  - copilot
  - aider
  - developer-automation
related:
  - /atlas/ai-tools/repository-context-packaging/
  - /atlas/ai-tools/repomix-for-ai-codebase-analysis/
  - /atlas/ai-tools/mcp-for-development-workflows/
  - /atlas/ai-tools/ai-code-review-agents/
  - /atlas/automation/agent-assisted-development-workflows/
  - /skill-hub/ai-assisted-development/ai-coding-agent-task-design/
  - /skill-hub/ai-assisted-development/ai-tool-selection-for-development/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/ai-tools/">AI Tools</a></li>
    <li aria-current="page">AI Coding Agents Landscape</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">

<header class="note-header">
  <p class="eyebrow">Knowledge Atlas</p>
  <h1>AI coding agents landscape</h1>
  <p class="note-subtitle">The right agent depends on where you work, how much context you can share, and how much autonomy you are willing to delegate.</p>
  <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
</header>

<aside class="atlas-meta-panel">
  <dl>
    <div><dt>Domain</dt><dd>AI-assisted development</dd></div>
    <div><dt>Type</dt><dd>decision framework</dd></div>
    <div><dt>Last reviewed</dt><dd>2026-06-13</dd></div>
  </dl>
</aside>

<div class="note-body">

<h2>What problem this solves</h2>

<p>Coding agents can read files, edit code, run tests, and even open pull requests. But they are not interchangeable. Some live in the terminal, some inside an IDE, and some run asynchronously in the cloud. Some work with any model; others lock you into one provider. Choosing the wrong agent for the task produces noise, cost overruns, or unsafe changes.</p>

<h2>Three agent shapes</h2>

<h3>1. Terminal agents</h3>

<p>Terminal agents run in your shell. They are editor-agnostic and work well for developers who already live in the terminal, over SSH, or in CI contexts.</p>

<table>
  <thead>
    <tr><th>Tool</th><th>Vendor</th><th>Key traits</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="https://github.com/openai/codex">Codex CLI</a></td><td>OpenAI</td><td>Open-source Rust CLI; cloud tasks in OpenAI-managed sandboxes; bundled with ChatGPT Plus/Pro; MCP-native.</td></tr>
    <tr><td><a href="https://claude.com/code">Claude Code</a></td><td>Anthropic</td><td>Terminal-first agent; strong multi-file reasoning; native MCP; project memory via <code>CLAUDE.md</code>; usage-based billing.</td></tr>
    <tr><td><a href="https://github.com/Aider-AI/aider">Aider</a></td><td>Open source (Paul Gauthier)</td><td>BYO-LLM, model-agnostic via LiteLLM; git-native auto-commits; repo map; architect mode; no PTY required for headless use.</td></tr>
  </tbody>
</table>

<p>Terminal agents are best for: complex refactors, backend work, long-running tasks, headless runs, and teams that want to stay editor-agnostic.</p>

<h3>2. IDE agents</h3>

<p>IDE agents embed AI into the editor. They excel at daily coding, visual diffs, and inline assistance.</p>

<table>
  <thead>
    <tr><th>Tool</th><th>Vendor</th><th>Key traits</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="https://cursor.com">Cursor</a></td><td>Anysphere</td><td>VS Code fork with Composer multi-file agent, tab completion, Agents Window for parallel tasks, and MCP support.</td></tr>
    <tr><td><a href="https://windsurf.com">Windsurf</a></td><td>Codeium / OpenAI (acquired May 2026)</td><td>VS Code fork with Cascade agentic flow; lower starting price; strategic uncertainty after acquisition.</td></tr>
    <tr><td><a href="https://github.com/features/copilot">GitHub Copilot</a></td><td>GitHub / Microsoft</td><td>IDE extension for VS Code, JetBrains, Neovim, Xcode; agent mode for synchronous multi-step tasks; coding agent for async issue-to-PR.</td></tr>
  </tbody>
</table>

<p>IDE agents are best for: front-end work, daily editing, visual diff review, and teams that prefer a GUI.</p>

<h3>3. Autonomous engineering agents</h3>

<p>These agents attempt to carry out larger engineering tasks with less continuous supervision.</p>

<table>
  <thead>
    <tr><th>Tool</th><th>Vendor</th><th>Key traits</th></tr>
  </thead>
  <tbody>
    <tr><td>Devin</td><td>Cognition</td><td>Cloud-based autonomous engineer; high cost; waitlist/enterprise focus.</td></tr>
    <tr><td><a href="https://github.com/All-Hands-AI/OpenHands">OpenHands</a></td><td>Open source (All Hands AI)</td><td>Docker-based sandboxed agent; multi-model; heavier setup.</td></tr>
    <tr><td><a href="https://github.com/princeton-nlp/SWE-agent">SWE-agent</a></td><td>Open source (Princeton NLP)</td><td>Research agent for GitHub issues; strong benchmark results; not a commercial product.</td></tr>
  </tbody>
</table>

<p>Autonomous agents are best for: well-specified isolated tasks, research, benchmarking, and environments with strong review gates.</p>

<h2>Decision criteria</h2>

<table>
  <thead>
    <tr><th>Question</th><th>If yes, consider</th></tr>
  </thead>
  <tbody>
    <tr><td>Do you work mostly in the terminal or over SSH?</td><td>Codex CLI, Claude Code, Aider</td></tr>
    <tr><td>Do you want inline completion and visual diffs?</td><td>Cursor, Windsurf, Copilot</td></tr>
    <tr><td>Are you already deep in the OpenAI ecosystem?</td><td>Codex CLI, ChatGPT Copilot</td></tr>
    <tr><td>Do you need model flexibility or local models?</td><td>Aider, OpenHands</td></tr>
    <tr><td>Is your workflow GitHub-centric?</td><td>GitHub Copilot coding agent, CodeRabbit</td></tr>
    <tr><td>Do you need maximum reasoning on complex refactors?</td><td>Claude Code, Cursor</td></tr>
    <tr><td>Do you need fully autonomous issue-to-PR?</td><td>Devin, OpenHands, Copilot coding agent</td></tr>
  </tbody>
</table>

<h2>When to use which tool</h2>

<ul>
  <li><strong>Repomix + terminal agent</strong> for architecture audits and focused implementation tasks.</li>
  <li><strong>Cursor / Copilot</strong> for daily editing and small-scope changes inside the IDE.</li>
  <li><strong>Claude Code / Codex CLI</strong> for complex, multi-file refactors and terminal-centric workflows.</li>
  <li><strong>Aider</strong> when you want model choice, git-native workflow, or programmatic invocation.</li>
  <li><strong>CodeRabbit / Copilot code review</strong> for first-pass review before a human approves.</li>
</ul>

<h2>Safety and privacy checks</h2>

<ul>
  <li>Cloud agents copy repository content to vendor-managed infrastructure. Review the vendor's data policy before use.</li>
  <li>Terminal agents with shell access can run destructive commands. Use permission prompts, sandboxing, and dry runs.</li>
  <li>IDE agents may send code to third-party models. Configure privacy modes and enterprise controls where available.</li>
  <li>Autonomous agents need explicit stop conditions and human review gates before merge.</li>
</ul>

<h2>Common mistakes</h2>

<ul>
  <li>Treating an IDE agent as a substitute for architectural thinking.</li>
  <li>Letting a terminal agent run broad shell commands without reviewing the plan.</li>
  <li>Using a cloud agent on a private repo without checking data residency.</li>
  <li>Comparing agents by hype instead of by workflow fit.</li>
</ul>

<h2>Related Atlas pages</h2>

<ul>
  <li><a href="/atlas/ai-tools/repository-context-packaging/">Repository Context Packaging</a></li>
  <li><a href="/atlas/ai-tools/repomix-for-ai-codebase-analysis/">Repomix for AI Codebase Analysis</a></li>
  <li><a href="/atlas/ai-tools/mcp-for-development-workflows/">MCP for Development Workflows</a></li>
  <li><a href="/atlas/ai-tools/ai-code-review-agents/">AI Code Review Agents</a></li>
  <li><a href="/atlas/automation/agent-assisted-development-workflows/">Agent-Assisted Development Workflows</a></li>
</ul>

<h2>Related Skill Hub pages</h2>

<ul>
  <li><a href="/skill-hub/ai-assisted-development/ai-coding-agent-task-design/">AI Coding Agent Task Design</a></li>
  <li><a href="/skill-hub/ai-assisted-development/ai-tool-selection-for-development/">AI Tool Selection for Development</a></li>
  <li><a href="/skill-hub/ai-assisted-development/ai-generated-code-review/">AI-Generated Code Review</a></li>
</ul>

<h2>Sources and limitations</h2>

<p>Primary sources: official product pages and GitHub repositories for Codex CLI, Claude Code, Aider, Cursor, Windsurf, GitHub Copilot, OpenHands, and SWE-agent. Pricing and feature availability change frequently; verify on official sites. Claims about benchmark performance are vendor or third-party reported and should be treated as directional, not proof of suitability for a specific codebase.</p>

</div>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}

</article>
