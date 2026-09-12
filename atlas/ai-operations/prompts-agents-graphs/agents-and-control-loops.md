---
layout: default
title: "Agents Are Feedback Loops, Not Digital Employees"
description: "A practical model of AI agents as decision loops with tools, observations, stopping conditions, state, and bounded autonomy."
permalink: /atlas/ai-operations/prompts-agents-graphs/agents-and-control-loops/
atlas_section: ai-operations
domain: Enterprise AI architecture
subdomain: Agentic systems
concept_type: concept deep dive
status: needs_verification
verified: false
level: 1
last_modified_at: 2026-09-12
author: Dzmitryi Kharlanau
robots: noindex,follow
sitemap: false
tags:
  - agents
  - control-loops
  - tools
  - enterprise-ai
related:
  - /atlas/ai-operations/prompts-agents-graphs/
  - /atlas/ai-operations/prompts-agents-graphs/three-graphs/
  - /atlas/ai-operations/ai-agent-for-sap-support/
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/ai-operations/">AI Operations</a></li><li><a href="/atlas/ai-operations/prompts-agents-graphs/">Prompts → Agents → Graphs</a></li><li aria-current="page">Agents and control loops</li></ol></nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Architecture layer 2 · Agency</p>
    <h1>Agents are feedback loops, not digital employees</h1>
    <p class="note-subtitle">The least misleading way to understand an agent is not to imagine a tiny employee living inside the model. Imagine a controller that repeatedly observes, chooses, acts, and checks what happened.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <div class="note-body">
    <h2>The word “agent” became too cheap</h2>
    <p>A chatbot with a system prompt is sometimes called an agent. A scheduled script with one LLM call is called an agent. A multi-hour coding system with shell access is also called an agent. The term now covers so much that it can hide more than it explains.</p>
    <p>A better architectural test is simple: <strong>does the model choose what to do next based on feedback from the environment?</strong> If the path is predefined by code, we mostly have a workflow. If the model can inspect the situation, select a tool or subtask, observe the result, and revise its next action, agency has entered the design.</p>

    <h2>The minimum useful loop</h2>
    <pre><code>Goal
  ↓
Observe current state
  ↓
Choose next action
  ↓
Use tool / produce result
  ↓
Observe environment again
  ↓
Done? ── no ──→ choose next action
  │
 yes
  ↓
Return result + evidence</code></pre>
    <p>The intelligence is not merely in the model call. It is in the loop between the model and something outside the model. A coding agent reads a repository, edits files, runs tests, sees failures, and changes course. A support agent reads permitted evidence, chooses a diagnostic check, receives a result, and decides whether it has enough evidence to continue.</p>

    <h2>Five parts that matter more than the agent's name</h2>
    <div class="decision-table"><table><thead><tr><th>Part</th><th>Question</th><th>Typical failure</th></tr></thead><tbody>
      <tr><td>Objective</td><td>What does “done” mean?</td><td>The agent optimizes for activity instead of outcome.</td></tr>
      <tr><td>Observations</td><td>What facts can it inspect?</td><td>It reasons fluently over incomplete or stale context.</td></tr>
      <tr><td>Actions / tools</td><td>What may it do?</td><td>A broad tool gives a model more authority than the use case needs.</td></tr>
      <tr><td>Policy</td><td>Which actions require rules or approval?</td><td>Autonomy silently crosses a business-risk boundary.</td></tr>
      <tr><td>Stopping condition</td><td>When must the loop stop, escalate, or fail?</td><td>The agent keeps spending, retrying, or compounding an error.</td></tr>
    </tbody></table></div>

    <h2>Workflow versus agent is a control decision</h2>
    <p>Anthropic's practical distinction is useful: workflows orchestrate models and tools through predefined code paths; agents let the model dynamically direct its process and tool use. That does not make agents “more advanced” in every case. It means control moves from code toward the model.</p>
    <p>If an invoice must always pass the same seven validations, deterministic workflow control is a feature. If an incident can require a different diagnostic path depending on logs, system state, historical patterns, and missing evidence, allowing the model to choose the next diagnostic step may be valuable.</p>
    <p>The design question is therefore not “Can an agent do this?” Frontier models can attempt many things. The question is “Where is model-directed control worth the added uncertainty, cost, latency, and evaluation burden?”</p>

    <h2>Why tool design often matters more than extra reasoning</h2>
    <p>Suppose an agent has one tool named <code>run_sap_action(request: string)</code>. It is wonderfully flexible and architecturally alarming. The model must translate vague intent into an unbounded action, and reviewers have little contract to inspect.</p>
    <p>Now compare narrow tools:</p>
    <pre><code>read_bp_field(bp_id, field)
read_replication_status(message_id)
compare_source_target(bp_id, field)
create_correction_draft(bp_id, expected_value, evidence_ids)
request_owner_approval(draft_id)</code></pre>
    <p>The agent can still reason flexibly, but the environment exposes smaller, testable capabilities. Tool schemas become part of the safety model. Anthropic's later guidance on tools makes a similar point: agents depend heavily on clear, well-designed interfaces and evaluations, not merely on a stronger model.</p>

    <h2>“Multi-agent” is not a synonym for “serious”</h2>
    <p>Splitting one problem into five fictional job titles can make a diagram impressive while making the system worse. Every handoff creates another context boundary, another chance to lose evidence, another latency cost, and another thing to evaluate.</p>
    <p>Use multiple agents when there is a genuine reason to separate control or context: different tool permissions, different expertise contracts, independent evaluation, parallel investigation, or a clear manager/worker decomposition. Do not create a “Researcher Agent,” “Thinker Agent,” and “Writer Agent” merely because humans have departments.</p>
    <p>A single agent with good tools and a well-designed state model is often easier to understand and debug than a swarm.</p>

    <h2>Ground truth is the difference between a loop and a hallucination carousel</h2>
    <p>An agent should repeatedly touch reality. For a coding task, reality is the repository, compiler, tests, and runtime. For an enterprise process, reality may be a system status, a message log, an approved document, a database record, a reconciliation result, or a human decision.</p>
    <p>If the agent only reads its own previous prose, an iterative loop can make a wrong story more polished without making it more true. Environmental feedback must be designed into the loop.</p>

    <h2>Autonomy should follow reversibility</h2>
    <p>A practical enterprise rule is to grant more autonomy where mistakes are cheap, observable, and reversible, and less where the blast radius is high.</p>
    <ul>
      <li><strong>Usually safe to automate earlier:</strong> search, classification, summarization, evidence collection, duplicate detection, draft generation, read-only comparisons.</li>
      <li><strong>Often needs explicit gates:</strong> master-data writes, financial decisions, authorization changes, configuration changes, production releases, irreversible external communication.</li>
    </ul>
    <p>This is not anti-agent conservatism. It is what lets useful autonomy survive contact with production.</p>

    <h2>The deeper transition</h2>
    <p>Once an agent can perform several steps, the next bottleneck is rarely another persona. It is continuity and structure. What has already happened? Which evidence is still valid? Which branch was tried? Which action changed the environment? What is the current state? Which entity is this evidence about?</p>
    <p>That is where state and graphs enter — not because “graphs come after agents” on a trend chart, but because longer-running decisions need explicit representations of execution and reality.</p>

    <h2>Primary references</h2>
    <ul>
      <li><a href="https://www.anthropic.com/engineering/building-effective-agents" target="_blank" rel="noopener noreferrer">Anthropic — Building effective agents</a></li>
      <li><a href="https://www.anthropic.com/engineering/writing-tools-for-agents" target="_blank" rel="noopener noreferrer">Anthropic — Writing effective tools for agents</a></li>
      <li><a href="https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/" target="_blank" rel="noopener noreferrer">OpenAI — A practical guide to building AI agents</a></li>
    </ul>

    <h2>Next</h2>
    <p>Continue with <a href="/atlas/ai-operations/prompts-agents-graphs/three-graphs/">Three graphs people keep mixing together</a>.</p>
  </div>

  <section class="atlas-related"><h2>Related pages</h2><ul><li><a href="/atlas/ai-operations/prompts-agents-graphs/prompts-to-systems/">Why prompts become a layer</a></li><li><a href="/atlas/ai-operations/prompts-agents-graphs/three-graphs/">Three graph types</a></li><li><a href="/atlas/ai-operations/ai-agent-for-sap-support/">AI Agent for SAP Support</a></li></ul></section>
  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>