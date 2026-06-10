---
layout: default
title: "Integration Error Handling Working Skill"
description: "Design retry, dead letter, and escalation logic so transient failures recover safely and permanent failures escalate correctly."
permalink: /skill-hub/integration-architecture/integration-error-handling-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/integration-architecture/">Integration Architecture</a></li>
    <li aria-current="page">Integration Error Handling</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Integration Architecture</p>
  <h1>Integration Error Handling Working Skill</h1>
  <p class="lead">Classify integration failures, design retry and dead letter behavior, and build escalation paths so no message is lost silently and no permanent failure is retried forever.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you classify integration failures by type, design a retry policy that handles transient failures without causing storms, define dead letter criteria and reprocess workflows, create escalation paths for unresolvable errors, and document the error handling policy so operators and consumers know what to expect.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>You are designing a new integration and need to define what happens when it fails.</li>
      <li>Recurring failures are exhausting support capacity with manual retries.</li>
      <li>A dead letter queue is filling up and no one knows the reprocess procedure.</li>
      <li>Retry logic is causing cascading failures or thundering herds on recovering systems.</li>
      <li>An audit finding notes missing message reliability or traceability.</li>
      <li>Consumers report they cannot tell whether a failure is retryable or fatal.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Situation 1: Manual IDoc retries 20 times per day</h3>
    <p>Customer master IDocs fail in SAP with status 51 due to a mapping validation error. The AMS operator manually reprocesses each IDoc in BD87 after fixing the data. This happens 20 times per day. There is no automated retry, no root cause fix, and no escalation when the volume spikes.</p>
    <h3>Situation 2: API consumer does not know whether to retry</h3>
    <p>A downstream system calls a REST API and receives a 500 error. The consumer has no documentation on whether this is transient or permanent. It retries immediately, then again, then again. The API is already overloaded; the retries make it worse. Eventually the consumer gives up and drops the request.</p>
    <h3>Situation 3: Dead letter queue fills with no review process</h3>
    <p>An event broker routes failed events to a dead letter topic. The topic grows by hundreds of messages per week. There is no scheduled review, no reprocess runbook, and no owner. After six months, the team discovers that a whole category of orders was never processed.</p>
    <h3>Situation 4: Retry storm on recovering downstream system</h3>
    <p>A downstream billing system goes down for maintenance. When it comes back, all queued messages retry simultaneously. The billing system is overwhelmed and fails again. The cycle repeats until the queue is manually paused.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Interface inventory with failure history.</li>
      <li>Middleware retry capabilities: max retries, backoff options, dead letter support.</li>
      <li>SAP error handling tools: AIF, IDoc status, qRFC, tRFC, BD87, SM58.</li>
      <li>SLA requirements: max acceptable delay, ordering requirements.</li>
      <li>Dead letter queue or topic configuration.</li>
      <li>Consumer retry behavior: what consumers do on failure.</li>
      <li>Escalation contacts: who handles unresolvable errors per interface.</li>
      <li>Business impact per failure type: cost of delay, cost of data loss.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Is this failure transient (network, timeout, downstream restart) or permanent (schema mismatch, validation error, bad data)?</li>
      <li>What is the maximum retry count, and what happens after the last retry?</li>
      <li>What is the backoff strategy: fixed, linear, exponential, or custom?</li>
      <li>Who reviews dead letter messages, and how often?</li>
      <li>How is a poison message identified and quarantined?</li>
      <li>What is the business impact of delayed reprocessing versus immediate rejection?</li>
      <li>How does the consumer know a message failed, and what action should it take?</li>
      <li>If message ordering matters, how do retries preserve or recover sequence?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Classify failure types per interface.</strong> For each interface, list the failure modes and classify each as transient, permanent, or data-related. Document the symptom and root cause pattern.</li>
      <li><strong>Define retry policy per type.</strong> For transient failures, define max retries, backoff strategy, and jitter. For permanent failures, define immediate dead letter or rejection.</li>
      <li><strong>Define dead letter criteria.</strong> Specify when a message goes to dead letter: max retries exceeded, permanent failure, poison message, schema validation failure.</li>
      <li><strong>Design escalation path.</strong> For dead letter messages, define: who reviews, how often, what tools they use, and when to escalate to development or business.</li>
      <li><strong>Create reprocess runbook.</strong> Document the safe steps to reprocess a dead letter message: validation, environment, order preservation, idempotency check, confirmation.</li>
      <li><strong>Test failure scenarios.</strong> Simulate each failure type in a controlled environment. Verify retry behavior, dead letter routing, alert firing, and runbook accuracy.</li>
      <li><strong>Monitor retry and dead letter metrics.</strong> Track retry rate, dead letter growth rate, time-to-review, and reprocess success rate. Alert on anomalies.</li>
      <li><strong>Review weekly.</strong> For the first month after go-live, review failure patterns, tune retry parameters, and update runbooks based on real behavior.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the failure is a network error or timeout, retry with exponential backoff and jitter.</li>
      <li>If the failure is a schema mismatch or data validation error, send to dead letter immediately; do not retry.</li>
      <li>If retry count exceeds three without success, escalate to human review and stop automatic retry.</li>
      <li>If the dead letter queue grows by more than ten messages per day, trigger a process review.</li>
      <li>If the consumer is external, provide explicit error codes distinguishing retryable from non-retryable failures.</li>
      <li>If SAP IDoc fails, use AIF for structured error handling, categorization, and reprocessing.</li>
      <li>If message ordering matters, retry in sequence or use idempotency so out-of-order reprocessing is safe.</li>
      <li>If a downstream system is recovering, use circuit breaker or rate-limited retry to prevent thundering herds.</li>
      <li>If a message fails with the same permanent error on every retry, classify it as a poison message and quarantine it.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Error Handling Policy per Interface</strong> — Failure types, retry policy, dead letter criteria. See template below.</li>
      <li><strong>Retry Configuration Specification</strong> — Max retries, backoff, jitter, circuit breaker settings.</li>
      <li><strong>Dead Letter Process</strong> — Review schedule, owner, tools, escalation.</li>
      <li><strong>Escalation Matrix</strong> — Who handles what, when to escalate, contact paths.</li>
      <li><strong>Reprocess Runbook</strong> — Safe steps to reprocess dead letter messages.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Error Handling Policy</h3>
    <pre><code>---
artifact: Error Handling Policy
id: EHP-001
interface: Interface ID
status: draft | reviewed | approved
---

## Interface
<!-- Source → Target, protocol -->

## Failure type classification

| Failure Type | Symptom | Root Cause | Retryable | Max Retries | Backoff | Action After Max |
|--------------|---------|------------|-----------|-------------|---------|------------------|
| Transient timeout | HTTP 504, connection reset | Network, downstream restart | Yes | 3 | Exponential 1s→8s | Dead letter + alert |
| Schema mismatch | HTTP 400, validation error | Contract change, bad payload | No | 0 | N/A | Dead letter + alert |
| Auth failure | HTTP 401, 403 | Expired token, permission change | Yes* | 2 | Fixed 5s | Dead letter + alert |
| Rate limit | HTTP 429 | Consumer over limit | Yes | 5 | Exponential 1s→30s | Dead letter + alert |
| Data validation | IDoc status 51, AIF error | Mapping, missing field | No | 0 | N/A | Dead letter + business review |
| Downstream unavailable | HTTP 503, queue full | Maintenance, overload | Yes | 3 | Exponential 2s→16s | Dead letter + alert |

*Auth failure is retryable only if token refresh is automated.

## Dead letter configuration

| Attribute | Value |
|-----------|-------|
| Dead letter destination | Topic / Queue / Table |
| Retention | 30 days |
| Review frequency | Daily |
| Review owner | Name / Team |
| Escalation threshold | > 10 messages / day |

## Reprocess runbook reference
<!-- Link to runbook ID -->

## Consumer error contract
| Error Code | Retryable | Consumer Action |
|------------|-----------|-----------------|
| E001 | Yes | Backoff 5s and retry |
| E002 | No | Log and stop; contact support |

## Owner
<!-- Technical owner + operational owner -->

## Review date
<!-- When this policy is revalidated -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every interface has classified failure types with clear retryable / non-retryable distinction.</li>
      <li>Retry policy is documented with max count, backoff, and jitter.</li>
      <li>Dead letter process exists with named reviewer and review frequency.</li>
      <li>Escalation path is defined with thresholds.</li>
      <li>Reprocess runbook is tested in a non-production environment.</li>
      <li>No silent message loss: every failure is logged, alerted, or routed to dead letter.</li>
      <li>Consumer receives actionable error information (retryable flag, error code, description).</li>
      <li>Circuit breaker or rate limit is configured for downstream recovery scenarios.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Infinite retry on permanent failures. <strong>Consequence:</strong> Resources are wasted, logs fill, and the real problem is never escalated.</li>
      <li><strong>Mistake:</strong> No dead letter process. <strong>Consequence:</strong> Failed messages are dropped or accumulate indefinitely.</li>
      <li><strong>Mistake:</strong> Silent failures (no alert, no log, no dead letter). <strong>Consequence:</strong> Data loss is discovered days or weeks later during reconciliation.</li>
      <li><strong>Mistake:</strong> Retry without idempotency, causing duplicates. <strong>Consequence:</strong> Downstream systems process the same message multiple times.</li>
      <li><strong>Mistake:</strong> Different error handling for the same interface depending on which consumer reports it. <strong>Consequence:</strong> Inconsistent behavior and untraceable failures.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <ul>
      <li><strong>Classify failures before designing retry:</strong> Do not assume all failures are transient. Separate network, auth, schema, data, and downstream failures.</li>
      <li><strong>Use SAP-specific tools:</strong> For SAP IDoc and RFC failures, reference AIF, BD87, SM58, and qRFC monitoring. Link to Atlas diagnostics.</li>
      <li><strong>Ensure idempotency:</strong> Every retryable interface must have an idempotency mechanism documented.</li>
      <li><strong>Produce artifacts:</strong> Generate an Error Handling Policy, reprocess runbook, and escalation matrix. Do not stop at general advice.</li>
      <li><strong>Avoid generic language:</strong> Do not write "implement robust error handling." Write "Retry transient timeouts up to 3 times with exponential backoff; route schema mismatches to dead letter immediately."</li>
      <li><strong>Handle missing information:</strong> If middleware dead letter capabilities are unknown, list them as a blocking dependency.</li>
      <li><strong>Link to Atlas diagnostics:</strong> Reference <a href="/atlas/concepts/retry-and-error-handling/">Retry and Error Handling</a>, <a href="/atlas/concepts/dead-letter-queue/">Dead Letter Queue</a>, <a href="/atlas/concepts/idempotency/">Idempotency</a>, and <a href="/atlas/diagnostics/sap-integration-error-handling-diagnostics/">SAP Integration Error Handling Diagnostics</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/integration-architecture/integration-observability-working-skill/">Integration Observability</a> — Detect failures so error handling can trigger.</li>
      <li><a href="/skill-hub/integration-architecture/api-integration-working-skill/">API Integration</a> — Define error contracts for APIs.</li>
      <li><a href="/skill-hub/integration-architecture/event-driven-architecture-working-skill/">Event-Driven Architecture</a> — Handle event delivery failures.</li>
      <li><a href="/skill-hub/integration-architecture/interface-ownership-working-skill/">Interface Ownership</a> — Assign dead letter review and escalation owners.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/retry-and-error-handling/">Retry and Error Handling</a> — Conceptual foundation.</li>
      <li><a href="/atlas/concepts/dead-letter-queue/">Dead Letter Queue</a> — Dead letter patterns.</li>
      <li><a href="/atlas/concepts/idempotency/">Idempotency</a> — Safe retry design.</li>
      <li><a href="/atlas/diagnostics/sap-integration-error-handling-diagnostics/">SAP Integration Error Handling Diagnostics</a> — SAP-specific patterns.</li>
      <li><a href="/atlas/diagnostics/sap-qrfc-trfc-diagnostics/">SAP qRFC / tRFC Diagnostics</a> — Queue retry and monitoring.</li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — IDoc failure classification.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of integration error handling practice. It is not official SAP, AWS, Azure, or vendor documentation. SAP-specific guidance references standard AIF, IDoc, and RFC mechanisms available in common releases; custom implementations may differ. The skill assumes middleware provides some form of retry and dead letter capability; if not, the first step is capability assessment, not policy design.</p>
  </section>
</article>
