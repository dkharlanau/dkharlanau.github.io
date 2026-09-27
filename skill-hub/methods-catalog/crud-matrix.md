---
layout: default
title: "CRUD Matrix — Practical Data Responsibility Method"
description: "Use a CRUD matrix to map which process, capability, role, or system creates, reads, updates, and deletes business entities."
permalink: /skill-hub/methods-catalog/crud-matrix/
last_modified_at: 2026-09-27
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/methods-catalog/">Methods &amp; Frameworks</a></li>
    <li aria-current="page">CRUD Matrix</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Methods Catalog — Data &amp; Systems</p>
  <h1>CRUD Matrix</h1>
  <p class="lead">Use a CRUD matrix when data ownership and system responsibility are unclear. It shows who creates, reads, updates, or deletes an entity across processes or systems.</p>

  <section>
    <h2>What this method is for</h2>
    <p>CRUD stands for <strong>Create, Read, Update, Delete</strong>. A matrix places business entities on one axis and processes, capabilities, systems, or roles on the other. Each cell records which operations occur.</p>
    <p>The value is in anomalies: two systems both create the same master object, a process updates data it does not own, an interface reads a field that has no reliable source, or a deletion responsibility is missing.</p>
  </section>

  <section>
    <h2>When to use it</h2>
    <ul>
      <li>A target architecture needs to define system-of-record responsibilities.</li>
      <li>Master data is changed in several systems and conflicts appear.</li>
      <li>An interface design is missing source/target ownership.</li>
      <li>A migration must identify which application owns each object after cutover.</li>
      <li>A privacy or retention requirement needs to know where deletion or anonymization occurs.</li>
    </ul>
  </section>

  <section>
    <h2>Choose the right matrix</h2>
    <div class="table-scroll">
      <table class="study-table">
        <thead><tr><th>Rows</th><th>Columns</th><th>Use it to answer</th></tr></thead>
        <tbody>
          <tr><td>Business entities</td><td>Systems</td><td>Which system owns and manipulates each object?</td></tr>
          <tr><td>Business entities</td><td>Processes</td><td>Where in the lifecycle is data created or changed?</td></tr>
          <tr><td>Business entities</td><td>Capabilities</td><td>Which capability needs which data operations?</td></tr>
          <tr><td>Business entities</td><td>Roles</td><td>Which business role is allowed to perform which data operation?</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Define business entities.</strong> Customer, Business Partner, Material/Product, Sales Order, Delivery, Invoice, Purchase Order.</li>
      <li><strong>Choose the second dimension.</strong> Systems for architecture, processes for lifecycle analysis, roles for governance.</li>
      <li><strong>Populate observed CRUD operations.</strong> Use evidence from interfaces, process steps, authorizations, configuration, and data lineage.</li>
      <li><strong>Mark the authoritative owner separately.</strong> CRUD alone does not mean system of record.</li>
      <li><strong>Find duplicate Create/Update authority.</strong> Decide whether it is intentional synchronization or uncontrolled multi-master behavior.</li>
      <li><strong>Find missing lifecycle operations.</strong> Who deactivates, archives, deletes, or anonymizes?</li>
      <li><strong>Trace cross-system operations into interfaces.</strong> A read/update relationship often implies data movement or API/event requirements.</li>
      <li><strong>Validate with data and system owners.</strong></li>
    </ol>
  </section>

  <section>
    <h2>SAP example — Business Partner across landscape</h2>
    <div class="table-scroll">
      <table class="study-table">
        <thead><tr><th>Entity</th><th>MDG</th><th>S/4HANA</th><th>CRM</th><th>Data Platform</th></tr></thead>
        <tbody>
          <tr><td>Business Partner core</td><td>C/R/U</td><td>R</td><td>R</td><td>R</td></tr>
          <tr><td>Sales-area extension</td><td>C/R/U</td><td>R</td><td>R</td><td>R</td></tr>
          <tr><td>CRM engagement attributes</td><td>R</td><td>R</td><td>C/R/U</td><td>R</td></tr>
          <tr><td>Deletion / block status</td><td>U</td><td>R</td><td>R</td><td>R</td></tr>
        </tbody>
      </table>
    </div>
    <p>The matrix should then record which system is authoritative for each attribute group and how updates propagate. A simple “all systems update customer data” answer is a governance warning.</p>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If two systems both Create or Update the same authoritative attribute, define conflict and synchronization rules explicitly.</li>
      <li>If a system has U but no business ownership, investigate unauthorized or technical-only mutation.</li>
      <li>If no system owns deletion, blocking, retention, or anonymization, the lifecycle is incomplete.</li>
      <li>If a system only reads replicated data, do not call it the system of record.</li>
      <li>If CRUD relationships cross a system boundary, continue with <a href="/skill-hub/systems-analysis/interface-requirement-analysis-working-skill/">Interface Requirement Analysis</a>.</li>
      <li>If the overall system boundary is unclear, use <a href="/skill-hub/architecture/system-context-mapping-working-skill/">System Context Mapping</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Copy-ready template</h2>
    <pre><code>Legend: C=create, R=read, U=update, D=delete/deactivate

| Entity / Attribute Group | System A | System B | System C | Authoritative Owner | Sync / Interface | Notes |
|---|---|---|---|---|---|---|
| &lt;entity&gt; | CRU | R | R | &lt;system/role&gt; | &lt;event/API/file&gt; | ... |

## Anomalies
- Multiple create/update:
- Missing delete/deactivate:
- Read without reliable source:
- Update without clear owner:
- Conflicting system-of-record claim:

## Follow-up
- Interface requirement:
- Data governance decision:
- Migration rule:
- Retention/privacy rule:</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Entities are business objects, not database tables only.</li>
      <li>CRUD assignments are evidence-based.</li>
      <li>Authoritative ownership is recorded separately.</li>
      <li>Duplicate C/U rights are reviewed.</li>
      <li>End-of-life operations are considered.</li>
      <li>Cross-system CRUD relationships lead to interface or lineage analysis.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Calling every read replica a master.</strong> Read access does not define authority.</li>
      <li><strong>Working only at table level.</strong> Technical tables can hide the business object and ownership model.</li>
      <li><strong>Ignoring attribute groups.</strong> One system may own core customer data while another owns channel-specific attributes.</li>
      <li><strong>Using “D” only as physical deletion.</strong> Enterprise systems often use blocking, archiving, or anonymization instead.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>An AI agent should extract only evidenced CRUD operations, distinguish operation from authority, flag multi-master patterns, and preserve unknown cells as unknown. It should not infer system-of-record status from where data happens to be visible.</p>
  </section>

  <section>
    <h2>Related skills and methods</h2>
    <ul>
      <li><a href="/skill-hub/systems-analysis/interface-requirement-analysis-working-skill/">Interface Requirement Analysis</a></li>
      <li><a href="/skill-hub/architecture/system-context-mapping-working-skill/">System Context Mapping</a></li>
      <li><a href="/skill-hub/dama-dmbok/master-data-management-working-skill/">Master Data Management</a></li>
      <li><a href="/skill-hub/dama-dmbok/data-lineage-working-skill/">Data Lineage</a></li>
      <li><a href="/skill-hub/integration-architecture/interface-ownership-working-skill/">Interface Ownership</a></li>
    </ul>
  </section>

  <section>
    <h2>Status and limitations</h2>
    <p>A CRUD matrix is a compact responsibility view, not a complete data model, authorization design, lineage model, or interface specification. Use it to expose responsibility questions and then route those questions to the right deeper skill.</p>
  </section>
</article>