---
layout: default
title: "State Machine Diagrams — Entity Lifecycle and Valid Transitions"
description: "How to model states, events, transitions, guards, and invalid lifecycle paths for enterprise entities."
permalink: /skill-hub/tools-frameworks/state-machine-diagrams/
last_modified_at: 2026-09-26
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/tools-frameworks/">Tools &amp; Frameworks</a></li><li aria-current="page">State Machine Diagrams</li></ol></nav>
<article class="section note-detail atlas-page">
<p class="eyebrow">Lifecycle modeling</p><h1>State Machine Diagrams</h1>
<p class="lead">Use a state machine when the important question is not the process step but the valid condition of an entity over time: what states exist, what event changes the state, and what guard allows or blocks the transition.</p>

<section><h2>Core model</h2>
<table class="study-table"><thead><tr><th>Element</th><th>Question</th></tr></thead><tbody>
<tr><td>State</td><td>What stable condition is the entity in?</td></tr>
<tr><td>Event</td><td>What happened that may cause a transition?</td></tr>
<tr><td>Transition</td><td>From which state to which state?</td></tr>
<tr><td>Guard</td><td>What condition must be true?</td></tr>
<tr><td>Action</td><td>What happens during the transition?</td></tr>
</tbody></table>
</section>

<section><h2>Working method</h2>
<ol>
<li>Choose one entity: sales order, delivery, purchase order, interface message, approval request.</li>
<li>List observed business-relevant states.</li>
<li>For every transition, name the event that causes it.</li>
<li>Add guard conditions only when they are verified or explicitly marked as assumptions.</li>
<li>Identify impossible, terminal, blocked, and recovery states.</li>
<li>Compare the model with production data to find states that documentation missed.</li>
<li>Derive validation and test scenarios from valid and invalid transitions.</li>
</ol></section>

<section><h2>SAP example</h2><p>A sales order can move through states such as Draft → Complete → Credit Blocked → Released → Delivery Due → Completed. The useful model must show what causes each transition and what prevents an invalid jump, not merely copy status-field labels.</p></section>

<section><h2>Decision rules</h2><ul>
<li>If the state is only a screen page or process activity, it may not be a real entity state.</li>
<li>If the same event produces different outcomes, look for guard conditions or hidden rules.</li>
<li>If data contains a state that the model says is impossible, investigate before “fixing” the data.</li>
<li>If several entities interact, use a sequence or process model alongside the state machine.</li>
</ul></section>

<section><h2>Pair it with</h2><ul>
<li><a href="/skill-hub/systems-analysis/state-lifecycle-analysis-working-skill/">State &amp; Lifecycle Analysis</a></li>
<li><a href="/skill-hub/business-analysis/business-rules-discovery-working-skill/">Business Rules Discovery</a></li>
<li><a href="/skill-hub/tools-frameworks/sequence-diagrams/">Sequence Diagrams</a></li>
</ul></section>

<section><h2>Reference</h2><ul><li><a href="https://www.omg.org/uml/">Object Management Group — UML</a></li></ul></section>
<section><h2>Verification status and limitations</h2><p>This page teaches the practical state-machine subset used in analysis and testing. It does not cover all UML state-machine semantics.</p></section>
</article>
