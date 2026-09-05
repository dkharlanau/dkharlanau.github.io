---
layout: default
title: "SAP Performance and Technical Operations — Practical S/4HANA Troubleshooting"
description: "A practical SAP performance playbook covering SM50, SM66, SM51, SM12, SM13, SM04, ST03N, STAD, ST05, SAT, HANA, tRFC, qRFC, bgRFC, traces, queues, logs, and S/4HANA Cloud Public Edition differences."
permalink: /labs/enterprise-context/performance/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-03
last_reviewed: 2026-09-03
publication_wave: "sap-operations-review-2026-09"
review_method: "current SAP primary sources + public/private deployment-boundary review + page-level factual review"
structured_data:
  type: TechArticle
primary_topic: "sap-performance-operations"
hide_global_cta: true
career_impact: mapped
career_skills:
  - delivery-observability
  - integration-recovery
  - integration-deployment
tags:
  - sap
  - s4hana
  - performance
  - basis
  - troubleshooting
  - monitoring
  - trfc
  - qrfc
  - bgrfc
  - hana
  - integration
  - cloud-alm
search_intent: "SAP S/4HANA performance troubleshooting SM50 SM66 SM12 SM13 SM58 SMQ1 SMQ2 ST05"
semantic_links:
  - type: "related_topic"
    title: "SAP Integration Architecture"
    url: "/labs/enterprise-context/integrations/"
  - type: "related_topic"
    title: "SAP Integration Operations"
    url: "/labs/enterprise-context/integration-operations/"
  - type: "related_topic"
    title: "SAP Development Architecture"
    url: "/labs/enterprise-context/development/"
  - type: "prerequisite"
    title: "SAP S/4HANA Deployment Models"
    url: "/labs/enterprise-context/deployment-models/"
  - type: "related_topic"
    title: "End-to-End Analytics"
    url: "/labs/enterprise-context/end-to-end-analytics/"
source_links:
  - title: "SM50 - Process Overview"
    url: "https://help.sap.com/docs/SUPPORT_CONTENT/basis/3354611544.html"
  - title: "SM50 in Detail: Detailed Information About a Work Process"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_BW4HANA/e067931e0b0a4b2089f4db327879cd55/ca4b45a220b040e18f1e9bea2ac223f6.html"
  - title: "Overview of Monitoring and Administration Tools"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/e067931e0b0a4b2089f4db327879cd55/47ce686c5a460a55e10000000a421937.html"
  - title: "Display and Manage User Sessions"
    url: "https://help.sap.com/docs/SAP_NETWEAVER_731_BW_ABAP/d0739d980ecf42ae9f3b4c19e21a4b6e/47c32b96f41f2974e10000000a42189b.html"
  - title: "Troubleshooting Using Central Monitoring Functions"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_BW4HANA/753088fc00704d0a80e7fbd6803c8adb/48d4f9e41904154ee10000000a421937.html"
  - title: "STAD - Business Transaction Analysis"
    url: "https://help.sap.com/docs/SUPPORT_CONTENT/basis/3354611558.html"
  - title: "Tracing"
    url: "https://help.sap.com/docs/SUPPORT_CONTENT/bwdabc/3361386604.html"
  - title: "Analyzing Performance with the ABAP Runtime Analysis"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/ba879a6e2ea04d9bb94c7ccd7cdac446/3c74c6163ce4459888bc06dedda37685.html"
  - title: "SQL Performance Monitoring"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/a24970c68fcf4770a64bf9a78e3719e2/355d59ff44ce4f789d6b29cda7ec45fa.html"
  - title: "SQL Performance Tuning Worklist"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/a24970c68fcf4770a64bf9a78e3719e2/713ff185b9b347aaacbe3ada28d4fa72.html"
  - title: "DBA Cockpit for SAP HANA - Performance"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/a0dcc12ff0e94ee7a1b0f2369c59eccf/faf07e2ead0f4396bbaa3a69c0e099e1.html"
  - title: "DBA Cockpit for SAP HANA - Expensive Statements"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/6b8fe8492ce14d24af5855c3d10701e3/b782c9687e0b42d295af27789ad58541.html"
  - title: "Monitoring tRFC"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/753088fc00704d0a80e7fbd6803c8adb/48821b412ddd3cb8e10000000a42189d.html"
  - title: "qRFC Administration"
    url: "https://help.sap.com/docs/SAP_NETWEAVER_700/109c9fd96c53101484f0ceb38844e91e/489c43f42ab0062fe10000000a42189d.html"
  - title: "Checking Queue Status"
    url: "https://help.sap.com/docs/SAP_NETWEAVER_731_BW_ABAP/753088fc00704d0a80e7fbd6803c8adb/48c1642f425831ebe10000000a42189b.html"
  - title: "bgRFC Monitor"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/753088fc00704d0a80e7fbd6803c8adb/48927c5caa6b17cee10000000a421937.html"
  - title: "Update Program Administration (SM14)"
    url: "https://help.sap.com/docs/SAP_NETWEAVER_700/10970dcb6c531014af68b7c1d32e9eab/e5de872c35cd11d3acb00000e83539c3.html"
  - title: "Updating Asynchronously in Steps"
    url: "https://help.sap.com/docs/SAP_NETWEAVER_702/fe24b0146c551014891ad42d6b2789e5/417af4d1a79e11d1950f0000e82de14a.html"
  - title: "Technical Monitoring Cockpit - SAP S/4HANA Cloud Public Edition 2608"
    url: "https://help.sap.com/docs/SAP_S4HANA_CLOUD/0cc8af9d2f2e40f38b38b46b49325e2d/16e2eaf5bffb4fb394d72e702d09d310.html"
  - title: "SAP S/4HANA Cloud Public Edition - SAP Cloud ALM Setup"
    url: "https://help.sap.com/docs/cloud-alm/setup-administration/sap-s4hana-cloud-public-edition"
  - title: "SAP Cloud ALM - System Health"
    url: "https://help.sap.com/docs/cloud-alm/applicationhelp/system-health"
  - title: "SAP Cloud ALM - Real User Monitoring"
    url: "https://help.sap.com/docs/cloud-alm/applicationhelp/rum-monitoring"
# ai-discovery-managed:start
primary_topic: "sap-performance-operations"
ai_sidecar: "/ai/pages/labs--enterprise-context--performance.json"
entity_mentions:
  - "sap-s4hana"
  - "sap-integration"
semantic_links:
  - type: "related_topic"
    title: "SAP AIF — Configuration, Monitoring and Safe Reprocessing"
    url: "/labs/enterprise-context/aif/"
  - type: "integrates_with"
    title: "SAP Testing: S/4HANA Logistics, Integrations and ABAP"
    url: "/labs/enterprise-context/testing/"
  - type: "integrates_with"
    title: "Integration Operations & Recovery — Enterprise Context Lab"
    url: "/labs/enterprise-context/integration-operations/"
  - type: "integrates_with"
    title: "SAP DRF — Data Replication Framework"
    url: "/labs/enterprise-context/integrations/drf/"
  - type: "related_topic"
    title: "SAP S/4HANA 2025: Release Readiness and Conversion"
    url: "/labs/enterprise-context/release-readiness/"
  - type: "integrates_with"
    title: "SAP Sales Integration Map — IDocs, APIs, Events and Handoffs"
    url: "/labs/enterprise-context/sales-processes/integrations/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">SAP Enterprise</a></li><li aria-current="page">Performance</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">SAP Enterprise / Performance and technical operations</p>
      <h1>Find the bottleneck before you touch the system.</h1>
      <p>This playbook connects user symptoms to SAP application servers, work processes, locks, update tasks, RFC queues, traces, ABAP runtime, SQL, HANA, and cloud monitoring. It is written for diagnosis, not for memorizing transaction codes.</p>
      <a class="research-canvas__button" href="#five-minute-path">Start with the first five minutes <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Performance playbook scope">
      <p>Diagnostic layers</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>WP</strong><small>Processes and servers</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>LUW</strong><small>Locks, update and RFC</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Trace</strong><small>ABAP, SQL and HANA</small></div>
      <em>Reviewed against SAP Help, Technical Monitoring (Cloud), and SAP Cloud ALM documentation.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">monitor_heart</span>
    <p><strong>Performance is a path, not a transaction.</strong> A slow save can be CPU, database time, an enqueue wait, update backlog, an RFC call, an overloaded work process pool, or a downstream queue.</p>
    <p><strong>Do not repair the symptom first.</strong> Deleting a lock, repeating an update, killing a work process, deleting a queue LUW, or resending a message can create duplicates or hide the real failure.</p>
  </section>

  <section class="research-canvas__inventory" id="five-minute-path" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">First five minutes</p>
      <h2>Determine the scope before collecting deep traces.</h2>
      <p>The first question is not “Which transaction should I open?” It is “How wide is the problem?”</p>
    </header>
    <div class="research-route-list">
      <a href="#system-wide"><span>01</span><strong>Is everything slow?</strong><small>Check all application servers, work process saturation, workload history, operating-system pressure, database pressure, and major integration backlogs.</small><i class="material-symbols-outlined" aria-hidden="true">public</i></a>
      <a href="#single-flow"><span>02</span><strong>Is one transaction, user, or document slow?</strong><small>Use STAD or the active work process first. Then choose ST05, SAT, or a focused trace from evidence.</small><i class="material-symbols-outlined" aria-hidden="true">person_search</i></a>
      <a href="#locks-updates"><span>03</span><strong>Does the user wait during save or posting?</strong><small>Check locks, update processing, dumps, and the current work process before blaming SQL.</small><i class="material-symbols-outlined" aria-hidden="true">lock_clock</i></a>
      <a href="#rfc-queues"><span>04</span><strong>Did the business process cross a system boundary?</strong><small>Separate synchronous RFC, tRFC, qRFC, bgRFC, IDoc, web service, and application-level processing.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="#traces"><span>05</span><strong>Only then trace.</strong><small>Use the smallest trace that can answer the question. Broad tracing creates noise and can add overhead.</small><i class="material-symbols-outlined" aria-hidden="true">troubleshoot</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Mental model</p>
      <h2>Follow one request through the technical layers.</h2>
      <p>For a classic ABAP request, think in this order: entry point → application server → work process → ABAP logic → lock/update/RFC dependency → database → response. Fiori and APIs add HTTP, ICM, Gateway or service layers in front.</p>
    </header>
    <div class="research-route-list">
      <a href="#servers"><span>L1</span><strong>Instance and dispatcher</strong><small>Which application server received the work, and does that instance still have capacity?</small><i class="material-symbols-outlined" aria-hidden="true">dns</i></a>
      <a href="#work-processes"><span>L2</span><strong>Work process</strong><small>DIA, BTC, UPD, UP2, SPO and other process types execute different workloads. Saturation at one type can block only part of the system.</small><i class="material-symbols-outlined" aria-hidden="true">memory</i></a>
      <a href="#locks-updates"><span>L3</span><strong>SAP LUW controls</strong><small>Logical locks and update tasks are part of transaction consistency. Waiting here can look like generic slowness.</small><i class="material-symbols-outlined" aria-hidden="true">sync_lock</i></a>
      <a href="#rfc-queues"><span>L4</span><strong>Remote dependency</strong><small>A caller can wait for a remote system, or a reliable asynchronous LUW can remain in a queue after the dialog has finished.</small><i class="material-symbols-outlined" aria-hidden="true">swap_horiz</i></a>
      <a href="#sql-hana"><span>L5</span><strong>Database execution</strong><small>High database time may come from expensive SQL, too much data, poor access paths, locking, or workload pressure.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="servers" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Servers and users</p>
      <h2>Know whether you are looking at one instance or the whole system.</h2>
      <p>This distinction prevents many false conclusions.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/e067931e0b0a4b2089f4db327879cd55/47ce686c5a460a55e10000000a421937.html" target="_blank" rel="noopener"><span>SM51</span><strong>Application servers</strong><small>Shows the ABAP application server instances in the system. Use it to see the landscape and move to the correct instance before opening instance-local tools.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_NETWEAVER_731_BW_ABAP/d0739d980ecf42ae9f3b4c19e21a4b6e/47c32b96f41f2974e10000000a42189b.html" target="_blank" rel="noopener"><span>SM04</span><strong>User sessions on the current application server</strong><small>Shows users, sessions, connection type, transaction and memory for the instance you are on. An RFC or HTTP connection can exist without a normal GUI transaction.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="#tool-map"><span>AL08</span><strong>System-wide user view</strong><small>Useful when the user may be connected to another application server. Confirm active sessions before removing a suspected stale lock.</small><i class="material-symbols-outlined" aria-hidden="true">groups</i></a>
      <a href="#work-processes"><span>Rule</span><strong>Always correlate user → instance → work process.</strong><small>A user name alone does not tell you which process is executing now or which server owns the relevant trace file.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="work-processes" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SM50 and SM66</p>
      <h2>Read work processes as a live queue of system pressure.</h2>
      <p>SM50 is instance-local. SM66 gives a system-wide work process view. A few running processes are normal; the pattern matters.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SUPPORT_CONTENT/basis/3354611544.html" target="_blank" rel="noopener"><span>SM50</span><strong>Process Overview</strong><small>Use it when you know the affected instance or need detail such as ABAP stack, memory, database statistics, current action, user, report, runtime, and process trace.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="#system-wide"><span>SM66</span><strong>Global Work Process Overview</strong><small>Use it when the problem may span several application servers or when you want to find long-running work without checking each instance separately.</small><i class="material-symbols-outlined" aria-hidden="true">lan</i></a>
      <a href="#wp-status"><span>Status</span><strong>Waiting is usually healthy capacity.</strong><small>A waiting work process is idle and ready for work. A system where nearly every relevant work process is running for a sustained period deserves investigation.</small><i class="material-symbols-outlined" aria-hidden="true">hourglass_empty</i></a>
      <a href="#wp-status"><span>HOLD</span><strong>Hold is not automatically an error.</strong><small>Read the hold reason. Examples include debugging, locks, updates, GUI waits and remote communication. Too many held processes can reduce available capacity.</small><i class="material-symbols-outlined" aria-hidden="true">pause_circle</i></a>
      <a href="#wp-status"><span>PRIV</span><strong>PRIV points to private memory use.</strong><small>The work process is reserved for one user after memory behavior crosses the normal shared-memory path. Treat repeated PRIV patterns as a memory and workload question, not a reason to kill the process immediately.</small><i class="material-symbols-outlined" aria-hidden="true">memory_alt</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="wp-status" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Work process interpretation</p>
      <h2>Type tells you what pool is under pressure.</h2>
      <p>Exact process configuration is system-specific, but the operating logic is stable.</p>
    </header>
    <div class="research-route-list">
      <a href="#work-processes"><span>DIA</span><strong>Dialog</strong><small>User dialog steps and many online requests. If all dialog processes are busy, new dialog requests wait in the dispatcher queue.</small><i class="material-symbols-outlined" aria-hidden="true">desktop_windows</i></a>
      <a href="#work-processes"><span>BTC</span><strong>Background</strong><small>Background jobs. Check SM37 when a long job consumes resources or when parallel background work affects online users.</small><i class="material-symbols-outlined" aria-hidden="true">schedule</i></a>
      <a href="#locks-updates"><span>UPD</span><strong>Update V1</strong><small>Processes time-critical update tasks. A backlog or failed update mechanism can make saves fail or leave business documents incomplete.</small><i class="material-symbols-outlined" aria-hidden="true">system_update_alt</i></a>
      <a href="#locks-updates"><span>UP2</span><strong>Update V2</strong><small>Processes lower-priority secondary updates. V2 is separated from V1 so less critical work does not delay time- and lock-critical updates.</small><i class="material-symbols-outlined" aria-hidden="true">low_priority</i></a>
      <a href="#tool-map"><span>SPO</span><strong>Spool</strong><small>Output processing. Spool saturation is a different failure class from slow dialog processing.</small><i class="material-symbols-outlined" aria-hidden="true">print</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="locks-updates" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Locks and updates</p>
      <h2>SM12 and SM13 protect consistency. Treat them carefully.</h2>
      <p>A lock is not “bad” because it is old, and an update request is not safe to repeat because it failed.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/e067931e0b0a4b2089f4db327879cd55/47ce686c5a460a55e10000000a421937.html" target="_blank" rel="noopener"><span>SM12</span><strong>SAP logical locks</strong><small>Identify lock object, owner, client, host, time and related activity. SAP enqueue locks are application-level consistency controls; do not confuse them with database row or table locks.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="#lock-check"><span>Check</span><strong>Before deleting a lock</strong><small>Verify the user in SM04/AL08, active work in SM50/SM66, related background jobs in SM37, and the business transaction. A lock can still be valid even when the GUI looks idle.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="https://help.sap.com/docs/SAP_NETWEAVER_700/10970dcb6c531014af68b7c1d32e9eab/e5de872c35cd11d3acb00000e83539c3.html" target="_blank" rel="noopener"><span>SM13</span><strong>Individual update requests</strong><small>Use SM13 to display and handle update requests. Check the user, transaction, update modules, status, timestamp and error before any repeat or delete action.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_NETWEAVER_700/10970dcb6c531014af68b7c1d32e9eab/e5de872c35cd11d3acb00000e83539c3.html" target="_blank" rel="noopener"><span>SM14</span><strong>Update system administration</strong><small>Use when the question is the update system itself: servers, groups and parameters. SM13 is the better tool for individual update requests.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="#errors"><span>ST22</span><strong>Look for the cause, not only the failed update.</strong><small>An update error may have a related ABAP short dump. Also correlate system log, application log and the business document state.</small><i class="material-symbols-outlined" aria-hidden="true">bug_report</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="lock-check" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lock decision</p>
      <h2>A safe lock investigation has four checks.</h2>
      <p>Use the sequence before choosing delete.</p>
    </header>
    <div class="research-route-list">
      <a href="#servers"><span>1</span><strong>Owner</strong><small>Is the SAP user still active? On which application server? Which session or connection type?</small><i class="material-symbols-outlined" aria-hidden="true">person</i></a>
      <a href="#work-processes"><span>2</span><strong>Execution</strong><small>Is a work process still running the request, waiting for a remote call, or held for another reason?</small><i class="material-symbols-outlined" aria-hidden="true">memory</i></a>
      <a href="#tool-map"><span>3</span><strong>Background work</strong><small>Is a job still active under the same user or business object?</small><i class="material-symbols-outlined" aria-hidden="true">schedule</i></a>
      <a href="#errors"><span>4</span><strong>Failure evidence</strong><small>Did the session terminate abnormally? Check ST22, SM21, developer traces and application logs before removing the remaining lock.</small><i class="material-symbols-outlined" aria-hidden="true">plagiarism</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="rfc-queues" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">RFC and queues</p>
      <h2>First identify the RFC type. The monitor depends on it.</h2>
      <p>“RFC failed” is not a complete diagnosis. Synchronous calls, tRFC, qRFC and bgRFC have different persistence, ordering and recovery behavior.</p>
    </header>
    <div class="research-route-list">
      <a href="#sync-rfc"><span>sRFC</span><strong>Synchronous RFC</strong><small>The caller waits for the remote result. Investigate current work process state, destination/connection, Gateway, remote execution time and RFC trace when needed.</small><i class="material-symbols-outlined" aria-hidden="true">sync</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/753088fc00704d0a80e7fbd6803c8adb/48821b412ddd3cb8e10000000a42189d.html" target="_blank" rel="noopener"><span>tRFC</span><strong>Transactional RFC — SM58</strong><small>Reliable asynchronous unit with a transaction ID. SM58 lists calls that were not completed successfully or had to be scheduled. Successful calls are confirmed and removed from the tRFC tables.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_NETWEAVER_700/109c9fd96c53101484f0ceb38844e91e/489c43f42ab0062fe10000000a42189d.html" target="_blank" rel="noopener"><span>qRFC</span><strong>Queued RFC — SMQ1 / SMQ2</strong><small>qRFC adds ordered processing through logical queues. SMQ1 monitors outbound queues; SMQ2 monitors inbound queues.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/753088fc00704d0a80e7fbd6803c8adb/48927c5caa6b17cee10000000a421937.html" target="_blank" rel="noopener"><span>bgRFC</span><strong>Background RFC — SBGRFCMON</strong><small>bgRFC is a separate implementation and functional alternative to classic tRFC/qRFC for applications that use it. Its units are monitored in SBGRFCMON, not by assuming they will appear in SM58 or SMQ1/SMQ2.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sync-rfc" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Synchronous RFC</p>
      <h2>When the caller waits, follow both sides.</h2>
      <p>A synchronous RFC can make a local transaction look slow even when local ABAP and SQL are fine.</p>
    </header>
    <div class="research-route-list">
      <a href="#tool-map"><span>SM59</span><strong>Destination definition and tests</strong><small>Check that the destination resolves, authenticates and reaches the target. A successful connection test still does not prove the business function is fast.</small><i class="material-symbols-outlined" aria-hidden="true">link</i></a>
      <a href="#tool-map"><span>SMGW</span><strong>RFC Gateway</strong><small>Use the Gateway monitor for RFC connection-level evidence and registered server programs when the problem is at the communication layer.</small><i class="material-symbols-outlined" aria-hidden="true">router</i></a>
      <a href="#work-processes"><span>SM50</span><strong>Caller state</strong><small>A held work process with a remote communication reason is evidence that the caller is waiting outside the local ABAP step.</small><i class="material-symbols-outlined" aria-hidden="true">pause</i></a>
      <a href="#traces"><span>ST05</span><strong>RFC trace</strong><small>Use a focused RFC trace when you need call direction, called function, data volume and duration rather than a broad system trace.</small><i class="material-symbols-outlined" aria-hidden="true">troubleshoot</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="trfc" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">tRFC</p>
      <h2>SM58 is an exception monitor, not a history of successful calls.</h2>
      <p>This point is important during support: an empty SM58 normally means there is no remaining unsuccessful tRFC LUW for the selection.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/753088fc00704d0a80e7fbd6803c8adb/48821b412ddd3cb8e10000000a42189d.html" target="_blank" rel="noopener"><span>1</span><strong>Read destination, TID and error text.</strong><small>The error in SM58 is part of the evidence path. Determine whether the failure is communication, target runtime, authorization, application logic or temporary availability.</small><i class="material-symbols-outlined" aria-hidden="true">receipt_long</i></a>
      <a href="#errors"><span>2</span><strong>Check the target system.</strong><small>If execution reached the target, inspect the target short dump, system log and application log where relevant.</small><i class="material-symbols-outlined" aria-hidden="true">travel_explore</i></a>
      <a href="#tool-map"><span>3</span><strong>Check SM59 and SMGW for communication issues.</strong><small>Do not resend a failing LUW repeatedly while the destination or target problem is still present.</small><i class="material-symbols-outlined" aria-hidden="true">router</i></a>
      <a href="#recovery"><span>4</span><strong>Recover only after the cause is controlled.</strong><small>Before manual execution, rollback, delete or resend, understand whether the business operation is idempotent and whether the target may already contain a partial or completed result.</small><i class="material-symbols-outlined" aria-hidden="true">restart_alt</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="qrfc" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">qRFC</p>
      <h2>The first blocked LUW can stop everything behind it.</h2>
      <p>That serialization is the purpose of the queue. It protects order, but it also means one root cause can create a large backlog.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_NETWEAVER_700/109c9fd96c53101484f0ceb38844e91e/489c43f42ab0062fe10000000a42189d.html" target="_blank" rel="noopener"><span>SMQ1</span><strong>Outbound queue on the sending side</strong><small>Use it to see outbound queue names, destinations, LUWs and status before the calls are successfully handed into the target processing path.</small><i class="material-symbols-outlined" aria-hidden="true">outbox</i></a>
      <a href="https://help.sap.com/docs/SAP_NETWEAVER_700/109c9fd96c53101484f0ceb38844e91e/489c43f42ab0062fe10000000a42189d.html" target="_blank" rel="noopener"><span>SMQ2</span><strong>Inbound queue on the receiving side</strong><small>Use it when the LUW has reached the target queue but processing is blocked, waiting or failed.</small><i class="material-symbols-outlined" aria-hidden="true">move_to_inbox</i></a>
      <a href="https://help.sap.com/docs/SAP_NETWEAVER_700/109c9fd96c53101484f0ceb38844e91e/489c43f42ab0062fe10000000a42189d.html" target="_blank" rel="noopener"><span>SMQS</span><strong>Outbound queue scheduler</strong><small>Scheduler administration for outbound destinations. If queues exist but scheduling is not occurring, do not inspect only the LUW status.</small><i class="material-symbols-outlined" aria-hidden="true">schedule_send</i></a>
      <a href="https://help.sap.com/docs/SAP_NETWEAVER_700/109c9fd96c53101484f0ceb38844e91e/489c43f42ab0062fe10000000a42189d.html" target="_blank" rel="noopener"><span>SMQR</span><strong>Inbound queue scheduler</strong><small>Registration and scheduler control for inbound queues.</small><i class="material-symbols-outlined" aria-hidden="true">schedule</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="queue-status" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Queue status</p>
      <h2>Read the status as a failure class, not as a color.</h2>
      <p>Exact retry behavior can differ by direction and configuration. These meanings are the safe diagnostic starting points.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_NETWEAVER_731_BW_ABAP/753088fc00704d0a80e7fbd6803c8adb/48c1642f425831ebe10000000a42189b.html" target="_blank" rel="noopener"><span>SYSFAIL</span><strong>Execution failed in the target processing path.</strong><small>A serious system or application exception blocked the queue. Read the queue error and check the corresponding target dump or application evidence before restart.</small><i class="material-symbols-outlined" aria-hidden="true">error</i></a>
      <a href="https://help.sap.com/docs/SAP_NETWEAVER_700/109c9fd96c53101484f0ceb38844e91e/489c44a82ab0062fe10000000a42189d.html" target="_blank" rel="noopener"><span>CPICERR</span><strong>Communication problem.</strong><small>Investigate Gateway, destination, network and target availability. Outbound automatic repetition can depend on SM59 destination configuration.</small><i class="material-symbols-outlined" aria-hidden="true">wifi_off</i></a>
      <a href="https://help.sap.com/docs/SAP_NETWEAVER_731_BW_ABAP/753088fc00704d0a80e7fbd6803c8adb/48c1642f425831ebe10000000a42189b.html" target="_blank" rel="noopener"><span>STOP</span><strong>Queue was stopped explicitly.</strong><small>Do not unlock it automatically. Find who or which application stopped it and whether the stop condition is still valid.</small><i class="material-symbols-outlined" aria-hidden="true">stop_circle</i></a>
      <a href="https://help.sap.com/docs/SAP_NETWEAVER_731_BW_ABAP/753088fc00704d0a80e7fbd6803c8adb/48c1642f425831ebe10000000a42189b.html" target="_blank" rel="noopener"><span>WAITING</span><strong>Dependency on another queue.</strong><small>The first LUW can wait because another related queue has higher-priority work. Follow the dependency instead of restarting randomly.</small><i class="material-symbols-outlined" aria-hidden="true">hourglass_top</i></a>
      <a href="#qrfc"><span>READY</span><strong>Ready is not the same as processed.</strong><small>If READY entries accumulate, also inspect scheduler registration, available resources and whether processing is actually progressing.</small><i class="material-symbols-outlined" aria-hidden="true">play_circle</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="recovery" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Recovery rule</p>
      <h2>Restart is a business action with technical buttons.</h2>
      <p>Reliable transport does not remove duplicate risk, partial processing risk, or application-specific dependencies.</p>
    </header>
    <div class="research-route-list">
      <a href="#rfc-queues"><span>1</span><strong>Identify the business object.</strong><small>What document, delivery, material, order, event or posting does the LUW represent?</small><i class="material-symbols-outlined" aria-hidden="true">description</i></a>
      <a href="#errors"><span>2</span><strong>Prove the failure boundary.</strong><small>Was the call never sent, received but not executed, executed and rolled back, or executed successfully while only the acknowledgement failed?</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="#trfc"><span>3</span><strong>Check idempotency and duplicate controls.</strong><small>Know what happens if the same business operation is executed again.</small><i class="material-symbols-outlined" aria-hidden="true">fingerprint</i></a>
      <a href="#qrfc"><span>4</span><strong>Respect queue ordering.</strong><small>Deleting the first LUW may release later LUWs and change business sequence. That is not a purely technical cleanup.</small><i class="material-symbols-outlined" aria-hidden="true">format_list_numbered</i></a>
      <a href="#tool-map"><span>5</span><strong>Record the recovery evidence.</strong><small>Capture cause, action, owner, affected objects, retry result and any manual business correction.</small><i class="material-symbols-outlined" aria-hidden="true">history_edu</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="errors" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Logs and traces</p>
      <h2>Use the log that belongs to the failing layer.</h2>
      <p>One incident may need several layers of evidence.</p>
    </header>
    <div class="research-route-list">
      <a href="#tool-map"><span>ST22</span><strong>ABAP short dumps</strong><small>Use when ABAP runtime terminated. Correlate user, time, program, exception and call context.</small><i class="material-symbols-outlined" aria-hidden="true">bug_report</i></a>
      <a href="#tool-map"><span>SM21</span><strong>System log</strong><small>Use for application server and system-level events around the incident time. Remember that server-local evidence may matter.</small><i class="material-symbols-outlined" aria-hidden="true">article</i></a>
      <a href="#tool-map"><span>ST11</span><strong>Developer traces</strong><small>Read dispatcher, work process, Gateway or other developer traces when the failure is below normal application logging. Use the correct instance and timestamp.</small><i class="material-symbols-outlined" aria-hidden="true">terminal</i></a>
      <a href="#tool-map"><span>SLG1</span><strong>Application Log</strong><small>Use when the application writes structured business or technical messages. Object and subobject selection often matters more than the transaction code.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#integration-logs"><span>SRT</span><strong>Web service monitoring</strong><small>For ABAP web services, SRT_MONI and SRT_UTIL are part of the diagnostic path. Keep transport, protocol and business processing separate.</small><i class="material-symbols-outlined" aria-hidden="true">webhook</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="single-flow" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">ST03N and STAD</p>
      <h2>Use statistics before expensive tracing when possible.</h2>
      <p>Statistics tell you whether time is concentrated in one transaction, user, task type, server or resource component.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_BW4HANA/753088fc00704d0a80e7fbd6803c8adb/48d4f9e41904154ee10000000a421937.html" target="_blank" rel="noopener"><span>ST03N</span><strong>Workload Monitor — aggregated view</strong><small>Use it for workload history and patterns: which transactions, users, task types or instances consume time and resources over a period.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SUPPORT_CONTENT/basis/3354611558.html" target="_blank" rel="noopener"><span>STAD</span><strong>Individual statistical records</strong><small>Use it when you know the user, transaction, program or time. Statistical records contain response-time proportions, database accesses, memory use and RFC calls for individual execution steps.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="#traces"><span>Rule</span><strong>ST03N finds the pattern. STAD finds the execution. Trace explains the hot path.</strong><small>This sequence reduces random tracing and gives you a baseline for comparison.</small><i class="material-symbols-outlined" aria-hidden="true">insights</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="traces" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Trace selection</p>
      <h2>Choose the smallest tool that can answer the question.</h2>
      <p>Trace only the user, process, transaction or time window you need whenever the tool supports it.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SUPPORT_CONTENT/bwdabc/3361386604.html" target="_blank" rel="noopener"><span>ST05</span><strong>Performance Trace</strong><small>SQL trace for database calls, RFC trace for remote calls, Enqueue trace for lock operations, and Buffer trace for table-buffer behavior. ST05 is the right tool when the question is a specific technical interaction.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/ba879a6e2ea04d9bb94c7ccd7cdac446/3c74c6163ce4459888bc06dedda37685.html" target="_blank" rel="noopener"><span>SAT</span><strong>ABAP Runtime Analysis</strong><small>Use it to find where ABAP runtime and memory are consumed and to identify hot methods, functions, loops and statements in a specific application flow.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SUPPORT_CONTENT/abap/3353525954.html" target="_blank" rel="noopener"><span>ST12</span><strong>Combined ABAP + performance trace</strong><small>Useful when available because it combines ABAP runtime and ST05-style performance analysis. ST12 is delivered with ST-A/PI service tools and is not guaranteed to exist in every system.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/a24970c68fcf4770a64bf9a78e3719e2/355d59ff44ce4f789d6b29cda7ec45fa.html" target="_blank" rel="noopener"><span>SQLM</span><strong>SQL Monitor</strong><small>Use for longer-running productive SQL monitoring when you need frequency and runtime evidence across real business usage, not one short trace window.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/a24970c68fcf4770a64bf9a78e3719e2/713ff185b9b347aaacbe3ada28d4fa72.html" target="_blank" rel="noopener"><span>SWLT</span><strong>SQL Performance Tuning Worklist</strong><small>Combines SQL Monitor runtime evidence with static performance findings so tuning candidates can be ranked by actual business relevance.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sql-hana" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">HANA and SQL</p>
      <h2>HANA does not make inefficient access patterns disappear.</h2>
      <p>Fast columnar execution still suffers when code reads too much data, executes the same statement too often, creates expensive joins, transfers large result sets, or runs under heavy database pressure.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/a0dcc12ff0e94ee7a1b0f2369c59eccf/faf07e2ead0f4396bbaa3a69c0e099e1.html" target="_blank" rel="noopener"><span>DBACOCKPIT</span><strong>Database performance view</strong><small>For SAP HANA, DBA Cockpit provides database monitoring and performance analysis. Use it when ABAP evidence points to database pressure rather than immediately changing code.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/6b8fe8492ce14d24af5855c3d10701e3/b782c9687e0b42d295af27789ad58541.html" target="_blank" rel="noopener"><span>Expensive</span><strong>Expensive Statements</strong><small>Analyze SQL statements above the configured duration threshold. The expensive statement trace is not necessarily enabled by default; trace configuration is an administrative decision.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/a0dcc12ff0e94ee7a1b0f2369c59eccf/ca6c2f538ec341f3b50ee2579cecf65f.html" target="_blank" rel="noopener"><span>EXPLAIN</span><strong>Execution plan</strong><small>Use the plan to understand the optimizer strategy before proposing an index or SQL rewrite. On HANA, “add an index” should never be the first reflex.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="#system-wide"><span>ST06</span><strong>Operating-system pressure</strong><small>On systems where you have classic Basis access, ST06 helps separate CPU, memory and host-resource pressure from an application-only issue.</small><i class="material-symbols-outlined" aria-hidden="true">memory</i></a>
      <a href="#tool-map"><span>ST02</span><strong>Buffer and memory indicators</strong><small>Useful for SAP memory and buffer health. Do not tune buffers from one snapshot; correlate repeated evidence and system sizing.</small><i class="material-symbols-outlined" aria-hidden="true">memory_alt</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="system-wide" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">System-wide slowdown</p>
      <h2>Use breadth first, then narrow down.</h2>
      <p>If many users complain at the same time, tracing one user first is usually too narrow.</p>
    </header>
    <div class="research-route-list">
      <a href="#servers"><span>1</span><strong>SM51 / SM66</strong><small>Are all instances healthy? Are work processes saturated on one server or across the system? Is one report or user dominating runtime?</small><i class="material-symbols-outlined" aria-hidden="true">dns</i></a>
      <a href="#single-flow"><span>2</span><strong>ST03N</strong><small>Was the slowdown real in workload statistics? Which task type, transaction, user, instance or time period changed?</small><i class="material-symbols-outlined" aria-hidden="true">query_stats</i></a>
      <a href="#sql-hana"><span>3</span><strong>ST06 / database monitoring</strong><small>Check host CPU, memory and database pressure. High work process utilization can be a consequence of slow database work, not only too few work processes.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
      <a href="#locks-updates"><span>4</span><strong>SM12 / SM13</strong><small>Look for widespread enqueue or update symptoms when posting and save operations are affected.</small><i class="material-symbols-outlined" aria-hidden="true">lock</i></a>
      <a href="#rfc-queues"><span>5</span><strong>SM58 / SMQ1 / SMQ2 / SBGRFCMON</strong><small>Large asynchronous backlogs can be both a symptom and a cause of business-process delay.</small><i class="material-symbols-outlined" aria-hidden="true">queue</i></a>
      <a href="#errors"><span>6</span><strong>ST22 / SM21</strong><small>Check whether the slowdown aligns with runtime errors, instance restarts, communication errors or other system events.</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="integration-logs" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Integration logs</p>
      <h2>Separate business message state from transport state.</h2>
      <p>An IDoc, qRFC LUW and application document can describe different stages of the same business exchange.</p>
    </header>
    <div class="research-route-list">
      <a href="#rfc-queues"><span>Transport</span><strong>SM58 / SMQ1 / SMQ2 / SBGRFCMON</strong><small>Use these for the RFC transport or queued unit layer.</small><i class="material-symbols-outlined" aria-hidden="true">swap_horiz</i></a>
      <a href="#tool-map"><span>IDoc</span><strong>WE02 / WE05 / BD87</strong><small>Use IDoc status and records for the ALE/IDoc message layer. A transport-level success does not automatically mean the target business document posted correctly.</small><i class="material-symbols-outlined" aria-hidden="true">description</i></a>
      <a href="#errors"><span>SOAP</span><strong>SRT_MONI / SRT_UTIL</strong><small>Use for ABAP web service message monitoring and traces where applicable.</small><i class="material-symbols-outlined" aria-hidden="true">webhook</i></a>
      <a href="#public-cloud"><span>Cloud</span><strong>SAP Cloud ALM Integration &amp; Exception Monitoring</strong><small>For cloud and hybrid landscapes, use the central monitoring path instead of expecting every component to expose classic Basis transactions.</small><i class="material-symbols-outlined" aria-hidden="true">cloud</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="public-cloud" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Deployment model</p>
      <h2>Public Cloud changes the operating model, not the need for evidence.</h2>
      <p>Do not design SAP S/4HANA Cloud Public Edition support around unrestricted classic Basis, OS and database access.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/0cc8af9d2f2e40f38b38b46b49325e2d/16e2eaf5bffb4fb394d72e702d09d310.html" target="_blank" rel="noopener"><span>F4031</span><strong>Technical Monitoring Cockpit</strong><small>SAP S/4HANA Cloud Public Edition provides a Technical Monitoring Cockpit for administrators and developers. Current 2608 documentation lists System Workload, Sampled Work Process Data, System Outbound Communication and SQL Trace Analysis.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/btp/technical-monitoring-cockpit-cloud-version/monitoring-system-workload-data-provisioning" target="_blank" rel="noopener"><span>Workload</span><strong>System Workload vs sampled work processes</strong><small>System Workload is based on completed ABAP statistics records and aggregates. Sampled Work Process Data takes frequent samples and can show currently running workload that has not finished yet.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/cloud-alm/setup-administration/sap-s4hana-cloud-public-edition" target="_blank" rel="noopener"><span>ALM</span><strong>SAP Cloud ALM</strong><small>Public Edition supports Business Process Monitoring, Integration &amp; Exception Monitoring, Real User Monitoring, Job &amp; Automation Monitoring, and Health Monitoring through SAP Cloud ALM setup.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/cloud-alm/applicationhelp/rum-monitoring" target="_blank" rel="noopener"><span>RUM</span><strong>Real User Monitoring</strong><small>Use end-user and backend request performance evidence when the question is user experience across cloud services rather than one ABAP work process.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/cloud-alm/applicationhelp/system-health" target="_blank" rel="noopener"><span>Health</span><strong>Health Monitoring</strong><small>Use health and resource metrics, reported errors, connectivity and performance KPIs for supported services. It complements, rather than replaces, request-level performance analysis.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">On-premise / Private Edition</p>
      <h2>Classic tools remain powerful because you own more of the stack.</h2>
      <p>Exact availability still depends on release, authorization, architecture and operational responsibility.</p>
    </header>
    <div class="research-route-list">
      <a href="#tool-map"><span>ABAP</span><strong>Application-server tools</strong><small>SM51, SM50, SM66, SM04, SM12, SM13, ST22, SM21, ST11, ST03N, STAD, ST05 and SAT remain core diagnostic tools in classic ABAP operations.</small><i class="material-symbols-outlined" aria-hidden="true">settings</i></a>
      <a href="#sql-hana"><span>DB</span><strong>Database and host diagnostics</strong><small>DBA Cockpit, ST06 and lower-level traces are available when your operating model and authorizations allow them.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="#public-cloud"><span>Hybrid</span><strong>Central monitoring still matters.</strong><small>SAP Cloud ALM also supports SAP S/4HANA and SAP S/4HANA Cloud Private Edition, so classic transactions and central observability can be used together.</small><i class="material-symbols-outlined" aria-hidden="true">cloud_sync</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="tool-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Tool map</p>
      <h2>What to open, and what question it answers.</h2>
      <p>Use this as a memory map, not as a sequence that must always be executed.</p>
    </header>
    <div class="research-route-list">
      <a href="#servers"><span>SM51</span><strong>Which application servers are in the system?</strong><small>Server overview and navigation to instance-local analysis.</small><i class="material-symbols-outlined" aria-hidden="true">dns</i></a>
      <a href="#work-processes"><span>SM50</span><strong>What is running on this instance now?</strong><small>Work process state, user, report, action, runtime, stack, memory and process trace.</small><i class="material-symbols-outlined" aria-hidden="true">memory</i></a>
      <a href="#work-processes"><span>SM66</span><strong>What is running across all instances now?</strong><small>Global work process overview.</small><i class="material-symbols-outlined" aria-hidden="true">lan</i></a>
      <a href="#servers"><span>SM04</span><strong>Which users and sessions are on this application server?</strong><small>Instance-local user/session view.</small><i class="material-symbols-outlined" aria-hidden="true">person</i></a>
      <a href="#servers"><span>AL08</span><strong>Which users are active system-wide?</strong><small>Useful across several application servers.</small><i class="material-symbols-outlined" aria-hidden="true">groups</i></a>
      <a href="#locks-updates"><span>SM12</span><strong>Which SAP logical locks exist?</strong><small>Lock owner, object and age; deletion only after ownership checks.</small><i class="material-symbols-outlined" aria-hidden="true">lock</i></a>
      <a href="#locks-updates"><span>SM13</span><strong>Which update requests failed or are pending?</strong><small>Individual update request analysis and controlled recovery.</small><i class="material-symbols-outlined" aria-hidden="true">system_update_alt</i></a>
      <a href="#locks-updates"><span>SM14</span><strong>Is the update system configured and active correctly?</strong><small>Update servers, groups and parameters.</small><i class="material-symbols-outlined" aria-hidden="true">settings</i></a>
      <a href="#single-flow"><span>ST03N</span><strong>Where is workload time concentrated over a period?</strong><small>Aggregated workload and performance patterns.</small><i class="material-symbols-outlined" aria-hidden="true">query_stats</i></a>
      <a href="#single-flow"><span>STAD</span><strong>What happened in one execution?</strong><small>Individual statistics records with response, DB, memory and RFC details.</small><i class="material-symbols-outlined" aria-hidden="true">receipt_long</i></a>
      <a href="#errors"><span>ST22</span><strong>Did ABAP terminate?</strong><small>Short dump analysis.</small><i class="material-symbols-outlined" aria-hidden="true">bug_report</i></a>
      <a href="#errors"><span>SM21</span><strong>Did the system log an infrastructure event?</strong><small>System log around the incident window.</small><i class="material-symbols-outlined" aria-hidden="true">article</i></a>
      <a href="#errors"><span>ST11</span><strong>What do developer traces say?</strong><small>Dispatcher, work process and other technical trace files.</small><i class="material-symbols-outlined" aria-hidden="true">terminal</i></a>
      <a href="#traces"><span>ST05</span><strong>Which SQL, RFC, enqueue or buffer calls are expensive?</strong><small>Focused performance trace.</small><i class="material-symbols-outlined" aria-hidden="true">troubleshoot</i></a>
      <a href="#traces"><span>SAT</span><strong>Where does ABAP code spend runtime?</strong><small>Runtime analysis and call hierarchy.</small><i class="material-symbols-outlined" aria-hidden="true">code</i></a>
      <a href="#traces"><span>SQLM</span><strong>Which SQL is expensive in real productive usage over time?</strong><small>Longer-running SQL monitor.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
      <a href="#traces"><span>SWLT</span><strong>Which SQL tuning candidates matter most?</strong><small>Runtime evidence plus static findings.</small><i class="material-symbols-outlined" aria-hidden="true">playlist_add_check</i></a>
      <a href="#sql-hana"><span>DBACOCKPIT</span><strong>Is HANA or the database layer the bottleneck?</strong><small>Database performance, expensive statements, plans and diagnostics.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="#sql-hana"><span>ST06</span><strong>Is the host under CPU or memory pressure?</strong><small>Operating-system monitoring where available.</small><i class="material-symbols-outlined" aria-hidden="true">memory</i></a>
      <a href="#sync-rfc"><span>SM59</span><strong>Is the RFC destination technically reachable?</strong><small>Destination configuration and tests.</small><i class="material-symbols-outlined" aria-hidden="true">link</i></a>
      <a href="#sync-rfc"><span>SMGW</span><strong>Is the RFC Gateway layer healthy?</strong><small>RFC connections and Gateway-level diagnostics.</small><i class="material-symbols-outlined" aria-hidden="true">router</i></a>
      <a href="#rfc-queues"><span>SM58</span><strong>Which tRFC LUWs remain unsuccessful?</strong><small>Transactional RFC exception monitor.</small><i class="material-symbols-outlined" aria-hidden="true">sync_problem</i></a>
      <a href="#qrfc"><span>SMQ1</span><strong>Which outbound qRFC queues are blocked?</strong><small>Sending-side queues.</small><i class="material-symbols-outlined" aria-hidden="true">outbox</i></a>
      <a href="#qrfc"><span>SMQ2</span><strong>Which inbound qRFC queues are blocked?</strong><small>Receiving-side queues.</small><i class="material-symbols-outlined" aria-hidden="true">move_to_inbox</i></a>
      <a href="#qrfc"><span>SMQS</span><strong>Is outbound queue scheduling configured?</strong><small>QOUT scheduler administration.</small><i class="material-symbols-outlined" aria-hidden="true">schedule_send</i></a>
      <a href="#qrfc"><span>SMQR</span><strong>Is inbound queue scheduling configured?</strong><small>QIN scheduler administration.</small><i class="material-symbols-outlined" aria-hidden="true">schedule</i></a>
      <a href="#rfc-queues"><span>SBGRFCMON</span><strong>Which bgRFC units or queues are blocked?</strong><small>Background RFC monitor.</small><i class="material-symbols-outlined" aria-hidden="true">queue</i></a>
      <a href="#integration-logs"><span>SLG1</span><strong>What did the application log?</strong><small>Business/application log by object and subobject.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#integration-logs"><span>SRT_MONI</span><strong>What happened to ABAP web service messages?</strong><small>Web service message monitoring.</small><i class="material-symbols-outlined" aria-hidden="true">webhook</i></a>
      <a href="#system-wide"><span>SM37</span><strong>Is a background job long-running, delayed or failed?</strong><small>Background job status, runtime and log.</small><i class="material-symbols-outlined" aria-hidden="true">schedule</i></a>
      <a href="#public-cloud"><span>F4031</span><strong>How do I monitor Public Edition technically?</strong><small>Technical Monitoring Cockpit and its workload, work-process, outbound communication and SQL analysis views.</small><i class="material-symbols-outlined" aria-hidden="true">cloud</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Incident playbooks</p>
      <h2>Common symptoms and the evidence path.</h2>
      <p>These paths are starting points. Stop as soon as the evidence identifies the boundary.</p>
    </header>
    <div class="research-route-list">
      <a href="#system-wide"><span>A</span><strong>“Everything is slow.”</strong><small>SM51/SM66 → ST03N → ST06/database → ST22/SM21 → large lock/update/RFC backlogs. Do not start with SAT on one program.</small><i class="material-symbols-outlined" aria-hidden="true">public</i></a>
      <a href="#single-flow"><span>B</span><strong>“Only VA01 / MIGO / one custom app is slow.”</strong><small>STAD → active SM50 process if reproducible → ST05 or SAT depending whether time is DB/RFC/lock or ABAP runtime → HANA plan only if DB evidence justifies it.</small><i class="material-symbols-outlined" aria-hidden="true">person_search</i></a>
      <a href="#locks-updates"><span>C</span><strong>“Save hangs or document says locked.”</strong><small>SM50 hold/action → SM12 owner → SM04/AL08 and SM37 → ST22/SM21 if session ended → remove only stale lock after business confirmation.</small><i class="material-symbols-outlined" aria-hidden="true">lock_clock</i></a>
      <a href="#locks-updates"><span>D</span><strong>“Posting failed after Save.”</strong><small>SM13 → update module/error → ST22 → business document state → only then repeat or correct update.</small><i class="material-symbols-outlined" aria-hidden="true">system_update_alt</i></a>
      <a href="#trfc"><span>E</span><strong>“Interface did not reach the target.”</strong><small>Identify technology → SM58 for tRFC, SMQ1/SMQ2 for qRFC, SBGRFCMON for bgRFC → SM59/SMGW for communication → target logs for execution.</small><i class="material-symbols-outlined" aria-hidden="true">sync_problem</i></a>
      <a href="#qrfc"><span>F</span><strong>“Thousands of qRFC entries are waiting.”</strong><small>Find the first blocked queue/LUW → read status → SYSFAIL: target execution evidence; CPICERR: communication; STOP/WAITING: control/dependency → fix first cause before mass restart.</small><i class="material-symbols-outlined" aria-hidden="true">queue</i></a>
      <a href="#sql-hana"><span>G</span><strong>“DB time is high.”</strong><small>STAD/ST05 or SQLM → identify statement and frequency → DBA Cockpit/expensive statements/plan → inspect data volume and access path → tune with evidence.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="#public-cloud"><span>H</span><strong>“Public Cloud app is slow.”</strong><small>Technical Monitoring Cockpit System Workload / Sampled Work Process Data / SQL Trace Analysis plus SAP Cloud ALM Real User and Health Monitoring. Escalate with timestamps and request evidence, not screenshots alone.</small><i class="material-symbols-outlined" aria-hidden="true">cloud</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead-level reasoning</p>
      <h2>What a strong SAP Lead answer sounds like.</h2>
      <p>The value is in the order of investigation and the control of recovery risk.</p>
    </header>
    <div class="research-route-list">
      <a href="#five-minute-path"><span>1</span><strong>Start with scope.</strong><small>“I first separate system-wide degradation from one user, transaction, document or integration path.”</small><i class="material-symbols-outlined" aria-hidden="true">filter_alt</i></a>
      <a href="#work-processes"><span>2</span><strong>Use live and historical evidence together.</strong><small>“SM50/SM66 show what is happening now; ST03N/STAD show whether that pattern is normal and where time was spent.”</small><i class="material-symbols-outlined" aria-hidden="true">timeline</i></a>
      <a href="#locks-updates"><span>3</span><strong>Protect transactional consistency.</strong><small>“I do not delete locks or repeat update requests until I know whether the owner is active and what business object is affected.”</small><i class="material-symbols-outlined" aria-hidden="true">shield</i></a>
      <a href="#rfc-queues"><span>4</span><strong>Name the RFC type.</strong><small>“SM58 is tRFC. SMQ1/SMQ2 are qRFC. SBGRFCMON is bgRFC. I do not use one queue monitor as a generic interface monitor.”</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#traces"><span>5</span><strong>Trace with a hypothesis.</strong><small>“ST05 answers SQL/RFC/enqueue questions; SAT answers ABAP runtime questions; SQLM/SWLT are better for longer-term SQL evidence.”</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="#public-cloud"><span>6</span><strong>Adapt to the deployment model.</strong><small>“In Public Edition I use SAP-delivered monitoring apps and Cloud ALM rather than assuming unrestricted Basis, OS or HANA administration access.”</small><i class="material-symbols-outlined" aria-hidden="true">cloud_done</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary references</p>
      <h2>SAP Help sources used for this playbook.</h2>
      <p>Release-sensitive behavior should always be checked against the documentation for the exact SAP S/4HANA or ABAP Platform release in the target system.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SUPPORT_CONTENT/basis/3354611544.html" target="_blank" rel="noopener"><span>SAP</span><strong>SM50 - Process Overview</strong><small>Work process types, status, hold reasons and process operations.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_BW4HANA/753088fc00704d0a80e7fbd6803c8adb/48d4f9e41904154ee10000000a421937.html" target="_blank" rel="noopener"><span>SAP</span><strong>Central Monitoring Functions</strong><small>STAD, ST03N and ST05 as core performance analysis tools.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/753088fc00704d0a80e7fbd6803c8adb/48821b412ddd3cb8e10000000a42189d.html" target="_blank" rel="noopener"><span>SAP</span><strong>Monitoring tRFC</strong><small>SM58 behavior, LUW/TID handling and successful-call cleanup.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_NETWEAVER_700/109c9fd96c53101484f0ceb38844e91e/489c43f42ab0062fe10000000a42189d.html" target="_blank" rel="noopener"><span>SAP</span><strong>qRFC Administration</strong><small>SMQ1, SMQ2, SMQS and SMQR roles.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/753088fc00704d0a80e7fbd6803c8adb/48927c5caa6b17cee10000000a421937.html" target="_blank" rel="noopener"><span>SAP</span><strong>bgRFC Monitor</strong><small>SBGRFCMON and bgRFC unit model.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/0cc8af9d2f2e40f38b38b46b49325e2d/16e2eaf5bffb4fb394d72e702d09d310.html" target="_blank" rel="noopener"><span>2608</span><strong>S/4HANA Cloud Public Edition Technical Monitoring Cockpit</strong><small>Public Cloud workload, work process, outbound communication and SQL analysis capabilities.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/cloud-alm/setup-administration/sap-s4hana-cloud-public-edition" target="_blank" rel="noopener"><span>ALM</span><strong>SAP Cloud ALM for S/4HANA Cloud Public Edition</strong><small>Supported central monitoring applications and setup.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">gpp_maybe</span>
    <p><strong>Operational boundary:</strong> permissions, production-change rules and incident procedures vary by customer and deployment model. Use read-only diagnosis first. Destructive actions such as terminating processes, deleting locks, deleting LUWs or changing trace configuration require the correct authorization and business ownership.</p>
    <p><strong>Release boundary:</strong> transaction availability and exact screen behavior can differ by ABAP Platform and S/4HANA release. Public Edition uses a restricted cloud operating model; use the apps and monitoring services available in the tenant release.</p>
  </section>
</div>
