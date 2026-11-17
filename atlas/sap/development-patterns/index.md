---
layout: default
title: "SAP Development Pattern Library — ABAP, RAP, CAP and Integration"
description: "16 practical design patterns for SAP developers: architecture vocabulary, implementation moves, failure modes and design review phrases."
permalink: /atlas/sap/development-patterns/
author: "Dzmitryi Kharlanau"
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-17
hide_global_cta: true
tags:
  - sap
  - abap
  - software-architecture
  - design-patterns
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>
  <li><a href="/">Home</a></li><li><a href="/atlas/">Atlas</a></li><li><a href="/atlas/sap/">SAP</a></li>
  <li aria-current="page">Development Patterns</li>
</ol></nav>
<div class="research-canvas">
  <header class="research-canvas__hero">
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">SAP engineering · Shared architecture language</p>
      <h1>Give the design a name.<br />Make the trade-off discussable.</h1>
      <p>ABAP enhancements, RAP business objects, CAP services and IDoc integrations are easier to maintain when developers share precise names for recurring design decisions. Not a checklist of fashionable patterns: a compact working vocabulary for real SAP constraints.</p>
      <a class="research-canvas__button" href="#choose">Find a pattern <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Pattern library inventory">
      <p>First edition · 17 November 2026</p>
      <div class="research-canvas__signal-line"><span>16</span><strong>Pattern notes</strong><small>Stable IDs</small></div>
      <div class="research-canvas__signal-line"><span>5</span><strong>Architecture lenses</strong><small>ABAP · RAP · CAP · Integration · Core</small></div>
      <div class="research-canvas__signal-line"><span>1</span><strong>Review language</strong><small>When · why · risk · proof</small></div>
      <em>Public working edition. Articles are available to read but noindex until editorial verification.</em>
    </div>
  </header>
  <section class="research-canvas__boundary">
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>Pattern is a decision, not a badge.</strong> Naming Strategy, Managed RAP or Outbox does not validate a design. State the problem, transaction owner, alternatives, risks and one test that can falsify the proposal. SAP CAP means Cloud Application Programming Model; RAP and CAP are programming models, not interchangeable design patterns.</p>
  </section>
  <section class="research-canvas__inventory" id="choose">
    <header><p class="research-canvas__eyebrow">Start from the pain</p><h2>Which design problem are you solving?</h2><p>Pick a symptom, then open a pattern. Every page includes a small SAP example and a sentence you can use during code review.</p></header>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Architecture problem to pattern mapping">
      <table class="study-table__table">
        <thead><tr><th scope="col">What keeps going wrong?</th><th scope="col">Pattern to discuss</th><th scope="col">First question</th></tr></thead>
        <tbody>
          <tr><td>One enhancement does everything</td><td><a href="/atlas/sap/development-patterns/thin-entry-point/">Thin Entry Point</a></td><td>What can be tested without the runtime?</td></tr>
          <tr><td>Country and sales org IF forests</td><td><a href="/atlas/sap/development-patterns/strategy-policy/">Strategy</a> / <a href="/atlas/sap/development-patterns/decision-table/">Decision Table</a></td><td>Is variation an algorithm or just data?</td></tr>
          <tr><td>External and target keys differ</td><td><a href="/atlas/sap/development-patterns/anti-corruption-layer/">Anti-Corruption Layer</a></td><td>Where does translation finish?</td></tr>
          <tr><td>Delta IDoc wipes existing values</td><td><a href="/atlas/sap/development-patterns/delta-aware-merge/">Delta-Aware Merge</a></td><td>What counts as absent vs cleared?</td></tr>
          <tr><td>New custom transactional app</td><td><a href="/atlas/sap/development-patterns/managed-rap-business-object/">Managed RAP BO</a></td><td>Who owns the persistence?</td></tr>
          <tr><td>Existing transaction needs modern API</td><td><a href="/atlas/sap/development-patterns/unmanaged-rap-facade/">Unmanaged RAP Facade</a></td><td>Who controls save and COMMIT?</td></tr>
          <tr><td>Cloud app exposes ERP schema</td><td><a href="/atlas/sap/development-patterns/cap-service-facade/">CAP Service Facade</a></td><td>What contract does the consumer need?</td></tr>
          <tr><td>Retries create duplicate changes</td><td><a href="/atlas/sap/development-patterns/idempotent-consumer/">Idempotent Consumer</a></td><td>What uniquely identifies the business intent?</td></tr>
          <tr><td>DB update succeeds but event is lost</td><td><a href="/atlas/sap/development-patterns/transactional-outbox/">Transactional Outbox</a></td><td>Is intent stored with the transaction?</td></tr>
          <tr><td>Extension relies on internal SAP APIs</td><td><a href="/atlas/sap/development-patterns/released-api-boundary/">Released API Boundary</a></td><td>Is the object released for this edition?</td></tr>
        </tbody>
      </table>
    </div>
  </section>
<section class="research-canvas__inventory" id="abap-oo"><header><p class="research-canvas__eyebrow">ABAP OO</p><h2>Make enhancements and rules understandable</h2><p>Extract behavior from SAP hooks, choose how rules vary, and keep data access testable.</p></header><div class="research-route-list">
<a href="/atlas/sap/development-patterns/thin-entry-point/"><span>SDP-01</span><strong>Thin Entry Point</strong><small>A BAdI, user exit or IDoc hook should route work, not become the application.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
<a href="/atlas/sap/development-patterns/strategy-policy/"><span>SDP-02</span><strong>Strategy / Policy Resolver</strong><small>Replace a forest of country, channel or organization CASE branches with named policies.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
<a href="/atlas/sap/development-patterns/repository-and-dependency-injection/"><span>SDP-03</span><strong>Repository + Dependency Injection</strong><small>Hide database and SAP API calls behind a testable boundary.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
<a href="/atlas/sap/development-patterns/anti-corruption-layer/"><span>SDP-04</span><strong>Anti-Corruption Layer (ACL)</strong><small>Translate legacy or external meanings once, before they reach core rules.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
<a href="/atlas/sap/development-patterns/decision-table/"><span>SDP-06</span><strong>Decision Table / Rules as Data</strong><small>When the business owns many combinations, stop encoding them as nested IF statements.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
</div></section>
<section class="research-canvas__inventory" id="rap"><header><p class="research-canvas__eyebrow">RAP</p><h2>Design business-object contracts</h2><p>Start from ownership, then choose managed/unmanaged, business behavior and draft.</p></header><div class="research-route-list">
<a href="/atlas/sap/development-patterns/managed-rap-business-object/"><span>SDP-08</span><strong>Managed RAP Business Object</strong><small>Let the RAP runtime own ordinary persistence, locking and transactional plumbing for custom data.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
<a href="/atlas/sap/development-patterns/unmanaged-rap-facade/"><span>SDP-09</span><strong>Unmanaged RAP Facade</strong><small>Modernize the service contract around proven transactional logic without rewriting the engine first.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
<a href="/atlas/sap/development-patterns/behavior-rule-placement/"><span>SDP-10</span><strong>RAP Validation vs Determination vs Action</strong><small>Use the RAP behavior concept that matches the business meaning.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
<a href="/atlas/sap/development-patterns/draft-workflow/"><span>SDP-11</span><strong>RAP Draft Workflow</strong><small>Separate 'I am editing' from 'the active business state has changed'.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
</div></section>
<section class="research-canvas__inventory" id="cap"><header><p class="research-canvas__eyebrow">CAP</p><h2>Keep cloud services business-oriented</h2><p>Let CDS and the CAP runtime handle ordinary service work; put custom logic at the right lifecycle boundary.</p></header><div class="research-route-list">
<a href="/atlas/sap/development-patterns/cap-service-facade/"><span>SDP-12</span><strong>CAP Service Facade</strong><small>Expose a purpose-built service contract instead of publishing the database model verbatim.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
<a href="/atlas/sap/development-patterns/cap-event-handler/"><span>SDP-13</span><strong>CAP Event Handler / Lifecycle Hook</strong><small>Add custom logic around CAP's service events while keeping the service contract in charge.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
</div></section>
<section class="research-canvas__inventory" id="integration"><header><p class="research-canvas__eyebrow">Integration</p><h2>Build for partial updates, replay and failure</h2><p>Interpret deltas correctly, handle duplicate delivery and design observable recovery.</p></header><div class="research-route-list">
<a href="/atlas/sap/development-patterns/delta-aware-merge/"><span>SDP-05</span><strong>Delta-Aware Merge / Patch Semantics</strong><small>A missing field, an explicitly cleared field and a deleted segment must not mean the same thing.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
<a href="/atlas/sap/development-patterns/idempotent-consumer/"><span>SDP-14</span><strong>Idempotent Consumer</strong><small>A retry must not create a second business effect.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
<a href="/atlas/sap/development-patterns/transactional-outbox/"><span>SDP-15</span><strong>Transactional Outbox / Commit-Then-Publish</strong><small>Never claim an event was delivered just because business code reached its last line.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
<a href="/atlas/sap/development-patterns/retry-and-dead-letter/"><span>SDP-16</span><strong>Retry + Dead Letter / Quarantine</strong><small>Retry a temporary outage; quarantine bad data; never run an infinite retry storm.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
</div></section>
<section class="research-canvas__inventory" id="clean-core"><header><p class="research-canvas__eyebrow">Clean Core</p><h2>Protect the SAP lifecycle boundary</h2><p>Choose released contracts and make exceptions visible.</p></header><div class="research-route-list">
<a href="/atlas/sap/development-patterns/released-api-boundary/"><span>SDP-07</span><strong>Released API Boundary (Clean Core)</strong><small>Depend on an intentional SAP contract, not on a convenient internal table or implementation detail.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
</div></section>
  <section class="research-canvas__inventory">
    <header><p class="research-canvas__eyebrow">Use the vocabulary</p><h2>Make patterns visible in tickets, ADRs and pull requests.</h2><p>Write the ID, the architectural boundary, why it fits, the rejected alternative and the proof. A name alone is not an architecture review.</p></header>
    <div class="research-route-list">
      <a href="/atlas/sap/development-patterns/design-review/"><span>ADR</span><strong>Design review template &amp; phrases</strong><small>Copy a concrete review structure. Compare good architecture language with empty buzzwords.</small><i class="material-symbols-outlined" aria-hidden="true">article</i></a>
      <a href="/atlas/sap/development-patterns/manifest.json"><span>JSON</span><strong>Machine-readable pattern manifest</strong><small>Stable IDs, slugs, category, summary and canonical URL for tools and agents.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/labs/enterprise-context/development/"><span>LAB</span><strong>RAP vs CAP vs ABAP Cloud architecture guide</strong><small>Choose the runtime and transaction boundary before choosing an implementation pattern.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
    </div>
  </section>
  <section class="research-canvas__boundary"><span class="material-symbols-outlined" aria-hidden="true">verified_user</span><p><strong>Trust boundary:</strong> Synthetic examples and conceptual code sketches only. These pages are independent learning notes, not SAP-certified code or official employer/client guidance. Confirm released APIs, RAP contracts, IDoc semantics and CAP runtime behavior in the specific SAP release before implementation.</p></section>
  <div class="research-canvas__support">{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
