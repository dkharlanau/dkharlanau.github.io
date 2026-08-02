---
layout: default
title: "Think in Systems, Not Boxes — SAP Architect Field Course"
description: "Start architecture work with a business moment, a system boundary, and an evidence trail instead of a product list."
permalink: /skill-hub/sap-architecture-course/system-mindset/
last_modified_at: 2026-07-31
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
sap_architecture_course: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/sap-architecture-course/">SAP Architect Field Course</a></li><li aria-current="page">Think in systems</li></ol></nav>

<article class="course-bite">
  <header><p class="eyebrow">01 / Foundation</p><h1>Think in systems, not boxes.</h1><p class="lead">Architecture begins when you stop asking “Which product do we need?” and start asking “What must happen, who owns the decision, and what changes when it goes wrong?”</p></header>

  <section><h2>The move that changes the whole conversation</h2><p>A system is not its application diagram. It is the arrangement that gets a business outcome from one reliable state to another. A sales order becomes releasable. A supplier becomes usable. Stock becomes available to promise. A support analyst can explain why an invoice did not post.</p><p>That sounds obvious, but projects often start one level too low. Somebody brings a product, a platform choice, or a preferred pattern into the room before the team has agreed on the business moment. The result is a diagram with beautiful arrows and no owner for the uncomfortable bit: the decision.</p><p>Your first job as an architect is to pull the conversation back up. Give the system a clear job. Then draw the edge around what it owns. Everything outside that edge is a dependency, not a vague “integration.”</p></section>

  <section><h2>Use a four-question opening</h2><ol><li><strong>What is the moment?</strong> State the business trigger in plain language: “A buyer approves a purchase request” is better than “P2P integration.”</li><li><strong>What state changes?</strong> Name the before and after. If no state changes, you may be looking at a report, notification, or query—not a transaction.</li><li><strong>Who owns the decision?</strong> One system or role must be authoritative for a state. “Everybody updates it” is an early warning sign.</li><li><strong>What happens when the path breaks?</strong> The answer reveals whether the design is operational or only presentable.</li></ol>
  <aside class="course-bite__checkpoint"><h3>Field test</h3><p>If the team cannot describe a failure in a normal sentence, do not accept a solution yet. “The middleware has an error” is not a business impact. “A confirmed delivery was not created, so the warehouse never saw the request” is.</p></aside></section>

  <section><h2>Draw the boundary before the landscape</h2><p>For each system, write one sentence beginning with “This system owns…”. Good answers are specific: pricing determination, customer master approval, shipment visibility, the legal accounting document, the canonical employee identity. Weak answers are product names or vague platform roles.</p><p>Then make an honest dependency list. A dependency is not just an API. It can be a master-data rule, an identity provider, a batch window, a manual approval, a shared code table, or a third-party SLA.</p>
  <div class="course-bite__artifact"><h3>Your first architecture card</h3><pre><code>Business moment: [what just happened?]
State change: [before] → [after]
Decision owner: [system / role]
Inputs it trusts: [data + source]
Outputs it creates: [event, document, status]
Dependencies: [systems, people, time windows]
Failure behaviour: [what waits, retries, stops, or escalates?]
Evidence to collect: [IDs, timestamps, status, logs]</code></pre></div></section>

  <section><h2>Do not confuse a context map with a component diagram</h2><p>A context map is deliberately boring. It is for agreeing responsibility. Use it when you need business and technology people to point at the same boundary. A component diagram comes later, once you need to show how a chosen solution is built.</p><p>In SAP work this distinction matters because the landscape is already crowded. S/4HANA, BTP services, middleware, data platforms, partner applications, and local tools can quickly become a wallpaper of logos. Logos are not architecture. Ownership, states, and contracts are.</p><p>When someone adds a box, ask what it owns. If the answer is “it helps,” ask what would stop working if it disappeared. That usually exposes whether it is a necessary capability, a technical convenience, or a duplicated function.</p></section>

  <section><h2>The questions that make you sound like an architect</h2><ul><li>Which team has the right to say this record is valid?</li><li>What data is copied here, and what data is merely read?</li><li>Can the process continue when the receiving system is unavailable?</li><li>What is the smallest evidence set needed to explain a bad outcome?</li><li>What decision is expensive to reverse after go-live?</li><li>Which behaviour is policy, and which is only an implementation accident?</li></ul></section>

  <section><h2>What to take into the next module</h2><p>Bring one real business moment and its architecture card. In the integration module, you will decide which messages cross the boundary, when they need an answer, and who has to recover when they do not arrive.</p><p class="course-bite__links"><a href="/skill-hub/sap-architecture-course/integration/">Continue: Make integration carry its own weight</a><br><a href="/skill-hub/architecture/system-context-mapping-working-skill/">Deepen the skill: System Context Mapping</a></p><p class="course-source">This independent module is informed by SAP Architecture Center material on reference architectures and architecture modelling. Check your own landscape and official SAP documentation before treating any pattern as a product prescription.</p></section>

  {% include atlas/author-block.html %}
</article>
