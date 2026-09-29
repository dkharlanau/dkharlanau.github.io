---
layout: default
title: "PostgreSQL MVCC and Performance — Vacuum, Transactions, Connections, and Memory"
description: "A practical PostgreSQL performance guide built around MVCC: long transactions, autovacuum, XID pressure, connection concurrency, memory, locks, replica reads, and evidence-driven tuning."
permalink: /atlas/databases/postgresql-mvcc-performance/
last_modified_at: 2026-09-29
atlas_section: databases
domain: Data platforms
subdomain: PostgreSQL
concept_type: performance guide
status: needs_verification
verified: false
level: 1
author: Dzmitryi Kharlanau
robots: noindex,follow
sitemap: false
tags:
  - postgresql
  - mvcc
  - autovacuum
  - performance
  - concurrency
  - transactions
related:
  - /atlas/databases/
  - /atlas/databases/postgresql-mental-model/
  - /atlas/databases/postgresql-indexes-partitioning/
  - /atlas/databases/postgresql-production-reliability/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/databases/">Databases</a></li>
    <li aria-current="page">PostgreSQL MVCC and Performance</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">PostgreSQL / Performance</p>
    <h1>Performance debt accumulates while the database still looks healthy.</h1>
    <p class="note-subtitle">MVCC makes PostgreSQL highly concurrent, but it also creates maintenance obligations. Long transactions, excessive concurrency, and bad memory assumptions can turn those obligations into nonlinear failure.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <div class="note-body">
    <h2>Start with the MVCC consequence</h2>
    <p>PostgreSQL lets readers and writers proceed with limited blocking by keeping multiple row versions. That is the strength of MVCC. The cost is that obsolete versions cannot simply disappear the moment an UPDATE or DELETE happens. PostgreSQL must preserve versions that can still be visible to an older snapshot, then later make their space reusable.</p>
    <p>This creates a performance principle that is easy to miss: <strong>transaction lifetime changes storage behavior</strong>. A query can be fast by itself and still harm the system if it keeps an old snapshot alive for too long.</p>

    <h2>Idle is not always harmless</h2>
    <p>Separate three states:</p>
    <table>
      <thead><tr><th>State</th><th>What it means</th><th>Main risk</th></tr></thead>
      <tbody>
        <tr><td>Idle connection</td><td>A session is open but not currently running a transaction.</td><td>Process/memory overhead and excessive connection count.</td></tr>
        <tr><td>Idle in transaction</td><td>A transaction is open, but no statement is currently running.</td><td>Locks and old snapshots can remain held; cleanup can be delayed.</td></tr>
        <tr><td>Long active query</td><td>A statement is executing for a long time.</td><td>Old snapshot retention, resource consumption, replica conflicts, and delayed maintenance.</td></tr>
      </tbody>
    </table>
    <p>When an application has hundreds or thousands of sessions, first ask how many are truly doing useful work. Raw connection count is not workload throughput.</p>

    <h2>Autovacuum is part of the engine, not optional housekeeping</h2>
    <p>VACUUM makes space from dead row versions reusable and freezes old transaction IDs so the visibility system remains safe. ANALYZE refreshes statistics used by the planner. Autovacuum schedules this work continuously.</p>
    <p>Disabling or starving autovacuum can produce an attractive short-term benchmark because background work disappears. The debt remains: table and index bloat grows, planner statistics age, and anti-wraparound maintenance becomes increasingly urgent. A busy write-heavy table often needs <em>more</em> deliberate autovacuum capacity, not less.</p>
    <p>A useful tuning unit is the table, not only the server. A high-churn queue table and a mostly static reference table can need very different thresholds and cost settings.</p>

    <h2>XID pressure is a throughput problem with a clock attached</h2>
    <p>Traditional PostgreSQL transaction IDs are a finite 32-bit space used by MVCC visibility. PostgreSQL protects the system by freezing sufficiently old tuples before their transaction IDs become ambiguous after wraparound.</p>
    <p>At very high transaction rates, the system can consume XIDs faster than expected. One practical lever is batching: if business semantics allow 1,000 small writes to commit together, the application can reduce transaction overhead and XID consumption dramatically compared with 1,000 independent commits.</p>
    <p>The rule is not “batch everything.” The decision depends on the required atomicity, latency, retry behavior, and failure boundary.</p>

    <h2>Connections are concurrency, not free capacity</h2>
    <p>PostgreSQL uses a process-based connection model. More sessions mean more backend processes, more memory overhead, more scheduling, and more contention on shared structures. Raising <code>max_connections</code> does not create CPU cores or I/O bandwidth.</p>
    <p>Connection pooling separates application concurrency from database concurrency. A pooler such as PgBouncer can accept many client connections while allowing a much smaller number of active server connections. This is often useful when the application has bursts of waiting clients but only tens of queries can productively run at once.</p>
    <p>Do not choose the pool size from a generic formula alone. Measure throughput and latency while varying active concurrency. The useful point is where more parallel work stops increasing completed work and starts increasing queueing, waits, or tail latency.</p>

    <h2><code>work_mem</code> is not “memory per server”</h2>
    <p>A common tuning mistake is to multiply available RAM by a comfortable percentage and assign the result to <code>work_mem</code>. PostgreSQL can allocate work memory for multiple sort, hash, and related plan nodes, across many concurrent queries. Parallel plans can add more consumers.</p>
    <p>This creates two failure modes:</p>
    <ul>
      <li><strong>Too low:</strong> operations spill to temporary files and become I/O-bound.</li>
      <li><strong>Too high:</strong> concurrent queries can exhaust host memory and trigger severe swapping or the operating-system OOM killer.</li>
    </ul>
    <p>A safer approach is a conservative system default plus targeted session-level increases for known analytical operations, validated under realistic concurrency.</p>

    <h2>Do not tune shared buffers from folklore</h2>
    <p><code>shared_buffers</code> is important, but the “correct” value depends on workload, data working set, operating-system cache behavior, storage, and query mix. A value that helps an OLTP working set may add little to a scan-heavy analytical workload.</p>
    <p>Use rules of thumb as an initial experiment, not as an answer. Benchmark the workload before and after the change and observe both database and host metrics.</p>

    <h2>Locks: solve the consistency requirement, not the symptom</h2>
    <p>Explicit table or row locks are sometimes correct. They are also easy to overuse. Strong locks can serialize work, create lock queues, and make unrelated sessions appear frozen behind the blocker.</p>
    <p>Before adding an explicit lock, identify the invariant you need:</p>
    <ul>
      <li>Must two transactions update the same row in order?</li>
      <li>Can optimistic concurrency detect a conflict and retry?</li>
      <li>Would <code>SELECT ... FOR UPDATE</code> on a narrow row set be sufficient?</li>
      <li>Would <code>SERIALIZABLE</code> isolation plus retry semantics express the rule more safely?</li>
    </ul>
    <p>There is no universal “never lock” rule. The design goal is to hold the weakest lock over the smallest scope for the shortest time while keeping the business invariant true.</p>

    <h2>Replica reads introduce a consistency contract</h2>
    <p>Read replicas are useful for scaling read workload, but asynchronous replication can return stale data. A read-modify-write business operation that reads from a lagging replica and writes to the primary can therefore make a decision from an old state.</p>
    <p>Classify reads before routing them:</p>
    <table>
      <thead><tr><th>Read type</th><th>Can tolerate lag?</th><th>Example</th></tr></thead>
      <tbody>
        <tr><td>Informational</td><td>Often yes</td><td>Historical dashboard.</td></tr>
        <tr><td>Read-your-writes</td><td>Usually no immediately after a write</td><td>User saves a change, then opens the same record.</td></tr>
        <tr><td>Decision-critical</td><td>Usually no</td><td>Balance, inventory reservation, eligibility decision.</td></tr>
        <tr><td>Analytical snapshot</td><td>Depends on freshness SLA</td><td>Operational reporting with a documented lag budget.</td></tr>
      </tbody>
    </table>
    <p>This is an application architecture choice, not merely a replication setting.</p>

    <h2>Performance triage protocol</h2>
    <ol>
      <li><strong>Define the symptom.</strong> Latency, throughput, CPU, I/O, lock wait, replication lag, temporary files, or connection storm?</li>
      <li><strong>Locate the workload.</strong> Which queries, users, jobs, and time windows correlate with it?</li>
      <li><strong>Inspect active state.</strong> Use <code>pg_stat_activity</code>, wait events, locks, and transaction age.</li>
      <li><strong>Rank expensive SQL.</strong> Use <code>pg_stat_statements</code> where enabled to separate frequent moderate cost from rare extreme cost.</li>
      <li><strong>Read representative plans.</strong> Compare estimated and actual rows, buffers, and the expensive nodes.</li>
      <li><strong>Check maintenance debt.</strong> Dead tuples, vacuum/analyze history, XID age, disk growth, WAL, temp I/O.</li>
      <li><strong>Change one causal layer.</strong> Query, index, schema, concurrency, maintenance, or configuration.</li>
      <li><strong>Re-run at realistic concurrency.</strong> A single-query speedup is not enough if overall throughput or tail latency degrades.</li>
    </ol>

    <h2>Useful measurements</h2>
    <table>
      <thead><tr><th>Question</th><th>Useful evidence</th></tr></thead>
      <tbody>
        <tr><td>What is running now?</td><td><code>pg_stat_activity</code>, wait events, locks.</td></tr>
        <tr><td>Which SQL consumes the workload?</td><td><code>pg_stat_statements</code>.</td></tr>
        <tr><td>Is the planner wrong about row counts?</td><td><code>EXPLAIN (ANALYZE, BUFFERS)</code> on a safe representative query.</td></tr>
        <tr><td>Is maintenance keeping up?</td><td><code>pg_stat_user_tables</code>, vacuum/analyze timestamps, dead tuple estimates, transaction age.</td></tr>
        <tr><td>Is I/O the bottleneck?</td><td><code>pg_stat_io</code>, host I/O, temporary files, buffer statistics.</td></tr>
        <tr><td>Is replication healthy?</td><td><code>pg_stat_replication</code>, WAL positions, replay/flush/write lag as applicable.</td></tr>
      </tbody>
    </table>

    <h2>Sources</h2>
    <ul>
      <li>Jimmy Angelakos, <em>PostgreSQL Mistakes and How to Avoid Them</em>, chapter 6 and Appendix B.</li>
      <li><a href="https://www.postgresql.org/docs/current/mvcc.html">PostgreSQL: Concurrency Control</a></li>
      <li><a href="https://www.postgresql.org/docs/current/routine-vacuuming.html">PostgreSQL: Routine Vacuuming</a></li>
      <li><a href="https://www.postgresql.org/docs/current/runtime-config-resource.html">PostgreSQL: Resource Consumption</a></li>
      <li><a href="https://www.postgresql.org/docs/current/monitoring-stats.html">PostgreSQL: Statistics Collector and Views</a></li>
      <li><a href="https://www.postgresql.org/docs/current/pgstatstatements.html">PostgreSQL: pg_stat_statements</a></li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Continue</h2>
    <ul>
      <li><a href="/atlas/databases/postgresql-mental-model/">PostgreSQL mental model</a></li>
      <li><a href="/atlas/databases/postgresql-indexes-partitioning/">Indexes and partitioning</a></li>
      <li><a href="/atlas/databases/postgresql-production-reliability/">Production reliability</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
