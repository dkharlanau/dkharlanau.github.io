---
layout: default
title: "EventStorming — Collaborative Domain Discovery"
description: "How to use EventStorming to discover business events, commands, policies, hotspots, and boundaries across business and IT."
permalink: /skill-hub/tools-frameworks/eventstorming/
last_modified_at: 2026-09-26
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/tools-frameworks/">Tools &amp; Frameworks</a></li><li aria-current="page">EventStorming</li></ol></nav>
<article class="section note-detail atlas-page">
<p class="eyebrow">Collaborative discovery</p><h1>EventStorming</h1>
<p class="lead">Use EventStorming when a complex domain is split across departments, systems, and specialist language. The workshop starts from business events that already happened or should happen, then exposes commands, rules, actors, policies, and hotspots.</p>

<section><h2>Why it is useful</h2><p>A normal workshop often starts with opinions or a solution. EventStorming starts with observable domain events: “Sales Order Created”, “Credit Check Failed”, “Delivery Released”, “Goods Issue Posted”. This gives business and technical participants a shared timeline before they argue about architecture.</p></section>

<section><h2>Basic flow</h2>
<ol>
<li>Define the business area and time horizon.</li>
<li>Ask participants to write important past-tense domain events.</li>
<li>Place events in time order.</li>
<li>Mark disagreements, missing knowledge, delays, loops, and pain points as hotspots.</li>
<li>Add the commands or user/system actions that cause important events.</li>
<li>Add actors, business policies, external systems, and key information.</li>
<li>Look for natural boundaries where language, ownership, or rules change.</li>
<li>Convert the result into follow-up work: process maps, requirements, decision models, integration boundaries, or experiments.</li>
</ol></section>

<section><h2>Use it when</h2><ul>
<li>Each department describes the same process differently.</li>
<li>The process is event-heavy and spans many systems.</li>
<li>You need to discover hidden rules before designing an integration or workflow.</li>
<li>The main risk is misunderstanding the domain, not drawing the final diagram.</li>
</ul></section>

<section><h2>Do not use it as</h2><ul>
<li>A replacement for final BPMN, interface contracts, or acceptance criteria.</li>
<li>A workshop where the architect places all notes while others watch.</li>
<li>A reason to redesign architecture before the domain is understood.</li>
</ul></section>

<section><h2>SAP example</h2><p>For a delivery-block problem, the event line may reveal that the business thinks “Order Approved” means the block is removed, while SAP actually waits for a separate status or background step. That mismatch becomes a testable analysis question instead of a vague complaint.</p></section>

<section><h2>Output checklist</h2><ul>
<li>Events are written in past tense.</li>
<li>Hotspots are visible and assigned follow-up owners.</li>
<li>Rules and policies are separated from events.</li>
<li>System names do not replace business meaning.</li>
<li>Boundaries are hypotheses until validated.</li>
</ul></section>

<section><h2>Pair it with</h2><ul>
<li><a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis</a></li>
<li><a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Elicitation</a></li>
<li><a href="/skill-hub/tools-frameworks/bpmn/">BPMN</a></li>
<li><a href="/skill-hub/tools-frameworks/c4-system-context/">C4 System Context</a></li>
</ul></section>

<section><h2>Reference</h2><ul><li><a href="https://www.eventstorming.com/">EventStorming — official site by Alberto Brandolini</a></li></ul></section>
<section><h2>Verification status and limitations</h2><p>This is a compact field guide, not the full EventStorming method. Workshop facilitation quality strongly affects the result.</p></section>
</article>
