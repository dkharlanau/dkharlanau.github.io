---
layout: default
title: "RACI — Responsibility Assignment Matrix"
description: "How to use RACI to clarify who performs work, who owns the outcome, who must be consulted, and who only needs information."
permalink: /skill-hub/tools-frameworks/raci/
last_modified_at: 2026-09-26
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/tools-frameworks/">Tools &amp; Frameworks</a></li><li aria-current="page">RACI</li></ol></nav>
<article class="section note-detail atlas-page">
<p class="eyebrow">Ownership tool</p><h1>RACI</h1>
<p class="lead">Use RACI when delivery ownership is unclear. It maps work items to four participation types: Responsible, Accountable, Consulted, and Informed.</p>

<section><h2>What problem it solves</h2>
<p>Teams often know the org chart but still do not know who owns a process step, data correction, approval, test, or release task. RACI turns that ambiguity into a visible matrix.</p>
</section>

<section><h2>Use it when</h2><ul>
<li>Two teams both think the other team owns a task.</li>
<li>A cross-functional SAP process has hand-offs between business, functional, development, integration, and operations teams.</li>
<li>A deliverable receives many reviews but nobody is accountable for accepting it.</li>
<li>An incident repeatedly stalls because the resolver and the decision owner are different roles.</li>
</ul></section>

<section><h2>Do not use it when</h2><ul>
<li>You need to clarify <em>who makes a decision</em>. Use DACI or RAPID instead.</li>
<li>The process itself is unclear. Map the process first; then assign ownership.</li>
<li>You are using named people where stable roles would be better.</li>
</ul></section>

<section><h2>How to build a useful RACI</h2>
<ol>
<li>List concrete work items or deliverables in rows. Avoid vague rows such as “support” or “governance”.</li>
<li>List stable roles in columns.</li>
<li>Assign at least one Responsible role to each work item.</li>
<li>Assign one clear Accountable role where possible. If two roles both believe they are accountable, treat that as a governance issue to resolve.</li>
<li>Add Consulted roles only when two-way input is required before the work is complete.</li>
<li>Add Informed roles only when they need the result but do not shape it.</li>
<li>Review empty rows, overloaded roles, and rows with too many Consulted roles.</li>
</ol></section>

<section><h2>Decision rules</h2><ul>
<li>If nobody can approve or accept the outcome, the row has no effective Accountable owner.</li>
<li>If almost every role is Consulted, the matrix is hiding a decision problem.</li>
<li>If one role is Responsible for nearly everything, test whether the process is under-designed or the role is overloaded.</li>
<li>If the row describes a decision rather than work, switch to a decision-rights model.</li>
</ul></section>

<section><h2>SAP example</h2>
<p>For a customer master change: Master Data Operations may be Responsible for maintaining the record, Sales Operations Accountable for the commercial correctness of sales-area data, Finance Consulted for payment terms, and the integration team Informed when the change affects downstream replication.</p>
</section>

<section><h2>Copyable template</h2>
<pre><code>| Work item | Sales | SAP Functional | Integration | Data | Operations |
|---|---|---|---|---|---|
| Confirm business requirement | A | R | C | C | I |
| Configure change | C | A/R | I | I | I |
| Validate replication | I | C | A/R | C | C |
| Approve production result | A | R | C | C | I |</code></pre>
</section>

<section><h2>Pair it with</h2><ul>
<li><a href="/skill-hub/business-analysis/stakeholder-analysis-working-skill/">Stakeholder Analysis</a></li>
<li><a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis</a></li>
<li><a href="/skill-hub/tools-frameworks/decision-rights-daci-rapid/">DACI / RAPID</a> for decision ownership</li>
</ul></section>

<section><h2>References</h2><ul>
<li><a href="https://it.cornell.edu/it-service-management/raci-and-rasci-definitions">Cornell University — RACI and RASCI definitions</a></li>
<li><a href="https://www.projectmanagement.com/wikis/234008/raci">ProjectManagement.com — RACI</a></li>
</ul></section>

<section><h2>Verification status and limitations</h2><p>This is a practical working interpretation. RACI has many variants. The important point is not the letters; it is explicit ownership tied to real work.</p></section>
</article>
