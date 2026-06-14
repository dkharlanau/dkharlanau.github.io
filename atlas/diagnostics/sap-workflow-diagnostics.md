---
layout: default
title: "SAP Workflow Diagnostics"
description: "A conservative diagnostic frame for stuck workflow items, missing agents, deadlines, and workflow administration in SAP."
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
    <p class="note-subtitle">A first-pass structure for finding why workflow items are stuck, routed to the wrong agent, or missed their deadlines.</p>
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
    <p>This guide focuses on work items that are visible in the universal worklist or workflow inbox, not on custom workflow development or complex multi-step approval redesign.</p>

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
      <li><strong>SWIA</strong> — workflow administration; inspect work item status, agents, and execution log.</li>
      <li><strong>SWI1</strong> — work item selection; find work items by task, status, creation date, or business object.</li>
      <li><strong>SWU3</strong> — automatic workflow customizing; check runtime environment and consistency.</li>
      <li><strong>SWI2_DIAG</strong> — diagnosis of work items with errors or agent problems.</li>
      <li><strong>SBWP</strong> — shared workplace inbox; confirm what the user actually sees.</li>
      <li><strong>/IWFND/ERROR_LOG</strong> — for Fiori My Inbox errors triggered through Gateway.</li>
      <li><strong>SLG1</strong> — application log with object WORKFLOW for runtime errors.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>SWWUSERWI</strong> — user-specific work item assignments.</li>
      <li><strong>SWW_WI_STATUS</strong> — work item status transitions.</li>
      <li><strong>SWW_WI_2</strong> — work item header data.</li>
      <li><strong>SWW_CONTOB</strong> — container elements for a work item.</li>
      <li><strong>SWWWIHEAD</strong> — work item header archive.</li>
      <li><strong>Task TS*</strong> — standard workflow tasks referenced in the item.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the workflow template, task, and affected business object from the user report.</li>
      <li>Find the work item in SWI1 using selection criteria such as creation date, task, or object key.</li>
      <li>Open the work item in SWIA and read the agent list, container values, and execution log.</li>
      <li>If no agent is assigned, check the rule or org assignment in the workflow definition or HR organizational data.</li>
      <li>Run SWU3 to verify that workflow runtime jobs are scheduled and the runtime environment is consistent.</li>
      <li>Check SM37 for the status of workflow-related background jobs such as SWWDHEX and SWWERRE.</li>
      <li>Review SLG1 for workflow runtime errors around the time the item was created.</li>
      <li>For My Inbox issues, check /IWFND/ERROR_LOG and the Fiori app configuration.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Forward the work item to a valid agent or substitute in SWIA.</li>
      <li>Correct the org assignment, role, or responsibility rule that determines agents.</li>
      <li>Restart or complete the workflow background jobs if they are stuck or cancelled.</li>
      <li>Correct the deadline expression or container binding in the workflow builder if it is misconfigured.</li>
      <li>Ask the user to refresh the inbox or clear browser cache for Fiori My Inbox.</li>
      <li>Escalate to the workflow development team if the definition itself needs correction.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>Capture the workflow template, task number, work item ID, affected business object key, expected agent, actual agent, status, and any exact error text from SWIA or the inbox. Also record whether the issue is isolated to one user, one task, or a time window.</p>

    <h2>Escalation signals</h2>
    <ul>
      <li>Multiple work items are stuck across different templates at the same time.</li>
      <li>Agent rules consistently return no agents for an entire org unit.</li>
      <li>Workflow runtime jobs are failing with short dumps in ST22.</li>
      <li>My Inbox is unavailable for many users and Gateway error logs show systemic failures.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame for workflow runtime issues, not a guide to workflow design or SAP Business Workplace configuration. It does not cover complex custom binding logic, BRF+ rules, or HR organizational management redesign.</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
