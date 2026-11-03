---
layout: default
title: "SAP Workflow Diagnostics"
description: "Troubleshoot SAP Business Workflow work items in ERROR, STARTED, or In Process: SWIA, SWPC, SWPR, runtime checks, and safe MDG change request recovery."
last_modified_at: 2026-11-03
permalink: /atlas/diagnostics/sap-workflow-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: SAP operations
concept_type: diagnostic guide
sap_area: "Workflow (SWF_* )"
business_process: Workflow operations
status: needs_verification
verified: false
level: 1
author: Dzmitryi Kharlanau
tags:
  - diagnostics
  - sap-ams
  - workflow
related:
  - /atlas/diagnostics/sap-background-job-diagnostics/
  - /atlas/diagnostics/sap-application-log-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Workflow Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP workflow diagnostics</h1>
    <p class="note-subtitle">Find the work item, distinguish a runtime interruption from a task error, and recover safely with SWIA, SWPC, or SWPR.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Workflow operations</dd></div>
      <div><dt>SAP area</dt><dd>Workflow (SWF_* )</dd></div>
      <div><dt>Indexing</dt><dd>Noindex, review candidate</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>SAP Business Workflow routes approval and notification steps through tasks, agents, and deadlines. A workflow item can stall when an agent is missing, a rule fails, a background job is delayed, or a deadline passes without escalation. The diagnostic task is to locate the work item, read its error and agent determination logs, and decide whether the issue is organizational data, workflow definition, or runtime infrastructure.</p>
    <p>The workflow instance, its individual work items, and the underlying business object are three different states. A workflow can be <strong>STARTED</strong> while a background work item is shown as <strong>In Process</strong>; an MDG change request may have already changed business data. Do not infer one state from another. This guide is for classic SAP Business Workflow on ABAP systems, including applicable SAP MDG scenarios. Fiori flexible workflow administration and Cloud Public Edition have separate app actions and release-specific behavior.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>A user cannot see an expected approval item in SBWP or My Inbox.</li>
      <li>Work item status remains "ready" or "in process" for longer than the expected SLA.</li>
      <li>Deadline monitoring sends missed-deadline notifications repeatedly.</li>
      <li>Agent determination fails with "no agent found" or an empty recipient list.</li>
      <li>Workflow notification emails are not delivered or contain broken links.</li>
      <li>A completed workflow step does not trigger the next step.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing or incorrect agent:</strong> the responsible role, position, or user is not assigned, is locked, or has an invalid email address.</li>
      <li><strong>Rule resolution failure:</strong> an agent rule based on org structure or responsibility returns no result or an unexpected result.</li>
      <li><strong>Background job delay:</strong> the workflow background job SWWDHEX or SWWERRE is not running or is backlogged.</li>
      <li><strong>Deadline configuration:</strong> the deadline expression points to a missing container element or uses an incorrect offset.</li>
      <li><strong>Binding error:</strong> data passed between workflow steps does not match the expected container structure.</li>
      <li><strong>Workflow definition version mismatch:</strong> active work items reference an older version of the workflow.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>SWIA</strong> — workflow administration; inspect individual work items, technical logs, containers, and allowed administrative actions.</li>
      <li><strong>SWPC</strong> — continue a workflow after a runtime interruption or system crash, when its selection criteria apply.</li>
      <li><strong>SWPR</strong> — workflow restart after error, once the cause and existing business outcome are understood.</li>
      <li><strong>SWI1</strong> — work item selection; find work items by task, status, creation date, or business object.</li>
      <li><strong>SWU3</strong> — automatic workflow customizing; check runtime environment and consistency.</li>
      <li><strong>SWI2_DIAG</strong> — diagnosis of work items with errors or agent problems.</li>
      <li><strong>SBWP</strong> — shared workplace inbox; confirm what the user actually sees.</li>
      <li><strong>/IWFND/ERROR_LOG</strong> — for Fiori My Inbox errors triggered through Gateway.</li>
      <li><strong>SM58</strong> — relevant transactional RFC units and workflow RFC errors; no entry is not proof of a completed step.</li>
      <li><strong>SM37 / ST22 / SM21</strong> — workflow-related jobs, short dumps, and system log near the failure time.</li>
      <li><strong>SM12</strong> — application locks if an MDG activation or background task is blocked.</li>
      <li><strong>SLG1</strong> — process-specific application logs, when the relevant component writes them; choose the correct object and subobject.</li>
    </ul>

    <h2 id="workflow-recovery">Workflow error handling: SWIA, SWPC, or SWPR?</h2>
    <p><strong>Start with the exact status and the last successful checkpoint.</strong> A work item that is <em>In Process</em> is not automatically a work item in <em>ERROR</em>. Also distinguish a stuck background task from a top-level workflow that never created its next task.</p>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="SAP workflow symptom to recovery transaction decision table">
      <table class="study-table__table">
        <thead><tr><th scope="col">Observed symptom</th><th scope="col">First tool</th><th scope="col">Decision and caution</th></tr></thead>
        <tbody>
          <tr><td>One work item shows <strong>ERROR</strong>.</td><td><code>SWIA</code> for technical log; <code>SWPR</code> for controlled recovery.</td><td>Correct the cause and establish the original business outcome before restarting. SAP's error-restart report can also attempt to recreate the next item when no erroneous child item exists; that is not permission to restart blindly.</td></tr>
          <tr><td>Top-level workflow stays <strong>STARTED</strong> after a system crash; the preceding step completed and no new step is open.</td><td><code>SWIA</code> to verify the gap; then <code>SWPC</code> if eligible.</td><td>The classic SWPC report targets long-running started workflows (SAP describes those started for longer than a day). Confirm an interrupted transition rather than an ordinary waiting step.</td></tr>
          <tr><td>A background work item is <strong>In Process</strong> for too long.</td><td><code>SWIA</code>, then <code>SM58</code>, <code>ST22</code>, <code>SM21</code>, <code>SWU3</code>.</td><td>Inspect the actual task and runtime condition. The workflow might not appear in SWPC, and neither SWPC nor SWPR is a universal fix for an in-process task.</td></tr>
          <tr><td>Dialog task is <strong>READY</strong> but the approver sees nothing.</td><td><code>SWIA</code> / <code>SWI1</code> / <code>SWI2_DIAG</code>.</td><td>Check actual agents, possible agents, substitutes, responsibility rules, and inbox service. Do not replay a business step to correct routing.</td></tr>
          <tr><td>MDG approval finished, but activation or replication is missing.</td><td>MDG change request log and application-specific logs, then <code>SWIA</code>.</td><td>First establish whether activation already committed and whether replication is a separate failed stage. Avoid duplicate activation or outbound messages.</td></tr>
        </tbody>
      </table>
    </div>

    <h3>What each recovery transaction actually does</h3>
    <ul>
      <li><strong>SWIA — Work Item Administration:</strong> locate a specific work item and inspect its technical history. The available administrative actions depend on item type, state, authorizations, and system release. An option such as manually completing, replacing, or executing without an agent check changes workflow behavior; it is not the same as resuming the runtime after a crash.</li>
      <li><strong>SWPC — Continue Workflow After System Crash:</strong> find qualifying top-level workflows that stopped progressing after a system interruption and continue their runtime processing. It does not guarantee recovery of every background task labeled In Process.</li>
      <li><strong>SWPR — Workflow Restart After Error:</strong> find and restart workflow instances affected by an error after correction. SAP documents that the report restarts an erroneous dialog/background work item, or can attempt to generate the next work item if none is in error. Review the exact selection and log first.</li>
    </ul>
    <p><strong>Important exception:</strong> SAP KBA 3227538 describes a post-system-copy symptom where a background step stays In Process, tRFC appears successful, there is no short dump, and the top-level workflow cannot be found in SWPC. Absence from SWPC must trigger further diagnosis, not an arbitrary manual completion.</p>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>SWWUSERWI</strong> — user-specific work item assignments.</li>
      <li><strong>SWW_WI_STATUS</strong> — work item status transitions.</li>
      <li><strong>SWWWIHEAD</strong> — work item header data; use the supported workflow transactions for routine administration rather than changing database tables.</li>
      <li><strong>SWW_CONTOB</strong> — container elements for a work item.</li>
      <li><strong>Task TS*</strong> — standard workflow tasks referenced in the item.</li>
    </ul>

    <h2 id="in-process-runbook">Runbook: a work item remains In Process</h2>
    <ol>
      <li><strong>Identify the real business state.</strong> Record the affected process and document or MDG change request key, current business status, exact work item ID, workflow instance ID, client, time, and expected next step.</li>
      <li><strong>Follow the technical workflow history.</strong> In <code>SWIA</code> or <code>SWI1</code>, open the workflow and technical log. Look at the chronological view, last completed work item, active background step, error details, and container references. Do not assume that a work item displayed as In Process actually completed its business method.</li>
      <li><strong>Check the business application.</strong> In MDG, open the change request workflow log and show background steps. Inspect validation/activation evidence and active master data before considering a restart; replication to a downstream system is a distinct checkpoint.</li>
      <li><strong>Find the runtime cause.</strong> Correlate timestamps in <code>SM58</code>, <code>ST22</code>, <code>SM21</code>, relevant <code>SM37</code> jobs, and <code>SWU3</code> workflow runtime setup. Check <code>SM12</code> only if locks matter. Determine whether the task had a failing authorization, a dump, a waiting RFC, an unavailable system resource, or a business validation failure.</li>
      <li><strong>Choose the smallest supported action.</strong> For a verified error, correct the cause and consider <code>SWPR</code>. For a top-level STARTED workflow with a missing next step after interruption, inspect eligibility in <code>SWPC</code>. For a single In Process item with no confirmed error or interruption, investigate its runtime and task implementation with the workflow/Basis owner before any SWIA administrative intervention.</li>
      <li><strong>Use one controlled recovery.</strong> Capture the work item and its status before and after; record operator, approval, action, and timestamp. Do not simultaneously trigger multiple recovery paths or run them across a bulk selection without a tested scope.</li>
      <li><strong>Verify both layers.</strong> The workflow must reach its expected next step or completion, and the MDG change request must show the intended validation/approval/activation result. Check for duplicate effects, incorrect master data, and unexpected downstream messages before closing the incident.</li>
    </ol>

    <h2 id="mdg-example">Synthetic MDG example: approval completed, background step stuck</h2>
    <p>A change request has completed approval. Its next background work item, for example a status-setting or activation-related task, remains <strong>In Process</strong> and no new dialog step appears. The request is still open. This is an illustrative case, not a recorded customer incident.</p>
    <ol>
      <li>In the MDG change request workflow log, display background steps; then inspect the exact work item in SWIA.</li>
      <li>Read the step history and runtime checks before deciding whether execution was interrupted or the business method completed without workflow acknowledgement.</li>
      <li>Check relevant workflow runtime/RFC, application authorization, dump, lock, and activation evidence. The workflow background user and its required MDG authorizations are release-specific: examples include older <code>WF-BATCH</code> and newer <code>SAP_WFRT</code>; confirm the actual configured user rather than assuming either.</li>
      <li>If the business data has already been activated, do not repeat activation as a diagnostic shortcut. If it has not, choose a supported recovery path based on the actual work item/workflow state and obtain the responsible owner's approval.</li>
      <li>After recovery, compare the CR state, technical workflow log, activated objects, and any downstream replication evidence.</li>
    </ol>
    <details class="study-review">
      <summary>Practice decision: what if SWPC returns no workflow?</summary>
      <p>Do not conclude that SWPC is broken or that manual completion is safe. Confirm whether the top-level workflow meets SWPC's selection/age criteria; revisit the In Process background item in SWIA and the runtime evidence. SAP KBA 3227538 documents a scenario with no matching SWPC entry after a system copy. Escalate to the workflow/Basis owner with the technical work item, CR status, and supporting logs rather than creating a new approval or activation step by guesswork.</p>
    </details>

    <h2>Safe actions and common traps</h2>
    <ul>
      <li><strong>Safe first:</strong> read logs, resolve incorrect agents or authorizations, correct business validation, and confirm runtime setup. Forward a dialog work item only when the intended processor and governance rules allow it.</li>
      <li><strong>Recover only with evidence:</strong> restart an errored step, continue an interrupted workflow, or intervene through SWIA when the intended result and the existing business outcome have both been checked.</li>
      <li><strong>Avoid as shortcuts:</strong> manually complete or logically delete a background task, use Execute Without Check, restart all work items, or repeat MDG activation without reconciliation. Those actions can skip controls or duplicate side effects.</li>
    </ul>

    <h2>Official SAP references</h2>
    <ul>
      <li><a href="https://help.sap.com/docs/SAP_NETWEAVER_702/fe1eec266c551014a965feb5b6d5dade/4f257c69e85a18c3e10000000a421937-1202.html">SAP Help: Workflow Runtime Administration</a> — classic crash continuation and runtime tools.</li>
      <li><a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/4400bdc8dd4648a5a2e5c1c8e05198d7/4f2564418bfb18c4e10000000a421937.html">SAP Help: Restarting Workflows After Errors</a> — how the error-restart report processes child work items.</li>
      <li><a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/a602ff71a47c441bb3000504ec938fea/4f2c69040428435ee10000000a421937.html">SAP Help: Changing Work Items</a> — manual administrative state changes and restart conditions.</li>
      <li><a href="https://help.sap.com/docs/SAP_MASTER_DATA_GOVERNANCE/db97296fe85d45f9b846e8cd2a580fbd/c39fd020cc704b3f85d142804ae9f792.html">SAP Help: MDG Workflow Log</a> — display background steps and access the technical log.</li>
      <li><a href="https://userapps.support.sap.com/sap/support/knowledge/en/3227538">SAP KBA 3227538</a> — a post-system-copy In Process background-step symptom that may not appear in SWPC (full KBA may require SAP support access).</li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/df79cc5284084a4ee10000000a423f68.html">SAP Help: MDG Rule-Based Workflow</a> — background user and activation considerations; details vary by release.</li>
    </ul>
    <p>Sources consulted 3 November 2026. Commands and recovery actions must be checked against the installed SAP release and change-control process. This guide remains a noindex review candidate, not an SAP-certified procedure.</p>

    <h2>What to capture first</h2>
    <p>Capture the workflow template, task number, work item ID, top-level workflow ID, affected business object key, current MDG change request status where applicable, expected and actual next step, precise timestamps, status history, background user, technical error text, and proof of whether the business method already committed. Record the affected scope and recovery approval in the incident, without exposing confidential identifiers on public pages.</p>

    <h2>Escalation signals</h2>
    <ul>
      <li>Multiple work items are stuck across different templates at the same time.</li>
      <li>Agent rules consistently return no agents for an entire org unit.</li>
      <li>Workflow runtime jobs are failing with short dumps in ST22.</li>
      <li>My Inbox is unavailable for many users and Gateway error logs show systemic failures.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page covers classic SAP Business Workflow troubleshooting. It is not a workflow design manual, a promise that every runtime error is recoverable through SWIA/SWPC/SWPR, or a replacement for release-specific SAP support instructions. Flexible workflow in SAP S/4HANA Cloud may expose recovery through Fiori administration instead. Custom task logic, MDG rule-based process design, BRFplus routing, and organizational-management redesign require their own investigation.</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
