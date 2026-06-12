---
layout: default
title: "Risk and Dependency Mapping Working Skill"
description: "Identify what could go wrong, what depends on what, and which risks are connected so that mitigation plans address root causes instead of symptoms."
permalink: /skill-hub/decision-validation/risk-dependency-mapping-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/decision-validation/">Decision & Validation</a></li>
    <li aria-current="page">Risk and Dependency Mapping</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Decision & Validation</p>
  <h1>Risk and Dependency Mapping Working Skill</h1>
  <p class="lead">Identify what could go wrong, what depends on what, and which risks are connected so that mitigation plans address root causes instead of symptoms.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you map risks and dependencies together, not as separate lists. A risk register alone tells you what might fail. A dependency map alone tells you what must happen first. Combined, they show which risks trigger other risks, which dependencies create fragility, and where a single mitigation can break a cascade. The output is a Risk and Dependency Map that turns a project plan from a wish list into a robust network with known failure modes and owned mitigations.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A project plan is approved but no one has asked what happens if the data migration fails.</li>
      <li>A change impact assessment identifies risks but does not show which risks are connected.</li>
      <li>An integration rollout depends on firewall changes, security reviews, and vendor patches — and none of the timelines are aligned.</li>
      <li>A steering committee wants to know the top three risks that could kill the project, not a list of 47 minor concerns.</li>
      <li>A post-incident review reveals that the root cause was a cascade: a delay in master data cleansing caused a delay in testing, which caused a go-live delay, which caused a compliance breach.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP S/4 rollout: go-live date cascade</h3>
    <p>A global SAP S/4 rollout has a go-live date of October 1. The plan assumes data migration will finish by August 15. Data migration depends on business unit cleansing, which depends on a data quality tool that depends on a vendor patch scheduled for July 1. The risk map shows that if the vendor patch slips by two weeks, the cleansing slips by four weeks, the migration slips by six weeks, and the go-live is missed. The dependency chain is: vendor patch → data quality tool → cleansing → migration → go-live. Without mapping this chain, the project manager tracks the go-live date as "green" until September, when the cascade is already unstoppable.</p>

    <h3>Integration deployment: new API blocked by firewall and security review</h3>
    <p>A team deploys a new REST API between SAP and a warehouse management system. The API depends on a network firewall rule change, which depends on a security review, which depends on vendor documentation that the vendor has not delivered. The risk map shows three connected risks: vendor documentation delay (probability: high, impact: medium), security review delay (probability: medium, impact: high), and firewall rule delay (probability: low, impact: high). The cascade is: vendor documentation → security review → firewall rule → API deployment. The mitigation is not to push the API team harder; it is to get the vendor documentation early or find an alternative security review path.</p>

    <h3>Master data governance: MDG implementation rejected by business units</h3>
    <p>A central MDG implementation is planned to standardize customer master data. The risk map shows that business unit resistance (probability: medium, impact: high) triggers data quality failures (probability: high, impact: high), which triggers integration errors (probability: high, impact: medium), which triggers downstream billing blocks (probability: high, impact: high). The cascade is: resistance → poor data quality → integration errors → billing blocks → revenue delay. The mitigation at the root is not to fix the integration errors; it is to address business unit ownership concerns before go-live, breaking the cascade at the source.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Project plan or change scope with milestones, deliverables, and owners.</li>
      <li>System landscape diagram showing interfaces, data flows, and dependencies.</li>
      <li>Stakeholder list with roles, decision rights, and known concerns.</li>
      <li>Historical incident data or post-mortem reports for similar changes.</li>
      <li>Change records or release notes showing past delays and their causes.</li>
      <li>Vendor commitments and delivery schedules (if applicable).</li>
      <li>Regulatory or compliance deadlines that cannot be moved.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the trigger for this risk, and when would we first notice it?</li>
      <li>What other risks does this risk activate if it materializes?</li>
      <li>What is the probability of this risk, and what is the business impact if it happens?</li>
      <li>Who owns the mitigation, and who owns the contingency if mitigation fails?</li>
      <li>What is the longest dependency chain in this plan, and what is the weakest link?</li>
      <li>Which risks share a common root cause, and can be mitigated together?</li>
      <li>If this risk happens, what is the first business process that fails?</li>
      <li>What evidence do we have for the probability estimate, or is it a guess?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Identify risks.</strong> For each milestone, deliverable, and interface, ask: what could go wrong? List risks by name, trigger, and affected process.</li>
      <li><strong>Classify risk type.</strong> Label each risk as business (stakeholder, regulatory, market), technical (system, integration, data), or organizational (skill, capacity, governance).</li>
      <li><strong>Identify triggers.</strong> For each risk, state the specific event or condition that would cause it to materialize. Example: "vendor patch delivered after July 15."</li>
      <li><strong>Assess probability and impact.</strong> Use a simple 3×3 grid: probability (low/medium/high) and impact (low/medium/high). Document the evidence behind each rating.</li>
      <li><strong>Map dependencies.</strong> Draw arrows between risks: if Risk A materializes, does it increase the probability or impact of Risk B? If yes, draw a dependency arrow.</li>
      <li><strong>Find cascade effects.</strong> Trace the longest chains of dependent risks. A chain of three or more risks is a cascade that needs upstream mitigation.</li>
      <li><strong>Identify root-cause risks.</strong> Risks with many outgoing arrows are root causes. Risks with many incoming arrows are symptoms. Focus mitigation on root causes.</li>
      <li><strong>Create mitigation plans.</strong> For each root-cause risk, define: mitigation action, owner, deadline, and success criterion. For symptom risks, define contingency actions.</li>
      <li><strong>Assign owners.</strong> Every risk must have a named owner. Every mitigation must have a named owner. If no owner exists, flag a governance gap.</li>
      <li><strong>Monitor and review.</strong> Set review dates tied to project milestones. Update the map when new risks appear, dependencies change, or mitigations succeed or fail.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a risk has no owner, it is not managed — flag a governance gap before proceeding.</li>
      <li>If risks form a cascade of three or more, mitigate the upstream (root-cause) risk first. Treating downstream symptoms is wasteful.</li>
      <li>If probability is high and impact is high, the risk requires active mitigation, not just monitoring.</li>
      <li>If probability is high but impact is low, accept or monitor — do not spend executive attention on it.</li>
      <li>If impact is high but probability is low, prepare a contingency plan but do not allocate full-time resources to prevention.</li>
      <li>If two risks share a common root cause, group them and create one mitigation plan.</li>
      <li>If a mitigation plan has no deadline or success criterion, it is not a plan — it is an intention.</li>
      <li>If a dependency is external (vendor, regulator, partner), assign a higher probability of delay than internal dependencies.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Risk and Dependency Map</strong> — a visual or tabular map showing risks, their types, triggers, probability/impact, and dependency arrows. See template below.</li>
      <li><strong>Risk Register</strong> — consolidated table of all risks with status, owner, mitigation, and contingency.</li>
      <li><strong>Cascade Analysis</strong> — list of the longest dependency chains and the weakest link in each.</li>
      <li><strong>Mitigation Plan</strong> — actions, owners, deadlines, and success criteria for root-cause risks.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Risk and Dependency Map (compact)</h3>
    <pre><code>---
artifact: Risk and Dependency Map
id: RDM-001
date: YYYY-MM-DD
scope: "Project or change being assessed"
---

## Risk Register
| ID | Risk | Type | Trigger | Probability | Impact | Owner | Mitigation | Contingency |
|----|------|------|---------|-------------|--------|-------|------------|-------------|
| R1 | <!-- Description --> | Business/Technical/Org | <!-- Trigger --> | L/M/H | L/M/H | <!-- Name --> | <!-- Action --> | <!-- Action --> |
| R2 | <!-- Description --> | Business/Technical/Org | <!-- Trigger --> | L/M/H | L/M/H | <!-- Name --> | <!-- Action --> | <!-- Action --> |
| R3 | <!-- Description --> | Business/Technical/Org | <!-- Trigger --> | L/M/H | L/M/H | <!-- Name --> | <!-- Action --> | <!-- Action --> |

## Dependency Map
| From | To | Relationship | Evidence |
|------|----|--------------|----------|
| R1 | R2 | If R1 occurs, R2 probability increases | <!-- Why --> |
| R2 | R3 | If R2 occurs, R3 impact increases | <!-- Why --> |

## Cascade Analysis
<!-- Longest chains and weakest links -->

### Chain 1
R1 → R2 → R3 → R4
- Weakest link: <!-- Which risk is most likely to fail first -->
- Root cause mitigation: <!-- Action, owner, deadline -->

## Root-Cause Risk Summary
| Root-Cause Risk | Downstream Risks Affected | Mitigation Action | Owner | Deadline | Success Criterion |
|-----------------|---------------------------|-------------------|-------|----------|-------------------|
| R1 | R2, R3, R4 | <!-- Action --> | <!-- Name --> | YYYY-MM-DD | <!-- Measurable --> |

## Monitoring Schedule
| Review Date | Milestone | What to Check | Owner |
|-------------|-----------|-------------|-------|
| YYYY-MM-DD | <!-- Milestone --> | <!-- Check --> | <!-- Name --> |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every risk has a specific trigger, not a vague fear.</li>
      <li>Every risk is classified as business, technical, or organizational.</li>
      <li>Probability and impact are rated with evidence, not guesswork.</li>
      <li>Dependency arrows exist between risks that are causally connected.</li>
      <li>Cascade chains of three or more risks are identified and documented.</li>
      <li>Root-cause risks are distinguished from symptom risks.</li>
      <li>Every risk has a named owner.</li>
      <li>Every mitigation has a named owner, a deadline, and a success criterion.</li>
      <li>External dependencies are flagged with higher probability of delay.</li>
      <li>The map is reviewed and updated at defined milestones.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Listing risks without mapping dependencies.</strong> Consequence: the team treats each risk in isolation. A mitigation that fixes one risk fails because the root cause is still active, triggering three new risks.</li>
      <li><strong>Treating symptoms as root causes.</strong> Consequence: the team mitigates integration errors when the real problem is business unit resistance to MDG. The errors recur because the root cause is untouched.</li>
      <li><strong>Assigning risk ownership to a role instead of a person.</strong> Consequence: when the risk materializes, no one is accountable. The project manager ends up owning every risk by default.</li>
      <li><strong>Using high probability for every risk to get attention.</strong> Consequence: the risk register becomes noise. Real high-probability risks are drowned out by inflated concerns.</li>
      <li><strong>Creating mitigation plans without deadlines or success criteria.</strong> Consequence: mitigations are never completed. The plan looks good on paper but never executes.</li>
      <li><strong>Ignoring external dependencies.</strong> Consequence: vendor delays, security review queues, and regulatory approvals are treated as internal controllable tasks. The plan slips without warning.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A risk register with 20 rows of vague statements: "Data migration might fail," "Integration could have issues," "Users may resist change," "Vendor might be late." No triggers, no probabilities, no dependencies, no owners. The document is a list of fears, not a management tool.</p>
    <p><strong>Why it is weak:</strong> A project manager cannot act on "might fail." There is no trigger to watch, no probability to prioritize, no dependency to break, and no owner to call. The document is filed and forgotten until the risks materialize — at which point it is too late.</p>

    <h3>Strong output</h3>
    <p>A Risk and Dependency Map with: (1) 12 specific risks with named triggers ("vendor patch delivered after July 15," "business unit cleansing completion rate below 80% by August 1"); (2) classification into business, technical, and organizational; (3) probability and impact rated with evidence ("historical vendor delay rate: 40% over 3 years," "past migration required 3 extra weeks when cleansing was incomplete"); (4) dependency arrows showing R1 → R2 → R3 → R4 cascades; (5) root-cause identification: R1 (vendor patch delay) is the root cause of a chain affecting migration and go-live; (6) mitigation plan for R1 with owner, deadline, and success criterion ("Procurement to escalate to vendor account manager by June 20; success = patch delivered by July 1"); (7) monitoring schedule tied to milestones.</p>
    <p><strong>Why it is strong:</strong> Every risk is actionable. The cascade shows where to intervene. The root-cause mitigation is specific and measurable. The project manager can track triggers and know when to escalate. The document is a living management tool, not a static list.</p>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><code>You are a risk and dependency mapper. I will give you a project plan, system landscape, and stakeholder context. Produce a Risk and Dependency Map with: (1) specific risks with triggers, (2) classification (business/technical/organizational), (3) probability and impact with evidence, (4) dependency arrows between risks, (5) cascade chains of 3+ risks, (6) root-cause vs symptom identification, (7) mitigation plans with owner, deadline, and success criterion, (8) monitoring schedule. Do not use vague language like "might fail" or "could have issues." Every risk must have a specific trigger and a named owner. Flag external dependencies explicitly.</code></p>

    <ul>
      <li><strong>Map dependencies before listing mitigations.</strong> A mitigation that fixes a symptom while leaving the root cause active is wasted effort.</li>
      <li><strong>Always name a person as owner, not a role.</strong> "Project manager" is not an owner. "Maria Chen, PMO" is an owner.</li>
      <li><strong>Never invent probability or impact.</strong> If no evidence exists, state "unknown — requires validation" and flag it.</li>
      <li><strong>Trace the longest cascade chains.</strong> A chain of three or more risks is a project killer that needs upstream mitigation.</li>
      <li><strong>Do not treat all risks as high priority.</strong> Use the probability/impact grid to focus attention on high/high risks.</li>
      <li><strong>Flag external dependencies with higher probability.</strong> Vendor, regulator, and partner delays are more likely than internal delays.</li>
      <li><strong>Link to Atlas diagnostics</strong> when risks involve SAP processes or integration. For example, reference <a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> for process risk identification or <a href="/scenarios/invoice-verification-three-way-match-delays/">Invoice Verification Three-Way Match Delays</a> for cascade examples in P2P.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/sap-ams/change-impact-analysis-working-skill/">Change Impact Analysis Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/stakeholder-analysis-working-skill/">Stakeholder Analysis Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/gap-analysis-working-skill/">Gap Analysis Working Skill</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — Diagnostic context for identifying process risks.</li>
      <li><a href="/scenarios/invoice-verification-three-way-match-delays/">Invoice Verification Three-Way Match Delays</a> — Example of a cascade risk in P2P.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of risk and dependency mapping practices. It is not official PMBOK, ISO 31000, or SAP methodology. It focuses on practical project and change management in enterprise and SAP contexts.</p>
    <p>Known limitations: the skill requires access to project plans, system landscapes, and stakeholder input. In environments with poor documentation or shifting timelines, the map becomes outdated quickly and requires continuous refresh. The skill does not cover formal quantitative risk analysis (Monte Carlo simulation, expected monetary value) or enterprise risk management frameworks. It is designed for operational project use, not board-level risk governance.</p>
  </section>
</article>
