---
layout: default
title: "Operational Knowledge Capture — Working Skill"
description: "Turn firefighting into reusable knowledge: capture what was done, why it worked, and when it applies."
permalink: /skill-hub/sap-ams/operational-knowledge-capture-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/sap-ams/">SAP AMS</a></li>
    <li aria-current="page">Operational Knowledge Capture</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — SAP AMS / Operations</p>
  <h1>Operational Knowledge Capture</h1>
  <p class="lead">Turn firefighting into reusable knowledge: capture what was done, why it worked, and when it applies.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you document operational knowledge in a form that the next person — or an AI agent — can actually use. It captures not just the solution but the context: what was happening, what almost went wrong, why the fix worked, and when the same fix applies again. The output is an Operational Knowledge Capture Note that reduces repeat incidents and onboarding time.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>An incident was resolved after significant troubleshooting and the method should be reusable.</li>
      <li>A workaround was discovered for a known system limitation and other teams need to know it.</li>
      <li>A complex configuration or custom code behavior was decoded and the explanation should survive the person who found it.</li>
      <li>A new team member is joining and needs to understand how the landscape actually works, not just how it was designed.</li>
      <li>An AI agent or automation tool needs structured operational knowledge to handle routine incidents.</li>
      <li>A runbook or procedure was updated during an emergency and the update needs to be formalized.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Example 1: The "magic" transaction sequence for stuck IDocs</h3>
    <p>A consultant discovers that IDocs in status 64 can be cleared with a specific sequence of BD87, WE19, and a custom program — but only when the error is a specific partner profile mismatch. The knowledge capture records the exact sequence, the error pattern that justifies it, the cases where it does not apply (status 51 with syntax errors), and the verification step. Six months later, a new consultant uses the note to resolve the same issue in 10 minutes instead of 2 hours.</p>

    <h3>Example 2: The weekend restart procedure that always misses one step</h3>
    <p>After every planned restart, the qRFC queues fail to process because one RFC destination is not verified before queue release. The knowledge capture updates the runbook with the missing step, explains why the destination matters (it handles CRM replication), and adds a verification command. The next restart follows the updated runbook and avoids the queue buildup.</p>

    <h3>Example 3: The customer-specific pricing condition that breaks every quarter</h3>
    <p>A pricing condition for a specific customer group is maintained manually and expires every quarter because the validity period is not extended. The knowledge capture documents the condition type, the customer group, the transaction to extend it, the business owner who must approve the extension, and the report that detects the upcoming expiration. The next quarter, the report triggers a proactive ticket instead of a reactive emergency.</p>

    <h3>Example 4: The MDG change request activation that fails for one specific entity type</h3>
    <p>A data steward finds that MDG change request activation fails for supplier entities when a specific industry sector is selected, due to a missing mapping in the CVI synchronization. The knowledge capture records the entity type, the industry sector, the error message, the workaround (manual CVI sync after activation), and the long-term fix (update the mapping table). Future stewards avoid the failure and know when the workaround is still needed.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>The incident ticket or triage record with full symptom, resolution, and timeline.</li>
      <li>The exact transactions, programs, commands, or configuration paths used to resolve the issue.</li>
      <li>The system landscape where the resolution was applied: client, system, module.</li>
      <li>The business context: which process, which user group, which time window.</li>
      <li>What was tried that did not work — the failed attempts are as valuable as the success.</li>
      <li>The stakeholder who owns the process or data and can verify the knowledge is correct.</li>
      <li>Any related documentation, runbooks, or wiki pages that should be updated or linked.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What was the exact symptom, and what was the last successful state before the failure?</li>
      <li>What specific steps were taken to resolve the issue, in what order, and in which system?</li>
      <li>Why did those steps work? What was the underlying mechanism or system behavior?</li>
      <li>What was tried that did not work, and why did it fail?</li>
      <li>Under what conditions does this knowledge apply, and when does it not apply?</li>
      <li>What would have happened if the resolution had not been applied, or had been applied incorrectly?</li>
      <li>Who owns the process or system where this knowledge applies, and who can verify it is still valid?</li>
      <li>How will someone know this knowledge exists when they encounter the same symptom?</li>
      <li>When should this knowledge be reviewed or retired?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Capture immediately after resolution.</strong> Do not wait. Memory decays fast. Schedule 15 minutes after every non-trivial incident to document.</li>
      <li><strong>Record the situation.</strong> What was happening? Which system, which process, which users, which time window? Include urgency and business impact.</li>
      <li><strong>Record what was done.</strong> Step by step. Include transaction codes, program names, table names, configuration paths, and exact values. Assume the reader has moderate SAP knowledge but no context about this specific landscape.</li>
      <li><strong>Record why it worked.</strong> Explain the system behavior, data flow, or configuration logic that made the fix effective. This is the difference between a runbook and a cheat sheet.</li>
      <li><strong>Record what almost went wrong.</strong> Document failed attempts, wrong paths, assumptions that were false, and near misses. This prevents the next person from repeating the same dead ends.</li>
      <li><strong>Define preconditions.</strong> When does this knowledge apply? Which system version, which client, which module, which data state? Be explicit about exclusions.</li>
      <li><strong>Define limitations.</strong> What does this procedure not cover? What are the edge cases where it fails or needs escalation?</li>
      <li><strong>Define verification.</strong> How does the next person confirm the procedure is still valid? Which transaction, which report, which check?</li>
      <li><strong>Name an owner.</strong> Who maintains this knowledge? Who can answer questions if the note is unclear?</li>
      <li><strong>Set a review date.</strong> Operational knowledge rots. Systems change. Set a review date based on system stability: 3 months for volatile areas, 6 months for stable ones.</li>
      <li><strong>Make it discoverable.</strong> Store the note where people look for help: ticket system, wiki, knowledge base, or runbook repository. Tag it with symptom keywords, error messages, and transaction codes.</li>
      <li><strong>Link related knowledge.</strong> Connect to other capture notes, runbooks, Atlas pages, or ticket histories that cover adjacent topics.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the resolution took more than 30 minutes to find, it must be captured.</li>
      <li>If the same symptom has occurred twice, capture it and link both tickets to the note.</li>
      <li>If the fix involves a workaround for a known system limitation, capture it and flag it as temporary.</li>
      <li>If the fix requires access to a restricted system or elevated authorization, document the approval process.</li>
      <li>If the knowledge applies to only one client or system, state that explicitly. Do not generalize without verification.</li>
      <li>If a runbook already exists for this topic, update the runbook rather than creating a separate note.</li>
      <li>If the root cause is a bug or defect that will be fixed in a patch, set the review date to the patch release date and plan to retire the note.</li>
      <li>If the knowledge involves a custom program or enhancement, include the program name and version.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Operational Knowledge Capture Note</strong> — The primary artifact. See the template below or the <a href="/skill-hub/artifact-templates/">Artifact Templates</a> page.</li>
      <li><strong>Updated Runbook or Wiki Page</strong> — If the knowledge fits an existing procedure, update it rather than creating a new document.</li>
      <li><strong>Knowledge Link in Ticket System</strong> — A comment or link in the resolved ticket pointing to the capture note for future reference.</li>
      <li><strong>Stakeholder Notification</strong> — A brief message to the business owner or data steward informing them that operational knowledge about their process has been documented.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Operational Knowledge Capture Note (compact)</h3>
    <pre><code>---
artifact: Operational Knowledge Capture Note
id: OKC-001
date: YYYY-MM-DD
author: Name
topic: Incident | Procedure | Workaround | Decision
---

## Situation
<!-- What was happening. Context, urgency, systems involved. -->

## Symptom
<!-- Exact error, behavior, or observation -->

## What was done
<!-- Step by step. Commands, transactions, settings. -->

## Why it worked
<!-- Causal explanation, not just description -->

## What was tried and failed
<!-- Dead ends, wrong paths, false assumptions -->

## What almost went wrong
<!-- Near misses or risks that were avoided -->

## Preconditions
<!-- When this knowledge applies and when it does not -->

## Limitations
<!-- What this procedure does not cover -->

## Verification
<!-- How to confirm the procedure is still valid -->

## Owner
<!-- Who maintains this knowledge -->

## Review date
<!-- When this note should be revalidated -->

## Related knowledge
<!-- Links to other capture notes, runbooks, tickets, Atlas pages -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The note was written within 24 hours of incident resolution.</li>
      <li>The symptom is described with exact error text, transaction, and at least one example record ID.</li>
      <li>The resolution steps are numbered and include exact transaction codes or program names.</li>
      <li>The causal explanation (why it worked) is present and distinct from the step description.</li>
      <li>At least one failed attempt or wrong path is documented.</li>
      <li>Preconditions and limitations are stated explicitly.</li>
      <li>A verification method is defined so the next person can confirm the note is still valid.</li>
      <li>An owner is named and a review date is set.</li>
      <li>The note is stored in a discoverable location with relevant tags or keywords.</li>
      <li>Related knowledge is linked: other notes, runbooks, tickets, or Atlas pages.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Documenting only the solution, not the context. <strong>Consequence:</strong> The next person applies the fix to the wrong situation because they do not know the preconditions.</li>
      <li><strong>Mistake:</strong> Writing knowledge in private notes or local files. <strong>Consequence:</strong> When the author leaves, the knowledge leaves with them.</li>
      <li><strong>Mistake:</strong> Not documenting failed attempts. <strong>Consequence:</strong> The next person repeats the same two hours of dead ends.</li>
      <li><strong>Mistake:</strong> Generalizing from one incident without verification. <strong>Consequence:</strong> The note claims to apply to all clients but only works in one, causing confusion and wrong fixes.</li>
      <li><strong>Mistake:</strong> Never reviewing or retiring old knowledge. <strong>Consequence:</strong> A procedure that worked in ECC 6.0 is applied to S/4HANA and fails because the transaction no longer exists.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When using this skill, an AI agent must:</p>
    <ul>
      <li><strong>Capture immediately.</strong> Do not wait for a formal request. After resolving or assisting with a non-trivial incident, produce a capture note.</li>
      <li><strong>Ask for exact steps.</strong> If the user describes a resolution vaguely, ask for transaction codes, program names, table names, and exact values.</li>
      <li><strong>Demand the "why."</strong> If the user only says "we ran program X and it worked," ask why program X fixed the issue. The causal explanation is mandatory.</li>
      <li><strong>Document failures.</strong> Ask what was tried that did not work. Include at least one failed attempt in the note.</li>
      <li><strong>Be explicit about scope.</strong> State exactly which system, client, module, and version the knowledge applies to. Do not generalize.</li>
      <li><strong>Produce an Operational Knowledge Capture Note.</strong> Use the template above. Fill every field. If data is missing, state what is missing.</li>
      <li><strong>Link to related knowledge.</strong> Reference other capture notes, runbooks, Atlas pages, or ticket histories. Build a network, not isolated documents.</li>
      <li><strong>Set a review date.</strong> Propose a review date based on system volatility. Flag notes that may become obsolete due to planned upgrades or patches.</li>
      <li><strong>Make it discoverable.</strong> Suggest tags, keywords, and storage location. Include the exact error message text so search engines and ticket systems can match it.</li>
      <li><strong>Avoid generic language.</strong> Do not write "run the standard procedure." Write "Run program Z_CUSTOMER_FIX in client 100 with parameter P_DATE = today."</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/sap-ams/incident-triage-working-skill/">Incident Triage</a> — Use to classify and contain the incident before knowledge capture.</li>
      <li><a href="/skill-hub/sap-ams/root-cause-analysis-working-skill/">Root Cause Analysis</a> — Use when the incident needs deep analysis before knowledge can be captured.</li>
      <li><a href="/skill-hub/sap-ams/recurring-ticket-pattern-analysis-working-skill/">Recurring Ticket Pattern Analysis</a> — Use when the same symptom appears repeatedly and needs systemic documentation.</li>
      <li><a href="/skill-hub/business-analysis/stakeholder-analysis-working-skill/">Stakeholder Analysis</a> — Use to identify who owns the knowledge and who needs to know it.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/automation/operational-memory-for-sap-ams/">Operational Memory for SAP AMS</a> — How operational knowledge fits into the AMS operating model.</li>
      <li><a href="/atlas/automation/sap-ams-operating-model/">SAP AMS Operating Model</a> — The broader context for knowledge capture in AMS.</li>
      <li><a href="/atlas/ai-operations/ai-ready-process-documentation/">AI-Ready Process Documentation</a> — How to structure knowledge so AI agents can use it.</li>
      <li><a href="/atlas/ai-operations/ai-agent-for-sap-support/">AI Agent for SAP Support</a> — How AI agents consume operational knowledge.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of knowledge management practice. It is not official SAP or ITIL documentation. The effectiveness of knowledge capture depends heavily on organizational culture: if there is no shared repository or no time allocated for documentation, the skill cannot overcome those barriers. The skill assumes the user has access to a ticket system, wiki, or knowledge base. Some operational knowledge involves proprietary or client-specific procedures that cannot be shared in public repositories.</p>
  </section>
</article>
