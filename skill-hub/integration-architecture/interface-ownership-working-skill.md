---
layout: default
title: "Interface Ownership Working Skill"
description: "Assign clear ownership to every interface, document who decides what, and prevent failures from sitting unresolved because no one is responsible."
permalink: /skill-hub/integration-architecture/interface-ownership-working-skill/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/integration-architecture/">Integration Architecture</a></li>
    <li aria-current="page">Interface Ownership</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Integration Architecture</p>
  <h1>Interface Ownership Working Skill</h1>
  <p class="lead">Map every interface in your landscape to a named owner for business decisions, technical decisions, and operational response. Close ownership gaps before they become incidents.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>This skill helps you inventory all interfaces in a landscape, classify them by type and criticality, assign four distinct ownership roles per interface, document the ownership matrix, identify gaps, and establish a change process so ownership stays current.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>Post-merger or platform consolidation requires an interface cleanup.</li>
      <li>A new project is handing over integrations to AMS or operations.</li>
      <li>Recurring interface failures sit unresolved for days because teams point at each other.</li>
      <li>An audit finding notes missing governance or unclear responsibilities for integrations.</li>
      <li>A schema change breaks a consumer and no one knows who approved it.</li>
      <li>The AMS team receives alerts but does not know which business unit to contact for data validation.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Situation 1: IDoc failures sit unresolved</h3>
    <p>Customer master IDocs from SAP to a CRM are failing with status 51. The SAP basis team says the IDoc is correct. The CRM team says the data is wrong. The middleware team says the routing is fine. After three days, a sales manager complains that new customers cannot be created. No one was clearly responsible for end-to-end resolution.</p>
    <h3>Situation 2: Schema change without approval</h3>
    <p>A developer adds a mandatory field to a customer API to support a new project. Two downstream systems start failing because they do not send the new field. There is no documented owner who approves schema changes, so the developer assumed it was safe.</p>
    <h3>Situation 3: AMS team lacks business context</h3>
    <p>The AMS monitoring tool alerts on a failed file transfer. The AMS operator can see the technical error but does not know which business process is affected, who validates the file content, or whether the failure is urgent. The alert sits unactioned for hours.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Interface inventory: all known APIs, IDocs, RFCs, file transfers, events.</li>
      <li>System landscape diagram showing sources, targets, and middleware.</li>
      <li>Organizational chart or team directory.</li>
      <li>Existing SLAs or operational agreements.</li>
      <li>Incident history for the last 6–12 months (to find pain points).</li>
      <li>Middleware configuration: queues, topics, routing rules.</li>
      <li>Project documentation for recent or upcoming interfaces.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Who approves schema or format changes for this interface?</li>
      <li>Who is paged when this interface fails outside business hours?</li>
      <li>Who validates data quality at the source system?</li>
      <li>Who validates data quality at the target system?</li>
      <li>Who pays for middleware capacity increases for this interface?</li>
      <li>Who decides when this interface is deprecated?</li>
      <li>Who ensures the interface complies with security and privacy policies?</li>
      <li>What is the escalation path when the owner is unresponsive?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>List all interfaces.</strong> Gather from middleware, SAP (WE02, SM58, BD87), API gateways, file transfer logs, and project docs. Include active, dormant, and planned interfaces.</li>
      <li><strong>Classify by type and criticality.</strong> Tag each interface as API, IDoc, RFC, file, or event. Rate criticality by business impact: critical, major, minor, dormant.</li>
      <li><strong>Define four ownership roles per interface.</strong>
        <ul>
          <li><strong>Business owner:</strong> approves schema changes, validates semantics, decides deprecation.</li>
          <li><strong>Technical owner:</strong> designs and maintains the interface, approves implementation changes.</li>
          <li><strong>Operational owner:</strong> monitors, responds to alerts, performs first-line diagnosis.</li>
          <li><strong>Consumer representative:</strong> speaks for downstream consumers, validates compatibility.</li>
        </ul>
      </li>
      <li><strong>Document in ownership matrix.</strong> Record interface ID, source, target, direction, type, criticality, and all four owners. See template below.</li>
      <li><strong>Identify gaps.</strong> Flag interfaces with missing owners, conflicting claims, or owners who have left the organization.</li>
      <li><strong>Assign missing owners.</strong> For each gap, propose an owner based on domain, system, or incident history. Get written confirmation.</li>
      <li><strong>Define change process.</strong> Document how ownership is updated when systems change, teams reorganize, or projects end.</li>
      <li><strong>Validate with incident drill.</strong> Simulate a failure for a critical interface. Verify that the operational owner knows who to contact and that the business owner can make decisions.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If an interface has no business owner, assign one from the source data domain.</li>
      <li>If the operational owner is missing, default to the AMS or integration operations team.</li>
      <li>If a consumer is external or from another business unit, designate a consumer representative.</li>
      <li>If ownership is disputed between two teams, escalate to the architecture or governance board.</li>
      <li>If an interface is critical and unowned, treat it as a P1 risk and assign an interim owner within 24 hours.</li>
      <li>If an owner changes, update the matrix within 48 hours and notify all stakeholders.</li>
      <li>If an interface has no consumer for 12 months, initiate deprecation review with the business owner.</li>
      <li>If an interface crosses legal entities or countries, assign a compliance owner in addition to the four standard roles.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Interface Ownership Matrix</strong> — All interfaces with owners and criticality. Link to <a href="/skill-hub/artifact-templates/">Interface Ownership Matrix template</a>.</li>
      <li><strong>Ownership Gap Report</strong> — Missing owners, risks, and assignment actions.</li>
      <li><strong>RACI for Interface Changes</strong> — Who is responsible, accountable, consulted, informed for schema, infra, and deprecation changes.</li>
      <li><strong>Runbook for Ownership Updates</strong> — How to update the matrix when teams or systems change.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Interface Ownership Matrix (Compact)</h3>
    <pre><code>---
artifact: Interface Ownership Matrix
id: IOM-001
date: YYYY-MM-DD
scope: System landscape | Project | Domain
---

## Interfaces

| Interface ID | Source | Target | Direction | Type | Criticality | Business Owner | Technical Owner | Operational Owner | Consumer Rep | SLA | Status |
|--------------|--------|--------|-----------|------|-------------|----------------|-----------------|-------------------|--------------|-----|--------|
| IF-001 | SAP S/4 | Salesforce | Outbound | API | Critical | MDM Lead | Integration Lead | AMS Team | CRM Lead | 4h | Active |
| IF-002 | SAP S/4 | Warehouse | Outbound | IDoc | Major | Logistics Mgr | SAP Dev | AMS Team | WH Ops | 8h | Active |
| IF-003 | Bank | SAP S/4 | Inbound | File | Critical | Finance Mgr | SAP Dev | AMS Team | Treasury | 2h | Active |

## Ownership gaps

| Interface ID | Missing Role | Risk | Action | Assignee | Due Date |
|--------------|--------------|------|--------|----------|----------|
| IF-004 | Business Owner | No one approves schema changes | Assign from Sales domain | Integration Lead | YYYY-MM-DD |
| IF-005 | Operational Owner | Alerts go to unmonitored mailbox | Route to AMS Team | AMS Manager | YYYY-MM-DD |

## Unowned interfaces
<!-- Interfaces discovered but not in any ownership model -->

## Change process
<!-- How ownership is updated when systems change -->

## Review frequency
<!-- Quarterly recommended -->
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every active interface has a named business owner.</li>
      <li>Every active interface has a named technical owner.</li>
      <li>Every active interface has a named operational owner.</li>
      <li>Critical interfaces have a consumer representative.</li>
      <li>Change process is documented and communicated.</li>
      <li>Matrix is reviewed at least quarterly.</li>
      <li>Ownership gaps have assigned resolution owners and due dates.</li>
      <li>Incident drill confirmed that operational owners know escalation paths.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Assigning only a technical owner and forgetting the business owner. <strong>Consequence:</strong> Schema changes are approved by developers who do not understand business semantics.</li>
      <li><strong>Mistake:</strong> Creating the ownership matrix once and never updating it. <strong>Consequence:</strong> Owners have left, teams have reorganized, and the matrix is fiction.</li>
      <li><strong>Mistake:</strong> Assuming the vendor or external partner owns everything. <strong>Consequence:</strong> Internal accountability is missing; the vendor is blamed for internal decisions.</li>
      <li><strong>Mistake:</strong> No escalation path when the owner is unresponsive. <strong>Consequence:</strong> Incidents stall because the primary owner is on vacation and no one knows who covers.</li>
      <li><strong>Mistake:</strong> Ownership matrix stored in a personal file or wiki with no access for AMS. <strong>Consequence:</strong> The people who need it during an incident cannot find it.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <ul>
      <li><strong>Gather context first:</strong> Collect the interface inventory, system landscape, org chart, and incident history before assigning owners.</li>
      <li><strong>Use the Interface Ownership Matrix template:</strong> Produce a filled matrix, not a list of recommendations.</li>
      <li><strong>Ask who is paged, who approves, who validates:</strong> These questions reveal the real owners better than org charts.</li>
      <li><strong>Identify gaps explicitly:</strong> List every interface with a missing role, the risk, and the proposed assignee.</li>
      <li><strong>Avoid generic language:</strong> Do not write "clear ownership is important." Write "Assign the MDM Lead as business owner for IF-001."</li>
      <li><strong>Link to Atlas diagnostics:</strong> Reference <a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">SAP Interface Monitoring Diagnostics</a> and <a href="/atlas/diagnostics/sap-integration-error-handling-diagnostics/">SAP Integration Error Handling Diagnostics</a> for operational context.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/integration-architecture/api-integration-working-skill/">API Integration</a> — Design interfaces after ownership is clear.</li>
      <li><a href="/skill-hub/integration-architecture/integration-observability-working-skill/">Integration Observability</a> — Build monitoring around owned interfaces.</li>
      <li><a href="/skill-hub/integration-architecture/integration-error-handling-working-skill/">Integration Error Handling</a> — Define error response for owned interfaces.</li>
      <li><a href="/skill-hub/architecture/system-context-mapping-working-skill/">System Context Mapping</a> — Map the landscape before inventorying interfaces.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/integration-ownership-model/">Integration Ownership Model</a> — Conceptual foundation.</li>
      <li><a href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">IDoc / AIF Integration Diagnostics</a> — Operational patterns for owned interfaces.</li>
      <li><a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">SAP Interface Monitoring Diagnostics</a> — Monitoring interfaces.</li>
      <li><a href="/atlas/diagnostics/sap-integration-error-handling-diagnostics/">SAP Integration Error Handling Diagnostics</a> — Error handling for owned interfaces.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of integration ownership practice. It is not official SAP, ITIL, or vendor documentation. The four-role model is a practical simplification; some organizations may need additional roles (security, compliance, legal). The skill assumes the interface inventory can be discovered from middleware and SAP; in heavily decentralized landscapes, discovery may require manual effort.</p>
  </section>
</article>
