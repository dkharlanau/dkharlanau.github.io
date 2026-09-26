---
layout: default
title: "CRUD Matrix — Process-to-Data Responsibility Map"
description: "How to use a CRUD matrix to show which processes create, read, update, or delete data and expose unclear data ownership."
permalink: /skill-hub/tools-frameworks/crud-matrix/
last_modified_at: 2026-09-26
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/tools-frameworks/">Tools &amp; Frameworks</a></li><li aria-current="page">CRUD Matrix</li></ol></nav>
<article class="section note-detail atlas-page">
<p class="eyebrow">Data responsibility tool</p><h1>CRUD Matrix</h1>
<p class="lead">Use a CRUD matrix when processes and data objects are known, but responsibility for creating and changing data is not. It maps processes or capabilities against data objects using Create, Read, Update, and Delete.</p>

<section><h2>What it reveals</h2><ul>
<li>Objects that nobody clearly creates.</li>
<li>Objects updated by many processes or systems.</li>
<li>Processes that depend on data but have no control over its quality.</li>
<li>Potential system-of-record conflicts.</li>
<li>Missing lifecycle steps such as retirement or deletion.</li>
</ul></section>

<section><h2>Working method</h2>
<ol>
<li>Choose the data objects at the right level: Business Partner, Material, Sales Order, Pricing Condition, not every database table.</li>
<li>List business processes or capabilities in rows.</li>
<li>Mark C, R, U, and D only when the behavior is real and relevant.</li>
<li>Identify where more than one process creates or updates the same object.</li>
<li>Separate technical replication from business ownership.</li>
<li>Confirm the source of truth and correction owner for important attributes.</li>
</ol></section>

<section><h2>SAP example</h2>
<pre><code>| Process | Business Partner | Material | Sales Order | Pricing Condition |
|---|---|---|---|---|
| Customer onboarding | C/U | R | - | R |
| Order management | R | R | C/U | R |
| Pricing management | R | R | R | C/U |
| Integration replication | R | R | R | R |</code></pre>
<p>The integration row may technically write replicated records, but that does not make Integration the business owner of the data.</p></section>

<section><h2>Decision rules</h2><ul>
<li>If several systems create the same business object, verify whether they create different scopes or whether there is a master-data conflict.</li>
<li>If many processes update one object, go to attribute-level ownership for the disputed fields.</li>
<li>If a process only reads data, do not assign it ownership because it suffers from bad data.</li>
<li>If “Delete” is impossible for legal or audit reasons, model retirement, blocking, or archiving instead.</li>
</ul></section>

<section><h2>Pair it with</h2><ul>
<li><a href="/skill-hub/problem-solving-operations/data-discovery-mapping-working-skill/">Data Discovery &amp; Mapping</a></li>
<li><a href="/skill-hub/dama-dmbok/master-data-management-working-skill/">Master Data Management</a></li>
<li><a href="/skill-hub/tools-frameworks/raci/">RACI</a></li>
<li><a href="/skill-hub/tools-frameworks/c4-system-context/">C4 System Context</a></li>
</ul></section>

<section><h2>Verification status and limitations</h2><p>CRUD is a compact analysis matrix. It does not by itself define attribute ownership, data quality rules, integration semantics, or retention policy.</p></section>
</article>
