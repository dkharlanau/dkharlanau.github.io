---
layout: default
title: "C4 System Context — System Boundary Map"
description: "How to use the C4 System Context view to show people, software systems, external dependencies, and the boundary of the system in scope."
permalink: /skill-hub/tools-frameworks/c4-system-context/
last_modified_at: 2026-09-26
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/tools-frameworks/">Tools &amp; Frameworks</a></li><li aria-current="page">C4 System Context</li></ol></nav>
<article class="section note-detail atlas-page">
<p class="eyebrow">Architecture boundary tool</p><h1>C4 System Context</h1>
<p class="lead">Use a C4 System Context diagram when a team needs one simple answer: what system are we talking about, who uses it, what other systems does it depend on, and what is outside its boundary?</p>

<section><h2>What to show</h2><ul>
<li>The software system in scope.</li>
<li>People or roles that use it.</li>
<li>External software systems it interacts with.</li>
<li>Short relationship labels that explain why the connection exists.</li>
</ul></section>

<section><h2>What not to show yet</h2><ul>
<li>Internal services, modules, databases, classes, or deployment nodes.</li>
<li>Every interface field or protocol setting.</li>
<li>A legend full of technology detail that the audience does not need.</li>
</ul></section>

<section><h2>Working method</h2>
<ol>
<li>Name the system and its primary business purpose.</li>
<li>List the direct users or roles.</li>
<li>List systems that directly exchange information or trigger behavior.</li>
<li>Label each relationship with a business purpose, not only a protocol.</li>
<li>Mark uncertain ownership or boundaries as questions.</li>
<li>Validate the map with business, functional, integration, and operations participants.</li>
<li>Go deeper to container or component views only when the decision requires it.</li>
</ol></section>

<section><h2>SAP example</h2><p>For SAP S/4HANA Order-to-Cash, the context can show Sales Users, Customers, SAP S/4HANA, CRM or commerce channels, SAP Integration Suite, warehouse systems, tax services, and finance/reporting consumers. The diagram should explain the relationship purpose without becoming an interface inventory.</p></section>

<section><h2>Decision rules</h2><ul>
<li>If a stakeholder cannot tell what is inside versus outside the system, stay at context level.</li>
<li>If the question is message order or API behavior, pair the context view with a sequence diagram.</li>
<li>If a relationship has no owner, create an ownership action rather than hiding the gap.</li>
<li>If the diagram contains dozens of internal components, it is no longer a context diagram.</li>
</ul></section>

<section><h2>Pair it with</h2><ul>
<li><a href="/skill-hub/architecture/system-context-mapping-working-skill/">System Context Mapping</a></li>
<li><a href="/skill-hub/systems-analysis/interface-requirement-analysis-working-skill/">Interface Requirement Analysis</a></li>
<li><a href="/skill-hub/tools-frameworks/sequence-diagrams/">Sequence Diagrams</a></li>
<li><a href="/skill-hub/integration-architecture/interface-ownership-working-skill/">Interface Ownership</a></li>
</ul></section>

<section><h2>Reference</h2><ul><li><a href="https://c4model.com/">C4 model — official site</a></li></ul></section>
<section><h2>Verification status and limitations</h2><p>This page focuses on the System Context level of C4. It does not replace detailed solution, deployment, security, or interface design.</p></section>
</article>
