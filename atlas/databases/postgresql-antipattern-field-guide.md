---
layout: default
title: "PostgreSQL Anti-Pattern Field Guide — Signals, Failure Modes, and Better Moves"
description: "A practical PostgreSQL anti-pattern matrix distilled into diagnostic signals: what looks reasonable, why it fails, what to do instead, and what evidence to inspect."
permalink: /atlas/databases/postgresql-antipattern-field-guide/
last_modified_at: 2026-09-29
atlas_section: databases
domain: Data platforms
subdomain: PostgreSQL
concept_type: field guide
status: needs_verification
verified: false
level: 1
author: Dzmitryi Kharlanau
robots: noindex,follow
sitemap: false
tags:
  - postgresql
  - antipatterns
  - sql
  - data-modeling
  - performance
  - reliability
related:
  - /atlas/databases/
  - /atlas/databases/postgresql-query-patterns/
  - /atlas/databases/postgresql-data-modeling/
  - /atlas/databases/postgresql-mvcc-performance/
  - /atlas/databases/postgresql-production-reliability/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/databases/">Databases</a></li>
    <li aria-current="page">PostgreSQL Anti-Pattern Field Guide</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">PostgreSQL / Field Guide</p>
    <h1>The dangerous pattern is usually “reasonable now, expensive later.”</h1>
    <p class="note-subtitle">This guide turns common PostgreSQL mistakes into a diagnostic matrix: the tempting shortcut, the hidden mechanism, the safer direction, and the evidence that should decide.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <div class="note-body">
    <h2>How to use this guide</h2>
    <p>Do not treat the rows below as universal lint rules. PostgreSQL is workload-sensitive. Use each entry as a trigger for a question: <em>Does this mechanism exist in our system, and does the evidence show that it matters?</em></p>
    <p>The recurring structure is:</p>
    <p><strong>tempting shortcut → hidden mechanism → operational consequence → evidence-based alternative.</strong></p>

    <h2>SQL semantics and query shape</h2>
    <table>
      <thead><tr><th>Signal</th><th>Hidden failure mode</th><th>Better move</th><th>Verify with</th></tr></thead>
      <tbody>
        <tr><td><code>NOT IN (SELECT ...)</code> over nullable data</td><td>A single NULL can make the predicate evaluate to unknown rather than true.</td><td>Use <code>NOT EXISTS</code> when the business meaning is “no matching row exists,” and handle NULL intentionally.</td><td>NULL edge-case test; plan shape.</td></tr>
        <tr><td><code>BETWEEN</code> for consecutive time windows</td><td>Both boundaries are inclusive, so adjacent windows can overlap.</td><td>Use half-open intervals: <code>&gt;= start AND &lt; end</code>.</td><td>Rows exactly at the boundary.</td></tr>
        <tr><td><code>count(nullable_column)</code> used as row count</td><td>NULL values are excluded from the aggregate.</td><td>Use <code>count(*)</code> for rows; count the column only when non-NULL presence is the metric.</td><td>Rows with NULL in the counted column.</td></tr>
        <tr><td>Integer division for percentages</td><td>The fractional part can be truncated before later arithmetic.</td><td>Cast before division; protect zero denominators with <code>NULLIF</code>.</td><td>Small numerators and zero totals.</td></tr>
        <tr><td>Function/cast applied to an indexed column in the predicate</td><td>The query expression may no longer match the stored index key.</td><td>Transform the comparison value, use a range, or create a deliberate expression index.</td><td><code>EXPLAIN</code>; presence of an index condition.</td></tr>
        <tr><td><code>SELECT *</code> when the caller needs two columns</td><td>Extra heap reads, network transfer, deserialization, memory, and sometimes loss of index-only access.</td><td>Project only the required columns.</td><td>Buffers, row width, network payload.</td></tr>
        <tr><td>Whole-table filtering in application code</td><td>The database sends and the application processes data that SQL could discard earlier.</td><td>Push filtering, joins, aggregation, and ordering to PostgreSQL where appropriate.</td><td>Rows transferred versus rows consumed.</td></tr>
        <tr><td>CTE chosen because “CTEs are always faster/slower”</td><td>Modern PostgreSQL can inline many CTEs; materialization behavior depends on the query.</td><td>Use CTEs to express meaningful sets, then inspect the plan; control materialization only when justified.</td><td><code>EXPLAIN (ANALYZE, BUFFERS)</code>.</td></tr>
      </tbody>
    </table>

    <h2>Types and data modeling</h2>
    <table>
      <thead><tr><th>Signal</th><th>Hidden failure mode</th><th>Better move</th><th>Verify with</th></tr></thead>
      <tbody>
        <tr><td>Global events stored as <code>timestamp without time zone</code></td><td>The stored value has no instant/time-zone context; elapsed-time logic becomes ambiguous across zones and DST.</td><td>Use <code>timestamptz</code> for real instants; store zone metadata separately when the original zone matters.</td><td>Cross-zone and DST-boundary tests.</td></tr>
        <tr><td><code>time with time zone</code> for operational events</td><td>An offset without a date cannot encode daylight-saving context cleanly.</td><td>Model the full instant when chronology matters.</td><td>Seasonal offset changes.</td></tr>
        <tr><td><code>char(n)</code> used as a “fast fixed-width string”</td><td>Blank-padding semantics create comparison/pattern surprises without the assumed storage benefit.</td><td>Use <code>text</code> plus an explicit domain constraint if length is a real rule.</td><td>Trailing-space, LIKE, regex tests.</td></tr>
        <tr><td><code>varchar(n)</code> length chosen from UI expectations</td><td>The arbitrary limit becomes schema debt and changing it can require DDL.</td><td>Use <code>text</code>; constrain only genuine business limits.</td><td>Longest valid real-world values.</td></tr>
        <tr><td><code>money</code> used for multi-currency business data</td><td>Locale influences formatting/interpretation and the type does not carry a currency code.</td><td>Use exact <code>numeric</code> plus explicit currency and domain rules.</td><td>Rounding and currency-conversion tests.</td></tr>
        <tr><td><code>SERIAL</code> used by default in new schemas</td><td>Sequence ownership and privileges are less explicit; copied table definitions can surprise.</td><td>Prefer SQL-standard identity columns for new design.</td><td>Role privileges; table-copy behavior.</td></tr>
        <tr><td>Sequence expected to be gapless</td><td>Values can be consumed by rolled-back transactions.</td><td>Separate surrogate identity from legally/business-required numbering.</td><td>Rollback and retry scenarios.</td></tr>
        <tr><td>Nullable column inside a logical composite identity</td><td>Default uniqueness treats NULLs as distinct, which may allow duplicates from the application's perspective.</td><td>Clarify the domain; consider an explicit value, normalization, or <code>NULLS NOT DISTINCT</code>.</td><td>Duplicate inserts with NULL.</td></tr>
        <tr><td>Stable relational entities hidden inside JSONB</td><td>Foreign keys, types, joins, and constraints move into repeated casts and application logic.</td><td>Keep stable relational structure relational; use JSONB for genuine variability or document boundaries.</td><td>Repeated extracted join/filter keys.</td></tr>
        <tr><td><code>SQL_ASCII</code> in a multilingual system</td><td>Encoding validation/conversion is largely absent, so incompatible byte sequences can be mixed.</td><td>Use UTF-8 for new systems and plan explicit conversion for legacy data.</td><td>Encoding inventory and round-trip tests.</td></tr>
      </tbody>
    </table>

    <h2>Indexes and physical design</h2>
    <table>
      <thead><tr><th>Signal</th><th>Hidden failure mode</th><th>Better move</th><th>Verify with</th></tr></thead>
      <tbody>
        <tr><td>“B-tree is the index type”</td><td>Different operators and data structures need different access methods.</td><td>Choose B-tree, GIN, GiST, SP-GiST, or BRIN from query operators and distribution.</td><td>Representative plans and workload.</td></tr>
        <tr><td>One huge GIN index over an entire JSON document</td><td>Large write/storage cost may be paid for keys the workload never queries.</td><td>Index only the fields or operators that matter.</td><td>Index size, update cost, top predicates.</td></tr>
        <tr><td>Full index over a state column when only a tiny state subset matters</td><td>Most index entries provide no operational value but still consume space and write work.</td><td>Consider a partial index for the stable active subset.</td><td>Predicate selectivity and query frequency.</td></tr>
        <tr><td>Adding indexes until reads become fast</td><td>Write amplification, WAL, vacuum work, storage, and cache pressure increase.</td><td>Maintain an index budget tied to real query paths.</td><td><code>pg_stat_user_indexes</code>, workload writes, size.</td></tr>
        <tr><td>Dropping “unused” indexes from one node's statistics</td><td>A replica or periodic workload may use the index even if the local primary does not.</td><td>Observe long enough and across the topology before removal.</td><td>Per-node and time-window usage.</td></tr>
        <tr><td>Partitioning because a table is simply “big”</td><td>Queries that do not constrain the partition key still scan many partitions; planning overhead rises.</td><td>Partition when pruning, retention, maintenance, or placement aligns with a stable key.</td><td>Pruned partitions, retention operations, planning time.</td></tr>
        <tr><td>Multi-column RANGE partitioning used as if it were hierarchical</td><td>Combined range boundaries are lexicographic, not independent levels.</td><td>Use explicit subpartitioning when the hierarchy is “time, then branch/tenant/etc.”</td><td>Boundary inserts and pruning plans.</td></tr>
      </tbody>
    </table>

    <h2>Concurrency and performance</h2>
    <table>
      <thead><tr><th>Signal</th><th>Hidden failure mode</th><th>Better move</th><th>Verify with</th></tr></thead>
      <tbody>
        <tr><td>Default PostgreSQL configuration promoted directly to production</td><td>Defaults are conservative portability defaults, not workload-specific capacity decisions.</td><td>Benchmark and tune against real workload and resources.</td><td>Throughput, latency, I/O, memory.</td></tr>
        <tr><td>Huge <code>work_mem</code> because RAM is available</td><td>Multiple plan nodes across concurrent queries can allocate memory independently.</td><td>Keep a safe default; raise per session/job when justified.</td><td>Concurrency test, temp-file use, host memory.</td></tr>
        <tr><td><code>max_connections</code> raised to match all clients</td><td>Backend processes and shared structures contend; latency can explode before throughput improves.</td><td>Bound database concurrency and queue excess work through pooling.</td><td>Active sessions, latency curve, wait events.</td></tr>
        <tr><td>Thousands of mostly idle sessions</td><td>Process and snapshot-management overhead remain even without useful work.</td><td>Right-size pools; consider transaction pooling when semantics allow.</td><td>Idle/active ratio in <code>pg_stat_activity</code>.</td></tr>
        <tr><td><code>idle in transaction</code> left open</td><td>Locks and old snapshots can block DDL and delay vacuum cleanup.</td><td>Fix application transaction scope; use timeouts as a secondary guard.</td><td>Transaction age and blockers.</td></tr>
        <tr><td>Long analytical query on a hot OLTP table/replica</td><td>Old snapshots or recovery conflicts can hold back cleanup or cause cancellation.</td><td>Isolate workloads, shorten transactions, or design reporting architecture explicitly.</td><td>Query age, replica conflicts, vacuum state.</td></tr>
        <tr><td>Autovacuum disabled to “save resources”</td><td>Bloat, stale statistics, and anti-wraparound pressure accumulate.</td><td>Tune autovacuum capacity to write rate; override hot tables where needed.</td><td>Dead tuples, analyze/vacuum history, XID age.</td></tr>
        <tr><td>Very high commit rate for tiny independent writes</td><td>Transaction overhead and XID consumption rise rapidly.</td><td>Batch where the business atomicity boundary allows it.</td><td>Transactions/sec, XID age, latency requirements.</td></tr>
        <tr><td>Explicit strong locks used as the first concurrency tool</td><td>Lock queues serialize unrelated work and amplify latency.</td><td>Use the weakest sufficient lock, optimistic retries, or serializable isolation where appropriate.</td><td>Blocking graph and wait duration.</td></tr>
      </tbody>
    </table>

    <h2>Administration, security, and recovery</h2>
    <table>
      <thead><tr><th>Signal</th><th>Hidden failure mode</th><th>Better move</th><th>Verify with</th></tr></thead>
      <tbody>
        <tr><td>No historical database metrics</td><td>Teams cannot distinguish a spike from a trend or plan capacity.</td><td>Retain workload, storage, WAL, latency, vacuum, and replication history.</td><td>Trend dashboards and incident timelines.</td></tr>
        <tr><td>Logs grow in the same constrained filesystem as data</td><td>Verbose logging can consume space needed for database files or WAL.</td><td>Use deliberate rotation/retention and separate storage where appropriate.</td><td>Filesystem growth and log policy.</td></tr>
        <tr><td><code>listen_addresses='*'</code> without a network reason</td><td>The database listens on interfaces that may not need exposure.</td><td>Bind intentionally and enforce network and HBA policy.</td><td>Listening sockets and reachable networks.</td></tr>
        <tr><td><code>trust</code> authentication in production</td><td>Identity is accepted without credential verification for matching connections.</td><td>Use an appropriate authenticated method and least-access HBA rules.</td><td>HBA path and connection tests.</td></tr>
        <tr><td>Application objects owned by superuser</td><td>Routine operations inherit unnecessary authority and increase blast radius.</td><td>Separate owners, application roles, migrations, monitoring, and admin duties.</td><td>Role membership and object ownership.</td></tr>
        <tr><td>Unreviewed <code>SECURITY DEFINER</code> functions</td><td>Owner privileges plus unsafe object resolution can create escalation paths.</td><td>Use definer rights only when required; secure <code>search_path</code> and grants.</td><td>Test as low-privilege users.</td></tr>
        <tr><td>“We have RAID/snapshots, so we have backups”</td><td>Redundancy does not protect from all corruption, operator error, or historical recovery needs.</td><td>Keep independent backups and define recovery objectives.</td><td>Restore exercise.</td></tr>
        <tr><td>Backups succeed but restores are never tested</td><td>The first full recovery test happens during the outage.</td><td>Rehearse restore, WAL recovery, startup, and business validation regularly.</td><td>Recorded RPO/RTO from a real exercise.</td></tr>
        <tr><td>Manual failover script for a critical cluster</td><td>Rare failure paths are the least-tested code and can create split-brain or long downtime.</td><td>Use mature HA orchestration and test failure semantics.</td><td>Failover drills and fencing behavior.</td></tr>
      </tbody>
    </table>

    <h2>Upgrades and migrations</h2>
    <table>
      <thead><tr><th>Signal</th><th>Hidden failure mode</th><th>Better move</th><th>Verify with</th></tr></thead>
      <tbody>
        <tr><td>Only the target-version release notes are read</td><td>Behavioral changes in intermediate major versions are missed.</td><td>Review every major release between source and target.</td><td>Change inventory mapped to application features.</td></tr>
        <tr><td>Upgrade tested on tiny synthetic data</td><td>Plan, collation, extension, and capacity regressions remain invisible.</td><td>Use production-like data volume and representative workload in pre-production.</td><td>Critical query baselines and load tests.</td></tr>
        <tr><td>Migration assumes types mean the same thing across databases</td><td>Boolean, date/time, numeric, text, NULL, and collation semantics can differ.</td><td>Map behavior, not only type names; validate transformed data.</td><td>Boundary-value and reconciliation tests.</td></tr>
        <tr><td>Legacy encoding treated as a transport detail</td><td>Invalid or mixed byte sequences can fail import or corrupt meaning.</td><td>Inventory encodings, convert explicitly, and validate representative multilingual data.</td><td>Round-trip and invalid-byte checks.</td></tr>
      </tbody>
    </table>

    <h2>Three meta-patterns behind most of the mistakes</h2>
    <ol>
      <li><strong>Borrowed assumptions.</strong> A habit from another database, language, ORM, or cloud product is applied to PostgreSQL without checking its semantics.</li>
      <li><strong>Local optimization.</strong> A change improves one query or benchmark while increasing write cost, operational risk, or future maintenance.</li>
      <li><strong>Deferred reality.</strong> Backups, vacuum, capacity, upgrade work, and documentation are postponed because the system still works today.</li>
    </ol>
    <p>The durable counter-pattern is simple: make the invariant explicit, inspect the mechanism, measure the real workload, and prove the change under the conditions where it has to survive.</p>

    <h2>Sources</h2>
    <ul>
      <li>Jimmy Angelakos, <em>PostgreSQL Mistakes and How to Avoid Them</em>, chapters 2–11 and Appendix B.</li>
      <li><a href="https://www.postgresql.org/docs/current/">PostgreSQL 18 documentation</a></li>
      <li><a href="/atlas/databases/postgresql-query-patterns/">Query patterns — expanded explanation</a></li>
      <li><a href="/atlas/databases/postgresql-data-modeling/">Data modeling — expanded explanation</a></li>
      <li><a href="/atlas/databases/postgresql-indexes-partitioning/">Indexes and partitioning — expanded explanation</a></li>
      <li><a href="/atlas/databases/postgresql-mvcc-performance/">MVCC and performance — expanded explanation</a></li>
      <li><a href="/atlas/databases/postgresql-production-reliability/">Production reliability — expanded explanation</a></li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Continue</h2>
    <ul>
      <li><a href="/atlas/databases/postgresql-mental-model/">PostgreSQL mental model</a></li>
      <li><a href="/atlas/databases/postgresql-troubled-database-playbook/">Troubled database playbook</a></li>
      <li><a href="/atlas/databases/">Database Engineering hub</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
