---
layout: default
title: "Status Update Writing Working Skill"
description: "Write a project status update that tells the truth about progress, risks, blockers, and next steps without hiding bad news."
permalink: /skill-hub/work-documentation-handover/status-update-writing-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/work-documentation-handover/">Work Documentation and Handover</a></li>
    <li aria-current="page">Status Update Writing</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Work Documentation and Handover</p>
  <h1>Status Update Writing Working Skill</h1>
  <p class="lead">Write a project status update that tells the truth about progress, risks, blockers, and next steps without hiding bad news.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Status updates are the primary mechanism by which stakeholders understand whether a project is healthy, at risk, or in trouble. Most status updates fail because they hide bad news, use vague language, or report activity instead of progress. This skill produces a Status Update Memo: a structured, honest document that states what was accomplished, what is blocked, what has changed, and what will happen next. The output is designed for busy stakeholders who need to make decisions, not for project managers who want to look good. It is the difference between informed governance and pleasant fiction.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A steering committee or project sponsor needs a regular update on project health.</li>
      <li>A project manager needs to communicate a schedule slip, resource shortfall, or scope change without causing panic.</li>
      <li>A team lead needs to report sprint or phase progress to a program management office.</li>
      <li>A customer-facing project requires a formal status report as part of the engagement contract.</li>
      <li>An AI agent is generating a status summary from project data and needs a structure that humans can trust and act on.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP implementation: steering committee needs to know about a delay</h3>
    <p>An S/4HANA implementation project is three weeks behind schedule due to a data migration issue. The project manager writes a status update that says "we are making good progress and working through some data challenges." The steering committee interprets this as green and does not intervene. Two weeks later, the delay is six weeks and the go-live date is threatened. A proper Status Update Memo would have stated: milestone "data migration complete" is three weeks late due to duplicate vendor records in the legacy system. The impact is a six-week go-live delay unless we add two data cleansing resources. The recommended action is to approve the additional resources or accept the delay. The steering committee would have had the information to decide.</p>

    <h3>Integration project: middleware performance is degrading</h3>
    <p>A middleware integration between SAP and a warehouse system is experiencing throughput degradation. The integration team reports "monitoring is in place and we are investigating." The status is vague. The program manager does not know whether the issue is critical or cosmetic. A proper Status Update Memo would have stated: throughput has dropped from 500 messages per minute to 200, which is below the SLA threshold of 300. The root cause is under investigation; leading hypothesis is queue worker saturation. The risk is that order processing will backlog during peak hours. The next step is to add a queue worker by Friday and validate throughput. The program manager knows the severity, the risk, and the action.</p>

    <h3>Support operations: monthly AMS review with the customer</h3>
    <p>An AMS team provides monthly status updates to a customer. The update lists 47 tickets closed, 3 open, and "all SLAs met." The customer is satisfied but does not know that the three open tickets are critical BP replication failures that have been open for two weeks. A proper Status Update Memo would have stated: 47 tickets closed within SLA. Three tickets are open beyond target resolution time. Two are BP replication failures affecting customer master data quality. One is a performance issue in the monthly reconciliation job. The risk is that unresolved master data issues will block sales orders. The recommended action is a focused session on BP replication diagnostics next Tuesday. The customer sees the real risk and can act.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Project plan or backlog showing planned milestones, tasks, and deadlines.</li>
      <li>Actual progress data: completed tasks, tested features, deployed configurations, resolved tickets.</li>
      <li>Issue and risk register showing open items, their severity, and their impact on schedule or quality.</li>
      <li>Change log showing scope changes, requirement changes, or environment changes since the last update.</li>
      <li>Resource status: team capacity, vacancies, vacations, and new additions.</li>
      <li>Budget or cost status if the update includes financial health.</li>
      <li>Stakeholder concerns or questions from the last update that need to be addressed.</li>
      <li>Decision requests: what does the stakeholder need to decide or approve before the next update?</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What milestones were planned since the last update, and which were met, missed, or modified?</li>
      <li>What is the most important bad news that the stakeholders need to know? If you are hiding it, why?</li>
      <li>What is blocked, and what is needed to unblock it? Is it a decision, a resource, or an external deliverable?</li>
      <li>What has changed since the last update? New risks, new assumptions, new dependencies?</li>
      <li>What is the trend? Are we catching up, falling behind, or holding steady?</li>
      <li>What does the stakeholder need to decide or approve before the next update?</li>
      <li>What would happen if the stakeholder did nothing? Is the project self-correcting or does it need intervention?</li>
      <li>What is the one thing that, if fixed, would improve the project health the most?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Gather the inputs.</strong> Collect the project plan, actual progress, issue register, change log, and resource data. Do not rely on memory.</li>
      <li><strong>Compare plan to actual.</strong> For each milestone or task since the last update: state what was planned, what actually happened, and the variance. Use concrete measures: dates, counts, percentages, not feelings.</li>
      <li><strong>Identify the top three issues.</strong> Not ten. Three. For each: describe the issue, its impact on the project, and what is needed to resolve it. Be specific about what the stakeholder must provide.</li>
      <li><strong>Identify the top risks.</strong> What could go wrong next? For each: describe the risk, the likelihood, the impact, and the mitigation plan. If the risk is unmitigated, say so.</li>
      <li><strong>State what has changed.</strong> New scope, new requirements, new team members, new tools, new constraints. If nothing changed, say "No changes since last update."</li>
      <li><strong>State the next steps.</strong> What will the team do before the next update? Include specific actions, owners, and target dates. If the next steps depend on a stakeholder decision, state that dependency.</li>
      <li><strong>Write the decision requests.</strong> If the stakeholder needs to approve, decide, or fund something, state it clearly. Include the options, the recommended option, and the consequence of each.</li>
      <li><strong>Write the Status Update Memo.</strong> Use the template below. Lead with the headline, not the details. The first paragraph should tell the stakeholder whether the project is green, yellow, or red and why.</li>
      <li><strong>Review for honesty.</strong> Read the memo and ask: did I hide anything? Did I use vague language to soften bad news? If yes, rewrite it to be direct.</li>
      <li><strong>Distribute and follow up.</strong> Send the memo to the agreed distribution list. Schedule time to discuss the decision requests and the top risks. Do not let the memo be the end of the conversation.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a milestone is missed, state the miss, the reason, and the new target date. Do not redefine the milestone to make it look met.</li>
      <li>If a risk is unmitigated, state the risk and request mitigation resources. Do not omit it because it is uncomfortable.</li>
      <li>If the project status is red, say red in the first sentence. Do not bury the status in paragraph three.</li>
      <li>If the update is green, provide evidence. Green without evidence is not credible.</li>
      <li>If a decision is needed, provide options and a recommendation. Do not dump the problem on the stakeholder without analysis.</li>
      <li>If the update is overdue, explain why and state when the next update will arrive. Do not promise dates you cannot meet.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Status Update Memo</strong> — Structured project status report with headline, progress, issues, risks, changes, next steps, and decision requests. See template below.</li>
      <li><strong>Appendix: Detailed Progress</strong> — Optional detailed task list, milestone chart, or burn-down for stakeholders who want depth.</li>
      <li><strong>Decision Request Card</strong> — One-page summary of what the stakeholder needs to decide, with options and consequences.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Status Update Memo (compact)</h3>
    <pre><code>---
artifact: Status Update Memo
id: SUM-&lt;project&gt;-&lt;date&gt;
project: &lt;Project name&gt;
period: &lt;Start date&gt; to &lt;End date&gt;
status: green | yellow | red
author: &lt;Name and role&gt;
reviewer: &lt;Name and role&gt
doc_status: draft | reviewed | sent
---

## Headline
&lt;One paragraph stating the overall status, the most important change, and the top risk or blocker. Be direct.&gt;

## Progress vs Plan
| Milestone / Task | Planned | Actual | Variance | Status |
|------------------|---------|--------|----------|--------|
| &lt;Name&gt; | YYYY-MM-DD | YYYY-MM-DD | &lt;+/- days&gt; | &lt;green / yellow / red&gt; |

## Top Issues
| Issue | Impact | Owner | What is Needed | Target Resolution |
|-------|--------|-------|----------------|---------------------|
| &lt;Description&gt; | &lt;Schedule / cost / quality&gt; | &lt;Name&gt; | &lt;Resource / decision / external&gt; | YYYY-MM-DD |

## Top Risks
| Risk | Likelihood | Impact | Mitigation | Status |
|------|------------|--------|------------|--------|
| &lt;Description&gt; | &lt;high / medium / low&gt; | &lt;Schedule / cost / quality&gt; | &lt;Plan&gt; | &lt;active / mitigated / escalated&gt; |

## Changes Since Last Update
- &lt;Scope change, requirement change, team change, environment change, or "No changes"&gt;

## Next Steps
| Action | Owner | Target Date | Dependency |
|--------|-------|-------------|------------|
| &lt;Action&gt; | &lt;Name&gt; | YYYY-MM-DD | &lt;None / decision / external&gt; |

## Decision Requests
| Request | Options | Recommended | Consequence of Not Deciding | Needed By |
|---------|---------|-------------|---------------------------|-----------|
| &lt;What is needed&gt; | &lt;Option A, B&gt; | &lt;Option&gt; | &lt;What happens&gt; | YYYY-MM-DD |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The headline tells the truth in the first paragraph. No burying bad news.</li>
      <li>Progress is measured against the plan, not described in vague terms.</li>
      <li>Issues are ranked by impact, not by frequency. The top three are named.</li>
      <li>Each issue states what is needed to resolve it and who must provide it.</li>
      <li>Risks are forward-looking and include mitigation status.</li>
      <li>Changes are documented, even if the change is "no changes."</li>
      <li>Next steps have owners, dates, and dependencies.</li>
      <li>Decision requests include options, a recommendation, and the consequence of inaction.</li>
      <li>The update is reviewed by the project manager and a peer for honesty before sending.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Writing an activity report instead of a progress report.</strong> Consequence: the stakeholder sees that people are busy but cannot tell whether the project is on track. "The team worked hard on testing" is not a status update.</li>
      <li><strong>Hiding bad news behind vague language.</strong> Consequence: the stakeholder is surprised by a crisis that was visible weeks earlier. "We are working through some challenges" is not honest if the milestone is six weeks late.</li>
      <li><strong>Listing every issue instead of the top three.</strong> Consequence: the stakeholder cannot prioritize. A list of 20 issues is not actionable; it is noise.</li>
      <li><strong>Asking for decisions without providing options.</strong> Consequence: the stakeholder must do the analysis that the project manager should have done. The update becomes a homework assignment.</li>
      <li><strong>Sending the update without following up on decision requests.</strong> Consequence: the stakeholder reads the memo, does nothing, and the project remains blocked. A status update is the start of a conversation, not the end.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A two-page email: "The team has been very busy this sprint. We completed a lot of testing and made progress on the data migration. There are a few challenges with the vendor master data, but we are working on them. The integration team is doing great work on the middleware. Next sprint we will continue testing and start UAT. Please let us know if you have any questions." No status color, no plan comparison, no issue specifics, no risks, no decision requests, no dates. The stakeholder learns nothing useful.</p>
    <p><strong>Why it fails:</strong> The stakeholder cannot tell whether the project is healthy. The bad news is hidden. The challenges are not actionable. The update is indistinguishable from a project that is three months behind schedule.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Status Update Memo
id: SUM-S4-IMPL-2026-06-12
project: S/4HANA Implementation Phase 2
period: 2026-05-29 to 2026-06-12
status: yellow
author: P. Jensen, Project Manager
reviewer: S. Mueller, Program Lead
doc_status: sent
---

## Headline
The project is yellow. Data migration milestone "Vendor Master Clean" is two weeks late due to duplicate records in the legacy system. Without intervention, go-live will slip by four weeks. The integration work is on track. We need a decision on additional data cleansing resources by 2026-06-18.

## Progress vs Plan
| Milestone / Task | Planned | Actual | Variance | Status |
|------------------|---------|--------|----------|--------|
| Vendor Master Clean | 2026-05-30 | 2026-06-13 | +14 days | red |
| PI Mapping Complete | 2026-06-10 | 2026-06-10 | 0 days | green |
| UAT Environment Ready | 2026-06-15 | 2026-06-15 | 0 days | green |
| Credit Check Configuration | 2026-06-12 | 2026-06-14 | +2 days | yellow |

## Top Issues
| Issue | Impact | Owner | What is Needed | Target Resolution |
|-------|--------|-------|----------------|---------------------|
| Duplicate vendor records in legacy system | Go-live delay | M. Chen | Two additional data cleansing resources for 3 weeks | 2026-06-30 |
| Credit check configuration incomplete | UAT delay | S. Mueller | Functional sign-off on rule set | 2026-06-16 |

## Top Risks
| Risk | Likelihood | Impact | Mitigation | Status |
|------|------------|--------|------------|--------|
| Go-live slips by 4 weeks if vendor data not cleaned by June 30 | high | schedule | Add resources + parallel cleansing tracks | active |
| UAT finds critical credit check bugs | medium | quality | Early rule review with finance team | mitigated |
| Basis team unavailable for go-live support | low | schedule | Pre-book basis support for go-live weekend | planned |

## Changes Since Last Update
- Added parallel data cleansing track for vendor and customer master (approved 2026-06-05).
- UAT scope reduced to exclude consignment procurement (approved 2026-06-08).
- No other changes.

## Next Steps
| Action | Owner | Target Date | Dependency |
|--------|-------|-------------|------------|
| Submit resource request for data cleansing | P. Jensen | 2026-06-13 | Steering committee approval |
| Complete credit check rule sign-off | S. Mueller | 2026-06-16 | Finance team availability |
| Start UAT sprint 1 | M. Chen | 2026-06-17 | UAT environment ready |

## Decision Requests
| Request | Options | Recommended | Consequence of Not Deciding | Needed By |
|---------|---------|-------------|---------------------------|-----------|
| Approve 2 additional data cleansing resources | A) Approve 2 resources for 3 weeks; B) Accept 4-week go-live delay | Option A | Go-live slips to September, missing peak season readiness | 2026-06-18 |
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Project status update writer for an enterprise SAP project.</p>
    <p><strong>Context:</strong> You have project data, milestone tracking, issue registers, and risk logs. You need to produce a Status Update Memo that tells the truth and enables stakeholder decisions.</p>
    <p><strong>Task:</strong> Create a structured Status Update Memo using the template below. Lead with the headline. Report progress against plan. Name the top three issues and risks. Request decisions with options.</p>
    <p><strong>Output format:</strong> Structured Status Update Memo in Markdown with tables for progress, issues, risks, next steps, and decision requests.</p>

    <ul>
      <li><strong>Never hide bad news.</strong> State the status color in the first sentence. If the project is red, say red.</li>
      <li><strong>Never use vague progress language.</strong> "Making progress" and "working through challenges" are not status. Use plan vs actual with dates and variances.</li>
      <li><strong>Always name the top three issues and risks.</strong> Not ten. Three. Stakeholders cannot prioritize twenty items.</li>
      <li><strong>Always state what is needed to resolve each issue.</strong> If it is a decision, say so. If it is a resource, name it.</li>
      <li><strong>Always provide options for decision requests.</strong> Include a recommendation and the consequence of inaction.</li>
      <li><strong>Do not report activity.</strong> "The team worked hard on testing" is not progress. "Testing is 80% complete, 3 critical defects remain" is progress.</li>
      <li><strong>Review for honesty before sending.</strong> Ask: did I soften anything? Did I omit a risk? If yes, rewrite.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/work-documentation-handover/decision-summary-writing-working-skill/">Decision Summary Writing Working Skill</a> — Use to document decisions that are made in response to status update requests.</li>
      <li><a href="/skill-hub/work-documentation-handover/meeting-notes-to-action-log-working-skill/">Meeting Notes to Action Log Working Skill</a> — Use to convert steering committee meeting notes into trackable actions.</li>
      <li><a href="/skill-hub/decision-validation/risk-dependency-mapping-working-skill/">Risk-Dependency Mapping Working Skill</a> — Use to map risks and dependencies before reporting them in the status update.</li>
      <li><a href="/skill-hub/work-documentation-handover/handover-note-writing-working-skill/">Handover Note Writing Working Skill</a> — Use to package status history into a handover package.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — Context for process health assessments that may appear in status updates.</li>
      <li><a href="/atlas/concepts/consulting-principles-for-sap/">Consulting Principles for SAP</a> — Principles that shape honest consulting communication.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of project status communication practices. It is not official PMBOK, PRINCE2, or SAP documentation. It focuses on honest, structured status updates for enterprise and SAP projects where stakeholder trust is essential and hidden bad news is expensive.</p>
    <p>Known limitations: the skill does not cover project management methodology, earned value analysis, or portfolio reporting. It produces the status memo, not the underlying project controls. It assumes the project manager has access to accurate progress data. It does not cover customer communication strategies or legal disclosure requirements for publicly traded companies. The templates should be adapted to the organization's reporting standards and governance cadence.</p>
  </section>
</article>
