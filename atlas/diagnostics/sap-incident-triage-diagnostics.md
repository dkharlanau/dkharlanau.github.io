---
layout: default
title: SAP Incident Triage Diagnostics
description: Conservative diagnostic frame for classifying and routing SAP support
  incidents before deep investigation.
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
- /atlas/diagnostics/sap-alerting-diagnostics/
- /atlas/diagnostics/sap-change-control-diagnostics/
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
    <p class="note-subtitle">A first-pass structure for classifying and routing SAP support incidents.</p>
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
    <h2>Core idea</h2>
    <p>Good triage prevents wrong teams, missing evidence, and wasted time. The diagnostic goal in the first minutes is to classify the incident by symptom area, urgency, and the minimum evidence needed before assignment.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Incident description is vague or only says 'system is slow'.</li>
      <li>Ticket is routed to a team that does not own the failing area.</li>
      <li>Multiple users report different symptoms for the same underlying issue.</li>
      <li>Incident is treated as urgent but has no business impact yet.</li>
      <li>Previous incidents for the same symptom were closed without root cause.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing classification:</strong> the ticket lacks module, process, or object information.</li>
      <li><strong>Incorrect routing:</strong> routing rules rely on keywords that do not match the actual failure area.</li>
      <li><strong>Insufficient evidence:</strong> logs, error messages, or timestamps were not collected.</li>
      <li><strong>Urgency mismatch:</strong> priority is set by who reported it, not by business impact.</li>
      <li><strong>No known-pattern link:</strong> the symptom matches a known diagnostic page but was not checked.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>Ticket fields — module, process, object, error text, time, user.</li>
      <li>Atlas/Skill Hub diagnostic index — find a matching pattern.</li>
      <li>System status monitors — SM50, SM66, SM37 for workload or job issues.</li>
      <li>Application log (SLG1) or short dumps (ST22) for the time window.</li>
      <li>Recent changes — transports, jobs, master data updates.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>Incident/ticket system</strong> — classification and routing metadata.</li>
      <li><strong>SM50 / SM66</strong> — work process overview.</li>
      <li><strong>TBTCO</strong> — background job status.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Read the ticket and extract: symptom, process area, object key, time, user, and business impact.</li>
      <li>Classify as master data, configuration, integration, authorization, batch, or performance.</li>
      <li>Check for matching diagnostic pages or known patterns in the Atlas.</li>
      <li>Collect minimum evidence: error text, status, log object, or job name.</li>
      <li>Set priority based on business impact, not reporter seniority.</li>
      <li>Route to the team that owns the component and attach the evidence.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Add mandatory classification fields to the incident form.</li>
      <li>Maintain routing rules based on object type and module keywords.</li>
      <li>Link frequently seen symptoms to diagnostic pages in the knowledge base.</li>
      <li>Create an evidence checklist for each major symptom category.</li>
      <li>Review closed incidents for recurring patterns and update triage guidance.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Triage tickets are most useful when they include a clear symptom, process area, affected object, time, user, and the business impact that justifies the priority.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a triage diagnostic, not an ITIL incident-management process guide. It does not cover SLA definitions or escalation policies.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>
</article>
