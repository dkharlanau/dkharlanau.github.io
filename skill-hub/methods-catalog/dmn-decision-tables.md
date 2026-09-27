---
layout: default
title: "DMN Decision Tables — Practical Business Decision Modeling"
description: "Use DMN-style decision tables to make complex business decision logic explicit, reviewable, testable, and separate from process flow."
permalink: /skill-hub/methods-catalog/dmn-decision-tables/
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
    <li aria-current="page">DMN Decision Tables</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Methods Catalog — Decision Logic</p>
  <h1>DMN Decision Tables</h1>
  <p class="lead">Use a decision table when prose and process branches can no longer explain business logic safely. Make the inputs, combinations, outputs, and gaps visible.</p>

  <section>
    <h2>What this method is for</h2>
    <p>Decision Model and Notation (DMN) is a standard for modeling decisions and business rules. A decision table is one of its most useful practical forms: input conditions are arranged against explicit outcomes so business, analysts, developers, and testers can review the same logic.</p>
    <p>Keep process flow and decision logic separate. BPMN can show <em>when</em> a decision is needed. DMN can show <em>how</em> the outcome is determined.</p>
  </section>

  <section>
    <h2>When to use it</h2>
    <ul>
      <li>A business rule contains many “if / and / except when” clauses.</li>
      <li>Different teams implement the same decision differently.</li>
      <li>Testing misses combinations because rules live in prose.</li>
      <li>A pricing, eligibility, routing, credit, tax, or approval decision needs explicit traceability.</li>
      <li>A process diagram has become unreadable because one gateway has many rule branches.</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Name one decision.</strong> Example: “Determine delivery priority.”</li>
      <li><strong>Name the output.</strong> What value must the decision produce?</li>
      <li><strong>List required input data.</strong> Use business terms and identify the source of each input.</li>
      <li><strong>Collect rules and examples.</strong> Use <a href="/skill-hub/business-analysis/business-rules-discovery-working-skill/">Business Rules Discovery</a> and <a href="/skill-hub/methods-catalog/example-mapping/">Example Mapping</a> where needed.</li>
      <li><strong>Build table rows.</strong> Each row represents a meaningful combination and output.</li>
      <li><strong>Check overlaps and gaps.</strong> Can two rows match? Can no row match?</li>
      <li><strong>Define priority or hit behavior where necessary.</strong> If multiple rules can match, the table must state how to resolve that.</li>
      <li><strong>Create test cases from rows and boundaries.</strong></li>
      <li><strong>Validate with the business decision owner.</strong> Technical correctness is not enough.</li>
    </ol>
  </section>

  <section>
    <h2>SAP example — order approval route</h2>
    <div class="table-scroll">
      <table class="study-table">
        <thead><tr><th>Order value</th><th>Margin</th><th>Customer risk</th><th>Outcome</th></tr></thead>
        <tbody>
          <tr><td>&lt; 10,000</td><td>&gt;= 20%</td><td>Low</td><td>Auto approve</td></tr>
          <tr><td>&lt; 10,000</td><td>&lt; 20%</td><td>Any</td><td>Sales Manager approval</td></tr>
          <tr><td>&gt;= 10,000</td><td>Any</td><td>Low</td><td>Sales Director approval</td></tr>
          <tr><td>Any</td><td>Any</td><td>High</td><td>Credit review required</td></tr>
        </tbody>
      </table>
    </div>
    <p>The table immediately raises an important question: if an order is above 10,000 and customer risk is High, which outcome wins? That ambiguity is much harder to see in prose.</p>
  </section>

  <section>
    <h2>Decision rules for the modeling work</h2>
    <ul>
      <li>If a table row cannot be explained to the business owner, the input model is probably too technical.</li>
      <li>If two rows can match and the outputs conflict, define hit policy or redesign the rules.</li>
      <li>If no row covers a valid input combination, define a default or expose the gap.</li>
      <li>If one input comes from an unreliable source, treat data quality as part of decision risk.</li>
      <li>If the table has many unrelated outputs, split the decision into smaller dependent decisions.</li>
      <li>If the process needs routing around the decision, use <a href="/skill-hub/methods-catalog/bpmn/">BPMN</a> for the surrounding flow.</li>
    </ul>
  </section>

  <section>
    <h2>Copy-ready template</h2>
    <pre><code>## Decision
&lt;business question&gt;

## Output
&lt;decision result / type&gt;

## Inputs
| Input | Business meaning | Source | Valid values / range | Owner |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Decision table
| Rule | Input A | Input B | Input C | Output | Rationale / Source |
|---|---|---|---|---|---|
| R1 | ... | ... | ... | ... | ... |
| R2 | ... | ... | ... | ... | ... |

## Hit behavior
&lt;one match / priority / collect / other&gt;

## Gaps and overlaps
- ...

## Test boundaries
- ...
- ...

## Decision owner
&lt;business role&gt;</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>One clear decision and output are modeled.</li>
      <li>Every input has business meaning and a source.</li>
      <li>Rows use mutually understood conditions.</li>
      <li>Overlaps and uncovered combinations are tested.</li>
      <li>Multiple-match behavior is explicit.</li>
      <li>Boundary values become test cases.</li>
      <li>A business owner validates the logic.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Copying code conditions into a table.</strong> The business cannot validate technical implementation syntax.</li>
      <li><strong>Ignoring input ownership.</strong> A perfect rule with bad source data still makes bad decisions.</li>
      <li><strong>Building one giant table for several decisions.</strong> Decompose the logic.</li>
      <li><strong>Assuming rows are complete because they look structured.</strong> Systematic gap and overlap review is essential.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>An AI agent should extract rules from evidence, propose normalized inputs, detect possible overlaps and gaps, and derive candidate test cases. It must mark inferred rules as assumptions and must not treat generated logic as approved business policy.</p>
  </section>

  <section>
    <h2>Related skills and methods</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/business-rules-discovery-working-skill/">Business Rules Discovery</a></li>
      <li><a href="/skill-hub/methods-catalog/example-mapping/">Example Mapping</a></li>
      <li><a href="/skill-hub/methods-catalog/bpmn/">BPMN</a></li>
      <li><a href="/skill-hub/testing-quality-delivery/test-scenario-derivation-working-skill/">Test Scenario Derivation</a></li>
      <li><a href="/skill-hub/systems-analysis/state-lifecycle-analysis-working-skill/">State &amp; Lifecycle Analysis</a></li>
    </ul>
  </section>

  <section>
    <h2>Reference and limitations</h2>
    <p><a href="https://www.omg.org/dmn/">Object Management Group</a> maintains the DMN standard. This page focuses on practical decision tables and does not teach the complete DMN notation, FEEL expression language, or execution semantics.</p>
  </section>
</article>