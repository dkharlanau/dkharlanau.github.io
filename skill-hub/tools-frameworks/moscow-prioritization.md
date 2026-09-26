---
layout: default
title: "MoSCoW — Scope Prioritization Under a Fixed Constraint"
description: "How to use Must, Should, Could, and Won't to make scope choices explicit without turning every request into a Must."
permalink: /skill-hub/tools-frameworks/moscow-prioritization/
last_modified_at: 2026-09-26
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/tools-frameworks/">Tools &amp; Frameworks</a></li><li aria-current="page">MoSCoW</li></ol></nav>
<article class="section note-detail atlas-page">
<p class="eyebrow">Prioritization tool</p><h1>MoSCoW</h1>
<p class="lead">Use MoSCoW when a team must make scope choices for a specific timebox, release, or delivery constraint. The technique is useful only when “Must” has a hard definition and “Won't” is an explicit current decision, not a polite parking lot.</p>

<section><h2>The categories</h2>
<table class="study-table"><thead><tr><th>Category</th><th>Working definition</th></tr></thead><tbody>
<tr><td>Must</td><td>Without it, the target outcome or release is not viable.</td></tr>
<tr><td>Should</td><td>Important and high value, but a temporary workaround or later delivery is acceptable.</td></tr>
<tr><td>Could</td><td>Useful if capacity remains after stronger priorities.</td></tr>
<tr><td>Won't this time</td><td>Explicitly outside this scope or timebox.</td></tr>
</tbody></table>
</section>

<section><h2>Working method</h2>
<ol>
<li>Name the decision boundary: release, sprint, phase, or cutover.</li>
<li>Agree the test for “Must” before classifying anything.</li>
<li>Classify items using business outcome, dependency, compliance, risk, and workaround evidence.</li>
<li>Challenge every Must: what exactly fails if it is absent?</li>
<li>Make the Won't list visible.</li>
<li>Check whether the Must set fits the available constraint. If not, the prioritization is not finished.</li>
</ol></section>

<section><h2>SAP example</h2><p>For an initial rollout, legal invoice output may be Must, a specialized sales dashboard Should, automated exception classification Could, and a low-volume legacy variant Won't for this release. The classification depends on the release outcome and constraints, not on permanent product value.</p></section>

<section><h2>Decision rules</h2><ul>
<li>If everything is Must, nothing has been prioritized.</li>
<li>If a Must has a safe workaround, challenge whether it is really Should.</li>
<li>If an item is a prerequisite for another Must, include that dependency in the reasoning.</li>
<li>If value and effort need continuous ranking rather than categories, use a different prioritization model.</li>
</ul></section>

<section><h2>Pair it with</h2><ul>
<li><a href="/skill-hub/business-analysis/scope-boundary-definition-working-skill/">Scope Boundary Definition</a></li>
<li><a href="/skill-hub/tools-frameworks/impact-mapping/">Impact Mapping</a></li>
<li><a href="/skill-hub/tools-frameworks/user-story-mapping/">User Story Mapping</a></li>
<li><a href="/skill-hub/productivity-execution-control/priority-triage-working-skill/">Priority Triage</a></li>
</ul></section>

<section><h2>Reference</h2><ul><li><a href="https://www.agilebusiness.org/resource/what-is-moscow-prioritization.html">Agile Business Consortium — MoSCoW prioritization</a></li></ul></section>
<section><h2>Verification status and limitations</h2><p>MoSCoW is a categorical scope technique. It should not be treated as a universal portfolio scoring model.</p></section>
</article>
