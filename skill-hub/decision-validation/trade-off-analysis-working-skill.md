---
layout: default
title: "Trade-Off Analysis Working Skill"
description: "Compare competing objectives across multiple dimensions so that decisions are made on evidence rather than on the loudest voice in the room."
permalink: /skill-hub/decision-validation/trade-off-analysis-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/decision-validation/">Decision & Validation</a></li>
    <li aria-current="page">Trade-Off Analysis</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Decision & Validation</p>
  <h1>Trade-Off Analysis Working Skill</h1>
  <p class="lead">Compare competing objectives across multiple dimensions so that decisions are made on evidence rather than on the loudest voice in the room.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you make structured decisions when no option is perfect. It forces you to separate what is mandatory from what is preferred, to score options against evidence rather than opinion, and to test whether your decision is robust if priorities shift. The output is a Trade-Off Analysis Note that shows stakeholders exactly why one option was chosen and why the others were rejected — with numbers, not narrative.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A technology choice requires comparing build, buy, and configure options with different cost and risk profiles.</li>
      <li>A scope decision must separate must-have capabilities from nice-to-have features under budget pressure.</li>
      <li>An architecture decision needs to balance implementation speed, operational complexity, and future scalability.</li>
      <li>Resource allocation requires choosing between projects when not all can be funded.</li>
      <li>A vendor selection must compare functionality, cost, support quality, and integration effort.</li>
      <li>A steering committee needs evidence for a go/no-go decision on a major change.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP S/4HANA migration: custom code vs standard vs extension</h3>
    <p>An organization migrating from SAP ECC to S/4HANA must decide whether to keep a custom Z-program for credit checking, adopt the standard S/4 credit management function, or build a side-by-side extension. The trade-off spans clean core compliance (mandatory for maintenance), user experience (the custom screen is familiar), migration effort (the Z-program needs refactoring), and ongoing support cost. Without structured trade-off analysis, the project either carries dead code into the new system or breaks a critical business process by forcing standard functionality before it is ready.</p>

    <h3>Integration architecture: API vs event-driven vs batch</h3>
    <p>A team must choose how to connect a new e-commerce platform to SAP for order-to-cash processing. API-first offers fast implementation and simple debugging. Event-driven offers real-time decoupling and better scalability under peak load. Batch offers lowest cost and simplest operations. The trade-off requires scoring each option against criteria like real-time requirement, peak volume handling, operational monitoring complexity, and team skill availability. Without this analysis, the team defaults to what they know best, which may fail during Black Friday traffic.</p>

    <h3>Master data governance: central MDG vs decentralized ownership</h3>
    <p>A global company must decide whether to centralize master data governance in SAP MDG or allow regional business units to maintain their own data with periodic synchronization. Centralization offers consistency and compliance but creates latency and regional dissatisfaction. Decentralization offers responsiveness but produces duplicates and conflicting tax classifications. The trade-off analysis must score each model against data quality targets, regulatory requirements, regional autonomy needs, and operational cost.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>A precise decision statement: what exactly is being chosen, and by whom.</li>
      <li>A list of viable options (minimum 2, ideally 3–5). Include the "do nothing" option where relevant.</li>
      <li>Decision criteria from stakeholders, separated into must-haves (pass/fail) and weighted factors (scored).</li>
      <li>Evidence for each option against each criterion: costs, capability references, benchmarks, system test results, or vendor documentation.</li>
      <li>Constraints: budget ceiling, compliance mandates, timeline deadlines, skill availability.</li>
      <li>Stakeholder weighting priorities for the scored criteria.</li>
      <li>Historical data or precedent from similar decisions (optional but valuable).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the exact decision we are making, and who has the authority to decide?</li>
      <li>What happens to the business if we make the wrong choice — and how will we know?</li>
      <li>Which criteria are non-negotiable (must-haves), and which are preferred (weighted)?</li>
      <li>Who will live with the consequences of this decision for the next three years?</li>
      <li>What evidence do we have for each option, and what is still unknown?</li>
      <li>If we eliminate the worst option, does the ranking of the remaining options change?</li>
      <li>What would make us change our mind after the decision is made?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Write the decision statement.</strong> One sentence: "We are deciding between X and Y for Z purpose, to be decided by [owner] by [date]."</li>
      <li><strong>List all viable options.</strong> Include the "do nothing" or "delay" option if it is realistic. Describe each option in enough detail that a non-technical reader understands it.</li>
      <li><strong>Define criteria.</strong> Separate must-haves (binary: pass/fail) from weighted criteria (scored 1–5). Limit weighted criteria to 5–7 to avoid dilution.</li>
      <li><strong>Gather evidence.</strong> For each option and each criterion, find facts: vendor quotes, system test results, reference calls, benchmark data, or documented precedent. Do not rely on team opinion.</li>
      <li><strong>Score options against weighted criteria.</strong> Use the same scale for every option. Document the evidence behind each score.</li>
      <li><strong>Apply weights.</strong> Weighted score = raw score × criterion weight. Sum for each option. Ensure weights sum to 1.0.</li>
      <li><strong>Check must-haves.</strong> Eliminate any option that fails a must-have criterion, regardless of its weighted score.</li>
      <li><strong>Analyze sensitivity.</strong> Change each weight by ±20% and re-calculate. Does the winner change? If yes, the decision is fragile.</li>
      <li><strong>Document the rationale.</strong> State the winning option, the margin of victory, the reason the runner-up was rejected, and any key assumptions.</li>
      <li><strong>Present with uncertainty.</strong> State what evidence is weak, what is unknown, and what event would trigger a reconsideration.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If an option fails a must-have criterion, eliminate it regardless of its weighted score.</li>
      <li>If the top two options are within 10% of each other on total weighted score, the decision is not robust — revisit criteria or gather more evidence.</li>
      <li>If evidence for a criterion is missing, score it as "unknown" rather than assuming a neutral score.</li>
      <li>If stakeholders disagree on weights, run sensitivity analysis with both sets before forcing consensus.</li>
      <li>If the cheapest option wins but carries a high risk, flag the risk and the cost of mitigation separately.</li>
      <li>If "do nothing" is not a realistic option, still include it to show the cost of inaction.</li>
      <li>If the same person scores and weights all criteria, have a second reviewer challenge the scores.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Trade-Off Analysis Note</strong> — decision statement, options, criteria, weights, scores, sensitivity analysis, must-have elimination, recommendation with rationale. See template below.</li>
      <li><strong>Criteria and Weights Register</strong> — table of criteria, type (must-have/weighted), weight, source of weight, and stakeholder who proposed it.</li>
      <li><strong>Evidence Log</strong> — supporting facts, references, and data for each score, with source and date.</li>
      <li><strong>Sensitivity Analysis Summary</strong> — table showing winner under different weight scenarios.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Trade-Off Analysis Note</h3>
    <pre><code>---
artifact: Trade-Off Analysis Note
id: TOA-001
date: YYYY-MM-DD
decision: "What is being decided"
authority: "Who decides"
---

## Decision Statement
<!-- One sentence. Example: "We are deciding between API-first, event-driven, and batch integration for e-commerce order-to-cash, to be decided by the Enterprise Architecture Board by 2026-07-15." -->

## Options
<!-- 2–5 options. Include 'do nothing' if relevant. Describe each in 1–2 sentences. -->

### Option 1: [Name]
<!-- Description and key characteristics -->

### Option 2: [Name]
<!-- Description and key characteristics -->

### Option 3: [Name]
<!-- Optional -->

## Must-Have Criteria
<!-- Pass/fail. Any option that fails is eliminated. -->
- [ ] Criterion 1: [Description] — Source: [Who required it]
- [ ] Criterion 2: [Description] — Source: [Who required it]

## Weighted Criteria and Weights
<!-- Weights sum to 1.0 -->
| Criterion | Weight | Source |
|-----------|--------|--------|
| Criterion 1 | 0.30 | Business sponsor |
| Criterion 2 | 0.25 | Operations lead |
| Criterion 3 | 0.20 | Architecture board |
| Criterion 4 | 0.15 | Compliance officer |
| Criterion 5 | 0.10 | Project manager |

## Scoring Matrix
<!-- Scale: 1 = Poor, 3 = Adequate, 5 = Excellent -->
| Criterion | Weight | Option 1 | Option 2 | Option 3 |
|-----------|--------|----------|----------|----------|
| Criterion 1 | 0.30 | 3 (evidence: ...) | 5 (evidence: ...) | 4 (evidence: ...) |
| Criterion 2 | 0.25 | 4 (evidence: ...) | 3 (evidence: ...) | 3 (evidence: ...) |

## Weighted Scores
| Option | Total Score | Margin |
|--------|-------------|--------|
| Option 1 | 3.45 | — |
| Option 2 | 4.20 | +0.75 |
| Option 3 | 3.80 | +0.35 |

## Must-Have Elimination
<!-- List any options eliminated and why -->

## Sensitivity Analysis
<!-- Change weights by ±20%. Does the winner change? -->
- Winner holds if scalability weight drops from 0.30 to 0.18.
- Runner-up overtakes if cost weight rises above 0.40.

## Recommendation
<!-- Winning option, margin, and why the runner-up was rejected -->

## Key Assumptions and Unknowns
<!-- What could change this decision? -->

## Evidence Sources
<!-- Links or references to supporting data -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The decision statement is explicit, narrow, and names the decision authority.</li>
      <li>At least two viable options are compared, including "do nothing" where relevant.</li>
      <li>Criteria clearly distinguish must-haves (pass/fail) from weighted factors (scored).</li>
      <li>Weights are documented, sum to 1.0, and traceable to stakeholder input.</li>
      <li>Every score is backed by evidence with a source, not by team opinion.</li>
      <li>Sensitivity analysis is performed and the decision's robustness is stated.</li>
      <li>Must-have elimination is documented with clear reasons.</li>
      <li>The rationale explains why the winner won and why the runner-up lost.</li>
      <li>Key assumptions and unknowns are stated explicitly.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Treating stakeholder preference as evidence.</strong> Consequence: the analysis confirms existing bias instead of testing it. The loudest voice wins, and the project fails in implementation.</li>
      <li><strong>Using equal weights for all criteria to avoid conflict.</strong> Consequence: trivial criteria drown out critical ones. A decision that looks balanced is actually arbitrary.</li>
      <li><strong>Scoring an option as "average" when evidence is missing.</strong> Consequence: unknown risks are treated as safe. The project discovers the gap only after commitment.</li>
      <li><strong>Skipping sensitivity analysis.</strong> Consequence: the decision breaks the first time a stakeholder challenges the weights. The team has no defense.</li>
      <li><strong>Forgetting to include the "do nothing" option.</strong> Consequence: the cost of inaction is invisible. The project may be solving the wrong problem or missing a simpler alternative.</li>
      <li><strong>Conflating must-haves and weighted criteria.</strong> Consequence: an option that fails a critical requirement wins because it scores high on preferences, creating a compliance or operational failure.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A single paragraph stating: "Option A is recommended because it scores highest in the weighted matrix. The team feels it is the best fit for our needs. Option B was also good but more expensive. We should proceed with Option A."</p>
    <p><strong>Why it is weak:</strong> No evidence is cited. No criteria are listed. No sensitivity analysis is shown. The phrase "team feels" reveals opinion masquerading as analysis. A stakeholder cannot verify or challenge the conclusion.</p>

    <h3>Strong output</h3>
    <p>A Trade-Off Analysis Note with: (1) decision statement — "API-first vs event-driven vs batch for order-to-cash integration, decided by Architecture Board" ; (2) three options described with evidence from vendor documentation and load tests; (3) six criteria — two must-haves (sub-second response under 10,000 orders/hour, SAP-certified integration) and four weighted (scalability 0.30, implementation speed 0.25, operational complexity 0.25, total cost 0.20); (4) weighted scores showing event-driven at 4.20, API-first at 3.85, batch at 2.90; (5) sensitivity analysis showing event-driven still wins if scalability weight drops from 0.30 to 0.18; (6) rationale: "Event-driven wins because it passes both must-haves and scores 12% higher on scalability, which is the primary business concern. API-first was rejected because it fails the real-time must-have under peak load. Batch was eliminated because it fails the sub-second must-have."</p>
    <p><strong>Why it is strong:</strong> Every score has evidence. The decision is robust to weight changes. The rejection of each alternative is explicit and tied to criteria. A stakeholder can verify the logic or challenge a specific score.</p>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><code>You are a trade-off analyst. I will give you a decision statement, a list of options, decision criteria, and evidence. Produce a Trade-Off Analysis Note with: (1) decision statement, (2) options described with evidence, (3) criteria classified as must-have or weighted with weights summing to 1.0, (4) scoring matrix with evidence cited for each score, (5) weighted scores, (6) sensitivity analysis (change weights by ±20%), (7) must-have elimination, (8) recommendation with rationale. Do not use generic language like "best fit" or "optimal solution." Cite evidence for every score. Flag unknowns explicitly as "unknown — evidence missing."</code></p>

    <ul>
      <li><strong>Verify the decision statement is narrow.</strong> "Choose an integration approach" is too broad. "Choose between API-first and event-driven for order-to-cash" is usable.</li>
      <li><strong>Separate must-haves from weighted criteria before scoring.</strong> An option that fails a must-have must be eliminated regardless of its weighted score.</li>
      <li><strong>Never invent evidence.</strong> If data is missing, score the criterion as "unknown" and flag it.</li>
      <li><strong>Always run sensitivity analysis.</strong> A decision that flips when weights change by 20% is not robust.</li>
      <li><strong>Document the rationale for rejecting the runner-up.</strong> A good trade-off note explains why the second-best option lost.</li>
      <li><strong>Do not use generic conclusions.</strong> Instead of "Option A is best," write "Option A wins because it passes all must-haves and scores highest on the two criteria weighted highest by the business sponsor."</li>
      <li><strong>Link to Atlas diagnostics</strong> when the trade-off involves SAP architecture or integration. For example, reference <a href="/atlas/concepts/sap-integration-architecture/">SAP Integration Architecture</a> or <a href="/atlas/concepts/event-driven-architecture/">Event-Driven Architecture</a> for criteria definitions.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/architecture/architecture-decision-record-working-skill/">Architecture Decision Record Working Skill</a></li>
      <li><a href="/skill-hub/decision-validation/option-comparison-matrix-working-skill/">Option Comparison Matrix Working Skill</a></li>
      <li><a href="/skill-hub/decision-validation/evidence-based-recommendation-working-skill/">Evidence-Based Recommendation Writing Working Skill</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/sap-integration-architecture/">SAP Integration Architecture</a> — Criteria and patterns for integration trade-offs.</li>
      <li><a href="/atlas/concepts/event-driven-architecture/">Event-Driven Architecture</a> — One of the common options in integration trade-offs.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of trade-off analysis practices. It is not official BABOK, TOGAF, or SAP documentation. It focuses on practical technology and architecture decisions in enterprise and SAP contexts.</p>
    <p>Known limitations: the skill requires access to evidence and stakeholder input. In environments with poor documentation or shifting requirements, trade-off analysis becomes iterative. The skill does not cover formal multi-criteria decision analysis (MCDA) mathematics or optimization algorithms. It assumes a small number of options and criteria; for large-scale procurement with dozens of vendors, specialized procurement tools are more appropriate.</p>
  </section>
</article>
