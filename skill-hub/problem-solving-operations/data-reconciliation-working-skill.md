---
author: "Dzmitryi Kharlanau"
layout: default
title: "Data Reconciliation — Working Skill"
description: "A reusable method for comparing datasets, explaining differences, classifying exceptions, and proving that data is complete and consistent."
permalink: /skill-hub/problem-solving-operations/data-reconciliation-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/problem-solving-operations/">Problem Solving &amp; Operations</a></li><li aria-current="page">Data Reconciliation</li></ol></nav>

<article class="section note-detail atlas-page">
<p class="eyebrow">Working skill / Data operations</p>
<h1>Explain the difference, not only the count.</h1>
<p class="lead">Use this skill when two or more datasets should represent the same business reality but do not match. The method works for Excel, CSV, database extracts, interfaces, migrations, financial controls, master data, and operational reporting.</p>

<h2>Use when</h2>
<ul><li>Source and target row counts differ.</li><li>Totals match but individual records do not.</li><li>A migration, interface, data load, or report must be validated.</li><li>Teams compare files manually and cannot explain recurring exceptions.</li></ul>

<h2>Required inputs</h2>
<ul><li>Datasets or extracts to compare.</li><li>Business meaning of each dataset.</li><li>Candidate keys and relationship rules.</li><li>Expected filters, time windows, units, currencies, and aggregation level.</li><li>Known transformations or mappings.</li></ul>

<h2>Workflow</h2>
<ol>
<li><strong>Define the reconciliation question.</strong> State what should match and at which grain.</li>
<li><strong>Profile each dataset.</strong> Record columns, types, row counts, nulls, duplicates, date range, and key candidates.</li>
<li><strong>Normalize comparison rules.</strong> Align formats, units, currencies, time zones, casing, whitespace, and approved transformations.</li>
<li><strong>Validate keys.</strong> Check uniqueness, nulls, composite-key needs, and one-to-many relationships.</li>
<li><strong>Run structural checks.</strong> Missing columns, type changes, unexpected values, duplicate keys.</li>
<li><strong>Run population checks.</strong> Source only, target only, matched, duplicate, filtered, transformed.</li>
<li><strong>Run value checks.</strong> Compare important fields and totals at the correct business grain.</li>
<li><strong>Classify exceptions.</strong> Expected transformation, timing difference, mapping issue, missing record, duplicate, business rule, source defect, target defect, or unknown.</li>
<li><strong>Trace material differences.</strong> Follow a sample from source through transformation to target.</li>
<li><strong>Validate correction.</strong> Re-run the same reconciliation rules after the fix.</li>
<li><strong>Save reusable logic.</strong> If the work repeats, turn mappings, keys, checks, and tolerances into a reusable data procedure.</li>
</ol>

<h2>Decision rules</h2>
<ul><li>Never compare totals before confirming that both datasets use the same scope and grain.</li><li>If no stable key exists, stop and define a matching strategy before calculating exception counts.</li><li>If duplicates exist on a supposed unique key, treat that as a separate data-quality issue.</li><li>If a difference is allowed, document the rule and tolerance. “Expected difference” without a rule is not a result.</li><li>For large exception sets, classify first and inspect representative samples instead of reading rows one by one.</li></ul>

<h2>Output</h2>
<p>Produce a <strong>Data Reconciliation Record</strong> with dataset identity, scope, grain, keys, normalization rules, control totals, match statistics, exception classes, material examples, root causes, correction, and rerun evidence.</p>

<h2>Quality gates</h2>
<ul><li>Both datasets have a documented business grain.</li><li>Key quality is measured before matching.</li><li>Filters and time windows are identical or differences are explained.</li><li>Exceptions are classified, not stored as one unexplained bucket.</li><li>Material differences can be traced from source to target.</li><li>The same checks can be rerun after correction.</li></ul>

<h2>Related skills</h2>
<ul><li><a href="/labs/reusable-data-procedures/">Reusable Data Procedures</a></li><li><a href="/skill-hub/dama-dmbok/data-quality-root-cause-working-skill/">Data Quality Root Cause</a></li><li><a href="/skill-hub/problem-solving-operations/evidence-driven-troubleshooting-working-skill/">Evidence-Driven Troubleshooting</a></li></ul>
</article>
