---
layout: default
title: "PostgreSQL Data Modeling — Time, Text, Money, Identity, UUID, JSONB, and Constraints"
description: "A practical PostgreSQL data-modeling guide: choose types and constraints that preserve business meaning instead of encoding accidental implementation habits."
permalink: /atlas/databases/postgresql-data-modeling/
last_modified_at: 2026-09-29
atlas_section: databases
domain: Data platforms
subdomain: PostgreSQL
concept_type: data modeling guide
status: needs_verification
verified: false
level: 1
author: Dzmitryi Kharlanau
robots: noindex,follow
sitemap: false
tags:
  - postgresql
  - data-modeling
  - timestamptz
  - jsonb
  - uuid
  - constraints
related:
  - /atlas/databases/
  - /atlas/databases/postgresql-query-patterns/
  - /atlas/databases/postgresql-indexes-partitioning/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/databases/">Databases</a></li>
    <li aria-current="page">PostgreSQL Data Modeling</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">PostgreSQL / Data Modeling</p>
    <h1>A data type is a business decision with storage consequences.</h1>
    <p class="note-subtitle">Good schemas make invalid states difficult to represent. Weak schemas push meaning into application code, conventions, and tribal memory.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <div class="note-body">
    <h2>Start from the invariant</h2>
    <p>Choosing a PostgreSQL type should begin with the statement the system must keep true. “This is a timestamp” is too vague. Is it an instant on the global timeline, a local wall-clock appointment, a calendar date, a recurring time of day, or a duration? “This is a price” is also incomplete. Does it require exact arithmetic, a currency, scale rules, and positive-value constraints?</p>
    <p>The schema is strongest when those answers are visible in types, constraints, relationships, and names rather than reconstructed later from application behavior.</p>

    <h2>Time: distinguish an instant from a local clock reading</h2>
    <p>Use <code>timestamptz</code> for an event that happened at a specific instant: an order creation, payment receipt, API event, job start, or audit record. PostgreSQL stores the instant and displays it according to the session time zone; it does not preserve the original zone label that the client typed.</p>
    <p>Use <code>timestamp without time zone</code> when the value intentionally has no global instant semantics, for example “the shop opens at 09:00 local date X” in a model where the location or zone is stored separately. The mistake is not that the type exists. The mistake is storing global events in a type that has no zone context and then performing elapsed-time calculations across locations or daylight-saving transitions.</p>
    <p><code>time with time zone</code> is rarely the right representation because a zone offset without a date lacks the context needed for daylight-saving rules. For most operational events, model the full instant.</p>

    <h2>Text: length limits should express a rule, not a guess</h2>
    <p><code>char(n)</code> adds blank-padding semantics that surprise pattern matching and waste attention. <code>varchar(n)</code> is often used because another database or ORM made a length mandatory, not because the domain really has that limit. PostgreSQL does not make <code>varchar(n)</code> inherently faster than unrestricted text.</p>
    <p>If a real business rule says a code is at most 12 characters, make the rule explicit:</p>
<pre><code class="language-sql">code text NOT NULL
  CHECK (char_length(code) &lt;= 12)</code></pre>
    <p>This separates the storage type from the domain rule and makes the constraint easier to evolve. For repeated business concepts, a domain can centralize the rule when that improves consistency.</p>

    <h2>Money: store exact value and currency separately</h2>
    <p>PostgreSQL's <code>money</code> type is influenced by locale and does not carry a currency code. For enterprise data, a safer model is usually an exact <code>numeric</code> amount plus an explicit currency column, with scale and range rules appropriate to the domain.</p>
<pre><code class="language-sql">amount numeric(19,4) NOT NULL,
currency_code text NOT NULL
  CHECK (currency_code ~ '^[A-Z]{3}$')</code></pre>
    <p>The exact precision and currency validation should follow the system of record and business requirements. Do not copy the example mechanically into accounting software.</p>

    <h2>Identity: prefer explicit identity semantics over SERIAL for new design</h2>
    <p><code>SERIAL</code> is convenient legacy shorthand around a sequence and default expression. SQL-standard identity columns make ownership and lifecycle clearer and behave better when schemas are copied or managed through privileges.</p>
<pre><code class="language-sql">id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY</code></pre>
    <p>Do not confuse a database sequence with a gapless business number. Sequence values can be consumed by transactions that later roll back. Invoice, receipt, or legal document numbering may need a separate controlled process.</p>

    <h2>UUID: choose it for distribution, not fashion</h2>
    <p>The book demonstrates the storage and index cost of random UUIDv4 keys compared with <code>bigint</code>. That remains a useful warning, but the conclusion needs a 2026 update: PostgreSQL 18 includes <code>uuidv7()</code>, which generates time-ordered UUIDs with better index locality than random UUIDv4.</p>
    <p>The design question is therefore not “UUID or integer?” in the abstract:</p>
    <table>
      <thead><tr><th>Need</th><th>Reasonable direction</th></tr></thead>
      <tbody>
        <tr><td>Single database generates internal surrogate keys</td><td>Identity <code>bigint</code> is simple, compact, and efficient.</td></tr>
        <tr><td>Many nodes must generate IDs without coordination</td><td>UUID can remove a coordination dependency.</td></tr>
        <tr><td>Externally exposed identifiers should not reveal simple sequence order</td><td>UUID may be useful, but do not treat obscurity as authorization.</td></tr>
        <tr><td>Write locality matters and UUID is required</td><td>Consider UUIDv7 on supported versions rather than random UUIDv4.</td></tr>
      </tbody>
    </table>
    <p>UUID is 128 bits. Use the larger key because it solves a real architectural problem, not because it looks globally unique.</p>

    <h2>NULL and uniqueness: decide what unknown means</h2>
    <p>By default, PostgreSQL unique constraints treat two NULL values as distinct, so a composite unique key can allow multiple rows that appear equivalent to the application when one component is NULL. PostgreSQL supports <code>NULLS NOT DISTINCT</code> when the domain requires NULL values to compare as equal for uniqueness.</p>
<pre><code class="language-sql">UNIQUE NULLS NOT DISTINCT
  (product_id, warehouse_id, area)</code></pre>
    <p>But treat this as a semantic choice, not merely an UPSERT fix. If NULL really means “common area,” an explicit value or normalized relationship may describe the domain more clearly.</p>

    <h2>JSONB: use flexibility at the edges, not as an excuse to abandon relationships</h2>
    <p>JSONB is valuable when attributes are genuinely variable, the application needs to preserve external documents, or an object is often read and written as a unit. PostgreSQL also indexes JSONB effectively for appropriate operators.</p>
    <p>The warning from the book is about <em>relational JSON</em>: storing stable entities, foreign-key relationships, numeric values, dates, and join keys inside blobs, then reconstructing the relational model with casts and JSON operators in every query.</p>
    <p>A simple test: if you repeatedly extract the same JSON keys to join, constrain, sort, and aggregate them, those keys are asking to become columns.</p>

    <h2>Encoding and collation are schema-level dependencies</h2>
    <p>For new systems, use UTF-8. <code>SQL_ASCII</code> largely disables encoding validation and conversion, making it possible to mix incompatible byte sequences that later become difficult or impossible to decode reliably.</p>
    <p>Collation is separate from encoding. It affects comparison and ordering rules and can influence indexes. Record the expected locale/provider behavior and test migrations across operating-system or ICU changes when text ordering matters.</p>

    <h2>Constraints belong close to the data</h2>
    <p>Application validation is useful, but it is not a substitute for database invariants when several applications, jobs, migrations, or users can write the same data. Use <code>NOT NULL</code>, <code>CHECK</code>, unique constraints, foreign keys, and exclusion constraints when they express facts that must remain true regardless of the writer.</p>
    <p>A useful review question is: “If a new integration bypassed the main application tomorrow, which business rules would the database still protect?”</p>

    <h2>Modeling checklist</h2>
    <ol>
      <li>Write the business invariant in plain language.</li>
      <li>Choose the type that preserves that meaning without hidden conventions.</li>
      <li>Decide whether NULL represents unknown, not applicable, not yet known, or a real state that deserves its own value.</li>
      <li>Put stable relationships into relational constraints.</li>
      <li>Use JSONB for variability, not to avoid modeling known structure.</li>
      <li>Choose key strategy from coordination, exposure, locality, and lifecycle requirements.</li>
      <li>Test boundary values, time-zone transitions, currency precision, duplicates, and migrations.</li>
    </ol>

    <h2>Sources</h2>
    <ul>
      <li>Jimmy Angelakos, <em>PostgreSQL Mistakes and How to Avoid Them</em>, chapters 3 and 5 and Appendix B.</li>
      <li><a href="https://www.postgresql.org/docs/current/datatype-datetime.html">PostgreSQL: Date/Time Types</a></li>
      <li><a href="https://www.postgresql.org/docs/current/datatype-character.html">PostgreSQL: Character Types</a></li>
      <li><a href="https://www.postgresql.org/docs/current/ddl-constraints.html">PostgreSQL: Constraints</a></li>
      <li><a href="https://www.postgresql.org/docs/current/datatype-json.html">PostgreSQL: JSON Types</a></li>
      <li><a href="https://www.postgresql.org/docs/18/functions-uuid.html">PostgreSQL 18: UUID Functions</a></li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Continue</h2>
    <ul>
      <li><a href="/atlas/databases/postgresql-query-patterns/">Query patterns</a></li>
      <li><a href="/atlas/databases/postgresql-indexes-partitioning/">Indexes and partitioning</a></li>
      <li><a href="/atlas/databases/postgresql-production-reliability/">Production reliability</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
