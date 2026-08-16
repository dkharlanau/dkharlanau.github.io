---
author: "Dzmitryi Kharlanau"
layout: default
title: "Process Deviation Analysis — Working Skill"
description: "A cross-domain method for finding where an actual process diverged from expected behavior and identifying the control, data, timing, configuration, or ownership reason."
permalink: /skill-hub/problem-solving-operations/process-deviation-analysis-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/problem-solving-operations/">Problem Solving &amp; Operations</a></li><li aria-current="page">Process Deviation Analysis</li></ol></nav>

<article class="section note-detail atlas-page">
<p class="eyebrow">Working skill / Process diagnostics</p>
<h1>Find the first point where reality left the expected path.</h1>
<p class="lead">Use this skill when a business object exists and the process continued, but the route, status, value, owner, or outcome is wrong.</p>

<h2>Use when</h2>
<ul><li>A document or case followed the wrong branch.</li><li>A workflow skipped, blocked, or selected the wrong owner.</li><li>A calculation, determination, routing, status, or approval result differs from a known-good case.</li><li>The issue may come from data, rules, configuration, timing, integration, or user input.</li></ul>

<h2>Required inputs</h2>
<ul><li>One failing case and preferably one comparable successful case.</li><li>Expected process sequence or business rule.</li><li>Actual timestamps, statuses, decisions, inputs, and system events.</li><li>Relevant master/reference data and rule/configuration values.</li><li>Recent process or system changes.</li></ul>

<h2>Workflow</h2>
<ol>
<li><strong>Define expected outcome.</strong> State what should have happened.</li>
<li><strong>Trace the actual sequence.</strong> Build the real path from trigger to current state.</li>
<li><strong>Compare with a known-good path.</strong> Align both cases step by step.</li>
<li><strong>Find the first divergence.</strong> Ignore later symptoms until the first difference is explained.</li>
<li><strong>Compare inputs at that decision point.</strong> Data, rule, status, time, organization, role, configuration, feature flag, external response, or custom logic.</li>
<li><strong>Identify the decision mechanism.</strong> Which rule or component selected the next state?</li>
<li><strong>Test the explanation.</strong> Confirm that the same condition explains both the failing and successful case.</li>
<li><strong>Classify the deviation.</strong> Input, data, rule/configuration, code, integration timing, authorization, manual action, process design, or unknown.</li>
<li><strong>Define correction and regression scope.</strong> Fix the case and identify other cases that may be affected by the same condition.</li>
<li><strong>Validate the business path.</strong> Repeat or simulate the decision with corrected conditions.</li>
</ol>

<h2>Decision rules</h2>
<ul><li>Start with the first divergence, not the final error message.</li><li>If the failed and successful cases have different inputs, test those differences before assuming a platform defect.</li><li>If the rule behaved as designed but the business result is wrong, the problem is process or rule design, not technical execution.</li><li>If timing changes the result, record the exact sequence and dependency state.</li><li>If a manual correction hides the deviation, preserve the original evidence before changing the case.</li></ul>

<h2>Output</h2>
<p>Produce a <strong>Process Deviation Record</strong> with expected path, actual path, first divergence, decision mechanism, input comparison, deviation class, correction, regression scope, and validation evidence.</p>

<h2>Quality gates</h2>
<ul><li>The expected path is explicit.</li><li>The first divergence is identified.</li><li>The relevant decision inputs are compared.</li><li>The explanation covers both failing and known-good behavior.</li><li>Regression scope includes other objects that share the same rule or condition.</li></ul>

<h2>Related skills</h2>
<ul><li><a href="/skill-hub/problem-solving-operations/evidence-driven-troubleshooting-working-skill/">Evidence-Driven Troubleshooting</a></li><li><a href="/skill-hub/business-analysis/business-rules-discovery-working-skill/">Business Rules Discovery</a></li><li><a href="/skill-hub/sap-ams/change-impact-analysis-working-skill/">Change Impact Analysis</a></li></ul>
</article>
