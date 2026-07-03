---
layout: default
title: SAP Authorization and Role Diagnostics
description: Diagnose SAP authorization failures using SU53, role and profile checks,
  organizational values, and trace evidence before requesting access changes.
permalink: /atlas/diagnostics/sap-authorization-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: SAP AMS operations
concept_type: diagnostic guide
sap_area: Authorization / roles / security
business_process: SAP AMS support
status: reviewed
verified: true
level: 2
last_reviewed: '2026-06-13'
author: Dzmitryi Kharlanau
tags:
- sap-ams
- authorization
- roles
- security
- su53
related:
- /atlas/diagnostics/sap-business-partner-replication-diagnostics/
- /atlas/diagnostics/sap-customer-master-replication-diagnostics/
robots: index,follow
sitemap: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Authorization and Role Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP authorization and role diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for authorization failures, missing roles, and profile gaps in SAP support.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>SAP AMS support</dd></div>
      <div><dt>SAP area</dt><dd>Authorization / roles / security</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Authorization failures stop users before they can reproduce a functional issue. The diagnostic goal is to capture the missing authorization object, compare it with the user's roles and profiles, and decide whether the fix is a role change, a user exit, or a process change.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>User receives 'No authorization' or 'You are not authorized' messages.</li>
      <li>A transaction starts but specific functions or fields are grayed out.</li>
      <li>Background job fails with authorization errors under its service user.</li>
      <li>An interface or RFC call fails with authorization_check errors.</li>
      <li>Authorization works in one client but not another after a transport.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing authorization object:</strong> the role does not contain the required object/activity/value.</li>
      <li><strong>Organizational level mismatch:</strong> the user is authorized for a different company code, plant, or sales organization.</li>
      <li><strong>Profile not generated:</strong> the role was changed but the profile was not regenerated or not assigned.</li>
      <li><strong>Buffer refresh:</strong> user context still holds the old authorization after a role change.</li>
      <li><strong>User comparison incomplete:</strong> the user master record was not compared after role changes.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>SU53 — display authorization check values from the last failed check.</li>
      <li>PFCG — role maintenance: check objects, organizational levels, and profile generation status.</li>
      <li>SU01 — user master: compare roles and profiles assigned to the user.</li>
      <li>ST01 — authorization trace for harder cases.</li>
      <li>SU56 — authorization buffer for the current user session.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>UST04 / UST12</strong> — user master authorization profiles.</li>
      <li><strong>AGR_1251</strong> — authorization values in roles.</li>
      <li><strong>USR02</strong> — user master logon data.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Reproduce the error or capture SU53 immediately after it occurs.</li>
      <li>Identify the missing authorization object, field, and required value.</li>
      <li>Check whether the user has a role that should contain that object.</li>
      <li>If the role exists, verify profile generation, user comparison, and buffer refresh.</li>
      <li>If the role does not contain the object, decide whether to extend the role or change the process.</li>
      <li>Document the authorization object and value before requesting a security change.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Add the missing authorization object/activity to the correct role and regenerate the profile.</li>
      <li>Adjust organizational levels if the user works across company codes or plants.</li>
      <li>Run user comparison for affected users after role changes.</li>
      <li>Refresh the user context or have the user log off and on again.</li>
      <li>Escalate to security team if the request conflicts with segregation of duties.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Authorization tickets are most useful when they include the SU53 screenshot or authorization object, the user's roles, the transaction and activity, and the business reason for access.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a support diagnostic, not a security role design or SoD review guide. It does not replace the security team's authorization concept.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>
</article>
