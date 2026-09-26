---
layout: default
title: "Example Mapping — Rules, Examples, Questions"
description: "How to use Example Mapping to refine a story by separating rules, concrete examples, and unresolved questions."
permalink: /skill-hub/tools-frameworks/example-mapping/
last_modified_at: 2026-09-26
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/tools-frameworks/">Tools &amp; Frameworks</a></li><li aria-current="page">Example Mapping</li></ol></nav>
<article class="section note-detail atlas-page">
<p class="eyebrow">Requirements refinement tool</p><h1>Example Mapping</h1>
<p class="lead">Use Example Mapping when a requirement sounds clear until people try to test it. It separates the story, the business rules, concrete examples, and questions that still block understanding.</p>

<section><h2>The four parts</h2>
<table class="study-table"><thead><tr><th>Part</th><th>Purpose</th></tr></thead><tbody>
<tr><td>Story</td><td>The capability or outcome being discussed.</td></tr>
<tr><td>Rule</td><td>A business condition that constrains the story.</td></tr>
<tr><td>Example</td><td>A concrete case showing how the rule behaves.</td></tr>
<tr><td>Question</td><td>An unresolved point that requires a decision or evidence.</td></tr>
</tbody></table>
</section>

<section><h2>Working method</h2>
<ol>
<li>Take one story or requirement.</li>
<li>Ask which rules determine correct behavior.</li>
<li>For each rule, create at least one concrete example with actual values or conditions.</li>
<li>Add boundary and failure examples.</li>
<li>Capture every disagreement as a question instead of hiding it in wording.</li>
<li>Stop refinement when the examples are sufficient to write testable acceptance criteria.</li>
</ol></section>

<section><h2>SAP example</h2><p>Story: “Prevent delivery when the customer is over the credit limit.” Rule: “A blocked order cannot create a delivery until released.” Example: customer exposure is 105,000 EUR against a 100,000 EUR limit; order is blocked; credit manager releases it; delivery becomes possible. Question: does an emergency override exist, and who owns it?</p></section>

<section><h2>Decision rules</h2><ul>
<li>If a rule has no example, the team may not understand the rule precisely enough.</li>
<li>If examples contradict each other, do not average them into vague wording. Resolve the rule.</li>
<li>If there are many interacting rules, move them into a decision table or DMN model.</li>
<li>If questions dominate the session, the story is not ready for implementation.</li>
</ul></section>

<section><h2>Copyable template</h2>
<pre><code>Story:
Rule 1:
- Example:
- Boundary example:
- Failure example:

Rule 2:
- Example:

Questions:
- ?
- ?

Ready when:
- rules are explicit
- examples are testable
- material questions have owners</code></pre></section>

<section><h2>Pair it with</h2><ul>
<li><a href="/skill-hub/business-analysis/acceptance-criteria-working-skill/">Acceptance Criteria</a></li>
<li><a href="/skill-hub/business-analysis/business-rules-discovery-working-skill/">Business Rules Discovery</a></li>
<li><a href="/skill-hub/tools-frameworks/dmn-decision-tables/">DMN &amp; Decision Tables</a></li>
</ul></section>

<section><h2>Reference</h2><ul><li><a href="https://cucumber.io/docs/bdd/example-mapping/">Cucumber — Example Mapping</a></li></ul></section>
<section><h2>Verification status and limitations</h2><p>Example Mapping is a refinement technique, not a full requirements method. It works best on a bounded story or rule set.</p></section>
</article>
