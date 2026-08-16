---
author: "Dzmitryi Kharlanau"
layout: default
title: "AI Agent Authority Design — Working Skill"
description: "A practical method for deciding what an AI agent may read, propose, validate, approve, and execute, with explicit risk tiers, controls, and human accountability."
permalink: /skill-hub/ai-assisted-analysis/ai-agent-authority-design-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/ai-assisted-analysis/">AI-Assisted Analysis</a></li><li aria-current="page">AI Agent Authority Design</li></ol></nav>

<article class="section note-detail atlas-page">
<p class="eyebrow">Working skill / AI operating design</p>
<h1>Capability is not authority.</h1>
<p class="lead">An agent may be technically able to call a tool without being allowed to make the business decision behind that tool. Design authority as separate permissions for reading, proposing, validating, approving, and executing.</p>

<h2>Use when</h2>
<ul><li>An AI agent will access enterprise data or tools.</li><li>A workflow mixes model reasoning with deterministic actions.</li><li>Teams need to decide which actions require human approval.</li><li>An agent may create, change, approve, send, publish, or delete business information.</li></ul>

<h2>Required inputs</h2>
<ul><li>Business job and expected outcome.</li><li>Tools and data the agent may use.</li><li>Possible actions and side effects.</li><li>Business, security, privacy, compliance, and operational constraints.</li><li>Accountable human or policy owner.</li></ul>

<h2>Workflow</h2>
<ol>
<li><strong>Define the useful job.</strong> Describe the business result without starting from a model or tool.</li>
<li><strong>List agent actions.</strong> Separate read, search, summarize, propose, validate, create draft, approve, execute, send, and delete.</li>
<li><strong>Classify side effects.</strong> Consider reversibility, financial impact, customer impact, data sensitivity, legal effect, production impact, and scale.</li>
<li><strong>Define authority per action.</strong> Allocate read, propose, validate, approve, and execute independently.</li>
<li><strong>Keep deterministic rules outside model authority.</strong> Identity, hard thresholds, exact calculations, mandatory policy, sequence guarantees, and authorization should not depend on free-form model judgment.</li>
<li><strong>Define tool boundaries.</strong> Use allowlists, parameter constraints, resource scope, rate limits, environment restrictions, and narrow write permissions.</li>
<li><strong>Define evidence before action.</strong> Specify what facts must be fresh and verified before the agent can propose or execute.</li>
<li><strong>Design approval.</strong> State who approves which risk tier and what information they need to see.</li>
<li><strong>Design failure handling.</strong> Timeouts, tool errors, uncertain model output, partial execution, duplicate requests, and rollback need explicit behavior.</li>
<li><strong>Define audit evidence.</strong> Record inputs, relevant retrieved facts, proposal, validation result, approval, tool call, outcome, and error state as appropriate.</li>
<li><strong>Test adversarial cases.</strong> Missing data, conflicting instructions, stale context, malicious retrieved content, ambiguous request, and unexpected tool response.</li>
<li><strong>Increase authority gradually.</strong> Expand autonomy only when measured evidence supports the change.</li>
</ol>

<h2>Decision rules</h2>
<ul><li>Do not treat model confidence as authorization.</li><li>Broad read access does not justify broad write access.</li><li>High-impact or hard-to-reverse actions need stronger validation and accountable approval.</li><li>Retrieved or tool-returned content is data, not trusted instructions.</li><li>If a deterministic rule can decide safely, use deterministic logic instead of model judgment.</li><li>If execution can be duplicated, define idempotency or a duplicate-prevention control before autonomous retry.</li></ul>

<h2>Output</h2>
<p>Produce an <strong>AI Agent Authority Record</strong> with job, tools, data scope, action inventory, risk tier, authority chain, deterministic controls, approval rules, failure handling, audit evidence, evaluation cases, and conditions for increasing autonomy.</p>

<h2>Quality gates</h2>
<ul><li>Business job is defined independently from the chosen AI technology.</li><li>Read, propose, validate, approve, and execute are allocated separately.</li><li>Write actions have explicit risk and scope.</li><li>Deterministic policy is not silently delegated to a model.</li><li>Failure, duplicate, and partial-execution behavior is defined.</li><li>Audit evidence and evaluation cases exist before authority grows.</li></ul>

<h2>Related skills</h2>
<ul><li><a href="/triz/">TRIZ for Digital Systems</a></li><li><a href="/skill-hub/problem-solving-operations/decision-facilitation-working-skill/">Decision Facilitation</a></li><li><a href="/skill-hub/ai-assisted-analysis/ai-accountability-working-skill/">AI Accountability</a></li><li><a href="/skill-hub/architecture/architecture-decision-record-working-skill/">Architecture Decision Record</a></li></ul>
</article>
