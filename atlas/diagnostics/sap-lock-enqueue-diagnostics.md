---
layout: default
title: "SAP Lock / Enqueue Diagnostics"
description: "Conservative diagnostic frame for SAP enqueue lock conflicts, stuck SM12 entries, and deadlock-related failures."
permalink: /atlas/diagnostics/sap-lock-enqueue-diagnostics/
last_modified_at: 2026-06-13
atlas_section: diagnostics
domain: SAP AMS
subdomain: SAP AMS operations
concept_type: diagnostic guide
sap_area: "Enqueue / SM12"
business_process: "SAP AMS support"
status: needs_verification
verified: false
level: 1
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau
tags:
  - sap-ams
  - enqueue
  - sm12
  - lock
  - diagnostics
related:
  - /atlas/diagnostics/sap-update-termination-diagnostics/
  - /atlas/diagnostics/sap-background-job-diagnostics/
  - /atlas/diagnostics/sap-master-data-activation-diagnostics/
  - /atlas/diagnostics/sap-application-log-diagnostics/
robots: noindex,follow
sitemap: false
---

**Source:** Practical pattern derived from SAP support experience. Not yet verified against public SAP documentation.
**Date checked:** 2026-06-13
**Confidence:** medium
**Related page/topic:** /atlas/diagnostics/sap-update-termination-diagnostics/
**Practical implication:** Identify the lock owner, lock argument, and whether the owner session is still active before deciding to wait, terminate a session, or fix the underlying program.
**Tags:** sap-ams, enqueue, sm12, lock, diagnostics

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Lock / Enqueue Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP lock / enqueue diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a transaction, update, or background job is blocked by an enqueue lock.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>SAP AMS support</dd></div>
      <div><dt>SAP area</dt><dd>Enqueue / SM12</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP documentation.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>SAP uses enqueue locks to prevent two processes from changing the same object at the same time. When a lock is held too long or not released, other users and background jobs wait or fail. The diagnostic goal is to find the lock owner, confirm whether the owner is still doing useful work, and decide whether to wait, terminate the session, or fix the program that holds the lock.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>A user or job receives "Object is locked by user X" or a similar enqueue message.</li>
      <li>A transaction appears to hang before saving or changing an object.</li>
      <li>A background job fails with an enqueue or timeout error.</li>
      <li>An update request terminates in SM13 with a lock conflict.</li>
      <li>SM12 shows old lock entries that do not match any active session.</li>
      <li>Deadlock messages appear in SM21 or in application logs.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>User session left open:</strong> a user started a change transaction and left the screen open.</li>
      <li><strong>Long-running process:</strong> a dialog step, report, or batch job holds the lock for an extended time.</li>
      <li><strong>Lock not released after failure:</strong> the program that set the lock dumped or was cancelled without releasing it.</li>
      <li><strong>Enqueue server issue:</strong> the enqueue service or replication in a clustered environment is delayed or split.</li>
      <li><strong>Deadlock between competing processes:</strong> two processes each hold a lock the other needs.</li>
      <li><strong>RFC or tRFC queue holds a lock:</strong> an asynchronous call owns the lock longer than expected.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>SM12</strong> — lock entry monitor: owner, lock argument, time, and mode.</li>
      <li><strong>SM04 / AL08</strong> — active user sessions to see if the owner is still logged on and active.</li>
      <li><strong>SM50 / SM66</strong> — work process overview for long-running dialog or background tasks.</li>
      <li><strong>SM13</strong> — update terminations caused by lock conflicts.</li>
      <li><strong>ST22</strong> — short dumps where a lock was not released.</li>
      <li><strong>SM21</strong> — system log for enqueue or deadlock messages.</li>
      <li><strong>SM58</strong> — tRFC queue if an asynchronous call owns the lock.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>SM12</strong> — enqueue lock entry monitor.</li>
      <li><strong>SM04 / AL08</strong> — user session overview.</li>
      <li><strong>SM50 / SM66</strong> — work process overview.</li>
      <li><strong>SM21</strong> — system log.</li>
      <li><strong>SM58</strong> — asynchronous RFC error log.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Record the object key, user, transaction, and exact error message of the blocked process.</li>
      <li>Open SM12 and filter by the object or user to find the lock owner and lock argument.</li>
      <li>Check SM04/AL08 to see if the owner session is still active and what transaction it is running.</li>
      <li>Check SM50/SM66 for a long-running work process owned by the same user.</li>
      <li>If the owner session is gone, check ST22 and SM21 for a dump or enqueue server issue.</li>
      <li>Decide whether to wait, ask the user to complete the transaction, or delete the stale lock.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Ask the lock owner to complete or exit the transaction.</li>
      <li>Terminate a stale or runaway session only after confirming it is safe.</li>
      <li>Delete stale SM12 entries only with functional approval and after verifying no active process.</li>
      <li>Reschedule batch jobs to avoid peak dialog times or competing jobs.</li>
      <li>Adjust program logic to release locks as early as possible.</li>
      <li>Escalate to Basis if the enqueue server itself appears unstable.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Lock issues are usually operational, not bugs. The key evidence is the lock owner, the lock argument, how long the lock has been held, and whether the owner session is still active. Never delete production locks without approval.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a Basis guide for enqueue server configuration or high-availability setup. It does not cover SAP HANA row-store locking details.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>

    <h2>Next diagnostic steps</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-update-termination-diagnostics/">SAP Update Termination Diagnostics</a> — if the lock caused an update termination.</li>
      <li><a href="/atlas/diagnostics/sap-background-job-diagnostics/">SAP Background Job Failure Diagnostics</a> — if a batch job failed on a lock.</li>
      <li><a href="/atlas/diagnostics/sap-master-data-activation-diagnostics/">SAP Master Data Activation Diagnostics</a> — if locks block MDG or mass activation.</li>
    </ul>

    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-application-log-diagnostics/">SAP Application Log Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-incident-triage-diagnostics/">SAP Incident Triage Diagnostics</a></li>
    </ul>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
