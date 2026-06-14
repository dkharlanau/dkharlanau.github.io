---
layout: default
title: "Atlas Diagnostics — SAP Support and AMS Diagnostics"
description: "Curated diagnostic patterns for SAP AMS, support tickets, operational blockers, and repeat incidents."
permalink: /atlas/diagnostics/
last_modified_at: 2026-06-13
status: reviewed
verified: true
related:
  - /atlas/concepts/order-to-cash/
  - /atlas/data-quality/sap-master-data-quality/
  - /atlas/ai-operations/ai-agent-for-sap-support/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li aria-current="page">Diagnostics</li>
  </ol>
</nav>

<section class="section atlas-hero">
  <p class="eyebrow">Diagnostics</p>
  <h1>Support patterns for repeat SAP incidents and process blockers.</h1>
  <p class="lead">Diagnostics pages are written for the moment when a process is stuck and the team needs a clear first pass: which area is likely involved, what evidence to collect, and where uncertainty remains.</p>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Diagnostic flow</p>
    <h2>How to use this index</h2>
  </header>
  <p>Start with the symptom, not the module. Each process path below maps a business area to a hub page, and each hub page routes to deeper diagnostics. The hubs and most diagnostics pages are review candidates: useful for triage, but not yet promoted to verified status.</p>
  <ol>
    <li><strong>Classify the symptom</strong> — is it a blocked document, a missing master data record, an integration failure, or a mismatch between expected and posted data?</li>
    <li><strong>Pick a process path</strong> — order-to-cash, procure-to-pay, integration, or master data.</li>
    <li><strong>Use the hub matrix</strong> — match the symptom to the first SAP check and collect the listed evidence.</li>
    <li><strong>Follow the diagnostic page</strong> — deeper pages provide transactions, tables, and boundaries.</li>
    <li><strong>Escalate when needed</strong> — customizing changes, cross-module issues, and mass corrections need functional review.</li>
  </ol>

  <h3>Evidence checklist for any diagnostic</h3>
  <ul>
    <li>Document number and item, or object key.</li>
    <li>Current status and status history.</li>
    <li>Organizational data (sales area, purchasing organization, plant, company code).</li>
    <li>Master data keys (use synthetic or generalized identifiers only).</li>
    <li>Error text, log reference, or IDoc/queue number.</li>
    <li>Business impact and urgency.</li>
  </ul>

  <h3>Escalation boundaries</h3>
  <p>Diagnostic pages help identify where the failure lives. They do not replace functional consultation, customizing change control, or official SAP documentation. Escalate when the fix requires configuration changes, affects financial reporting, crosses legal entities, or could create duplicate data.</p>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Process paths</p>
    <h2>Diagnostic hubs</h2>
  </header>
  <p>These hubs group related diagnostics by process area. They are marked as review candidates until human review is completed.</p>
  <div class="atlas-card-grid">
    <a class="atlas-card" href="/atlas/diagnostics/sap-sd-order-to-cash-diagnostics-hub/">
      <h2>Order-to-Cash</h2>
      <p>Sales order blocks, delivery blocks, billing blocks, pricing, credit, and invoice split.</p>
      <span class="link-arrow">Open hub</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-procurement-diagnostics-hub/">
      <h2>Procure-to-Pay</h2>
      <p>Requisitions, purchase orders, release strategy, goods receipt, invoice verification, and three-way match.</p>
      <span class="link-arrow">Open hub</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-integration-diagnostics-hub/">
      <h2>Integration</h2>
      <p>IDoc, AIF, qRFC/tRFC, RFC destinations, ALE, and interface monitoring.</p>
      <span class="link-arrow">Open hub</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-master-data-diagnostics-hub/">
      <h2>Master Data</h2>
      <p>MDG activation, BP/customer/vendor replication, CVI, key mapping, and duplicates.</p>
      <span class="link-arrow">Open hub</span>
    </a>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Pilot Diagnostic</p>
    <h2>Reviewed diagnostic page</h2>
  </header>
  <div class="atlas-card-grid">
    <a class="atlas-card" href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">
      <h2>SAP Sales Order Block Diagnosis</h2>
      <p>A practical split between incompletion, credit, delivery, billing, master data, and governance blockers.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-invoice-split-analysis/">
      <h2>SAP Invoice Split Analysis</h2>
      <p>Trace why billing creates multiple invoices instead of one consolidated document.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">
      <h2>SAP Goods Receipt Diagnostics</h2>
      <p>Investigate where physical receipt, stock, invoice matching, and accounting diverge.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/pos-sales-not-reflected-in-sap/">
      <h2>POS Sales Not Reflected in SAP</h2>
      <p>Trace missing retail sales from POS transmission to downstream posting.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">
      <h2>IDoc and AIF Integration Diagnostics</h2>
      <p>Trace interface failures to partner profiles, segments, master data, or timing issues.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-credit-management-diagnostics/">
      <h2>SAP Credit Management Diagnostics</h2>
      <p>A first-pass structure for separating credit block causes from delivery, billing, and master data issues.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-delivery-block-analysis/">
      <h2>SAP Delivery Block Analysis</h2>
      <p>A first-pass structure for understanding why a sales order cannot create a delivery.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-billing-block-analysis/">
      <h2>SAP Billing Block Analysis</h2>
      <p>A first-pass structure for understanding why a sales document cannot be billed.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">
      <h2>SAP Incompletion Procedure Diagnostics</h2>
      <p>A first-pass structure for finding why a sales document is incomplete and what that blocks downstream.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Procurement and Inventory</p>
    <h2>MM diagnostics and P2P blockers</h2>
  </header>
  <div class="atlas-card-grid">
    <a class="atlas-card" href="/atlas/diagnostics/sap-invoice-verification-diagnostics/">
      <h2>SAP Invoice Verification Diagnostics</h2>
      <p>Separate invoice blocks caused by price, quantity, tax, or reference mismatches.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-movement-types-diagnostics/">
      <h2>SAP Movement Types Diagnostics</h2>
      <p>Find why a goods movement posts to the wrong stock type, account, or status.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-stock-transfer-diagnostics/">
      <h2>SAP Stock Transfer Diagnostics</h2>
      <p>Find why stock is stuck in transit, missing at destination, or posted with wrong valuation.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-three-way-match-diagnostics/">
      <h2>SAP Three-Way Match Diagnostics</h2>
      <p>Find why purchase order, goods receipt, and invoice do not align.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-purchase-order-creation-diagnostics/">
      <h2>SAP Purchase Order Creation Diagnostics</h2>
      <p>Find why a purchase order cannot be created, saved, or released.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-source-determination-diagnostics/">
      <h2>SAP Source Determination Diagnostics</h2>
      <p>Find why the system cannot determine a valid supplier for a requisition or order.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-purchasing-info-record-diagnostics/">
      <h2>SAP Purchasing Info Record Diagnostics</h2>
      <p>Find why a supplier, material, or price relationship is missing or invalid.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-release-strategy-diagnostics/">
      <h2>SAP Release Strategy Diagnostics</h2>
      <p>Find why a purchase order or requisition is blocked by approval workflow.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-purchase-requisition-diagnostics/">
      <h2>SAP Purchase Requisition Diagnostics</h2>
      <p>Find why a purchase requisition cannot be created, approved, or converted to a PO.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-service-entry-sheet-diagnostics/">
      <h2>SAP Service Entry Sheet Diagnostics</h2>
      <p>Find why a service cannot be accepted, entered, or invoiced.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-account-assignment-diagnostics/">
      <h2>SAP Account Assignment Diagnostics</h2>
      <p>Find why a purchase document posts to the wrong cost object or rejects posting.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-material-document-diagnostics/">
      <h2>SAP Material Document Diagnostics</h2>
      <p>Find why a goods movement document is missing, incorrect, or cannot be reversed.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-reservation-diagnostics/">
      <h2>SAP Reservation Diagnostics</h2>
      <p>Find why a reservation cannot be created, consumes wrong stock, or blocks MRP.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-physical-inventory-diagnostics/">
      <h2>SAP Physical Inventory Diagnostics</h2>
      <p>Find why a physical count does not match system stock or why a difference cannot be posted.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-consignment-procurement-diagnostics/">
      <h2>SAP Consignment Procurement Diagnostics</h2>
      <p>Find why consignment stock is not visible, cannot be consumed, or creates wrong liability postings.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-subcontracting-procurement-diagnostics/">
      <h2>SAP Subcontracting Procurement Diagnostics</h2>
      <p>Find why subcontracting components are not issued, finished goods are not received, or costs are misallocated.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-batch-determination-diagnostics/">
      <h2>SAP Batch Determination Diagnostics</h2>
      <p>Find why batch determination fails, returns the wrong batch, or cannot find a valid batch in MM, SD, or WM.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-mrp-exception-diagnostics/">
      <h2>SAP MRP Exception Diagnostics</h2>
      <p>Find why MRP produces exception messages, why planned orders or purchase requisitions are not created, or why a material appears overstocked or short.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-schedule-agreement-diagnostics/">
      <h2>SAP Schedule Agreement Diagnostics</h2>
      <p>Find why a scheduling agreement or delivery schedule cannot be created, released, or received.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-rfq-quota-arrangement-diagnostics/">
      <h2>SAP RFQ and Quota Arrangement Diagnostics</h2>
      <p>Find why an RFQ, quotation, or quota arrangement does not determine the expected supplier split.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-quality-management-inspection-diagnostics/">
      <h2>SAP Quality Management Inspection Diagnostics</h2>
      <p>Find why an inspection lot cannot be created, results-recorded, or usage-decided.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Sales and Delivery Execution</p>
    <h2>Delivery, returns, and logistics execution diagnostics</h2>
  </header>
  <div class="atlas-card-grid">
    <a class="atlas-card" href="/atlas/diagnostics/sap-delivery-processing-diagnostics/">
      <h2>SAP Delivery Processing Diagnostics</h2>
      <p>Find why a delivery cannot be picked, packed, or posted with goods issue.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-returns-processing-diagnostics/">
      <h2>SAP Returns Processing Diagnostics</h2>
      <p>Find why a customer return cannot be created, received, credited, or reconciled.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Financial Operations</p>
    <h2>Tax, G/L, cost objects, bank, and payment diagnostics</h2>
  </header>
  <div class="atlas-card-grid">
    <a class="atlas-card" href="/atlas/diagnostics/sap-tax-determination-diagnostics/">
      <h2>SAP Tax Determination Diagnostics</h2>
      <p>Find why a transaction determines the wrong tax code, rate, or jurisdiction.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-gl-account-master-diagnostics/">
      <h2>SAP GL Account Master Diagnostics</h2>
      <p>Find why a G/L account cannot be posted to, extended, or used in account determination.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-cost-center-profit-center-diagnostics/">
      <h2>SAP Cost Center and Profit Center Diagnostics</h2>
      <p>Find why a cost center or profit center master record blocks posting, assignment, or reporting.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-bank-account-determination-diagnostics/">
      <h2>SAP Bank Account Determination Diagnostics</h2>
      <p>Find why a payment run selects the wrong house bank, account, or payment method.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-payment-run-dunning-diagnostics/">
      <h2>SAP Payment Run and Dunning Diagnostics</h2>
      <p>Find why a payment proposal or dunning run excludes items, fails, or produces unexpected output.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Basis and System Operations</p>
    <h2>Background jobs, spool, and system-level diagnostics</h2>
  </header>
  <div class="atlas-card-grid">
    <a class="atlas-card" href="/atlas/diagnostics/sap-background-job-diagnostics/">
      <h2>SAP Background Job Failure Diagnostics</h2>
      <p>Find why a background job failed, was cancelled, did not start, or produced incorrect results.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-spool-output-diagnostics/">
      <h2>SAP Spool and Print Output Diagnostics</h2>
      <p>Find why a spool request failed, why print output was not generated, or why a document output never reached the printer.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-application-log-diagnostics/">
      <h2>SAP Application Log Diagnostics</h2>
      <p>Find incident evidence in application logs, system logs, and developer traces.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-alerting-diagnostics/">
      <h2>SAP Alerting Diagnostics</h2>
      <p>Find why alerting misses real failures, generates false positives, or routes to the wrong team.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-authorization-diagnostics/">
      <h2>SAP Authorization and Role Diagnostics</h2>
      <p>Find missing roles, profile gaps, and authorization failures.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-change-control-diagnostics/">
      <h2>SAP Change Control Diagnostics</h2>
      <p>Find transport request failures, import errors, and sequencing issues.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-transport-governance-diagnostics/">
      <h2>SAP Transport Governance Diagnostics</h2>
      <p>Find queue conflicts, import-order errors, and governance gaps.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-incident-triage-diagnostics/">
      <h2>SAP Incident Triage Diagnostics</h2>
      <p>Classify and route SAP support incidents before deep investigation.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-workflow-diagnostics/">
      <h2>SAP Workflow Diagnostics</h2>
      <p>Find why workflow items are stuck, routed to the wrong agent, or missed their deadlines.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-plant-maintenance-order-diagnostics/">
      <h2>SAP Plant Maintenance Order Diagnostics</h2>
      <p>Find why a PM order or notification cannot be created, released, settled, or completed.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Integration and Interfaces</p>
    <h2>IDoc, ALE, RFC, and monitoring diagnostics</h2>
  </header>
  <div class="atlas-card-grid">
    <a class="atlas-card" href="/atlas/diagnostics/sap-idoc-status-diagnostics/">
      <h2>SAP IDoc Status Diagnostics</h2>
      <p>Interpret IDoc status codes and decide the next action based on status.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">
      <h2>SAP Interface Monitoring Diagnostics</h2>
      <p>Find why interface monitoring misses failures, generates false alerts, or does not cover critical paths.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-ale-distribution-model-diagnostics/">
      <h2>SAP ALE Distribution Model Diagnostics</h2>
      <p>Find why master data is not distributed, arrives at the wrong target, or creates duplicate objects.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-qrfc-trfc-diagnostics/">
      <h2>SAP qRFC and tRFC Diagnostics</h2>
      <p>Find why RFC calls are stuck, failing, or executing out of order.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-output-message-control-diagnostics/">
      <h2>SAP Output and Message Control Diagnostics</h2>
      <p>Find why a document output was not created, not sent, or sent to the wrong recipient.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-integration-error-handling-diagnostics/">
      <h2>SAP Integration Error Handling Diagnostics</h2>
      <p>Classify integration errors, decide retry versus escalation, and prevent recurrence.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-inbound-processing-diagnostics/">
      <h2>SAP Inbound Processing Diagnostics</h2>
      <p>Find why an inbound message was not received, not posted, or created wrong data.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-outbound-processing-diagnostics/">
      <h2>SAP Outbound Processing Diagnostics</h2>
      <p>Find why an outbound message was not created, not sent, or arrived corrupted at the partner.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-rfc-destination-diagnostics/">
      <h2>SAP RFC Destination Diagnostics</h2>
      <p>Find why an RFC destination fails, why tRFC or qRFC queues are stuck, or why cross-system calls return errors.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-rest-api-diagnostics/">
      <h2>SAP REST API Diagnostics</h2>
      <p>Find HTTP/REST API connectivity, authentication, and payload failures.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-soap-diagnostics/">
      <h2>SAP SOAP Diagnostics</h2>
      <p>Find SOAP web-service failures, proxy errors, and WSDL mismatches.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-cloud-connector-diagnostics/">
      <h2>SAP Cloud Connector Diagnostics</h2>
      <p>Find SAP BTP Cloud Connector connectivity, tunnel, and destination issues.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-api-gateway-diagnostics/">
      <h2>SAP API Gateway Diagnostics</h2>
      <p>Find API gateway routing, authentication, and policy failures.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-odata-service-diagnostics/">
      <h2>SAP OData Service Diagnostics</h2>
      <p>Find why an OData service fails metadata, activation, or runtime calls.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-fiori-launchpad-diagnostics/">
      <h2>SAP Fiori Launchpad Diagnostics</h2>
      <p>Find why a Fiori tile, group, or app is missing or fails to launch.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Master Data and Replication</p>
    <h2>BP, vendor, customer, MDG, and governance diagnostics</h2>
  </header>
  <div class="atlas-card-grid">
    <a class="atlas-card" href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">
      <h2>SAP Business Partner Replication Diagnostics</h2>
      <p>Find why a business partner was not replicated, arrived incomplete, or created duplicates.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-vendor-master-replication-diagnostics/">
      <h2>SAP Vendor Master Replication Diagnostics</h2>
      <p>Find why a vendor was not replicated, arrived with wrong data, or created a duplicate.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-customer-master-replication-diagnostics/">
      <h2>SAP Customer Master Replication Diagnostics</h2>
      <p>Find why a customer was not replicated, arrived with wrong data, or created a duplicate.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-mdg-to-s4-replication-diagnostics/">
      <h2>SAP MDG to S/4 Replication Diagnostics</h2>
      <p>Find why master data approved in MDG does not appear correctly in S/4HANA target systems.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-key-mapping-diagnostics/">
      <h2>SAP Key Mapping Diagnostics</h2>
      <p>Find why objects have different keys across systems, causing duplicates, broken links, or failed replications.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-bp-relationship-diagnostics/">
      <h2>SAP BP Relationship Diagnostics</h2>
      <p>Find why a business partner relationship is missing, invalid, or prevents transactions.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-cvi-synchronization-diagnostics/">
      <h2>SAP CVI Synchronization Diagnostics</h2>
      <p>Find why a business partner, customer, or vendor is not synchronized correctly through CVI.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-number-range-diagnostics/">
      <h2>SAP Number Range Diagnostics</h2>
      <p>Find why a document or master data object cannot be created due to number range problems.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-master-data-duplicate-diagnostics/">
      <h2>SAP Master Data Duplicate Diagnostics</h2>
      <p>Find why duplicate master data records exist, how to identify them, and how to prevent recurrence.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-organizational-data-diagnostics/">
      <h2>SAP Organizational Data Diagnostics</h2>
      <p>Find why a master data object is missing organizational assignments, has wrong ones, or fails validation.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/sap-material-master-extension-diagnostics/">
      <h2>SAP Material Master Extension Diagnostics</h2>
      <p>Find why a material master cannot be extended to a new plant, sales organization, or view, or why a material is blocked for a business process.</p>
      <span class="link-arrow">Read diagnostic</span>
    </a>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Related</p>
    <h2>Related Atlas pages</h2>
  </header>
  <ul>
    <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
    <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
    <li><a href="/atlas/ai-operations/ai-agent-for-sap-support/">AI Agent for SAP Support</a></li>
  </ul>
</section>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
