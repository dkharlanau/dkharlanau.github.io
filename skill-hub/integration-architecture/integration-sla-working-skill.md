---
layout: default
title: "Integration SLA and SLO Design Working Skill"
description: "Turn business expectations into measurable availability, latency, throughput, and freshness objectives with clear KPIs, measurement points, and breach actions."
permalink: /skill-hub/integration-architecture/integration-sla-working-skill/
last_modified_at: 2026-09-26
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/integration-architecture/">Integration Architecture</a></li>
    <li aria-current="page">SLA and SLO Design</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Integration Architecture</p>
  <h1>Integration SLA and SLO Design Working Skill</h1>
  <p class="lead">Translate business expectations into measurable service objectives. Define what availability, latency, throughput, and freshness mean for this interface, where each metric is measured, and what happens when the target is missed.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you move from vague requirements such as <em>highly available</em>, <em>real time</em>, or <em>fast enough</em> to measurable service levels. The result is not just a percentage. It is a complete control model: <mark class="key-idea">business need → measurable objective → measurement point → threshold → owner → breach action.</mark></p>
    <p>Use it before choosing or approving an integration pattern, and again before go-live to prove that monitoring and capacity can support the commitment.</p>
  </section>

  <section>
    <h2>The mental model: SLA, SLO, SLI, and KPI</h2>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="SLA SLO SLI and KPI comparison">
      <table class="study-table__table">
        <thead>
          <tr>
            <th scope="col">Term</th>
            <th scope="col">What it means</th>
            <th scope="col">Example</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">SLA</th>
            <td>A service commitment agreed with a consumer or business stakeholder. It may include consequences, escalation, or support obligations.</td>
            <td>Customer-order API availability is at least 99.9% per calendar month during the agreed service window.</td>
          </tr>
          <tr>
            <th scope="row">SLO</th>
            <td>A measurable objective used to design and operate the service. It can be internal or part of an SLA.</td>
            <td>99% of valid order requests complete in less than 800 ms at p99 load profile.</td>
          </tr>
          <tr>
            <th scope="row">SLI</th>
            <td>The indicator used to measure the objective.</td>
            <td>Successful eligible requests divided by all eligible requests.</td>
          </tr>
          <tr>
            <th scope="row">KPI</th>
            <td>A broader performance metric used for operations or management. Some KPIs can also be SLIs.</td>
            <td>Queue depth, retry rate, p95 latency, consumer lag, or age of last successful file.</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p><mark class="key-idea">Do not start with a target such as 99.9%.</mark> Start with the business process, the failure impact, and the time window in which the consumer needs a usable outcome.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A project says an interface must be "real time" but no one can state the maximum acceptable delay.</li>
      <li>An API team has an uptime target but no agreed latency percentile or load profile.</li>
      <li>An event stream is fast in testing but consumer lag grows during peak volume.</li>
      <li>A batch file arrives successfully, but the business still works with yesterday's data.</li>
      <li>An observability team needs thresholds that come from business requirements instead of guesswork.</li>
      <li>Different consumers ask for different service levels and the architecture team needs to decide whether one service tier can support them.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Situation 1: "Real time" order confirmation</h3>
    <p>Sales asks for real-time order confirmation from SAP. One consumer is an interactive portal and needs a response in under one second for almost every request. Another consumer only refreshes a dashboard every five minutes. A single vague requirement would over-design one path and under-design the other.</p>

    <h3>Situation 2: API is up, but users still see failures</h3>
    <p>The API gateway health check reports 100% uptime. During a month-end peak, 8% of requests time out at the consumer because the downstream SAP service is saturated. Infrastructure availability looks healthy, but consumer-visible availability is not.</p>

    <h3>Situation 3: Batch job succeeds but data is stale</h3>
    <p>A nightly supplier extract finishes without technical errors. The source job starts six hours late, so the file is already stale when it reaches the analytics platform. Availability is fine. Freshness is not.</p>

    <h3>Situation 4: Throughput hides a growing backlog</h3>
    <p>An event consumer processes 500 messages per second and the team calls that good throughput. Peak incoming volume is 650 messages per second, so the queue grows every minute. The measured processing rate is not enough to meet the business deadline.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Business process and consumer journey affected by the integration.</li>
      <li>Critical business deadlines: response time, cut-off time, posting window, shipment window, or reporting deadline.</li>
      <li>Normal, peak, and burst volume profile.</li>
      <li>Consumer list and any different service needs by consumer.</li>
      <li>Existing incident and performance history where available.</li>
      <li>System and middleware monitoring capabilities.</li>
      <li>Dependency map: source, middleware, network, target, broker, database, and external services.</li>
      <li>Support hours, maintenance windows, and operational ownership.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What business outcome is unavailable when this integration fails?</li>
      <li>How long can the business wait before the delay becomes material?</li>
      <li>Where should time measurement start, and where should it stop?</li>
      <li>What counts as a successful request, message, file, or data refresh?</li>
      <li>What traffic is eligible for the SLA and what is explicitly excluded?</li>
      <li>What is the expected peak load, not only the daily average?</li>
      <li>Do all consumers need the same target?</li>
      <li>Which dependencies consume part of the end-to-end service budget?</li>
      <li>Can the proposed KPI actually be measured in production?</li>
      <li>Who acts when the objective is breached?</li>
    </ul>
  </section>

  <section>
    <h2>The four core service dimensions</h2>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Integration SLA dimensions">
      <table class="study-table__table">
        <thead>
          <tr>
            <th scope="col">Dimension</th>
            <th scope="col">Question it answers</th>
            <th scope="col">Useful KPIs / SLIs</th>
            <th scope="col">Common design effect</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">Availability</th>
            <td>Can the consumer successfully use the integration during the agreed service window?</td>
            <td>Successful request ratio; successful scheduled-run ratio; unavailable minutes; failed transaction ratio.</td>
            <td>Redundancy, failover, dependency design, maintenance policy, recovery process.</td>
          </tr>
          <tr>
            <th scope="row">Latency</th>
            <td>How long does one business request or event take from the agreed start point to a usable result?</td>
            <td>p50, p95, p99 latency; percentage within threshold; timeout ratio; end-to-end event delay.</td>
            <td>Synchronous vs asynchronous pattern, batching, retry delay, network path, queueing, caching.</td>
          </tr>
          <tr>
            <th scope="row">Throughput</th>
            <td>How much work can the integration complete while still meeting its other objectives?</td>
            <td>Completed requests per second; messages per minute; records per hour; peak sustained rate; backlog growth; consumer lag.</td>
            <td>Capacity, partitioning, parallelism, backpressure, rate limits, scaling model.</td>
          </tr>
          <tr>
            <th scope="row">Freshness</th>
            <td>How old is the information when the consumer can use it?</td>
            <td>Age of data; percentage delivered within freshness window; last successful update age; batch arrival delay.</td>
            <td>Batch frequency, CDC or events, cache policy, replication design, scheduling and cut-off logic.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Availability: define usable service, not server uptime</h2>
    <p>Availability is only meaningful after you define the unit of service and the eligible window. A health endpoint can be green while business requests fail downstream.</p>
    <p>For a request-driven interface, a useful starting formula is:</p>
    <pre><code>request availability = successful eligible requests / all eligible requests × 100</code></pre>
    <p>For a scheduled batch interface, the unit may be a completed delivery window instead:</p>
    <pre><code>batch availability = successful deliveries within the agreed window / eligible scheduled deliveries × 100</code></pre>
    <p>Define what counts as <strong>successful</strong>, <strong>eligible</strong>, and <strong>excluded</strong>. Planned maintenance, invalid consumer requests, dependency failures, and force-majeure events must not be silently removed from the denominator. Their treatment belongs in the agreement.</p>

    <h3>Availability target translated into time budget</h3>
    <p>If availability is measured as wall-clock time over a 30-day, 24×7 window, the percentage creates a concrete unavailable-time budget:</p>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Thirty day availability time budget examples">
      <table class="study-table__table">
        <thead>
          <tr>
            <th scope="col">Availability target</th>
            <th scope="col">Maximum unavailable time in 30 days</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>99.0%</td><td>7 h 12 min</td></tr>
          <tr><td>99.9%</td><td>43 min 12 s</td></tr>
          <tr><td>99.95%</td><td>21 min 36 s</td></tr>
          <tr><td>99.99%</td><td>4 min 19 s</td></tr>
        </tbody>
      </table>
    </div>
    <p>These are examples, not recommended targets. The correct target depends on the business process and the measurement method.</p>
  </section>

  <section>
    <h2>Latency: measure the path the business actually waits for</h2>
    <p>Latency is a duration. The hard part is choosing the correct start and stop points. For an API it may be from gateway acceptance to complete response. For an event it may be from the business fact timestamp to the moment the consumer can use the event.</p>
    <pre><code>end-to-end latency =
source processing
+ network and middleware time
+ queue wait
+ target processing</code></pre>
    <p><mark class="key-idea">Do not use the average alone.</mark> A good average can hide slow tail requests. Use percentiles such as p95 or p99 and, where useful, the percentage of transactions completed within the business threshold.</p>
    <p>Useful KPIs include p50, p95, p99, timeout ratio, queue wait time, and end-to-end event delay.</p>
  </section>

  <section>
    <h2>Throughput: measure completed work under realistic load</h2>
    <p>Throughput is the rate at which useful work completes. It is not the same as a configured rate limit and it is not enough to quote the fastest test result.</p>
    <pre><code>throughput = completed business units / elapsed time</code></pre>
    <p>Measure sustained performance at normal and peak demand. Compare incoming rate with completed rate. If incoming work is consistently higher than completed work, backlog grows even when the throughput number looks large.</p>
    <p>Useful KPIs include completed requests per second, messages per minute, records per hour, peak sustained rate, queue depth, backlog growth rate, consumer lag, and resource saturation.</p>
  </section>

  <section>
    <h2>Freshness: measure the age of usable information</h2>
    <p>Freshness is different from latency. Latency measures how long processing takes. Freshness measures how old the information is when the consumer can use it.</p>
    <pre><code>freshness age = consumer-usable timestamp - source business timestamp</code></pre>
    <p>A batch job can have low processing latency and still deliver stale data if it starts late. An API can have 200 ms response latency and still return data that was replicated two hours ago.</p>
    <p>Useful KPIs include age of newest record, percentage of records within the freshness window, time since last successful update, batch arrival delay, CDC lag, and event consumer lag.</p>
  </section>

  <section>
    <h2>Choose KPIs by integration pattern</h2>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="SLA KPIs by integration pattern">
      <table class="study-table__table">
        <thead>
          <tr>
            <th scope="col">Pattern</th>
            <th scope="col">Availability</th>
            <th scope="col">Latency</th>
            <th scope="col">Throughput</th>
            <th scope="col">Freshness</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">Synchronous API</th>
            <td>Successful eligible request ratio</td>
            <td>p95 / p99 response time</td>
            <td>Completed requests per second under agreed load</td>
            <td>Needed when the API serves replicated, cached, or delayed data</td>
          </tr>
          <tr>
            <th scope="row">Event stream</th>
            <td>Successful event publication and consumption</td>
            <td>Business fact to consumer-usable event</td>
            <td>Messages per second plus backlog growth</td>
            <td>Consumer lag or age of latest consumed event</td>
          </tr>
          <tr>
            <th scope="row">Batch / file</th>
            <td>Successful delivery within the agreed window</td>
            <td>Job or transfer completion duration</td>
            <td>Records or files processed per unit of time</td>
            <td>Age of data at delivery and time since last successful refresh</td>
          </tr>
          <tr>
            <th scope="row">Data product</th>
            <td>Output-port availability</td>
            <td>Query or delivery delay</td>
            <td>Consumer concurrency or delivery capacity</td>
            <td>Data age against the product freshness objective</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Start from business impact.</strong> Identify the business outcome, deadline, and cost of delay or unavailability.</li>
      <li><strong>Define the service unit.</strong> Decide whether you measure a request, event, message group, file, batch delivery, or data-product refresh.</li>
      <li><strong>Set measurement boundaries.</strong> Write the exact start point, stop point, service window, and eligible population for every metric.</li>
      <li><strong>Choose the SLI or KPI.</strong> Select the smallest set of metrics that proves the business requirement. Avoid collecting metrics with no decision attached.</li>
      <li><strong>Set the objective.</strong> Define the target, evaluation window, percentile where needed, and any separate peak-load condition.</li>
      <li><strong>Map dependencies and budgets.</strong> Identify which source, middleware, broker, network, and target components consume the end-to-end budget.</li>
      <li><strong>Test against realistic load.</strong> Validate normal, peak, burst, dependency failure, retry, and recovery behavior before committing to the SLA.</li>
      <li><strong>Connect objectives to monitoring.</strong> Create production measurements, thresholds, dashboards, and alerts that use the same definitions as the SLA.</li>
      <li><strong>Assign breach actions.</strong> Define who responds, when escalation starts, and what evidence proves recovery.</li>
      <li><strong>Review with real data.</strong> Compare observed performance with the objective after go-live and adjust architecture or the agreement when evidence shows the target is wrong.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Integration SLA decision rules">
      <table class="study-table__table">
        <thead>
          <tr>
            <th scope="col">Condition</th>
            <th scope="col">Decision</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>The business can only use the process when the end-to-end transaction succeeds.</td>
            <td>Measure consumer-visible availability, not only middleware or server health.</td>
          </tr>
          <tr>
            <td>Slow tail requests can break the user or downstream process.</td>
            <td>Use p95 or p99 latency and a within-threshold ratio; do not use the average alone.</td>
          </tr>
          <tr>
            <td>Incoming peak volume is higher than sustained completed throughput.</td>
            <td>Fix capacity, backpressure, scaling, or pattern choice before committing to the target.</td>
          </tr>
          <tr>
            <td>A batch or replicated dataset can be old even when delivery succeeds.</td>
            <td>Define freshness separately from availability and processing latency.</td>
          </tr>
          <tr>
            <td>Consumers have materially different requirements.</td>
            <td>Define consumer-specific objectives or explicit service tiers instead of forcing one target on all consumers.</td>
          </tr>
          <tr>
            <td>Strict event ordering is required.</td>
            <td>Include its effect on parallelism, throughput, latency, retry, and replay in the service objective.</td>
          </tr>
          <tr>
            <td>The proposed measurement point is not observable in production.</td>
            <td>Add telemetry before making the objective a committed SLA.</td>
          </tr>
          <tr>
            <td>The service objective depends on downstream systems.</td>
            <td>Document dependency budgets and escalation paths; do not hide normal dependency failures in exclusions.</td>
          </tr>
          <tr>
            <td>No reliable performance baseline exists.</td>
            <td>Measure first and label any temporary objective as provisional before making a contractual commitment.</td>
          </tr>
          <tr>
            <td>A KPI can breach without a named owner or action.</td>
            <td>Treat it as reporting only. Add ownership and a runbook before calling it an operational control.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Deliverables</h2>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Integration SLA deliverables">
      <table class="study-table__table">
        <thead>
          <tr>
            <th scope="col">Deliverable</th>
            <th scope="col">What it contains</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">SLA / SLO Definition</th>
            <td>Business outcome, service window, objectives, targets, exclusions, and breach rules.</td>
          </tr>
          <tr>
            <th scope="row">SLI / KPI Measurement Map</th>
            <td>Metric formula, start and stop points, data source, aggregation window, and dashboard location.</td>
          </tr>
          <tr>
            <th scope="row">Capacity and Load Envelope</th>
            <td>Normal, peak, and burst demand plus tested sustainable throughput and latency behavior.</td>
          </tr>
          <tr>
            <th scope="row">Dependency Budget Map</th>
            <td>How source, middleware, network, broker, and target components consume the end-to-end objective.</td>
          </tr>
          <tr>
            <th scope="row">Breach and Escalation Matrix</th>
            <td>Threshold, severity, owner, first action, escalation path, and recovery evidence.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Template</h2>
    <h3>Integration Service Level Brief</h3>
    <pre><code>---
artifact: Integration Service Level Brief
id: SLA-001
interface: Interface ID
status: draft | reviewed | approved
---

## Business outcome
&lt;What business process depends on this integration?&gt;

## Consumer and service window
&lt;Consumer / 24x7 / business hours / batch cut-off window&gt;

## Measurement boundaries
&lt;Exact start point → exact point where the consumer can use the result&gt;

## Objectives

| Dimension | SLI / KPI | Target | Evaluation window | Measurement point | Breach action |
|-----------|-----------|--------|-------------------|-------------------|---------------|
| Availability | Successful eligible requests / eligible requests | &lt;target&gt; | Monthly | Consumer edge | Page operational owner |
| Latency | p99 end-to-end duration | &lt;target&gt; | 5 min + monthly | Start → usable result | Investigate saturation / queue |
| Throughput | Completed business units per second | &lt;target&gt; | Peak load window | End-to-end | Scale / backpressure review |
| Freshness | Consumer-usable time - source business time | &lt;target&gt; | Continuous / per batch | Source timestamp → consumer | Data pipeline incident |

## Load profile
&lt;Normal, peak, burst, concurrency&gt;

## Dependencies and budgets
&lt;Source, middleware, broker, network, target, external services&gt;

## Exclusions
&lt;Explicit and agreed exclusions only&gt;

## Owners
Business owner:
Technical owner:
Operational owner:
Consumer representative:

## Evidence
&lt;Baseline, load-test result, monitoring query, dashboard&gt;

## Review date
YYYY-MM-DD
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Each objective is tied to a business outcome or deadline.</li>
      <li>Availability defines the eligible population and what counts as success.</li>
      <li>Latency has explicit start and stop points and uses a percentile where tail behavior matters.</li>
      <li>Throughput is tested at normal, peak, and burst demand, not only quoted from configuration.</li>
      <li>Freshness is defined separately when data can be stale even if transport succeeds.</li>
      <li>Every target has an evaluation window and measurement source.</li>
      <li>Dependencies and exclusions are explicit.</li>
      <li>Production telemetry can calculate every committed metric.</li>
      <li>Each breach has a named operational owner and action.</li>
      <li>The objective was tested against realistic load and failure conditions before approval.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Common integration SLA mistakes">
      <table class="study-table__table">
        <thead>
          <tr>
            <th scope="col">Mistake</th>
            <th scope="col">Consequence</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">Writing "99.9%" without a denominator or service window</th>
            <td>The number cannot be measured consistently and teams argue about every breach.</td>
          </tr>
          <tr>
            <th scope="row">Using average latency only</th>
            <td>Slow tail requests disappear inside a healthy average while users still time out.</td>
          </tr>
          <tr>
            <th scope="row">Treating rate limit as throughput</th>
            <td>The configured ceiling is mistaken for proven capacity.</td>
          </tr>
          <tr>
            <th scope="row">Treating successful batch completion as fresh data</th>
            <td>The technical job is green while the business receives stale information.</td>
          </tr>
          <tr>
            <th scope="row">Monitoring component health instead of consumer outcome</th>
            <td>All infrastructure dashboards can be green while the end-to-end service is unusable.</td>
          </tr>
          <tr>
            <th scope="row">Creating an SLA before establishing observability</th>
            <td>The organization commits to a target it cannot prove or diagnose.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <ul>
      <li><strong>Start from business impact:</strong> Do not invent availability or latency targets. Derive them from business deadlines, consumer behavior, and failure cost.</li>
      <li><strong>Define measurement boundaries:</strong> Every KPI must state where measurement starts, where it stops, and which population is eligible.</li>
      <li><strong>Separate the four dimensions:</strong> Availability, latency, throughput, and freshness answer different questions. Do not substitute one for another.</li>
      <li><strong>Use percentiles for latency:</strong> Prefer p95 or p99 when slow-tail behavior matters; never rely on the average alone.</li>
      <li><strong>Validate capacity:</strong> Throughput targets require realistic load evidence, not product limits copied from documentation.</li>
      <li><strong>Connect to operations:</strong> Every committed objective needs telemetry, an owner, an alert or review rule, and a breach action.</li>
      <li><strong>Link the next design skill:</strong> Use API Integration, Event-Driven Architecture, Integration Observability, and Integration Error Handling to implement the resulting objectives.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/integration-architecture/api-integration-working-skill/">API Integration</a> — Apply availability, latency, and capacity objectives to synchronous interfaces.</li>
      <li><a href="/skill-hub/integration-architecture/event-driven-architecture-working-skill/">Event-Driven Architecture</a> — Apply latency, throughput, ordering, durability, and consumer-lag objectives to events.</li>
      <li><a href="/skill-hub/integration-architecture/integration-observability-working-skill/">Integration Observability</a> — Turn the objectives into measurable dashboards, thresholds, and alerts.</li>
      <li><a href="/skill-hub/integration-architecture/integration-error-handling-working-skill/">Integration Error Handling</a> — Design retry and escalation within the service-level budget.</li>
      <li><a href="/skill-hub/integration-architecture/interface-ownership-working-skill/">Interface Ownership</a> — Assign business, technical, operational, and consumer ownership for the commitment.</li>
      <li><a href="/skill-hub/integration-architecture/data-mesh-working-skill/">Data Mesh</a> — Define freshness and service levels for data-product output ports.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/sap-integration-architecture/">SAP Integration Architecture</a> — Broader architectural context for SAP-centric integrations.</li>
      <li><a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">SAP Interface Monitoring Diagnostics</a> — Operational signals used to prove service levels.</li>
      <li><a href="/atlas/concepts/retry-and-error-handling/">Retry and Error Handling</a> — How retry behavior affects latency and recovery.</li>
      <li><a href="/atlas/concepts/idempotency/">Idempotency</a> — Safe processing when retries are required.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of service-level design for enterprise integrations. It is not a contractual template and it is not official SAP, SRE, ITIL, or vendor guidance. Example percentages and time budgets are explanatory only. Real targets must be validated against the business process, the exact system landscape, measured production behavior, support model, and any contractual or regulatory obligations.</p>
  </section>
</article>
