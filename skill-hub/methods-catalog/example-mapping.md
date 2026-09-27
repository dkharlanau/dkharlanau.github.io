---
layout: default
title: "Example Mapping — Practical Requirement Clarification Method"
description: "Use Example Mapping to clarify a story through rules, concrete examples, open questions, and story splits before development."
permalink: /skill-hub/methods-catalog/example-mapping/
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
    <li aria-current="page">Example Mapping</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Methods Catalog — Requirement Discovery</p>
  <h1>Example Mapping</h1>
  <p class="lead">Use Example Mapping when a requirement sounds clear until someone asks “what happens when…?”. Concrete examples expose hidden rules and unanswered questions faster than more abstract prose.</p>

  <section>
    <h2>What this method is for</h2>
    <p>Example Mapping structures a short discovery conversation around four things: the <strong>story</strong>, the <strong>rules</strong> or acceptance criteria, concrete <strong>examples</strong> that illustrate each rule, and <strong>questions</strong> nobody can answer yet. The discussion can also reveal stories that should be split or deferred.</p>
    <p>It is especially useful before implementation or test design because examples can become the basis for acceptance scenarios.</p>
  </section>

  <section>
    <h2>When to use it</h2>
    <ul>
      <li>A user story contains words such as “valid,” “eligible,” “appropriate,” or “standard” without explicit rules.</li>
      <li>Developers and testers keep discovering edge cases during implementation.</li>
      <li>A business rule has exceptions that do not fit one sentence.</li>
      <li>A refinement meeting is long because people discuss different examples without naming the rule behind them.</li>
      <li>The team needs testable acceptance criteria, not another paragraph.</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Choose one story or requirement.</strong> Keep the scope small enough for a focused conversation.</li>
      <li><strong>Ask for the main rule.</strong> What condition determines expected behavior?</li>
      <li><strong>Ask for a concrete example.</strong> Use real values: customer type, country, amount, date, material, status.</li>
      <li><strong>Try to break the rule.</strong> Change one input and ask what should happen.</li>
      <li><strong>Capture unanswered questions immediately.</strong> Do not guess to keep the meeting moving.</li>
      <li><strong>Add more rules only when examples prove they are distinct.</strong></li>
      <li><strong>Split the story when the map grows too wide.</strong> A large map often signals multiple behaviors hiding in one backlog item.</li>
      <li><strong>Convert confirmed examples into acceptance criteria or test scenarios.</strong></li>
    </ol>
  </section>

  <section>
    <h2>SAP example — free freight rule</h2>
    <div class="table-scroll">
      <table class="study-table">
        <thead><tr><th>Type</th><th>Content</th></tr></thead>
        <tbody>
          <tr><td>Story</td><td>As Sales Operations, I want freight to be waived for eligible domestic orders.</td></tr>
          <tr><td>Rule</td><td>Standard domestic orders at or above 1,000 EUR receive free freight.</td></tr>
          <tr><td>Example</td><td>DE customer, standard order, net value 1,250 EUR → freight = 0.</td></tr>
          <tr><td>Example</td><td>DE customer, standard order, net value 900 EUR → standard freight applies.</td></tr>
          <tr><td>Question</td><td>Does the threshold use order net value before or after header discounts?</td></tr>
          <tr><td>Question</td><td>Are express deliveries excluded?</td></tr>
        </tbody>
      </table>
    </div>
    <p>The unanswered questions are more valuable than a premature “done” story because they expose pricing logic that could otherwise become a defect.</p>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a rule has no example, the team may not share the same interpretation.</li>
      <li>If examples contradict each other, the rule is incomplete or the domain language is inconsistent.</li>
      <li>If too many questions remain, the story is not ready for implementation.</li>
      <li>If one rule needs many independent behaviors, split the story or move complex logic to <a href="/skill-hub/methods-catalog/dmn-decision-tables/">DMN</a>.</li>
      <li>If examples are confirmed, feed them into <a href="/skill-hub/business-analysis/acceptance-criteria-working-skill/">Acceptance Criteria</a> and test design.</li>
    </ul>
  </section>

  <section>
    <h2>Copy-ready template</h2>
    <pre><code>## Story / Requirement
&lt;one focused behavior&gt;

### Rule 1
&lt;business rule / acceptance rule&gt;

Examples:
- Given &lt;concrete inputs&gt;, when &lt;event&gt;, then &lt;expected result&gt;
- Given &lt;changed input&gt;, when &lt;event&gt;, then &lt;expected result&gt;

Questions:
- ?
- ?

### Rule 2
...

## Story splits discovered
- &lt;separate behavior&gt;

## Ready?
- Rules confirmed:
- Questions unresolved:
- Examples converted to acceptance/test scenarios:</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The session covers one focused story or behavior.</li>
      <li>Rules are explicit.</li>
      <li>Examples use concrete values.</li>
      <li>At least one boundary or negative example is explored where relevant.</li>
      <li>Unanswered questions remain visible.</li>
      <li>Confirmed examples flow into acceptance criteria or tests.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Writing examples that just repeat the rule.</strong> Use real values that can reveal ambiguity.</li>
      <li><strong>Answering unknowns by assumption.</strong> Questions are an output, not a failure.</li>
      <li><strong>Running Example Mapping as a documentation task after development.</strong> Its main value is discovery before commitment.</li>
      <li><strong>Inviting only analysts.</strong> Business, development, and quality perspectives expose different cases.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>An AI agent should generate candidate examples only as prompts for review, never as accepted business facts. It should label each rule, example, and question separately and highlight contradictions or missing boundary cases.</p>
  </section>

  <section>
    <h2>Related skills and methods</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/acceptance-criteria-working-skill/">Acceptance Criteria</a></li>
      <li><a href="/skill-hub/business-analysis/user-story-refinement-working-skill/">User Story Refinement</a></li>
      <li><a href="/skill-hub/business-analysis/business-rules-discovery-working-skill/">Business Rules Discovery</a></li>
      <li><a href="/skill-hub/methods-catalog/dmn-decision-tables/">DMN Decision Tables</a></li>
    </ul>
  </section>

  <section>
    <h2>Reference and limitations</h2>
    <p><a href="https://cucumber.io/docs/bdd/example-mapping/">Cucumber</a> documents Example Mapping around a story, rules, examples, and questions. This page adapts the method to enterprise and SAP requirement analysis.</p>
  </section>
</article>