---
layout: default
title: "Sequence Diagrams — Interaction Order Across Systems"
description: "How to use sequence diagrams to show actors, systems, messages, timing order, failures, retries, and response paths."
permalink: /skill-hub/tools-frameworks/sequence-diagrams/
last_modified_at: 2026-09-26
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/tools-frameworks/">Tools &amp; Frameworks</a></li><li aria-current="page">Sequence Diagrams</li></ol></nav>
<article class="section note-detail atlas-page">
<p class="eyebrow">Interaction modeling</p><h1>Sequence Diagrams</h1>
<p class="lead">Use a sequence diagram when the order of interactions matters. It shows which actor or system sends what message to whom, in what order, and what happens on the return path or failure path.</p>

<section><h2>Use it when</h2><ul>
<li>An API call works in isolation but the end-to-end orchestration fails.</li>
<li>Two systems disagree about who initiates a message.</li>
<li>A timeout, retry, callback, or asynchronous acknowledgement changes the outcome.</li>
<li>You need to compare a synchronous and asynchronous integration option.</li>
</ul></section>

<section><h2>Working method</h2>
<ol>
<li>Choose one scenario, such as “create order from commerce platform”.</li>
<li>Place actors and systems from left to right.</li>
<li>Write the trigger at the top.</li>
<li>Add messages in time order with useful business names.</li>
<li>Show important responses, errors, retries, timeouts, or callbacks.</li>
<li>Mark where data is persisted or ownership changes if it matters.</li>
<li>Validate the diagram against logs, interface contracts, or implementation evidence.</li>
</ol></section>

<section><h2>SAP example</h2>
<pre><code>Customer -> Commerce: Submit order
Commerce -> Integration: Create order request
Integration -> S/4HANA: Sales order API call
S/4HANA -> Integration: Order number / error
Integration -> Commerce: Confirmation
Commerce -> Customer: Order accepted</code></pre>
<p>Add the failure path: what happens if S/4HANA returns a business error, times out, or accepts the order but the response is lost?</p></section>

<section><h2>Decision rules</h2><ul>
<li>If the main question is system boundary, start with C4 System Context.</li>
<li>If the main question is entity lifecycle, use a state-machine view.</li>
<li>If retries can create duplicates, explicitly show idempotency or duplicate handling.</li>
<li>If the diagram describes a future design, separate assumptions from verified current behavior.</li>
</ul></section>

<section><h2>Pair it with</h2><ul>
<li><a href="/skill-hub/systems-analysis/interface-requirement-analysis-working-skill/">Interface Requirement Analysis</a></li>
<li><a href="/skill-hub/tools-frameworks/c4-system-context/">C4 System Context</a></li>
<li><a href="/skill-hub/integration-architecture/api-integration-working-skill/">API Integration</a></li>
<li><a href="/skill-hub/integration-architecture/integration-error-handling-working-skill/">Integration Error Handling</a></li>
</ul></section>

<section><h2>Reference</h2><ul><li><a href="https://www.omg.org/uml/">Object Management Group — UML</a></li></ul></section>
<section><h2>Verification status and limitations</h2><p>This page uses sequence diagrams as a practical interaction tool. It does not cover the full UML interaction specification.</p></section>
</article>
