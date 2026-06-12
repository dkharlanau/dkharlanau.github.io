---
layout: default
title: "Priority Triage Working Skill"
description: "Compare tasks by impact, urgency, and effort to decide what to do now, what to do next, and what to decline or defer so capacity is allocated to the highest-value work."
permalink: /skill-hub/productivity-execution-control/priority-triage-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/productivity-execution-control/">Productivity and Execution Control</a></li>
    <li aria-current="page">Priority Triage</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Productivity and Execution Control</p>
  <h1>Priority Triage Working Skill</h1>
  <p class="lead">Compare tasks by business impact, urgency, and effort to produce a defensible priority decision that tells the team what to do now, what to do next, and what to decline or defer.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Every team has more work than capacity. The default behavior is to work on whatever arrived last, whatever is loudest, or whatever feels easiest. This skill replaces that chaos with a structured comparison. The output is a Priority Triage Result: a ranked list of tasks with a decision for each — do now, do next, schedule, delegate, or decline. Each decision is justified by impact, urgency, and effort scores. The result gives the team a shared rationale for what is being worked on and what is not. It protects high-value work from being crowded out by low-value noise.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>Monday morning and the inbox contains 20 tasks that all claim to be urgent.</li>
      <li>A project has slipped and the team must decide which features to keep and which to cut.</li>
      <li>An incident has created a queue of follow-up tasks and no one knows which to fix first.</li>
      <li>A stakeholder demands immediate attention for a low-impact request while a high-impact deadline looms.</li>
      <li>A team is planning a sprint or phase and needs to sequence work packages by value.</li>
      <li>An AI agent is being asked to plan a schedule and must justify the sequence with evidence.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>AMS support queue: three critical tickets, one analyst</h3>
    <p>On Monday morning, the support queue shows three tickets marked critical: (1) a credit block preventing a 2M EUR shipment, (2) a report timeout that delays month-end closing, and (3) a user lockout that stops one purchaser from creating orders. The analyst has four hours before a planned system maintenance window. Without triage, the analyst picks the user lockout because it is easiest. With triage, the credit block scores highest on impact (revenue at risk) and urgency (shipment today). The report timeout is next. The user lockout is deferred because the impact is one user and the workaround is to use a colleague's account. The triage result is defensible to the service manager and the business.</p>

    <h3>Sprint planning: feature overload</h3>
    <p>A two-week sprint has 12 story points of capacity and 24 story points of requested work. The product owner wants everything. The triage process scores each story by impact (revenue, user adoption, compliance risk), urgency (deadline, dependency), and effort (points, complexity). The result: four stories are approved for the sprint, three are moved to the next sprint, and five are declined or moved to the backlog with a note that they do not meet the impact threshold. The team has a clear scope and a clear rationale for what is excluded.</p>

    <h3>Post-incident cleanup: ten follow-up actions, no owner</h3>
    <p>After a weekend integration failure, the incident review produces ten follow-up actions: fix the retry logic, update monitoring thresholds, add an alert, document the error pattern, review the API contract, inform the business team, check data consistency, reprocess failed IDocs, update the runbook, and schedule a post-mortem. The team has one day of cleanup capacity. Triage scores each action by impact (prevents recurrence, reduces detection time, fixes data) and effort (hours). The result: fix retry logic and reprocess IDocs are done now (high impact, moderate effort). Update monitoring and add alert are done next (prevents recurrence, low effort). The remaining six are scheduled across the next two weeks. The team does not waste capacity on documentation while the failure mechanism is still broken.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Task list with descriptions, requesters, and any stated deadlines or priorities.</li>
      <li>Capacity estimate: available hours, team size, or story points for the period.</li>
      <li>Business impact context: revenue at risk, compliance deadlines, customer commitments, operational dependencies.</li>
      <li>Effort estimates for each task, or a rough sizing (small, medium, large).</li>
      <li>Dependency map showing which tasks block others and which are blocked.</li>
      <li>Stakeholder preferences or mandates that must be respected even if they score lower.</li>
      <li>Historical data on how long similar tasks took and what the consequences were of delay (optional).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the business consequence if this task is not done today? This week? This month?</li>
      <li>How many users, customers, or processes are affected?</li>
      <li>Is there a hard deadline, or is the urgency artificial?</li>
      <li>What is the effort required, and is it proportional to the impact?</li>
      <li>Does this task block other work, or is it blocked by other work?</li>
      <li>Can this task be delegated, automated, or eliminated?</li>
      <li>What is the cost of switching context if we start this task now and stop something else?</li>
      <li>Has this task been triaged before, and if so, why was it deferred?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Collect all tasks.</strong> Gather every task that is competing for attention. Include the vague ones. Do not filter yet. If a task is missing, the triage is incomplete.</li>
      <li><strong>Score impact.</strong> For each task, rate impact on a 1–5 scale: 1 = no measurable effect, 5 = business-critical (revenue, compliance, customer commitment at risk). Write a one-sentence justification for the score.</li>
      <li><strong>Score urgency.</strong> For each task, rate urgency on a 1–5 scale: 1 = no deadline, 5 = immediate consequence if not done today. Write a one-sentence justification. If the urgency is artificial (someone is shouting), note it.</li>
      <li><strong>Score effort.</strong> For each task, estimate effort in hours or story points. If precise estimates are unavailable, use T-shirt sizing: S (≤4 hours), M (4–16 hours), L (16–40 hours), XL (>40 hours). Convert to a numeric score: S=1, M=2, L=3, XL=4.</li>
      <li><strong>Calculate priority score.</strong> Use the formula: Priority Score = (Impact × Urgency) ÷ Effort. This rewards high-impact, high-urgency, low-effort tasks and penalizes low-impact, low-urgency, high-effort tasks. Round to one decimal place.</li>
      <li><strong>Rank by priority score.</strong> Sort the task list from highest to lowest score. Ties are broken by impact first, then urgency.</li>
      <li><strong>Apply capacity filter.</strong> Starting from the top of the ranked list, add tasks to the "do now" list until capacity is filled. Be honest about capacity. If a task is larger than remaining capacity, move it to "do next" unless it is critical and must displace something else.</li>
      <li><strong>Apply dependency filter.</strong> Check that no task in "do now" is blocked by a task in "do next" or "decline." If so, move the blocking task up or the blocked task down.</li>
      <li><strong>Apply mandate filter.</strong> If a stakeholder mandates a task regardless of score, include it but flag it as a mandate override. Document the override reason.</li>
      <li><strong>Decide on each remaining task.</strong> For tasks below the capacity line: do next (schedule for next period), delegate (give to another team or person), or decline (inform the requester that the task will not be done and why).</li>
      <li><strong>Document the triage result.</strong> Use the template below. Include task name, scores, decision, rationale, and any overrides.</li>
      <li><strong>Communicate the result.</strong> Share the triage result with the team and stakeholders. For declined tasks, send a brief message explaining the decision and inviting the requester to re-submit with new impact or urgency evidence.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If impact is 1 and urgency is 1, decline the task unless it is a mandate.</li>
      <li>If effort is XL and impact is less than 4, defer the task to a dedicated planning session rather than starting it in routine capacity.</li>
      <li>If two tasks have the same priority score, the one with higher impact wins. If impact is equal, the one with higher urgency wins.</li>
      <li>If a task is blocked by another task, the blocking task must be in the same or earlier period as the blocked task.</li>
      <li>If a stakeholder mandates a task regardless of score, include it but flag the override and document the reason.</li>
      <li>If a task has been deferred more than twice, require the requester to re-justify impact and urgency before it is triaged again.</li>
      <li>If a task is urgent but low-impact, consider whether it can be delegated or automated rather than consuming core team capacity.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Priority Triage Result</strong> — Ranked task list with impact, urgency, effort scores, priority score, decision, and rationale. See template below.</li>
      <li><strong>Capacity Allocation Map</strong> — Visual or tabular summary showing how available capacity is distributed across do-now, do-next, delegate, and decline categories.</li>
      <li><strong>Decline Communication</strong> — Brief message to requesters of declined tasks, explaining the decision and inviting re-submission with new evidence.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Priority Triage Result (compact)</h3>
    <pre><code>---
artifact: Priority Triage Result
period: &lt;sprint, week, or phase&gt;
capacity: &lt;hours or points available&gt
date: YYYY-MM-DD
status: draft | confirmed
---

## Scoring key
- Impact: 1 (none) to 5 (business-critical)
- Urgency: 1 (no deadline) to 5 (immediate consequence)
- Effort: S=1, M=2, L=3, XL=4
- Priority Score = (Impact × Urgency) ÷ Effort

## Triage table
| Rank | Task | Impact | Urgency | Effort | Score | Decision | Rationale |
|------|------|--------|---------|--------|-------|----------|-----------|
| 1 | &lt;Task name&gt; | 5 | 4 | M | 10.0 | do now | &lt;one sentence&gt; |
| 2 | &lt;Task name&gt; | 4 | 5 | L | 6.7 | do now | &lt;one sentence&gt; |
| 3 | &lt;Task name&gt; | 3 | 3 | S | 9.0 | do next | &lt;one sentence&gt; |
| 4 | &lt;Task name&gt; | 2 | 2 | M | 2.0 | decline | &lt;one sentence&gt; |

## Override log
| Task | Override | Reason | Approved by |
|------|----------|--------|-------------|
| &lt;Task name&gt; | mandate | &lt;reason&gt; | &lt;name&gt; |

## Decline communications
- &lt;Task name&gt;: Message sent to &lt;requester&gt; on YYYY-MM-DD explaining &lt;reason&gt;.
</code></pre>

    <h3>Capacity Allocation Map (compact)</h3>
    <pre><code>| Category | Hours / Points | Tasks | % of capacity |
|----------|--------------|-------|---------------|
| do now | 16 | 3 | 64% |
| do next | 6 | 2 | 24% |
| delegate | 2 | 1 | 8% |
| decline | 0 | 2 | 0% |
| buffer | 1 | — | 4% |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every task in the queue is scored for impact, urgency, and effort.</li>
      <li>Each score has a one-sentence justification, not just a number.</li>
      <li>Priority scores are calculated consistently using the same formula for all tasks.</li>
      <li>The ranked list fits within the stated capacity, with a small buffer for unexpected work.</li>
      <li>No task in "do now" is blocked by a task in a later category.</li>
      <li>Any mandate overrides are documented with a reason and approver.</li>
      <li>Declined tasks have a communication sent to the requester with an explanation.</li>
      <li>The triage result is shared with the team before work starts.</li>
      <li>Tasks deferred more than twice are re-justified before being triaged again.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Treating all incoming tasks as equally important.</strong> Consequence: capacity is consumed by low-impact work while high-impact work waits. The team is busy but not effective.</li>
      <li><strong>Ignoring effort and only scoring impact and urgency.</strong> Consequence: a massive, low-probability project scores higher than a quick, high-value fix. The team spends weeks on something that could have been done in hours.</li>
      <li><strong>Letting the loudest stakeholder override the triage without documentation.</strong> Consequence: the triage process loses credibility. The team learns that shouting works, and the volume of urgent-but-unimportant requests increases.</li>
      <li><strong>Not communicating declines.</strong> Consequence: the requester assumes the task is in progress, plans around it, and is surprised when it never happens. Trust erodes.</li>
      <li><strong>Running triage once and never updating it.</strong> Consequence: new urgent tasks are appended to the end of the list, and the original ranking becomes obsolete within days. The team reverts to reactive behavior.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A mental note: "I'll do the credit block first, then the report, then whatever else I have time for." No scores, no rationale, no capacity check, no communication to stakeholders. The analyst works until tired, then stops. Some tasks are forgotten. The team cannot explain why one task was chosen over another when challenged.</p>
    <p><strong>Why it fails:</strong> The decision is invisible and unaccountable. When a stakeholder asks why their task was not done, there is no evidence. When the analyst is overloaded, they cannot show what displaced their work. The process is indistinguishable from personal preference.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Priority Triage Result
period: Week 2026-W24
capacity: 20 hours
date: 2026-06-12
status: confirmed
---

## Scoring key
- Impact: 1 (none) to 5 (business-critical)
- Urgency: 1 (no deadline) to 5 (immediate consequence)
- Effort: S=1, M=2, L=3, XL=4
- Priority Score = (Impact × Urgency) ÷ Effort

## Triage table
| Rank | Task | Impact | Urgency | Effort | Score | Decision | Rationale |
|------|------|--------|---------|--------|-------|----------|-----------|
| 1 | Unblock credit hold for customer C-50001 | 5 | 5 | M | 12.5 | do now | 2M EUR shipment blocked; must release today. |
| 2 | Fix month-end report timeout (ZREPORT) | 4 | 4 | M | 8.0 | do now | Closing delayed 2 days; affects 3 company codes. |
| 3 | Add monitoring alert for IDoc queue depth | 3 | 3 | S | 9.0 | do next | Prevents weekend recurrence; low effort. |
| 4 | Update API contract documentation | 2 | 2 | M | 2.0 | decline | No consumer waiting; defer to next sprint. |
| 5 | User lockout for purchaser P-120 | 2 | 3 | S | 6.0 | delegate | Workaround exists; assign to L1 support. |

## Override log
| Task | Override | Reason | Approved by |
|------|----------|--------|-------------|
| — | — | — | — |

## Decline communications
- Update API contract documentation: Message sent to integration lead on 2026-06-12 explaining deferral to next sprint. Re-submission welcome with consumer deadline evidence.
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Priority triage analyst for an enterprise delivery team.</p>
    <p><strong>Context:</strong> You have a list of tasks competing for limited capacity. You need to produce a Priority Triage Result that the team can use to decide what to do now, what to do next, and what to decline.</p>
    <p><strong>Task:</strong> Score each task for impact, urgency, and effort. Calculate a priority score. Rank the tasks. Apply capacity, dependency, and mandate filters. Produce a triage table with decisions and rationale.</p>
    <p><strong>Output format:</strong> Structured Priority Triage Result per the template, followed by a capacity allocation map and decline communications.</p>

    <ul>
      <li><strong>Never skip scoring for any task in the queue.</strong> If a task is missing information, score it conservatively and flag the gap.</li>
      <li><strong>Always justify scores with one sentence.</strong> A number without rationale is not defensible.</li>
      <li><strong>Use the same formula for every task.</strong> Do not change the scoring method to favor a particular outcome.</li>
      <li><strong>Respect capacity limits honestly.</strong> Do not squeeze more work into a period than the team can execute.</li>
      <li><strong>Check dependencies before finalizing the ranking.</strong> A blocked task in "do now" with its blocker in "decline" is a logical error.</li>
      <li><strong>Document mandate overrides explicitly.</strong> If a stakeholder overrides the score, record the task, the reason, and the approver.</li>
      <li><strong>Send decline communications to requesters.</strong> Do not silently drop tasks. Explain the decision and invite re-submission with new evidence.</li>
      <li><strong>Do not invent impact or urgency.</strong> If the business context is missing, state that the score is provisional and ask for clarification.</li>
      <li><strong>Link to Atlas diagnostics</strong> when tasks involve SAP incidents. For example, credit block tasks should reference <a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/productivity-execution-control/task-clarification-working-skill/">Task Clarification Working Skill</a> — Use to clarify tasks before scoring them for triage.</li>
      <li><a href="/skill-hub/productivity-execution-control/daily-execution-review-working-skill/">Daily Execution Review Working Skill</a> — Use to review and refresh the triage result daily.</li>
      <li><a href="/skill-hub/productivity-execution-control/blocker-escalation-working-skill/">Blocker Escalation Working Skill</a> — Use when a high-priority task is blocked and must be escalated.</li>
      <li><a href="/skill-hub/decision-validation/trade-off-analysis-working-skill/">Trade-Off Analysis Working Skill</a> — Use when the triage requires comparing dissimilar options with competing criteria.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a> — Context for triaging credit block incidents by revenue impact.</li>
      <li><a href="/atlas/diagnostics/sap-background-job-diagnostics/">SAP Background Job Diagnostics</a> — Context for triaging batch failures and timeout issues.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of priority triage practices. It is not official ITIL, PMP, or agile framework documentation. It focuses on practical triage for enterprise teams where capacity is limited and stakeholders demand justification for what is and is not being worked on.</p>
    <p>Known limitations: the scoring formula is a heuristic, not an optimization algorithm. It does not account for probabilistic risk, resource skill matching, or strategic alignment beyond impact and urgency. It assumes tasks are independent enough to be scored individually. For complex portfolios with interdependent projects, additional portfolio management tools may be needed. The skill does not cover automated scheduling algorithms or resource leveling software.</p>
  </section>
</article>
