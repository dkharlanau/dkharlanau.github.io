---
layout: default
title: "BP and MDG Replication Practice: Evidence to Recovery"
description: "Five synthetic SAP practice cases for diagnosing BP and MDG replication gaps, choosing safe checks, defining recovery boundaries and explaining decisions."
permalink: /learn/packs/bp-mdg-replication/
locale: en
pack_id: bp-mdg-replication
content_model: learning_pack
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-10
tags: [SAP, SAP-MDG, Business-Partner, Replication, Diagnostics]
hide_global_cta: true
---

<link rel="stylesheet" href="{{ '/assets/site-focus.css' | relative_url }}" />
<article class="focus-page focus-reading-wide">
  <header class="focus-intro">
    <p class="eyebrow"><a href="{{ '/learn/' | relative_url }}">SAP learning</a> / Free pilot pack</p>
    <h1>Diagnose before you recover.</h1>
    <p class="focus-lead">BP / MDG replication practice: follow the evidence from intended change to business outcome, then decide what is safe to do next.</p>
    <p class="focus-meta">Draft v0.2.0 · Five synthetic cases · Suggested practice time: 70 minutes · No SAP system required</p>
    <p class="focus-notice">All objects, counts, timestamps and circumstances below are invented for training. This is not a customer case, production runbook, certification dump or official SAP assessment. The pack has not yet passed human technical review.</p>
  </header>

  <section aria-labelledby="pack-outcome-title">
    <p class="eyebrow">Outcome</p>
    <h2 id="pack-outcome-title">Trace the result, not the green status.</h2>
    <p>The goal is to diagnose a source-to-target discrepancy without collapsing selection, transport, application and business outcome into one status. You will practise evidence checks, recovery boundaries and concise owner-based communication.</p>
    <p>Use the existing <a href="{{ '/labs/enterprise-context/mdg/' | relative_url }}">MDG workspace</a> and <a href="{{ '/labs/enterprise-context/integrations/drf/' | relative_url }}">DRF reference</a> for subject context. This pack is a practice layer; it does not duplicate those explanations.</p>
    <div class="focus-method-strip" aria-label="Replication evidence chain">
      <div class="focus-method-step"><strong>Intent</strong><span>Which object and field should change?</span></div>
      <div class="focus-method-step"><strong>Source</strong><span>Is the intended source state confirmed?</span></div>
      <div class="focus-method-step"><strong>Outbound</strong><span>Was the object and value actually selected?</span></div>
      <div class="focus-method-step"><strong>Target</strong><span>Was the change applied to the right object?</span></div>
      <div class="focus-method-step"><strong>Outcome</strong><span>Does the current business state match the intent?</span></div>
    </div>
  </section>

  <section class="focus-section" aria-labelledby="pack-workflow-title">
    <h2 id="pack-workflow-title">Practice workflow</h2>
    <ol class="focus-steps">
      <li><strong>Attempt first.</strong> Time-box each case and write the decision before opening the review.</li>
      <li><strong>Partition.</strong> Keep different evidence patterns in different exception groups until evidence supports one cause.</li>
      <li><strong>Choose checks.</strong> Ask for evidence that can distinguish competing hypotheses instead of collecting logs without a question.</li>
      <li><strong>Define actions.</strong> State authority, recovery scope, reconciliation and stop conditions before replay or overwrite.</li>
    </ol>
    <p>Suggested response shape for every case: <strong>Facts → Unknowns → Hypotheses → Discriminating checks → Decision → Owner → Verification.</strong></p>
  </section>

  <nav class="focus-case-nav" aria-label="Pack cases">
    <a href="#case-1"><strong>01 Selection gap</strong><span>Intended objects do not all appear outbound.</span></a>
    <a href="#case-2"><strong>02 Application gap</strong><span>Transport is green; target state is not.</span></a>
    <a href="#case-3"><strong>03 Blank semantics</strong><span>A clear in the source does not clear the target.</span></a>
    <a href="#case-4"><strong>04 Concurrent change</strong><span>A later timestamp does not decide authority.</span></a>
    <a href="#case-5"><strong>05 Recovery design</strong><span>Several exception classes need different treatment.</span></a>
  </nav>

  <section class="focus-section focus-case" id="case-1" aria-labelledby="case-1-title">
    <span class="focus-case-label">Case 01</span>
    <h2 id="case-1-title">Green transport, incomplete business result</h2>
    <p>A fictional team changes a communication attribute on 12 Business Partners in its governed source. The changes are activated. The agreed target outcome is the new value on all 12 corresponding target records after the observation window.</p>
    <div class="focus-table" role="region" aria-label="Case 1 synthetic replication evidence" tabindex="0">
      <table>
        <caption>Training evidence only; counts are distinct Business Partners, not message counts.</caption>
        <thead><tr><th scope="col">Stage</th><th scope="col">Evidence supplied</th><th scope="col">Known gap</th></tr></thead>
        <tbody>
          <tr><th scope="row">Source</th><td>12 intended records show the activated value.</td><td>No source discrepancy demonstrated.</td></tr>
          <tr><th scope="row">Outbound</th><td>Payload membership identifies 10 of those records.</td><td>No outbound evidence for the other 2.</td></tr>
          <tr><th scope="row">Transport</th><td>Successful delivery is reported for those 10.</td><td>This alone is not target application proof.</td></tr>
          <tr><th scope="row">Target</th><td>8 of the 10 delivered records show the intended value.</td><td>The other 2 delivered records still show the old value.</td></tr>
        </tbody>
      </table>
    </div>
    <p>No complete replication configuration, target application evidence, later-change history or retry-safety assessment has been supplied. Do not invent those missing facts.</p>
    <div class="focus-task">
      <h3>Your task — eight-minute decision brief</h3>
      <ol>
        <li>State the confirmed result and separate the unresolved groups.</li>
        <li>Give two plausible hypotheses for each group and one check that would distinguish them.</li>
        <li>Explain whether you approve a retry now and what evidence would change that decision.</li>
        <li>Write a three-sentence status update with owner and next checkpoint.</li>
      </ol>
    </div>
    <details class="focus-answer">
      <summary>Open the worked review after your attempt</summary>
      <h3>A defensible answer</h3>
      <p><strong>Confirmed:</strong> 8 of 12 target outcomes are demonstrated. Four remain unresolved in two disjoint groups: two without supplied outbound evidence and two delivered but not showing the intended value. This does not establish one shared root cause, and it does not prove that all four need replay.</p>
      <p><strong>Group A:</strong> plausible explanations include selection/filter conditions or a trigger/processing gap. Check the actual replication model, target assignment, relevant selection/filter settings, change chronology and outbound evidence. Absence from the supplied extract is not proof that a record was never sent.</p>
      <p><strong>Group B:</strong> plausible explanations include target application rejection, value mapping/payload semantics or a later target-side change. Correlate object identity and intended field through payload, target application evidence and change history.</p>
      <p><strong>Decision:</strong> do not approve an unrestricted replay. Establish current state, route ownership, duplicate/overwrite risk and bounded recovery criteria first. A limited repair needs an authorized scope, a test, reconciliation and a stop condition.</p>
    </details>
  </section>

  <section class="focus-section focus-case" id="case-2" aria-labelledby="case-2-title">
    <span class="focus-case-label">Case 02</span>
    <h2 id="case-2-title">Delivered does not mean applied</h2>
    <p>Six fictional Business Partners are expected to receive a changed classification attribute. The outbound evidence contains all six intended object identities and the intended value. The transport layer reports successful delivery for all six. Four target records show the intended value; two still show the previous value.</p>
    <p>The only additional evidence is a message-level success status. No target application log, target validation result, mapping trace or later change history has been provided.</p>
    <div class="focus-task">
      <h3>Your task — diagnose the boundary</h3>
      <ol>
        <li>Name what the transport evidence proves and what it does not prove.</li>
        <li>Give at least three hypotheses for the two unchanged target records.</li>
        <li>Choose the first two checks you would request and explain why they are discriminating.</li>
        <li>Define the completion condition for this incident class.</li>
      </ol>
    </div>
    <details class="focus-answer">
      <summary>Open the worked review after your attempt</summary>
      <h3>Keep transport and application separate</h3>
      <p>A transport success supports the claim that the message reached the next technical boundary represented by that status. It does not, by itself, establish that the receiving application accepted the intended field on the intended object or that the current business state still matches it.</p>
      <p>Useful hypotheses include target validation/application failure, a mapping or value-semantic difference, incorrect object identity/key mapping, or a later target-side change. The first checks should correlate the two object identities and intended field through the actual inbound/application evidence and the target change history. Which technical transaction or log is relevant depends on the route and product release.</p>
      <p>A stronger completion condition is the intended current value on the correctly mapped target object, within the agreed observation window, with unresolved exceptions explicitly owned. “Message delivered” can remain a transport measure; it should not silently become the business completion measure.</p>
    </details>
  </section>

  <section class="focus-section focus-case" id="case-3" aria-labelledby="case-3-title">
    <span class="focus-case-label">Case 03</span>
    <h2 id="case-3-title">The source is blank. The target is not.</h2>
    <p>A fictional cleanup explicitly removes an old communication value from five source Business Partners. After replication, all five target records still show the old value. Outbound evidence shows the objects were processed, but the supplied payload extract does not make it clear whether the field was sent as an explicit clear instruction, sent as an empty value, or omitted.</p>
    <p>A teammate proposes a mass overwrite because “blank in the source obviously means delete in the target.” No interface contract or release-specific behavior has been checked.</p>
    <div class="focus-task">
      <h3>Your task — separate business intent from interface semantics</h3>
      <ol>
        <li>State the business intent and the missing technical contract.</li>
        <li>List the evidence needed before deciding whether this is source data, mapping, payload or target behavior.</li>
        <li>Explain why a direct mass overwrite is or is not justified by the evidence supplied.</li>
        <li>Propose a reusable test that should exist before the next cleanup.</li>
      </ol>
    </div>
    <details class="focus-answer">
      <summary>Open the worked review after your attempt</summary>
      <h3>Blank, omitted and clear are not interchangeable assumptions</h3>
      <p>The business intent is clear: the old target value should no longer exist. The technical semantics are not. Before deciding on recovery, establish how the actual replication contract represents clearing that field, whether the intended field was present in the outbound/inbound representation, and what the target application does with that representation in the relevant release and configuration.</p>
      <p>The evidence chain should distinguish source state, outbound field presence/value, transformation or mapping behavior, target application evidence and current target state. A direct overwrite may produce the desired snapshot while bypassing the cause, validation and ownership model; it is not justified merely because the source appears blank.</p>
      <p>A reusable prevention control is a small clear/update/no-change test matrix for fields where omission and clearing could differ, followed by target reconciliation. The expected semantics should be explicit rather than reconstructed during an incident.</p>
    </details>
  </section>

  <section class="focus-section focus-case" id="case-4" aria-labelledby="case-4-title">
    <span class="focus-case-label">Case 04</span>
    <h2 id="case-4-title">The later timestamp does not decide which value should win</h2>
    <p>A fictional governed source activates value A at 10:02. Outbound evidence for the object is timestamped 10:03. The target change history contains a local change to value B at 10:04 and integration-related activity at 10:05. The current target value is B.</p>
    <p>The team knows that timestamps come from different system contexts, and it has not yet confirmed clock alignment, time-zone handling, field-level ownership or whether local target maintenance is permitted for this attribute.</p>
    <div class="focus-task">
      <h3>Your task — reason about concurrency</h3>
      <ol>
        <li>Explain why “target timestamp is later” is not enough to declare success or failure.</li>
        <li>Identify the ownership and chronology evidence you need.</li>
        <li>State two different valid outcomes depending on the governance rule.</li>
        <li>Define a safe next action that does not destroy evidence.</li>
      </ol>
    </div>
    <details class="focus-answer">
      <summary>Open the worked review after your attempt</summary>
      <h3>Chronology supports a decision; it does not create the governance rule</h3>
      <p>First confirm comparable clocks/time zones and correlate the events to the same object and field. Then establish the authority rule: is the governed source authoritative for this attribute, is a local target change allowed, and what should happen when both occur close together?</p>
      <p>If the governed source is authoritative and the later target edit is unauthorized or temporary, the unresolved outcome may be a governance or overwrite problem. If target-local ownership is explicitly allowed for this field, value B may be the intended final state even though it differs from the source snapshot. The right answer depends on the ownership contract, not on timestamp ordering alone.</p>
      <p>Preserve the change history and current-state evidence, stop any broad corrective overwrite, and resolve the field-level authority plus event order before choosing recovery.</p>
    </details>
  </section>

  <section class="focus-section focus-case" id="case-5" aria-labelledby="case-5-title">
    <span class="focus-case-label">Case 05</span>
    <h2 id="case-5-title">One exception list is not one recovery action</h2>
    <p>A fictional migration-support team has 37 unresolved Business Partners after a controlled update. Eleven have no supplied outbound membership evidence. Eighteen were delivered but do not yet have target-state proof. Eight currently differ from the intended source value and also show later target-side changes.</p>
    <p>An operator proposes replaying all 37 in one batch to “get back to green.” There is no agreed duplicate/overwrite assessment across all three groups and no single business owner has accepted that one recovery action is appropriate.</p>
    <div class="focus-task">
      <h3>Your task — design the recovery decision</h3>
      <ol>
        <li>Partition the 37 records and define the minimum evidence needed for each group.</li>
        <li>State which group, if any, is closest to a replay decision and what still blocks it.</li>
        <li>Design a bounded pilot, stop condition and reconciliation rule.</li>
        <li>Choose one prevention control and one operating measure for the next run.</li>
        <li>Prepare a Lead-level status update that distinguishes technical status from business completion.</li>
      </ol>
    </div>
    <details class="focus-answer">
      <summary>Open the worked review after your attempt</summary>
      <h3>Recover by evidence class</h3>
      <p>The 11 without outbound evidence first need selection/trigger/filter evidence; replay may be irrelevant if they were intentionally excluded or the source event was never eligible. The 18 delivered records need target application and current-state evidence; transport success is not enough. The 8 with later target-side changes need chronology plus ownership before any overwrite decision.</p>
      <p>No group is ready for an unconditional mass replay from the supplied evidence. A bounded pilot would select a small homogeneous exception class after replay safety is demonstrated, record the exact pre-state, execute only within authorized scope, verify the intended target fields, and stop on an unexpected duplicate, overwrite, validation failure or new exception pattern.</p>
      <p>For prevention, reconcile intended object/field outcomes against current target state and classify exceptions by evidence boundary. Measure unresolved business discrepancies after the observation window relative to intended updates; keep transport success as a separate operational signal.</p>
      <p>A concise status can say: “The 37 exceptions are split into three evidence classes and are not treated as one replay population. Owners are establishing selection evidence, target application evidence and later-change authority before recovery. Business completion will be reported from reconciled target state, with any residual exceptions explicitly owned.”</p>
    </details>
  </section>

  <section class="focus-section" aria-labelledby="pack-rubric-title">
    <h2 id="pack-rubric-title">Review the reasoning, not the confidence</h2>
    <p>For each dimension, use 0 = absent or unsafe; 1 = partly addressed; 2 = explicit and tied to the supplied evidence. The maximum is 10. There is no validated pass threshold.</p>
    <div class="focus-table" role="region" aria-label="Practice review rubric" tabindex="0">
      <table>
        <caption>Manual self-review rubric; not an employment or certification score.</caption>
        <thead><tr><th scope="col">Dimension</th><th scope="col">What a strong response demonstrates</th></tr></thead>
        <tbody>
          <tr><th scope="row">Evidence</th><td>Separates confirmed state, missing evidence and hypotheses.</td></tr>
          <tr><th scope="row">Diagnosis</th><td>Chooses checks that distinguish causes, not a generic transaction-code list.</td></tr>
          <tr><th scope="row">Safety</th><td>Defines authority, scope, pre-state, reconciliation and stop conditions before recovery.</td></tr>
          <tr><th scope="row">Communication</th><td>States the business gap, accountable owner and next decision without hiding behind technical status.</td></tr>
          <tr><th scope="row">Prevention</th><td>Turns the incident into one reusable control and a measure with a meaningful denominator.</td></tr>
        </tbody>
      </table>
    </div>
    <p>After each case, rewrite the weakest dimension and explain the decision aloud in two minutes without reading the worked review. The second attempt is the useful artifact.</p>
  </section>

  <section class="focus-section" aria-labelledby="pack-worksheet-title">
    <h2 id="pack-worksheet-title">Reusable decision worksheet</h2>
    <div class="focus-diagnostic-sheet" aria-label="Replication decision worksheet">
      <div class="focus-diagnostic-sheet__head"><strong>One object or one homogeneous exception class</strong><span class="focus-meta">Use sanitized or synthetic data during practice.</span></div>
      <dl>
        <div class="focus-diagnostic-row"><dt>Intended outcome</dt><dd>Which object, field and final business state should exist?</dd></div>
        <div class="focus-diagnostic-row"><dt>Confirmed evidence</dt><dd>What is directly observed at source, outbound, target application and current target state?</dd></div>
        <div class="focus-diagnostic-row"><dt>Unknowns</dt><dd>Which missing facts could change the recovery decision?</dd></div>
        <div class="focus-diagnostic-row"><dt>Discriminating checks</dt><dd>Which two or three checks separate the leading hypotheses?</dd></div>
        <div class="focus-diagnostic-row"><dt>Recovery boundary</dt><dd>Authority, population, pre-state, duplicate/overwrite risk, test, stop condition and rollback/recovery path.</dd></div>
        <div class="focus-diagnostic-row"><dt>Verification</dt><dd>How will the target business outcome be reconciled, and who owns residual exceptions?</dd></div>
      </dl>
    </div>
  </section>

  <section class="focus-section" aria-labelledby="pack-limits-title">
    <h2 id="pack-limits-title">Technical context, sources and limitations</h2>
    <p>SAP documents both SOA and ALE replication paths for Business Partner scenarios. The SAP S/4HANA ALE documentation recommends SOA-based replication to SAP S/4HANA because ALE does not cover all Business Partner attributes. Actual evidence locations, payload behavior, configuration and supported recovery depend on the landscape, route and product release. This pack deliberately does not prescribe one universal transaction sequence.</p>
    <p><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/287a3851fd167062e10000000a44538d.html">SAP Help: Business Partner replication using ALE</a> · <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/74b0b157c81944ffaac6ebc07245b9dc/5efcb922c8e9408095bf900611f6cfdd.html">SAP Help: replication using SOA</a></p>
    <p>Continue with <a href="{{ '/labs/interview-readiness/' | relative_url }}">Interview Readiness</a> or <a href="{{ '/labs/assessment/' | relative_url }}">Assessment Practice</a>. This pilot does not write to either progress model and collects no answer text.</p>
    <p class="focus-meta">Public sources checked 10 September 2026. The scenarios, counts, worksheet and rubric are original synthetic training material; source checks do not constitute human approval of this pack.</p>
  </section>
</article>
