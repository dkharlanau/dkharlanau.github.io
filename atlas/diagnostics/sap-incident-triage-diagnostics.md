---
layout: default
title: SAP Incident Triage Diagnostics
description: A practical first-pass method for turning vague SAP incidents into clear business impact, evidence, ownership, and next action.
permalink: /atlas/diagnostics/sap-incident-triage-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: SAP AMS operations
concept_type: diagnostic guide
sap_area: Incident management / triage
business_process: SAP AMS support
status: reviewed
verified: true
level: 2
last_reviewed: '2026-06-13'
author: Dzmitryi Kharlanau
tags:
- sap-ams
- incident-management
- triage
- support
- diagnostics
related:
- /atlas/sap/incident-triage/
- /atlas/diagnostics/sap-application-log-diagnostics/
- /atlas/diagnostics/sap-background-job-diagnostics/
robots: index,follow
sitemap: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Incident Triage Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP incident triage diagnostics</h1>
    <p class="note-subtitle">The first ten minutes should reduce uncertainty. They should not produce a longer ticket with the same vague symptom.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>SAP AMS support</dd></div>
      <div><dt>SAP area</dt><dd>Incident management / triage</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Triage is a reduction exercise</h2>
    <p>A weak ticket says “SAP is slow”, “order not working”, or “interface failed”. A useful triage result is smaller and more concrete: one business outcome, one affected object or population, one time window, one known last-good step, and one owner for the next check.</p>
    <p>You do not need the root cause during triage. You need enough evidence to stop the ticket from bouncing between teams.</p>

    <h2>Capture six things before choosing the team</h2>
    <div class="decision-table"><table><thead><tr><th>Question</th><th>Why it matters</th></tr></thead><tbody>
      <tr><td>What business result failed?</td><td>“Cannot create delivery” is more useful than “SD issue”.</td></tr>
      <tr><td>Who or what is affected?</td><td>One user, one document, one plant, or the whole company imply very different scope.</td></tr>
      <tr><td>When did it start?</td><td>A precise time window can connect the issue to jobs, interfaces, transports, or data changes.</td></tr>
      <tr><td>What still works?</td><td>A working boundary is often as valuable as the failure itself.</td></tr>
      <tr><td>What changed recently?</td><td>Recent releases, master data, schedules, certificates, or integration changes can shorten the search.</td></tr>
      <tr><td>What is the business impact?</td><td>Priority should describe lost service, money, volume, deadline, or control risk, not job title.</td></tr>
    </tbody></table></div>

    <h2>Classify by failure layer, not by keyword</h2>
    <p>Module names are useful routing hints, but a sales-order symptom can come from master data, credit, pricing, ATP, workflow, authorization, integration, or a custom enhancement. A purchasing symptom can come from finance or inventory. “SD”, “MM”, and “Basis” are not root causes.</p>
    <p>A better first classification is the failed layer:</p>
    <ul>
      <li><strong>Business document or process status</strong> such as block, incompletion, wrong document flow, or missing follow-on document.</li>
      <li><strong>Master data</strong> such as missing extension, wrong control value, or replication gap.</li>
      <li><strong>Integration</strong> such as message generation, transport, mapping, queue, or target posting.</li>
      <li><strong>Authorization</strong> when there is evidence of a failed access check.</li>
      <li><strong>Batch or scheduling</strong> when the expected background execution did not complete.</li>
      <li><strong>Technical runtime or performance</strong> when dumps, work processes, database/runtime evidence, or broad degradation support that path.</li>
      <li><strong>Recent change</strong> when the timing and affected scope point to a release or configuration change.</li>
    </ul>

    <h2>Do not open every monitor</h2>
    <p>Tools are chosen from the symptom. If a job failed, start with the job. If an IDoc failed, start with the message. If one user cannot execute an action, check the document state and authorization evidence. If the whole system is slow, technical workload tools may be appropriate.</p>
    <p>Opening SM50, SM66, SM37, SLG1, ST22, and five other transactions for every ticket is not thoroughness. It is a lack of hypothesis wearing a support badge.</p>

    <h2>A practical triage flow</h2>
    <ol>
      <li><strong>Rewrite the symptom in business language.</strong> What should happen, and what happens instead?</li>
      <li><strong>Bound the scope.</strong> One object or many? One user or many? One system or cross-system?</li>
      <li><strong>Capture time and evidence.</strong> Exact message, document/object key, timestamp, user or technical user, and any relevant status.</li>
      <li><strong>Find the last good step.</strong> This usually tells you which team should look next.</li>
      <li><strong>Check recent change and known pattern.</strong> Use operational memory, not memory theatre. Link a known issue only when the evidence matches.</li>
      <li><strong>Set impact and priority.</strong> State the number of users/orders/plants affected, financial or operational deadline, and workaround if any.</li>
      <li><strong>Route with a question.</strong> Send the next team a concrete diagnostic question, not the original complaint.</li>
    </ol>

    <h2>Example of a better handoff</h2>
    <p>Instead of: “Urgent, sales order stuck, please check.”</p>
    <p>Use: “Order 4711 item 10 is complete and confirmed, but no delivery is created for today's due date. Two other orders for the same plant work. The issue started after the morning master-data load. Please check delivery relevance and plant/shipping data for this material.”</p>
    <p>The second version may still be wrong about the cause. That is acceptable. It gives the next person evidence that can be tested.</p>

    <h2>When triage should stop</h2>
    <p>Triage is finished when the impact is understood, the evidence is sufficient for the next specialist, and ownership is clear. It should not become a miniature root-cause investigation performed by a queue manager while the real owner waits.</p>

    <h2>What good triage improves</h2>
    <p>Measure fewer reassignments, shorter time to useful evidence, better priority accuracy, and fewer incidents reopened because the downstream business result was never checked. Those signals tell you more than the number of tickets touched by the triage team.</p>
  </div>
</article>
