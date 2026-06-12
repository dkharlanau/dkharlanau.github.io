---
layout: default
title: "Business Problem to Backlog Working Skill"
description: "Transform a vague business complaint into a structured analysis backlog with priorities, owners, and dependencies that a team can execute."
permalink: /skill-hub/ai-assisted-analysis/business-problem-to-backlog-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/ai-assisted-analysis/">AI-Assisted Analysis</a></li>
    <li aria-current="page">Business Problem to Backlog</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — AI-Assisted Analysis</p>
  <h1>Business Problem to Backlog</h1>
  <p class="lead">Transform a vague business complaint into a structured analysis backlog with priorities, owners, and dependencies that a team can execute.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Business complaints arrive as vague statements: "invoices are always late," "sales orders keep getting blocked," "the integration is unreliable." This skill uses AI to decompose the complaint into a structured analysis backlog: root cause hypotheses, diagnostic tasks, prioritization, ownership, and dependencies. The output is a backlog that can be tracked in Jira, Azure DevOps, or a simple markdown table — and that distinguishes analysis work from implementation work.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A business complaint arrives without clear scope or measurable impact.</li>
      <li>You are starting a diagnostic engagement and need to structure the first weeks of work.</li>
      <li>You need to prioritize a queue of problems and assign them to the right people.</li>
      <li>A project is stuck because the problem statement keeps changing.</li>
      <li>You need to separate "find out why" tasks from "fix it" tasks before committing implementation effort.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>"Invoices are always late"</h3>
    <p>The finance director complains that invoices sit in blocked status for weeks. The real problem could be tolerance misalignment, GR timing gaps, price changes after GR, or interface mapping errors. A weak response is to assign a developer to "fix the invoice process." A strong response is to decompose the complaint into analysis tasks: verify tolerance configuration, audit GR timing patterns, review recent price changes, and inspect EDI field mappings. Only after analysis is complete can the team choose the right implementation.</p>
    <h3>"Sales orders keep getting blocked"</h3>
    <p>The sales operations manager reports repeated order blocks. The backlog must distinguish between a master data audit (are customers missing critical fields?), an incompletion procedure review (are the requirements too strict?), a replication timing analysis (does MDG lag cause partial records?), and a governance change (can we enforce completeness at entry?). Each analysis task has a different owner and a different dependency chain.</p>
    <h3>"The integration is unreliable"</h3>
    <p>The IT manager says the middleware drops messages. The backlog must separate interface monitoring setup (what is not being watched?), error pattern analysis (which errors recur and when?), ownership clarification (who responds when an IDoc fails?), and technical redesign (should we change the protocol?). The first three are analysis tasks. The last one is implementation and must wait until the analysis is complete.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li><strong>Problem statement</strong> — the original complaint, in the stakeholder's words.</li>
      <li><strong>Business impact estimate</strong> — frequency, cost, or operational consequence (even rough).</li>
      <li><strong>Stakeholder list</strong> — who is affected, who has data, who can approve.</li>
      <li><strong>Existing backlog or ticket history</strong> — to see if this problem has been attempted before.</li>
      <li><strong>System documentation</strong> — relevant SAP modules, interfaces, or data sources.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the measurable business impact — tickets per week, hours lost, revenue delayed?</li>
      <li>Which systems are involved, and which transactions or interfaces touch the problem?</li>
      <li>Who owns the data, and who owns the process?</li>
      <li>What has already been tried, and why did it fail or not get implemented?</li>
      <li>Is the problem new, recurring, or increasing in frequency?</li>
      <li>What would "fixed" look like, and can we measure it?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Capture the problem statement.</strong> Record the complaint verbatim. Do not rephrase it into consultant language yet.</li>
      <li><strong>Validate the problem with data.</strong> Check ticket volume, error logs, or process metrics to confirm the problem is real and quantify it.</li>
      <li><strong>Generate root cause hypotheses.</strong> Use AI to suggest plausible root causes, but label them as hypotheses, not conclusions.</li>
      <li><strong>Decompose into analysis tasks.</strong> For each hypothesis, define an analysis task that would confirm or reject it. Each task must have a clear output: "evidence that X is true or false."</li>
      <li><strong>Distinguish analysis from implementation.</strong> If a task says "fix," "build," or "deploy," it is implementation. Rewrite it as analysis: "determine whether fixing X is the right approach."</li>
      <li><strong>Assign ownership.</strong> Every task needs a human owner who can execute it or access the required data. If ownership is unclear, create a separate task to find the owner.</li>
      <li><strong>Map dependencies.</strong> Identify which tasks must be completed before others can start. If a task has no dependencies, it is a candidate for the first sprint.</li>
      <li><strong>Estimate effort.</strong> For analysis tasks, estimate in hours or days, not weeks. Analysis tasks should be short. If an estimate exceeds five days, split the task.</li>
      <li><strong>Prioritize.</strong> Rank tasks by impact of the evidence they produce and by how many downstream tasks they unblock. High-evidence, low-dependency tasks go first.</li>
      <li><strong>Format for tracking.</strong> Convert the backlog into the team's tracking tool (Jira, Azure DevOps, markdown) with tags that distinguish analysis from implementation.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a task requires implementation before analysis is complete, split it: the analysis task comes first, the implementation task is parked.</li>
      <li>If ownership is unclear, create an ownership-finding task before any other work starts.</li>
      <li>If a task has no dependencies, it can be started immediately; queue it for the first iteration.</li>
      <li>If a task depends on multiple other tasks, schedule it after the last dependency finishes.</li>
      <li>If an analysis task estimate exceeds five days, split it into smaller verification steps.</li>
      <li>If a hypothesis is rejected by an analysis task, archive the related implementation tasks and inform the team.</li>
      <li>If the problem statement changes during analysis, stop and re-validate the backlog before continuing.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Analysis Backlog</strong> — structured tasks with type, owner, estimate, and priority.</li>
      <li><strong>Dependency Map</strong> — visual or tabular view of which tasks unblock which.</li>
      <li><strong>Hypothesis Register</strong> — root cause hypotheses with links to the tasks that validate them.</li>
      <li><strong>Implementation Parking Lot</strong> — implementation tasks that must wait until analysis is complete.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Analysis Backlog</h3>
    <pre><code>---
title: Analysis Backlog
problem: [verbatim problem statement]
project: [project name]
backlog_owner: [name]
date: [YYYY-MM-DD]
---

## Hypothesis Register
| # | Hypothesis | Evidence Needed | Validation Task | Status |
|---|------------|-----------------|-----------------|--------|
| 1 | [H1] | [what would confirm or reject] | [task ID] | [Open / In Progress / Rejected / Confirmed] |

## Analysis Backlog
| ID | Task | Type | Owner | Estimate | Dependencies | Priority | Status |
|----|------|------|-------|----------|--------------|----------|--------|
| A-001 | [task] | [Data / Process / Config / Integration] | [owner] | [hours/days] | [none / A-002] | [1-5] | [Open] |

## Implementation Parking Lot
| ID | Task | Blocked By | Tentative Owner |
|----|------|------------|-----------------|
| I-001 | [task] | [A-003, A-004] | [owner] |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>[ ] Every task has a human owner who has been consulted.</li>
      <li>[ ] Analysis tasks and implementation tasks are in separate sections.</li>
      <li>[ ] Every analysis task has a clear output: "evidence that X is true or false."</li>
      <li>[ ] Dependencies are mapped and no task has a circular dependency.</li>
      <li>[ ] Effort estimates are in hours or days, and no analysis task exceeds five days.</li>
      <li>[ ] The problem statement is recorded verbatim and has not been silently rephrased.</li>
      <li>[ ] The backlog can be pasted into a tracking tool without reformatting.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Mixing analysis and implementation tasks in the same backlog. <strong>Consequence:</strong> The team starts building a solution before understanding the problem, resulting in rework or a fix that addresses the wrong root cause.</li>
      <li><strong>Mistake:</strong> Assigning tasks to people who were not consulted. <strong>Consequence:</strong> The assigned owner rejects the task or lacks access to the data needed, causing delays and ownership disputes.</li>
      <li><strong>Mistake:</strong> Skipping validation of the problem statement with data. <strong>Consequence:</strong> The backlog targets a symptom that is not the real problem, and the analysis produces findings that no one cares about.</li>
      <li><strong>Mistake:</strong> Letting AI generate implementation tasks before analysis is complete. <strong>Consequence:</strong> The AI proposes solutions to hypotheses that are later rejected, wasting planning and design effort.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>
    <h3>Weak output — bad AI usage</h3>
    <p>A consultant asks AI to "create a backlog for fixing invoice delays." The AI produces a list of tasks: "Fix tolerance configuration," "Rebuild the EDI interface," "Train AP staff," and "Hire a process owner." The tasks have no owners, no dependencies, and no distinction between analysis and implementation. The team starts on "Rebuild the EDI interface" because it sounds decisive, but the real problem is a tolerance misalignment that could be fixed in a configuration session. Three weeks are wasted on interface redesign before the root cause analysis reveals the truth.</p>
    <h3>Strong output — good AI usage</h3>
    <p>The consultant uses AI to decompose "invoice delays" into hypotheses: tolerance misalignment, GR timing gaps, interface mapping errors, and price changes after GR. The AI then suggests analysis tasks for each hypothesis: "Review OMR6 tolerance settings against actual variance distribution" (2 days, FI lead), "Audit GR posting timestamps for the last 100 blocked invoices" (3 days, MM lead), "Compare EDI segment mappings for quantity and price fields" (2 days, integration lead). The dependency map shows that the tolerance and GR tasks are independent and can run in parallel. The EDI mapping task depends on the tolerance task because if tolerance is the root cause, the interface may not need changes. The backlog is imported into Jira and the first sprint is planned with four analysis tasks and no implementation tasks.</p>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <h3>AI Prompt Pattern</h3>
    <pre><code>Role: You are a backlog decomposition assistant.
Context: I have a business complaint: [problem statement]. I need an analysis backlog, not an implementation plan.
Tasks:
1. Generate 3-5 root cause hypotheses for this complaint.
2. For each hypothesis, define an analysis task that would confirm or reject it.
3. Distinguish analysis tasks from implementation tasks. Remove implementation tasks.
4. Assign owners based on the stakeholder list: [list].
5. Map dependencies between tasks.
6. Estimate effort for each analysis task in hours or days. If a task exceeds 5 days, split it.
7. Prioritize by evidence value and dependency count.
8. Output an Analysis Backlog in the template format provided.
Constraints: Do not propose solutions before analysis. Do not invent owners. If ownership is unclear, flag it as a task to find the owner.</code></pre>
    <h3>Agent dos</h3>
    <ul>
      <li>Ask for the problem statement in the stakeholder's own words before generating the backlog.</li>
      <li>Produce the hypothesis register as a separate artifact.</li>
      <li>Separate analysis tasks from implementation tasks explicitly.</li>
      <li>Map dependencies and flag tasks that have no dependencies as quick starts.</li>
    </ul>
    <h3>Agent don'ts</h3>
    <ul>
      <li>Do not generate implementation tasks before analysis is complete.</li>
      <li>Do not assign tasks to stakeholders without confirming they can execute them.</li>
      <li>Do not skip the data validation step before decomposing the problem.</li>
      <li>Do not present hypotheses as conclusions.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/gap-analysis-working-skill/">Gap Analysis</a> — comparing current state against target state after analysis is complete.</li>
      <li><a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis</a> — mapping how work happens before decomposing problems.</li>
      <li><a href="/skill-hub/sap-ams/root-cause-analysis-working-skill/">Root Cause Analysis</a> — structured method for tracing defects to their origin.</li>
      <li><a href="/skill-hub/business-analysis/stakeholder-analysis-working-skill/">Stakeholder Analysis</a> — identifying who owns the tasks and the data.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — structured frame for cross-process audits that produce backlogs.</li>
      <li><a href="/scenarios/invoice-verification-three-way-match-delays/">Invoice Verification Three-Way Match Delays</a> — example of how a vague complaint decomposes into specific analysis tasks.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of AI-assisted backlog decomposition. It is not an official Agile, Scrum, SAP, or BABOK method. The skill assumes that the problem statement is available and that stakeholders can be identified. If the problem is genuinely unknown or the stakeholders are unavailable, the backlog will contain too many ownership-finding tasks and may not be actionable. AI-generated hypotheses are not guaranteed to be correct; they are starting points for investigation. Use this skill as a structured accelerator, not as a replacement for human judgment and stakeholder consultation.</p>
  </section>
</article>
