---
layout: default
title: "Stakeholder Analysis Working Skill"
description: "Identify who affects or is affected by a change, what they control, what they need, and how to get reliable information from them."
permalink: /skill-hub/business-analysis/stakeholder-analysis-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/business-analysis/">Business Analysis</a></li>
    <li aria-current="page">Stakeholder Analysis</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Business Analysis</p>
  <h1>Stakeholder Analysis Working Skill</h1>
  <p class="lead">Map who matters, what they control, and how to get reliable information from them — before you waste time interviewing the wrong people.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Every project, incident, or process change involves people who make decisions, people who do the work, and people who suffer when things break. This skill identifies all three groups, verifies their claims to ownership, and plans how to engage each one so that the right information reaches the right person at the right time. The output prevents the common failure mode where critical insights sit with unconsulted users while executives debate scope they do not operate.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A project kickoff meeting ends with no clear list of who to talk to next.</li>
      <li>An incident affects multiple departments and each blames a different root cause.</li>
      <li>A process change crosses organizational boundaries and no one claims end-to-end ownership.</li>
      <li>A data governance initiative needs data owners, but the org chart shows only department heads.</li>
      <li>An integration failure spans multiple systems and each team says "not our problem."</li>
      <li>A requirements document is rejected because "you should have asked [person no one mentioned]."</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP BP replication failure between S/4 and CRM</h3>
    <p>Business partners created in SAP S/4 do not appear in Salesforce. The CRM team says it is an SAP problem. The SAP team says the IDoc was sent. The real stakeholders are: the MDM team (owns BP data model), the integration team (owns the IDoc/PI flow), the sales operations team (suffers from missing customers), and the data steward (approves BP changes). Without mapping all four, the fix addresses only the technical symptom and leaves the governance gap.</p>

    <h3>New credit management rollout</h3>
    <p>A project to implement automated credit checks needs to identify who sets credit limits, who approves exceptions, and who is notified when orders block. The finance director sets policy but does not know the SAP transaction. The credit controller uses the transaction but cannot change configuration. The sales manager wants exceptions but has no authority. The stakeholder map must separate policy authority from operational execution from system configuration.</p>

    <h3>Invoice verification delays in three-way match</h3>
    <p>Invoices sit unposted for weeks. The process spans: procurement (creates PO), warehouse (confirms GR), AP (receives invoice), and a shared service center (posts). Each team has a different system view. The stakeholder map must identify who receives the physical invoice, who enters data, who resolves discrepancies, and who approves payment — because fixing any one step without the others just moves the bottleneck.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Organizational chart or directory showing departments and reporting lines.</li>
      <li>System ownership matrix or RACI chart (if it exists).</li>
      <li>Incident tickets showing which teams were involved in past issues.</li>
      <li>Process documentation or <a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis Notes</a> for the affected workflow.</li>
      <li>Previous project stakeholder lists (if available).</li>
      <li>System user role assignments to verify who has access to which transactions.</li>
      <li>List of known integration points and their technical owners.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Who can confirm this process works as documented, and who can show you the actual screens they use?</li>
      <li>Who loses money, time, or compliance standing when this process or system fails?</li>
      <li>Who has the authority to change this configuration, rule, or workflow?</li>
      <li>Who is consulted today but not informed? Who is informed but not consulted?</li>
      <li>Which stakeholder's absence from the project would guarantee failure?</li>
      <li>Who claims ownership but cannot demonstrate system access or decision authority?</li>
      <li>Who performs the work but is not in any meeting or distribution list?</li>
      <li>Which role is missing from the org chart but essential to the process?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>List all roles that touch the process or system.</strong> Start from the process steps, not from names. For each step, ask: who performs it, who approves it, who is notified, who suffers if it fails.</li>
      <li><strong>Classify by influence and interest.</strong> Use a simple power grid: high influence / high interest (key players), high influence / low interest (keep satisfied), low influence / high interest (ground truth source), low influence / low interest (monitor only).</li>
      <li><strong>Identify the information each stakeholder holds.</strong> Document what they know that no one else knows: passwords, exceptions, workarounds, historical reasons, unwritten rules.</li>
      <li><strong>Map decision authority vs operational involvement.</strong> Separate people who can say yes from people who do the work. A person can be both, but rarely is.</li>
      <li><strong>Verify ownership claims with system evidence.</strong> Check user roles, approval workflows, and configuration change logs. If a stakeholder claims ownership but has no system access, flag as unverified.</li>
      <li><strong>Plan engagement method per stakeholder.</strong> Match the method to the classification: interviews for ground truth, briefings for keep-satisfied, workshops for key players.</li>
      <li><strong>Document in Stakeholder Interview Briefs.</strong> One brief per interview. Include facts confirmed, assumptions surfaced, needs identified, and follow-up actions.</li>
      <li><strong>Validate and update the map.</strong> Stakeholder maps decay. Revalidate after major project milestones or incidents.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a stakeholder claims ownership but cannot show system access or documented authority, ownership is unverified — do not rely on it.</li>
      <li>If two stakeholders claim the same ownership, document the conflict and ask who controls the budget or configuration for that area.</li>
      <li>If a stakeholder is high-influence but low-interest, keep them informed with summaries; do not overload with operational detail.</li>
      <li>If a stakeholder is low-influence but high-interest, they are your best source of ground truth — interview them first.</li>
      <li>If no stakeholder can be found for a critical process step, flag it as a governance gap before proposing any process or system change.</li>
      <li>If stakeholder analysis reveals missing roles that no one is hiring for, add them to the project risk log.</li>
      <li>If a stakeholder was not involved in a past incident but should have been, update the engagement plan to include them going forward.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Stakeholder Map</strong> — Grid or matrix showing each stakeholder's role, influence, interest, information held, and engagement method.</li>
      <li><strong>Stakeholder Interview Brief</strong> — Per-interview record. See template below and <a href="/skill-hub/artifact-templates/">Artifact Templates</a> for full format.</li>
      <li><strong>Ownership Verification Matrix</strong> — Table mapping claimed ownership to system evidence: user roles, approval rights, configuration access.</li>
      <li><strong>Engagement Plan</strong> — Schedule and method for each stakeholder: interview, briefing, workshop, review.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Stakeholder Interview Brief (compact)</h3>
    <pre><code>---
artifact: Stakeholder Interview Brief
id: SIB-001
date: YYYY-MM-DD
interviewer: Name
stakeholder: Name | Role | Area
---

## Context
<!-- Why this interview happened. What project or problem. -->

## Questions asked
<!-- Numbered list of questions from the skill page -->

## Answers given
<!-- What the stakeholder said. Use quotes where precise. -->

## Facts confirmed
<!-- Verifiable statements -->

## Assumptions surfaced
<!-- Things the stakeholder believes but has not verified -->

## Needs identified
<!-- What the stakeholder actually needs, not what they asked for -->

## Pain points
<!-- Specific complaints with context -->

## Constraints
<!-- Budget, time, policy, system limits -->

## Risks mentioned
<!-- What the stakeholder is worried about -->

## Decisions required
<!-- What the stakeholder cannot decide alone -->

## Follow-up actions
<!-- Who does what by when -->

## Related interviews
<!-- Links to other stakeholder briefs -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every critical process step has an identified stakeholder.</li>
      <li>Every stakeholder has a verified contact, role, and area.</li>
      <li>Ownership claims are backed by system access or documented authority.</li>
      <li>No critical stakeholder is missing from the map.</li>
      <li>Engagement methods are tailored to influence/interest classification, not generic.</li>
      <li>Interview briefs separate facts from assumptions.</li>
      <li>The map is dated and has a planned review trigger.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Assuming the org chart equals decision authority.</strong> Consequence: you interview department heads who delegate to unseen operators, missing the people who actually know the workarounds.</li>
      <li><strong>Treating all stakeholders equally.</strong> Consequence: key players are under-engaged while low-influence stakeholders are overloaded with detail they cannot act on.</li>
      <li><strong>Failing to verify ownership claims.</strong> Consequence: decisions are made by people without authority, or authority is assumed by people who only perform the work.</li>
      <li><strong>Not updating the stakeholder map as the project evolves.</strong> Consequence: new blockers appear late because roles changed, people left, or new teams became involved.</li>
      <li><strong>Ignoring stakeholders who are hard to reach.</strong> Consequence: critical information sits with remote teams, external vendors, or part-time users who were never interviewed.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>AI agents should use this skill to identify and map stakeholders before conducting interviews or making recommendations.</p>
    <ul>
      <li><strong>Start with process steps, not names.</strong> For each step, ask who performs it, who approves it, and who suffers when it fails.</li>
      <li><strong>Verify ownership claims</strong> by checking system user roles, approval workflows, or documented authority. Do not accept job titles as proof.</li>
      <li><strong>Classify stakeholders by decision power and operational involvement,</strong> not just by job title or seniority.</li>
      <li><strong>Produce a Stakeholder Interview Brief for each interview.</strong> Separate facts confirmed from assumptions surfaced.</li>
      <li><strong>Flag missing stakeholders as governance gaps.</strong> If a critical step has no owner, state this explicitly and do not proceed as if ownership exists.</li>
      <li><strong>Link to Atlas diagnostics</strong> when stakeholder gaps relate to SAP processes. For example, unclear credit management ownership should reference <a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a>.</li>
      <li><strong>Do not invent stakeholders or contact details.</strong> If a role is missing, flag it. Do not fill gaps with generic placeholders.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Elicitation Working Skill</a></li>
      <li><a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis Working Skill</a></li>
      <li><a href="/skill-hub/sap-ams/change-impact-analysis-working-skill/">Change Impact Analysis Working Skill</a></li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — Diagnostic context for process ownership.</li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a> — Cross-functional ownership in O2C.</li>
      <li><a href="/scenarios/master-data-issues-blocking-sales-orders/">Master Data Issues Blocking Sales Orders</a> — Scenario with multiple stakeholder layers.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of stakeholder analysis practices. It is not official BABOK or IIBA documentation. It focuses on enterprise and SAP contexts where system evidence can verify ownership claims.</p>
    <p>Known limitations: the skill assumes access to organizational charts, system roles, or process documentation. In flat organizations or startups without formal roles, the classification framework may need adaptation. The skill does not cover political stakeholder management or influence strategies beyond information engagement.</p>
  </section>
</article>
