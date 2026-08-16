---
author: "Dzmitryi Kharlanau"
layout: default
title: "Delta / Cutoff Control — Working Skill"
description: "A practical method to control incremental data windows, cutoffs, watermarks, late arrivals, duplicates, reprocessing, and reconciliation across migrations and integrations."
permalink: /skill-hub/problem-solving-operations/delta-cutoff-control-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/problem-solving-operations/">Problem Solving &amp; Operations</a></li><li aria-current="page">Delta / Cutoff Control</li></ol></nav>

<section class="section atlas-hero">
  <p class="eyebrow">Working Skill / Data &amp; Cutover</p>
  <h1>Define exactly where one data window ends and the next begins.</h1>
  <p class="lead">Incremental loads and cutovers fail at boundaries: inclusive versus exclusive timestamps, late records, clock differences, retries, duplicates, and forgotten backfills. Delta control makes the boundary explicit and reconciles what crossed it.</p>
</section>

<section class="section">
  <header class="section-heading"><h2>Use this skill when</h2></header>
  <ul>
    <li>Designing incremental file, API, event, CDC, or batch extraction.</li>
    <li>Preparing migration deltas between mock, preload, freeze, and go-live.</li>
    <li>Defining a business cutoff for orders, inventory, invoices, or master data.</li>
    <li>Reprocessing failed time windows.</li>
    <li>Investigating missing or duplicated records around a boundary.</li>
  </ul>
</section>

<section class="section">
  <header class="section-heading"><h2>Operating model</h2></header>
  <p><strong>Population → Delta Key → Window → Watermark → Extract → Apply → Reconcile → Advance</strong></p>
</section>

<section class="section">
  <header class="section-heading"><h2>Method</h2></header>
  <ol>
    <li><strong>Define the population.</strong> State which business objects belong to the flow and which are excluded.</li>
    <li><strong>Choose the delta key.</strong> Creation time, change time, sequence, version, event offset, document number range, or source-provided change token.</li>
    <li><strong>Define window semantics.</strong> State timezone and whether start/end values are inclusive or exclusive.</li>
    <li><strong>Define the watermark.</strong> Record when it is read, stored, advanced, and recovered after failure.</li>
    <li><strong>Handle late arrivals.</strong> Decide whether to use overlap, lookback, source change log, replay, or periodic full reconciliation.</li>
    <li><strong>Handle duplicates.</strong> Define stable business or technical keys and idempotent apply behaviour.</li>
    <li><strong>Control reprocessing.</strong> A failed window must be repeatable without silently skipping or duplicating records.</li>
    <li><strong>Define business cutoff.</strong> For migrations or cutovers, state when source transactions stop, continue in delta mode, or require manual control.</li>
    <li><strong>Reconcile each window.</strong> Compare counts, keys, totals, statuses, and exceptions before advancing the accepted watermark where risk requires it.</li>
    <li><strong>Record evidence.</strong> Keep window ID, parameters, extracted/applied counts, rejected records, watermark, and reconciliation result.</li>
  </ol>
</section>

<section class="section">
  <header class="section-heading"><h2>Boundary questions</h2></header>
  <table>
    <thead><tr><th>Question</th><th>Risk if unclear</th></tr></thead>
    <tbody>
      <tr><td>Which timestamp or sequence drives delta?</td><td>Changed records may never be selected</td></tr>
      <tr><td>Is the end boundary inclusive?</td><td>Duplicates or gaps between runs</td></tr>
      <tr><td>Which timezone is authoritative?</td><td>Records around daylight or zone boundaries shift windows</td></tr>
      <tr><td>When does watermark advance?</td><td>Failure may skip unprocessed records</td></tr>
      <tr><td>How are late arrivals handled?</td><td>Old business events appear after the window has closed</td></tr>
      <tr><td>Can the same window be replayed?</td><td>Recovery creates duplicates or requires manual guessing</td></tr>
    </tbody>
  </table>
</section>

<section class="section">
  <header class="section-heading"><h2>Working template</h2></header>
  <pre><code>Delta / Cutoff Control Record

Flow:
Population:
Delta key:
Timezone:
Window start:
Window end:
Boundary semantics:
Watermark before:
Watermark after:

Late-arrival strategy:
Duplicate strategy:
Replay strategy:
Business cutoff:
Source freeze / open transactions:

Extracted count:
Applied count:
Rejected count:
Reconciliation:
Exceptions:
Decision to advance watermark:
Owner:
</code></pre>
</section>

<section class="section">
  <header class="section-heading"><h2>Quality gates</h2></header>
  <ul>
    <li>Delta key and timezone are explicit.</li>
    <li>Inclusive/exclusive boundary semantics are documented.</li>
    <li>Watermark is not advanced before required processing evidence exists.</li>
    <li>Late arrivals and replay are designed, not improvised after failure.</li>
    <li>Apply logic is duplicate-aware.</li>
    <li>Cutover delta has reconciliation before business handover.</li>
  </ul>
</section>

<section class="section">
  <header class="section-heading"><h2>Related skills</h2></header>
  <ul>
    <li><a href="/skill-hub/problem-solving-operations/data-migration-validation-working-skill/">Data Migration Validation</a></li>
    <li><a href="/skill-hub/problem-solving-operations/data-reconciliation-working-skill/">Data Reconciliation</a></li>
    <li><a href="/skill-hub/problem-solving-operations/cutover-hypercare-control-working-skill/">Cutover &amp; Hypercare Control</a></li>
    <li><a href="/skill-hub/problem-solving-operations/batch-queue-troubleshooting-working-skill/">Batch &amp; Queue Troubleshooting</a></li>
  </ul>
</section>
