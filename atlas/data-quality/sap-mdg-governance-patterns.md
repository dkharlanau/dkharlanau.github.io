---
layout: default
title: "SAP MDG Governance Patterns"
description: "How SAP Master Data Governance moves a change from request to activation and replication, and how to locate failures in that chain."
permalink: /atlas/data-quality/sap-mdg-governance-patterns/
atlas_section: data-quality
domain: Data operations
subdomain: Master data governance
concept_type: data quality
sap_area: MDG / master data governance
business_process: Cross-process operations
status: needs_verification
verified: false
last_reviewed: 2026-09-23
last_modified_at: 2026-09-23
author: Dzmitryi Kharlanau
tags:
  - master-data
  - data-quality
  - mdg
  - governance
related:
  - /atlas/data-quality/master-data-governance-failure-modes/
  - /atlas/data-quality/sap-master-data-quality/
  - /atlas/data-quality/sap-master-data-replication-patterns/
  - /atlas/sap/sap-mdg/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/data-quality/">Data Quality</a></li>
    <li aria-current="page">SAP MDG Governance Patterns</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Data Quality Note</p>
    <h1>SAP MDG governance patterns</h1>
    <p class="note-subtitle">The useful question in an MDG incident is not simply whether the record exists. It is which governance state the change reached, and where the chain stopped.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Cross-process operations</dd></div>
      <div><dt>SAP area</dt><dd>MDG / master data governance</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Read MDG as a sequence of states</h2>
    <p>In SAP Master Data Governance, a proposed change and an active master record are deliberately different states. In a typical central-governance flow, a user creates a change request, the changed data is stored in the MDG staging area, checks and workflow actions are performed, and approved data is written to the active area. Distribution to other systems is a further step.</p>

    <p>That gives us a practical operating model:</p>

    <p><strong>request → staging → checks → workflow decision → activation → active data → replication → target acceptance</strong></p>

    <p>Most support confusion comes from collapsing two or more of these states into one. A change request can be approved but not active. A record can be active in the MDG hub but absent from a target system. A target can receive a message and still reject the business data. Each state needs different evidence.</p>

    <h2>Workflow controls who can act next</h2>
    <p>A change request status is not only a label. SAP MDG configuration determines which processing options are allowed for a status, while workflow moves the request through the configured steps. Open change requests can also interlock the contained data to protect it from conflicting processing by another open request.</p>

    <p>When a request appears “stuck”, first separate workflow from data quality. If the data is valid but no useful action is available, the problem may be in workflow routing, agent determination, step configuration, or status. Changing master data fields will not repair that control flow.</p>

    <h2>Checks do not all have the same meaning</h2>
    <p>MDG can perform several kinds of checks during change-request processing. SAP documents required-field and validity checks as activation-relevant: if these checks return errors, the change request cannot be activated until the errors are resolved. Validation rules can also be assigned to change-request processes through the relevant configuration.</p>

    <p>Duplicate checking has a different role. The standard duplicate check identifies potential matches and warns the user; the user may still decide to continue with creation. A duplicate record therefore does not automatically prove that the duplicate-check function failed. We need to know which search method and thresholds were configured, what candidates were returned, and what decision the process allowed the user to make.</p>

    <h2>Approval, activation, and replication are separate boundaries</h2>
    <p>An approval means the workflow accepted the proposed change. Activation means the accepted data was written to the active area. Replication then moves active master data to connected systems according to the configured integration model. Treating those three events as one “successful MDG change” makes downstream failures difficult to locate.</p>

    <p>The replication technology is also object- and landscape-specific. For example, current SAP documentation for Business Partner replication from MDG states that ALE can be used, but recommends SOA-based replication when the target is SAP S/4HANA because ALE does not cover all Business Partner-related attributes. That is a useful reminder not to assume one universal MDG distribution path.</p>

    <h2>Use the visible state to choose the next evidence</h2>
    <div class="decision-table">
      <table>
        <thead>
          <tr><th>Observed state</th><th>Likely boundary</th><th>Evidence that matters next</th></tr>
        </thead>
        <tbody>
          <tr><td>Change request exists but no one can progress it</td><td>Workflow or status</td><td>Current step, permitted actions, agent or responsibility assignment, and status history.</td></tr>
          <tr><td>Request is approved but activation does not complete</td><td>Validation or activation</td><td>Validation log, required-field or consistency errors, and the object state in staging.</td></tr>
          <tr><td>Record is active in MDG but missing from one target</td><td>Replication</td><td>Replication model, target selection, outbound processing, message status, and target response.</td></tr>
          <tr><td>Record exists in the target but is unusable there</td><td>Target acceptance or scope</td><td>Which attributes, relationships, or organizational data arrived and which target checks rejected or ignored them.</td></tr>
          <tr><td>A likely duplicate was created</td><td>Duplicate-check design or decision</td><td>Configured search method, threshold, candidate list, and whether the process allowed the user to continue.</td></tr>
        </tbody>
      </table>
    </div>

    <h2>Do not repair the wrong layer</h2>
    <p>A local correction in a target system can restore a business process, but it may also create a new inconsistency if MDG remains the governed source. Before changing the target, establish whether the source record is wrong, the governed change never became active, the replication path failed, or the target interpreted the data differently.</p>

    <p>The same discipline applies to workflow incidents. Reassigning one request may clear today's queue without fixing the routing rule that will block tomorrow's requests. A useful incident closes both questions: <em>how do we restore the current process?</em> and <em>which control allowed the same failure mode to exist?</em></p>

    <h2>A compact MDG support trace</h2>
    <p>For a concrete object, trace the change in this order:</p>
    <ol>
      <li><strong>Identify the change request and requested business change.</strong> Confirm the object, organizational scope, expected result, and current request status.</li>
      <li><strong>Inspect the staged data.</strong> Establish whether the requested values are present before investigating distribution.</li>
      <li><strong>Read the checks and workflow state.</strong> Distinguish a data error from a routing or approval problem.</li>
      <li><strong>Confirm activation.</strong> Do not infer active data from an approval alone.</li>
      <li><strong>Identify the replication path for this object and target.</strong> Check the configured model, filters, message processing, and acknowledgements rather than assuming ALE, SOA, or another mechanism.</li>
      <li><strong>Confirm the target business state.</strong> A technically delivered message is not enough if the object is incomplete or unusable in the required organizational context.</li>
    </ol>

    <p>This page focuses on the MDG runtime chain. Broader ownership, system-of-record, retirement, and feedback-loop failures are covered in <a href="/atlas/data-quality/master-data-governance-failure-modes/">Master Data Governance Failure Modes</a>; replication technologies and transport-layer evidence are covered in <a href="/atlas/data-quality/sap-master-data-replication-patterns/">SAP Master Data Replication Patterns</a>.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/77f5b94bdfcf4a2fa40d82098354fa11.html">Change Request Processing</a> — staging, checks, approval, and activation in central governance.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/87cf7c52b6f6856ae10000000a423f68.html">Configure Change Request Settings</a> — change-request statuses and permitted processing.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/4d523f354bf74b049cfd5f59aa56aac4.html">Duplicate Check</a> — duplicate candidates, scores, warning behavior, and user decision.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/3e034647df8746e1b459e8c37dc3b65d.html">Using Validation Rules</a> — validation-rule usage in change requests and other MDG processes.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/6fe343fea9b943f4875eb4425f19ed43.html">Data Replication of Business Partner Master Data Using ALE</a> — ALE support and SAP's SOA recommendation for replication to SAP S/4HANA.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Workflow steps, change-request types, validation logic, duplicate-check technology, activation behavior, and replication mechanisms vary by governed object, deployment, configuration, and SAP release. Verify the exact process in the target system before using this page as a configuration guide.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-mdg/">SAP MDG</a></li>
      <li><a href="/atlas/data-quality/master-data-governance-failure-modes/">Master Data Governance Failure Modes</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-replication-patterns/">SAP Master Data Replication Patterns</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
