---
author: "Dzmitryi Kharlanau"
layout: default
title: "Configuration Drift Analysis — Working Skill"
description: "A cross-domain method for explaining why environments or systems behave differently by comparing effective configuration, version, feature state, dependencies, and deployment history."
permalink: /skill-hub/problem-solving-operations/configuration-drift-analysis-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/problem-solving-operations/">Problem Solving &amp; Operations</a></li><li aria-current="page">Configuration Drift Analysis</li></ol></nav>

<article class="section note-detail atlas-page">
<p class="eyebrow">Working skill / Environment diagnostics</p>
<h1>Compare effective state, not configuration screenshots.</h1>
<p class="lead">When DEV works and production does not, or two tenants behave differently, the useful question is which effective configuration difference explains the behavior. Build a controlled diff across version, settings, feature flags, secrets, dependencies, data, and deployment history.</p>

<h2>Use when</h2>
<ul>
<li>The same function behaves differently between environments, tenants, regions, or nodes.</li>
<li>A release appears correct but production behavior does not match test.</li>
<li>Configuration was changed manually or through several delivery paths.</li>
<li>A suspected drift needs evidence before synchronization.</li>
</ul>

<h2>Required inputs</h2>
<ul>
<li>Failing and known-good environments or instances.</li>
<li>Exact behavior difference and one representative scenario.</li>
<li>Relevant configuration exports, effective settings, versions, feature flags, deployment history, and dependency endpoints where available.</li>
<li>Expected source of truth for configuration.</li>
</ul>

<h2>Workflow</h2>
<ol>
<li><strong>Define the behavioral difference.</strong> Record the same input and expected result in both environments.</li>
<li><strong>Define comparison scope.</strong> Identify components, services, modules, business rules, and dependencies that can affect the scenario.</li>
<li><strong>Capture effective state.</strong> Prefer runtime or effective configuration over intended repository values.</li>
<li><strong>Compare versions and deployment state.</strong> Application version, package, schema, plugin, runtime, model, or transport level may differ.</li>
<li><strong>Compare configuration.</strong> Settings, flags, routes, endpoints, thresholds, jobs, policies, and environment variables.</li>
<li><strong>Compare identity and secrets references.</strong> Check references and expiry state without exposing secret values.</li>
<li><strong>Compare dependencies.</strong> External services, data sources, queues, storage, reference data, and network routes.</li>
<li><strong>Compare data conditions.</strong> A behavior difference can come from business data rather than configuration.</li>
<li><strong>Rank differences by causal relevance.</strong> Do not treat every diff as a defect.</li>
<li><strong>Test one difference.</strong> Use a safe reversible test or controlled reproduction.</li>
<li><strong>Correct through the governed source.</strong> Avoid manual production synchronization if configuration should be managed elsewhere.</li>
<li><strong>Validate and prevent recurrence.</strong> Confirm behavior and add drift detection or deployment control where useful.</li>
</ol>

<h2>Decision rules</h2>
<ul>
<li>A configuration diff is evidence of difference, not proof of cause.</li>
<li>If runtime state differs from source-controlled state, investigate delivery or override mechanisms before editing runtime values.</li>
<li>If data differs materially, separate data-condition analysis from configuration drift.</li>
<li>Do not copy all settings from a working environment into production as a diagnostic shortcut.</li>
<li>If sensitive credentials or security policy are involved, compare metadata and ownership rather than secret values.</li>
</ul>

<h2>Output</h2>
<p>Produce a <strong>Configuration Drift Analysis Record</strong> with scenario, environments, effective-state diff, version diff, dependency diff, data-condition diff, candidate causes, test evidence, correction source, and prevention control.</p>

<h2>Quality gates</h2>
<ul>
<li>The same scenario is compared in both environments.</li>
<li>Effective runtime state is distinguished from intended state.</li>
<li>Version, configuration, dependencies, identity references, and data conditions are considered separately.</li>
<li>Candidate differences are ranked by causal relevance.</li>
<li>The correction uses the governed source of truth where one exists.</li>
<li>Validation confirms behavior after correction.</li>
</ul>

<h2>Related skills</h2>
<ul><li><a href="/skill-hub/problem-solving-operations/evidence-driven-troubleshooting-working-skill/">Evidence-Driven Troubleshooting</a></li><li><a href="/skill-hub/sap-ams/change-impact-analysis-working-skill/">Change Impact Analysis</a></li><li><a href="/skill-hub/problem-solving-operations/release-readiness-working-skill/">Release Readiness</a></li></ul>
</article>
