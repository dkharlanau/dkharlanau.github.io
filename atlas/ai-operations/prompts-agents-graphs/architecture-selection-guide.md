---
layout: default
title: "Architecture Selection Guide: Prompt, Workflow, Agent, RAG, or Graph?"
description: "A practical decision guide for choosing the smallest AI architecture that solves the real problem without unnecessary agents, graphs, or autonomy."
permalink: /atlas/ai-operations/prompts-agents-graphs/architecture-selection-guide/
atlas_section: ai-operations
domain: Enterprise AI architecture
subdomain: Architecture decisions
concept_type: decision guide
status: needs_verification
verified: false
level: 1
last_modified_at: 2026-09-12
author: Dzmitryi Kharlanau
robots: noindex,follow
sitemap: false
tags:
  - architecture
  - agents
  - rag
  - graphs
  - decision-framework
related:
  - /atlas/ai-operations/prompts-agents-graphs/
  - /atlas/automation/rule-based-automation-vs-ai/
  - /atlas/ai-operations/ai-agent-for-sap-support/
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/ai-operations/">AI Operations</a></li><li><a href="/atlas/ai-operations/prompts-agents-graphs/">Prompts → Agents → Graphs</a></li><li aria-current="page">Architecture selection guide</li></ol></nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Decision guide · Use the smallest sufficient architecture</p>
    <h1>Prompt, workflow, agent, RAG, or graph?</h1>
    <p class="note-subtitle">A mature architecture does not contain the largest number of fashionable components. It contains the smallest set of components that can meet the outcome, evidence, control, and recovery requirements.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <div class="note-body">
    <h2>Start with the failure you need to eliminate</h2>
    <p>Technology-first questions create technology-shaped answers. “How can we use agents?” produces agents. “Where can we use a knowledge graph?” produces a graph. Neither question establishes that the component is useful.</p>
    <p>Start instead with an operational failure:</p>
    <ul>
      <li>the model gives inconsistent outputs for the same bounded task;</li>
      <li>the answer lacks current evidence;</li>
      <li>the correct next step depends on what a tool returns;</li>
      <li>a process must pause, retry, branch, or recover;</li>
      <li>the same entity appears across many systems and documents;</li>
      <li>the current state cannot be explained without reconstructing prior events;</li>
      <li>an action cannot be trusted unless its outcome is re-observed.</li>
    </ul>
    <p>Each failure suggests a different architectural addition.</p>

    <h2>The shortest useful map</h2>
    <div class="decision-table"><table><thead><tr><th>If the problem is...</th><th>Start with...</th><th>Do not jump straight to...</th></tr></thead><tbody>
      <tr><td>One bounded transformation or explanation</td><td>Prompt + structured output + evaluation</td><td>Agent</td></tr>
      <tr><td>Known sequence of steps</td><td>Deterministic workflow</td><td>Multi-agent orchestration</td></tr>
      <tr><td>Need current external facts or actions</td><td>Tools with narrow contracts</td><td>Longer prompt</td></tr>
      <tr><td>Need information from a document corpus</td><td>Retrieval / RAG</td><td>Knowledge graph by default</td></tr>
      <tr><td>Next step depends on observations and cannot be fully preplanned</td><td>Agent loop</td><td>Large fixed workflow pretending to cover every branch</td></tr>
      <tr><td>Run must pause, resume, retry, or expose paths</td><td>Structured state + execution graph</td><td>Chat transcript as state</td></tr>
      <tr><td>Relationships are the main query</td><td>Domain / knowledge graph</td><td>Vector search alone</td></tr>
      <tr><td>Sequence, lineage, and causality matter</td><td>Event history + provenance graph</td><td>Current snapshot only</td></tr>
      <tr><td>System may change real business state</td><td>Approval/policy gates + action tools + independent verification</td><td>Unbounded autonomous agent</td></tr>
    </tbody></table></div>

    <h2>Use a prompt when uncertainty is inside one decision</h2>
    <p>A prompt is enough when all relevant context can be supplied, the task has a clear end, and no external feedback is needed during execution. Classification, extraction, rewriting, comparison, and bounded analysis often fit here.</p>
    <p>Strengthen this design with examples, output schemas, deterministic validations, and an evaluation set before inventing orchestration.</p>

    <h2>Use a workflow when the path is known</h2>
    <p>If the business process says A must happen before B, and B before C, encode that sequence. An LLM can participate in individual steps without controlling the whole process.</p>
    <pre><code>extract fields
  → validate required fields
  → classify exception
  → create draft
  → human review
  → publish</code></pre>
    <p>This is not less advanced than an agent. It is more appropriate when predictability is part of the requirement.</p>

    <h2>Use tools when the model needs reality</h2>
    <p>Retrieval and tools are often the real upgrade people attribute to agents. If a model answers poorly because it lacks live order status, give it a read tool. If it cannot create a ticket, expose a narrow ticket-creation tool. If it needs authoritative policy, retrieve the policy.</p>
    <p>Do not compensate for missing reality with stronger language in the prompt.</p>

    <h2>Use RAG when the problem is finding relevant evidence</h2>
    <p>RAG is appropriate when useful facts live in documents or records too large or dynamic to place permanently in the prompt. It reduces the need to rely on model memory and can attach source evidence.</p>
    <p>But RAG does not automatically give the corpus a coherent domain model. Retrieving five relevant chunks about a Business Partner does not tell the system that two chunks refer to the same BP, which source owns an attribute, or which message caused a later state change.</p>

    <h2>Use an agent when the next step genuinely cannot be fixed in advance</h2>
    <p>An agent earns its complexity when the system must repeatedly inspect an environment and decide what to do next. Examples include open-ended code modification, complex research, or diagnostics where each observation changes the investigation path.</p>
    <p>Before using an agent, define:</p>
    <ul>
      <li>the objective and stopping condition;</li>
      <li>the permitted observations;</li>
      <li>the permitted actions;</li>
      <li>budget and iteration limits;</li>
      <li>high-risk action gates;</li>
      <li>how success will be verified;</li>
      <li>how traces will be evaluated.</li>
    </ul>

    <h2>Use an execution graph when runs become operational objects</h2>
    <p>If a run can last long enough to fail, pause, branch, wait for approval, or resume later, represent its state explicitly. The execution graph makes possible transitions inspectable and gives recovery a defined location.</p>
    <p>This is especially useful when an enterprise process cannot simply restart from the beginning after a partial write.</p>

    <h2>Use a knowledge graph when relationships are not incidental</h2>
    <p>A graph becomes useful when the system repeatedly asks multi-hop relationship questions:</p>
    <ul>
      <li>Which interfaces can update this attribute?</li>
      <li>Which process steps depend on this master-data object?</li>
      <li>Which systems receive data from this source through this transformation?</li>
      <li>Which controls, owners, and policies govern this business entity?</li>
    </ul>
    <p>If the dominant question is simply “find relevant text,” semantic retrieval may be simpler.</p>

    <h2>Use an event/provenance model when “why” is temporal</h2>
    <p>Current state answers <em>what</em>. Event history often answers <em>why</em>.</p>
    <p>If root cause depends on ordering, retries, stale messages, competing writers, approvals, transformations, or version changes, preserve the event chain. Do not ask an LLM to infer history from a final snapshot.</p>

    <h2>Use a closed loop when the system is allowed to act</h2>
    <p>The moment an AI system can change a production state, success criteria and post-action verification become first-class architecture.</p>
    <p>A controlled action pattern is:</p>
    <pre><code>evidence
  → recommendation
  → deterministic preconditions
  → authorization / approval
  → narrow action
  → independent post-state read
  → acceptance test
  → exception or completion</code></pre>

    <h2>Red flags that architecture is being driven by hype</h2>
    <ul>
      <li>The team has named five agents but cannot define one measurable outcome.</li>
      <li>The graph schema starts with technology categories rather than business questions.</li>
      <li>“Memory” means sending the whole transcript back to the model.</li>
      <li>The agent can write data but has no independent verifier.</li>
      <li>The design uses RAG and a graph but cannot state which queries require each one.</li>
      <li>Every failure is answered by adding another LLM call.</li>
      <li>There is no deterministic baseline to prove the agent improved anything.</li>
    </ul>

    <h2>A practical enterprise architecture stack</h2>
    <p>For a genuinely complex case, the final system may still contain many layers:</p>
    <pre><code>Experience / API layer
        ↓
Agent or workflow policy
        ↓
Execution state + checkpoints
        ↓
Tools and deterministic controls
        ↓
Retrieval + domain graph + event history
        ↓
Enterprise systems and documents
        ↓
Observability + verification + evaluation</code></pre>
    <p>The important thing is that every layer has a job. None is present merely to make the architecture look current.</p>

    <h2>The career implication</h2>
    <p>Knowing how to prompt a model is useful. Knowing an agent framework is useful. But the more defensible skill is being able to decide <em>which representation and control structure the business problem needs</em>.</p>
    <p>That requires combining domain knowledge with system design: entities, events, ownership, dependencies, failure modes, permissions, tools, state, evaluations, and recovery. In enterprise AI, this combination is often scarcer than familiarity with any one framework.</p>

    <h2>One question to keep</h2>
    <blockquote>What is the smallest explicit model of reality and control that would let this system make a better decision than a prompt alone?</blockquote>
    <p>If the answer is “none,” keep the prompt. If the answer is “it needs to inspect a tool and choose the next check,” add agency. If it needs to understand connected entities and reconstruct change, add the relevant graph. Architecture should follow the missing capability.</p>

    <h2>Continue</h2>
    <p>Return to the <a href="/atlas/ai-operations/prompts-agents-graphs/">cluster map</a>, or connect these concepts to the existing <a href="/atlas/ai-operations/ai-agent-for-sap-support/">AI Agent for SAP Support</a> architecture.</p>
  </div>

  <section class="atlas-related"><h2>Related pages</h2><ul><li><a href="/atlas/automation/rule-based-automation-vs-ai/">Rule-Based Automation vs AI</a></li><li><a href="/atlas/ai-operations/prompts-agents-graphs/closed-loop-enterprise-ai/">Verified closed loop</a></li><li><a href="/atlas/ai-operations/prompts-agents-graphs/sap-business-partner-change-case/">SAP Business Partner graph case</a></li></ul></section>
  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>