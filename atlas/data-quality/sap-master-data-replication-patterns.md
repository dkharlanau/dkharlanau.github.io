---
layout: default
title: "SAP Master Data Replication Patterns"
description: "How master data replicates across SAP systems, where the chain breaks, and what evidence to collect first."
permalink: /atlas/data-quality/sap-master-data-replication-patterns/
atlas_section: data-quality
domain: Data operations
subdomain: Master data distribution
concept_type: data quality
sap_area: MDG / ALE / IDoc / replication
business_process: Cross-process operations
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
tags:
  - master-data
  - data-quality
  - replication
  - integration
  - idoc
related:
  - /atlas/data-quality/sap-mdg-governance-patterns/
  - /atlas/diagnostics/idoc-aif-integration-diagnostics/
  - /atlas/data-quality/sap-master-data-quality/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/data-quality/">Data Quality</a></li>
    <li aria-current="page">SAP Master Data Replication Patterns</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Data Quality Note</p>
    <h1>SAP master data replication patterns</h1>
    <p class="note-subtitle">Trace how master data moves across systems, why it stops, and how to narrow the failure to the right layer.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Cross-process operations</dd></div>
      <div><dt>SAP area</dt><dd>MDG / ALE / IDoc / replication</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Master data replication is not a single pipeline. It is a set of technologies — ALE/IDoc, SLT, MDG distribution, APIs, and CVI synchronization — each with its own failure modes. A useful diagnostic does not assume the technology; it confirms which path the record took, where it stopped, and whether the failure is structural or transient.</p>

    <h2>Key sections</h2>

    <h3>ALE/IDoc distribution</h3>
    <p>The classic SAP method: a change triggers an IDoc that is sent to partner systems via a distribution model. Common breakpoints:</p>
    <ul>
      <li>IDoc stuck in status 64 (not passed to application) because the processing function is not scheduled or is failing.</li>
      <li>IDoc in status 51 (application error) because the target system rejects the segment content or master data is missing.</li>
      <li>Filter object in the distribution model excludes the record based on company code, plant, or other criteria the user did not expect.</li>
      <li>Segment missing in the distribution model for the message type, so the IDoc arrives incomplete.</li>
    </ul>

    <h3>SLT (SAP Landscape Transformation)</h3>
    <p>SLT replicates table-level changes in near real time. It is often used for analytics or sidecar systems. In master data contexts, watch for:</p>
    <ul>
      <li>Table-level replication does not enforce business rules, so a replicated record may be technically present but logically incomplete.</li>
      <li>Transformation rules that mask, rename, or filter fields can create mismatches between source and target.</li>
      <li>Replication latency: the target system queries data before SLT has finished the initial load or caught up with deltas.</li>
    </ul>

    <h3>MDG distribution</h3>
    <p>MDG activates a record and then distributes it to connected systems. Failures here are often silent to the end user:</p>
    <ul>
      <li>Distribution model missing a target system for the entity type.</li>
      <li>Key mapping failure: the MDG key does not resolve to the target system key.</li>
      <li>Partial distribution: header arrives, but organizational views or relationships do not.</li>
    </ul>

    <h3>API-based replication</h3>
    <p>Modern landscapes use OData or SOAP APIs to push or pull master data. Failures tend to be protocol-level or mapping-level:</p>
    <ul>
      <li>API consumer not authorized for the entity set or field.</li>
      <li>Payload structure does not match the API metadata, especially after an upgrade or patch.</li>
      <li>Batch size or timeout limits cause partial success: some records created, others not.</li>
    </ul>

    <h3>Business Partner synchronization (CVI)</h3>
    <p>Customer/Vendor Integration (CVI) synchronizes the Business Partner object with customer and vendor master records. This is a frequent source of replication-like symptoms:</p>
    <ul>
      <li>Business Partner created, but customer or vendor not generated because CVI mapping is incomplete.</li>
      <li>Direction setting (BP to customer, customer to BP, or both) causes unexpected overwrites.</li>
      <li>Number range or grouping mismatch prevents synchronization.</li>
    </ul>

    <h2>Common breakpoints</h2>
    <ul>
      <li><strong>IDoc status 64 or 51:</strong> check WE02/WE05 for the error segment, then BD87 for status monitor details.</li>
      <li><strong>Filter mismatch:</strong> verify the distribution model filter objects against the actual organizational values in the record.</li>
      <li><strong>Key mapping failure:</strong> confirm that the source and target systems agree on the identifier, especially after system copies or mergers.</li>
      <li><strong>Segment missing:</strong> review the distribution model for the message type and compare with the IDoc segment list.</li>
      <li><strong>Timing issues:</strong> the target system processes a transaction before the master data replication completes. This is common in high-velocity or parallel landscapes.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the replication path: ALE, SLT, MDG, API, or CVI.</li>
      <li>Confirm whether the source record is complete and active.</li>
      <li>Check the transport layer: IDoc status, SLT job log, MDG distribution log, or API response.</li>
      <li>Inspect the target system: is the record missing entirely, partially present, or present but with different values?</li>
      <li>Determine if the failure is isolated to one object, one system, one message type, or one time window.</li>
      <li>Look for recent changes: distribution model edits, filter updates, system copies, or master data model changes.</li>
    </ol>

    <h2>Key transactions</h2>
    <ul>
      <li><strong>BD10</strong> — send master data object (customer, vendor, material) manually.</li>
      <li><strong>BD12</strong> — send customer or vendor via ALE.</li>
      <li><strong>WE02 / WE05</strong> — IDoc list and detailed display.</li>
      <li><strong>LTRC</strong> — SLT replication monitoring and configuration.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>A replication ticket should state the source system, target system, object type and key, expected result, actual result, and the replication method if known. "Customer missing in plant 1000" is not enough. Include whether an IDoc was generated, its status, and whether the record exists in the target with a different key or missing views.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page does not provide configuration instructions for ALE, SLT, MDG, or API replication. It does not cover every possible IDoc message type or custom interface. It does not replace SAP's official integration documentation.</p>

    <p><em>This is not official SAP documentation and not a replacement for system-specific analysis.</em></p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/data-quality/sap-mdg-governance-patterns/">SAP MDG Governance Patterns</a></li>
      <li><a href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">IDoc and AIF Integration Diagnostics</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
