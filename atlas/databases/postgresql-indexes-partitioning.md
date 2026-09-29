---
layout: default
title: "PostgreSQL Indexes and Partitioning — Design from Query Shape"
description: "A practical PostgreSQL guide to B-tree, GIN, GiST, BRIN, partial and expression indexes, plus partitioning decisions based on query shape, selectivity, and data lifecycle."
permalink: /atlas/databases/postgresql-indexes-partitioning/
last_modified_at: 2026-09-29
atlas_section: databases
domain: Data platforms
subdomain: PostgreSQL
concept_type: access path guide
status: needs_verification
verified: false
level: 1
author: Dzmitryi Kharlanau
robots: noindex,follow
sitemap: false
tags:
  - postgresql
  - indexes
  - partitioning
  - btree
  - gin
  - brin
related:
  - /atlas/databases/
  - /atlas/databases/postgresql-query-patterns/
  - /atlas/databases/postgresql-data-modeling/
  - /atlas/databases/postgresql-mvcc-performance/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/databases/">Databases</a></li>
    <li aria-current="page">PostgreSQL Indexes and Partitioning</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">PostgreSQL / Access Paths</p>
    <h1>An index is a contract with a query pattern.</h1>
    <p class="note-subtitle">The goal is not to “have indexes.” The goal is to give the planner a cheap path to the rows the workload actually asks for.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <div class="note-body">
    <h2>Start with the query, not the index menu</h2>
    <p>Every index has two costs: it occupies storage and it must be maintained when data changes. The benefit is narrower: it helps only query patterns that match its access method, indexed values, operator classes, ordering, and selectivity. That is why “add an index” can be correct and still be a poor design.</p>
    <p>Before creating one, write down the actual predicate, expected result size, ordering requirement, update rate, and data growth. Then choose the smallest structure that supports that shape.</p>

    <h2>B-tree: the default for ordered comparisons</h2>
    <p>B-tree is PostgreSQL's default index type and is effective for equality, ranges, and ordered retrieval. It is a strong fit for primary keys, timestamps queried by range, business codes, and sortable scalar values.</p>
    <p>But a B-tree is not a general search engine. A leading wildcard such as <code>LIKE '%hydrogen%'</code> cannot use the same ordinary prefix ordering that makes <code>LIKE 'hydrogen%'</code> efficient. Full-text search, arrays, document containment, spatial relationships, and very large naturally ordered tables may call for other access methods.</p>

    <h2>GIN, GiST, SP-GiST, and BRIN solve different problems</h2>
    <table>
      <thead><tr><th>Index family</th><th>Good fit</th><th>Question to ask first</th></tr></thead>
      <tbody>
        <tr><td>B-tree</td><td>Equality, range, ordering, prefix-compatible patterns.</td><td>Can the values be usefully ordered, and is the predicate selective enough?</td></tr>
        <tr><td>GIN</td><td>Composite values such as arrays, JSONB keys/containment, and full-text vectors.</td><td>Are queries looking for components inside a value?</td></tr>
        <tr><td>GiST</td><td>Extensible search strategies, ranges, geometry, nearest-neighbor patterns.</td><td>Does the operator class match the relationship being queried?</td></tr>
        <tr><td>SP-GiST</td><td>Partitioned search spaces such as tries, quadtrees, and selected geometric/text patterns.</td><td>Does the data structure benefit from a non-balanced partitioning strategy?</td></tr>
        <tr><td>BRIN</td><td>Huge tables where indexed values correlate with physical row order, commonly append-heavy time data.</td><td>Can compact block summaries eliminate most of the table?</td></tr>
      </tbody>
    </table>
    <p>Choosing among them is a workload decision. “GIN is faster” or “BRIN is smaller” is incomplete without the operator, data distribution, write rate, and acceptable false-positive rechecks.</p>

    <h2>Partial indexes: index the active slice when the workload is asymmetric</h2>
    <p>One of the book's clearest examples uses a support-ticket table with roughly 500,000 rows but only 250 open tickets. A normal index on status improved the query, but indexed the huge closed-ticket majority that the application did not care about. A partial index restricted to open tickets was dramatically smaller in that demonstration—about 16 KB instead of roughly 3.4 MB—and the measured count query dropped from about 3.7 ms to 0.8 ms.</p>
    <p>Those numbers belong to that synthetic workload, not to every database. The transferable lesson is stronger than the benchmark: when a stable predicate defines the small operational subset you query repeatedly, a partial index can align storage with the business state you actually use.</p>
<pre><code class="language-sql">CREATE INDEX tickets_open_idx
ON support.tickets (status)
WHERE status = 10;</code></pre>
    <p>Partial indexes are especially interesting for active rows, unprocessed events, non-deleted records, or a small status subset. They are less useful when the predicate changes frequently or the workload also needs the excluded rows through the same path.</p>

    <h2>Expression indexes: index the operation you really query</h2>
    <p>If every lookup normalizes a value the same way, an expression index can make that transformed access path explicit. The query expression must match what was indexed closely enough for the planner to use it.</p>
<pre><code class="language-sql">CREATE INDEX users_lower_email_idx
ON users (lower(email));</code></pre>
    <p>Do not use expression indexes to hide a confused domain model. First ask whether the transformed value should be stored or constrained differently.</p>

    <h2>Covering and index-only plans: projection matters</h2>
    <p>When all required data can be satisfied from an index and visibility information permits it, PostgreSQL may use an index-only scan. Asking for extra columns can force heap access and remove that benefit. This is another reason to avoid selecting data the caller will discard.</p>
    <p><code>INCLUDE</code> columns can support covering indexes without making every included column part of the search key, but they still increase index size and write cost.</p>

    <h2>More indexes can make a write-heavy system slower</h2>
    <p>Each INSERT, DELETE, and many UPDATE operations must maintain relevant indexes. Too many indexes can increase WAL, random I/O, vacuum work, storage, and checkpoint pressure. Before adding another one, ask whether an existing index can support the query and whether the query itself can be simplified.</p>
    <p>Before removing an apparently unused index, check the observation window and topology. Usage statistics are local to a server instance; another physical replica can have a different read workload.</p>

    <h2>Partitioning is primarily a data-lifecycle and pruning tool</h2>
    <p>Partitioning splits one logical table into separately managed physical tables. It can improve operations in two important ways:</p>
    <ul>
      <li><strong>Pruning:</strong> when a query constrains the partition key, PostgreSQL can avoid partitions that cannot contain matching rows.</li>
      <li><strong>Lifecycle operations:</strong> old data can be detached or dropped by partition instead of deleting millions of rows one by one.</li>
    </ul>
    <p>This is why time-based partitioning works well for some event, audit, payment, and telemetry workloads: queries and retention often use the same time dimension.</p>

    <h2>Partitioning does not rescue a bad access pattern</h2>
    <p>If a query does not constrain the partition key, the planner may have to visit many partitions. Too many tiny partitions increase planning and management overhead. A poor partition key can scatter related data and create more work than the original table.</p>
    <p>Do not partition just because a table is “large.” Partition when the key aligns with query elimination, retention, maintenance, physical placement, or a known scale boundary.</p>

    <h2>Multi-column partitioning is not subpartitioning</h2>
    <p>The book highlights an easy conceptual trap: a multi-column range boundary is lexicographic over the combined key. It does not automatically mean “partition first by month, then independently by branch.” If that hierarchy is the requirement, use subpartitioning: create time partitions, then partition each relevant time partition by the second dimension.</p>

    <h2>Access-path review protocol</h2>
    <ol>
      <li>Capture the exact slow or high-volume query shape.</li>
      <li>Measure current plan, rows, buffers, latency, and call frequency.</li>
      <li>Estimate selectivity and data growth, not only today's table size.</li>
      <li>Choose the access method that matches the operators.</li>
      <li>Estimate index size and write amplification.</li>
      <li>For partitioning, prove pruning with representative predicates and prove lifecycle benefit with realistic retention operations.</li>
      <li>Re-run the workload, not just one query, because a locally faster read can make the overall system worse.</li>
    </ol>

    <h2>Sources</h2>
    <ul>
      <li>Jimmy Angelakos, <em>PostgreSQL Mistakes and How to Avoid Them</em>, chapters 1, 4, and 6.</li>
      <li><a href="https://www.postgresql.org/docs/18/indexes-types.html">PostgreSQL: Index Types</a></li>
      <li><a href="https://www.postgresql.org/docs/18/indexes-partial.html">PostgreSQL: Partial Indexes</a></li>
      <li><a href="https://www.postgresql.org/docs/18/indexes-expressional.html">PostgreSQL: Indexes on Expressions</a></li>
      <li><a href="https://www.postgresql.org/docs/18/ddl-partitioning.html">PostgreSQL: Table Partitioning</a></li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Continue</h2>
    <ul>
      <li><a href="/atlas/databases/postgresql-query-patterns/">Query patterns</a></li>
      <li><a href="/atlas/databases/postgresql-mvcc-performance/">MVCC, vacuum, and concurrency</a></li>
      <li><a href="/atlas/databases/postgresql-troubled-database-playbook/">Troubled database playbook</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
