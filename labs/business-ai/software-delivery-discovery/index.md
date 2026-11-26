---
layout: default
title: "Qualifying AI for Software Delivery — From Friction to a Testable Task"
description: "An evidence-led discovery playbook for identifying real software delivery bottlenecks, checking AI coding fit, and defining a verifiable first engineering task with SAP examples."
permalink: /labs/business-ai/software-delivery-discovery/
status: reviewed
verified: false
robots: index,follow
sitemap: true
last_modified_at: 2026-11-26
tags: [business-ai, discovery, software-delivery, codex, sap, presales]
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li aria-current="page">Software delivery discovery</li></ol></nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / Discovery playbook</p>
      <h1>Do not sell the tool.<br>Find the work worth fixing.</h1>
      <p>An engineering leader may be frustrated with slow releases, yet have no viable AI evaluation in mind. This guide turns a general complaint into evidence about work, business consequences, ownership, and a small task the team can actually check.</p>
      <a class="research-canvas__button" href="#discovery-lens">Work through the lens <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <div>
      <p><strong>Working rule:</strong> interest in coding agents is a conversation starter, not proof of a delivery opportunity.</p>
      <p><strong>Scope:</strong> this is a discovery and initial qualification guide. It deliberately stops before security architecture, tool deployment, permission design, or production rollout.</p>
      <p><strong>Product boundary:</strong> Codex is worth assessing when a bounded software engineering task can use accessible project context and produce an inspectable result. A general productivity complaint may point to process redesign, ordinary automation, another AI solution, or no project at all.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="patterns" data-reveal>
    <header><p class="research-canvas__eyebrow">Recognize the signal</p><h2>Five ways software delivery can get stuck</h2><p>Use these as clues, not categories to impose on the customer. Several problems often appear in the same delivery chain.</p></header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">What you notice</th><th scope="col">What to inspect</th><th scope="col">SAP delivery illustration (hypothetical)</th></tr></thead><tbody>
        <tr><th scope="row">Work accumulates</th><td>Where items wait, get rejected, or return for rework.</td><td>Changes to customer master integrations remain open across multiple sprints.</td></tr>
        <tr><th scope="row">Defects surface late</th><td>Which checks should have caught them and when.</td><td>Inbound IDoc mapping defects are first detected during business UAT.</td></tr>
        <tr><th scope="row">Knowledge is concentrated</th><td>Which decisions depend on individual experts or undocumented rules.</td><td>Only one ABAP developer understands a custom field exclusion framework.</td></tr>
        <tr><th scope="row">Handoffs multiply</th><td>Whether teams lack a shared artifact, acceptance criteria, or decision owner.</td><td>Functional, ABAP, and integration teams repeatedly reinterpret one requirement.</td></tr>
        <tr><th scope="row">Old code slows safe change</th><td>Which dependencies, tests, or modernization constraints create the delay.</td><td>Before changing an enhancement, the team manually traces its exits and consumers.</td></tr>
      </tbody></table>
    </div>
    <p><strong>Do not confuse a symptom with a cause.</strong> A slow backlog could be caused by limited coding capacity, but also by unclear specifications, approval queues, test environments, or competing priorities. The diagnostic task is to locate the delay before selecting technology.</p>
  </section>

  <section class="research-canvas__inventory" id="discovery-lens" data-reveal>
    <header><p class="research-canvas__eyebrow">Qualification</p><h2>Five evidence checks before recommending a pilot</h2><p>Each check has a question and a missing-evidence condition. They are a judgment aid, not a numerical scoring model.</p></header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Check</th><th scope="col">Ask naturally</th><th scope="col">Evidence to obtain</th></tr></thead><tbody>
        <tr><th scope="row">Persistence</th><td>When did this last happen, and has it happened before?</td><td>Examples from several changes, releases, or delivery teams; not a single anecdote.</td></tr>
        <tr><th scope="row">Consequences</th><td>What slips or becomes more expensive because of this?</td><td>Delayed releases, extra engineering hours, escaped defects, business disruption, or risk.</td></tr>
        <tr><th scope="row">Accountability</th><td>Who can prioritize an experiment and judge whether it helped?</td><td>A named technical or delivery owner with authority to involve the right people.</td></tr>
        <tr><th scope="row">Ability to evaluate</th><td>Could we reproduce one case with the material and tools your team already has?</td><td>Accessible repository or documentation, a safe evaluation environment, reviewers, and a proposed comparison method.</td></tr>
        <tr><th scope="row">Repeatable unit of work</th><td>Which one activity would you want to complete better next week?</td><td>A bounded code review, test update, defect investigation, documentation repair, or dependency assessment.</td></tr>
      </tbody></table>
    </div>
    <p>Do not demand complete answers at the first meeting. Select the two or three largest unknowns and agree on a way to resolve them. Absence of proof is a reason to continue discovery, not to invent certainty.</p>
  </section>

  <section class="research-canvas__inventory" id="decision-path" data-reveal>
    <header><p class="research-canvas__eyebrow">Decision path</p><h2>Move from a claim to an evaluation brief</h2></header>
    <div class="ecg-decision-columns">
      <div>
        <h3>What weak qualification looks like</h3>
        <p>“We are experimenting with AI coding tools.” This says nothing about where delivery fails, which outcome matters, or whether anyone can test a proposed improvement.</p>
        <p>Likewise, “our releases are late” describes a consequence. It does not yet identify a task suitable for an engineering agent.</p>
      </div>
      <div>
        <h3>What stronger evidence looks like</h3>
        <p>“The team often discovers missing regression tests after transport validation, which adds rework before a release. The engineering lead can provide representative change requests and review the generated tests.”</p>
        <p>This is still a hypothesis, but it points to a candidate task, an owner, and a route to verification.</p>
      </div>
    </div>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Evaluation brief field</th><th scope="col">Example</th></tr></thead><tbody>
        <tr><th scope="row">Engineering job</th><td>Identify missing regression coverage for a defined ABAP mapping change.</td></tr>
        <tr><th scope="row">Inputs</th><td>Approved code snapshot, change specification, existing tests, and defect history.</td></tr>
        <tr><th scope="row">Target</th><td>A reviewable test proposal or patch in an isolated branch; no productive SAP changes.</td></tr>
        <tr><th scope="row">Reviewer</th><td>ABAP owner and functional consultant.</td></tr>
        <tr><th scope="row">Acceptance</th><td>Relevant test cases cover agreed change scenarios and pass required checks; reviewers confirm no unsupported behavior was introduced.</td></tr>
        <tr><th scope="row">Comparison</th><td>Compare time, review effort, defect detection, and rework against the current workflow.</td></tr>
      </tbody></table>
    </div>
    <p><strong>Important SAP distinction:</strong> a model can suggest ABAP changes or explain dependencies, but release-specific system behavior and transport safety must be checked by engineers against the actual landscape. A successful code draft is not proof of a production-safe SAP change.</p>
  </section>

  <section class="research-canvas__inventory" id="fit-boundary" data-reveal>
    <header><p class="research-canvas__eyebrow">Fit boundary</p><h2>When is a coding agent even the right direction?</h2></header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Customer need</th><th scope="col">Initial direction</th><th scope="col">Next discovery move</th></tr></thead><tbody>
        <tr><th scope="row">Recurring repository-based engineering task</th><td>Candidate for Codex evaluation</td><td>Agree on inputs, artifacts, allowed actions, and review checks.</td></tr>
        <tr><th scope="row">Cross-team approvals are slow</th><td>Process and responsibility review first</td><td>Find the actual waiting point; agentic coding may be irrelevant.</td></tr>
        <tr><th scope="row">Employees struggle to find answers</th><td>Knowledge and information access evaluation</td><td>Validate source quality, permissions, freshness, and answer correctness.</td></tr>
        <tr><th scope="row">Business wants an AI feature in its product</th><td>Application and product discovery</td><td>Define user journeys, data, quality measures, and product constraints.</td></tr>
        <tr><th scope="row">No owner, no reproducible task, no checkable result</th><td>Not ready for a tool pilot</td><td>Gather evidence or defer rather than treating interest as qualified demand.</td></tr>
      </tbody></table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="practice" data-reveal>
    <header><p class="research-canvas__eyebrow">Consulting practice</p><h2>A two-minute discovery conversation</h2></header>
    <p><strong>Scenario (fictional):</strong> An SAP platform manager says: “Our release calendar is unreliable, and leadership wants us to try AI developers.” The team suspects that issues found during integration testing are driving repeated corrections.</p>
    <ol>
      <li><strong>Recognize the outcome:</strong> late discoveries may be affecting release confidence.</li>
      <li><strong>Locate the work:</strong> ask which review, test, or defect-investigation step produces avoidable rework.</li>
      <li><strong>Look for a pattern:</strong> request two or three recent examples and the frequency of similar incidents.</li>
      <li><strong>Find authority:</strong> confirm who owns engineering productivity and who can review an evaluation.</li>
      <li><strong>Define one candidate job:</strong> propose investigating a single reproducible validation defect with known inputs.</li>
      <li><strong>Agree on proof:</strong> establish the expected artifact, expert review, and baseline comparison.</li>
    </ol>
    <blockquote><p>“It sounds as though testing is creating uncertainty close to release dates. I would first examine one recurring validation activity. Could your team share a recent example, identify the engineer who owns it, and explain what a satisfactory result would look like?”</p></blockquote>
    <p><strong>Exercise:</strong> Explain why this is a discovery conversation rather than an implementation workshop. Then name one observation that would make you recommend ordinary process improvement instead of a coding agent.</p>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">source</span>
    <div>
      <p><strong>Editorial note:</strong> original synthesis and SAP examples prepared from learning notes on identifying and qualifying engineering AI opportunities. This is not a transcript or an official OpenAI qualification framework.</p>
      <p><strong>Related:</strong> <a href="/labs/business-ai/">Business AI discovery</a> · <a href="/labs/ai-ready/">Practical AI architecture</a>.</p>
    </div>
  </section>
</div>
