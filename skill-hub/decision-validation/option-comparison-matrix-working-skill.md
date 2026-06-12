---
layout: default
title: "Option Comparison Matrix Working Skill"
description: "Produce a structured comparison of options against weighted criteria so that stakeholders can see why one option is better without relying on narrative bias."
permalink: /skill-hub/decision-validation/option-comparison-matrix-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/decision-validation/">Decision & Validation</a></li>
    <li aria-current="page">Option Comparison Matrix</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Decision & Validation</p>
  <h1>Option Comparison Matrix Working Skill</h1>
  <p class="lead">Produce a structured comparison of options against weighted criteria so that stakeholders can see why one option is better without relying on narrative bias.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you create a decision matrix that makes the comparison between options visible and verifiable. It replaces long narrative documents with a compact table where every cell contains a score, evidence, and a source. The matrix is readable for executives who need the bottom line and actionable for implementers who need to understand the gaps in the chosen option.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>An ERP selection requires comparing SAP S/4, Oracle, and Microsoft Dynamics across functional, technical, and cost dimensions.</li>
      <li>An integration platform choice requires scoring SAP PI/PO, MuleSoft, and Boomi against throughput, monitoring, and team skill criteria.</li>
      <li>A cloud migration strategy requires comparing lift-and-shift, re-platform, and re-architect options against speed, cost, and risk.</li>
      <li>A vendor selection must compare three implementation partners against experience, methodology, cost, and reference quality.</li>
      <li>A steering committee needs a one-page view of why one option is better than the others.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>ERP selection: SAP S/4 vs Oracle vs Microsoft Dynamics</h3>
    <p>A mid-size manufacturer must replace its legacy ERP. The option comparison matrix scores each vendor against criteria like manufacturing functionality (weighted 0.25), integration flexibility (0.20), total cost of ownership (0.20), implementation partner availability (0.15), and cloud deployment options (0.20). The matrix reveals that SAP S/4 wins on manufacturing depth but scores lower on TCO due to licensing complexity. Oracle scores highest on analytics but fails the mandatory requirement for SAP-compatible IDoc integration. Without the matrix, the decision is driven by the vendor with the best demo, not by the capability gaps that will appear in year two.</p>

    <h3>Integration platform: SAP PI/PO vs MuleSoft vs custom middleware</h3>
    <p>A retail company needs to integrate 40 store POS systems with SAP. The matrix compares the existing SAP PI/PO landscape, a MuleSoft cloud deployment, and a custom lightweight middleware. Criteria include peak message throughput (0.30), operational monitoring maturity (0.25), SAP certification and support (0.20), team skill availability (0.15), and time to production (0.10). The matrix shows that SAP PI/PO wins on certification but fails on throughput under peak load. MuleSoft wins on throughput and monitoring but requires a new support contract. The custom option scores highest on cost but fails the mandatory support requirement.</p>

    <h3>Cloud migration strategy: lift-and-shift vs re-platform vs re-architect</h3>
    <p>A company running SAP ECC on-premises must move to Azure. The matrix compares three strategies. Lift-and-shift is fastest but carries the highest long-term cost. Re-platform (move to SAP HANA on Azure) balances speed and benefit. Re-architect (move to S/4HANA with clean core) offers the highest long-term value but takes 18 months. Criteria include time to cloud (0.25), total migration cost (0.25), operational cost reduction (0.20), business disruption risk (0.15), and future readiness (0.15). The matrix makes visible that re-platform wins on time and cost but scores lower on future readiness — a trade-off the board can understand and accept.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>The decision scope and boundary: what is in scope and what is explicitly excluded.</li>
      <li>A list of options under evaluation, each described with enough detail for scoring.</li>
      <li>Evaluation criteria derived from business requirements, not from vendor feature lists.</li>
      <li>A scoring scale definition (e.g., 1–5) with clear behavioral anchors for each level.</li>
      <li>A weighting scheme that reflects stakeholder priorities, not equal weights by default.</li>
      <li>Evidence for each option against each criterion: vendor quotes, proof-of-concept results, reference calls, benchmark data.</li>
      <li>Constraints that may eliminate options regardless of score: compliance mandates, exclusive contracts, budget ceilings.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What criteria are pass/fail (mandatory) versus scored (weighted)?</li>
      <li>What scoring scale eliminates ambiguity between scorers?</li>
      <li>Who scores, who reviews, and who has the final say?</li>
      <li>What evidence is required before a score can be assigned?</li>
      <li>How many criteria are too many? (Rule of thumb: more than 7 weighted criteria dilutes focus.)</li>
      <li>What would make an option score change after a deeper review?</li>
      <li>Are we comparing against requirements or against each other? (An option can score 5/5 on all criteria and still be wrong if the criteria are wrong.)</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Define the decision scope.</strong> State what is being decided, what is in scope, and what is excluded. Write one sentence.</li>
      <li><strong>List the options.</strong> Describe each option in 2–3 sentences. Include the "do nothing" or "status quo" option if it is realistic.</li>
      <li><strong>Define criteria.</strong> Derive criteria from business requirements, not vendor features. Separate mandatory (pass/fail) from weighted (scored). Limit weighted criteria to 5–7.</li>
      <li><strong>Define the scoring scale.</strong> Use a 1–5 scale with behavioral anchors. Example: 1 = does not meet requirement, 3 = meets requirement with known gaps, 5 = exceeds requirement with evidence.</li>
      <li><strong>Assign weights.</strong> Weights must reflect stakeholder priorities and sum to 1.0. Document who provided each weight and why.</li>
      <li><strong>Score each option independently.</strong> One scorer per option to reduce halo effects, or multiple scorers with reconciliation for outliers.</li>
      <li><strong>Calculate weighted scores.</strong> For each option, sum (raw score × criterion weight) across all weighted criteria.</li>
      <li><strong>Review and normalize.</strong> Check for scoring drift (one scorer consistently rates higher). Adjust if evidence supports it.</li>
      <li><strong>Apply mandatory elimination.</strong> Remove any option that fails a mandatory criterion, regardless of weighted score.</li>
      <li><strong>Document the matrix.</strong> Produce a clean table with options as rows, criteria as columns, raw scores in cells, and weighted totals in the final row. Include evidence references.</li>
      <li><strong>Present with context.</strong> Add a narrative paragraph explaining the winner, the margin, and the most important gaps in the winning option.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If an option fails a mandatory criterion, eliminate it regardless of weighted score.</li>
      <li>If two options differ by less than one point on a 1–5 scale for a critical criterion, the evidence is insufficient — gather more data.</li>
      <li>If one scorer is an outlier (more than one point from the mean on multiple criteria), investigate before averaging.</li>
      <li>If weighted criteria outnumber options by more than 3:1, simplify the matrix to avoid noise.</li>
      <li>If the winning option has a critical gap (score ≤ 2 on a high-weight criterion), flag it as a conditional win with mitigation plan.</li>
      <li>If weights were assigned by a single person without stakeholder input, label the matrix as "draft — pending weight validation."</li>
      <li>If the status quo option wins, the project may not be justified — revisit the business case.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Option Comparison Matrix</strong> — a compact table with options, criteria, raw scores, weights, and weighted totals. See template below.</li>
      <li><strong>Scoring Guide</strong> — definition of the 1–5 scale with behavioral anchors for each criterion.</li>
      <li><strong>Evidence Appendix</strong> — sources, dates, and summaries of the evidence used for each score.</li>
      <li><strong>Executive Summary</strong> — one paragraph stating the winner, margin, and key gaps in the winning option.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Option Comparison Matrix (compact)</h3>
    <pre><code>---
artifact: Option Comparison Matrix
id: OCM-001
date: YYYY-MM-DD
scope: "What is being decided"
authority: "Who decides"
---

## Decision Scope
<!-- One sentence. Example: "Select integration platform for 40-store POS-to-SAP connectivity." -->

## Options
| Option | Description |
|--------|-------------|
| Option 1 | <!-- 2–3 sentences --> |
| Option 2 | <!-- 2–3 sentences --> |
| Option 3 | <!-- 2–3 sentences --> |

## Mandatory Criteria (Pass/Fail)
| Criterion | Option 1 | Option 2 | Option 3 | Source |
|-----------|----------|----------|----------|--------|
| Must-have 1 | Pass/Fail | Pass/Fail | Pass/Fail | <!-- Who required it --> |
| Must-have 2 | Pass/Fail | Pass/Fail | Pass/Fail | <!-- Who required it --> |

## Weighted Criteria and Scoring
<!-- Scale: 1 = Poor, 3 = Adequate, 5 = Excellent. Include behavioral anchors. -->

| Criterion | Weight | Option 1 | Evidence | Option 2 | Evidence | Option 3 | Evidence |
|-----------|--------|----------|----------|----------|----------|----------|----------|
| Criterion 1 (0.30) | 0.30 | 3 | <!-- Source --> | 5 | <!-- Source --> | 4 | <!-- Source --> |
| Criterion 2 (0.25) | 0.25 | 4 | <!-- Source --> | 3 | <!-- Source --> | 3 | <!-- Source --> |
| Criterion 3 (0.20) | 0.20 | 3 | <!-- Source --> | 4 | <!-- Source --> | 2 | <!-- Source --> |
| Criterion 4 (0.15) | 0.15 | 5 | <!-- Source --> | 4 | <!-- Source --> | 3 | <!-- Source --> |
| Criterion 5 (0.10) | 0.10 | 2 | <!-- Source --> | 4 | <!-- Source --> | 5 | <!-- Source --> |

## Weighted Totals
| Option | Calculation | Total | Rank |
|--------|-------------|-------|------|
| Option 1 | (3×0.30)+(4×0.25)+(3×0.20)+(5×0.15)+(2×0.10) | 3.55 | 2 |
| Option 2 | (5×0.30)+(3×0.25)+(4×0.20)+(4×0.15)+(4×0.10) | 4.15 | 1 |
| Option 3 | (4×0.30)+(3×0.25)+(2×0.20)+(3×0.15)+(5×0.10) | 3.20 | 3 |

## Mandatory Elimination
<!-- List any options eliminated and the mandatory criterion they failed -->

## Executive Summary
<!-- Winner, margin, and key gaps in the winning option -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The decision scope is explicit and narrow.</li>
      <li>Every option is described in enough detail for a non-technical reader.</li>
      <li>Criteria are derived from business requirements, not vendor marketing.</li>
      <li>The scoring scale has behavioral anchors that reduce scorer ambiguity.</li>
      <li>Weights sum to 1.0 and are traceable to stakeholder input.</li>
      <li>Every score is backed by evidence with a source.</li>
      <li>Mandatory elimination is applied and documented.</li>
      <li>Weighted totals are calculated correctly.</li>
      <li>The executive summary states the winner, the margin, and the gaps in the winning option.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Using vendor feature lists as criteria.</strong> Consequence: the matrix compares what vendors say they have, not what the business needs. The winning option has features that will never be used while missing critical requirements.</li>
      <li><strong>Scoring without evidence.</strong> Consequence: scores reflect scorer bias or vendor persuasion. The matrix looks rigorous but is fiction.</li>
      <li><strong>Using equal weights to avoid difficult conversations.</strong> Consequence: the matrix produces a false sense of balance. A criterion that is critical to the business carries the same weight as a nice-to-have.</li>
      <li><strong>Skipping the scoring guide.</strong> Consequence: two scorers assign a 3 for different reasons. The matrix is inconsistent and cannot be reconciled.</li>
      <li><strong>Not including the status quo.</strong> Consequence: the project may not be justified. The matrix compares new options against each other but never against doing nothing.</li>
      <li><strong>Averaging outlier scores without investigation.</strong> Consequence: a scorer who misunderstood the option drags the average down, hiding a real strength or weakness.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A table with three columns (Option A, Option B, Option C) and five rows labeled "Cost," "Functionality," "Scalability," "Support," "Integration," each filled with checkmarks or vague ratings like "Good," "Better," "Best." No weights, no evidence, no scoring scale, no elimination logic.</p>
    <p><strong>Why it is weak:</strong> The ratings are arbitrary. A stakeholder cannot verify why Option B is "Better" on scalability. The matrix is a visualization of opinion, not a decision tool. It provides no traceability and no defense against challenge.</p>

    <h3>Strong output</h3>
    <p>A complete Option Comparison Matrix with: (1) decision scope — "Select integration platform for 40-store POS-to-SAP connectivity, decided by IT Steering Committee" ; (2) three options described with 2–3 sentences each; (3) two mandatory criteria (SAP-certified, sub-100ms latency) with pass/fail results; (4) five weighted criteria (throughput 0.30, monitoring 0.25, SAP certification 0.20, team skills 0.15, time to production 0.10) with behavioral anchors for the 1–5 scale; (5) raw scores with evidence references ("POC result from 2026-05-12," "Reference call with RetailCo on 2026-04-18"); (6) weighted totals showing Option 2 at 4.15, Option 1 at 3.55, Option 3 at 3.20; (7) mandatory elimination showing Option 3 failed latency; (8) executive summary: "Option 2 wins because it passes both mandatories and scores highest on throughput and monitoring, which are the two business-critical criteria. The key gap is team skill availability — a training plan is required."</p>
    <p><strong>Why it is strong:</strong> Every rating is traceable to evidence. The winner is justified by both mandatory compliance and weighted advantage. The gap in the winning option is explicit and actionable. A stakeholder can challenge a specific score or a specific weight without attacking the entire process.</p>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><code>You are an option comparison analyst. I will give you a decision scope, options, criteria, and evidence. Produce an Option Comparison Matrix with: (1) decision scope, (2) option descriptions, (3) mandatory criteria (pass/fail), (4) weighted criteria with behavioral anchors for a 1–5 scale, (5) raw scores with evidence cited, (6) weighted totals, (7) mandatory elimination, (8) executive summary. Do not use generic ratings like "good" or "best." Use numeric scores only. Cite evidence for every score. If evidence is missing, score as "unknown" and flag it.</code></p>

    <ul>
      <li><strong>Derive criteria from requirements, not from vendor features.</strong> A matrix built on vendor marketing compares the wrong things.</li>
      <li><strong>Always define behavioral anchors for the scoring scale.</strong> Without anchors, different scorers produce incomparable results.</li>
      <li><strong>Separate mandatory and weighted criteria before scoring.</strong> An option that fails a mandatory must be eliminated even if it has the highest weighted score.</li>
      <li><strong>Never invent evidence or scores.</strong> If data is missing, write "unknown" and flag the gap.</li>
      <li><strong>Include the status quo option.</strong> If the status quo wins, the project may not be justified.</li>
      <li><strong>Do not average scores without checking for outliers.</strong> If one scorer is more than one point from the mean, investigate before averaging.</li>
      <li><strong>Link to Atlas diagnostics</strong> when the comparison involves SAP integration or APIs. For example, reference <a href="/atlas/concepts/sap-integration-architecture/">SAP Integration Architecture</a> or <a href="/atlas/concepts/api-contracts/">API Contracts</a> for criteria.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/decision-validation/trade-off-analysis-working-skill/">Trade-Off Analysis Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/gap-analysis-working-skill/">Gap Analysis Working Skill</a></li>
      <li><a href="/skill-hub/architecture/solution-architecture-review-working-skill/">Solution Architecture Review Working Skill</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/sap-integration-architecture/">SAP Integration Architecture</a> — Patterns and criteria for integration platform comparisons.</li>
      <li><a href="/atlas/concepts/api-contracts/">API Contracts</a> — One of the common criteria in integration platform comparisons.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of decision matrix practices. It is not official BABOK, procurement methodology, or vendor framework documentation. It focuses on practical technology and vendor selection in enterprise and SAP contexts.</p>
    <p>Known limitations: the skill assumes a manageable number of options and criteria (2–5 options, 5–7 weighted criteria). For large-scale procurement with dozens of vendors and hundreds of requirements, specialized procurement tools or RFP scoring systems are more appropriate. The skill does not cover formal supplier qualification or legal compliance frameworks.</p>
  </section>
</article>
