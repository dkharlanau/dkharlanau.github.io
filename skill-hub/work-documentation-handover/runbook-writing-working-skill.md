---
layout: default
title: "Runbook Writing Working Skill"
description: "Write a step-by-step operational runbook that an on-call engineer can follow safely without knowing the system history."
permalink: /skill-hub/work-documentation-handover/runbook-writing-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/work-documentation-handover/">Work Documentation and Handover</a></li>
    <li aria-current="page">Runbook Writing</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Work Documentation and Handover</p>
  <h1>Runbook Writing Working Skill</h1>
  <p class="lead">Write a step-by-step operational runbook that an on-call engineer can follow safely without knowing the system history.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Operational incidents do not wait for the expert who knows the system best. They happen at night, on weekends, and during vacations. This skill produces an Operational Runbook: a precise, step-by-step procedure that an on-call engineer can execute safely without prior knowledge of the system history or deep domain expertise. The runbook is designed for stress: it assumes the reader is tired, under pressure, and possibly new to the environment. Every step is numbered, every decision is explicit, every command is exact, and every rollback option is stated. The output is the difference between a controlled response and a chaotic one.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A critical operational procedure must be performed by on-call engineers who may not be the primary experts.</li>
      <li>A system component fails in a predictable way and the recovery steps must be standardized to avoid ad-hoc fixes.</li>
      <li>A routine maintenance task is performed infrequently and the team needs a reminder of the exact sequence.</li>
      <li>An AI agent is being trained to assist with operational tasks and needs structured, unambiguous procedures.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP background job failure: runbook for queue restart</h3>
    <p>A critical background job ZIDOC_ALERT fails and the queue of failed IDocs grows. The primary engineer is on vacation. The on-call engineer must restart the job safely without causing duplicate processing or data loss. The runbook states: step 1, check SM37 for the failed job and note the job ID; step 2, check SM58 for locked entries; step 3, if no locked entries, release the job from SM37 with variant ZIDOC_ALERT_V1; step 4, monitor SM37 for 10 minutes; step 5, if the job fails again, stop and escalate to the basis team. Without the runbook, the on-call engineer restarts the job with the wrong variant, processes the same IDocs twice, and creates duplicate partner entries that require manual cleanup.</p>

    <h3>Database index rebuild: runbook for monthly maintenance</h3>
    <p>A monthly database index rebuild is required to prevent performance degradation in the customer reconciliation report. The task is performed once a month and no one remembers the exact sequence. The runbook states: step 1, check DB02 for index fragmentation above 30%; step 2, verify no long-running jobs are active in SM50; step 3, execute the rebuild script via DB13 with the scheduled variant; step 4, verify rebuild completion in DB02; step 5, run ZCUST_REP to confirm performance improvement. Without the runbook, the team skips the check for active jobs, rebuilds during peak hours, and locks the customer table for 20 minutes, blocking sales order creation.</p>

    <h3>Failover procedure: runbook for middleware switch</h3>
    <p>The primary SAP PI instance fails and the team must switch to the standby instance. The procedure involves updating RFC destinations, redirecting the message queue, and validating the first five messages. The runbook states: step 1, confirm primary instance failure via SMICM; step 2, update SM59 destination PI_PROD to point to PI_STANDBY; step 3, check SXMB_ADM for queue status on standby; step 4, release the first five messages individually and verify processing; step 5, if all five succeed, release the queue batch. If any fail, stop and call the integration architect. Without the runbook, the on-call engineer switches the destination but forgets to validate the first messages, and a mapping error on the standby instance goes undetected for two hours, corrupting 200 messages.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>The exact procedure as performed by the expert, including every screen, transaction, and command.</li>
      <li>The systems, environments, and clients where the procedure is executed.</li>
      <li>The prerequisites: access rights, system state, timing constraints, and dependencies.</li>
      <li>The success criteria: how to know the procedure worked.</li>
      <li>The failure criteria: what to watch for, when to stop, and what to do if the procedure fails.</li>
      <li>The rollback or recovery steps if the procedure causes unintended effects.</li>
      <li>The escalation path: who to call if the runbook does not resolve the issue.</li>
      <li>Historical incident data showing how the procedure has been used and what went wrong.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the trigger for this runbook? When does an engineer know it is time to use it?</li>
      <li>What is the first step? Is there a safety check before any action is taken?</li>
      <li>What are the exact commands, transactions, and parameter values? Can they be copy-pasted?</li>
      <li>What should the engineer see at each step? What output confirms the step is correct?</li>
      <li>What could go wrong at each step? What is the stop condition?</li>
      <li>What is the rollback plan if the procedure makes things worse?</li>
      <li>How long should each step take? What is the timeout before escalation?</li>
      <li>Who is the escalation contact, and what information must be provided when escalating?</li>
      <li>Has this runbook been tested by someone who does not know the system? If not, what assumptions are unverified?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Define the trigger.</strong> State the exact condition or alert that tells the on-call engineer to open this runbook. The trigger must be unambiguous: not "when the system is slow" but "when SM50 shows more than 50% work processes in PRIV mode for more than 10 minutes."</li>
      <li><strong>State the prerequisites.</strong> Before any action, the engineer must verify: system availability, access rights, no conflicting jobs, and the correct environment. Include a pre-flight checklist.</li>
      <li><strong>Write the procedure as numbered steps.</strong> Every step must be a single action. If a step contains a decision, use a nested "if-then-else" structure. Do not combine multiple actions into one step.</li>
      <li><strong>Include exact commands and parameters.</strong> Use the exact transaction code, program name, command syntax, or URL. If the command has a variant, state the variant name. If a parameter must be entered, state the value or the rule for deriving it.</li>
      <li><strong>Include expected output for each step.</strong> State what the engineer should see after executing the step. If the output is a table, describe the expected row. If it is a message, quote the expected message text.</li>
      <li><strong>Document failure paths at each step.</strong> For each step, state what to do if the expected output does not appear. Include a stop condition: "If you see error X, stop and escalate. Do not proceed."</li>
      <li><strong>Document the rollback procedure.</strong> If the procedure modifies data or configuration, include the exact steps to undo the change. The rollback must be tested, not theoretical.</li>
      <li><strong>State the success criteria.</strong> Define how the engineer knows the procedure is complete and successful. Include verification steps that run after the main procedure.</li>
      <li><strong>Include the escalation path.</strong> Name the contact, the contact method, and the information to provide. Include a template for the escalation message.</li>
      <li><strong>Test the runbook.</strong> Ask an engineer who has never performed the procedure to follow the runbook in a test environment. Observe where they hesitate, where they ask questions, and where they deviate. Revise the runbook based on the test.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a step has a conditional outcome, write both paths. Do not assume the engineer will know the right path.</li>
      <li>If a command requires a password or secret, reference the secure vault. Do not embed credentials in the runbook.</li>
      <li>If the procedure modifies production data, require a second-person review before execution. Document the review step.</li>
      <li>If the runbook is for an emergency, keep it to one page if possible. Emergency runbooks are not comprehensive manuals; they are survival guides.</li>
      <li>If the procedure has been updated, version the runbook and archive the old version. Do not let engineers use outdated steps.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Operational Runbook</strong> — Step-by-step procedure with triggers, prerequisites, exact commands, expected outputs, failure paths, rollback, and escalation. See template below.</li>
      <li><strong>Pre-Flight Checklist</strong> — One-page checklist of prerequisites and safety checks before the procedure begins.</li>
      <li><strong>Escalation Card</strong> — One-page contact list and information template for escalation.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Operational Runbook (compact)</h3>
    <pre><code>---
artifact: Operational Runbook
id: RB-&lt;system&gt;-&lt;number&gt;
runbook_name: &lt;Name of procedure&gt;
severity: &lt;P1 / P2 / P3 / routine&gt;
environment: &lt;Production / Test / Development&gt;
last_tested: YYYY-MM-DD
test_result: &lt;pass / fail / not tested&gt;
author: &lt;Name&gt
doc_reviewer: &lt;Name&gt
doc_status: draft | reviewed | approved
---

## Trigger
- &lt;Exact condition that starts this runbook&gt;
- &lt;Monitoring alert, ticket type, or user report&gt;

## Prerequisites (Pre-Flight Checklist)
- [ ] System &lt;name&gt; is reachable
- [ ] I have access to &lt;transaction or system&gt;
- [ ] No conflicting jobs are running in &lt;SM37 / SM50&gt;
- [ ] It is within the approved maintenance window (if applicable)
- [ ] A second reviewer is available (if required for production changes)

## Procedure
1. &lt;Action&gt; — &lt;Exact command or transaction&gt;
   - Expected output: &lt;What the engineer should see&gt;
   - If output is not as expected: &lt;Failure path or stop condition&gt;
2. &lt;Action&gt; — &lt;Exact command or transaction&gt;
   - Expected output: &lt;What the engineer should see&gt;
   - If output is not as expected: &lt;Failure path or stop condition&gt;
3. Decision: if &lt;condition&gt;, then &lt;step A&gt;. Else, &lt;step B&gt;.
   - Step A: &lt;Action&gt;
   - Step B: &lt;Action&gt;

## Rollback
| Step | Action | Expected Output | When to Use |
|------|--------|-----------------|-------------|
| R1 | &lt;Undo action&gt; | &lt;What confirms undo&gt; | &lt;Condition&gt; |
| R2 | &lt;Undo action&gt; | &lt;What confirms undo&gt; | &lt;Condition&gt; |

## Verification
- &lt;Step to confirm the procedure succeeded&gt;
- &lt;Step to confirm no side effects&gt;

## Escalation
- Contact: &lt;Name, role, phone / email&gt;
- Provide: &lt;System, incident ID, steps taken, current status, error message&gt;
- Escalate if: &lt;Specific conditions&gt;
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The trigger is specific and measurable. An engineer knows exactly when to open the runbook.</li>
      <li>Prerequisites are checked before any action is taken.</li>
      <li>Every step is a single action with an exact command or transaction.</li>
      <li>Expected output is described for every step.</li>
      <li>Failure paths are documented at every step where failure is possible.</li>
      <li>Rollback steps are tested and documented, not theoretical.</li>
      <li>Success criteria are verifiable and include a post-procedure check.</li>
      <li>Escalation contact and required information are stated.</li>
      <li>The runbook has been tested by an engineer who did not write it.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Writing a generic overview instead of a step-by-step procedure.</strong> Consequence: the engineer must interpret general advice under pressure, which leads to mistakes. "Restart the job" is not enough; specify the transaction, the job name, and the variant.</li>
      <li><strong>Omitting failure paths.</strong> Consequence: when a step fails, the engineer improvises. Improvisation under pressure often makes the situation worse.</li>
      <li><strong>Embedding passwords or secrets in the runbook.</strong> Consequence: security breach and credential rotation. Reference the secure vault or password manager.</li>
      <li><strong>Not testing the runbook with a new engineer.</strong> Consequence: the runbook contains assumptions that the writer did not realize. The new engineer gets stuck on step 3 and escalates unnecessarily.</li>
      <li><strong>Writing one runbook for multiple scenarios.</strong> Consequence: the engineer must read irrelevant sections under pressure. Split into separate runbooks for separate triggers.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A wiki page titled "IDoc Monitoring." It says: "If IDocs fail, check WE02 for errors. If the error is a mapping issue, fix the mapping in SAP PI. If the error is a data issue, correct the data in the source system. Reprocess the IDoc using BD87 or WE19. Monitor SM58 for RFC issues. Contact the integration team if the issue persists." No trigger specificity, no exact steps, no expected outputs, no failure paths, no rollback, no escalation contact details. The engineer must interpret every instruction under pressure.</p>
    <p><strong>Why it fails:</strong> It is an overview, not a procedure. The engineer does not know which tool to use when, what to look for, or when to stop. The runbook is not usable under pressure.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Operational Runbook
id: RB-PI-2026-003
runbook_name: Restart Failed IDoc Queue for ORDERS05
severity: P2
environment: Production
last_tested: 2026-06-05
test_result: pass
author: K. Schmidt
doc_reviewer: T. Nguyen
doc_status: approved
---

## Trigger
- Monitoring alert fires for ORDERS05 IDoc queue depth > 20
- User reports sales orders not appearing in S/4HANA from EDI
- SM58 shows failed tRFC entries for destination PI_TO_S4

## Prerequisites
- [ ] S/4HANA production client 100 is reachable
- [ ] I have access to WE02, WE19, SM58, and SXMB_ADM
- [ ] No conflicting IDoc mass reprocessing job is running in SM37
- [ ] It is outside the EDI blackout window (02:00–04:00 CET)

## Procedure
1. Check WE02 for ORDERS05 IDocs with status 51 or 63 in the last 2 hours.
   - Expected output: List of failed IDocs with error text. Count should match alert.
   - If no failed IDocs are found: Stop. Check SM58 for tRFC errors instead. Escalate to basis if SM58 is clear.
2. Open the first failed IDoc. Read the error text in the status record.
   - If error text contains "mapping": Go to step 3 (mapping fix).
   - If error text contains "data" or "master data": Go to step 4 (data correction).
   - If error text contains "system" or "RFC": Go to step 5 (RFC check).
3. Mapping fix path:
   - 3a. Open SAP PI message monitoring. Find the failed message for the IDoc.
   - 3b. If the mapping error is for a known missing field (e.g., delivery block), update the mapping table ZDLV_BLOCK_MAP in SE16.
   - 3c. Reprocess the single IDoc in WE19. Verify status changes to 53 in WE02.
   - 3d. If successful, reprocess the remaining affected IDocs one by one. Do NOT use BD87 for mapping errors until the mapping is confirmed fixed.
4. Data correction path:
   - 4a. Identify the missing or incorrect master data from the error text (e.g., material not found, customer blocked).
   - 4b. Correct the data in the source system or in S/4 master data. Do NOT reprocess until the data is corrected.
   - 4c. Reprocess the corrected IDoc in WE19. Verify status 53.
   - 4d. If multiple IDocs have the same data error, fix the data once, then reprocess the batch in BD87 after verification.
5. RFC check path:
   - 5a. Check SM58 for failed tRFC entries for destination PI_TO_S4.
   - 5b. If entries are in status SYSFAIL or COMMITFAIL, check the RFC destination in SM59. Test the connection.
   - 5c. If the connection test fails, check the gateway and network status. Do NOT reprocess IDocs until the RFC destination is green.
   - 5d. Once the connection is green, execute the failed tRFC entries in SM58. Verify in WE02 that IDocs process successfully.

## Rollback
| Step | Action | Expected Output | When to Use |
|------|--------|-----------------|-------------|
| R1 | Stop reprocessing in WE19 / BD87 | No new IDocs processed | If mapping or data fix is wrong |
| R2 | Reverse master data change in the source system | Data restored to previous state | If data correction caused new errors |
| R3 | Set IDoc to status 68 (no further processing) | Status 68 in WE02 | If the IDoc must be held for manual review |

## Verification
- All failed IDocs from the initial WE02 list show status 53 or 68.
- SM58 shows no failed tRFC entries for PI_TO_S4.
- Customer service confirms that new sales orders are appearing in S/4.
- Run ZCUST_REP to verify no duplicate orders were created.

## Escalation
- Contact: K. Schmidt (Integration Architect) — +49-xxx-xxx, k.schmidt@company.com
- Provide: System (S/4 client 100), incident ID, error text from WE02, steps taken, current status, IDoc numbers affected.
- Escalate if: RFC destination is green but IDocs still fail; mapping table is updated but error persists; more than 50 IDocs are affected; or the procedure exceeds 30 minutes.
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Runbook writer for SAP operational support and on-call engineering.</p>
    <p><strong>Context:</strong> You have an operational procedure, an expert interview, and incident history. You need to produce an Operational Runbook that an on-call engineer can follow safely without knowing the system history.</p>
    <p><strong>Task:</strong> Create a structured Operational Runbook using the template below. Include a specific trigger, pre-flight checklist, exact numbered steps, expected outputs, failure paths, rollback, and escalation.</p>
    <p><strong>Output format:</strong> Structured Operational Runbook in Markdown with tables for rollback and escalation.</p>

    <ul>
      <li><strong>Never write a generic overview.</strong> Every step must be a single action with an exact command or transaction. The engineer should not need to interpret.</li>
      <li><strong>Always include a pre-flight checklist.</strong> Prerequisites must be verified before any action. Safety first.</li>
      <li><strong>Always include expected output for each step.</strong> The engineer must know what success looks like at each point.</li>
      <li><strong>Always include failure paths.</strong> If the expected output does not appear, the engineer must know what to do. Include stop conditions.</li>
      <li><strong>Always include rollback steps.</strong> If the procedure modifies data or configuration, the undo path must be tested and documented.</li>
      <li><strong>Do not embed credentials or secrets.</strong> Reference the secure vault or password manager.</li>
      <li><strong>Test the runbook with a new engineer.</strong> If the test reveals ambiguity, rewrite the step until it is unambiguous.</li>
      <li><strong>Link to Atlas diagnostics</strong> when the runbook addresses documented SAP failure modes. For example, runbooks for background jobs should reference <a href="/atlas/diagnostics/sap-background-job-diagnostics/">SAP Background Job Diagnostics</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/work-documentation-handover/incident-documentation-working-skill/">Incident Documentation Working Skill</a> — Use to document the incident that the runbook is designed to address.</li>
      <li><a href="/skill-hub/work-documentation-handover/knowledge-article-writing-working-skill/">Knowledge Article Writing Working Skill</a> — Use to produce a quick-reference article for common symptoms; the runbook is the full procedure.</li>
      <li><a href="/skill-hub/work-documentation-handover/process-documentation-working-skill/">Process Documentation Working Skill</a> — Use to document the broader process that the runbook fits into.</li>
      <li><a href="/skill-hub/sap-ams/incident-triage-working-skill/">Incident Triage Working Skill</a> — Use to classify and route incidents before the runbook is opened.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-background-job-diagnostics/">SAP Background Job Diagnostics</a> — Diagnostic context for background job runbooks.</li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — Diagnostic context for IDoc runbooks.</li>
      <li><a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">SAP Interface Monitoring Diagnostics</a> — Monitoring context for integration runbooks.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of operational runbook practices. It is not official ITIL, SAP, or DevOps documentation. It focuses on runbooks for enterprise and SAP environments where on-call engineers rotate, system history is complex, and incidents are expensive. Known limitations: it does not cover incident response coordination, communication management, or war-room facilitation. It produces the procedural document, not the response team structure. It assumes access to an expert who can verify the exact steps. It does not cover automated runbooks or cloud-native infrastructure, though the principles apply. The templates should be adapted to the organization's runbook platform or wiki.</p>
  </section>
</article>
