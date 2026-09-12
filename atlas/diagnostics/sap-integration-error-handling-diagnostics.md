---
layout: default
title: "SAP Integration Error Handling Diagnostics"
description: "An evidence-first SAP integration guide for locating the failed checkpoint, deciding whether retry is safe, and verifying the business outcome."
permalink: /atlas/diagnostics/sap-integration-error-handling-diagnostics/
last_modified_at: 2026-09-12
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration and interfaces
concept_type: diagnostic guide
sap_area: "Integration / error management"
business_process: Integration
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau
article_visual: integration-retry-gates
og_image: /assets/img/articles/integration-retry-gates.webp
og_image_width: 1536
og_image_height: 1024
og_image_alt: "A failed integration message passes through outcome, cause, duplicate, ordering, and ownership evidence gates before a retry decision."

tags:
  - integration
  - sap-ale
  - diagnostics
  - error-handling
related:
  - /atlas/diagnostics/idoc-aif-integration-diagnostics/
  - /atlas/diagnostics/sap-idoc-status-diagnostics/
  - /atlas/diagnostics/sap-interface-monitoring-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Integration Error Handling Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP integration error handling diagnostics</h1>
    <p class="note-subtitle">Find the uncertain checkpoint, test the recovery gates, and verify one intended business outcome.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Integration</dd></div>
      <div><dt>SAP area</dt><dd>Integration / error management</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until integration error handling behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>An error status proves that one checkpoint did not complete as expected. It does not always prove whether the receiver changed business data. A timeout can occur before delivery, during processing, or after the receiver committed a result but before the acknowledgement returned. Therefore, the support decision is not simply “transient or permanent?” It is: what happened, what remains uncertain, and which action preserves the business outcome?</p>
    <p>Classify the observation, locate the first failed or unproven checkpoint, determine the current receiver-side outcome, and test the recovery gates. Retry only when the cause is removed or bounded, duplicate effects are controlled, ordering is preserved, and an owner can verify the result.</p>

    {% include article-visual.html %}

    <h2>Five gates before retry</h2>
    <table>
      <thead>
        <tr><th>Gate</th><th>Evidence question</th><th>Unsafe assumption</th></tr>
      </thead>
      <tbody>
        <tr><td>Outcome</td><td>Did the receiver create, update, reject, or partially apply the business object?</td><td>“Failed” means nothing happened downstream.</td></tr>
        <tr><td>Cause</td><td>Is the failing condition removed, or is the next attempt deliberately testing a bounded transient condition?</td><td>A later retry will behave differently without any changed evidence.</td></tr>
        <tr><td>Duplicate control</td><td>Can the receiver or integration design recognize the same business operation or message?</td><td>The same payload is automatically safe to execute twice.</td></tr>
        <tr><td>Ordering</td><td>Are earlier, later, or dependent messages waiting, and must their sequence be preserved?</td><td>One message can be replayed independently.</td></tr>
        <tr><td>Ownership and verification</td><td>Who is allowed to recover it, and which technical and business checks close the action?</td><td>A successful retry status completes the incident.</td></tr>
      </tbody>
    </table>

    <h2>Error observations are hypotheses</h2>
    <table>
      <thead>
        <tr><th>Observation</th><th>Possible interpretation</th><th>Evidence needed next</th></tr>
      </thead>
      <tbody>
        <tr><td>Connection error or timeout</td><td>The target was unavailable, the response was lost, or processing exceeded a limit.</td><td>Destination and runtime evidence plus a receiver-side search by business or idempotency key.</td></tr>
        <tr><td>Application validation error</td><td>Payload, master data, process state, or a business rule rejected the operation.</td><td>Full error detail, affected field or object, successful comparison, and the responsible data owner.</td></tr>
        <tr><td>Mapping or configuration error</td><td>The deployed route, partner, destination, credential, schema, or transformation does not match the contract.</td><td>Active configuration, deployment history, runtime trace, and a known-good message through the same path.</td></tr>
        <tr><td>Blocked queue or aged intermediate state</td><td>One failing unit, deliberate stop, dependency, scheduler condition, or capacity constraint is delaying progress.</td><td>First blocker, queue history, sequence, scheduler state, oldest age, depth, and throughput trend.</td></tr>
        <tr><td>Repeated volume-related failure</td><td>Capacity, throttling, payload size, batch design, or downstream service limits may be involved.</td><td>Time-series volume, latency, failure rate, payload profile, resource evidence, and documented limits.</td></tr>
      </tbody>
    </table>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>SM58</strong> — tRFC units and recorded error context; inspect the destination and receiver outcome before manual execution.</li>
      <li><strong>SMQ1 / SMQ2</strong> — qRFC outbound and inbound queues, including the first blocking unit and the sequence behind it.</li>
      <li><strong>WE02 / WE05</strong> — IDoc control data, direction, status history, timestamps, and application messages.</li>
      <li><strong>Middleware runtime monitor</strong> — the actual PI/PO, SAP Integration Suite, or other configured runtime record and correlation identifiers.</li>
      <li><strong>Receiver application</strong> — business object, application status, duplicate key, and expected-versus-actual result.</li>
      <li><strong>SM37</strong> — relevant scheduled job status and job log where background processing is part of the path.</li>
      <li><strong>SLG1</strong> — a relevant application log only where the process writes one; select the correct object, subobject, time window, and business reference.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EDIDC / EDIDS</strong> — IDoc control and status.</li>
      <li><strong>ARFCSDATA / ARFCSSTATE</strong> — tRFC data and status.</li>
      <li><strong>TRFCQOUT / TRFCQIN</strong> — qRFC queue tables.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Record the source and receiver system and client, interface path, direction, message or correlation ID, business key, timestamps with time zone, complete error text, and first observed impact.</li>
      <li>Map the actual checkpoints from source trigger through transport and middleware to receiver processing and the expected business object.</li>
      <li>Find the first failed or unproven checkpoint. Keep a technical error, a missing acknowledgement, and a missing business result as separate observations.</li>
      <li>Search the receiver using the documented business key, external reference, or idempotency key. Determine whether the operation was not applied, fully applied, rejected, or left in an uncertain or partial state.</li>
      <li>Compare affected and successful messages from the same path. Test scope by partner, payload, destination, deployment, time window, queue, and volume.</li>
      <li>Identify the cause and the evidence that it has changed. Availability now is useful evidence, but it does not resolve duplicate or ordering risk.</li>
      <li>Evaluate the five retry gates. If any gate is unproven, choose investigation, reconciliation, correction, or escalation before replay.</li>
      <li>Execute the authorized recovery on a bounded scope, retain the original identifiers, and verify both the technical checkpoint and the intended business outcome.</li>
    </ol>

    <h2>Choose the intervention from the evidence</h2>
    <table>
      <thead>
        <tr><th>Evidence state</th><th>Next action</th><th>Closure evidence</th></tr>
      </thead>
      <tbody>
        <tr><td>Receiver outcome is uncertain</td><td>Reconcile by business key and timestamp before any resend.</td><td>Existing object found, confirmed absent, or explicitly classified as partial.</td></tr>
        <tr><td>Data or business rule rejected the operation</td><td>Correct the owned data or process state, then reprocess the bounded message if the gates pass.</td><td>Correction reference, successful processing, and expected object state.</td></tr>
        <tr><td>Route or configuration is wrong</td><td>Use the governed configuration-change path; test with controlled evidence.</td><td>Approved change, deployed version, trace through each checkpoint, and business result.</td></tr>
        <tr><td>Temporary connectivity failed before a proven receiver commit</td><td>Use the designed retry mechanism when duplicate control, ordering, and ownership are established.</td><td>Original message correlated to one intended receiver outcome.</td></tr>
        <tr><td>Queue sequence is blocked</td><td>Resolve the first blocker and preserve the required order; avoid selecting a convenient later unit in isolation.</td><td>Queue progression, no unintended duplicate, and dependent outcomes verified.</td></tr>
      </tbody>
    </table>

    <h2>Interview exercise: failed after the call</h2>
    <p><strong>Synthetic case.</strong> An integration flow sends a create-order request. The runtime reports a timeout after 30 seconds and offers a retry. The receiver has not yet been searched by the external order reference. A dependent update message is waiting behind the create request.</p>
    <ol>
      <li>State what the timeout proves and what it leaves uncertain.</li>
      <li>Name the evidence required before retrying the create request.</li>
      <li>Explain how duplicate handling and ordering change the decision.</li>
      <li>Define the technical and business evidence that would close the incident.</li>
    </ol>
    <details class="study-review">
      <summary>Review the retry decision</summary>
      <p>The timeout proves that the caller did not receive the expected response within the limit. It does not prove that the receiver failed to create the order. First search the receiver with the stable external reference or documented idempotency key and correlate timestamps and message identifiers. If an order exists, reconcile its state and do not create it again. If it is absent, establish whether the receiver or integration design can suppress a duplicate and whether the original request could still complete.</p>
      <p>The waiting update makes sequence part of the recovery decision: it may depend on the created order and must not overtake it. Close the incident only when one intended order exists in the required state, the dependent update is correctly applied or deliberately held, and the original and recovered technical records are linked in the support evidence.</p>
    </details>

    <h2>Support takeaway</h2>
    <p>A useful handover states the failed or uncertain checkpoint, the receiver-side outcome, the suspected cause and supporting evidence, duplicate and ordering controls, affected scope, business impact, recovery owner, and verification plan. “Network error — please retry” is an observation and an action request, not yet a safe diagnosis.</p>

    <h2>Source checks</h2>
    <ul>
      <li><a href="https://help.sap.com/docs/cloud-integration/sap-cloud-integration/quality-of-service">SAP Cloud Integration: Quality of Service</a> — end-to-end delivery depends on the protocols and capabilities of sender and receiver; duplicate effects require receiver-side idempotency.</li>
      <li><a href="https://help.sap.com/docs/cloud-integration/sap-cloud-integration/define-idempotent-process-call">SAP Cloud Integration: Define Idempotent Process Call</a> — duplicate detection has explicit scope and limitations, especially when acknowledgement is uncertain.</li>
      <li><a href="https://help.sap.com/docs/cloud-integration/sap-cloud-integration/apply-retry-pattern">SAP Cloud Integration: Apply the Retry Pattern</a> — retry mechanisms are designed for anticipated temporary failures and depend on the integration pattern.</li>
      <li><a href="https://help.sap.com/docs/SAP_NETWEAVER_AS_ABAP_752/984899fe989d4efab0409b818433f892/5212f73b7803b009e10000000a114084.html">SAP NetWeaver: Set Up Monitoring of qRFC Calls</a> — qRFC monitoring reflects application-specific queues and chronological processing.</li>
      <li><a href="https://help.sap.com/docs/SUPPORT_CONTENT/abapconn/3354079694.html">SAP: SM58 connection-error guidance</a> — inspect the affected RFC destination before manually reprocessing a failed tRFC unit.</li>
    </ul>
    <p>Sources checked on 12 September 2026. Exact monitors, transaction availability, quality-of-service behavior, and recovery functions depend on the configured products, protocols, release, and interface design. This page remains noindex until human verification.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic and interview-practice frame, not a configuration recipe. It does not claim that every interface uses the same retry mechanism, duplicate store, queue, monitor, or transaction. Confirm the actual message contract, quality of service, receiver behavior, authorizations, and release-specific documentation before changing configuration or replaying production data.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">Idoc Aif Integration Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP Idoc Status Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">SAP Interface Monitoring Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
