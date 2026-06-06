---
layout: default
title: "SAP MDG Governance Patterns"
description: "Common SAP Master Data Governance patterns, failure modes, and diagnostic approach for AMS and support teams."
permalink: /atlas/data-quality/sap-mdg-governance-patterns/
atlas_section: data-quality
domain: Data operations
subdomain: Master data governance
concept_type: data quality
sap_area: MDG / master data governance
business_process: Cross-process operations
status: needs_verification
verified: false
last_reviewed: 2026-06-09
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
    <p class="note-subtitle">How MDG organizes master data creation, change, validation, and distribution — and where that chain breaks in real operations.</p>
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
    <h2>Core idea</h2>
    <p>SAP Master Data Governance (MDG) is not just a data-quality tool. It is a workflow and ownership layer that sits between business requesters and the operational systems that consume master data. When MDG works, bad records are caught before distribution. When it fails, the same defects propagate to every target system and generate parallel support tickets.</p>

    <h2>Key sections</h2>

    <h3>Central governance vs. federated</h3>
    <p>In central governance, one MDG instance owns creation and change for all systems. This gives consistency but creates a bottleneck if workflow steps are too granular or approvers are unavailable. Federated governance allows local teams to maintain certain attributes or organizational extensions, but risks divergence if validation rules differ across regions. In practice, many landscapes are hybrid: central for financial and classification attributes, federated for plant-level extensions.</p>

    <h3>Change request workflows</h3>
    <p>A change request (CR) in MDG moves master data through staging, validation, approval, and activation. Common friction points:</p>
    <ul>
      <li>CR stuck in approval because the responsible agent is not assigned or is out of office.</li>
      <li>Multiple CRs for the same object create conflicts in the staging area.</li>
      <li>Users create a new CR instead of editing an existing one, producing duplicates.</li>
      <li>Workflow variant is too rigid for urgent operational changes (e.g., a blocked supplier that prevents goods receipt).</li>
    </ul>

    <h3>Data quality rules and duplicate check</h3>
    <p>MDG can enforce validation rules at entry time: mandatory fields, format checks, and matching against existing records. Two common misconfigurations:</p>
    <ul>
      <li><strong>Too strict:</strong> rules reject valid but non-standard entries, forcing users to bypass MDG or overload support.</li>
      <li><strong>Too loose:</strong> duplicates slip through because matching thresholds are set low or key fields are excluded from the check.</li>
    </ul>
    <p>Duplicate check should cover name, address, tax number, and industry-specific identifiers. If the check runs only after staging, the cost of correction is higher.</p>

    <h3>Distribution to target systems</h3>
    <p>Once a record is activated in MDG, it must reach the operational systems where it is used. Distribution can use IDoc, WebService, or RFC. Failures here are often invisible to the business user until a downstream transaction blocks:</p>
    <ul>
      <li>Distribution model missing a target system or message type.</li>
      <li>Key mapping between MDG and target system is inconsistent.</li>
      <li>Target system is temporarily unavailable and the queue is not monitored.</li>
      <li>Partial distribution: some views arrive, others do not, leaving the record incomplete in the target.</li>
    </ul>

    <h3>Staging area confusion</h3>
    <p>The staging area holds data that is not yet active. Users and support sometimes expect to see a record in the target system before it has been approved and activated. A clear handoff between "staging visible" and "distributed active" prevents false escalations.</p>

    <h2>Common failure modes</h2>
    <ul>
      <li><strong>Workflow bottlenecks:</strong> approval queues grow because roles are not staffed or escalation rules are missing.</li>
      <li><strong>Validation mismatch:</strong> MDG rules differ from the target system's own checks, so a record passes MDG but fails in ERP.</li>
      <li><strong>Ownership gaps:</strong> the MDG team manages workflow configuration; the business owns data content; neither owns end-to-end quality. Result: recurring defects.</li>
      <li><strong>Distribution silence:</strong> errors in distribution are not surfaced to the requester, so the first signal is a blocked sales order or purchase order days later.</li>
    </ul>

    <h2>Diagnostic questions</h2>
    <ul>
      <li>Is the record active in MDG, still in staging, or failed in distribution?</li>
      <li>Which workflow step is the CR waiting on, and is the agent assigned?</li>
      <li>Does the validation error reflect a real data problem, or a rule that is too strict for the business context?</li>
      <li>Is the failure isolated to one object, one target system, one message type, or one time window?</li>
      <li>Who is accountable for fixing the record, and who is accountable for fixing the rule or workflow?</li>
    </ul>

    <h2>Key transactions</h2>
    <ul>
      <li><strong>USMD_CREQUEST</strong> — change request monitor and processing.</li>
      <li><strong>USMD_EDITION</strong> — data model and edition management.</li>
      <li><strong>USMD_DSP</strong> — distribution status and error logs.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>When a master data issue reaches AMS, first determine whether the problem is in the data itself, the MDG workflow, or the distribution layer. Fixing the record without checking the workflow or distribution model guarantees a repeat ticket. A useful MDG incident should include: the change request number, the object type and ID, the workflow step where it stopped, and whether the record is visible in the target system.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page does not provide step-by-step MDG configuration instructions. It does not cover every possible distribution technology or custom workflow variant. It does not replace SAP's official MDG documentation or system-specific analysis.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/data-quality/master-data-governance-failure-modes/">Master Data Governance Failure Modes</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-replication-patterns/">SAP Master Data Replication Patterns</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
