---
author: "Dzmitryi Kharlanau"
layout: default
title: "Evidence-Driven Troubleshooting — Working Skill"
description: "A product-neutral troubleshooting method for reproducing failures, isolating the first failing layer, testing hypotheses, changing safely, and validating recovery."
permalink: /skill-hub/problem-solving-operations/evidence-driven-troubleshooting-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/problem-solving-operations/">Problem Solving &amp; Operations</a></li><li aria-current="page">Evidence-Driven Troubleshooting</li></ol></nav>

<article class="section note-detail atlas-page">
<p class="eyebrow">Working skill / Troubleshooting</p>
<h1>Find the first failing layer before changing the system.</h1>
<p class="lead">Use this method when something does not work and the failing component is not yet known. It applies to enterprise applications, SaaS, APIs, background jobs, cloud services, files, and integration flows.</p>

<h2>Use when</h2>
<ul><li>A user reports an error but the responsible component is unclear.</li><li>The same workflow succeeds for one user, object, environment, or time period and fails for another.</li><li>A recent deployment, configuration change, data load, or dependency change may be related.</li><li>The team is already trying random fixes without a stable evidence set.</li></ul>

<h2>Required inputs</h2>
<ul><li>Observed behavior and expected behavior.</li><li>Exact time, environment, user or service identity, and affected object.</li><li>At least one failing example and, if possible, one known-good comparison.</li><li>Recent change history.</li><li>Access to the evidence source for the suspected layers: browser, logs, monitoring, API trace, data, queue, job, configuration, or platform telemetry.</li></ul>

<h2>Workflow</h2>
<ol>
<li><strong>State the symptom.</strong> Write one sentence that can be tested.</li>
<li><strong>Reproduce or verify.</strong> Do not diagnose a memory of an error.</li>
<li><strong>Capture evidence before changes.</strong> Save timestamps, identifiers, request IDs, screenshots, logs, payloads, status, and relevant configuration.</li>
<li><strong>Build the path.</strong> List the layers involved from trigger to business result.</li>
<li><strong>Find the first divergence.</strong> Compare failing and known-good cases and locate the earliest layer where they differ.</li>
<li><strong>Create small hypotheses.</strong> Each hypothesis must have a test that can reject it.</li>
<li><strong>Test one variable at a time.</strong> Record the result. Keep or reject the hypothesis.</li>
<li><strong>Choose the smallest safe action.</strong> Prefer reversible containment before permanent change.</li>
<li><strong>Validate end to end.</strong> Technical green status is not enough. Confirm the expected business result.</li>
<li><strong>Decide what comes next.</strong> Close, perform RCA, create a change, improve monitoring, or create a reusable procedure.</li>
</ol>

<h2>Diagnostic layers</h2>
<p>Use the layers that fit the system. Do not force every incident through every layer.</p>
<ol><li>Business input and object state</li><li>User or service identity and authorization</li><li>Client / browser / UI</li><li>Application logic</li><li>API or integration boundary</li><li>Queue, scheduler, or background processing</li><li>Data and persistence</li><li>Configuration and feature controls</li><li>Platform, network, database, or external dependency</li></ol>

<h2>Decision rules</h2>
<ul>
<li>If the symptom cannot be reproduced, collect more evidence before proposing a cause.</li>
<li>If failing and known-good cases differ, test the earliest meaningful difference first.</li>
<li>If a recent change correlates with the first failure, treat it as a hypothesis, not proof.</li>
<li>If a retry can create duplicates or inconsistent state, stop until idempotency or recovery behavior is known.</li>
<li>If the issue crosses a system boundary, preserve correlation IDs and evidence from both sides before escalation.</li>
<li>If the cause remains unclear after reasonable isolation, hand off with rejected hypotheses and missing evidence, not just “needs deeper analysis.”</li>
</ul>

<h2>Output</h2>
<p>Produce an <strong>Evidence-Driven Troubleshooting Record</strong> with symptom, scope, timeline, failing path, evidence, hypotheses, tests, isolated layer, action, risk, validation, and next skill.</p>

<h2>Quality gates</h2>
<ul><li>The symptom is testable.</li><li>Evidence was captured before material changes.</li><li>A known-good comparison was used when available.</li><li>At least one hypothesis was explicitly rejected.</li><li>The isolated layer explains the observed evidence.</li><li>The final validation checks the business result, not only a technical status.</li></ul>

<h2>Related skills</h2>
<ul><li><a href="/skill-hub/problem-solving-operations/data-reconciliation-working-skill/">Data Reconciliation</a></li><li><a href="/skill-hub/problem-solving-operations/process-deviation-analysis-working-skill/">Process Deviation Analysis</a></li><li><a href="/skill-hub/sap-ams/root-cause-analysis-working-skill/">Root Cause Analysis</a></li><li><a href="/skill-hub/problem-solving-operations/procedure-design-working-skill/">Procedure / Runbook Design</a></li><li><a href="/skill-hub/sap-ams/fiori-app-troubleshooting-working-skill/">SAP Fiori adapter example</a></li></ul>
</article>
