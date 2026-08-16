---
author: "Dzmitryi Kharlanau"
layout: default
title: "Data Discovery & Mapping — Working Skill"
description: "A cross-domain method for learning unfamiliar datasets, finding candidate keys and relationships, proposing mappings, and validating them with real data."
permalink: /skill-hub/problem-solving-operations/data-discovery-mapping-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/problem-solving-operations/">Problem Solving &amp; Operations</a></li><li aria-current="page">Data Discovery &amp; Mapping</li></ol></nav>

<article class="section note-detail atlas-page">
<p class="eyebrow">Working skill / Data operations</p>
<h1>Understand the data before writing the mapping.</h1>
<p class="lead">Use this skill when files or extracts arrive with weak documentation. Profile the real values, find stable keys and relationships, propose field mappings, and test them against data before saving reusable logic.</p>

<h2>Use when</h2>
<ul>
<li>Several Excel, CSV, database, or application extracts must be connected.</li>
<li>Column names are inconsistent and business meaning is partly unknown.</li>
<li>A migration, interface, reconciliation, or reporting task needs a mapping.</li>
<li>Manual file work repeats and should become a reusable data procedure.</li>
</ul>

<h2>Required inputs</h2>
<ul>
<li>Sample datasets or representative extracts.</li>
<li>Known business purpose and expected result.</li>
<li>Any available data dictionary, mapping, report definition, or process context.</li>
<li>Known sensitive fields and handling restrictions.</li>
</ul>

<h2>Workflow</h2>
<ol>
<li><strong>Inventory the datasets.</strong> Record file or table identity, source, time period, row count, columns, encoding, and refresh logic.</li>
<li><strong>Profile every column.</strong> Measure type, nulls, distinct count, common values, min/max, patterns, duplicates, and sample values.</li>
<li><strong>Infer business meaning carefully.</strong> Separate confirmed meaning from hypothesis based on name or values.</li>
<li><strong>Find candidate keys.</strong> Test uniqueness, nulls, stability, composite keys, and business versus technical identifiers.</li>
<li><strong>Find relationships.</strong> Test value overlap and cardinality between candidate fields across datasets.</li>
<li><strong>Identify transformations.</strong> Look for formatting, code translation, unit conversion, concatenation, splitting, date logic, defaults, and filtering.</li>
<li><strong>Propose mappings.</strong> For every mapped field record source, target, transformation, confidence, and evidence.</li>
<li><strong>Validate mappings on real rows.</strong> Join representative data, inspect matched and unmatched records, and check value-level consistency.</li>
<li><strong>Classify exceptions.</strong> Missing key, duplicate, unmapped code, format issue, timing issue, source defect, target rule, or unknown.</li>
<li><strong>Confirm uncertain semantics.</strong> Ask a domain owner only where data evidence cannot decide.</li>
<li><strong>Save reusable logic.</strong> Persist approved keys, mappings, transformations, checks, and tolerances as a reusable procedure when the work repeats.</li>
</ol>

<h2>Decision rules</h2>
<ul>
<li>Do not treat similar column names as proof of semantic equivalence.</li>
<li>A candidate key is not accepted until uniqueness and null behavior are measured.</li>
<li>If a mapping requires many exceptions, question the relationship before adding more rules.</li>
<li>Do not hide uncertain mapping logic inside code. Record confidence and unresolved meaning.</li>
<li>If sensitive data is present, minimize samples and avoid copying unnecessary values into public artifacts.</li>
</ul>

<h2>Output</h2>
<p>Produce a <strong>Data Discovery &amp; Mapping Record</strong> with dataset inventory, profiles, candidate keys, relationships, mapping table, transformation rules, exception classes, validation statistics, open questions, and reusable procedure candidates.</p>

<h2>Quality gates</h2>
<ul>
<li>Every dataset has a documented grain and time scope.</li>
<li>Candidate keys have measured uniqueness and null rates.</li>
<li>Relationships have evidence and cardinality.</li>
<li>Mappings separate confirmed rules from hypotheses.</li>
<li>Mappings are tested on real rows, not only column names.</li>
<li>Reusable logic includes validation checks, not only transformations.</li>
</ul>

<h2>Related skills</h2>
<ul><li><a href="/skill-hub/problem-solving-operations/data-reconciliation-working-skill/">Data Reconciliation</a></li><li><a href="/labs/reusable-data-procedures/">Reusable Data Procedures</a></li><li><a href="/skill-hub/dama-dmbok/data-quality-root-cause-working-skill/">Data Quality Root Cause</a></li></ul>
</article>
