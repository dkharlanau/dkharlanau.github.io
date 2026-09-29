---
layout: default
title: "PostgreSQL Mental Model — Planner, MVCC, WAL, and Workload"
description: "A practical PostgreSQL mental model for reasoning about query plans, processes, MVCC, WAL, statistics, maintenance, and workload before tuning."
permalink: /atlas/databases/postgresql-mental-model/
last_modified_at: 2026-09-29
atlas_section: databases
domain: Data platforms
subdomain: PostgreSQL
concept_type: mental model
status: needs_verification
verified: false
level: 1
author: Dzmitryi Kharlanau
robots: noindex,follow
sitemap: false
tags:
  - postgresql
  - mvcc
  - query-planner
  - wal
  - database-performance
related:
  - /atlas/databases/
  - /atlas/databases/postgresql-query-patterns/
  - /atlas/databases/postgresql-mvcc-performance/
  - /atlas/databases/postgresql-production-reliability/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/databases/">Databases</a></li>
    <li aria-current="page">PostgreSQL Mental Model</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">PostgreSQL / Mental Model</p>
    <h1>Understand the machine before tuning the knobs.</h1>
    <p class="note-subtitle">PostgreSQL becomes easier to diagnose when you stop treating a slow query, a lock, and a vacuum problem as separate mysteries.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>A useful mental model is not “PostgreSQL stores tables and runs SQL.” It is closer to this: PostgreSQL is a concurrent state machine that chooses access paths from statistics, gives transactions controlled views of changing data, persists changes through WAL, and continuously performs maintenance so old row versions and transaction history do not become a liability.</p>
    <p>This matters because the visible symptom is often one layer away from the cause. “The database is slow” may really mean the planner estimated the wrong cardinality. “VACUUM is expensive” may mean long transactions prevented routine cleanup until debt accumulated. “We need 2,000 connections” may mean the application has no admission control.</p>

    <h2>Six moving parts</h2>
    <table>
      <thead><tr><th>Part</th><th>What it decides or protects</th><th>What to ask when it fails</th></tr></thead>
      <tbody>
        <tr><td>Backend processes</td><td>Each client session is served by a PostgreSQL backend process, with shared structures coordinating work.</td><td>How many sessions are active, waiting, idle, or opening at once?</td></tr>
        <tr><td>Planner / optimizer</td><td>Chooses a plan from estimated costs and statistics.</td><td>Are estimates wrong? Is the predicate indexable? Is the chosen plan appropriate for the real row count?</td></tr>
        <tr><td>MVCC</td><td>Lets readers and writers coexist through row versions and transaction visibility.</td><td>Which snapshot is being held, and what old versions must remain visible?</td></tr>
        <tr><td>WAL</td><td>Records changes needed for crash recovery and replication before modified data pages are safely persisted.</td><td>Is WAL growing, archiving, replaying, or lagging as expected?</td></tr>
        <tr><td>VACUUM / ANALYZE</td><td>Reclaims reusable space, protects against transaction-ID wraparound, and refreshes planner statistics.</td><td>Is maintenance keeping up with write volume, or being blocked by long-lived transactions?</td></tr>
        <tr><td>Storage and memory</td><td>Buffers hot data, sorts and hashes intermediate results, and ultimately performs I/O.</td><td>Is the bottleneck CPU, memory pressure, cache misses, temporary files, or physical I/O?</td></tr>
      </tbody>
    </table>

    <h2>The planner is not a rule engine</h2>
    <p>PostgreSQL does not follow a simple hierarchy such as “index exists, therefore use index.” It compares possible plans using a cost model and statistics. A sequential scan can be the correct plan when much of a table is needed. An index can be useless when the query transforms the indexed column into a different expression. A perfectly valid index can be ignored when the planner expects it to touch too many heap pages.</p>
    <p>The practical consequence is important: do not diagnose a plan by ideology. Compare estimated rows with actual rows, inspect filters and access methods, then ask whether the statistics and query shape explain the decision.</p>

    <h2>MVCC changes the meaning of “delete” and “update”</h2>
    <p>In PostgreSQL, an UPDATE creates a new row version and makes the old version obsolete for future snapshots. A DELETE also leaves a version that cannot be physically forgotten while an older transaction may still need to see it. That is why maintenance is structural, not cosmetic.</p>
    <p>Once this is clear, several production rules stop looking arbitrary:</p>
    <ul>
      <li>Long-running transactions can retain old versions and delay cleanup.</li>
      <li><code>idle in transaction</code> is more dangerous than a merely idle connection because a transaction can continue to hold locks and visibility state.</li>
      <li>Autovacuum is part of the storage model. Disabling it does not remove the work; it postpones the bill.</li>
      <li>High write rates consume transaction IDs quickly, so maintenance capacity must scale with workload.</li>
    </ul>

    <h2>WAL is part of your availability model</h2>
    <p>Write-ahead logging is not just an internal detail. WAL connects crash recovery, physical replication, continuous archiving, and point-in-time recovery. If a system has replication but no tested restore path, it has redundancy but not necessarily recoverability. If WAL archiving is broken, a backup strategy that depends on PITR is broken even if the last base backup succeeded.</p>

    <h2>Configuration is workload-specific</h2>
    <p>The book demonstrates why PostgreSQL's conservative self-managed defaults should not be mistaken for production tuning, but it also shows the opposite failure: making memory settings huge can reduce throughput or crash the host. In particular, <code>work_mem</code> is not a single global budget for the server; it can be consumed by multiple plan operations across concurrent queries.</p>
    <p>So avoid one-number folklore such as “set X to 25% of RAM” as a final answer. A better sequence is workload → measurement → controlled change → repeatable benchmark → production observation.</p>

    <h2>A practical diagnostic order</h2>
    <ol>
      <li><strong>Correctness first.</strong> Confirm that the query and data model express the intended business rule.</li>
      <li><strong>Plan second.</strong> Use <code>EXPLAIN</code> and, when safe, <code>EXPLAIN ANALYZE</code> to inspect how PostgreSQL reaches the data.</li>
      <li><strong>Cardinality third.</strong> Compare estimated rows with actual rows and inspect statistics when they diverge materially.</li>
      <li><strong>Concurrency fourth.</strong> Look for waits, locks, connection pressure, long transactions, and replica lag.</li>
      <li><strong>Maintenance fifth.</strong> Check vacuum/analyze health, bloat indicators, WAL, disk, and temporary-file pressure.</li>
      <li><strong>Configuration last.</strong> Tune only after the workload and bottleneck are visible.</li>
    </ol>

    <h2>What not to conclude too early</h2>
    <table>
      <thead><tr><th>Observation</th><th>Weak conclusion</th><th>Better question</th></tr></thead>
      <tbody>
        <tr><td>Sequential scan</td><td>“Missing index.”</td><td>How selective is the predicate, and how much of the table is actually needed?</td></tr>
        <tr><td>High CPU</td><td>“Need a bigger server.”</td><td>Which queries and plan nodes consume CPU, and are we doing avoidable work?</td></tr>
        <tr><td>Many sessions</td><td>“Need higher max_connections.”</td><td>How many sessions are truly active, and should excess demand queue in a pooler?</td></tr>
        <tr><td>Autovacuum running often</td><td>“Vacuum is hurting performance.”</td><td>Is the write workload generating cleanup debt faster than maintenance can process it?</td></tr>
        <tr><td>Replica read is stale</td><td>“Replication is broken.”</td><td>What consistency guarantee does this application operation actually require?</td></tr>
      </tbody>
    </table>

    <h2>Version note</h2>
    <p>PostgreSQL 18 is the current stable major release. It introduced, among other changes, a new asynchronous I/O subsystem, broader index use through skip-scan support, retained optimizer statistics during <code>pg_upgrade</code>, and built-in <code>uuidv7()</code>. These improvements do not replace the mental model above; they make it even more important to validate assumptions against the version actually running.</p>

    <h2>Sources</h2>
    <ul>
      <li>Jimmy Angelakos, <em>PostgreSQL Mistakes and How to Avoid Them</em>, especially chapters 1, 6, 7, and 11.</li>
      <li><a href="https://www.postgresql.org/docs/18/using-explain.html">PostgreSQL: Using EXPLAIN</a></li>
      <li><a href="https://www.postgresql.org/docs/18/routine-vacuuming.html">PostgreSQL: Routine Vacuuming</a></li>
      <li><a href="https://www.postgresql.org/docs/18/monitoring.html">PostgreSQL: Monitoring Database Activity</a></li>
      <li><a href="https://www.postgresql.org/docs/18/release-18.html">PostgreSQL 18 release notes</a></li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Continue</h2>
    <ul>
      <li><a href="/atlas/databases/postgresql-query-patterns/">PostgreSQL query patterns</a></li>
      <li><a href="/atlas/databases/postgresql-mvcc-performance/">MVCC, vacuum, and concurrency</a></li>
      <li><a href="/atlas/databases/postgresql-production-reliability/">Production reliability</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
