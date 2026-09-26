---
layout: default
title: "FMEA — Failure Mode and Effects Analysis"
description: "How to use FMEA to identify failure modes, consequences, causes, controls, and improvement actions before release."
permalink: /skill-hub/tools-frameworks/fmea/
last_modified_at: 2026-09-26
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/tools-frameworks/">Tools &amp; Frameworks</a></li><li aria-current="page">FMEA</li></ol></nav>
<article class="section note-detail atlas-page">
<p class="eyebrow">Risk and resilience tool</p><h1>FMEA</h1>
<p class="lead">Use Failure Mode and Effects Analysis before release or design approval when the team needs to ask systematically: how can this fail, what happens if it fails, why could it fail, how would we detect it, and what control should reduce the risk?</p>

<section><h2>Core fields</h2>
<table class="study-table"><thead><tr><th>Field</th><th>Question</th></tr></thead><tbody>
<tr><td>Function / step</td><td>What is supposed to happen?</td></tr>
<tr><td>Failure mode</td><td>How could it fail?</td></tr>
<tr><td>Effect</td><td>What is the business or system consequence?</td></tr>
<tr><td>Cause</td><td>What could produce the failure?</td></tr>
<tr><td>Control</td><td>What prevents or detects it today?</td></tr>
<tr><td>Action</td><td>What should change?</td></tr>
</tbody></table>
</section>

<section><h2>Working method</h2>
<ol>
<li>Choose one process, interface, release, or design area.</li>
<li>Walk through each important function or step.</li>
<li>List credible failure modes.</li>
<li>Describe effects before debating causes.</li>
<li>Identify causes and current prevention/detection controls.</li>
<li>Use severity, occurrence, and detectability ratings only with agreed scales.</li>
<li>Prioritize actions using business criticality and evidence, not one score alone.</li>
<li>Assign owners and verify the residual risk after action.</li>
</ol></section>

<section><h2>SAP example</h2>
<p>Function: replicate Business Partner to a downstream system. Failure mode: message accepted by middleware but rejected downstream. Effect: customer cannot be used for fulfilment. Cause: invalid country-specific field combination. Current control: technical monitoring only. Action: add business validation before send plus a reconciliation alert for accepted-but-not-created records.</p></section>

<section><h2>Decision rules</h2><ul>
<li>If a failure has severe business impact but low detectability, strengthen detection even if occurrence is low.</li>
<li>If a control only detects the symptom after business impact, look for an upstream preventive control.</li>
<li>If a rating cannot be justified with evidence or an agreed scale, mark it as judgment rather than precision.</li>
<li>If the failure already happened, pair FMEA with evidence-driven root cause analysis instead of using FMEA as a substitute for investigation.</li>
</ul></section>

<section><h2>Copyable template</h2>
<pre><code>| Function | Failure mode | Effect | Cause | Current control | Risk evidence | Action | Owner |
|---|---|---|---|---|---|---|---|</code></pre></section>

<section><h2>Pair it with</h2><ul>
<li><a href="/skill-hub/problem-solving-operations/failure-mode-resilience-review-working-skill/">Failure-Mode &amp; Resilience Review</a></li>
<li><a href="/skill-hub/problem-solving-operations/control-design-working-skill/">Control Design</a></li>
<li><a href="/skill-hub/sap-ams/root-cause-analysis-working-skill/">Root Cause Analysis</a></li>
</ul></section>

<section><h2>Verification status and limitations</h2><p>FMEA has industry-specific variants and scoring conventions. This page uses the common reasoning structure, not a regulated industry procedure.</p></section>
</article>
