---
author: "Dzmitryi Kharlanau"
layout: default
title: "Release Readiness — Working Skill"
description: "A cross-domain method for deciding whether a change is ready to move into production based on scope, evidence, dependencies, rollback, monitoring, ownership, and business acceptance."
permalink: /skill-hub/problem-solving-operations/release-readiness-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/problem-solving-operations/">Problem Solving &amp; Operations</a></li><li aria-current="page">Release Readiness</li></ol></nav>

<article class="section note-detail atlas-page">
<p class="eyebrow">Working skill / Delivery control</p>
<h1>Ready means evidence exists for the risky parts.</h1>
<p class="lead">A release is not ready because the ticket says "tested". Readiness means the change boundary is known, critical behavior was validated, dependencies and owners are clear, rollback is possible, and production signals are prepared.</p>

<h2>Use when</h2>
<ul>
<li>A release, deployment, transport, configuration change, data load, model update, or integration change is approaching production.</li>
<li>Several teams own different parts of one release and the final go/no-go decision is unclear.</li>
<li>Testing passed but production dependencies, monitoring, rollback, or business readiness are uncertain.</li>
<li>A high-risk change needs explicit evidence before approval.</li>
</ul>

<h2>Required inputs</h2>
<ul>
<li>Release scope and change list.</li>
<li>Risk and impact assessment.</li>
<li>Test evidence and unresolved defects.</li>
<li>Dependencies, owners, deployment sequence, and production window.</li>
<li>Rollback or recovery approach.</li>
<li>Monitoring, alerting, support, and business communication plan.</li>
</ul>

<h2>Workflow</h2>
<ol>
<li><strong>Freeze the decision scope.</strong> State exactly what is included, excluded, and still changing.</li>
<li><strong>Classify release risk.</strong> Consider business criticality, data mutation, integration reach, security, reversibility, user volume, timing, and novelty.</li>
<li><strong>Review evidence by risk.</strong> Link each important risk to a test, review, control, or accepted exception.</li>
<li><strong>Check unresolved defects.</strong> Separate cosmetic issues, known limitations, accepted risks, and release blockers.</li>
<li><strong>Check dependencies.</strong> Validate versions, configuration, credentials, data, endpoints, jobs, feature flags, infrastructure, and external teams.</li>
<li><strong>Check production execution.</strong> Confirm sequence, owner per step, timing, access, automation, checkpoints, and stop conditions.</li>
<li><strong>Check rollback and recovery.</strong> Define when rollback is possible, when forward recovery is safer, and who can decide.</li>
<li><strong>Check observability.</strong> Identify the signals that prove the release works: errors, latency, throughput, business documents, data quality, user path, or queue health.</li>
<li><strong>Check business readiness.</strong> Confirm communications, support coverage, training or process changes, and accountable business acceptance when needed.</li>
<li><strong>Run go/no-go review.</strong> Record decision, conditions, exceptions, owners, and evidence gaps.</li>
<li><strong>Validate after release.</strong> Use the planned signals and close only after technical and business outcomes are stable.</li>
</ol>

<h2>Decision rules</h2>
<ul>
<li>No rollback does not automatically mean no-go, but the release then needs an explicit recovery strategy and stronger evidence.</li>
<li>A passed test is weak evidence if the test data, environment, or dependency state does not represent production risk.</li>
<li>An unresolved defect is acceptable only when impact, workaround, owner, and acceptance are explicit.</li>
<li>If critical dependencies have no confirmed owner or production state, readiness is not proven.</li>
<li>If monitoring cannot detect the main failure modes, add validation before release or define a manual control.</li>
<li>Do not hide a conditional go behind a green status. Record the condition and who owns it.</li>
</ul>

<h2>Output</h2>
<p>Produce a <strong>Release Readiness Record</strong> with scope, risk, evidence map, defects, dependencies, execution steps, rollback or recovery, monitoring, business readiness, go/no-go decision, conditions, and post-release validation.</p>

<h2>Quality gates</h2>
<ul>
<li>Release scope is frozen enough for a meaningful decision.</li>
<li>Critical risks have linked evidence or explicit acceptance.</li>
<li>Dependencies and owners are named.</li>
<li>Rollback or recovery is executable, not just described.</li>
<li>Production validation signals exist before release.</li>
<li>The go/no-go decision includes conditions and accountable owners.</li>
</ul>

<h2>Related skills</h2>
<ul>
<li><a href="/skill-hub/sap-ams/change-impact-analysis-working-skill/">Change Impact Analysis</a></li>
<li><a href="/skill-hub/testing-quality-delivery/deployment-readiness-checklist-working-skill/">Deployment Readiness Checklist</a></li>
<li><a href="/skill-hub/decision-validation/risk-dependency-mapping-working-skill/">Risk and Dependency Mapping</a></li>
<li><a href="/skill-hub/problem-solving-operations/procedure-design-working-skill/">Procedure / Runbook Design</a></li>
</ul>
</article>
