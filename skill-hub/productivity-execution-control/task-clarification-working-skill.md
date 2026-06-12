---
layout: default
title: "Task Clarification Working Skill"
description: "Turn a vague or ambiguous task into a clear, actionable work item with defined inputs, outputs, success criteria, and ownership so the assignee can start immediately."
permalink: /skill-hub/productivity-execution-control/task-clarification-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/productivity-execution-control/">Productivity and Execution Control</a></li>
    <li aria-current="page">Task Clarification</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Productivity and Execution Control</p>
  <h1>Task Clarification Working Skill</h1>
  <p class="lead">Turn a vague or ambiguous task into a clear, actionable work item with defined inputs, outputs, success criteria, and ownership so the assignee can start immediately and finish with confidence.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Most project delays start with a poorly defined task. A ticket says "fix the integration issue" or a meeting note says "review the process." No one knows what done looks like, what information is needed, or who decides whether the result is acceptable. This skill converts vague assignments into a Clarified Task Brief: a one-page document that states the task, the inputs, the expected output, the acceptance criteria, the owner, and the deadline. The brief becomes the contract between the requester and the assignee. It eliminates ambiguity, prevents rework, and makes progress measurable.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A task is assigned with a single sentence or a vague subject line.</li>
      <li>Two people interpret the same task differently and produce conflicting results.</li>
      <li>A task has been open for days with no progress because the assignee does not know where to start.</li>
      <li>A task is returned as "not what I asked for" even though the assignee followed instructions.</li>
      <li>An AI agent is being asked to perform work and the prompt is ambiguous or underspecified.</li>
      <li>A work package from a WBS needs to be converted into an executable task for a single owner.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP support ticket: "Customer master is wrong"</h3>
    <p>A ticket arrives with the subject "Customer master is wrong." The assignee spends two hours trying to identify which customer, which field, and what "wrong" means. After back-and-forth messages, it turns out that the payment terms are outdated for one customer in one company code. A Clarified Task Brief would have stated: "Update payment terms for customer C-10001 in company code 1000 from ZB30 to ZB15. Input: current customer master record. Output: updated customer master with payment terms ZB15. Acceptance: customer record displays ZB15 in XD03 and the change is logged in the change log. Owner: support analyst. Deadline: 2026-06-14." The task would have been completed in 15 minutes.</p>

    <h3>Project task: "Improve the reporting process"</h3>
    <p>A project manager assigns a task: "Improve the reporting process." The analyst produces a 20-page document proposing a new data warehouse. The manager wanted a one-page checklist to reduce report generation time from 30 minutes to 10 minutes. A Clarified Task Brief would have asked: what is the current time? What is the target time? What is the scope of reports? What is the budget for tools? The brief would have prevented the mismatch and saved a week of wasted work.</p>

    <h3>Integration task: "Handle the IDoc error"</h3>
    <p>An operations lead assigns: "Handle the IDoc error." The developer reprocesses the IDoc. The business user complains that the root cause was never identified and the error will recur. A Clarified Task Brief would have distinguished between three possible tasks: (1) reprocess the failed IDoc, (2) diagnose why the IDoc failed, or (3) implement a fix to prevent recurrence. Each has a different input, output, and owner. Without clarification, the wrong task was performed.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Original task description, ticket, email, or meeting note that created the assignment.</li>
      <li>Context: the system, process, project, or business area affected.</li>
      <li>Stakeholder who requested the task and who will accept the result.</li>
      <li>Any existing documentation, logs, or data samples that describe the current state.</li>
      <li>Constraints: deadline, budget, tools available, authority limits.</li>
      <li>Related tasks or dependencies that affect how this task is performed.</li>
      <li>Historical examples of similar tasks that succeeded or failed (optional).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the current state, and what is the desired state?</li>
      <li>What is the smallest change that would satisfy the requester?</li>
      <li>What system, transaction, or document must be changed?</li>
      <li>What data or evidence is needed before work can begin?</li>
      <li>Who will verify that the task is complete, and what criteria will they use?</li>
      <li>What is the deadline, and what happens if the deadline is missed?</li>
      <li>What is out of scope: what should the assignee not do?</li>
      <li>What has been tried before, and why did it succeed or fail?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Capture the original request.</strong> Copy the exact text of the task, ticket, or message. Do not paraphrase. The original wording is evidence of what was asked.</li>
      <li><strong>Identify the requester and the acceptor.</strong> Name the person who asked for the task and the person who will judge completion. If they are different, both must agree on the brief.</li>
      <li><strong>State the current state.</strong> Describe what exists now, with references to systems, documents, or data. Example: "Customer C-10001 in company code 1000 has payment terms ZB30."</li>
      <li><strong>State the desired state.</strong> Describe what must be true when the task is complete. Example: "Customer C-10001 in company code 1000 has payment terms ZB15."</li>
      <li><strong>Define the output artifact.</strong> Name the document, configuration change, log, report, or update that proves the task is done. Example: "Updated customer master record with change log entry."</li>
      <li><strong>Define acceptance criteria.</strong> List 2–5 verifiable conditions that the acceptor will check. Example: "XD03 shows ZB15." "Change log shows the update on 2026-06-14." "No other fields were modified."</li>
      <li><strong>Define inputs required.</strong> List what the assignee needs to begin: access, data, approvals, documentation, or decisions from others.</li>
      <li><strong>Define out-of-scope items.</strong> Explicitly list what the assignee should not do. This prevents scope creep and mismatched expectations.</li>
      <li><strong>Define the owner and deadline.</strong> Name one person accountable and a date by which the brief must be completed.</li>
      <li><strong>Validate the brief with the requester.</strong> Send the brief back to the requester and ask: "Is this what you meant?" Do not start work until the brief is confirmed. If the requester changes the brief, update it and reconfirm.</li>
      <li><strong>Execute against the brief.</strong> Use the brief as the contract. If new information changes the task, update the brief and reconfirm before continuing.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the requester and acceptor are different, the brief must be confirmed by both before work starts.</li>
      <li>If the desired state cannot be described in one sentence, the task is too large and must be split into multiple briefs.</li>
      <li>If the inputs are not available, the task is blocked until the inputs are provided, not started with assumptions.</li>
      <li>If the acceptance criteria are subjective, replace them with measurable conditions or system states.</li>
      <li>If the deadline is missing, request one. If no deadline is given, set a proposed deadline and confirm it.</li>
      <li>If the task has been tried before and failed, include the failure mode in the brief so the assignee does not repeat it.</li>
      <li>If the brief changes during execution, update the brief and reconfirm with the requester before continuing.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Clarified Task Brief</strong> — One-page document with task statement, current state, desired state, output, acceptance criteria, inputs, out-of-scope items, owner, and deadline. See template below.</li>
      <li><strong>Confirmation Record</strong> — Evidence that the requester confirmed the brief (email, chat, or sign-off in the ticket).</li>
      <li><strong>Change Log</strong> — Record of changes to the brief after initial confirmation, with reasons and reconfirmations.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Clarified Task Brief (compact)</h3>
    <pre><code>---
artifact: Clarified Task Brief
id: CTB-&lt;number&gt;
status: draft | confirmed | in progress | complete
---

## Task statement
&lt;One sentence describing what must be done&gt;

## Original request
&lt;Copy the original ticket, email, or message exactly&gt;

## Context
- System / process: &lt;name&gt;
- Project / phase: &lt;name&gt;
- Requester: &lt;name&gt;
- Acceptor: &lt;name&gt;

## Current state
&lt;What is true now&gt;

## Desired state
&lt;What must be true when the task is complete&gt;

## Output artifact
&lt;What document, change, or evidence proves completion&gt;

## Acceptance criteria
- [ ] &lt;Verifiable condition 1&gt;
- [ ] &lt;Verifiable condition 2&gt;
- [ ] &lt;Verifiable condition 3&gt;

## Inputs required
- &lt;Data, access, documentation, or decision needed&gt;
- &lt;Second input&gt;

## Out of scope
- &lt;What the assignee must not do&gt;
- &lt;Second out-of-scope item&gt;

## Owner and deadline
- Owner: &lt;name&gt;
- Deadline: YYYY-MM-DD
- Proposed start date: YYYY-MM-DD

## Change log
| Date | Change | Reason | Confirmed by |
|------|--------|--------|--------------|
| — | — | — | — |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The task statement is one sentence and describes a single outcome.</li>
      <li>The original request is copied verbatim, not paraphrased.</li>
      <li>Current state and desired state are specific enough to verify without interpretation.</li>
      <li>Acceptance criteria are measurable, not subjective.</li>
      <li>At least one input is identified; if none are needed, this is explicitly stated.</li>
      <li>At least one out-of-scope item is identified to prevent drift.</li>
      <li>The owner is a single named person, not a team or department.</li>
      <li>The deadline is specific and confirmed by the requester.</li>
      <li>The brief has been confirmed by the requester before work started.</li>
      <li>Any changes to the brief are logged and reconfirmed.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Paraphrasing the original request instead of copying it.</strong> Consequence: the brief drifts from the requester's intent. When the output is rejected, there is no evidence of what was originally asked.</li>
      <li><strong>Defining acceptance criteria as "the requester is happy."</strong> Consequence: the criteria are subjective and unverifiable. The assignee does not know when to stop, and the requester does not know what to check.</li>
      <li><strong>Skipping the confirmation step.</strong> Consequence: the assignee works on an assumption, and the requester rejects the result because it does not match their unspoken expectations.</li>
      <li><strong>Starting work before inputs are available.</strong> Consequence: the assignee makes assumptions about data or access, produces a flawed output, and must redo the work when the real inputs arrive.</li>
      <li><strong>Not defining out-of-scope items.</strong> Consequence: the assignee does extra work that is not needed, or the requester assumes adjacent tasks are included and is disappointed when they are not.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A forwarded email with a note: "Please handle this." No task statement, no current state, no desired state, no acceptance criteria, no deadline. The assignee must infer everything from the forwarded thread, which contains conflicting opinions, outdated information, and no decision.</p>
    <p><strong>Why it fails:</strong> The assignee spends more time interpreting the request than doing the work. The result is unpredictable. The requester is dissatisfied because their implicit expectations were not met. The cycle repeats with additional back-and-forth messages.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Clarified Task Brief
id: CTB-2026-044
status: confirmed
---

## Task statement
Update payment terms for customer C-10001 in company code 1000 from ZB30 to ZB15.

## Original request
"Customer master is wrong — payment terms should be 15 days, not 30. Please fix." — Email from Anna Kowalski, 2026-06-12.

## Context
- System / process: SAP S/4HANA customer master (XD02/XD03)
- Project / phase: Ongoing AMS support
- Requester: Anna Kowalski (AR team lead)
- Acceptor: Anna Kowalski

## Current state
Customer C-10001 in company code 1000 has payment terms ZB30 (30 days net).

## Desired state
Customer C-10001 in company code 1000 has payment terms ZB15 (15 days net).

## Output artifact
Updated customer master record with change log entry.

## Acceptance criteria
- [ ] XD03 displays payment terms ZB15 for customer C-10001 in company code 1000.
- [ ] Change log shows the update on 2026-06-14 with reason "Customer request per email."
- [ ] No other fields (address, bank details, tax number) were modified.
- [ ] AR team confirms the change in their next reconciliation run.

## Inputs required
- XD02 access in company code 1000.
- Approval from customer master governance team (already received via ticket APP-2026-112).

## Out of scope
- Updating other customers.
- Changing credit limit or risk class.
- Informing the customer directly (AR team handles communication).

## Owner and deadline
- Owner: Dmitri Volkov
- Deadline: 2026-06-14
- Proposed start date: 2026-06-12

## Change log
| Date | Change | Reason | Confirmed by |
|------|--------|--------|--------------|
| — | — | — | — |
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Task clarification specialist for enterprise support and project work.</p>
    <p><strong>Context:</strong> You have a vague task description, ticket, or message. You need to produce a Clarified Task Brief that the assignee can use to start work immediately and the requester can use to verify completion.</p>
    <p><strong>Task:</strong> Extract the original request, define current and desired state, specify acceptance criteria, identify inputs and out-of-scope items, and name an owner and deadline. Confirm the brief with the requester before work starts.</p>
    <p><strong>Output format:</strong> Structured Clarified Task Brief per the template, followed by a confirmation request message.</p>

    <ul>
      <li><strong>Never paraphrase the original request.</strong> Copy it verbatim. Paraphrasing introduces interpretation drift.</li>
      <li><strong>Always define current and desired state in specific, verifiable terms.</strong> Use system names, transaction codes, field values, and document IDs where possible.</li>
      <li><strong>Acceptance criteria must be checkboxes, not opinions.</strong> Each criterion must be verifiable by inspection, test, or log.</li>
      <li><strong>Always identify out-of-scope items.</strong> If the requester did not specify boundaries, propose them and ask for confirmation.</li>
      <li><strong>Never start work without confirmed inputs.</strong> If data, access, or approval is missing, flag the gap and wait.</li>
      <li><strong>Never guess the deadline.</strong> If no deadline is given, propose one and request confirmation.</li>
      <li><strong>Do not invent context or history.</strong> If you do not know what was tried before, state that the history is unknown and ask for it.</li>
      <li><strong>Link to Atlas diagnostics</strong> when the task touches SAP processes. For example, customer master tasks should reference <a href="/atlas/diagnostics/sap-customer-vendor-master-diagnostics/">SAP Customer Vendor Master Diagnostics</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/productivity-execution-control/work-breakdown-planning-working-skill/">Work Breakdown Planning Working Skill</a> — Use to decompose a project before clarifying individual tasks.</li>
      <li><a href="/skill-hub/productivity-execution-control/priority-triage-working-skill/">Priority Triage Working Skill</a> — Use to decide which clarified tasks to execute first.</li>
      <li><a href="/skill-hub/productivity-execution-control/blocker-escalation-working-skill/">Blocker Escalation Working Skill</a> — Use when a clarified task is blocked by missing inputs or decisions.</li>
      <li><a href="/skill-hub/business-analysis/acceptance-criteria-working-skill/">Acceptance Criteria Working Skill</a> — Use to strengthen the acceptance criteria section of the brief.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-customer-vendor-master-diagnostics/">SAP Customer Vendor Master Diagnostics</a> — Diagnostic context for tasks involving customer or vendor master data.</li>
      <li><a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a> — Validation context for tasks involving mandatory field completeness.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of task clarification practices. It is not official ITIL, BABOK, or SAP methodology. It focuses on practical clarification for enterprise support and project work where ambiguity causes delays and rework.</p>
    <p>Known limitations: the skill assumes the requester is available to confirm the brief. It does not cover tasks where the requester is unavailable or uncooperative. It treats the brief as a bilateral contract, not a unilateral assignment. For complex tasks requiring multi-week execution, the brief may need to be supplemented with a detailed work plan or design document. The skill does not cover legal or compliance review of task scopes.</p>
  </section>
</article>
