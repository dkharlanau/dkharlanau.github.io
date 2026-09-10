---
layout: default
title: "BP and MDG Replication Practice: Diagnose Before You Retry"
description: "A synthetic SAP interview and assessment exercise: distinguish source selection, message delivery and target-state evidence before proposing recovery."
permalink: /learn/packs/bp-mdg-replication/
locale: en
pack_id: bp-mdg-replication
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-10
hide_global_cta: true
---

<link rel="stylesheet" href="{{ '/assets/site-focus.css' | relative_url }}" />
<article class="focus-page focus-reading">
  <header class="focus-intro">
    <p class="eyebrow"><a href="{{ '/learn/' | relative_url }}">SAP learning</a> / Free pack preview</p>
    <h1>Diagnose before you retry.</h1>
    <p class="focus-lead">BP / MDG replication: explain the gap between a successful message and the intended business result.</p>
    <p class="focus-meta">Draft v0.1.0 · One synthetic case · Suggested practice time: 15 minutes · No SAP system required</p>
    <p class="focus-notice">All counts and circumstances below are invented for training. This is not a customer case, a production runbook or an official SAP assessment. The preview has not yet passed human technical review.</p>
  </header>

  <section aria-labelledby="pack-outcome-title">
    <h2 id="pack-outcome-title">What you will practise</h2>
    <p>Separate facts from hypotheses, locate missing evidence across systems and propose a controlled recovery decision. You should already understand the basic purpose of Business Partner master data and source-to-target replication.</p>
    <p>Use the existing <a href="{{ '/labs/enterprise-context/mdg/' | relative_url }}">MDG workspace</a> and <a href="{{ '/labs/enterprise-context/integrations/drf/' | relative_url }}">DRF reference</a> for subject study. This pack adds a practice task, not another copy of those explanations.</p>
  </section>

  <section class="focus-section" aria-labelledby="pack-case-title">
    <h2 id="pack-case-title">The case: green transport, incomplete business result</h2>
    <p>A fictional team changes a communication attribute on 12 Business Partners in its source system. The changes are activated. The agreed target outcome is the new value on all 12 corresponding target records. A reviewer supplies the following evidence after the agreed observation window.</p>
    <div class="focus-table" role="region" aria-label="Synthetic replication evidence" tabindex="0">
      <table>
        <caption>Training evidence only; counts are distinct Business Partners, not message counts.</caption>
        <thead><tr><th scope="col">Stage</th><th scope="col">Evidence supplied</th><th scope="col">Known gap</th></tr></thead>
        <tbody>
          <tr><th scope="row">Source</th><td>12 intended records show the activated value.</td><td>No source discrepancy demonstrated.</td></tr>
          <tr><th scope="row">Outbound</th><td>Payload membership identifies 10 of those records.</td><td>No outbound evidence for the other 2.</td></tr>
          <tr><th scope="row">Transport</th><td>The transport reports successful delivery for those 10.</td><td>No target application proof in this status alone.</td></tr>
          <tr><th scope="row">Target</th><td>8 of the 10 delivered records show the intended value.</td><td>The other 2 delivered records still show the old value.</td></tr>
        </tbody>
      </table>
    </div>
    <p>No replication configuration, complete target application log, later-change history or retry-safety assessment has been supplied. Do not invent those missing facts.</p>
  </section>

  <section class="focus-section" aria-labelledby="pack-attempt-title">
    <h2 id="pack-attempt-title">Your task: an eight-minute decision brief</h2>
    <ol>
      <li>State the confirmed result and separate the two unresolved groups.</li>
      <li>Give two plausible hypotheses for each group and specify the evidence that would distinguish them.</li>
      <li>Propose the next safe checks. Explain why you would or would not approve a retry now.</li>
      <li>Write a three-sentence status update naming the unresolved outcome, owner and next checkpoint.</li>
      <li>Suggest one prevention control and one measure that checks whether it helped.</li>
    </ol>
    <p>Use this response shape: <strong>Facts → Unknowns → Hypotheses → Safe checks → Decision → Owner → Verification.</strong> Write your answer in your own notes before opening the review. Do not use real client records.</p>
    <p class="focus-meta">The browser's print command can produce an exercise sheet. The review section is hidden in print; no download service or account is required.</p>
  </section>

  <details class="focus-answer">
    <summary>Open the worked review after your attempt</summary>
    <h2>A defensible answer</h2>
    <p><strong>Confirmed:</strong> 8 of 12 target outcomes are demonstrated. Four remain unresolved in two disjoint groups: two without outbound evidence and two delivered but not showing the intended value. This does not establish one shared root cause, and it does not prove that all four need replay.</p>
    <h3>Group A: no outbound evidence for two records</h3>
    <p>Possible explanations include selection or filter conditions, and a trigger or processing gap. Check the actual replication model, target assignment, relevant selection and filter settings, change chronology and outbound evidence. Absence from the supplied extract is not proof that a record was never sent.</p>
    <h3>Group B: delivered but still unchanged</h3>
    <p>Possible explanations include target application rejection or a value that was not carried or mapped as expected. A later target-side change is another hypothesis. Correlate the object identity and intended field through the actual payload, target application evidence and change history. A transport-level success must not be silently re-labelled business completion.</p>
    <h3>Recovery decision</h3>
    <p>Do not approve an unrestricted mass replay on this evidence. First establish current state, ownership, payload semantics and duplicate or overwrite risks for the affected route. Any repair requires an authorized scope, a limited test, reconciliation criteria and a stop condition. Do not disable validation or update tables directly to make the numbers look complete.</p>
    <h3>Status update example</h3>
    <p>“Eight of twelve intended target updates are confirmed. The integration owner is checking outbound evidence for two records; the target application owner is checking application and change-history evidence for two delivered records. No mass retry is approved; the next checkpoint is a reviewed exception list and a bounded recovery decision.”</p>
    <h3>Prevention</h3>
    <p>Propose reconciliation of intended objects and fields against the target outcome, with explicit exception ownership. Measure unresolved target discrepancies after the agreed observation window relative to the number of intended updates. Do not substitute the number of successful messages for that denominator.</p>
    <h3>Follow-up challenge</h3>
    <p><strong>The target timestamp is later than the source timestamp. Are we done?</strong> No. Time ordering alone does not establish the intended field values, object mapping or business outcome. Confirm time-zone and clock assumptions before using timestamps even as supporting evidence.</p>
  </details>

  <section class="focus-section" aria-labelledby="pack-rubric-title">
    <h2 id="pack-rubric-title">Review your reasoning, not your confidence</h2>
    <p>For each dimension, use 0 = absent or unsafe; 1 = partly addressed; 2 = explicit and tied to the supplied evidence. The maximum is 8. There is no validated pass threshold.</p>
    <div class="focus-table" role="region" aria-label="Practice review rubric" tabindex="0">
      <table>
        <caption>Manual self-review rubric; not an employment or certification score.</caption>
        <thead><tr><th scope="col">Dimension</th><th scope="col">What earns a clear explanation</th></tr></thead>
        <tbody>
          <tr><th scope="row">Evidence</th><td>Separates the two groups and does not turn hypotheses into facts.</td></tr>
          <tr><th scope="row">Diagnosis</th><td>Names discriminating checks, not only a list of transaction codes.</td></tr>
          <tr><th scope="row">Safety</th><td>Defines authority, scope, reconciliation and a stop condition before replay.</td></tr>
          <tr><th scope="row">Communication</th><td>States the business gap, accountable owner and next decision clearly.</td></tr>
        </tbody>
      </table>
    </div>
    <p>Revise the weakest dimension, then explain your decision in two minutes without reading the worked review. Continue in <a href="{{ '/labs/interview-readiness/' | relative_url }}">Interview Readiness</a> or <a href="{{ '/labs/assessment/' | relative_url }}">Assessment Practice</a>; this preview does not write to either progress model.</p>
  </section>

  <section class="focus-section" aria-labelledby="pack-sources-title">
    <h2 id="pack-sources-title">Technical context and limits</h2>
    <p>SAP documents both SOA and ALE replication paths. The current ALE guide recommends SOA-based replication to SAP S/4HANA because ALE does not cover all Business Partner attributes. Select documentation for the actual product release and route; this exercise does not prescribe one configuration for every landscape.</p>
    <p><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/287a3851fd167062e10000000a44538d.html">SAP Help: Business Partner replication using ALE</a> · <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/74b0b157c81944ffaac6ebc07245b9dc/5efcb922c8e9408095bf900611f6cfdd.html">SAP Help: replication using SOA</a></p>
    <p class="focus-meta">Public references checked 10 September 2026. The scenario and rubric are original training material; source checks do not constitute human approval of this pack.</p>
  </section>
</article>
