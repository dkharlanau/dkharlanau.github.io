---
layout: default
title: "Lessons Learned Capture Working Skill"
description: "Capture what worked, what failed, and what to change after a project phase or incident so the organization learns instead of repeating."
permalink: /skill-hub/work-documentation-handover/lessons-learned-capture-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/work-documentation-handover/">Work Documentation and Handover</a></li>
    <li aria-current="page">Lessons Learned Capture</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Work Documentation and Handover</p>
  <h1>Lessons Learned Capture Working Skill</h1>
  <p class="lead">Capture what worked, what failed, and what to change after a project phase or incident so the organization learns instead of repeating.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Organizations that do not capture lessons learned pay for the same mistakes repeatedly. This skill produces a Lessons Learned Register: a structured record of insights from a completed project, phase, or incident that identifies what to keep, what to fix, and what to avoid next time. The output is designed for action, not for archiving. Every lesson is paired with a recommended action, an owner, and a deadline. The register is the bridge between retrospective and improvement. Without it, retrospectives become therapy sessions that produce no change.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A project phase or project has ended and the team wants to capture insights before people move to other assignments.</li>
      <li>A significant incident has been resolved and the team wants to prevent recurrence by changing processes, tools, or behavior.</li>
      <li>A recurring problem pattern has been identified and the team needs to document the systemic cause and the fix.</li>
      <li>A team is preparing for a similar project and wants to learn from the previous one.</li>
      <li>An AI agent is analyzing project or incident history to suggest improvements and needs a structured capture format.</li>
      <li>A post-implementation review or audit requires evidence of organizational learning and improvement actions.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP implementation: missed data migration deadline</h3>
    <p>An S/4HANA implementation missed its data migration deadline by four weeks because the data quality assessment was performed too late. The project team holds a retrospective, discusses the issue, and moves on. Six months later, a new project repeats the same mistake. A Lessons Learned Register would have captured: the lesson (data quality assessment must happen before migration design, not during), the evidence (4-week delay, 200 duplicate vendor records found too late), the recommended action (add data quality assessment as a mandatory gate before migration design), the owner (program management office), and the deadline (update project template by next quarter). Without the register, the lesson is forgotten and the pattern repeats.</p>

    <h3>Integration incident: missing monitoring caused cascade failure</h3>
    <p>A middleware queue failure caused a cascade of 500 failed IDocs because the queue depth was not monitored. The team fixes the issue, clears the queue, and closes the incident. The next quarter, a different queue fails for the same reason. A Lessons Learned Register would have captured: the lesson (every middleware queue must have a depth alert), the evidence (500 failed IDocs, 6-hour recovery time), the recommended action (audit all PI queues and add alerts where missing), the owner (integration team lead), and the deadline (complete audit by end of quarter). Without the register, the integration team learns the same lesson twice.</p>

    <h3>Support transition: handover knowledge gap</h3>
    <p>A support consultant rolls off an account without documenting custom Z-transactions. The replacement consultant discovers the missing knowledge when a critical report fails. The issue is resolved, but the team does not capture the systemic lesson. The next roll-off, the same thing happens with a different consultant. A Lessons Learned Register would have captured: the lesson (every custom object must be documented in the handover package before roll-off), the evidence (two roll-offs with knowledge gaps, 4-hour incident recovery), the recommended action (add custom object inventory as a mandatory handover checklist item), the owner (AMS manager), and the deadline (update handover policy by next month). Without the register, the transition process remains vulnerable.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Project or incident records showing what happened, when, and why.</li>
      <li>Team feedback from a retrospective, review, or post-mortem meeting.</li>
      <li>Metrics or data showing the impact: delay, cost, quality, or customer impact.</li>
      <li>Root cause analysis findings if the lesson is derived from an incident.</li>
      <li>Existing process documentation, templates, or checklists that the lesson affects.</li>
      <li>Stakeholder input on what they observed and what they would change.</li>
      <li>Historical lessons learned registers from previous projects or incidents for pattern comparison.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What was supposed to happen, and what actually happened?</li>
      <li>What was the gap between plan and reality? What caused the gap?</li>
      <li>What did we do well that we should keep doing?</li>
      <li>What did we do poorly that we should stop doing?</li>
      <li>What surprised us? What assumption was wrong?</li>
      <li>What is the systemic cause, not just the symptom? Is the lesson about a process, a tool, a skill, or a communication pattern?</li>
      <li>What specific action will prevent this from happening again? Who will do it, and by when?</li>
      <li>Is this lesson applicable to other projects or teams? If so, how do we share it?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Schedule the capture session.</strong> Hold the lessons learned session within two weeks of project completion or incident resolution. Waiting longer causes memory decay and context loss.</li>
      <li><strong>Gather the inputs.</strong> Collect project records, incident timelines, metrics, and feedback. Share them with participants before the session so discussion is evidence-based, not opinion-based.</li>
      <li><strong>Structure the discussion.</strong> Use three categories: keep doing (what worked), stop doing (what failed), and start doing (what was missing). Limit the session to 90 minutes. Focus on systemic causes, not personal blame.</li>
      <li><strong>Capture lessons, not complaints.</strong> A lesson is a causal statement: "Because X happened, Y resulted. In the future, do Z instead." A complaint is "the communication was bad." Convert complaints into lessons by identifying the systemic cause.</li>
      <li><strong>Quantify the impact.</strong> For each lesson, include data: delay in days, cost in hours, incident count, or quality score. Quantified lessons are harder to ignore.</li>
      <li><strong>Define the action.</strong> For each lesson, define a specific, actionable improvement: a process change, a checklist addition, a training requirement, a tool configuration, or a template update. Vague actions like "improve communication" are not actionable.</li>
      <li><strong>Assign an owner and a deadline.</strong> Every action must have an owner who is accountable for implementation and a deadline that is realistic. Actions without owners are orphans. Actions without deadlines are wishes.</li>
      <li><strong>Write the Lessons Learned Register.</strong> Use the template below. Group lessons by category. Include the evidence, the action, the owner, and the deadline.</li>
      <li><strong>Validate and approve.</strong> Review the register with the team and with management. Confirm that the actions are funded and scheduled. If management rejects an action, document the rejection and the rationale.</li>
      <li><strong>Share and integrate.</strong> Share the register with other teams that face similar challenges. Integrate the lessons into project templates, checklists, and training materials. A lesson that stays in the register is wasted.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a lesson is not supported by evidence, label it as a hypothesis, not a confirmed lesson. Require validation before action.</li>
      <li>If the action requires funding or resources, escalate to management in the same session. Do not leave it as an unapproved action.</li>
      <li>If the same lesson appears in multiple registers, elevate it to a program-level or organizational lesson. Do not keep it as a project-level secret.</li>
      <li>If the lesson is about a person, reframe it as a process or skill gap. Lessons learned are not performance reviews.</li>
      <li>If the action is too large for one owner, break it into smaller actions with intermediate milestones.</li>
      <li>If the lesson is not applicable to future work, document it for archival but do not assign an action. Not every observation needs a change.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Lessons Learned Register</strong> — Structured record of insights, evidence, and improvement actions. See template below.</li>
      <li><strong>Improvement Action Plan</strong> — Extract of actions with owners, deadlines, and status for tracking.</li>
      <li><strong>Knowledge Base Update</strong> — Optional integration of lessons into project templates, checklists, or training materials.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Lessons Learned Register (compact)</h3>
    <pre><code>---
artifact: Lessons Learned Register
id: LL-&lt;project or incident&gt;-&lt;date&gt;
source: &lt;Project name or incident ID&gt
capture_date: YYYY-MM-DD
facilitator: &lt;Name&gt
doc_author: &lt;Name&gt
doc_reviewer: &lt;Name&gt
doc_status: draft | reviewed | approved
---

## Context
- Project / Incident: &lt;Name and ID&gt;
- Duration / Period: &lt;Start to end date&gt;
- Scope: &lt;What was covered&gt;
- Outcome: &lt;Success, partial success, failure, or incident resolution&gt;

## Keep Doing
| Lesson | Evidence | Why It Worked | Applicability |
|--------|----------|---------------|---------------|
| &lt;What to keep&gt; | &lt;Data or example&gt; | &lt;Causal explanation&gt; | &lt;Which projects or teams&gt; |

## Stop Doing
| Lesson | Evidence | Impact | Root Cause | Action to Prevent | Owner | Deadline |
|--------|----------|--------|------------|-------------------|-------|----------|
| &lt;What to stop&gt; | &lt;Data or example&gt; | &lt;Delay, cost, quality&gt; | &lt;Why it happened&gt; | &lt;Specific change&gt; | &lt;Name&gt; | YYYY-MM-DD |

## Start Doing
| Lesson | Evidence | Gap | Action | Owner | Deadline | Dependency |
|--------|----------|-----|--------|-------|----------|------------|
| &lt;What to start&gt; | &lt;Data or example&gt; | &lt;What was missing&gt; | &lt;Specific change&gt; | &lt;Name&gt; | YYYY-MM-DD | &lt;Resource or approval&gt; |

## Rejected or Deferred Actions
| Action | Reason for Rejection | Decision Maker | Date |
|--------|---------------------|----------------|------|
| &lt;Action&gt; | &lt;Why not approved&gt; | &lt;Name&gt; | YYYY-MM-DD |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every lesson is a causal statement with evidence, not an opinion or a complaint.</li>
      <li>Every lesson in "Stop Doing" and "Start Doing" has a specific, actionable improvement attached.</li>
      <li>Every action has an owner who has agreed to be accountable.</li>
      <li>Every action has a deadline that is realistic and tracked.</li>
      <li>Lessons are quantified where possible: delay, cost, incident count, or quality metric.</li>
      <li>The register was reviewed and approved by the team and management.</li>
      <li>Applicable lessons are shared with other teams or integrated into templates and checklists.</li>
      <li>Rejected or deferred actions are documented with the reason, so they do not resurface unresolved.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Capturing complaints instead of lessons.</strong> Consequence: the register is a venting document with no actionable output. "Communication was bad" is a complaint. "Daily stand-ups were skipped during the integration phase, causing handoff errors" is a lesson.</li>
      <li><strong>Writing vague actions like "improve testing."</strong> Consequence: no one knows what to do, and the action is never completed. Actions must be specific: "Add regression test for BP replication to the sprint 0 checklist."</li>
      <li><strong>Assigning actions without confirming ownership.</strong> Consequence: the action is orphaned. The owner must agree and be resourced.</li>
      <li><strong>Keeping the register in a project folder and never sharing it.</strong> Consequence: the next project team never sees it and repeats the same mistakes. The register must be integrated into organizational knowledge.</li>
      <li><strong>Blaming individuals instead of analyzing systems.</strong> Consequence: the team becomes defensive, honest discussion stops, and the real systemic causes are never identified. Lessons learned are not performance reviews.</li>
      <li><strong>Waiting too long to capture lessons.</strong> Consequence: memory fades, details are lost, and the register becomes superficial. Capture within two weeks of completion.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A retrospective meeting produces a whiteboard photo with these notes: "Good: teamwork. Bad: communication. Improve: testing. Action items: TBD." No evidence, no causal explanation, no specific actions, no owners, no deadlines. The photo is saved to a shared folder and never opened again. The next project repeats the same issues.</p>
    <p><strong>Why it fails:</strong> The output is not actionable. It is not evidence-based. It is not tracked. It is not shared. It is a feel-good exercise that produces no change.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Lessons Learned Register
id: LL-S4-IMPL-2026-001
source: S/4HANA Implementation Phase 2
capture_date: 2026-06-10
facilitator: P. Jensen
doc_author: M. Chen
doc_reviewer: S. Mueller
doc_status: approved
---

## Context
- Project / Incident: S/4HANA Implementation Phase 2 — Customer-Vendor Replication and Order-to-Cash
- Duration / Period: 2026-01-15 to 2026-06-05
- Scope: BP replication, credit management, delivery processing, billing integration
- Outcome: Partial success — go-live delayed by 4 weeks due to data migration issues; integration and billing completed on time.

## Keep Doing
| Lesson | Evidence | Why It Worked | Applicability |
|--------|----------|---------------|---------------|
| Weekly PI mapping review with the integration team | Zero mapping errors in production | Early detection of field mismatches before go-live | All integration projects |
| Daily stand-ups during the go-live preparation | 12 issues resolved in 5 days | Rapid identification and assignment of blockers | All go-live phases |

## Stop Doing
| Lesson | Evidence | Impact | Root Cause | Action to Prevent | Owner | Deadline |
|--------|----------|--------|------------|-------------------|-------|----------|
| Data quality assessment during migration design instead of before | 4-week delay, 200 duplicate vendor records | Schedule slip, resource overallocation | Data quality was not a project gate | Add data quality assessment as mandatory gate before migration design | Program Management Office | 2026-07-15 |
| Custom Z-report deployment without regression testing | ZCUST_REP failed in production with missing field | 6-hour incident, manual reconciliation | No regression test for custom reports | Add Z-object regression test to release checklist | Development Lead | 2026-07-01 |

## Start Doing
| Lesson | Evidence | Gap | Action | Owner | Deadline | Dependency |
|--------|----------|-----|--------|-------|----------|------------|
| Handover package review before consultant roll-off | Knowledge gap caused 4-hour incident on replacement's first week | No mandatory handover checklist | Add custom object inventory and open item list to handover checklist | AMS Manager | 2026-07-01 | HR policy update |
| Queue depth monitoring for all middleware interfaces | 500 failed IDocs due to unmonitored queue | Missing alert on queue depth | Audit all PI queues and add alerts where missing | Integration Team Lead | 2026-06-30 | Monitoring team capacity |

## Rejected or Deferred Actions
| Action | Reason for Rejection | Decision Maker | Date |
|--------|---------------------|----------------|------|
| Hire dedicated data quality team | Budget not approved for this fiscal year | CFO | 2026-06-08 |
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Lessons learned capture writer for enterprise and SAP projects.</p>
    <p><strong>Context:</strong> You have project records, incident timelines, retrospective notes, and metrics. You need to produce a Lessons Learned Register that turns experience into organizational improvement.</p>
    <p><strong>Task:</strong> Create a structured Lessons Learned Register using the template below. Categorize lessons into keep, stop, and start. Attach specific actions with owners and deadlines.</p>
    <p><strong>Output format:</strong> Structured Lessons Learned Register in Markdown with tables for keep, stop, and start categories.</p>

    <ul>
      <li><strong>Never capture complaints without converting them to lessons.</strong> "Communication was bad" is not a lesson. "Daily stand-ups were skipped during the integration phase, causing handoff errors" is a lesson.</li>
      <li><strong>Always quantify the impact.</strong> Use delay, cost, incident count, or quality metrics. Quantified lessons are harder to ignore.</li>
      <li><strong>Always define a specific action for every stop and start lesson.</strong> Vague actions like "improve testing" are not actionable. Use: "Add regression test for X to the sprint 0 checklist."</li>
      <li><strong>Always assign an owner and a deadline.</strong> The owner must agree. The deadline must be tracked. Orphan actions are wasted.</li>
      <li><strong>Always validate with the team and management.</strong> Confirm that actions are funded and scheduled. Document rejected actions with reasons.</li>
      <li><strong>Do not blame individuals.</strong> Reframe person-focused observations as process or skill gaps. Lessons learned are not performance reviews.</li>
      <li><strong>Share applicable lessons with other teams.</strong> A lesson that stays in one project folder is wasted. Integrate it into templates, checklists, and training.</li>
      <li><strong>Link to Atlas diagnostics</strong> when lessons touch documented SAP failure modes. For example, lessons about BP replication should reference <a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/work-documentation-handover/incident-documentation-working-skill/">Incident Documentation Working Skill</a> — Use to document the incident that the lesson is derived from.</li>
      <li><a href="/skill-hub/work-documentation-handover/handover-note-writing-working-skill/">Handover Note Writing Working Skill</a> — Use to package lessons learned into a handover package for the next team.</li>
      <li><a href="/skill-hub/sap-ams/recurring-ticket-pattern-analysis-working-skill/">Recurring Ticket Pattern Analysis Working Skill</a> — Use to identify patterns that generate lessons learned.</li>
      <li><a href="/skill-hub/decision-validation/evidence-based-recommendation-working-skill/">Evidence-Based Recommendation Working Skill</a> — Use to build recommendations for improvement actions based on evidence.</li>
      <li><a href="/skill-hub/work-documentation-handover/status-update-writing-working-skill/">Status Update Writing Working Skill</a> — Use to communicate lessons and improvement actions to stakeholders.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a> — Diagnostic context for BP replication lessons.</li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — Diagnostic context for integration lessons.</li>
      <li><a href="/atlas/automation/operational-memory-for-sap-ams/">Operational Memory for SAP AMS</a> — Framework for capturing and retaining operational lessons.</li>
      <li><a href="/atlas/concepts/consulting-principles-for-sap/">Consulting Principles for SAP</a> — Principles that shape how consultants learn and improve.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of lessons learned and retrospective practices. It is not official AAR (After Action Review), PMBOK, or SAP documentation. It focuses on converting experience into actionable improvement in enterprise and SAP environments where projects are complex, teams rotate, and knowledge retention is a challenge.</p>
    <p>Known limitations: the skill does not cover retrospective facilitation, team dynamics, or conflict resolution during lessons learned sessions. It assumes the session has already occurred and the task is to document and track the outcomes. It does not replace formal organizational change management or process improvement methodologies like Kaizen or Six Sigma, though it can feed into them. The templates should be adapted to the organization's project management office standards and improvement tracking tools.</p>
  </section>
</article>
