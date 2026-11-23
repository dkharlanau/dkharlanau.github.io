---
layout: default
author: "Dzmitryi Kharlanau"
title: "Amazon S3 and dbt, Explained: From Raw Files to Trusted Analytics"
description: "Learn what S3, Athena, Glue, and dbt each do. Follow a synthetic SAP-style order example, read a small dbt model, and learn how to test the numbers."
permalink: /atlas/concepts/s3-dbt-analytics-explained/
last_modified_at: 2026-11-22
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
tags:
  - data-engineering
  - analytics
  - aws
  - amazon-s3
  - dbt
  - data-quality
  - sap
related:
  - /skill-hub/dama-dmbok/s3-dbt-analytics-working-skill/
  - /atlas/concepts/data-lineage/
  - /atlas/concepts/data-contracts/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/concepts/">Concepts</a></li>
    <li aria-current="page">S3 and dbt for analytics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Data engineering / understand the system</p>
  <h1>Amazon S3 and dbt: from raw files to a number you can defend</h1>
  <p class="lead">Five rows arrive from an ERP export. A dashboard shows five orders. But there are only three. Where did the extra two come from — and which tool should fix the problem?</p>

  <p><strong>After this guide, you can:</strong> explain what S3 and dbt do (and do not do), trace a simple analytical pipeline, read its SQL model, and ask the right questions when the report looks wrong.</p>

  <h2>1. The mental model: storage is not analytics</h2>
  <p>Imagine a library. <strong>Amazon S3</strong> is the storage room: it keeps files as objects in buckets. <strong>AWS Glue Data Catalog</strong> is the catalogue: it describes what tables and columns exist. <strong>Amazon Athena</strong> is the reader: it runs SQL against data, including files stored in S3. <strong>dbt</strong> is the method for organising transformations, dependencies, tests, and documentation. dbt sends work to a supported data engine; it does not execute SQL inside S3.</p>

  <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Roles of Amazon S3, Glue, Athena, and dbt">
    <table class="study-table__table">
      <thead><tr><th scope="col">Part</th><th scope="col">Job</th><th scope="col">Not its job</th></tr></thead>
      <tbody>
        <tr><th scope="row">S3</th><td>Store raw and curated objects; manage access and retention.</td><td>Understand what an order or a revenue measure means.</td></tr>
        <tr><th scope="row">Glue Data Catalog</th><td>Register the table schema and location.</td><td>Fix incorrect business rules.</td></tr>
        <tr><th scope="row">Athena</th><td>Read and transform S3-backed data using SQL.</td><td>Decide the right business definition by itself.</td></tr>
        <tr><th scope="row">dbt</th><td>Manage SQL models, dependencies, data tests, and descriptions.</td><td>Extract data from SAP or provide its own compute engine.</td></tr>
        <tr><th scope="row">Dashboard</th><td>Show a business result.</td><td>Prove that upstream rows were deduplicated correctly.</td></tr>
      </tbody>
    </table>
  </div>

  <p><mark class="key-idea">Remember: Store → Describe → Query → Model → Test → Explain.</mark> Different responsibilities make failures easier to locate.</p>

  <h2>2. Follow one order through the pipeline</h2>
  <p><strong>Synthetic example:</strong> a daily export from an ERP-like order system lands in <code>s3://example-analytics/raw/orders_events/</code>. The statuses and fields below are invented for teaching; they are not standard SAP table or status codes.</p>

  <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Synthetic order status events">
    <table class="study-table__table">
      <thead><tr><th scope="col">Order</th><th scope="col">Updated</th><th scope="col">Event #</th><th scope="col">Status</th><th scope="col">Amount</th></tr></thead>
      <tbody>
        <tr><th scope="row">101</th><td>Nov 19, 08:00</td><td>1</td><td>open</td><td>120</td></tr>
        <tr><th scope="row">101</th><td>Nov 20, 09:00</td><td>2</td><td>shipped</td><td>120</td></tr>
        <tr><th scope="row">102</th><td>Nov 20, 08:10</td><td>1</td><td>cancelled</td><td>80</td></tr>
        <tr><th scope="row">103</th><td>Nov 20, 12:00</td><td>1</td><td>shipped</td><td>50</td></tr>
        <tr><th scope="row">103</th><td>Nov 21, 08:00</td><td>2</td><td>shipped</td><td>50</td></tr>
      </tbody>
    </table>
  </div>

  <p>The <code>event_seq</code> column (“Event #”) is a fictional source sequence that increases within each order. It breaks equal-timestamp ties; a real source must provide an authoritative ordering key, not an invented one.</p>

  <p>Five rows are <em>events</em>, not five different orders. There are three distinct order IDs. To answer “What is the current value of shipped orders?”, first keep the latest event for each order. The answer for this miniature dataset is <strong>170</strong> (120 + 50), not 220 or 340. This is <strong>shipped order value</strong>, not recognised revenue or payment received.</p>

  <p>The difficult concept here is <strong>grain</strong>: what does one row represent? Raw grain is “one event”. The reporting grain is “one latest order state”. Mixing them creates false totals even when SQL executes successfully.</p>
  <p><strong>The SAP connection:</strong> one customer can have several sales areas or partner assignments. If you join an order to every matching master-data row using only the customer ID, the order amount may multiply. Check the business key and join cardinality before blaming the dashboard.</p>

  <h2>3. Where the work actually happens</h2>

  <pre><code>ERP export / approved source
  |
  v
Amazon S3 / raw files             -- objects + retention + access
  |
  v
AWS Glue Data Catalog             -- schema and S3 location
  |
  v
Amazon Athena                     -- SQL reads and writes S3-backed data
  ^         |
  |         v
dbt models + tests  --------> curated analytical tables
                               |
                               v
                          BI / reporting
</code></pre>

  <p>dbt tells Athena which SQL models to build and in what dependency order. Athena performs the computation. Depending on materialisation and configuration, results can become tables or views; the physical storage of an Athena table may remain in S3. The pipeline still needs a separate, reliable extraction or ingestion step before dbt starts.</p>

  <h2>4. See the SQL without getting lost in tooling</h2>
  <p>In a dbt project, a <em>source</em> describes data already available in your data platform. The example below assumes an Athena-accessible table named <code>raw.orders_events</code>, with typed <code>updated_at</code>, <code>amount</code>, and <code>event_seq</code> columns. Creating and loading this source is a separate step.</p>

  <p><strong>models/sources.yml</strong> — tell dbt where the raw data lives:</p>
<pre><code class="language-yaml">version: 2

sources:
  - name: erp
    schema: raw
    tables:
      - name: orders_events
</code></pre>

  <p><strong>models/int_latest_order.sql</strong> — one current row per order:</p>
<pre><code class="language-sql">with ranked as (
    select
        order_id,
        status,
        amount,
        updated_at,
        event_seq,
        row_number() over (
            partition by order_id
            order by updated_at desc, event_seq desc
        ) as row_num
    from &#123;&#123; source('erp', 'orders_events') &#125;&#125;
)

select order_id, status, amount, updated_at, event_seq
from ranked
where row_num = 1
</code></pre>

  <p><strong>models/fct_shipped_order_value.sql</strong> — build a clearly named metric:</p>
<pre><code class="language-sql">select
    count(*) as shipped_orders,
    coalesce(sum(amount), 0) as shipped_order_value
from &#123;&#123; ref('int_latest_order') &#125;&#125;
where status = 'shipped'
</code></pre>

  <p><strong>Time boundary:</strong> the base model uses the latest state from all available events. To reproduce a report as of 2026-11-21 23:59:59, add <code>where updated_at &lt;= timestamp '2026-11-21 23:59:59'</code> inside the <code>ranked</code> CTE, <em>before</em> applying <code>row_number()</code>. Define a time zone and verify that the source extract is complete through the cutoff. Filtering after the window would incorrectly omit earlier valid states whenever a later correction exists.</p>

  <p>The <code>source()</code> call marks the upstream input. The <code>ref()</code> call marks a dependency on another dbt model. A dbt model is primarily a SQL <code>select</code> statement; the configured materialisation determines how the data platform creates its output.</p>

  <p><strong>models/properties.yml</strong> — record a minimum guarantee about the current-order model:</p>
<pre><code class="language-yaml">version: 2

models:
  - name: int_latest_order
    description: "One latest event per order in the synthetic example."
    columns:
      - name: order_id
        data_tests:
          - not_null
          - unique
      - name: status
        data_tests:
          - not_null
          - accepted_values:
              arguments:
                values: ['open', 'shipped', 'cancelled']
      - name: amount
        data_tests:
          - not_null
      - name: updated_at
        data_tests:
          - not_null
      - name: event_seq
        data_tests:
          - not_null
</code></pre>

  <p><code>accepted_values.arguments</code> requires a compatible dbt release (dbt Core 1.10.5 or newer); older releases use legacy test-argument syntax. These checks do not prove source completeness or reconcile a business metric.</p>

  <p>Then use the appropriate installed dbt CLI and adapter:</p>
<pre><code class="language-bash">dbt build --select +fct_shipped_order_value
</code></pre>

  <p>This builds the selected model and its upstream dependencies and runs relevant tests. The snippets illustrate the modelling pattern; they are <strong>not a complete deployable Athena project</strong>. Connection profiles, IAM, S3 query-result location, source table creation, adapter/version compatibility, and environment configuration must be supplied for the target account. See the dbt Athena adapter documentation below.</p>

  <h2>5. Three decisions that matter more than the commands</h2>
  <ol>
    <li><strong>Choose the grain.</strong> Do users need events, latest order state, or one row per order item? Write that down before aggregating.</li>
    <li><strong>Choose the source of truth.</strong> Is the extract complete? Do late events arrive? Can records be corrected or deleted? The synthetic example uses source-provided <code>event_seq</code> to break equal-timestamp ties. If a production source lacks a trusted sequence or ingestion ID, detect and reject ambiguous ties instead of silently reporting an arbitrary latest state.</li>
    <li><strong>Choose the business meaning.</strong> Shipped order value is not revenue. Net values may depend on cancellations, returns, currency, taxes, and business rules. A passing technical test cannot approve a metric definition.</li>
  </ol>

  <h2>6. What usually breaks in production</h2>
  <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Analytics pipeline failures and checks">
    <table class="study-table__table">
      <thead><tr><th scope="col">Symptom</th><th scope="col">Likely layer</th><th scope="col">First evidence to check</th></tr></thead>
      <tbody>
        <tr><th scope="row">Yesterday's data is missing</th><td>Ingestion / S3</td><td>Arrival time, object prefix, source export status, and job logs.</td></tr>
        <tr><th scope="row">SQL cannot read a field</th><td>Catalog / schema</td><td>Actual file layout, column types, partitions, and Glue metadata.</td></tr>
        <tr><th scope="row">Order value is doubled</th><td>Model grain / joins</td><td>Row counts and duplicate business keys before and after each model.</td></tr>
        <tr><th scope="row">Tests pass; KPI is still wrong</th><td>Business semantics</td><td>Approved metric definition, statuses, currencies, exclusions, and reconciliation.</td></tr>
        <tr><th scope="row">Queries are expensive</th><td>Data layout / compute</td><td>Bytes scanned, file format, partition filtering, and unnecessary full refreshes.</td></tr>
      </tbody>
    </table>
  </div>

  <p>For large analytical datasets, columnar formats such as Parquet and sensible partitioning can reduce scanned data. They are design choices, not automatic improvements for every tiny input. dbt incremental models may help with scale but introduce state, late-arrival, and correction complexity: start with a correct full build before optimising.</p>

  <h2>7. When this stack is a good fit — and when it is not</h2>
  <p><strong>S3 + Athena + dbt</strong> is worth evaluating when you already have files in AWS, need SQL analysis without operating a large warehouse cluster, and want version-controlled transformations with tests. A dedicated warehouse such as Redshift or another dbt-supported data platform may fit better when query patterns, concurrency, interactive latency, and team needs demand it. dbt also works with many platforms other than Athena.</p>

  <p>Do <strong>not</strong> use this pattern as a replacement for transactional ERP processing, an operational API, or real-time decisions that require strict latency. Do not export confidential SAP customer or employee records into a personal learning bucket. In enterprise work, start with approved extraction, data minimisation, access controls, encryption, retention, residency, and cost ownership. In AWS, keep public access blocked unless a deliberate, reviewed exception exists.</p>

  <h2>8. Test your understanding</h2>
  <ol>
    <li><strong>An order changes status twice. Which table would you use for historical changes?</strong> The raw event history, not the latest-state model.</li>
    <li><strong>A dbt test says order IDs are unique, but totals are wrong. What next?</strong> Check the business definition, joins, currency, cancellations, and source-to-target reconciliation.</li>
    <li><strong>A new file lands in S3, but Athena cannot see it. What next?</strong> Inspect the registered table's S3 location, partitions, schema and permissions before changing the dbt SQL.</li>
  </ol>

  <h2>9. Related practice</h2>
  <p><strong>Try it:</strong> use the companion <a href="/skill-hub/dama-dmbok/s3-dbt-analytics-working-skill/">S3 + dbt Analytics Working Skill</a> to design the same pipeline, perform the checks, and explain one failure to a business stakeholder.</p>

  <h2>Source references and version boundary</h2>
  <ul>
    <li><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html">AWS: What is Amazon S3?</a> — object storage and access model.</li>
    <li><a href="https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html">AWS: Athena with Glue Data Catalog</a> — queryable metadata and registered tables.</li>
    <li><a href="https://docs.aws.amazon.com/athena/latest/ug/serde-csv-choices.html">AWS: CSV SerDe choices</a> — reading timestamps from the sample.</li>
    <li><a href="https://docs.getdbt.com/docs/introduction">dbt: What is dbt?</a> — models, dependencies and supported engines.</li>
    <li><a href="https://docs.getdbt.com/docs/build/sources">dbt: Sources</a> — model lineage and upstream tables.</li>
    <li><a href="https://docs.getdbt.com/docs/build/data-tests">dbt: Data tests</a> — assertions and test behaviour.</li>
    <li><a href="https://docs.getdbt.com/docs/local/connect-data-platform/athena-setup">dbt: Athena adapter setup</a> — current adapter and connection details.</li>
    <li><a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html">AWS: S3 Block Public Access</a> — storage security.</li>
  </ul>

  <p><strong>Review boundary:</strong> educational synthesis based on official documentation checked in November 2026. The sample is fictional; no cloud execution, external system test, security review or business metric sign-off is claimed. Product, adapter, and version behaviour should be verified in the intended environment before implementation.</p>
</article>
