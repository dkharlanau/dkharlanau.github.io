---
author: "Dzmitryi Kharlanau"
layout: default
title: "Data Migration Validation — Working Skill"
description: "A cross-domain method for proving that migrated data is complete, correct, usable, and reconciled at business level before and after cutover."
permalink: /skill-hub/problem-solving-operations/data-migration-validation-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/problem-solving-operations/">Problem Solving &amp; Operations</a></li><li aria-current="page">Data Migration Validation</li></ol></nav>

<article class="section note-detail atlas-page">
<p class="eyebrow">Working skill / Data delivery</p>
<h1>Prove that the business object survived the move.</h1>
<p class="lead">Migration success is not a green load log. Validate that the right population moved, values were transformed correctly, relationships still work, business processes can use the data, and important exceptions are understood.</p>

<h2>Use when</h2>
<ul><li>Master, transactional, reference, or historical data moves between systems.</li><li>A mock load, rehearsal, cutover load, or post-go-live reconciliation needs evidence.</li><li>Technical load counts match but business users still report missing or unusable data.</li><li>A migration has mappings, defaults, filters, transformations, or deduplication rules.</li></ul>

<h2>Required inputs</h2>
<ul><li>Migration scope and business objects.</li><li>Source and target extracts or controlled samples.</li><li>Approved mappings, keys, filters, transformations, and default rules.</li><li>Expected population, time scope, and business grain.</li><li>Critical business scenarios that consume the migrated data.</li></ul>

<h2>Workflow</h2>
<ol>
<li><strong>Define the validation contract.</strong> State what population should move, what may be excluded, and what business result proves success.</li>
<li><strong>Freeze source scope.</strong> Record extraction time, filters, counts, and data version.</li>
<li><strong>Validate structure.</strong> Check required target fields, formats, code domains, relationships, and mandatory values.</li>
<li><strong>Validate population.</strong> Compare source eligible, excluded, loaded, rejected, target-only, duplicate, and missing records.</li>
<li><strong>Validate keys and relationships.</strong> Confirm identity mapping, parent-child links, references, and cross-object consistency.</li>
<li><strong>Validate transformations.</strong> Test code mappings, defaults, units, dates, currencies, aggregation, splitting, and derivation rules.</li>
<li><strong>Validate critical values.</strong> Compare business-important fields and control totals at the correct grain.</li>
<li><strong>Classify exceptions.</strong> Expected exclusion, known transformation, source defect, mapping defect, load defect, target rule, duplicate, or unknown.</li>
<li><strong>Run business-use tests.</strong> Prove migrated data can be searched, changed, referenced, processed, reported, or integrated as required.</li>
<li><strong>Sample risk-based cases.</strong> Include high-value, edge, historical, multilingual, unusual-code, and relationship-heavy records where relevant.</li>
<li><strong>Re-run after correction.</strong> Use the same controls so evidence is comparable.</li>
<li><strong>Record acceptance.</strong> State remaining exceptions, owner, business acceptance, and post-go-live controls.</li>
</ol>

<h2>Decision rules</h2>
<ul><li>Row count equality is not enough when records can be split, merged, filtered, or deduplicated.</li><li>Validate at business grain before comparing totals.</li><li>If key mapping is unstable, stop value reconciliation until identity is resolved.</li><li>A rejected record is acceptable only when reason, owner, and treatment are known.</li><li>Technical load success does not replace business-use validation.</li><li>For large populations, combine deterministic controls with risk-based sampling rather than manual inspection of random rows.</li></ul>

<h2>Output</h2>
<p>Produce a <strong>Data Migration Validation Record</strong> with scope, source freeze, population reconciliation, key and relationship checks, transformation controls, exception classes, business-use tests, acceptance, and rerun evidence.</p>

<h2>Quality gates</h2>
<ul><li>Source population and extraction point are reproducible.</li><li>Eligible, excluded, loaded, rejected, missing, and duplicate populations are explained.</li><li>Key and relationship integrity is measured.</li><li>Transformation rules are tested with real records.</li><li>Critical business scenarios use migrated data successfully.</li><li>Exceptions have treatment and ownership.</li></ul>

<h2>Related skills</h2>
<ul><li><a href="/skill-hub/problem-solving-operations/data-discovery-mapping-working-skill/">Data Discovery &amp; Mapping</a></li><li><a href="/skill-hub/problem-solving-operations/data-reconciliation-working-skill/">Data Reconciliation</a></li><li><a href="/skill-hub/problem-solving-operations/release-readiness-working-skill/">Release Readiness</a></li></ul>
</article>
