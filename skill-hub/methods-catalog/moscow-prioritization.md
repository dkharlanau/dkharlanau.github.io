---
layout: default
title: "MoSCoW Prioritization — Practical Scope Trade-off Method"
description: "Use MoSCoW to separate Must, Should, Could, and Won't Have this time and protect delivery from false priority inflation."
permalink: /skill-hub/methods-catalog/moscow-prioritization/
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
    <li aria-current="page">MoSCoW Prioritization</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Methods Catalog — Prioritization</p>
  <h1>MoSCoW Prioritization</h1>
  <p class="lead">Use MoSCoW when a fixed delivery window needs real trade-offs. The method fails if “Must” means “important” instead of “the outcome fails without it.”</p>

  <section>
    <h2>What this method is for</h2>
    <p>MoSCoW groups work into <strong>Must Have, Should Have, Could Have, and Won’t Have this time</strong>. Its value is not four labels. Its value is forcing the team to define a viable minimum and preserve contingency instead of treating all scope as fixed.</p>
  </section>

  <section>
    <h2>Practical meaning of each class</h2>
    <div class="table-scroll">
      <table class="study-table">
        <thead><tr><th>Class</th><th>Practical test</th><th>What to record</th></tr></thead>
        <tbody>
          <tr><td>Must Have</td><td>If missing, the agreed outcome, compliance, safety, or usable solution fails</td><td>Failure consequence</td></tr>
          <tr><td>Should Have</td><td>Important, but a temporary workaround or reduced outcome exists</td><td>Workaround and cost</td></tr>
          <tr><td>Could Have</td><td>Useful improvement that can be dropped without breaking the core outcome</td><td>Value if capacity remains</td></tr>
          <tr><td>Won’t Have this time</td><td>Explicitly outside this delivery window</td><td>Reason and possible revisit point</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Fix the time horizon.</strong> Priority without “for when?” becomes meaningless.</li>
      <li><strong>State the minimum usable outcome.</strong> What must be true at the end of the increment, release, or cutover?</li>
      <li><strong>Start by challenging Musts.</strong> Ask what happens if this item is missing on deployment day.</li>
      <li><strong>Separate compliance or technical dependency from preference.</strong> A required control may be Must even if users never see it.</li>
      <li><strong>Record workarounds for Shoulds.</strong> This proves the solution can still operate without the item for a limited period.</li>
      <li><strong>Keep a real Could pool.</strong> It creates delivery flexibility instead of pretending the entire scope is guaranteed.</li>
      <li><strong>Use Won’t Have actively.</strong> It is a scope boundary, not a graveyard.</li>
      <li><strong>Review effort balance.</strong> If almost all effort is Must, the method has not created real contingency.</li>
    </ol>
  </section>

  <section>
    <h2>SAP example — S/4 sales rollout</h2>
    <ul>
      <li><strong>Must:</strong> create, deliver, bill, and post the agreed core order types; legal tax calculation; required customer/master-data controls.</li>
      <li><strong>Should:</strong> automated approval for a low-volume exception where a governed manual approval can temporarily work.</li>
      <li><strong>Could:</strong> advanced dashboard for a KPI already available from an existing report.</li>
      <li><strong>Won’t this time:</strong> rare sales scenario for a region planned in wave 2.</li>
    </ul>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the stakeholder cannot state what fails without an item, it is not yet proven to be Must.</li>
      <li>If a workaround exists but creates unacceptable legal, safety, or operational risk, the item may still be Must.</li>
      <li>If every item is Must, split requirements or challenge the release boundary.</li>
      <li>If an item has no clear outcome value, use <a href="/skill-hub/methods-catalog/impact-mapping/">Impact Mapping</a> before prioritizing it.</li>
      <li>If priorities change, record why. Silent category changes destroy trust.</li>
    </ul>
  </section>

  <section>
    <h2>Copy-ready template</h2>
    <pre><code>| Item | Priority | Why | What fails if absent? | Workaround | Effort | Dependency | Revisit |
|---|---|---|---|---|---:|---|---|
| &lt;requirement&gt; | Must | ... | ... | none | ... | ... | ... |
| &lt;requirement&gt; | Should | ... | ... | &lt;temporary workaround&gt; | ... | ... | ... |
| &lt;requirement&gt; | Could | ... | ... | current process | ... | ... | ... |
| &lt;requirement&gt; | Won't this time | ... | nothing in this release | n/a | ... | ... | &lt;wave/date&gt; |</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The delivery horizon is explicit.</li>
      <li>Every Must has a failure consequence.</li>
      <li>Should items have a realistic temporary workaround where relevant.</li>
      <li>Could items create real contingency.</li>
      <li>Won’t Have is used to protect scope.</li>
      <li>Priorities are tied to outcomes, controls, risk, or dependencies rather than stakeholder volume.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Using Must for “very important.”</strong> Priority inflation removes the mechanism that protects delivery.</li>
      <li><strong>Prioritizing before requirements are understood.</strong> A vague item can hide several different priorities.</li>
      <li><strong>Ignoring effort.</strong> A list of labels without capacity context is not a release strategy.</li>
      <li><strong>Treating Won’t as rejected forever.</strong> The method is explicitly time-boxed.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>An AI agent should ask for the delivery horizon and minimum usable outcome before assigning categories. It should challenge each proposed Must with a failure test and keep recommendations separate from stakeholder-approved priority.</p>
  </section>

  <section>
    <h2>Related skills and methods</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/scope-boundary-definition-working-skill/">Scope Boundary Definition</a></li>
      <li><a href="/skill-hub/business-analysis/user-story-refinement-working-skill/">User Story Refinement</a></li>
      <li><a href="/skill-hub/methods-catalog/impact-mapping/">Impact Mapping</a></li>
      <li><a href="/skill-hub/methods-catalog/user-story-mapping/">User Story Mapping</a></li>
    </ul>
  </section>

  <section>
    <h2>Reference and limitations</h2>
    <p>The <a href="https://www.agilebusiness.org/resource/what-is-moscow-prioritization/">Agile Business Consortium</a> describes MoSCoW as Must Have, Should Have, Could Have, and Won’t Have this time, and stresses balancing priorities to keep delivery predictable. This page focuses on practical use in enterprise delivery.</p>
  </section>
</article>