---
layout: default
title: "Value Stream Mapping — Practical End-to-End Flow Method"
description: "Use Value Stream Mapping to see end-to-end lead time, processing time, queues, handoffs, and information flow before optimizing local process steps."
permalink: /skill-hub/methods-catalog/value-stream-mapping/
last_modified_at: 2026-09-27
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/methods-catalog/">Methods &amp; Frameworks</a></li>
    <li aria-current="page">Value Stream Mapping</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Methods Catalog — Flow Improvement</p>
  <h1>Value Stream Mapping</h1>
  <p class="lead">Use Value Stream Mapping when the problem is not one broken step but the total time and effort required to move value from request to customer outcome.</p>

  <section>
    <h2>What this method is for</h2>
    <p>Value Stream Mapping (VSM) looks at the whole flow, including value-creating and non-value-creating work, material or case flow, and information flow. A current-state map shows how work really moves now. A future-state map describes a better flow.</p>
    <p>For digital and SAP work, “inventory” can be physical stock, but it can also be orders waiting for release, invoices waiting for correction, tickets waiting in queues, or change requests waiting for approval.</p>
  </section>

  <section>
    <h2>When to use it</h2>
    <ul>
      <li>End-to-end lead time is long but each local team reports acceptable processing time.</li>
      <li>Work spends more time waiting than being processed.</li>
      <li>There are repeated handoffs, rework loops, queues, batches, or approvals.</li>
      <li>A transformation wants to improve the whole flow rather than automate one step.</li>
      <li>Teams argue about where the real bottleneck is.</li>
    </ul>
  </section>

  <section>
    <h2>Metrics worth capturing</h2>
    <div class="table-scroll">
      <table class="study-table">
        <thead><tr><th>Metric</th><th>Meaning</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>Process time</td><td>Time actively spent working on an item</td><td>6 min to correct order data</td></tr>
          <tr><td>Wait time</td><td>Time between active steps</td><td>14 h waiting for credit review</td></tr>
          <tr><td>Lead time</td><td>Total elapsed time through the value stream</td><td>2.4 days order request to release</td></tr>
          <tr><td>Queue / WIP</td><td>Items waiting or being processed</td><td>340 blocked orders</td></tr>
          <tr><td>First-pass quality</td><td>Items completed without rework</td><td>82% orders complete first time</td></tr>
          <tr><td>Batch frequency</td><td>How often work is moved or processed</td><td>Interface file every 4 hours</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Choose one value stream and one item type.</strong> Do not mix sales orders, returns, and service cases in one map unless they truly share the same flow.</li>
      <li><strong>Define customer value and the end condition.</strong> “Order created” may not be value if fulfillment still cannot start.</li>
      <li><strong>Walk the actual flow.</strong> Use system evidence, queue data, interviews, and real cases.</li>
      <li><strong>Map processing steps and information signals.</strong> Include what tells a team or system to act.</li>
      <li><strong>Measure active time and waiting separately.</strong> Do not estimate only total SLA.</li>
      <li><strong>Mark queues, rework, batches, approvals, and defect loops.</strong></li>
      <li><strong>Find the constraint and major delay sources.</strong> Avoid optimizing a fast step while the item waits elsewhere for hours.</li>
      <li><strong>Design a future state.</strong> Remove unnecessary waits, reduce batch size, improve first-pass quality, move validation upstream, or change flow ownership.</li>
      <li><strong>Create an improvement backlog with measures.</strong> Every improvement should state which flow metric it should change.</li>
    </ol>
  </section>

  <section>
    <h2>SAP example — invoice release</h2>
    <p>An invoice may require 7 minutes of actual processing but wait 36 hours for missing goods-receipt evidence and another 10 hours for approval. Automating the 7-minute posting step does little. The value-stream view points to upstream data completeness, approval queues, and batch timing as the dominant sources of delay.</p>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If wait time dominates process time, optimize queue, policy, batch, or dependency behavior before automating keystrokes.</li>
      <li>If defects return work upstream, measure rework as part of the stream rather than hiding it inside one team.</li>
      <li>If a local improvement increases downstream queue size, it is not an end-to-end improvement.</li>
      <li>If data is missing at a late step, look for an earlier validation point.</li>
      <li>If routing logic is the main problem, use <a href="/skill-hub/methods-catalog/bpmn/">BPMN</a> for detailed process logic.</li>
    </ul>
  </section>

  <section>
    <h2>Copy-ready template</h2>
    <pre><code>## Value stream
&lt;Item / request from trigger to customer outcome&gt;

## Customer outcome
&lt;What value means and when it is achieved&gt;

| Step | Owner/System | Process Time | Wait Time | Queue/WIP | First-pass quality | Information trigger | Rework reason |
|---|---|---:|---:|---:|---:|---|---|
| 1 | ... | ... | ... | ... | ... | ... | ... |

## Current state
- Total lead time:
- Total active process time:
- Main wait:
- Main rework loop:
- Main batch:
- Main constraint:

## Future-state moves
1. &lt;change&gt; → target metric:
2. &lt;change&gt; → target metric:

## Validation
- Baseline source:
- Review date:
- Expected business outcome:</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The map follows one item from trigger to customer outcome.</li>
      <li>Active work and waiting are measured separately.</li>
      <li>Information flow is visible, not only process steps.</li>
      <li>Queues and rework loops are explicit.</li>
      <li>Future-state changes target measured delay or quality problems.</li>
      <li>The team avoids local optimization that harms the whole flow.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Drawing a process map and calling it VSM.</strong> Without time, queues, quality, and information flow, the key analysis is missing.</li>
      <li><strong>Using workshop estimates when system data exists.</strong> Use timestamps, backlog counts, and monitoring evidence where possible.</li>
      <li><strong>Automating before understanding waiting.</strong> Processing time may be a small fraction of lead time.</li>
      <li><strong>Mapping too much.</strong> Choose a value stream and item family narrow enough to measure.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>An AI agent should calculate or preserve separate process and wait times, cite the source of each metric, label estimates as estimates, and rank delay sources by evidence. It should not recommend automation only because a step is manual.</p>
  </section>

  <section>
    <h2>Related skills and methods</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis</a></li>
      <li><a href="/skill-hub/methods-catalog/bpmn/">BPMN</a></li>
      <li><a href="/skill-hub/methods-catalog/sipoc/">SIPOC</a></li>
      <li><a href="/skill-hub/business-analysis/gap-analysis-working-skill/">Gap Analysis</a></li>
      <li><a href="/skill-hub/problem-solving-operations/process-deviation-analysis-working-skill/">Process Deviation Analysis</a></li>
    </ul>
  </section>

  <section>
    <h2>Reference and limitations</h2>
    <p>The <a href="https://www.lean.org/lexicon-terms/value-stream-mapping/">Lean Enterprise Institute</a> describes VSM as mapping the material and information flow required to bring a product from order to delivery, normally using current and future states. This page extends the same end-to-end logic to enterprise service and SAP flows.</p>
  </section>
</article>