---
layout: default
title: "DACI — Practical Decision Ownership Method"
description: "Use DACI to make decision ownership explicit: Driver, Approver, Contributors, and Informed."
permalink: /skill-hub/methods-catalog/daci/
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
    <li aria-current="page">DACI</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Methods Catalog — Decisions</p>
  <h1>DACI</h1>
  <p class="lead">Use DACI when a decision is stuck because too many people participate but nobody is clearly driving it or approving it.</p>

  <section>
    <h2>What this method is for</h2>
    <p>DACI separates four decision roles: <strong>Driver</strong> moves the decision to closure; <strong>Approver</strong> makes the final decision; <strong>Contributors</strong> provide facts, options, and constraints; <strong>Informed</strong> receive the decision and consequences.</p>
    <p>RACI is strong for recurring work and deliverables. DACI is stronger when the unit of work is one important decision.</p>
  </section>

  <section>
    <h2>When to use it</h2>
    <ul>
      <li>A solution option has been discussed for weeks without closure.</li>
      <li>Architecture, business, security, and operations all want a voice in the same decision.</li>
      <li>A workshop generates options but no one owns the next step.</li>
      <li>The project needs to know who can approve a scope, design, cutover, or policy choice.</li>
      <li>An escalation exists because “consensus” has become a veto by everyone.</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Write the decision as a question.</strong> Example: “Which integration pattern will carry sales-order status from S/4HANA to the customer portal?”</li>
      <li><strong>Set a decision deadline.</strong> Without a time boundary, Driver becomes meeting coordinator rather than decision owner.</li>
      <li><strong>Name one Driver.</strong> This role collects evidence, frames options, schedules review, and pushes unresolved points to closure.</li>
      <li><strong>Name one Approver where governance allows.</strong> The Approver owns the final call and accepts the trade-off.</li>
      <li><strong>Choose Contributors because of evidence they own.</strong> Architecture, security, process, support, data, or finance may contribute.</li>
      <li><strong>Keep Informed outside the decision loop.</strong> They need the result, not another meeting invitation.</li>
      <li><strong>Define the evidence needed before approval.</strong> Options, risks, cost, NFRs, test evidence, or operational impact.</li>
      <li><strong>Record the outcome.</strong> For architecture decisions, create an <a href="/skill-hub/architecture/architecture-decision-record-working-skill/">ADR</a>.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If there is no single Driver, the decision will usually drift.</li>
      <li>If there are several Approvers, define the governance sequence or escalation rule explicitly.</li>
      <li>If a Contributor has formal veto authority, do not pretend the role is only advisory.</li>
      <li>If the decision is reversible and low-cost, shorten the evidence cycle.</li>
      <li>If the decision is hard to reverse, increase evidence, review, and record quality.</li>
      <li>If the same decision repeats operationally, convert the logic into a rule, policy, or <a href="/skill-hub/methods-catalog/dmn-decision-tables/">DMN decision table</a>.</li>
    </ul>
  </section>

  <section>
    <h2>SAP example — choose an integration pattern</h2>
    <div class="table-scroll">
      <table class="study-table">
        <thead><tr><th>Role</th><th>Assignment</th><th>What they contribute</th></tr></thead>
        <tbody>
          <tr><td>Driver</td><td>Integration Architect</td><td>Frames API vs event options, gathers NFRs, closes open questions</td></tr>
          <tr><td>Approver</td><td>Solution Architecture Lead</td><td>Owns final pattern decision and landscape consequence</td></tr>
          <tr><td>Contributors</td><td>SAP SD Lead, Portal Lead, Security, Operations</td><td>Business event, consumer behavior, security, supportability</td></tr>
          <tr><td>Informed</td><td>Project Manager, QA, Service Desk</td><td>Receives the approved pattern and delivery impact</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Copy-ready template</h2>
    <pre><code>## Decision
&lt;One decision question&gt;

## Deadline
&lt;Date / milestone&gt;

## Driver
&lt;One role&gt;

## Approver
&lt;One role or explicit approval chain&gt;

## Contributors
- &lt;Role&gt; — evidence/input:
- &lt;Role&gt; — evidence/input:

## Informed
- &lt;Role&gt; — what they need after the decision:

## Evidence required
- &lt;fact, NFR, cost, risk, test, policy&gt;

## Options
1. &lt;Option&gt; — benefit / risk / constraint
2. &lt;Option&gt; — benefit / risk / constraint

## Decision
&lt;Selected option + reason&gt;

## Record
&lt;ADR / decision log / ticket link&gt;</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The decision is one clear question.</li>
      <li>There is one named Driver.</li>
      <li>Final approval authority is explicit.</li>
      <li>Contributors are selected for evidence, not status.</li>
      <li>The deadline and minimum evidence are known.</li>
      <li>The result is recorded with consequences.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Using DACI for every small task.</strong> It creates governance overhead.</li>
      <li><strong>Calling everyone a Contributor.</strong> The decision becomes another consensus meeting.</li>
      <li><strong>Confusing Driver with Approver.</strong> The person doing the coordination does not automatically own the final authority.</li>
      <li><strong>Closing the decision without documenting consequences.</strong> The same debate returns months later.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>An AI agent should turn a vague dispute into one decision question, identify missing authority information, build an option/evidence table, and keep proposed roles marked as proposals until confirmed. It should never infer an Approver only from seniority.</p>
  </section>

  <section>
    <h2>Related skills and methods</h2>
    <ul>
      <li><a href="/skill-hub/methods-catalog/raci-matrix/">RACI Matrix</a></li>
      <li><a href="/skill-hub/decision-validation/trade-off-analysis-working-skill/">Trade-off Analysis</a></li>
      <li><a href="/skill-hub/architecture/architecture-decision-record-working-skill/">Architecture Decision Record</a></li>
      <li><a href="/skill-hub/business-analysis/stakeholder-analysis-working-skill/">Stakeholder Analysis</a></li>
    </ul>
  </section>

  <section>
    <h2>Status and limitations</h2>
    <p>This is a practical decision-governance pattern. Organizations use variants with different role names. Match the method to the real approval model instead of forcing local governance into four letters.</p>
  </section>
</article>