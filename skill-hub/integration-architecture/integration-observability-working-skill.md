---
layout: default
title: "Integration Observability Working Skill"
description: "Design monitoring and alerting for integrations so failures are detected before business users report them, and diagnostics are fast and repeatable."
permalink: /skill-hub/integration-architecture/integration-observability-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/integration-architecture/">Integration Architecture</a></li>
    <li aria-current="page">Integration Observability</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Integration Architecture</p>
  <h1>Integration Observability Working Skill</h1>
  <p class="lead">Build monitoring that catches integration failures before business impact, and create diagnostic runbooks so the first responder knows exactly what to check.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you map each integration to its business impact, define failure modes and detection methods, set alert thresholds, assign alert recipients, create diagnostic runbooks, and validate the entire monitoring setup with simulated failures.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A new integration is going live and monitoring is "to be defined later."</li>
      <li>Business users report missing data before any technical alert fires.</li>
      <li>Middleware logs show errors but no one reviews them until a business escalation.</li>
      <li>An AMS handover requires operational documentation for existing integrations.</li>
      <li>A middleware or platform upgrade changes logging and alerting behavior.</li>
      <li>SLAs are being defined and you need to prove they can be monitored.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Situation 1: Customer orders stop flowing to the warehouse</h3>
    <p>Orders from the e-commerce platform to SAP S/4 are processed successfully, but the warehouse file transfer from SAP to the logistics system stops. No alert fires because the file transfer job does not have monitoring. The issue is discovered when picking lists do not print the next morning. Warehouse operations lose half a day.</p>
    <h3>Situation 2: Middleware logs show 500 errors but no one acts</h3>
    <p>The API gateway logs hundreds of 500 errors per day for a customer lookup API. The errors are visible in a dashboard but not alerted. The business team assumes SAP is slow. The SAP team assumes the middleware is misconfigured. No one owns the alert, so no one investigates.</p>
    <h3>Situation 3: New integration launched without monitoring</h3>
    <p>A project delivers a new billing integration on time. The go-live checklist has a monitoring item marked "post-go-live." After go-live, the project team disbands. The integration runs silently for two weeks, then fails. There is no runbook, no alert, and no one who knows how to diagnose it.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Interface inventory with ownership matrix.</li>
      <li>SLA requirements: availability, latency, throughput, freshness.</li>
      <li>Middleware monitoring capabilities: dashboards, metrics, log aggregation.</li>
      <li>SAP monitoring tools and transactions: SM58, SMQ1, SMQ2, BD87, WE02, SXI_MONITOR, AIF.</li>
      <li>Alerting infrastructure: email, SMS, paging, ticketing integration.</li>
      <li>Runbook templates or existing operational documentation.</li>
      <li>Business impact mapping: which processes fail when each interface fails.</li>
      <li>Historical incident data: how past failures were detected and resolved.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the business symptom when this integration fails?</li>
      <li>How long can this integration be down before business impact occurs?</li>
      <li>Who receives the alert, and who covers when that person is unavailable?</li>
      <li>What is the escalation path if the first responder cannot resolve the issue?</li>
      <li>What logs and metrics are available for this integration?</li>
      <li>What is the mean time to detect (MTTD) versus mean time to resolve (MTTR)?</li>
      <li>How do we distinguish between a total failure and a partial degradation?</li>
      <li>What is the false positive rate of the current alerts, and how do we tune it?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Map each interface to business impact.</strong> For every interface, document the business process affected, the symptom of failure, and the cost or risk per hour of downtime.</li>
      <li><strong>Define failure modes per interface.</strong> List the ways this interface can fail: timeout, schema mismatch, auth failure, data validation error, rate limit, downstream unavailable, silent data loss.</li>
      <li><strong>Choose detection method per failure mode.</strong> Match the failure to a detectable signal: HTTP status code, queue depth, IDoc status, file absence, data volume anomaly, latency spike.</li>
      <li><strong>Set alert thresholds.</strong> Define the metric, threshold, evaluation window, and severity. Base thresholds on SLA and historical baseline, not guesswork.</li>
      <li><strong>Assign alert recipients.</strong> Each alert goes to a named person or team with accountability, not a broad distribution list.</li>
      <li><strong>Create diagnostic runbook per alert.</strong> For each alert, write: what to check first, which transactions or logs to open, common causes, escalation criteria, and safe actions.</li>
      <li><strong>Test alert with simulated failure.</strong> Trigger each failure mode in a controlled way. Verify the alert fires, the recipient receives it, and the runbook leads to diagnosis.</li>
      <li><strong>Review weekly for the first month after go-live.</strong> Tune thresholds, fix false positives, and update runbooks based on real incidents.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If business impact exceeds $10,000 per hour, alert within 5 minutes of failure detection.</li>
      <li>If the failure is silent (no error code), use data volume, latency, or freshness anomaly detection.</li>
      <li>If SAP is involved, monitor SM58 (tRFC errors), SMQ1/SMQ2 (qRFC queues), BD87/WE02 (IDoc status), and AIF errors.</li>
      <li>If middleware is involved, monitor queue depth, error rate, latency, and consumer lag.</li>
      <li>If an alert fires more than three times per week without action, tune the threshold or fix the root cause.</li>
      <li>If no runbook exists for an alert, create one before the interface goes live.</li>
      <li>If an alert goes to a distribution list with more than five people, replace it with a named owner and an escalation path.</li>
      <li>If a file transfer is involved, monitor file arrival time, file size, and record count, not just job completion.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Monitoring Configuration Specification</strong> — Metrics, thresholds, evaluation windows, severities per interface.</li>
      <li><strong>Alert Matrix</strong> — Alert name, condition, recipient, escalation, runbook link. See template below.</li>
      <li><strong>Diagnostic Runbooks</strong> — One per critical alert: check steps, transactions, common causes, safe actions.</li>
      <li><strong>Integration Health Dashboard Definition</strong> — What to display, refresh rate, audience.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Alert Matrix</h3>
    <pre><code>---
artifact: Alert Matrix
id: ALM-001
date: YYYY-MM-DD
scope: Integration landscape | Project | Domain
---

## Alert definitions

| Alert ID | Interface | Failure Mode | Detection Method | Metric | Threshold | Window | Severity | Recipient | Escalation | Runbook |
|----------|-----------|--------------|------------------|--------|-----------|--------|----------|-----------|------------|---------|
| AL-001 | SAP→CRM Customer API | Timeout / 5xx | HTTP status | Error rate | > 1% | 5 min | P1 | AMS Lead | Integration Mgr | RB-001 |
| AL-002 | SAP→WH IDoc | Status 51 | IDoc status | Status 51 count | > 0 | 15 min | P2 | AMS Team | SAP Dev Lead | RB-002 |
| AL-003 | Bank→SAP File | File missing | File arrival | File age | > 2h | 1h | P1 | AMS Team | Finance Mgr | RB-003 |
| AL-004 | Event: OrderConfirmed | Consumer lag | Kafka lag | Lag per partition | > 10,000 | 5 min | P2 | Integration Team | Event Owner | RB-004 |

## Runbook index

| Runbook ID | Alert IDs | First Check | Key Transactions / Logs | Common Causes | Safe Actions | Escalation Criteria |
|------------|-----------|-------------|---------------------------|---------------|--------------|---------------------|
| RB-001 | AL-001 | Middleware health dashboard | API gateway logs, SAP SM58 | Auth expiry, SAP overload | Check SM58, verify token | > 3 failures in 1h |
| RB-002 | AL-002 | BD87 / WE02 for status 51 | IDoc content, segment details | Data validation, missing mapping | Review IDoc, check AIF | > 10 IDocs stuck |
| RB-003 | AL-003 | File transfer job log | Job scheduler, file system | Network issue, job failure | Verify job status, check path | File > 4h missing |
| RB-004 | AL-004 | Kafka consumer group lag | Consumer metrics, logs | Consumer down, slow processing | Check consumer health, restart | Lag growing > 1h |

## Review log
| Date | Action | Owner |
|------|--------|-------|
| YYYY-MM-DD | Initial creation | Name |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every critical interface has at least one alert.</li>
      <li>Every alert has a defined threshold and evaluation window.</li>
      <li>Every alert has a named recipient with accountability.</li>
      <li>A runbook exists for every alert that pages outside business hours.</li>
      <li>False positive rate is under 20% after the first month.</li>
      <li>Business impact is documented per interface.</li>
      <li>Simulated failure test confirmed alert delivery and runbook accuracy.</li>
      <li>Dashboard shows both technical health and business outcome indicators.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Monitoring middleware health only, not business outcome. <strong>Consequence:</strong> The queue is healthy but no messages are flowing; the alert never fires.</li>
      <li><strong>Mistake:</strong> Alerting on every error without threshold tuning. <strong>Consequence:</strong> Alert fatigue; real failures are buried in noise.</li>
      <li><strong>Mistake:</strong> No runbook, so the recipient does not know what to do. <strong>Consequence:</strong> Alerts are acknowledged and ignored, or escalated blindly.</li>
      <li><strong>Mistake:</strong> Alert goes to a distribution list with no accountability. <strong>Consequence:</strong> Everyone assumes someone else will handle it.</li>
      <li><strong>Mistake:</strong> Monitoring job completion but not file content or record count. <strong>Consequence:</strong> Empty files or truncated transfers go undetected.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <ul>
      <li><strong>Map to business impact first:</strong> Before choosing technical metrics, document what business process fails and how fast.</li>
      <li><strong>Use SAP-specific monitoring transactions:</strong> Reference SM58, SMQ1/SMQ2, BD87, WE02, and AIF for SAP-centric integrations.</li>
      <li><strong>Produce an Alert Matrix and runbooks:</strong> Do not stop at a list of metrics. Deliver actionable artifacts.</li>
      <li><strong>Avoid generic language:</strong> Do not write "monitoring is important for reliability." Write "Alert on IDoc status 51 within 15 minutes."</li>
      <li><strong>Handle missing infrastructure:</strong> If alerting infrastructure is missing, list it as a dependency and block go-live until resolved.</li>
      <li><strong>Link to Atlas diagnostics:</strong> Reference <a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">SAP Interface Monitoring Diagnostics</a>, <a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a>, and <a href="/atlas/diagnostics/sap-qrfc-trfc-diagnostics/">SAP qRFC/tRFC Diagnostics</a> for specific check steps.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/integration-architecture/integration-error-handling-working-skill/">Integration Error Handling</a> — Design what happens when monitoring detects a failure.</li>
      <li><a href="/skill-hub/integration-architecture/interface-ownership-working-skill/">Interface Ownership</a> — Assign alert recipients and runbook owners.</li>
      <li><a href="/skill-hub/sap-ams/incident-triage-working-skill/">Incident Triage</a> — Respond when alerts fire.</li>
      <li><a href="/skill-hub/sap-ams/root-cause-analysis-working-skill/">Root Cause Analysis</a> — Investigate recurring alert patterns.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">SAP Interface Monitoring Diagnostics</a> — SAP-specific monitoring.</li>
      <li><a href="/atlas/diagnostics/sap-integration-error-handling-diagnostics/">SAP Integration Error Handling Diagnostics</a> — Error patterns to monitor.</li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — IDoc failure detection.</li>
      <li><a href="/atlas/diagnostics/sap-qrfc-trfc-diagnostics/">SAP qRFC / tRFC Diagnostics</a> — Queue monitoring.</li>
      <li><a href="/atlas/diagnostics/sap-outbound-processing-diagnostics/">SAP Outbound Processing Diagnostics</a> — Outbound failure patterns.</li>
      <li><a href="/atlas/diagnostics/sap-inbound-processing-diagnostics/">SAP Inbound Processing Diagnostics</a> — Inbound failure patterns.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of integration observability practice. It is not official SAP, Datadog, Splunk, or vendor documentation. SAP-specific monitoring references standard transactions available in common S/4HANA and ECC releases; custom landscapes may have additional or different tools. The skill assumes some form of middleware or platform monitoring exists; if none exists, the first step is infrastructure procurement, not configuration.</p>
  </section>
</article>
