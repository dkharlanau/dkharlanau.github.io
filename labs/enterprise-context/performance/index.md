---
layout: default
title: "SAP Performance and Technical Operations — Practical S/4HANA Troubleshooting"
description: "A practical SAP S/4HANA performance guide for locating response time across work processes, locks and updates, remote calls, ABAP runtime, SQL/HANA, and cloud monitoring."
permalink: /labs/enterprise-context/performance/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-24
last_reviewed: 2026-09-24
publication_wave: "sap-operations-review-2026-09"
review_method: "SAP S/4HANA 2025 FPS01 + SAP S/4HANA Cloud Public Edition 2608 primary-source recheck + nearby Labs review + full editorial rewrite"
structured_data:
  type: TechArticle
primary_topic: "sap-s4hana"
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
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/e067931e0b0a4b2089f4db327879cd55/ca4b45a220b040e18f1e9bea2ac223f6.html"
  - title: "Workload Monitor"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/e067931e0b0a4b2089f4db327879cd55/2db8be3befaefc75e10000000a114084.html"
  - title: "Statistics"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/e067931e0b0a4b2089f4db327879cd55/3440a2f2a8e14faa95acb8a0387dc87e.html"
  - title: "Technical Monitoring in the ABAP Platform"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/6d9d967c861d4f78b5b90a4fe9b7d2e7/3dc65fa387a6430182dfafa9a1cde5e5.html"
  - title: "SAP Fiori App Descriptions Including App IDs"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/6d9d967c861d4f78b5b90a4fe9b7d2e7/fabdd762d87442588c162ff6fa02c138.html"
  - title: "Synchronous and Asynchronous Updating"
    url: "https://help.sap.com/docs/SAP_NETWEAVER_750/979cf1522d164bf7a781796efd8850ee/6b96ee764b054c5f929dea77ffcf7a6b.html"
  - title: "Managing Lock Entries"
    url: "https://help.sap.com/docs/SAP_NETWEAVER_AS_ABAP_752/6568469cf5a1460a8d85c58b83d21ec2/47ea39fae97f486ee10000000a42189d.html"
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
  - title: "Monitoring tRFC"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/753088fc00704d0a80e7fbd6803c8adb/48821b412ddd3cb8e10000000a42189d.html"
  - title: "qRFC Administration"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/753088fc00704d0a80e7fbd6803c8adb/489c43f42ab0062fe10000000a42189d.html"
  - title: "Checking Queue Status"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/753088fc00704d0a80e7fbd6803c8adb/48c1642f425831ebe10000000a42189b.html"
  - title: "bgRFC Monitor"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/753088fc00704d0a80e7fbd6803c8adb/48927c5caa6b17cee10000000a421937.html"
  - title: "Technical Monitoring Cockpit - SAP S/4HANA Cloud Public Edition 2608"
    url: "https://help.sap.com/docs/SAP_S4HANA_CLOUD/0cc8af9d2f2e40f38b38b46b49325e2d/16e2eaf5bffb4fb394d72e702d09d310.html"
  - title: "SQL Statement Analysis - SAP S/4HANA Cloud Public Edition 2608"
    url: "https://help.sap.com/docs/SAP_S4HANA_CLOUD/0cc8af9d2f2e40f38b38b46b49325e2d/2d3e9aff21194e81bbb781384b60b02c.html"
  - title: "ABAP Runtime Errors - SAP S/4HANA Cloud Public Edition 2608"
    url: "https://help.sap.com/docs/SAP_S4HANA_CLOUD/0cc8af9d2f2e40f38b38b46b49325e2d/7ca808df191e4fc6bf502d8dd80dd477.html"
  - title: "SAP S/4HANA Cloud Public Edition - SAP Cloud ALM Setup"
    url: "https://help.sap.com/docs/cloud-alm/setup-administration/sap-s4hana-cloud-public-edition"
# ai-discovery-managed:start
primary_topic: "sap-s4hana"
ai_sidecar: "/ai/pages/labs--enterprise-context--performance.json"
entity_mentions:
  - "sap-integration"
semantic_links:
  - type: "same_domain"
    title: "SAP Testing Strategy for S/4HANA Delivery"
    url: "/labs/enterprise-context/testing/"
  - type: "same_domain"
    title: "SAP S/4HANA 2025 Release Readiness Playbook"
    url: "/labs/enterprise-context/release-readiness/"
  - type: "related_topic"
    title: "SAP AIF — Monitoring, Error Handling and Reprocessing"
    url: "/labs/enterprise-context/aif/"
  - type: "same_domain"
    title: "SAP S/4HANA Deployment Models — Enterprise Context Lab"
    url: "/labs/enterprise-context/deployment-models/"
  - type: "same_domain"
    title: "SAP Development Architecture — RAP, CAP, ABAP Cloud and Clean Core"
    url: "/labs/enterprise-context/development/"
  - type: "same_domain"
    title: "FI/CO for Logistics — Enterprise Context Lab"
    url: "/labs/enterprise-context/finance-logistics/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">SAP Enterprise</a></li><li aria-current="page">Performance</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">SAP Enterprise / Performance and technical operations</p>
      <h1>Find where the time goes<br />before you change the system.</h1>
      <p>A slow SAP transaction is not a diagnosis. Response time can accumulate before a work process starts, inside ABAP, while waiting for a lock or update, during a remote call, or in SQL and HANA. The useful skill is to locate that boundary with evidence, then choose the narrowest tool that can explain it.</p>
      <a class="research-canvas__button" href="#five-minute-path">Start with the symptom <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Performance investigation model">
      <p>Three questions</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Scope</strong><small>One request or many users?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Time</strong><small>Where is elapsed time accumulating?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>State</strong><small>Is the wait safe to change?</small></div>
      <em>Diagnosis before intervention</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">monitor_heart</span>
    <div>
      <p><strong>Performance, failure, and business completion are different questions.</strong> A request can be slow and still succeed. It can return quickly while an asynchronous update or integration fails later. A queue can be healthy while the business waits because an earlier message is correctly blocking later work.</p>
      <p>Start by locating elapsed time. Change locks, updates, processes, or queues only after you understand the business state they protect.</p>
    </div>
    <a href="/labs/enterprise-context/integration-operations/">For message recovery, use Integration Operations <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="five-minute-path" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">First five minutes</p>
      <h2>Measure the width of the problem before its depth.</h2>
      <p>The first useful split is system-wide versus one execution. That choice determines whether we begin with capacity and workload history or with one request and its response-time components.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Many users or transactions</h3><p>Look for a shared resource: work-process saturation, host or database pressure, update backlog, a common remote dependency, or a large queue. Broad evidence comes before a deep trace of one program.</p></div>
      <div><h3>One user, app, or document</h3><p>Find one representative execution. Use statistics and the current work-process state to separate ABAP, database, lock, update, RFC, and queue time before tracing.</p></div>
      <div><h3>One deployment model</h3><p>Classic ABAP tools are not a universal operating model. On SAP S/4HANA Cloud Public Edition, use the technical-monitoring apps and services available in the tenant release rather than assuming unrestricted Basis, OS, or database access.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Request path</p>
      <h2>Follow one request through the components that can make it wait.</h2>
    </header>
    <div class="ecg-rail" aria-label="ABAP request performance path">
      <div class="ecg-rail__branch">
        <span class="ecg-node ecg-node--input">Request</span><span class="ecg-arrow" aria-hidden="true">→</span>
        <span class="ecg-node ecg-node--decision">Queue / work process</span><span class="ecg-arrow" aria-hidden="true">→</span>
        <span class="ecg-node ecg-node--decision">ABAP + dependencies</span><span class="ecg-arrow" aria-hidden="true">→</span>
        <span class="ecg-node ecg-node--decision">SQL / HANA</span><span class="ecg-arrow" aria-hidden="true">→</span>
        <span class="ecg-node ecg-node--output">Response</span>
      </div>
    </div>
    <p>For a classic ABAP request, an application server dispatches work to an appropriate work process. The program can then spend time in ABAP logic, database access, enqueue operations, update handling, RFC calls, or other services. Fiori and APIs add HTTP and service layers in front, but the same diagnostic rule survives: identify the component that owns the missing time.</p>
    <p>A concrete example makes this useful. If a save takes 12 seconds and statistics show most time in database processing, the next question is SQL. If most time is remote-call time, local SQL tuning is noise. If the active work process is held on an enqueue wait, the relevant object and lock owner matter more than either trace.</p>
  </section>

  <section class="research-canvas__inventory" id="servers" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Application servers</p>
      <h2>Know whether the evidence is instance-local or system-wide.</h2>
      <p>In a multi-instance ABAP system, the user, work process, trace, and resource pressure may belong to one application server while the rest of the system remains healthy.</p>
    </header>
    <p>SM51 gives the application-server view. SM50 is primarily a snapshot of work processes on the current instance, with detailed information such as current action, user, program, runtime, ABAP stack, memory, and database statistics. When the affected instance is unknown, use a system-wide process view rather than drawing conclusions from one server.</p>
  </section>

  <section class="research-canvas__inventory" id="work-processes" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Work processes</p>
      <h2>A busy process is evidence; a pattern of busy processes is a capacity signal.</h2>
      <p>Dialog, background, update, and spool work use different process types. Pressure in one pool can affect only part of the system.</p>
    </header>
    <p>A single long-running DIA or BTC process may be the business workload you expect. A sustained pattern where the relevant process pool is occupied and requests wait for a process is different: queue wait has become part of response time. SAP's current technical-monitoring model exposes queue wait separately because time spent waiting for a work process is not application execution time.</p>
    <p>The process detail is most useful when it links a symptom to an active program, action, SQL statement, remote call, lock, or memory condition. It is less useful as a reason to terminate a process simply because its runtime looks large.</p>
  </section>

  <section class="research-canvas__inventory" id="wp-status" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Status interpretation</p>
      <h2>Waiting, Hold, and PRIV mean different things.</h2>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Waiting</h3><p>In SM50, Waiting normally means the work process is idle and ready for work. Many waiting processes are capacity, not a problem.</p></div>
      <div><h3>Hold</h3><p>Hold means the process is tied to one user for a reason such as debugging, locks, updates, GUI interaction, or communication. The reason matters. Too many held processes can reduce available capacity.</p></div>
      <div><h3>PRIV</h3><p>PRIV is a memory-management condition in which a process is reserved for one user. Repeated or widespread PRIV states point to memory and workload behavior that deserves analysis; killing the process is not a root-cause fix.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="locks-updates" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Locks and updates</p>
      <h2>A save can wait after the business logic has already done most of its work.</h2>
      <p>SAP logical locks and the update system protect transactional consistency. They can create visible waiting, but they are not interchangeable with database locks or generic performance errors.</p>
    </header>
    <p>SM12 shows SAP lock entries managed by the enqueue service. A lock can be completely valid while another user experiences it as a delay. Before deleting anything, identify the lock object and owner, check whether the owning session or background work is still active, and understand which business transaction the lock protects.</p>
    <p>SM13 belongs to update processing. With asynchronous updating, the calling program hands work to the update system and does not wait for its result. With synchronous updating, the caller waits for the update result. That distinction matters during recovery: SAP explicitly documents that a failed synchronous update cannot simply be processed a second time in SM13.</p>
    <div class="ecg-diagnostic" id="lock-check">
      <div><h4>Before changing a lock</h4><p>Correlate owner, active session or job, work-process state, update state, and the business object. An old timestamp alone is not enough evidence that a lock is stale.</p></div>
      <div><h4>Before repeating an update</h4><p>Read the update type, failing module, error, and resulting document state. Recovery rules depend on how the application issued the update and what already committed.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="single-flow" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Statistics before trace</p>
      <h2>Use workload data to decide what deserves a trace.</h2>
      <p>ABAP statistics records already split response time into useful technical components. They are often enough to move from “slow” to a testable hypothesis.</p>
    </header>
    <p>ST03N is the broad view: workload over time, across instances, users, transactions, and response-time components. Individual statistics records provide the execution-level view: one dialog step or request with response time, CPU time, database activity, and other technical data. Together they answer two different questions—whether a pattern is systemic and what happened in one representative execution.</p>
    <p>That sequence also protects production systems from unnecessary tracing. If workload data already shows that a slowdown is almost entirely database time, trace the relevant SQL path. If the time is remote, follow the remote dependency. If CPU and ABAP processing dominate, ABAP runtime analysis becomes a better next step.</p>
  </section>

  <section class="research-canvas__inventory" id="traces" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Trace selection</p>
      <h2>Trace a hypothesis, not a user complaint.</h2>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>ST05</h3><p>Use a focused performance trace when the question is SQL, RFC, enqueue, or buffer activity in a reproducible flow. Keep the user and time window narrow.</p></div>
      <div><h3>SAT</h3><p>Use ABAP Runtime Analysis when the question is where ABAP execution spends CPU/runtime or which calls and statements dominate the program path.</p></div>
      <div><h3>SQLM / SWLT</h3><p>Use longer-running SQL evidence when the issue is frequency and productive impact rather than one trace window. SWLT helps combine runtime evidence with static findings to prioritize candidates.</p></div>
    </div>
    <p>Trace overhead and noise both increase with scope. Capture enough context to reproduce and correlate the request, then stop the trace. A technically rich trace that cannot be tied back to the reported business step is weak evidence.</p>
  </section>

  <section class="research-canvas__inventory" id="sql-hana" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SQL and HANA</p>
      <h2>High database time is the start of the SQL investigation, not its conclusion.</h2>
    </header>
    <p>First identify the statement, how often it runs, the amount of data it processes, and whether the cost is isolated or widespread. Then use database monitoring and the execution plan to understand why. On SAP HANA, an expensive statement can come from data volume, repeated execution, joins, filters, plan choices, concurrency, or broader database pressure; “add an index” is not a useful default diagnosis.</p>
    <p>DBA Cockpit and HANA analysis tools are appropriate when ABAP evidence points to the database layer. ST06 and similar host views matter when CPU, memory, disk, or operating-system pressure is shared across application workloads. The point is to keep the layers connected: database symptoms should explain the application response time you started with.</p>
  </section>

  <section class="research-canvas__inventory" id="system-wide" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">System-wide slowdown</p>
      <h2>When many users are slow, look for the shared constraint.</h2>
    </header>
    <p>Start with application-server and work-process capacity, then compare workload history for the affected period. If queue wait or process saturation increased, ask what consumed the pool. If database time rose across many transactions, move down to database and host evidence. If saves are the common symptom, inspect update and lock behavior. If only processes that call one remote service slow down, the shared constraint may be outside the local system.</p>
    <p>This breadth-first approach prevents a common failure mode: tracing one familiar transaction deeply while the actual problem is an overloaded instance, a database-wide issue, or a remote dependency affecting many callers.</p>
  </section>

  <section class="research-canvas__inventory" id="rfc-queues" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Remote calls and queues</p>
      <h2>A remote wait is a performance boundary; queue recovery is a separate operational problem.</h2>
      <p>First identify the communication model. Synchronous RFC, tRFC, qRFC, and bgRFC have different execution and persistence semantics, so they do not belong in one generic “RFC monitor.”</p>
    </header>
    <div class="ecg-decision-columns">
      <div id="sync-rfc"><h3>Synchronous RFC</h3><p>The caller waits for the remote result. If local statistics or the current work process show remote-call time, follow the destination and the target execution rather than tuning unrelated local code.</p></div>
      <div id="trfc"><h3>tRFC</h3><p>SM58 is mainly an exception view for transactional RFC calls that did not complete successfully or were scheduled. A successful tRFC does not remain there as permanent history.</p></div>
      <div id="qrfc"><h3>qRFC and bgRFC</h3><p>qRFC adds queue ordering and is monitored through the relevant outbound or inbound queue. bgRFC has its own unit model and SBGRFCMON. A blocked predecessor can legitimately hold later ordered work.</p></div>
    </div>
    <p id="queue-status">Queue status tells you why processing is not progressing; it does not by itself tell you whether a business object is safe to replay. Treat communication errors, application failures, explicit stops, and ordering dependencies as different failure classes.</p>
    <p id="recovery">For restart, duplicate handling, ordering, and business reconciliation, continue with <a href="/labs/enterprise-context/integration-operations/">Integration Operations &amp; Recovery</a>. This performance page only needs to establish whether remote execution or queued work explains the elapsed business time.</p>
  </section>

  <section class="research-canvas__inventory" id="errors" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Failure evidence</p>
      <h2>Use the evidence source owned by the failing layer.</h2>
    </header>
    <p>ST22 answers whether ABAP terminated with a runtime error. SM21 belongs to system-level events. Developer traces belong lower in the technical stack. Application Log is useful only where the application actually writes structured messages. These sources complement one another; none is a universal error log.</p>
    <p>A performance incident can need failure evidence when the request stopped rather than merely slowed, but do not let error hunting replace time analysis. A clean ST22 does not prove that an application was fast, just as a successful application log does not prove that the user saw acceptable response time.</p>
  </section>

  <section class="research-canvas__inventory" id="integration-logs" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Integration evidence</p>
      <h2>Transport state and application state can explain different parts of the same delay.</h2>
    </header>
    <p>SM58, qRFC monitors, and SBGRFCMON describe reliable-communication units. IDoc status, web-service monitoring, AIF, or an application log describe other stages. When performance crosses a system boundary, correlate the sender request with the transport/message identity and the receiver processing time instead of reading each monitor in isolation.</p>
  </section>

  <section class="research-canvas__inventory" id="public-cloud" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SAP S/4HANA Cloud Public Edition</p>
      <h2>The evidence model remains; the operating surface changes.</h2>
      <p>Public Edition does not expose the same unrestricted Basis, operating-system, and database administration model as an on-premise system. Use the SAP-delivered technical-monitoring apps available in the tenant release.</p>
    </header>
    <p>SAP's current ABAP Platform documentation lists Technical Monitoring Cockpit / System Workload and Sampled Work Process Data under app ID F4031, SQL Statement Analysis as F8784, and ABAP Runtime Errors as F7770. Current SAP S/4HANA Cloud Public Edition 2608 documentation also exposes SQL Statement Analysis for aggregated SQL performance and resource metrics and ABAP Runtime Errors for tenant short dumps.</p>
    <p>Those apps preserve the same reasoning: workload data tells us where time accumulates, sampled process data helps with currently running work, SQL analysis explains database consumers, and runtime-error evidence explains terminations. SAP Cloud ALM adds cross-service perspectives such as real-user, integration, job, and health monitoring where configured. Always use the documentation for the tenant's actual release rather than assuming a 2608 screen exists everywhere.</p>
  </section>

  <section class="research-canvas__inventory" id="tool-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Compact tool map</p>
      <h2>Choose a tool because of the question it can answer.</h2>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Live execution</h3><p><strong>SM50 / system-wide process view:</strong> what is running or waiting now, on which instance, for which user and program?</p></div>
      <div><h3>Workload history</h3><p><strong>ST03N / statistics records:</strong> where did response time accumulate across a period or in one execution?</p></div>
      <div><h3>Consistency</h3><p><strong>SM12 / SM13:</strong> is the request waiting on SAP locks or update processing, and what state is safe to change?</p></div>
      <div><h3>Code and calls</h3><p><strong>ST05 / SAT:</strong> which SQL, RFC, enqueue activity, or ABAP call path explains the measured time?</p></div>
      <div><h3>Database</h3><p><strong>DBA Cockpit / HANA analysis:</strong> which statement or database resource explains high database time?</p></div>
      <div><h3>Reliable communication</h3><p><strong>SM58 / qRFC monitors / SBGRFCMON:</strong> is asynchronous work blocked, and which communication model owns it?</p></div>
      <div><h3>Cloud technical monitoring</h3><p><strong>Fiori technical-monitoring apps / SAP Cloud ALM:</strong> what workload, SQL, runtime-error, user-experience, or service-health evidence is available in the cloud operating model?</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary references</p>
      <h2>SAP documentation behind the model.</h2>
      <p>Release-sensitive screens and app availability should be checked against the exact ABAP Platform or SAP S/4HANA Cloud release in the target system.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SUPPORT_CONTENT/basis/3354611544.html" target="_blank" rel="noopener"><span>SAP</span><strong>SM50 - Process Overview</strong><small>Work-process types, status, Hold reasons, and PRIV.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/e067931e0b0a4b2089f4db327879cd55/2db8be3befaefc75e10000000a114084.html" target="_blank" rel="noopener"><span>2025</span><strong>Workload Monitor</strong><small>Aggregated workload, response-time distribution, transactions, users, instances, and database time.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/e067931e0b0a4b2089f4db327879cd55/3440a2f2a8e14faa95acb8a0387dc87e.html" target="_blank" rel="noopener"><span>2025</span><strong>ABAP Statistics</strong><small>Relationship between workload aggregates and individual ABAP statistics records.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_NETWEAVER_750/979cf1522d164bf7a781796efd8850ee/6b96ee764b054c5f929dea77ffcf7a6b.html" target="_blank" rel="noopener"><span>SAP</span><strong>Synchronous and Asynchronous Updating</strong><small>Update-task execution and the restriction on reprocessing synchronous updates.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/6d9d967c861d4f78b5b90a4fe9b7d2e7/fabdd762d87442588c162ff6fa02c138.html" target="_blank" rel="noopener"><span>2025</span><strong>Technical Monitoring Apps</strong><small>Current ABAP Platform app names and IDs for workload, sampled processes, SQL analysis, and runtime errors.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/0cc8af9d2f2e40f38b38b46b49325e2d/2d3e9aff21194e81bbb781384b60b02c.html" target="_blank" rel="noopener"><span>2608</span><strong>SQL Statement Analysis</strong><small>Public Edition SQL performance and resource-consumption analysis.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">gpp_maybe</span>
    <div>
      <p><strong>Operational boundary:</strong> read-only diagnosis comes first. Terminating work processes, deleting locks, repeating updates, deleting queue units, or changing production trace settings can alter business state and require the correct authorization and ownership.</p>
      <p><strong>Release boundary:</strong> exact tools, screens, app IDs, and available metrics depend on the ABAP Platform and SAP S/4HANA deployment and release. Verify the target system before turning a diagnostic pattern into an operating procedure.</p>
    </div>
  </section>
</div>
