---
layout: default
title: "RACI Matrix — Practical Ownership Method"
description: "Use RACI to clarify who performs work, who is accountable for the result, who must be consulted, and who must be informed."
permalink: /skill-hub/methods-catalog/raci-matrix/
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
    <li aria-current="page">RACI Matrix</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Methods Catalog — Ownership</p>
  <h1>RACI Matrix</h1>
  <p class="lead">Use RACI when work crosses roles and the team needs a precise answer to four questions: who does it, who owns the result, who must give input, and who needs the outcome.</p>

  <section>
    <h2>What this method is for</h2>
    <p>RACI maps activities or deliverables against roles. <strong>R</strong> is Responsible: performs the work. <strong>A</strong> is Accountable: owns the result and accepts it. <strong>C</strong> is Consulted: provides input before the work or decision is complete. <strong>I</strong> is Informed: receives the result or status.</p>
    <p>Use it to remove ownership ambiguity. Do not use it as an org chart or as a replacement for process design.</p>
  </section>

  <section>
    <h2>When to use it</h2>
    <ul>
      <li>A process crosses Sales, Finance, Logistics, IT, and an external provider.</li>
      <li>Incidents move between teams because each team owns only part of the flow.</li>
      <li>A project has many approvers but no clear owner for the final deliverable.</li>
      <li>A business rule, interface, or master-data object has technical and business ownership.</li>
      <li>A handover fails because people assumed someone else would act.</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>List concrete activities or deliverables.</strong> Write “approve credit-limit change,” not “Credit Management.”</li>
      <li><strong>List roles, not names.</strong> Use Credit Manager, Sales Operations, SAP SD Lead, Integration Support.</li>
      <li><strong>Assign Responsible first.</strong> Ask who actually performs the work.</li>
      <li><strong>Assign one Accountable role where possible.</strong> Ask who has authority to accept the result and answer when it fails.</li>
      <li><strong>Add Consulted only when input can change the work.</strong> Do not make every stakeholder C.</li>
      <li><strong>Add Informed only when the result changes what that role needs to know or do.</strong></li>
      <li><strong>Review rows and columns.</strong> Rows reveal missing or overloaded ownership. Columns reveal roles with unrealistic involvement.</li>
      <li><strong>Test the matrix with a failure scenario.</strong> Ask: if this activity is not completed today, who acts and who answers for it?</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a row has no R, the work has no performer.</li>
      <li>If a row has no A, the result has no clear owner.</li>
      <li>If a row has several A roles, resolve approval authority instead of hiding the conflict in the matrix.</li>
      <li>If almost everyone is C, consultation is not selective enough.</li>
      <li>If the real problem is “who makes the decision?”, use <a href="/skill-hub/methods-catalog/daci/">DACI</a> instead of forcing RACI to model decision governance.</li>
      <li>If activities are still unclear, map the process first with <a href="/skill-hub/methods-catalog/sipoc/">SIPOC</a> or <a href="/skill-hub/methods-catalog/bpmn/">BPMN</a>.</li>
    </ul>
  </section>

  <section>
    <h2>SAP example — pricing condition change</h2>
    <div class="table-scroll">
      <table class="study-table">
        <thead>
          <tr><th>Activity</th><th>Sales Ops</th><th>Pricing Owner</th><th>SAP SD</th><th>Finance</th><th>Support</th></tr>
        </thead>
        <tbody>
          <tr><td>Define business rule</td><td>R</td><td>A</td><td>C</td><td>C</td><td>I</td></tr>
          <tr><td>Approve commercial impact</td><td>C</td><td>A/R</td><td>I</td><td>C</td><td>I</td></tr>
          <tr><td>Configure condition logic</td><td>C</td><td>A</td><td>R</td><td>I</td><td>I</td></tr>
          <tr><td>Validate regression</td><td>R</td><td>A</td><td>R</td><td>C</td><td>I</td></tr>
          <tr><td>Operate after go-live</td><td>C</td><td>A</td><td>C</td><td>I</td><td>R</td></tr>
        </tbody>
      </table>
    </div>
    <p>The matrix is useful because the role that configures the rule is not automatically the role accountable for the business outcome.</p>
  </section>

  <section>
    <h2>Copy-ready template</h2>
    <pre><code>| Activity / Deliverable | Role A | Role B | Role C | Role D | Evidence / Note |
|---|---|---|---|---|---|
| &lt;specific activity&gt; | R | A | C | I | &lt;ticket, policy, process step&gt; |
| &lt;specific activity&gt; |   | R | A | C | &lt;why this ownership is valid&gt; |

Legend:
R = Responsible — performs the work
A = Accountable — owns and accepts the result
C = Consulted — gives input before completion
I = Informed — receives result/status</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every row describes a specific action or deliverable.</li>
      <li>Every row has at least one R.</li>
      <li>Every important row has a clear A.</li>
      <li>Multiple A assignments are challenged, not accepted by default.</li>
      <li>C and I assignments have a reason.</li>
      <li>Business ownership is separated from technical execution where needed.</li>
      <li>The matrix has been validated by the people who actually perform the work.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mapping departments instead of work.</strong> The result looks complete but does not guide action.</li>
      <li><strong>Making the project manager Accountable for everything.</strong> This hides real business ownership.</li>
      <li><strong>Using RACI to settle authority conflicts silently.</strong> If two leaders both claim approval rights, the conflict needs an explicit decision.</li>
      <li><strong>Keeping an old RACI after the operating model changes.</strong> Ownership artifacts become dangerous when people trust obsolete assignments.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>An AI agent should extract activities and roles from verified process evidence, keep facts separate from proposed ownership, flag rows with missing or multiple accountable roles, and ask for confirmation before treating a proposed RACI as approved. Do not infer authority from job titles alone.</p>
  </section>

  <section>
    <h2>Related skills and methods</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/stakeholder-analysis-working-skill/">Stakeholder Analysis</a></li>
      <li><a href="/skill-hub/methods-catalog/daci/">DACI</a></li>
      <li><a href="/skill-hub/methods-catalog/stakeholder-power-interest-matrix/">Power–Interest Matrix</a></li>
      <li><a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis</a></li>
      <li><a href="/skill-hub/integration-architecture/interface-ownership-working-skill/">Interface Ownership</a></li>
    </ul>
  </section>

  <section>
    <h2>Reference and limitations</h2>
    <p>The <a href="https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/glossary/">IIBA BABOK glossary</a> defines the RACI matrix as a tool for identifying role responsibilities across activities or deliverables. This page is a practical working interpretation, not official IIBA guidance.</p>
  </section>
</article>