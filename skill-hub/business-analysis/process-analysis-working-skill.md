---
layout: default
title: "Process Analysis Working Skill"
description: "Document how work actually happens, where it breaks, what systems touch it, and who owns each step — not how it is supposed to happen."
permalink: /skill-hub/business-analysis/process-analysis-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/business-analysis/">Business Analysis</a></li>
    <li aria-current="page">Process Analysis</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Business Analysis</p>
  <h1>Process Analysis Working Skill</h1>
  <p class="lead">Map how work actually happens, where it breaks, and who owns each step — so improvements fix reality, not documentation.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Process documentation in most organizations describes an ideal state that no one follows. This skill documents the real process: the workarounds, the manual fixes, the system hops, the approval delays, and the exception paths. The output is a Process Analysis Note that shows what to fix, what to automate, and what to leave alone. It prevents the common failure where a redesign optimizes a process that does not exist.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A project needs a baseline "as-is" process before designing the "to-be" state.</li>
      <li>An incident recurs and the post-mortem shows the process has undocumented exception paths.</li>
      <li>An automation opportunity is identified but no one knows the full sequence of manual steps.</li>
      <li>A team is being handed over to another team and operational knowledge is scattered.</li>
      <li>A compliance audit asks for process documentation and the existing diagrams are three years old.</li>
      <li>An integration failure spans multiple process steps and each team only knows their own piece.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>Order-to-cash: orders block at credit check</h3>
    <p>A sales team reports that orders block unpredictably at credit check. The documented process says credit limit is checked at order creation. The real process shows: some customers have special agreements bypassing credit check, the credit controller updates limits weekly in a spreadsheet before entering them in SAP, and rush orders are created by a different team using a different transaction. Without mapping the real process, any credit management redesign breaks these workarounds and increases blocks.</p>

    <h3>Purchase-to-pay: invoices sit unposted</h3>
    <p>Accounts payable says invoices take weeks to post. The documented process says: receive invoice, match to PO, post. The real process shows: invoices arrive by email to a shared mailbox, a clerk prints and stamps them, another clerk enters header data, a third checks GR status in a separate system, discrepancies are escalated via instant message to a buyer who may be on vacation, and only then is the invoice posted. The bottleneck is not the posting transaction — it is the handoff between clerk and buyer.</p>

    <h3>Master data change: updates take three days</h3>
    <p>A business unit complains that customer master data changes take three days to propagate. The documented process says: request, approve, update, replicate. The real process shows: requests are sent by email to a data steward who works part-time, approval requires a signature from a manager who is rarely at their desk, updates are batched and run overnight, replication to CRM is manual because the interface broke six months ago and no one fixed it. The fix is not faster replication — it is fixing the broken interface and redesigning the approval handoff.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>System transaction logs or audit trails showing actual user activity.</li>
      <li>User interviews with people who perform each step, not just managers who oversee them.</li>
      <li>Existing process documentation (to be verified, not trusted).</li>
      <li>Incident tickets showing where the process breaks and how it is recovered.</li>
      <li>Screen recordings or live walkthroughs of the actual execution.</li>
      <li>IDoc, API, or integration flow logs if the process spans systems.</li>
      <li><a href="/skill-hub/business-analysis/stakeholder-analysis-working-skill/">Stakeholder Analysis</a> to know who to interview.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the first screen, transaction, or document used to start this process?</li>
      <li>What data is entered manually and what is populated automatically?</li>
      <li>Where does the process wait for someone else, and how long does that wait typically last?</li>
      <li>Which step has no clear owner, or has an owner who is unaware they own it?</li>
      <li>What is the longest wait time, and what causes it?</li>
      <li>Where do errors get caught today, and who fixes them?</li>
      <li>What do you do when the system does not let you proceed as documented?</li>
      <li>Which steps exist only to fix problems created by earlier steps?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Identify the process trigger and end state.</strong> What event starts it? What condition means it is complete? Be specific: "customer sends PO" not "order process starts."</li>
      <li><strong>Walk through actual execution with a user.</strong> Ask them to show you the real screens, not the training material. Record the sequence.</li>
      <li><strong>Record each step with actor, system, input, output, and duration.</strong> Use a table. Do not skip "obvious" steps like "save draft" or "check email."</li>
      <li><strong>Mark variations and exceptions.</strong> Ask: what happens if the customer is new? What happens if the amount is over a threshold? What happens on Friday afternoon?</li>
      <li><strong>Identify pain points with evidence.</strong> Do not record "slow" — record "takes 20 minutes because the search helps do not filter by date."</li>
      <li><strong>Map data flows between systems.</strong> Which fields move where? Which system is the source of truth for each field?</li>
      <li><strong>Verify ownership of each step.</strong> Ask who can change the step, not just who performs it. Check system roles if needed.</li>
      <li><strong>Document in a Process Analysis Note.</strong> Include trigger, steps, variations, pain points, system touchpoints, data flows, and ownership.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If process documentation contradicts actual execution, trust the execution and flag the documentation as outdated.</li>
      <li>If a step has no owner, stop and identify the owner before proposing any change to that step.</li>
      <li>If a step exists only to fix errors from an earlier step, the earlier step is the real problem.</li>
      <li>If two systems exchange data manually (email, spreadsheet, rekeying), that is an integration gap, not a process step.</li>
      <li>If duration data is unavailable, estimate from user memory and flag as unverified.</li>
      <li>If a variation happens more than 20 percent of the time, it is not an exception — it is part of the process.</li>
      <li>If a pain point has no evidence (no timing, no frequency, no ticket count), treat it as unverified opinion.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Process Analysis Note</strong> — Structured document with trigger, steps, variations, pain points, system touchpoints, data flows, and ownership. See template below.</li>
      <li><strong>As-Is Process Map</strong> — Visual or tabular representation of the process with exception paths.</li>
      <li><strong>Pain Point Register</strong> — Table of pain points with evidence, frequency, impact, and proposed improvement.</li>
      <li><strong>System Touchpoint Matrix</strong> — Which systems are involved, what data moves where, and integration gaps.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Process Analysis Note (compact)</h3>
    <pre><code>---
artifact: Process Analysis Note
id: PAN-001
date: YYYY-MM-DD
process: Name
scope: As-is | To-be | Gap
---

## Process name and trigger
<!-- What starts this process? Example: "Customer purchase order received via EDI." -->

## Steps
<!-- Numbered list of steps with actor and system -->

| Step | Actor | System | Action | Input | Output | Duration | Issues |
|------|-------|--------|--------|-------|--------|----------|--------|
| 1 | Clerk | SAP | Create sales order | Customer PO | Order | 5 min | Manual entry |

## Variations
<!-- Exceptions, escalations, alternative paths. Example: "If customer is new, route to credit team before order creation." -->

## Pain points
<!-- Where the process fails, slows, or frustrates. Include evidence. -->

## System touchpoints
<!-- Which systems are involved and how they connect -->

## Data flows
<!-- What data moves where. Example: "Customer number from SAP to CRM via IDoc." -->

## Ownership
<!-- Who owns the process end-to-end -->

## Improvement opportunities
<!-- Specific, actionable improvements with effort estimate -->

## Related processes
<!-- Links to other process analysis notes -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every step has an identified actor and system.</li>
      <li>Process trigger and end state are explicitly defined.</li>
      <li>Variations and exceptions are documented, not ignored.</li>
      <li>Pain points have evidence: timing, frequency, ticket count, or user quote.</li>
      <li>Data flows between systems are mapped with field-level detail where possible.</li>
      <li>Ownership is verified, not assumed from job titles.</li>
      <li>Duration is either measured or estimated with a confidence flag.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Documenting the ideal process instead of the real one.</strong> Consequence: improvements fail because they ignore actual workarounds that users depend on.</li>
      <li><strong>Skipping exception paths.</strong> Consequence: automation or redesign breaks on edge cases that happen weekly.</li>
      <li><strong>Not mapping data flows.</strong> Consequence: system changes break downstream processes because field mappings were assumed.</li>
      <li><strong>Assuming documented process is current.</strong> Consequence: decisions are based on fiction. The redesign optimizes a process abandoned two years ago.</li>
      <li><strong>Interviewing only managers.</strong> Consequence: missing the workarounds, keyboard shortcuts, and manual fixes that operators use daily.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>AI agents should use this skill to document real processes before making any recommendation about change, automation, or integration.</p>
    <ul>
      <li><strong>Always start with a real transaction or incident,</strong> not a diagram or document. Ask users to show you the actual screens they use.</li>
      <li><strong>Record exceptions and workarounds as primary process steps,</strong> not footnotes. If a workaround happens daily, it is the process.</li>
      <li><strong>Map data flows explicitly</strong> — which fields move between which systems, and which system is the source of truth.</li>
      <li><strong>Verify ownership by asking who can change the step,</strong> not just who performs it. Check system roles if available.</li>
      <li><strong>Produce a Process Analysis Note.</strong> If documentation contradicts reality, document reality and flag the documentation gap.</li>
      <li><strong>Link to Atlas diagnostics</strong> when process gaps relate to SAP. For example, O2C process blocks should reference <a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a>.</li>
      <li><strong>Do not optimize a process you have not observed.</strong> If you only have documentation, state that the analysis is unverified.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/gap-analysis-working-skill/">Gap Analysis Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/stakeholder-analysis-working-skill/">Stakeholder Analysis Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/business-rules-discovery-working-skill/">Business Rules Discovery Working Skill</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/order-to-cash/">Order-to-Cash</a> — Process context for O2C analysis.</li>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — Diagnostic patterns for SAP process review.</li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a> — Specific O2C block analysis.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of process analysis practices. It is not official BPMN, Six Sigma, or SAP documentation. It focuses on operational reality in enterprise systems and may not cover highly regulated or safety-critical process domains.</p>
    <p>Known limitations: the skill assumes access to users who can demonstrate the process. In remote or outsourced environments, screen recordings or transaction logs may substitute but with reduced accuracy. The skill does not cover process simulation or statistical process control.</p>
  </section>
</article>
