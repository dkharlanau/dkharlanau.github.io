---
layout: default
title: "PostgreSQL Query Patterns — NULL, Ranges, COUNT, CTEs, and Indexable Predicates"
description: "Practical PostgreSQL query patterns for avoiding silent correctness bugs and unnecessary work: NULL semantics, half-open ranges, COUNT, arithmetic, CTEs, indexable predicates, and minimal projection."
permalink: /atlas/databases/postgresql-query-patterns/
last_modified_at: 2026-09-29
atlas_section: databases
domain: Data platforms
subdomain: PostgreSQL
concept_type: query guide
status: needs_verification
verified: false
level: 1
author: Dzmitryi Kharlanau
robots: noindex,follow
sitemap: false
tags:
  - postgresql
  - sql
  - query-design
  - sql-null
  - explain
related:
  - /atlas/databases/
  - /atlas/databases/postgresql-mental-model/
  - /atlas/databases/postgresql-indexes-partitioning/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/databases/">Databases</a></li>
    <li aria-current="page">PostgreSQL Query Patterns</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">PostgreSQL / Query Design</p>
    <h1>Queries can be wrong while looking completely reasonable.</h1>
    <p class="note-subtitle">The most expensive SQL mistakes are often not syntax errors. They return plausible results, scale badly, or quietly disable the access path you thought you had.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <div class="note-body">
    <h2>1. Treat NULL as a third logical state</h2>
    <p>SQL is not ordinary two-valued application logic. A comparison involving an unknown value can evaluate to unknown rather than true or false. That is why a <code>NOT IN</code> subquery becomes dangerous when the subquery can return NULL: the outer predicate may never become true for rows you expected to keep.</p>
    <p>When the business question is “show rows for which no matching row exists,” express that relationship directly:</p>
<pre><code class="language-sql">SELECT c.email
FROM customer_contact_details AS c
WHERE c.state IS NOT NULL
  AND NOT EXISTS (
    SELECT 1
    FROM suppliers AS s
    WHERE s.state = c.state
  );</code></pre>
    <p>The rule is not “never use NOT IN.” It is: know whether NULL can enter the compared set, and use anti-join semantics when absence of a related row is what you actually mean.</p>

    <h2>2. Use half-open intervals for adjacent time windows</h2>
    <p><code>BETWEEN</code> includes both boundaries. That is harmless for many human-readable ranges, but dangerous for consecutive processing windows. If yesterday ends exactly where today begins, an inclusive upper bound can count the boundary twice.</p>
<pre><code class="language-sql">WHERE event_time &gt;= :window_start
  AND event_time &lt;  :window_end</code></pre>
    <p>The half-open interval <code>[start, end)</code> composes cleanly: one window ends exactly where the next starts. Use the same pattern for time slices, numeric buckets, paging keys, and incremental ETL windows unless the business rule explicitly requires a closed interval.</p>

    <h2>3. Decide whether you are counting rows or values</h2>
    <p><code>count(*)</code> counts rows. <code>count(column)</code> counts non-NULL values in that column. They answer different questions.</p>
    <table>
      <thead><tr><th>Question</th><th>Expression</th></tr></thead>
      <tbody>
        <tr><td>How many orders matched?</td><td><code>count(*)</code></td></tr>
        <tr><td>How many matched orders have a service value?</td><td><code>count(service_id)</code></td></tr>
        <tr><td>What share of matched orders are services?</td><td><code>count(service_id)::numeric / NULLIF(count(*), 0)</code></td></tr>
      </tbody>
    </table>
    <p>Being explicit about the denominator is part of correctness, not formatting.</p>

    <h2>4. Integer arithmetic stays integer until you change the type</h2>
    <p>Dividing integers can truncate the fractional part before later arithmetic is applied. If a ratio is conceptually fractional, convert before division and protect the denominator.</p>
<pre><code class="language-sql">SELECT
  item_count::numeric
  / NULLIF(item_count + service_count, 0)
  * 100 AS item_percent;</code></pre>
    <p>For money and exact business ratios, prefer exact numeric types where approximation is not acceptable.</p>

    <h2>5. Do not hide an indexed column behind a different expression by accident</h2>
    <p>An index is built on a value or expression. If the query transforms the indexed column into something else, the original index may no longer match the predicate.</p>
    <p>Weak pattern:</p>
<pre><code class="language-sql">WHERE date_trunc('second', event_time) = :second</code></pre>
    <p>Often better:</p>
<pre><code class="language-sql">WHERE event_time &gt;= :second
  AND event_time &lt;  :second + interval '1 second'</code></pre>
    <p>If the transformed expression really is the stable access pattern, an expression index may be appropriate. The key is to make the query and index describe the same expression deliberately.</p>

    <h2>6. Use CTEs to expose reasoning boundaries, not as cargo cult</h2>
    <p>A common table expression can make a complex query easier to read, test, and discuss. In modern PostgreSQL, a non-recursive CTE may be inlined into the surrounding query when that is safe and useful. <code>MATERIALIZED</code> can force a separate intermediate result; <code>NOT MATERIALIZED</code> can permit inlining in cases where you want the optimizer to see through the boundary.</p>
    <p>That means “CTE is faster” and “CTE is an optimization fence” are both bad universal rules. Use a CTE first to name a meaningful intermediate set. Then inspect the plan.</p>

    <h2>7. Select the data you need</h2>
    <p><code>SELECT *</code> is not merely a style preference when the application needs one or two columns. Extra columns increase I/O, network transfer, deserialization, memory use, and can prevent an index-only plan. Pulling an entire table into application memory to filter it there is a stronger version of the same mistake.</p>
    <p>A good default is to push filtering, joining, grouping, ordering, and projection into the database when the database has the relevant data and can execute the operation efficiently.</p>

    <h2>8. Test edge cases before performance</h2>
    <p>Before optimizing a query, try to break its meaning. A compact test set catches a surprising number of production defects:</p>
    <ul>
      <li>one matching row;</li>
      <li>no matching rows;</li>
      <li>NULL in every nullable predicate column;</li>
      <li>values exactly on range boundaries;</li>
      <li>zero denominator;</li>
      <li>duplicate rows on both sides of a join;</li>
      <li>unexpected case, whitespace, or encoding;</li>
      <li>enough rows to reveal a different plan.</li>
    </ul>

    <h2>9. Read the plan, but know what ANALYZE does</h2>
    <p><code>EXPLAIN</code> shows the chosen plan without executing the statement. <code>EXPLAIN ANALYZE</code> executes it and adds actual timing and row counts. For data-changing statements, that means the change is real unless you wrap it in a transaction and roll it back.</p>
    <p>When a plan is slow, start with four questions: Which node dominates time? Where do estimated and actual rows diverge? Is an expected index condition present? How many rows are removed by filters after they have already been read?</p>

    <h2>10. Use linters and AI as reviewers, not authorities</h2>
    <p>The book recommends tools such as SQLFluff, plpgsql_check, and Squawk because they catch different classes of mistakes before production. The same principle applies to LLM-generated SQL: use it to explore alternatives, explain plans, and challenge assumptions, but validate syntax, schema assumptions, correctness, and performance against the real database.</p>

    <h2>A compact review checklist</h2>
    <table>
      <thead><tr><th>Check</th><th>Question</th></tr></thead>
      <tbody>
        <tr><td>NULL</td><td>Can any operand be unknown, and what does that do to the predicate?</td></tr>
        <tr><td>Boundaries</td><td>Are adjacent ranges overlapping?</td></tr>
        <tr><td>Cardinality</td><td>Can joins or duplicates multiply rows?</td></tr>
        <tr><td>Type</td><td>Will arithmetic or casting change precision or semantics?</td></tr>
        <tr><td>Access path</td><td>Does the predicate match the indexed value or expression?</td></tr>
        <tr><td>Projection</td><td>Are we reading columns or rows the consumer will discard?</td></tr>
        <tr><td>Plan</td><td>Do estimates resemble reality?</td></tr>
        <tr><td>Scale</td><td>Does the same design remain acceptable when the table grows by 10× or 100×?</td></tr>
      </tbody>
    </table>

    <h2>Sources</h2>
    <ul>
      <li>Jimmy Angelakos, <em>PostgreSQL Mistakes and How to Avoid Them</em>, chapter 2 and Appendix B.</li>
      <li><a href="https://www.postgresql.org/docs/current/functions-subquery.html">PostgreSQL: Subquery Expressions</a></li>
      <li><a href="https://www.postgresql.org/docs/current/queries-with.html">PostgreSQL: WITH Queries</a></li>
      <li><a href="https://www.postgresql.org/docs/current/indexes-expressional.html">PostgreSQL: Indexes on Expressions</a></li>
      <li><a href="https://www.postgresql.org/docs/current/using-explain.html">PostgreSQL: Using EXPLAIN</a></li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Continue</h2>
    <ul>
      <li><a href="/atlas/databases/postgresql-data-modeling/">Data types and schema decisions</a></li>
      <li><a href="/atlas/databases/postgresql-indexes-partitioning/">Indexes and partitioning</a></li>
      <li><a href="/atlas/databases/postgresql-mvcc-performance/">MVCC and performance</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
