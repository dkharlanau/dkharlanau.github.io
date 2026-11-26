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


  <section class="research-canvas__inventory" id="workflow-led-conversation" data-reveal>
    <header><p class="research-canvas__eyebrow">Workshop method / From interest to evidence</p><h2>Trace one real change before discussing an AI tool</h2>
      <p>Broad interviews collect opinions. A useful discovery workshop reconstructs an actual delivery incident: what was supposed to happen, what happened instead, where work stopped, and who had to intervene. Only then should the team discuss whether an engineering assistant is relevant.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>The six-turn conversation</h3>
        <ol>
          <li><strong>Agree on the outcome.</strong> Ask which delivery commitment has become difficult to meet.</li>
          <li><strong>Follow the work.</strong> Ask participants to reconstruct one recent change from request through validation and release.</li>
          <li><strong>Look for recurrence.</strong> Compare that incident with other changes or releases rather than assuming it is typical.</li>
          <li><strong>Connect the consequence.</strong> Establish whether the delay created extra cost, delayed delivery, more defects, or another observable effect.</li>
          <li><strong>Find the accountable person.</strong> Distinguish the people experiencing the delay from the person authorized to improve the workflow.</li>
          <li><strong>Define a candidate experiment.</strong> Identify one task, available inputs, a target output, and the expert who can check it.</li>
        </ol>
      </div>
      <div>
        <h3>How to follow up without leading the witness</h3>
        <p>Instead of: <em>“Would automated testing solve your problem?”</em></p>
        <p>Try: <em>“Think of the most recent release where validation ran late. What was the last completed step before the delay began?”</em></p>
        <p>Then ask who waited, which artifact was incomplete, what the team did next, and how they eventually knew the change was acceptable.</p>
        <p><strong>Facilitation rule:</strong> collect concrete examples before discussing a product, agent workflow, or target architecture. Do not turn uncertainty into an assumed root cause.</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="workflow-map" data-reveal>
    <header><p class="research-canvas__eyebrow">Workflow mapping</p><h2>Find the constraint, not the loudest complaint</h2>
      <p>“Testing is slow” may refer to code coverage, test data, environment stability, approvals, or changing requirements. Record the steps in order and look for the point where progress actually stops.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Step in an illustrative SAP change</th><th scope="col">What to observe</th><th scope="col">Possible evidence</th></tr></thead><tbody>
        <tr><th scope="row">Requirement and specification</th><td>Does the team agree on expected field behavior and edge cases?</td><td>Approved specification and clarification history.</td></tr>
        <tr><th scope="row">ABAP implementation</th><td>Is time spent writing changes or discovering existing enhancement behavior?</td><td>Change history, dependencies, developer notes.</td></tr>
        <tr><th scope="row">Unit and integration checks</th><td>Are test cases missing, or do test environments fail independently of the code?</td><td>Test results, environment incidents, defect examples.</td></tr>
        <tr><th scope="row">Review and release</th><td>Is completion blocked by missing evidence, ownership, or approval queues?</td><td>Review timestamps, transport records, release decisions.</td></tr>
      </tbody></table>
    </div>
    <p><strong>Diagnostic fork:</strong> when the bottleneck is an unstable test system, generating more code is unlikely to help. When engineers repeatedly spend time creating or reviewing bounded tests with reliable inputs, an AI coding evaluation may be sensible. Both remain hypotheses until checked.</p>
  </section>

  <section class="research-canvas__inventory" id="stakeholder-perspectives" data-reveal>
    <header><p class="research-canvas__eyebrow">Stakeholder triangulation</p><h2>Five perspectives, one shared delivery story</h2>
      <p>Different roles see different failure points. Reconcile the accounts using artifacts and timelines rather than choosing the most senior person's explanation.</p></header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Voice</th><th scope="col">Useful contribution</th><th scope="col">Evidence to request</th></tr></thead><tbody>
        <tr><th scope="row">Engineering lead</th><td>Capacity, technical constraints, and quality priorities.</td><td>Recurring change types, defect trends, ownership.</td></tr>
        <tr><th scope="row">Platform or developer enablement</th><td>Shared tools, developer workflows, ability to run evaluations.</td><td>Available repositories, approved environments, evaluation owner.</td></tr>
        <tr><th scope="row">Product or delivery owner</th><td>Commercial deadlines and user impact.</td><td>Release milestones, missed commitments, business consequences.</td></tr>
        <tr><th scope="row">ABAP developer and SAP functional consultant</th><td>Actual workarounds, dependencies, and verification steps.</td><td>One change request, code and configuration context, review result.</td></tr>
        <tr><th scope="row">Security or governance contact</th><td>Whether a safe assessment is possible and who must be involved later.</td><td>Known restrictions and required specialist follow-up; not a full security design.</td></tr>
      </tbody></table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="evidence-snapshot" data-reveal>
    <header><p class="research-canvas__eyebrow">Reusable output / Discovery record</p><h2>Leave the meeting with decisions, not a transcript</h2>
      <p>Use four labels to prevent an early sales assumption from becoming an architectural fact.</p></header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Field</th><th scope="col">Hypothetical SAP release example</th></tr></thead><tbody>
        <tr><th scope="row">Observed or reported</th><td>The delivery manager reports repeated validation delays on customer master integration changes. This is a customer statement, not independently verified frequency.</td></tr>
        <tr><th scope="row">Possible explanation</th><td>Missing mapping regression cases may be driving rework. Alternative causes include incomplete requirements, environment issues, and review delays.</td></tr>
        <tr><th scope="row">Qualification judgment</th><td>Worth investigating as a delivery problem; Codex suitability remains unproven until a repeatable engineering task is isolated.</td></tr>
        <tr><th scope="row">Missing proof / next owner</th><td>Obtain two recent defects, representative code and test artifacts, affected release dates, and a named engineering reviewer. Ask the delivery owner to arrange a focused follow-up.</td></tr>
      </tbody></table>
    </div>
    <div class="ecg-decision-columns">
      <div><h3>One-page meeting record</h3>
        <ul><li>Delivery outcome under pressure and source of the claim.</li><li>Workflow steps and observed waiting point.</li><li>Evidence of recurrence and business impact.</li><li>Accountable owner and evaluation participants.</li><li>Candidate task, inputs and tools, target artifact, and reviewer.</li><li>Assumptions, missing evidence, next question, and owner of the follow-up.</li></ul>
      </div>
      <div><h3>What to say next</h3>
        <blockquote><p>“We have a credible release-delivery concern, but we do not yet know where most of the rework originates. Could we examine two recent changes with the people who implemented and validated them? Then we can decide whether one engineering task is suitable for a small, measurable AI evaluation.”</p></blockquote>
        <p><strong>Decision:</strong> advance only when the team can explain the candidate task and a realistic way to assess it. Otherwise gather evidence, select a different solution direction, or stop.</p>
      </div>
    </div>
  </section>


  <section class="research-canvas__inventory" id="progression-decision" data-reveal>
    <header><p class="research-canvas__eyebrow">After discovery / Decision gate</p><h2>Choose the next move, not the product pitch</h2>
      <p>Discovery is useful only if it changes what the team does next. A promising conversation is not automatically a qualified opportunity, and a qualified opportunity is not an approved implementation. Decide whether there is enough evidence to bring in technical specialists for a more focused assessment.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Decision</th><th scope="col">Use it when</th><th scope="col">Practical next action</th></tr></thead><tbody>
        <tr><th scope="row">Advance</th><td>The issue repeats, its consequences matter, the right owner participates, and a reviewable engineering task can be framed with plausible access to its inputs.</td><td>Arrange a focused technical evaluation discussion, with the task owner and a specialist who can test feasibility.</td></tr>
        <tr><th scope="row">Investigate further</th><td>The delivery concern is credible, but its bottleneck, accountable owner, scale, or candidate task remains uncertain.</td><td>Request one recent change or defect, map the timeline, and assign a person to close the most important evidence gap.</td></tr>
        <tr><th scope="row">Put on hold</th><td>Interest is genuine, but the organization has no current priority, capacity, or commitment to examine the workflow.</td><td>Record the reason and a concrete condition that would justify revisiting the conversation.</td></tr>
        <tr><th scope="row">Remove from the Codex path</th><td>The need is outside software engineering, no verifiable task exists, or the business case does not justify further effort.</td><td>Explain the mismatch; redirect to a better approach when warranted, or close the thread.</td></tr>
      </tbody></table>
    </div>
    <p><strong>Boundary:</strong> removing a prospect from the coding-agent path is not the same as rejecting its business need. Search and knowledge work, internal productivity, and AI-powered product features may warrant different solutions or no AI at all.</p>
  </section>

  <section class="research-canvas__inventory" id="technical-handoff" data-reveal>
    <header><p class="research-canvas__eyebrow">Readiness / Seller to architect</p><h2>Make the technical handoff specific enough to be useful</h2>
      <p>A seller does not need to settle deployment, permissions, or governance architecture. The seller does need to show that the proposed evaluation has a coherent job, usable material, an expected result, and somebody qualified to review it.</p></header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Handoff item</th><th scope="col">Minimum useful answer</th><th scope="col">Example for SAP ABAP</th></tr></thead><tbody>
        <tr><th scope="row">Task</th><td>One bounded activity that can be completed and inspected.</td><td>Produce or revise regression tests for one defined inbound mapping change.</td></tr>
        <tr><th scope="row">Inputs and tools</th><td>Identify the sources, code, documentation, tickets, and tooling the activity needs. Record access uncertainties.</td><td>Versioned mapping logic, specification, test harness, and prior defect cases; confirm what can be shared with the evaluation team.</td></tr>
        <tr><th scope="row">Output boundary</th><td>A named artifact or safe working environment, with a known extent of change.</td><td>Suggested tests and a reviewed patch in an isolated development branch; no production transport.</td></tr>
        <tr><th scope="row">Proof</th><td>Checks that can fail, plus the expert who will interpret the result.</td><td>Existing tests still pass, new tests cover agreed scenarios, and ABAP and functional reviewers accept the behavior.</td></tr>
        <tr><th scope="row">Open concerns</th><td>Identify which specialists must address access, security, governance, or review questions later.</td><td>Client data handling and repository access are flagged for the designated technical and security owners.</td></tr>
      </tbody></table>
    </div>
    <p><strong>Decision rule:</strong> uncertain access may still justify a specialist conversation if there is a realistic route to checking feasibility. Unknown inputs, no target artifact, and no possible verification mean the candidate task is not yet ready.</p>
  </section>

  <section class="research-canvas__inventory" id="recommendation-brief" data-reveal>
    <header><p class="research-canvas__eyebrow">Practical output / Recommendation</p><h2>Make the recommendation easy to challenge</h2>
      <p>An actionable recommendation is short enough to discuss, but explicit enough that another person can check its evidence.</p></header>
    <div class="ecg-decision-columns">
      <div>
        <h3>Five statements to complete</h3>
        <ol>
          <li><strong>Problem:</strong> name the recurring activity and where it breaks down.</li>
          <li><strong>Effect:</strong> identify the operational or business consequence and its evidence.</li>
          <li><strong>Owner:</strong> specify who is accountable and who will validate the work.</li>
          <li><strong>Reason to act:</strong> identify the current release, priority, or measurable reason for timing.</li>
          <li><strong>Next step:</strong> explain the candidate task, prerequisites, verification method, and people required.</li>
        </ol>
      </div>
      <div>
        <h3>Example recommendation (fictional)</h3>
        <p>Repeated rework on a customer integration enhancement is delaying release validation. The delivery manager has supplied examples from recent iterations, and the SAP development lead has agreed to examine test coverage. A specific change and existing test suite could support a controlled coding-assistant assessment, provided repository access is approved and a functional reviewer can check the result. Recommend a joint technical discovery session, not immediate rollout.</p>
        <p><strong>What is still unproven?</strong> Whether an AI-assisted approach improves completion time or defect detection against the team's current practice.</p>
      </div>
    </div>
    <div class="research-canvas__table-wrap">
      <h3>Counterexample: not ready to advance</h3>
      <table><thead><tr><th scope="col">Observed situation</th><th scope="col">Appropriate response</th></tr></thead><tbody>
        <tr><th scope="row">A stakeholder asks for a Codex demonstration but cannot identify a recurring task.</th><td>Explore workflow examples first; do not treat the demo request as proof of fit.</td></tr>
        <tr><th scope="row">Engineering reports significant delays, but the cause and owner are unknown.</th><td>Keep discovery open with an assigned evidence request and follow-up date.</td></tr>
        <tr><th scope="row">The urgent issue is an unavailable SAP test client.</th><td>Investigate infrastructure and environment recovery before proposing code generation.</td></tr>
        <tr><th scope="row">Employees need to find approved instructions in many documents.</th><td>Consider knowledge-search and productivity options rather than forcing a coding-agent use case.</td></tr>
      </tbody></table>
    </div>
    <p><strong>Practice question:</strong> A client has a critical deadline, an engaged CIO, and enthusiasm for AI, but no defined engineering task or reviewer. Would you advance the Codex opportunity? Explain what evidence must be collected first, in 45 seconds of professional English.</p>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">source</span>
    <div>
      <p><strong>Editorial note:</strong> original synthesis and SAP examples prepared from learning notes on identifying and qualifying engineering AI opportunities. This is not a transcript or an official OpenAI qualification framework.</p>
      <p><strong>Related:</strong> <a href="/labs/business-ai/">Business AI discovery</a> · <a href="/labs/ai-ready/">Practical AI architecture</a>.</p>
    </div>
  </section>
</div>
