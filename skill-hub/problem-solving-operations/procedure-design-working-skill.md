---
author: "Dzmitryi Kharlanau"
layout: default
title: "Procedure / Runbook Design — Working Skill"
description: "A reusable method for turning repeated operational work into an executable procedure with evidence, decision points, stop conditions, rollback, escalation, and validation."
permalink: /skill-hub/problem-solving-operations/procedure-design-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/problem-solving-operations/">Problem Solving &amp; Operations</a></li><li aria-current="page">Procedure / Runbook Design</li></ol></nav>

<article class="section note-detail atlas-page">
<p class="eyebrow">Working skill / Operational design</p>
<h1>Write the procedure so another person can stop safely.</h1>
<p class="lead">A useful runbook is not a list of clicks. It explains when to start, what evidence to collect, what result to expect, when to stop, how to recover, and who owns the next decision.</p>

<h2>Use when</h2>
<ul><li>The same operational task is performed repeatedly.</li><li>A recovery or support activity depends too much on one person's memory.</li><li>A task has risk, approvals, rollback, or escalation conditions.</li><li>An agent or junior consultant should execute part of the work under clear boundaries.</li></ul>

<h2>Required inputs</h2>
<ul><li>Purpose and expected business outcome.</li><li>Trigger and frequency.</li><li>Scope and exclusions.</li><li>Preconditions, access, tools, and dependencies.</li><li>Known risks and irreversible actions.</li><li>Executor, approver, business owner, and escalation owner.</li><li>At least one real or synthetic execution example.</li></ul>

<h2>Workflow</h2>
<ol>
<li><strong>Define the outcome.</strong> Describe success in observable terms.</li>
<li><strong>Define the trigger.</strong> State exactly when the procedure starts and when it must not be used.</li>
<li><strong>List preconditions.</strong> Access, data, approvals, backups, system state, and dependencies.</li>
<li><strong>Split the work into decision-sized steps.</strong> One step should produce one observable result.</li>
<li><strong>Add expected result and evidence to every important step.</strong></li>
<li><strong>Add decision points.</strong> Continue, retry, branch, stop, rollback, or escalate.</li>
<li><strong>Add stop conditions before risky actions.</strong> Do not hide them at the end of the document.</li>
<li><strong>Define rollback and recovery.</strong> State what can be reversed and what cannot.</li>
<li><strong>Define ownership.</strong> Separate executor, approver, business decision, and escalation.</li>
<li><strong>Define completion criteria.</strong> Include business validation and reconciliation where relevant.</li>
<li><strong>Dry-run the procedure.</strong> Give it to someone who did not write it. Record where they become uncertain.</li>
<li><strong>Version it.</strong> Capture owner, last review, change history, and next review trigger.</li>
</ol>

<h2>Step contract</h2>
<pre><code>Step
- Action
- Input
- Expected result
- Evidence
- Decision point
- Risk
- Continue / retry / stop / rollback / escalate
</code></pre>

<h2>Decision rules</h2>
<ul><li>If a step has no observable expected result, it is too vague.</li><li>If a risky action has no rollback or escalation rule, the procedure is not operationally ready.</li><li>If the executor must use hidden expert judgment, write the decision rule or link a separate Skill.</li><li>If the same branch contains complex diagnosis, call a troubleshooting Skill instead of expanding the runbook indefinitely.</li><li>If a procedure changes frequently because inputs vary, separate stable method from case-specific Template fields.</li></ul>

<h2>Output</h2>
<p>Produce a <strong>Procedure Definition</strong> and a copy-ready <strong>Run Record Template</strong>. The definition contains the stable method. The run record contains one execution with evidence and decisions.</p>

<h2>Quality gates</h2>
<ul><li>Trigger and exclusions are explicit.</li><li>Every critical step has an expected result.</li><li>Evidence requirements are named.</li><li>Stop and escalation conditions appear before dangerous actions.</li><li>Rollback is defined or explicitly impossible.</li><li>Completion includes business validation.</li><li>A second person can execute the procedure without relying on undocumented memory.</li></ul>

<h2>Related skills</h2>
<ul><li><a href="/labs/templates/#runbook">Procedure / Runbook Template</a></li><li><a href="/skill-hub/skill-template-contract/">Skill → Template Contract</a></li><li><a href="/skill-hub/problem-solving-operations/evidence-driven-troubleshooting-working-skill/">Evidence-Driven Troubleshooting</a></li><li><a href="/skill-hub/sap-ams/operational-knowledge-capture-working-skill/">Operational Knowledge Capture</a></li></ul>
</article>
