---
layout: default
author: "Dzmitryi Kharlanau"
title: "S3 + dbt Analytics Working Skill — Design, Test, Explain"
description: "A practical 45-minute exercise for designing a small AWS analytics pipeline, defining data grain, writing dbt checks, and diagnosing wrong totals."
permalink: /skill-hub/dama-dmbok/s3-dbt-analytics-working-skill/
last_modified_at: 2026-11-22
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
tags:
  - data-engineering
  - analytics
  - aws
  - dbt
  - data-quality
related:
  - /atlas/concepts/s3-dbt-analytics-explained/
  - /skill-hub/dama-dmbok/data-lineage-working-skill/
  - /skill-hub/dama-dmbok/data-quality-root-cause-working-skill/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/dama-dmbok/">Data &amp; DAMA</a></li>
    <li aria-current="page">S3 + dbt analytics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Working skill / 45-minute tabletop lab</p>
  <h1>Turn a file in S3 into a trustworthy analytical answer</h1>
  <p class="lead">You are asked to build a report from daily order extracts. The file exists; the first total is wrong. Instead of adding another filter, design the data flow and prove what each row means.</p>

  <p><strong>The outcome:</strong> one small architecture, one declared data grain, one model dependency, a test checklist, and an explanation a non-technical stakeholder can understand. The exercise uses synthetic data; it does not require AWS credentials.</p>

  <h2>When to use this skill</h2>
  <ul>
    <li>An ERP, CRM or operational system exports files for analytics.</li>
    <li>Multiple reports disagree because of duplicates, status history, or different business definitions.</li>
    <li>You need to choose whether S3 + Athena + dbt is a sensible first architecture.</li>
    <li>You want a code-reviewable transformation with evidence of data quality.</li>
  </ul>

  <h2>Inputs to prepare</h2>
  <ul>
    <li>The business question — for example, “What was the current shipped order value at the end of the day?”</li>
    <li>Example source columns: <code>order_id</code>, <code>status</code>, <code>updated_at</code>, <code>amount</code>, and <code>event_seq</code> (stable per-order sequence).</li>
    <li>Definition of one raw row, the update sequence, source owner, and expected refresh frequency.</li>
    <li>For a real implementation only: approved AWS account, region, S3/IAM access, Glue/Athena configuration, dbt adapter, and budget.</li>
  </ul>

  <h2>Exercise: 45 minutes, five decisions</h2>
  <ol>
    <li><strong>Minutes 0–8 — Write the decision.</strong> What should the report say? Define <em>shipped order value</em>, the reporting cut-off, currency, and the meaning of “current”. Do not call this revenue.</li>
    <li><strong>Minutes 8–15 — Draw the boundary.</strong> Sketch <code>Source → S3 → Glue Catalog → Athena ↔ dbt → curated model → dashboard</code>. Assign an owner to extraction, storage, query execution, SQL logic, and metric sign-off. Explain why dbt does not extract from SAP.</li>
    <li><strong>Minutes 15–25 — Set the grain.</strong> Use the five event rows in the <a href="/atlas/concepts/s3-dbt-analytics-explained/">companion example</a>. Distinguish “one event per update” from “one latest state per order”. The correct sample result is two shipped orders, value <strong>170</strong>.</li>
    <li><strong>Minutes 25–35 — Add checks.</strong> Declare the source in dbt. Make a latest-order model using <code>row_number()</code> ordered by timestamp and source sequence. Add <code>not_null</code> and <code>unique</code> tests on its <code>order_id</code>, plus status, timestamp, amount, and sequence checks. Include a source-vs-model count reconciliation. Record which business assumptions tests cannot prove.</li>
    <li><strong>Minutes 35–45 — Challenge the design.</strong> A late-arriving correction changes order 101 from shipped to cancelled. What changes in the metric? How would you detect the correction and rebuild affected results? Explain the change without using SQL jargon.</li>
  </ol>

  <h2>Deliverables: the four-line design card</h2>
  <pre><code>BUSINESS QUESTION: Current shipped order value, as of a defined cut-off
RAW GRAIN:         One row per order status event (stable event_seq)
CURATED GRAIN:     One latest state per order (timestamp + event_seq)
EVIDENCE:          Source completeness + key tests + metric reconciliation
</code></pre>

  <p>Then produce a one-page <strong>data flow</strong> with owners, storage locations, table schemas, a dbt model dependency, and the exact conditions that make the answer correct. This is more useful than a diagram with twenty tool logos.</p>

  <h2>The basic test set</h2>
  <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Data quality tests for the synthetic order pipeline">
    <table class="study-table__table">
      <thead><tr><th scope="col">Check</th><th scope="col">Where</th><th scope="col">What it catches</th></tr></thead>
      <tbody>
        <tr><th scope="row">Non-null order ID</th><td>Raw and current-state model</td><td>Rows that cannot be assigned to an order.</td></tr>
        <tr><th scope="row">Unique order ID</th><td>Current-state model only</td><td>Duplicate business keys after choosing the latest state.</td></tr>
        <tr><th scope="row">Allowed status values</th><td>Raw or staging</td><td>Unexpected status codes; do not silently drop them.</td></tr>
        <tr><th scope="row">Source completeness</th><td>Landing/extraction control</td><td>Missing expected batches, files, or date ranges.</td></tr>
        <tr><th scope="row">Reconciliation</th><td>Before and after transformation</td><td>Unexpected changes in counts and sums; distinguish valid exclusions from defects.</td></tr>
        <tr><th scope="row">Business sign-off</th><td>Metric definition</td><td>A technically correct query that answers the wrong question.</td></tr>
      </tbody>
    </table>
  </div>

  <p><strong>Important:</strong> a <code>unique</code> test on the raw event table would be wrong if multiple legitimate events can share one order ID. Test the declared grain, not your wish that every table have unique order IDs.</p>

  <h2>Copy a safe five-row sample</h2>
  <p>Save this as <code>orders_events.csv</code>. All values are fabricated. The <code>event_seq</code> value increases within each order and breaks timestamp ties. In Athena, register <code>order_id</code> and <code>event_seq</code> as integers, <code>amount</code> as decimal, and <code>updated_at</code> as timestamp. These timestamps have no offset: choose a business time zone for the lab.</p>
  <pre><code>order_id,status,updated_at,amount,event_seq
101,open,2026-11-19 08:00:00,120,1
101,shipped,2026-11-20 09:00:00,120,2
102,cancelled,2026-11-20 08:10:00,80,1
103,shipped,2026-11-20 12:00:00,50,1
103,shipped,2026-11-21 08:00:00,50,2
</code></pre>
  <p>If the real source has no <code>event_seq</code>, use an authoritative event ID or change sequence instead; a tied timestamp without a stable key is ambiguous. For historical cutoffs, filter raw events <em>before</em> ranking them.</p>
  <p>Check your result against this expected output: <strong>three latest orders, two currently shipped, shipped order value 170</strong>. If you get three shipped rows and 220 instead, you counted events rather than latest orders.</p>

  <p><strong>Offline exercise (no AWS account):</strong> run <code>python3 -m unittest discover -s tests -p 'test_s3_dbt_learning_example.py' -v</code> at the repository root. It executes the two published SQL models on SQLite and checks 170, duplicate events, a late cancellation, equal timestamps, and empty shipped selections. It does not claim Athena execution or dbt adapter compatibility.</p>

  <h2>How to make this a real AWS lab</h2>
  <ol>
    <li>Start with an approved <strong>synthetic CSV</strong> and a private S3 bucket. Organise separate prefixes for <code>raw/</code>, <code>curated/</code>, and Athena query results. Set retention and cost limits.</li>
    <li>Register the raw file schema and S3 location in Glue Data Catalog. For this quote-free CSV with human-readable timestamps, use Athena's default LazySimpleSerDe, not OpenCSVSerDe (which requires epoch milliseconds for timestamp fields). Skip the header with <code>TBLPROPERTIES ("skip.header.line.count"="1")</code> and preserve the shown column order. Confirm Athena reads exactly five rows. See <a href="https://docs.aws.amazon.com/athena/latest/ug/serde-csv-choices.html">AWS guidance on CSV SerDe selection</a>.</li>
    <li>Install a compatible dbt version and <a href="https://docs.getdbt.com/docs/local/connect-data-platform/athena-setup">dbt Athena adapter</a>; configure access, region, workgroup and S3 result location following the current adapter documentation. Do not put secrets in Git.</li>
    <li>Implement the two SQL models from the <a href="/atlas/concepts/s3-dbt-analytics-explained/">explainer</a> and a YAML data test; run <code>dbt build</code> in the configured environment.</li>
    <li>Inspect the test results and the SQL generated by dbt. Compare the analytical result with the hand-calculated answer, then change one record and repeat.</li>
    <li>Clean up the training resources when finished; S3 storage, queries and catalog-related features can incur charges.</li>
  </ol>

  <h2>Decision rules for an architect</h2>
  <ul>
    <li><strong>If the problem is moving data from SAP:</strong> design approved extraction/ingestion separately; dbt is primarily the transformation layer.</li>
    <li><strong>If the problem is SQL against files:</strong> S3 alone is insufficient; evaluate an engine such as Athena and a suitable catalog.</li>
    <li><strong>If the problem is inconsistent KPIs:</strong> start with grain, definitions and reconciliation before tuning compute.</li>
    <li><strong>If a full rebuild is correct but too slow:</strong> investigate incremental models, and plan for late data, corrections, idempotency and backfills.</li>
    <li><strong>If the system needs sub-second operational writes:</strong> do not use an analytics pipeline as a transactional database.</li>
  </ul>

  <h2>Ask an AI agent for useful work, not a generic tutorial</h2>
  <pre><code>Review this SYNTHETIC analytics design:
Source: daily ERP-like order status events in S3.
Engine: Athena; catalog: Glue; transformation: dbt.
Business question: current shipped order value.

Return:
1. A one-row-per-order grain contract
2. Two SQL model outlines and their dependencies
3. Five data-quality or reconciliation checks
4. Three failure scenarios with discriminating evidence
5. The business decisions that still need human approval

Separate confirmed input facts from assumptions.
Do not invent real SAP field mappings, client data, or AWS credentials.
</code></pre>

  <h2>Quality check: can you defend the result?</h2>
  <ul>
    <li>I can explain S3, Athena, Glue, and dbt without calling them interchangeable services.</li>
    <li>I can show why five raw events produce three current orders and a shipped value of 170.</li>
    <li>I can identify the exact business key, event ordering rule, and late-correction behaviour.</li>
    <li>I can name one technical test and one business check that serve different purposes.</li>
    <li>I can explain the cost, access, extraction, and version assumptions before proposing AWS deployment.</li>
  </ul>

  <p><strong>Next:</strong> practice <a href="/skill-hub/dama-dmbok/data-lineage-working-skill/">Data Lineage</a> to trace source-to-report evidence, then <a href="/skill-hub/dama-dmbok/data-quality-root-cause-working-skill/">Data Quality Root Cause</a> to diagnose the first failed test.</p>

  <h2>Sources and scope</h2>
  <p>Based on <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html">AWS S3 documentation</a>, <a href="https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html">Athena/Glue documentation</a>, and official <a href="https://docs.getdbt.com/docs/introduction">dbt concepts</a>, <a href="https://docs.getdbt.com/docs/build/sources">sources</a>, and <a href="https://docs.getdbt.com/docs/build/data-tests">data tests</a>. This is an unverified teaching exercise, not a production deployment guide, audit opinion, or claim of a tested enterprise implementation.</p>
</article>
