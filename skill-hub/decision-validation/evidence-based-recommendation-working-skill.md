---
layout: default
title: "Evidence-Based Recommendation Writing Working Skill"
description: "Write recommendations that state what should be done, why it should be done, and what evidence supports the claim — so that approvers can decide without guessing."
permalink: /skill-hub/decision-validation/evidence-based-recommendation-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/decision-validation/">Decision & Validation</a></li>
    <li aria-current="page">Evidence-Based Recommendation Writing</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Decision & Validation</p>
  <h1>Evidence-Based Recommendation Writing Working Skill</h1>
  <p class="lead">Write recommendations that state what should be done, why it should be done, and what evidence supports the claim — so that approvers can decide without guessing.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you write recommendations that decision-makers can approve or reject with confidence. It separates evidence from opinion, states what was considered and rejected, and makes the risks of the chosen path visible. The output is a Recommendation Note that tells the reader: what the situation is, what options were evaluated, what evidence supports each option, which option is recommended, why it is recommended, what the risks are, and what must happen next.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A steering committee needs a one-page recommendation with supporting evidence for a major investment decision.</li>
      <li>An architecture board must choose between competing integration patterns and needs a documented rationale.</li>
      <li>A change advisory board needs to approve or reject an emergency patch deployment with evidence of risk and benefit.</li>
      <li>A project manager must recommend a scope reduction to meet a deadline, with evidence of what is lost and what is preserved.</li>
      <li>A business analyst must recommend a process change, with evidence from system logs, stakeholder interviews, and pilot results.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>Steering committee: recommend SAP S/4 migration approach</h3>
    <p>A steering committee must decide whether to migrate to SAP S/4HANA through a greenfield implementation, a brownfield conversion, or a selective data transition. The evidence-based recommendation presents: (1) situation — current ECC system has 150 custom objects, 8 of which are critical; (2) options considered — greenfield (cleanest but longest), brownfield (fastest but carries custom debt), selective (balanced but complex); (3) evidence — greenfield pilot showed 6-month delay due to data model redesign; brownfield assessment showed 40% of custom objects are redundant; selective data transition reference from a peer company showed 18% cost overrun but on-time delivery; (4) recommendation — selective data transition with a parallel clean-core extension track; (5) risks — cost overrun if data archiving is not completed on schedule; (6) next steps — approve budget, begin data archiving sprint, select implementation partner by July 30.</p>

    <h3>Architecture board: recommend API strategy for customer integration</h3>
    <p>The architecture board must choose how to integrate a new customer portal with SAP. The recommendation presents: (1) situation — current customer master is maintained in SAP ECC via XD01; portal requires real-time validation; (2) options — direct RFC calls, OData API via SAP Gateway, middleware with event bus; (3) evidence — load test showing RFC calls fail at 500 concurrent users; OData reference showing 2,000-user capacity; middleware cost estimate from vendor; (4) recommendation — OData API with a middleware fallback for peak events; (5) risks — middleware fallback requires new operational runbook; (6) next steps — approve API contract, build load test environment, draft runbook.</p>

    <h3>Change advisory board: recommend emergency patch deployment</h3>
    <p>A critical IDoc interface failure is blocking goods receipts. The CAB must decide whether to approve an emergency patch outside the normal release window. The recommendation presents: (1) situation — IDoc status 51 errors since 02:00, affecting 12 purchase orders, blocking warehouse operations; (2) options — wait for standard release window (Monday), deploy emergency patch now (Friday), apply temporary workaround (manual posting); (3) evidence — system logs showing error pattern matches known bug SAP Note 1234567; manual posting took 4 hours for 3 orders yesterday; weekend warehouse schedule has 40 receipts planned; (4) recommendation — deploy emergency patch now with rollback plan; (5) risks — patch may affect other IDoc types; (6) next steps — CAB approval, deployment in 2 hours with monitoring, post-deployment validation of 5 IDoc types.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>A clear situation statement: what is happening, who is affected, and what the deadline is.</li>
      <li>A list of options that were seriously considered, including the "do nothing" or "status quo" option.</li>
      <li>Evidence for each option: system logs, data samples, benchmark results, stakeholder input, vendor quotes, pilot results, or precedent from similar decisions.</li>
      <li>Constraints: budget, timeline, compliance, or resource limits that eliminate some options.</li>
      <li>A risk assessment for the recommended option: what could go wrong and how it would be detected.</li>
      <li>The decision-maker's authority level and what they need to know to decide.</li>
      <li>A <a href="/skill-hub/decision-validation/trade-off-analysis-working-skill/">Trade-Off Analysis</a> or <a href="/skill-hub/decision-validation/option-comparison-matrix-working-skill/">Option Comparison Matrix</a> if the recommendation follows a structured comparison.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What should be done, in one sentence?</li>
      <li>Why should it be done, and what is the cost of not doing it?</li>
      <li>What evidence supports this recommendation, and where did the evidence come from?</li>
      <li>What other options were considered, and why were they rejected?</li>
      <li>Is this recommendation based on evidence, or on opinion, or on precedent? Label it.</li>
      <li>What are the risks of following this recommendation, and how will we know if they materialize?</li>
      <li>What must happen next, who must do it, and by when?</li>
      <li>What would make us reconsider this recommendation after it is approved?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>State the situation.</strong> Write one paragraph: what is happening, who is affected, what the business impact is, and what the deadline is. Attach evidence (logs, data, tickets).</li>
      <li><strong>Define the decision required.</strong> One sentence: "We need a decision on X by Y because Z." Name the decision-maker and the authority.</li>
      <li><strong>List options considered.</strong> Describe 2–4 options that were seriously evaluated. Include the status quo or "do nothing" option. For each option, state the key advantage and disadvantage.</li>
      <li><strong>Present evidence for each option.</strong> For each option, list the evidence that supports or contradicts it. Evidence types: system data (logs, metrics), stakeholder input (interviews, surveys), precedent (past similar decisions), vendor documentation, pilot or test results. Label each piece of evidence with its source and date.</li>
      <li><strong>State the recommendation.</strong> One sentence: "We recommend [Option X] because [primary reason]." The recommendation must be explicit, not implied.</li>
      <li><strong>Provide the rationale.</strong> Explain why the recommended option is better than the runner-up. Reference specific evidence. Address the runner-up's strengths and explain why they are insufficient in this situation.</li>
      <li><strong>List the risks of the recommendation.</strong> What could go wrong if the recommendation is followed? Include probability, impact, and detection method. Do not hide risks to make the recommendation look better.</li>
      <li><strong>Define next steps.</strong> What must happen if the recommendation is approved? List actions, owners, and deadlines. Also state what happens if the recommendation is rejected.</li>
      <li><strong>Append the evidence.</strong> Include or reference the raw data, logs, or documents that support the evidence claims. A recommendation without appendices is a claim without proof.</li>
      <li><strong>Review for opinion leakage.</strong> Read the recommendation and highlight every sentence that is not backed by evidence. Rewrite or label those sentences as "judgment — not evidence-based."</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the evidence for a critical claim is weaker than the opinion behind it, flag the claim as judgment and separate it from the evidence-based recommendation.</li>
      <li>If the recommendation is not the highest-scoring option from a prior analysis, explain why the highest-scoring option was rejected with evidence.</li>
      <li>If no evidence exists for a critical claim, do not make the claim — or state it as a hypothesis with a validation plan.</li>
      <li>If the "do nothing" option is not included, the recommendation may be solving the wrong problem. Always include it.</li>
      <li>If the risk section is shorter than the benefit section, the writer is hiding something. Lengthen the risk section.</li>
      <li>If the next steps have no owner or deadline, the recommendation is not actionable. Add owners and dates.</li>
      <li>If the decision-maker needs less detail, produce a summary page with appendices. Do not remove the evidence — move it.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Recommendation Note</strong> — the primary artifact with situation, options, evidence, recommendation, rationale, risks, and next steps. See template below.</li>
      <li><strong>Evidence Appendix</strong> — raw data, system logs, screenshots, reference call summaries, or vendor quotes that support the evidence claims.</li>
      <li><strong>Executive Summary</strong> — one page for decision-makers who need the bottom line without the full analysis.</li>
      <li><strong>Decision Record</strong> — what was decided, by whom, on what date, with what conditions or contingencies.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Recommendation Note</h3>
    <pre><code>---
artifact: Recommendation Note
id: REC-001
date: YYYY-MM-DD
authority: "Who decides"
decision_deadline: YYYY-MM-DD
---

## Situation
<!-- What is happening, who is affected, business impact, deadline. -->
<!-- Attach evidence: logs, data, tickets. -->

## Decision Required
<!-- One sentence. Example: "We need a decision on the integration approach for the customer portal by June 30, decided by the Architecture Board." -->

## Options Considered

### Option 1: [Name]
- Key advantage: <!-- Evidence-based -->
- Key disadvantage: <!-- Evidence-based -->
- Evidence: <!-- Source and date -->

### Option 2: [Name]
- Key advantage: <!-- Evidence-based -->
- Key disadvantage: <!-- Evidence-based -->
- Evidence: <!-- Source and date -->

### Option 3: [Name] (Status Quo / Do Nothing)
- Key advantage: <!-- Evidence-based -->
- Key disadvantage: <!-- Evidence-based -->
- Evidence: <!-- Source and date -->

## Evidence Summary
| Option | Evidence Type | Source | Date | Finding |
|--------|---------------|--------|------|---------|
| Option 1 | System log | <!-- Source --> | YYYY-MM-DD | <!-- Finding --> |
| Option 2 | Stakeholder interview | <!-- Source --> | YYYY-MM-DD | <!-- Finding --> |
| Option 3 | Precedent | <!-- Source --> | YYYY-MM-DD | <!-- Finding --> |

## Recommendation
<!-- One sentence. Be explicit. -->

## Rationale
<!-- Why the recommended option is better than the runner-up. Reference specific evidence. Address the runner-up's strengths. -->

## Risks of the Recommendation
| Risk | Probability | Impact | Detection Method | Mitigation |
|------|-------------|--------|------------------|------------|
| <!-- Risk --> | L/M/H | L/M/H | <!-- How we know --> | <!-- Action --> |
| <!-- Risk --> | L/M/H | L/M/H | <!-- How we know --> | <!-- Action --> |

## Next Steps (If Approved)
| Action | Owner | Deadline | Success Criterion |
|--------|-------|----------|-------------------|
| <!-- Action --> | <!-- Name --> | YYYY-MM-DD | <!-- Measurable --> |
| <!-- Action --> | <!-- Name --> | YYYY-MM-DD | <!-- Measurable --> |

## Next Steps (If Rejected)
<!-- What happens if the recommendation is not approved -->

## Evidence Appendix
<!-- Links or references to raw data, logs, documents -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The situation is stated with evidence, not just narrative.</li>
      <li>The decision required is explicit, with named authority and deadline.</li>
      <li>At least two options were seriously considered, including status quo.</li>
      <li>Every option has evidence with a source and date.</li>
      <li>The recommendation is stated in one explicit sentence.</li>
      <li>The rationale references specific evidence and addresses the runner-up's strengths.</li>
      <li>Risks are listed with probability, impact, and detection method.</li>
      <li>Next steps have named owners, deadlines, and success criteria.</li>
      <li>Opinion is labeled as judgment and separated from evidence.</li>
      <li>The evidence appendix is present or referenced.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Hiding the risks to make the recommendation look better.</strong> Consequence: the decision-maker approves without understanding the downside. When the risk materializes, the decision-maker feels deceived and trust is damaged.</li>
      <li><strong>Confusing opinion with evidence.</strong> Consequence: the recommendation is challenged on grounds that cannot be defended. The writer retreats to "in my experience" instead of data.</li>
      <li><strong>Not including the status quo option.</strong> Consequence: the project may be solving the wrong problem. The decision-maker cannot compare the cost of action against the cost of inaction.</li>
      <li><strong>Omitting the runner-up's strengths.</strong> Consequence: the recommendation looks biased. A decision-maker who knows the runner-up's advantages will distrust the writer.</li>
      <li><strong>Writing next steps without owners or deadlines.</strong> Consequence: the recommendation is approved but never executed. The note becomes a document, not a decision tool.</li>
      <li><strong>Attaching evidence that does not match the claim.</strong> Consequence: a careful reviewer discovers the disconnect. The writer's credibility is damaged for future recommendations.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A paragraph stating: "We recommend Option B because it is the most robust and scalable solution. The team has extensive experience with this approach, and it aligns with our strategic direction. Option A was considered but does not meet our long-term needs. We should proceed with Option B as soon as possible."</p>
    <p><strong>Why it is weak:</strong> No evidence is cited. "Most robust and scalable" is unverifiable. "Extensive experience" is opinion, not data. "Aligns with strategic direction" is narrative bias. The runner-up is dismissed without addressing its strengths. There are no risks, no next steps, no owners, and no deadline. A decision-maker cannot approve this with confidence.</p>

    <h3>Strong output</h3>
    <p>A Recommendation Note with: (1) situation — "IDoc status 51 errors since 02:00 affecting 12 purchase orders, blocking warehouse operations; 40 receipts planned for weekend" with system log extract; (2) decision required — "CAB approval for emergency patch deployment outside standard release window by 14:00 today" ; (3) three options: emergency patch now (advantage: fixes root cause; disadvantage: non-standard window), wait for Monday release (advantage: standard process; disadvantage: 40 receipts blocked), manual workaround (advantage: no patch risk; disadvantage: 4 hours per 3 orders based on yesterday's data); (4) evidence: SAP Note 1234567 matches error pattern; manual posting took 4 hours; weekend schedule has 40 receipts; (5) recommendation — "Deploy emergency patch now with rollback plan" ; (6) rationale — "The root cause is identified and fixed by SAP Note 1234567. Waiting until Monday blocks 40 receipts at an estimated cost of €12,000. Manual workaround is not feasible at this volume. The patch has been tested in the QA environment." ; (7) risks: patch may affect other IDoc types (detection: post-deployment validation of 5 types; mitigation: rollback plan); (8) next steps: CAB approval by 14:00, deployment by 16:00, validation by 18:00, with named owners and deadlines.</p>
    <p><strong>Why it is strong:</strong> Every claim is backed by evidence with a source. The runner-up (wait for Monday) is treated fairly with its own evidence. The recommendation is explicit and actionable. Risks are visible and mitigated. A decision-maker can approve or reject with full information.</p>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><code>You are a recommendation writer. I will give you a situation, options, and evidence. Produce a Recommendation Note with: (1) situation with evidence, (2) decision required with authority and deadline, (3) options considered with evidence for each, (4) explicit recommendation, (5) rationale referencing specific evidence, (6) risks with probability, impact, and detection, (7) next steps with owners and deadlines. Do not use generic language like "robust," "scalable," or "strategic direction." Cite evidence for every claim. Label opinion as "judgment." Include the status quo option. State what happens if the recommendation is rejected.</code></p>

    <ul>
      <li><strong>Separate evidence from opinion.</strong> Every sentence must be labeled as evidence (with source) or judgment (with owner). If it cannot be labeled, remove it.</li>
      <li><strong>Always include the status quo option.</strong> The cost of inaction is a valid comparison point. Without it, the recommendation may be unjustified.</li>
      <li><strong>Never hide risks.</strong> A recommendation with a short risk section looks suspicious. Lengthen it until it is honest.</li>
      <li><strong>Address the runner-up's strengths.</strong> A recommendation that ignores the second-best option looks biased. Explain why its strengths are insufficient in this context.</li>
      <li><strong>Never invent evidence.</strong> If data is missing, state "evidence not available — recommendation based on judgment and precedent" and flag it.</li>
      <li><strong>Make next steps actionable.</strong> Every step needs a named owner, a deadline, and a success criterion. Vague next steps are not next steps.</li>
      <li><strong>Link to Atlas diagnostics</strong> when the recommendation involves SAP processes or master data. For example, reference <a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> for evidence sources or <a href="/scenarios/master-data-issues-blocking-sales-orders/">Master Data Issues Blocking Sales Orders</a> for situation context.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/decision-validation/trade-off-analysis-working-skill/">Trade-Off Analysis Working Skill</a></li>
      <li><a href="/skill-hub/decision-validation/option-comparison-matrix-working-skill/">Option Comparison Matrix Working Skill</a></li>
      <li><a href="/skill-hub/architecture/architecture-decision-record-working-skill/">Architecture Decision Record Working Skill</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — Source of evidence for process-related recommendations.</li>
      <li><a href="/scenarios/master-data-issues-blocking-sales-orders/">Master Data Issues Blocking Sales Orders</a> — Example situation with evidence and recommendation context.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of recommendation writing practices. It is not official BABOK, management consulting methodology, or SAP documentation. It focuses on practical recommendations in enterprise and SAP contexts.</p>
    <p>Known limitations: the skill requires access to evidence, which may be scattered across system logs, stakeholder interviews, and vendor documentation. In environments with poor data availability, the recommendation will rely more on judgment and precedent — this must be labeled honestly. The skill does not cover formal decision theory, cost-benefit analysis, or investment appraisal methods (NPV, IRR). It assumes the decision-maker needs a structured narrative, not a financial model.</p>
  </section>
</article>
