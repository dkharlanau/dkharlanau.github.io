---
layout: default
title: "Operate the Architecture You Designed — SAP Architect Field Course"
description: "Make resilience, security, observability, ownership, and cost part of SAP architecture from the beginning."
permalink: /skill-hub/sap-architecture-course/operations-security-resilience/
last_modified_at: 2026-07-31
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
sap_architecture_course: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/sap-architecture-course/">SAP Architect Field Course</a></li><li aria-current="page">Operations, security, resilience</li></ol></nav>

<article class="course-bite">
  <header><p class="eyebrow">05 / Operate</p><h1>Operate the architecture you designed.</h1><p class="lead">A design is not complete because it works in a demo. It is complete when a reasonable operations team can see it, control it, recover it, and explain its cost.</p></header>

  <section><h2>Architecture meets reality after the happy path</h2><p>Production does not care whether a diagram looked clean. It introduces credentials that expire, queues that back up, users who change roles, data that arrives late, third parties that are unavailable, and month-end volume that was never in the sample file.</p><p>Operations and security are not a final review lane. They are design constraints. Ask the service desk, security owner, and process owner what they need to respond well before you decide how the solution is assembled.</p></section>

  <section><h2>Design for four kinds of evidence</h2><h3>Business evidence</h3><p>Can support identify the affected order, partner, document, or process step without decoding a technical trace first?</p><h3>Technical evidence</h3><p>Can the team follow the request, message, job, or event across the boundary with timestamps and correlation IDs?</p><h3>Control evidence</h3><p>Can an auditor or owner understand who accessed what, which automated action occurred, and under which approval?</p><h3>Cost evidence</h3><p>Can the team see the consumption, storage, traffic, or support workload that the design introduces before it becomes a surprise?</p>
  <aside class="course-bite__checkpoint"><h3>Practical test</h3><p>Give a support analyst one believable failure and fifteen minutes. If the design provides no route from business symptom to technical evidence, observability is not finished.</p></aside></section>

  <section><h2>Resilience is business-specific</h2><p>Do not ask whether the solution is “highly available.” Ask which business capability can pause, for how long, and what the safe fallback is. A reporting delay may be tolerable. A legal posting path or critical warehouse confirmation may not be. Design the recovery objective around the process, not around an adjective.</p><p>Useful resilience design includes a failure mode, a temporary operating mode, a reconciliation point, and a person or service responsible for recovery. Redundancy without recovery procedure is mostly expensive optimism.</p><div class="course-bite__artifact"><h3>Operational readiness card</h3><pre><code>Critical business capability: [what must continue]
Allowed interruption: [time + business reason]
Failure signals: [what alerts, who sees them]
Safe fallback: [manual/queued/degraded behaviour]
Recovery and reconciliation: [steps + evidence]
Access model: [human/service identity + least privilege]
Runbook owner: [role]
Cost watch: [usage or support measure]
Review trigger: [when this design must be revisited]</code></pre></div></section>

  <section><h2>Security belongs in the flow</h2><p>Architecture security is more than a list of controls. Identity tells the system who is acting. Authorisation tells it what that actor may do. Secrets, network paths, retention, and auditability determine whether the flow remains controlled when it leaves the diagram.</p><p>Keep service identities separate from people. Do not share technical users as a workaround. Limit access by purpose. And for AI or automation, be explicit about whether the system may read, recommend, draft, execute, or approve. These are different permission levels, not implementation details.</p></section>

  <section><h2>Finish strong: review it in a room</h2><p>Now you have enough material for an actual architecture conversation: system boundary, integration contract, data product, extension decision, and operational readiness. The capstone gives you a short way to present it, pressure-test it, and leave with decisions instead of vague action items.</p><p class="course-bite__links"><a href="/skill-hub/sap-architecture-course/architecture-room/">Continue: Run the architecture room</a><br><a href="/skill-hub/integration-architecture/integration-observability-working-skill/">Deepen the skill: Integration Observability</a><br><a href="/skill-hub/architecture/non-functional-requirements-working-skill/">Deepen the skill: Non-Functional Requirements</a></p><p class="course-source">Independent course material informed by public SAP Architecture Center operations, security, identity, and resiliency references. It is not a security assessment or a product configuration guide.</p></section>

  {% include atlas/author-block.html %}
</article>
