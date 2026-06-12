---
layout: default
title: "Meeting Notes to Action Log Working Skill"
description: "Convert raw meeting notes into a structured action log with owners, deadlines, and dependencies so decisions become executable tasks."
permalink: /skill-hub/work-documentation-handover/meeting-notes-to-action-log-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/work-documentation-handover/">Work Documentation and Handover</a></li>
    <li aria-current="page">Meeting Notes to Action Log</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Work Documentation and Handover</p>
  <h1>Meeting Notes to Action Log Working Skill</h1>
  <p class="lead">Convert raw meeting notes into a structured action log with owners, deadlines, and dependencies so decisions become executable tasks.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Meetings produce decisions, but decisions do not become work until someone is assigned, a deadline is set, and dependencies are understood. This skill converts raw meeting notes into an Action Log: a structured list of tasks that can be tracked, reported, and completed. The output is designed to bridge the gap between conversation and execution. It is different from convert-notes-to-requirements, which produces requirements documents, not task lists. This skill produces actionable tasks with owners and deadlines that can be entered into a project management tool, a ticketing system, or a shared tracker.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A meeting has ended and the team needs to know who is doing what by when.</li>
      <li>Meeting notes are verbose and unstructured, and the project manager needs a clean task list for tracking.</li>
      <li>A steering committee or working group meets regularly and needs consistent action tracking across meetings.</li>
      <li>An AI agent has generated meeting notes and a human needs to verify and convert them into trackable actions.</li>
      <li>A retrospective or review meeting produced observations that must be turned into improvement tasks.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP project: status meeting with scattered actions</h3>
    <p>A weekly SAP project status meeting produces three pages of notes: updates on development, testing delays, and a discussion about a BP replication issue. Buried in the notes are four implicit tasks: the basis team must increase the RFC connection limit, the functional team must re-test the BP relationship scenario, the project manager must schedule a steering committee update, and the integration team must fix a mapping error. Without an action log, two of these tasks are forgotten by the next meeting, the mapping error becomes a production incident, and the steering committee update is missed.</p>

    <h3>Data governance: workshop with decisions but no owners</h3>
    <p>A data governance workshop produces a whiteboard full of decisions: standardize material group codes, clean duplicate vendor records, define a new data quality rule, and implement a governance dashboard. The notes say "we agreed to do this" but do not say who will do it or by when. Without an action log, the workshop energy dissipates. Two weeks later, nothing has happened. The duplicate vendor records continue to block purchase orders.</p>

    <h3>Support operations: incident review meeting</h3>
    <p>An incident review meeting discusses a recent SAP IDoc failure. The notes mention that monitoring is insufficient, error handling is unclear, and the runbook is outdated. The implicit actions are: add a new alert for status 51 IDocs, update the error handling procedure, and revise the runbook. Without an action log, these improvements are discussed but never executed. The same incident type happens again the following month.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Raw meeting notes, transcript, or recording showing what was discussed and decided.</li>
      <li>Attendee list with roles, so actions can be assigned to the right people.</li>
      <li>Project or support tracker context, so action IDs and statuses can be aligned with existing work.</li>
      <li>Previous action log from the last meeting, to carry forward incomplete actions.</li>
      <li>Deadline constraints: sprint end, milestone date, go-live date, or SLA target.</li>
      <li>Decision log or meeting agenda, to separate pre-planned topics from emergent actions.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What was decided in the meeting? Decisions are not actions; actions are what must happen to implement the decision.</li>
      <li>Who said they would do something? If no one volunteered, who is the right owner?</li>
      <li>By when must this be done? If no deadline was mentioned, what is a realistic date?</li>
      <li>What does this action depend on? Does it need another action, a decision, or a resource first?</li>
      <li>Is this action new, or is it a continuation of a previous action? If it is a continuation, link to the previous action ID.</li>
      <li>Is this action a task, a decision, or information? Tasks belong in the action log. Decisions belong in the decision log. Information belongs in the minutes.</li>
      <li>What is the definition of done? How will the owner know the action is complete?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Read the notes and mark potential actions.</strong> Go through the notes and highlight every sentence that implies someone must do something. Use a different color for decisions, questions, and information.</li>
      <li><strong>Separate decisions from actions.</strong> A decision is "we will use SAP PI." The action is "the integration team will create the PI configuration document by Friday." Put decisions in the decision log, not the action log.</li>
      <li><strong>Convert each action into a task statement.</strong> Rewrite each action as a clear, specific task: "Who does what by when." Avoid vague phrasing like "look into" or "consider." Use verbs: write, review, test, deploy, update, confirm.</li>
      <li><strong>Assign an owner.</strong> Name the person who is accountable for completing the task. If the owner is unclear, assign the person who has the authority or skill to do it, and confirm with them. Never leave an action unassigned.</li>
      <li><strong>Set a deadline.</strong> Use the meeting context, sprint dates, or milestone dates to set a realistic deadline. If no deadline is possible, set a review date. Actions without deadlines are wishes, not work.</li>
      <li><strong>Identify dependencies.</strong> For each action, list what must happen before it can start. If an action depends on another action in the same log, link them by ID. Flag blockers explicitly.</li>
      <li><strong>Define done.</strong> State what the output or outcome is. For example: "Definition of done: updated runbook published to the wiki and link shared in the team channel."</li>
      <li><strong>Carry forward incomplete actions.</strong> Compare the new action log with the previous one. Carry forward actions that are still open, updating status and expected completion date.</li>
      <li><strong>Write the Action Log.</strong> Use the template below. Include meeting reference, action ID, task, owner, deadline, dependency, status, and definition of done.</li>
      <li><strong>Distribute and track.</strong> Share the action log with all attendees within 24 hours of the meeting. Enter actions into the project tracker or ticketing system. Review open actions at the start of the next meeting.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If an action has no owner, assign one immediately or escalate to the meeting chair. Do not leave it unassigned.</li>
      <li>If an action has no deadline, set a default deadline based on the meeting cadence. Weekly meetings get one-week deadlines unless otherwise specified.</li>
      <li>If an action is a decision, move it to the decision log. If it is a question, move it to a questions list or parking lot.</li>
      <li>If an action is too large, break it into smaller actions with intermediate milestones. Do not create a single action that spans multiple weeks with no intermediate check.</li>
      <li>If an action repeats across meetings, convert it into a recurring task or a process improvement, not an infinite action log entry.</li>
      <li>If an action depends on an external party, flag the external dependency and set a follow-up date. Do not assume the external party will deliver on time.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Action Log</strong> — Structured task list per meeting, with owners, deadlines, dependencies, and status. See template below.</li>
      <li><strong>Carry-Forward Report</strong> — List of actions from previous meetings that are still open, with updated status and revised dates.</li>
      <li><strong>Decision Log Extract</strong> — Decisions captured during the meeting, separated from the action log for clarity.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Action Log (compact)</h3>
    <pre><code>---
artifact: Action Log
meeting: &lt;Meeting name&gt;
date: YYYY-MM-DD
facilitator: &lt;Name&gt;
scribe: &lt;Name&gt;
status: draft | reviewed | distributed
---

## Carry-Forward Actions (from previous meetings)
| ID | Task | Owner | Deadline | Status | Notes |
|----|------|-------|----------|--------|-------|
| A-2026-001 | &lt;Task&gt; | &lt;Owner&gt; | YYYY-MM-DD | &lt;open | done | blocked&gt; | &lt;Update&gt; |

## New Actions (from this meeting)
| ID | Task | Owner | Deadline | Dependency | Status | Definition of Done |
|----|------|-------|----------|------------|--------|---------------------|
| A-2026-005 | &lt;Specific task&gt; | &lt;Owner&gt; | YYYY-MM-DD | &lt;Dependency or blocker&gt; | open | &lt;Outcome&gt; |
| A-2026-006 | &lt;Specific task&gt; | &lt;Owner&gt; | YYYY-MM-DD | A-2026-005 | open | &lt;Outcome&gt; |

## Decisions Made (for reference, not action log)
| Decision | Implied Action | Action ID |
|----------|---------------|-----------|
| &lt;Decision text&gt; | &lt;Task derived from decision&gt; | A-2026-005 |

## Blockers and Escalations
| Blocker | Affected Actions | Escalation Path | Follow-up Date |
|---------|-----------------|-----------------|----------------|
| &lt;Description&gt; | &lt;Action IDs&gt; | &lt;Who to escalate to&gt; | YYYY-MM-DD |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every action has a specific, verb-led task statement.</li>
      <li>Every action has a named owner who has been notified.</li>
      <li>Every action has a deadline or a review date.</li>
      <li>Dependencies are identified and linked to other actions or external deliverables.</li>
      <li>Decisions are separated from actions and stored in the decision log.</li>
      <li>Incomplete actions from previous meetings are carried forward with updated status.</li>
      <li>Each action has a definition of done that is verifiable.</li>
      <li>The action log is distributed within 24 hours of the meeting.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Recording decisions as actions without converting them into tasks.</strong> Consequence: the action log says "decide to use PI" but no one is tasked with creating the PI configuration. The decision sits idle.</li>
      <li><strong>Using vague task statements like "look into the issue."</strong> Consequence: the owner does not know what to do, and the task is never completed because the definition of done is unclear.</li>
      <li><strong>Leaving actions unassigned.</strong> Consequence: the task is not done. Unassigned actions are orphan tasks that no one owns.</li>
      <li><strong>Setting unrealistic deadlines to please stakeholders.</strong> Consequence: deadlines are missed, trust erodes, and the action log becomes a fiction document.</li>
      <li><strong>Creating mega-actions that span weeks.</strong> Consequence: the action is never completed because it is too large, and progress is invisible. Break it into smaller tasks.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A copy-paste of meeting notes with no structure: "We discussed the BP replication issue. The basis team said they would check the RFC connections. The functional team needs to test the relationship scenario. The PM should update the steering committee. Someone needs to fix the mapping error." No owners, no deadlines, no action IDs, no dependencies, no definition of done. The PM must re-read the notes every week to remember what was supposed to happen.</p>
    <p><strong>Why it fails:</strong> The team cannot track progress. Tasks are forgotten. Dependencies are invisible. The meeting was a waste of time because nothing gets executed.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Action Log
meeting: Weekly SAP Project Status — Sprint 4
date: 2026-06-10
facilitator: P. Jensen
scribe: M. Chen
status: distributed
---

## Carry-Forward Actions
| ID | Task | Owner | Deadline | Status | Notes |
|----|------|-------|----------|--------|-------|
| A-2026-042 | Update BP replication error handling in ZIDOC_ALERT | T. Nguyen | 2026-06-05 | done | Runbook updated and published |
| A-2026-043 | Schedule steering committee update for go-live readiness | P. Jensen | 2026-06-08 | open | Waiting for test completion report |

## New Actions
| ID | Task | Owner | Deadline | Dependency | Status | Definition of Done |
|----|------|-------|----------|------------|--------|---------------------|
| A-2026-050 | Increase RFC connection limit to 20 for BP replication | Basis Team | 2026-06-12 | None | open | SM59 shows 20 connections; test BP sync succeeds |
| A-2026-051 | Re-test BP relationship scenario for customer-vendor pairs | M. Chen | 2026-06-14 | A-2026-050 | open | Test cases pass; no status 51 in SMW01 |
| A-2026-052 | Create PI mapping correction for delivery block field | K. Schmidt | 2026-06-13 | None | open | Mapping updated in PI; test IDoc processes correctly |
| A-2026-053 | Send steering committee update with go-live readiness summary | P. Jensen | 2026-06-15 | A-2026-051 | open | Email sent with attached readiness report |

## Blockers
| Blocker | Affected Actions | Escalation Path | Follow-up Date |
|---------|-----------------|-----------------|----------------|
| Test client 300 is down for patching | A-2026-051 | Basis Lead | 2026-06-11 |
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Meeting action log writer for an enterprise project.</p>
    <p><strong>Context:</strong> You have raw meeting notes, a transcript, or a recording. You need to convert them into a structured Action Log that can be tracked in a project management tool or ticketing system.</p>
    <p><strong>Task:</strong> Extract actions, assign owners, set deadlines, identify dependencies, and define done. Separate decisions from actions. Carry forward incomplete actions from previous meetings.</p>
    <p><strong>Output format:</strong> Structured Action Log in Markdown with tables for carry-forward actions, new actions, decisions, and blockers.</p>

    <ul>
      <li><strong>Never leave an action unassigned.</strong> If the owner is unclear, assign the most likely person and flag for confirmation.</li>
      <li><strong>Always convert decisions into specific tasks.</strong> "Decide to use X" becomes "Create X configuration document by [date]."</li>
      <li><strong>Always set a deadline.</strong> If no deadline is mentioned, use the meeting cadence as a default. Weekly meeting actions get one week.</li>
      <li><strong>Always define done.</strong> The definition of done must be verifiable: a document published, a test passed, an email sent.</li>
      <li><strong>Separate decisions from actions.</strong> Decisions go in the decision log. Actions go in the action log. Do not mix them.</li>
      <li><strong>Carry forward incomplete actions.</strong> Compare with the previous action log. Update status and revised dates.</li>
      <li><strong>Do not invent owners or deadlines.</strong> If uncertain, use "TBD" and flag the action for clarification.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/work-documentation-handover/decision-summary-writing-working-skill/">Decision Summary Writing Working Skill</a> — Use to document decisions that are separated from the action log during conversion.</li>
      <li><a href="/skill-hub/ai-assisted-analysis/convert-notes-to-requirements-working-skill/">Convert Notes to Requirements Working Skill</a> — Use when meeting notes contain requirements that need structured documentation, not task tracking.</li>
      <li><a href="/skill-hub/work-documentation-handover/status-update-writing-working-skill/">Status Update Writing Working Skill</a> — Use to report on the progress of action log items.</li>
      <li><a href="/skill-hub/work-documentation-handover/handover-note-writing-working-skill/">Handover Note Writing Working Skill</a> — Use to package open action log items into a handover package.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — Context for process review meetings that generate action items.</li>
      <li><a href="/atlas/automation/operational-memory-for-sap-ams/">Operational Memory for SAP AMS</a> — Framework for capturing meeting outcomes as operational memory.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of meeting documentation practices. It is not official ITIL, BABOK, or SAP documentation. It focuses on the practical task of converting conversation into trackable work in enterprise and SAP contexts.</p>
    <p>Known limitations: the skill assumes meeting notes exist and are readable. It does not cover facilitation techniques, meeting design, or conflict resolution. It does not integrate with specific project management tools; the output is a Markdown artifact that can be copied into Jira, Azure DevOps, SAP Cloud ALM, or any other tracker. The templates should be adapted to the organization's tracking tool and naming conventions.</p>
  </section>
</article>
