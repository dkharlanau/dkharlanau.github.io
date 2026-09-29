---
layout: default
title: "PostgreSQL Troubled Database Playbook — Assess Before You Tune"
description: "A practical playbook for inheriting a troubled PostgreSQL database: stabilize risk, inventory the system, identify evidence, prioritize failure modes, make bounded changes, and prove recovery."
permalink: /atlas/databases/postgresql-troubled-database-playbook/
last_modified_at: 2026-09-29
atlas_section: databases
domain: Data platforms
subdomain: PostgreSQL
concept_type: operational playbook
status: needs_verification
verified: false
level: 1
author: Dzmitryi Kharlanau
robots: noindex,follow
sitemap: false
tags:
  - postgresql
  - database-assessment
  - troubleshooting
  - technical-debt
  - operations
related:
  - /atlas/databases/
  - /atlas/databases/postgresql-mental-model/
  - /atlas/databases/postgresql-mvcc-performance/
  - /atlas/databases/postgresql-production-reliability/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/databases/">Databases</a></li>
    <li aria-current="page">Troubled Database Playbook</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">PostgreSQL / Operational Playbook</p>
    <h1>Do not start by tuning. Start by reducing uncertainty.</h1>
    <p class="note-subtitle">When you inherit a database with unknown debt, the first job is to discover which risks are real, which are symptoms, and which changes can safely buy time for deeper work.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <div class="note-body">
    <h2>The failure mode: random improvement</h2>
    <p>A neglected database usually presents dozens of plausible problems at once: slow queries, disk pressure, stale versions, strange types, missing constraints, excessive connections, old PostgreSQL versions, fragile backups, and application code nobody wants to touch. Fixing whatever looks ugly first is emotionally satisfying and operationally risky.</p>
    <p>The better sequence is <strong>stabilize → map → measure → prioritize → change → verify → institutionalize</strong>. The goal is not to turn the system into an ideal schema immediately. The goal is to move it from uncertain and fragile to understood and controllable.</p>

    <h2>Phase 0 — protect the patient</h2>
    <p>Before structural work, identify conditions that can cause irreversible loss or an imminent outage.</p>
    <ul>
      <li>Is storage close to exhaustion, and what is growing?</li>
      <li>Are backups completing, and is there recent evidence of a successful restore?</li>
      <li>Is WAL archiving healthy if PITR depends on it?</li>
      <li>Is the database near transaction-ID wraparound pressure?</li>
      <li>Are long or idle-in-transaction sessions blocking maintenance or DDL?</li>
      <li>Is replication lag or slot retention creating a disk risk?</li>
      <li>Are application roles using superuser or trust-based access?</li>
    </ul>
    <p>If one of these is critical, stabilize it before spending a day redesigning indexes.</p>

    <h2>Phase 1 — build the system inventory</h2>
    <p>Inventory creates a shared map of what exists. Capture facts rather than interpretations.</p>
    <table>
      <thead><tr><th>Area</th><th>Capture</th><th>Why it matters</th></tr></thead>
      <tbody>
        <tr><td>Platform</td><td>PostgreSQL version, OS, deployment model, CPU, RAM, storage, extensions.</td><td>Defines supported features, upgrade path, and resource ceiling.</td></tr>
        <tr><td>Databases and schemas</td><td>Owners, sizes, object counts, dependencies, large tables.</td><td>Shows scope, concentration of data, and ownership risk.</td></tr>
        <tr><td>Data model</td><td>Primary/foreign keys, constraints, data types, NULL patterns, JSON use.</td><td>Reveals where integrity is enforced or delegated to applications.</td></tr>
        <tr><td>Workload</td><td>Peak periods, OLTP/analytics mix, batch jobs, top queries, connection patterns.</td><td>Prevents tuning a benchmark that does not represent production.</td></tr>
        <tr><td>Maintenance</td><td>Vacuum/analyze history, transaction age, bloat signals, index health.</td><td>Shows accumulated MVCC and planner debt.</td></tr>
        <tr><td>Reliability</td><td>Backups, WAL archive, replicas, failover, restore history, RPO/RTO.</td><td>Defines how much failure the business can survive.</td></tr>
        <tr><td>Security</td><td>Roles, ownership, HBA rules, network exposure, definer functions.</td><td>Shows excessive authority and escalation paths.</td></tr>
      </tbody>
    </table>

    <h2>Phase 2 — observe the workload before changing it</h2>
    <p>Collect enough runtime evidence to distinguish chronic design debt from a temporary incident. At minimum, inspect active sessions and waits, long transactions, high-impact SQL, table/index statistics, database size growth, WAL, I/O, and replication state.</p>
    <p>A useful rule is to separate <strong>total cost</strong> from <strong>single-call cost</strong>. A query that takes 50 ms but runs 20 million times can matter more than a 20-second report executed once per night.</p>

    <h2>Phase 3 — build a risk-ranked problem register</h2>
    <p>Do not rank by how embarrassing the schema looks. Rank by business consequence, probability, and how much uncertainty the issue creates.</p>
    <table>
      <thead><tr><th>Priority class</th><th>Examples</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>Data-loss / outage risk</td><td>Untested backup, disk exhaustion, wraparound pressure, broken archive, unsafe failover.</td><td>Stabilize immediately.</td></tr>
        <tr><td>Integrity / security risk</td><td>Missing uniqueness, privileged application role, unsafe <code>SECURITY DEFINER</code>, mixed encodings.</td><td>Contain, then repair with explicit migration.</td></tr>
        <tr><td>Systemic performance risk</td><td>Connection storm, long transactions, autovacuum falling behind, top workload query.</td><td>Measure and remove the dominant bottleneck.</td></tr>
        <tr><td>Maintainability debt</td><td>Confusing schema, redundant indexes, brittle scripts, no documentation.</td><td>Package into bounded follow-up projects.</td></tr>
        <tr><td>Cosmetic debt</td><td>Naming inconsistency with no operational effect.</td><td>Defer unless touched by a larger migration.</td></tr>
      </tbody>
    </table>

    <h2>Use “last good evidence → first bad evidence”</h2>
    <p>This diagnostic pattern works for databases as well as business processes. Instead of asking “Why is PostgreSQL slow?”, locate the last layer that behaves correctly and the first layer where evidence diverges.</p>
    <p>Example:</p>
    <ol>
      <li>Application latency increased.</li>
      <li>Database CPU increased at the same time.</li>
      <li><code>pg_stat_statements</code> shows one statement now dominates total execution time.</li>
      <li><code>EXPLAIN ANALYZE</code> shows actual rows far above the planner estimate.</li>
      <li>Statistics are old after a large data distribution change.</li>
      <li>After targeted ANALYZE, the plan changes and workload latency returns to baseline.</li>
    </ol>
    <p>The fix is not “increase CPU.” The evidence chain identifies the layer that failed.</p>

    <h2>Avoid the XY problem</h2>
    <p>An inherited system often arrives with proposed solutions already attached: “add RAM,” “create this index,” “partition the table,” “turn off vacuum during the batch,” or “move reports to a replica.” Treat those as hypotheses, not requirements.</p>
    <p>Rewrite each request as a problem statement: observable symptom, affected workload, business consequence, evidence, and desired outcome. Then test whether the proposed change addresses the cause.</p>

    <h2>Quick wins should buy optionality</h2>
    <p>A good quick win reduces immediate risk without making the future architecture harder. Examples include fixing a broken backup job, terminating a forgotten blocking transaction through PostgreSQL rather than killing the process, adding a highly targeted missing index, introducing connection pooling, or correcting an obviously unsafe role.</p>
    <p>A bad quick win hides the symptom while increasing debt: disabling autovacuum, raising connections without admission control, deleting unknown files to reclaim disk, or copying a production configuration from an unrelated blog post.</p>

    <h2>Turn each improvement into a bounded experiment</h2>
    <p>For every significant change, record:</p>
    <ul>
      <li><strong>Problem:</strong> what observable behavior is unacceptable?</li>
      <li><strong>Hypothesis:</strong> what mechanism explains it?</li>
      <li><strong>Evidence:</strong> what supports or rejects that explanation?</li>
      <li><strong>Change:</strong> what is the smallest intervention that tests the hypothesis?</li>
      <li><strong>Risk:</strong> what could regress, lock, corrupt, or become unavailable?</li>
      <li><strong>Rollback:</strong> how do we return to the prior state?</li>
      <li><strong>Verification:</strong> what measurements and business checks prove the outcome?</li>
    </ul>

    <h2>Do not finish at “fixed”</h2>
    <p>A repaired system that only one engineer understands remains fragile. Convert discoveries into durable operating assets:</p>
    <ul>
      <li>schema and ownership documentation;</li>
      <li>query and index rationale for critical paths;</li>
      <li>monitoring dashboards and actionable alerts;</li>
      <li>backup and restore runbooks with rehearsal evidence;</li>
      <li>upgrade procedure and compatibility inventory;</li>
      <li>known workload windows and capacity assumptions;</li>
      <li>engineering rules for transactions, connections, SQL review, and migrations.</li>
    </ul>

    <h2>Assessment output</h2>
    <p>A useful database assessment should not end as a 100-item defect list. Produce a small decision set:</p>
    <ol>
      <li>Immediate risks that must be contained.</li>
      <li>Three to five highest-leverage changes with evidence.</li>
      <li>Deferred debt with a reason for deferral.</li>
      <li>Capacity and upgrade horizon.</li>
      <li>Recovery and security gaps.</li>
      <li>Metrics that will prove whether the system is improving.</li>
    </ol>

    <h2>The deeper lesson</h2>
    <p>The book's final chapter is less about individual PostgreSQL tricks than about operating posture: anticipate growth, inspect access patterns, review code, test changes in a production-like environment, document what you learn, and address the real problem rather than the requested workaround. That mindset scales beyond PostgreSQL.</p>

    <h2>Sources</h2>
    <ul>
      <li>Jimmy Angelakos, <em>PostgreSQL Mistakes and How to Avoid Them</em>, chapter 11 and Appendix B.</li>
      <li><a href="https://www.postgresql.org/docs/18/monitoring.html">PostgreSQL: Monitoring Database Activity</a></li>
      <li><a href="https://www.postgresql.org/docs/18/app-pgdump.html">PostgreSQL: pg_dump</a></li>
      <li><a href="https://www.postgresql.org/docs/18/pgstatstatements.html">PostgreSQL: pg_stat_statements</a></li>
      <li><a href="https://www.postgresql.org/docs/18/routine-vacuuming.html">PostgreSQL: Routine Vacuuming</a></li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Continue</h2>
    <ul>
      <li><a href="/atlas/databases/postgresql-mental-model/">PostgreSQL mental model</a></li>
      <li><a href="/atlas/databases/postgresql-mvcc-performance/">MVCC and performance</a></li>
      <li><a href="/atlas/databases/postgresql-production-reliability/">Production reliability</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
