---
layout: default
title: "EventStorming — Practical Collaborative Domain Discovery"
description: "Use EventStorming to build shared understanding of business events, commands, policies, actors, systems, hotspots, and domain boundaries."
permalink: /skill-hub/methods-catalog/eventstorming/
last_modified_at: 2026-09-27
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/methods-catalog/">Methods &amp; Frameworks</a></li>
    <li aria-current="page">EventStorming</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Methods Catalog — Domain Discovery</p>
  <h1>EventStorming</h1>
  <p class="lead">Use EventStorming when knowledge about a business domain is distributed across business, operations, architects, and developers. Model what happens before deciding how systems should be built.</p>

  <section>
    <h2>What this method is for</h2>
    <p>EventStorming is a collaborative modeling technique centered on <strong>domain events</strong>: meaningful things that happened in the business. From events, teams can discover commands, actors, policies, external systems, read models, hotspots, and boundaries.</p>
    <p>The key value is collective learning. A wall full of notes is not the goal. The goal is a shared model that exposes conflicts, hidden rules, missing events, and different meanings of the same words.</p>
  </section>

  <section>
    <h2>When to use it</h2>
    <ul>
      <li>Business and IT use different language for the same process.</li>
      <li>A domain spans several SAP and non-SAP systems and no single person knows the whole flow.</li>
      <li>A modernization or integration project needs to understand real business events before designing APIs or services.</li>
      <li>Requirements workshops produce lists but not causal understanding.</li>
      <li>Teams suspect that system boundaries do not match business responsibility boundaries.</li>
    </ul>
  </section>

  <section>
    <h2>Core building blocks</h2>
    <div class="table-scroll">
      <table class="study-table">
        <thead><tr><th>Element</th><th>Question</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>Domain Event</td><td>What meaningful thing happened?</td><td>Sales Order Blocked</td></tr>
          <tr><td>Command</td><td>What action tried to make it happen?</td><td>Release Sales Order</td></tr>
          <tr><td>Actor</td><td>Who initiated the command?</td><td>Credit Controller</td></tr>
          <tr><td>Policy</td><td>What event causes another command or rule?</td><td>When Credit Limit Exceeded → Request Review</td></tr>
          <tr><td>External System</td><td>What outside system participates?</td><td>Credit-rating provider</td></tr>
          <tr><td>Read Model / Information</td><td>What information is needed to decide?</td><td>Exposure by customer</td></tr>
          <tr><td>Hotspot</td><td>Where are we uncertain or in conflict?</td><td>Who owns manual override?</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Working method — Big Picture first</h2>
    <ol>
      <li><strong>Invite people with different knowledge.</strong> Business, operations, support, architecture, development, data, and adjacent functions.</li>
      <li><strong>Define the domain or value stream boundary loosely.</strong> Do not over-design scope before discovery.</li>
      <li><strong>Storm domain events in past tense.</strong> “Delivery Created,” “Credit Check Failed,” “Invoice Posted.”</li>
      <li><strong>Place events in rough time order.</strong> Duplicates and contradictions are useful signals.</li>
      <li><strong>Mark hotspots.</strong> Unknown rules, policy conflicts, ownership gaps, inconsistent terminology.</li>
      <li><strong>Add commands and actors around important events.</strong> Ask what caused the event and who or what initiated it.</li>
      <li><strong>Add policies and external systems.</strong> This reveals automation, integrations, and cross-boundary dependencies.</li>
      <li><strong>Look for natural boundaries.</strong> Different language, rules, ownership, or rate of change can indicate separate domains or contexts.</li>
      <li><strong>Convert discoveries into focused artifacts.</strong> BPMN, DMN, context maps, requirements, ADRs, or backlog items.</li>
    </ol>
  </section>

  <section>
    <h2>SAP example — order-to-cash discovery</h2>
    <p>A cross-functional workshop may expose events such as Customer Created, Order Received, Price Determined, Credit Check Failed, Order Released, Delivery Created, Goods Issued, Invoice Posted, Payment Received, Dispute Opened. Hotspots can reveal that “order released” means commercial release to Sales but credit release to Finance, while integration teams use the same phrase for message processing.</p>
    <p>That language conflict is a design risk. Resolve the domain meaning before naming APIs, events, statuses, or test cases.</p>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the workshop starts drawing screens and APIs, return to business events and behavior.</li>
      <li>If participants disagree on event names, treat that as domain evidence, not facilitation failure.</li>
      <li>If a hotspot contains complex decision logic, continue with <a href="/skill-hub/methods-catalog/dmn-decision-tables/">DMN</a>.</li>
      <li>If a stable process flow must be documented, continue with <a href="/skill-hub/methods-catalog/bpmn/">BPMN</a>.</li>
      <li>If boundaries between systems are the issue, continue with <a href="/skill-hub/architecture/system-context-mapping-working-skill/">System Context Mapping</a>.</li>
      <li>If events are being invented without domain experts, stop and gather evidence.</li>
    </ul>
  </section>

  <section>
    <h2>Copy-ready capture template</h2>
    <pre><code>## Domain / Scope
&lt;area being explored&gt;

## Event chain
1. Event: &lt;past tense fact&gt;
   - Command:
   - Actor:
   - Information needed:
   - Policy / Rule:
   - External system:
   - Hotspot:

2. Event: ...

## Language conflicts
- Term:
  - Meaning A:
  - Meaning B:
  - Resolution owner:

## Candidate boundaries
- &lt;boundary&gt; — evidence:

## Follow-up artifacts
- BPMN:
- DMN:
- System Context:
- Requirements:
- ADR:
- Backlog:</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Events are business-meaningful and written as things that happened.</li>
      <li>Several functions or disciplines contributed.</li>
      <li>Hotspots remain visible instead of being silently resolved.</li>
      <li>Different meanings of important terms are recorded.</li>
      <li>Commands, policies, and actors explain important causal links.</li>
      <li>The workshop produces focused follow-up analysis, not only a photo of the wall.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Running the workshop only with IT.</strong> The model becomes a system flow rather than domain discovery.</li>
      <li><strong>Correcting participants too early.</strong> Contradictions are often the most valuable discovery.</li>
      <li><strong>Trying to make the board clean during exploration.</strong> Premature structure can hide uncertainty.</li>
      <li><strong>Treating every event as an integration event.</strong> Domain events are business facts; only some should become published technical events.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>An AI agent can cluster notes, detect duplicate terms, identify missing causal links, and prepare follow-up artifacts. It must not resolve hotspots or choose domain boundaries without human domain validation. Keep observed statements, hypotheses, and proposed structure separate.</p>
  </section>

  <section>
    <h2>Related skills and methods</h2>
    <ul>
      <li><a href="/skill-hub/methods-catalog/bpmn/">BPMN</a></li>
      <li><a href="/skill-hub/methods-catalog/dmn-decision-tables/">DMN Decision Tables</a></li>
      <li><a href="/skill-hub/architecture/system-context-mapping-working-skill/">System Context Mapping</a></li>
      <li><a href="/skill-hub/business-analysis/business-rules-discovery-working-skill/">Business Rules Discovery</a></li>
      <li><a href="/skill-hub/integration-architecture/event-driven-architecture-working-skill/">Event-Driven Architecture</a></li>
    </ul>
  </section>

  <section>
    <h2>Reference and limitations</h2>
    <p><a href="https://www.eventstorming.com/">EventStorming</a> was introduced by Alberto Brandolini as a collaborative modeling approach and has expanded from process modeling into organizational and software design contexts. This page uses the Big Picture style for enterprise discovery, not the full method.</p>
  </section>
</article>