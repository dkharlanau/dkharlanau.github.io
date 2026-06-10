---
layout: default
title: "Non-Functional Requirements"
description: "Define measurable quality attributes — performance, availability, security, maintainability — that constrain the solution."
permalink: /skill-hub/architecture/non-functional-requirements-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/architecture/">Architecture</a></li>
    <li aria-current="page">Non-Functional Requirements</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Architecture</p>
  <h1>Non-Functional Requirements</h1>
  <p class="lead">Define measurable quality attributes — performance, availability, security, maintainability — that constrain the solution.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill produces a set of non-functional requirements (NFRs) that constrain a solution design with measurable quality attributes. It moves beyond adjectives like "fast" or "secure" to specific, testable statements like "95th percentile response time under 2 seconds at 1,000 concurrent users" or "RPO under 15 minutes, RTO under 4 hours." The output is used during solution design, vendor evaluation, acceptance testing, and operational handover.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A project has detailed functional requirements but no quality targets, and the vendor proposal lacks performance commitments.</li>
      <li>An existing system is failing under load and you need to define what "enough" means before investing in scaling.</li>
      <li>You are writing a request for proposal and need NFRs that vendors can price and test against.</li>
      <li>An operations team is taking over a system and needs measurable targets for monitoring and alerting.</li>
      <li>A compliance audit found that security and availability requirements were never documented.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Example 1: SAP Fiori launch performance</h3>
    <p>A company rolls out SAP Fiori to 5,000 users. The functional requirements cover which apps and transactions are needed. The NFR work defines that the Fiori launchpad must load in under 3 seconds on a standard corporate laptop with 100 ms latency to the data center, and that search results must return in under 2 seconds for the 95th percentile. Without these numbers, the project cannot validate whether performance issues are in the app, the network, or the backend.</p>

    <h3>Example 2: Integration platform availability</h3>
    <p>A new SAP Integration Suite tenant will handle order-to-cash flows between S/4HANA and a CRM. The business states that "the integration must be reliable." The NFR work translates this into: message delivery success rate of 99.95%, maximum retry duration of 24 hours, alert generation within 5 minutes of failure, and RTO of 2 hours for critical flows. These targets drive the monitoring design and the SLA with the operations team.</p>

    <h3>Example 3: Data warehouse query performance</h3>
    <p>A SAP Datasphere implementation must support month-end reporting for 200 concurrent analysts. The NFR work defines that standard reports must complete in under 30 seconds, ad-hoc queries on pre-aggregated data in under 120 seconds, and that the system must handle 2x peak load without degradation. These numbers determine the sizing, the aggregation strategy, and the need for query optimization.</p>

    <h3>Example 4: Mobile warehouse application security</h3>
    <p>A custom mobile app for SAP EWM runs on handheld devices in a warehouse. The NFR work defines that data transmission must use TLS 1.3, device authentication must require certificate pinning, session timeout must be 15 minutes of inactivity, and offline data must be encrypted at rest using AES-256. These requirements drive the mobile architecture and the MDM policy.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Business context: user count, transaction volume, peak patterns, geographic distribution.</li>
      <li>Existing system baselines: current performance, availability, and incident history (if replacing or extending).</li>
      <li>Regulatory and compliance requirements: GDPR, SOX, industry-specific rules that affect security, retention, or audit.</li>
      <li>Operational constraints: existing monitoring tools, team skills, data center or cloud region limits.</li>
      <li>Stakeholder priorities: which quality attributes matter most (for example: a trading platform values latency over everything; a back-office system values maintainability).</li>
      <li>Budget and timeline: what is feasible to achieve and test within project constraints.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>How many users, transactions, or records must this system handle at peak? What is the growth forecast?</li>
      <li>What is the maximum acceptable downtime per month, and during which hours is downtime most costly?</li>
      <li>Which data is sensitive, who can access it, and what happens if it is exposed or lost?</li>
      <li>How quickly must the system recover after a failure, and how much data can we afford to lose?</li>
      <li>Which browsers, devices, or network conditions must the system support?</li>
      <li>How long must the system be maintainable, and who will maintain it?</li>
      <li>What is the slowest acceptable response time that users will still tolerate for each major function?</li>
      <li>Are there regulatory deadlines for data deletion, encryption, or audit logging?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Identify relevant quality attributes.</strong> From the standard set — Performance, Availability, Security, Scalability, Maintainability, Usability, Compliance — select the 3–5 that matter most for this system. Do not produce NFRs for every attribute if they are not relevant.</li>
      <li><strong>Define metrics for each attribute.</strong> Translate each attribute into one or more measurable metrics. For example, Availability becomes "uptime percentage," "RTO," and "RPO." Performance becomes "response time at percentile," "throughput," and "concurrent user capacity."</li>
      <li><strong>Set targets with context.</strong> For each metric, define a target value and the conditions under which it applies. A target without context is unverifiable. For example: "95th percentile response time under 2 seconds for the top 10 user actions, measured from the application server, under 1,000 concurrent users."</li>
      <li><strong>Classify targets by priority.</strong> Use Must have, Should have, Could have. Must-have NFRs are contractually or operationally critical. Should-have and Could-have NFRs provide flexibility during design and negotiation.</li>
      <li><strong>Map targets to verification methods.</strong> For each NFR, define how it will be tested or monitored: load test, penetration test, operational dashboard, audit log review, user acceptance test.</li>
      <li><strong>Identify dependencies and trade-offs.</strong> Document where NFRs conflict (for example: stronger encryption may increase latency) and how the conflict is resolved.</li>
      <li><strong>Validate with stakeholders.</strong> Review NFRs with business owners, operations, security, and compliance. Confirm that targets are achievable and that verification methods are acceptable.</li>
      <li><strong>Publish the NFR specification.</strong> Format as a structured document with attribute sections, metric tables, priority classifications, and verification plans.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a quality attribute cannot be measured, remove it or redefine it until it is measurable.</li>
      <li>If a target is stricter than the current baseline by more than 10x, require a feasibility study before accepting it.</li>
      <li>If two NFRs conflict, prioritize the one that protects revenue, compliance, or safety; document the trade-off explicitly.</li>
      <li>If an NFR has no defined verification method, classify it as aspirational, not as a requirement.</li>
      <li>If the operations team does not have the tools to monitor an NFR, either provide the tools or remove the NFR.</li>
      <li>If a security NFR is required by regulation, it is always Must have regardless of business priority.</li>
      <li>If an NFR target is copied from a different system without adaptation, validate it against this system's actual usage pattern.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>NFR Specification</strong> — Structured document with quality attributes, metrics, targets, priorities, and verification methods.</li>
      <li><strong>NFR Traceability Matrix</strong> — Table mapping each NFR to design elements, test cases, and monitoring dashboards.</li>
      <li><strong>Trade-off Register</strong> — Documented conflicts between NFRs and how they were resolved.</li>
      <li><strong>Verification Plan</strong> — Schedule and method for testing or monitoring each NFR before go-live and in production.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>NFR Specification (Markdown)</h3>
    <pre><code>## Performance

| ID | Metric | Target | Condition | Priority | Verification |
|----|--------|--------|-----------|----------|--------------|
| PERF-001 | 95th percentile response time | &lt; 2 seconds | Top 10 user actions, 1,000 concurrent users | Must have | Load test in pre-prod |
| PERF-002 | Throughput | &gt; 500 orders/minute | Peak hour, single application node | Must have | Load test |
| PERF-003 | Concurrent user capacity | 2,000 users | Without performance degradation | Should have | Load test |

## Availability

| ID | Metric | Target | Condition | Priority | Verification |
|----|--------|--------|-----------|----------|--------------|
| AVAIL-001 | Uptime | 99.9% | Excluding planned maintenance | Must have | Operational monitoring |
| AVAIL-002 | RTO | &lt; 4 hours | Critical business flows | Must have | Disaster recovery drill |
| AVAIL-003 | RPO | &lt; 15 minutes | All transactional data | Must have | Backup validation |

## Security

| ID | Metric | Target | Condition | Priority | Verification |
|----|--------|--------|-----------|----------|--------------|
| SEC-001 | Data encryption in transit | TLS 1.3 | All external interfaces | Must have | Penetration test |
| SEC-002 | Data encryption at rest | AES-256 | All databases and file stores | Must have | Configuration audit |
| SEC-003 | Session timeout | 15 minutes | Mobile devices, inactivity | Must have | Functional test |
| SEC-004 | Role-based access control | Enforced | All functions and data objects | Must have | Access review |

## Maintainability

| ID | Metric | Target | Condition | Priority | Verification |
|----|--------|--------|-----------|----------|--------------|
| MAINT-001 | Mean time to repair (MTTR) | &lt; 8 hours | P1 incidents | Should have | Incident history review |
| MAINT-002 | Documentation coverage | 100% | Public APIs, integration points | Should have | Documentation audit |
</code></pre>

    <h3>Trade-off Register</h3>
    <pre><code>| ID | NFRs in Conflict | Resolution | Rationale | Impact |
|----|------------------|------------|-----------|--------|
| TR-001 | SEC-001 (TLS 1.3) vs PERF-001 (&lt;2s response) | Accept TLS 1.3; optimize elsewhere | Security is regulatory; latency gain from weaker encryption is marginal | None if caching optimized |
| TR-002 | AVAIL-002 (RTO &lt;4h) vs budget constraint | RTO 4h for critical flows; 24h for non-critical | Cost of 4h RTO for all flows exceeds budget; business accepts tiered recovery | Non-critical flows have longer outage window |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every NFR is measurable with a specific metric and target value.</li>
      <li>Every target includes the conditions under which it applies.</li>
      <li>Every NFR has a priority classification (Must have, Should have, Could have).</li>
      <li>Every Must-have NFR has a defined verification method.</li>
      <li>All conflicts between NFRs are documented with a resolution and rationale.</li>
      <li>The NFRs have been reviewed by operations, security, and business stakeholders.</li>
      <li>No NFR uses unquantified adjectives like "fast," "secure," or "user-friendly."</li>
      <li>The verification plan is achievable within the project timeline and budget.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Writing NFRs as adjectives without metrics. <strong>Consequence:</strong> The design team cannot validate the solution, and disputes about whether quality is met are unresolvable.</li>
      <li><strong>Mistake:</strong> Copying NFRs from a previous project without checking relevance. <strong>Consequence:</strong> A back-office system gets trading-platform latency targets, driving unnecessary cost.</li>
      <li><strong>Mistake:</strong> Defining NFRs that the operations team cannot monitor. <strong>Consequence:</strong> The NFR exists on paper but no one knows when it is violated until a user complains.</li>
      <li><strong>Mistake:</strong> Treating all NFRs as Must have. <strong>Consequence:</strong> The project cannot trade off quality attributes during design, and costs escalate.</li>
      <li><strong>Mistake:</strong> Omitting the verification method. <strong>Consequence:</strong> The NFR is not tested before go-live, and production failures reveal that the target was never achievable.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ol>
      <li><strong>Reject unmeasurable adjectives.</strong> If the user provides an NFR like "the system must be fast," ask for the metric, target, and condition before proceeding.</li>
      <li><strong>Produce the metric table.</strong> Generate the NFR Specification as a Markdown table with ID, Metric, Target, Condition, Priority, and Verification columns.</li>
      <li><strong>Ask for context.</strong> Before setting targets, ask for user count, transaction volume, peak patterns, and regulatory requirements. Do not invent targets.</li>
      <li><strong>Flag conflicts.</strong> If the user provides NFRs that conflict, produce a Trade-off Register and ask for a resolution.</li>
      <li><strong>Link to verification.</strong> For each NFR, suggest a specific verification method. If the user cannot verify it, downgrade the priority or remove it.</li>
      <li><strong>Do not copy generic NFR sets.</strong> Every NFR set must be adapted to the specific system, user base, and operational context.</li>
      <li><strong>Reference Atlas for constraints.</strong> If the system is SAP-related, check <a href="/atlas/concepts/sap-clean-core-strategy/">SAP Clean Core Strategy</a> and <a href="/atlas/concepts/sap-integration-architecture/">SAP Integration Architecture</a> for platform-specific constraints that affect NFR feasibility.</li>
    </ol>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/architecture/solution-architecture-review-working-skill/">Solution Architecture Review</a> — Reviews designs against the NFRs this skill produces.</li>
      <li><a href="/skill-hub/architecture/architecture-decision-record-working-skill/">Architecture Decision Record</a> — Records trade-offs between conflicting NFRs.</li>
      <li><a href="/skill-hub/integration-architecture/integration-observability-working-skill/">Integration Observability</a> — How to monitor NFRs for integration flows.</li>
      <li><a href="/skill-hub/business-analysis/acceptance-criteria-working-skill/">Acceptance Criteria</a> — How NFRs become testable acceptance criteria.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/sap-integration-architecture/">SAP Integration Architecture</a> — Platform-specific constraints on availability and performance.</li>
      <li><a href="/atlas/concepts/sap-clean-core-strategy/">SAP Clean Core Strategy</a> — How clean core affects maintainability and upgrade NFRs.</li>
      <li><a href="/atlas/concepts/event-driven-architecture/">Event-Driven Architecture</a> — Patterns that affect latency, throughput, and availability targets.</li>
      <li><a href="/atlas/concepts/data-mesh-for-sap-landscapes/">Data Mesh for SAP Landscapes</a> — How data mesh patterns affect scalability and ownership NFRs.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of non-functional requirements practice. It is not official ISO, IEEE, or SAP documentation. It focuses on the practical subset of NFRs most commonly needed in enterprise and SAP projects. It does not cover specialized domains such as safety-critical systems, real-time embedded systems, or military-grade security. Use it as a structured method for defining measurable quality targets, not as a comprehensive engineering standards document.</p>
  </section>
</article>
