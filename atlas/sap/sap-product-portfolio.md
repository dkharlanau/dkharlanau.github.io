---
layout: default
title: "SAP Product Portfolio"
description: "The complete SAP product portfolio organized by category, with practical notes on what each product actually does and where it fits."
permalink: /atlas/sap/sap-product-portfolio/
atlas_section: sap
domain: SAP operations
subdomain: Product landscape
concept_type: reference
sap_area: "Cross-product"
business_process: "Enterprise operations"
status: needs_verification
verified: false
last_synced: 2026-07-14
last_reviewed: 2026-07-14
author: Dzmitryi Kharlanau

tags:
  - sap-products
  - sap-portfolio
  - sap-landscape
related:
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-btp/
  - /atlas/sap/sap-business-ai/
  - /atlas/sap/sap-ariba/
  - /atlas/sap/sap-ibp/
  - /atlas/sap/sap-ewm/
  - /atlas/sap/sap-tm/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Product Portfolio</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Reference</p>
    <h1>SAP Product Portfolio</h1>
    <p class="note-subtitle">Every major SAP product, what it does, and where it sits — synced from sap.com/products as of 2026-07-14.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Scope</dt><dd>Full SAP product portfolio</dd></div>
      <div><dt>Source</dt><dd>sap.com/products (public)</dd></div>
      <div><dt>Last synced</dt><dd>2026-07-14</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>How SAP organizes its portfolio</h2>
    <p>SAP groups its products into 14 portfolio categories. Some products appear in more than one category because they serve multiple functions. The table below lists every major product under its primary category, with a plain-language note on what it actually does.</p>

    <h2>Cloud ERP</h2>
    <table>
      <thead>
        <tr><th>Product</th><th>What it does</th><th>Who it is for</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>SAP S/4HANA Cloud, public edition</strong></td><td>Ready-to-run cloud ERP with pre-configured best practices. SAP manages upgrades; you get the latest features every release cycle.</td><td>Mid-to-large companies that want standard ERP without infrastructure overhead.</td></tr>
        <tr><td><strong>SAP S/4HANA Cloud, private edition</strong></td><td>S/4HANA in a dedicated cloud environment. More flexibility than public edition, closer to on-premise control, but SAP still handles the infrastructure.</td><td>Large enterprises migrating from ECC that need custom code and industry depth.</td></tr>
        <tr><td><strong>SAP S/4HANA (on-premise)</strong></td><td>The self-hosted version. Full control over upgrades, custom code, and infrastructure. Still supported but SAP is pushing customers toward cloud.</td><td>Organizations with strict data residency or deep customization requirements.</td></tr>
        <tr><td><strong>SAP Cloud ERP (GROW with SAP)</strong></td><td>A packaged entry point for midmarket companies adopting S/4HANA Cloud. Bundles ERP with onboarding tools and adoption services.</td><td>Midsize companies moving to cloud ERP for the first time.</td></tr>
        <tr><td><strong>SAP Business One</strong></td><td>ERP designed for small businesses. Covers finance, sales, purchasing, inventory, and light manufacturing. Runs on SQL Server or HANA.</td><td>Companies with roughly 10–500 employees that outgrew spreadsheets.</td></tr>
        <tr><td><strong>SAP Business ByDesign</strong></td><td>Cloud ERP suite for midmarket companies. Covers finance, HR, procurement, project management, CRM, and supply chain in one subscription.</td><td>Growing companies that want a single cloud suite without assembling modules.</td></tr>
      </tbody>
    </table>

    <h2>Business technology platform (BTP)</h2>
    <table>
      <thead>
        <tr><th>Product</th><th>What it does</th><th>Who it is for</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>SAP Integration Suite</strong></td><td>Cloud middleware for connecting SAP and non-SAP systems. Includes API management, event mesh, and pre-built integration content.</td><td>Anyone connecting S/4HANA to satellite products, third-party apps, or legacy systems.</td></tr>
        <tr><td><strong>SAP Build</strong></td><td>Low-code and pro-code development suite. Build Apps (no-code UI), Build Process Automation (workflows, RPA), Build Code (pro-code with Joule copilot).</td><td>Business users building simple apps; professional developers building extensions.</td></tr>
        <tr><td><strong>SAP HANA Cloud</strong></td><td>The HANA database as a managed cloud service. Multi-model (relational, graph, spatial, JSON) with elastic scaling.</td><td>Teams that need HANA capabilities without managing database infrastructure.</td></tr>
        <tr><td><strong>SAP Datasphere</strong></td><td>Data fabric that connects, models, and catalogs data across SAP and non-SAP sources. Preserves business context (semantics) instead of flattening everything into tables.</td><td>Data teams building a unified data layer without moving all data into one warehouse.</td></tr>
        <tr><td><strong>SAP Analytics Cloud</strong></td><td>BI, planning, and predictive analytics in one cloud tool. Connects live to S/4HANA, Datasphere, and third-party sources.</td><td>Finance and business analysts doing reporting, planning, and what-if scenarios.</td></tr>
        <tr><td><strong>SAP Master Data Governance (MDG)</strong></td><td>Central governance for business partner, material, and financial master data. Enforces validation rules and approval workflows before data enters the system.</td><td>Enterprises where bad master data causes downstream incidents across modules.</td></tr>
        <tr><td><strong>SAP Cloud Identity Services</strong></td><td>Identity authentication and provisioning for SAP cloud apps. Handles SSO, user lifecycle, and access policies.</td><td>IT teams managing user access across SAP cloud landscape.</td></tr>
        <tr><td><strong>SAP BTP, Kyma runtime</strong></td><td>Kubernetes-based runtime on BTP for deploying microservices and serverless functions. Used for side-by-side extensions.</td><td>Developers building cloud-native extensions to SAP systems.</td></tr>
      </tbody>
    </table>

    <h2>Business AI</h2>
    <table>
      <thead>
        <tr><th>Product</th><th>What it does</th><th>Who it is for</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>SAP Joule</strong></td><td>SAP's AI copilot embedded across cloud products. Answers questions, triggers workflows, and provides contextual recommendations inside SAP apps.</td><td>End users in SAP cloud products who want natural-language interaction with their data.</td></tr>
        <tr><td><strong>SAP Joule Agents</strong></td><td>Autonomous AI agents that execute multi-step business processes across SAP applications. They coordinate with each other and escalate to humans when needed.</td><td>Organizations automating cross-functional workflows with human oversight.</td></tr>
        <tr><td><strong>SAP Joule Studio</strong></td><td>Development environment for building custom Joule skills and agents. Part of SAP Build.</td><td>Developers creating custom AI agents grounded in SAP business context.</td></tr>
        <tr><td><strong>SAP Business AI (embedded)</strong></td><td>AI capabilities built into SAP products — predictive analytics in IBP, invoice matching in Ariba, demand forecasting in S/4HANA. Not a separate product; it ships inside each app.</td><td>Everyone using SAP cloud products. AI features activate per product license.</td></tr>
      </tbody>
    </table>

    <h2>Spend management</h2>
    <table>
      <thead>
        <tr><th>Product</th><th>What it does</th><th>Who it is for</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>SAP Ariba Buying</strong></td><td>Procurement catalog and purchase order management. Employees buy from approved catalogs; the system enforces compliance and approval rules.</td><td>Procurement teams managing indirect spend.</td></tr>
        <tr><td><strong>SAP Ariba Sourcing</strong></td><td>Strategic sourcing — RFPs, RFQs, auctions, supplier negotiations. Handles both indirect and direct materials sourcing.</td><td>Sourcing professionals running competitive bidding events.</td></tr>
        <tr><td><strong>SAP Ariba Contracts</strong></td><td>Contract lifecycle management. Authoring, negotiation, approval, renewal tracking, and obligation management.</td><td>Legal and procurement teams managing supplier contracts.</td></tr>
        <tr><td><strong>SAP Ariba Supplier Lifecycle</strong></td><td>Supplier onboarding, qualification, performance tracking, and risk assessment across the full supplier relationship.</td><td>Procurement teams managing large supplier bases.</td></tr>
        <tr><td><strong>SAP Fieldglass</strong></td><td>External workforce management. Tracks contingent workers, consultants, freelancers, and service providers. Covers hiring, onboarding, time tracking, invoicing, and compliance.</td><td>Companies with significant contractor or temporary workforce.</td></tr>
        <tr><td><strong>SAP Concur Expense</strong></td><td>Travel and expense management. Employees submit expenses via mobile; the system matches receipts, enforces policy, and feeds approved expenses into ERP for reimbursement.</td><td>Any company with employee travel and expense reporting.</td></tr>
        <tr><td><strong>SAP Concur Travel</strong></td><td>Corporate travel booking integrated with expense. Employees book flights, hotels, and cars within company policy; bookings flow automatically into expense reports.</td><td>Companies managing corporate travel programs.</td></tr>
        <tr><td><strong>SAP Concur Invoice</strong></td><td>Automated invoice capture, matching, and approval. Reduces manual AP processing and catches duplicate or non-compliant invoices.</td><td>Accounts payable teams processing high invoice volumes.</td></tr>
      </tbody>
    </table>

    <h2>Human capital management (HCM)</h2>
    <table>
      <thead>
        <tr><th>Product</th><th>What it does</th><th>Who it is for</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>SAP SuccessFactors Employee Central</strong></td><td>Core HR system of record. Employee master data, organizational structure, position management, time-off tracking, and global payroll integration.</td><td>HR teams replacing on-premise SAP HCM or legacy HR systems.</td></tr>
        <tr><td><strong>SAP SuccessFactors Recruiting</strong></td><td>Applicant tracking and recruitment marketing. Job posting, candidate pipeline, interview scheduling, and offer management. Now includes SmartRecruiters as SAP's ATS platform.</td><td>Talent acquisition teams.</td></tr>
        <tr><td><strong>SAP SuccessFactors Learning</strong></td><td>Learning management system. Course catalog, compliance training, certifications, and learning analytics.</td><td>L&amp;D teams managing employee training programs.</td></tr>
        <tr><td><strong>SAP SuccessFactors Performance &amp; Goals</strong></td><td>Performance reviews, goal setting, continuous feedback, and calibration. Links individual goals to company strategy.</td><td>HR teams running formal performance management cycles.</td></tr>
        <tr><td><strong>SAP SuccessFactors Compensation</strong></td><td>Salary planning, bonus calculations, long-term incentives, and pay-for-performance modeling.</td><td>Compensation and benefits teams.</td></tr>
        <tr><td><strong>SAP SuccessFactors Succession &amp; Development</strong></td><td>Talent pipeline management, succession planning, career pathing, and development plans.</td><td>HR and leadership teams planning workforce continuity.</td></tr>
        <tr><td><strong>SAP SuccessFactors Workforce Analytics</strong></td><td>HR reporting and analytics. Headcount, turnover, diversity, span-of-control, and workforce planning dashboards.</td><td>HR analysts and business leaders needing people data.</td></tr>
        <tr><td><strong>SAP SuccessFactors Onboarding</strong></td><td>Pre-day-one and first-90-days workflows. Paperwork, equipment requests, training assignments, and manager checklists.</td><td>HR teams streamlining new hire experience.</td></tr>
      </tbody>
    </table>

    <h2>CRM and customer experience (CX)</h2>
    <table>
      <thead>
        <tr><th>Product</th><th>What it does</th><th>Who it is for</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>SAP Commerce Cloud</strong></td><td>B2B and B2C e-commerce platform (formerly Hybris). Product catalog, pricing, promotions, order management, and omnichannel storefronts.</td><td>Companies selling online with complex B2B pricing or large product catalogs.</td></tr>
        <tr><td><strong>SAP Sales Cloud</strong></td><td>CRM for sales teams. Lead management, opportunity tracking, pipeline forecasting, quote generation, and territory management.</td><td>Field and inside sales teams.</td></tr>
        <tr><td><strong>SAP Service Cloud</strong></td><td>Customer service platform. Case management, knowledge base, self-service portal, field service scheduling, and omnichannel support.</td><td>Customer service and support organizations.</td></tr>
        <tr><td><strong>SAP Emarsys</strong></td><td>Marketing automation and customer engagement. Email campaigns, personalization, loyalty programs, and cross-channel marketing orchestration.</td><td>Marketing teams running B2C campaigns at scale.</td></tr>
        <tr><td><strong>SAP Customer Data Cloud</strong></td><td>Customer identity and consent management (formerly Gigya). Registration, login, profile management, and privacy compliance across digital properties.</td><td>Companies managing customer identities across web and mobile properties.</td></tr>
        <tr><td><strong>SAP CPQ (Configure, Price, Quote)</strong></td><td>Product configuration, pricing rules, and quote generation for complex or customizable products.</td><td>Manufacturers and B2B sellers with configurable products.</td></tr>
        <tr><td><strong>SAP FSM (Field Service Management)</strong></td><td>Dispatch, scheduling, and mobile execution for field technicians. Integrates with Service Cloud and S/4HANA service orders.</td><td>Companies with field service operations.</td></tr>
      </tbody>
    </table>

    <h2>Supply chain management</h2>
    <table>
      <thead>
        <tr><th>Product</th><th>What it does</th><th>Who it is for</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>SAP IBP (Integrated Business Planning)</strong></td><td>Cloud-based supply chain planning. Demand planning, supply planning, S&amp;OP, inventory optimization, and response management on HANA.</td><td>Supply chain planners replacing APO or spreadsheet-based planning.</td></tr>
        <tr><td><strong>SAP EWM (Extended Warehouse Management)</strong></td><td>Warehouse operations management. Bin-level inventory, wave picking, yard management, labor management, and automation integration (conveyors, robots).</td><td>Companies with complex warehouse operations or high-volume distribution centers.</td></tr>
        <tr><td><strong>SAP TM (Transportation Management)</strong></td><td>Transportation planning and execution. Freight ordering, carrier selection, route optimization, freight settlement, and shipment tracking.</td><td>Shippers and logistics providers managing transportation networks.</td></tr>
        <tr><td><strong>SAP Digital Manufacturing Cloud</strong></td><td>Cloud MES for production execution, quality management, and manufacturing analytics. Connects shop floor to S/4HANA planning.</td><td>Manufacturers digitalizing shop floor operations.</td></tr>
        <tr><td><strong>SAP Asset Performance Management</strong></td><td>Asset health monitoring, predictive maintenance, and reliability analytics. Uses IoT sensor data and machine learning to predict equipment failures.</td><td>Asset-intensive industries (utilities, oil &amp; gas, manufacturing).</td></tr>
        <tr><td><strong>SAP Yard Logistics</strong></td><td>Yard management for trucks, trailers, and containers. Check-in, dock assignment, and yard movement tracking.</td><td>Distribution centers and manufacturing plants with high trailer traffic.</td></tr>
        <tr><td><strong>SAP GTS (Global Trade Services)</strong></td><td>Trade compliance, customs management, and import/export documentation. Handles sanctions screening, preference calculation, and export declarations.</td><td>Companies with significant international trade volumes.</td></tr>
      </tbody>
    </table>

    <h2>Financial management</h2>
    <table>
      <thead>
        <tr><th>Product</th><th>What it does</th><th>Who it is for</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>SAP S/4HANA Finance</strong></td><td>Core financials — general ledger, accounts payable/receivable, asset accounting, and controlling on the Universal Journal (ACDOCA).</td><td>Every S/4HANA customer. This is the financial core.</td></tr>
        <tr><td><strong>SAP Central Finance</strong></td><td>Consolidates financial postings from multiple source ERPs into a single S/4HANA system. Enables centralized reporting without full migration.</td><td>Groups running multiple ERP systems across subsidiaries.</td></tr>
        <tr><td><strong>SAP Group Reporting</strong></td><td>Financial consolidation — intercompany elimination, currency translation, and consolidated financial statements.</td><td>Corporate finance teams preparing group financial reports.</td></tr>
        <tr><td><strong>SAP Treasury and Risk Management</strong></td><td>Cash management, liquidity forecasting, debt and investment management, and financial risk hedging.</td><td>Treasury departments managing corporate cash and financial risk.</td></tr>
        <tr><td><strong>SAP Document and Reporting Compliance</strong></td><td>Electronic invoicing, statutory reporting, and tax compliance across countries. Handles e-invoice mandates and SAF-T formats.</td><td>Finance teams dealing with multi-country compliance requirements.</td></tr>
        <tr><td><strong>SAP GRC (Governance, Risk, and Compliance)</strong></td><td>Access control, process control, and risk management. Segregation-of-duties analysis, automated controls monitoring, and audit management.</td><td>Compliance officers, internal audit, and IT security teams.</td></tr>
        <tr><td><strong>SAP Cash Management</strong></td><td>Real-time cash position visibility and liquidity forecasting. Bank statement integration and cash flow analysis.</td><td>Treasury and finance teams needing daily cash visibility.</td></tr>
      </tbody>
    </table>

    <h2>Business network</h2>
    <table>
      <thead>
        <tr><th>Product</th><th>What it does</th><th>Who it is for</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>SAP Business Network (for Procurement)</strong></td><td>B2B marketplace connecting buyers and suppliers. Suppliers publish catalogs; buyers punch out from Ariba into supplier systems. Order confirmations, ship notices, and invoices flow electronically.</td><td>Buyers and suppliers trading through the Ariba ecosystem.</td></tr>
        <tr><td><strong>SAP Business Network (for Logistics)</strong></td><td>Logistics collaboration network. Freight tendering, shipment tracking, and dock scheduling across carriers and logistics partners.</td><td>Shippers and carriers coordinating transportation.</td></tr>
        <tr><td><strong>SAP Business Network (for Asset Intelligence)</strong></td><td>Asset data sharing between manufacturers, operators, and service providers. Equipment manuals, maintenance history, and performance data in a shared registry.</td><td>Asset owners and equipment manufacturers sharing maintenance data.</td></tr>
      </tbody>
    </table>

    <h2>Business process transformation</h2>
    <table>
      <thead>
        <tr><th>Product</th><th>What it does</th><th>Who it is for</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>SAP Signavio Process Manager</strong></td><td>Process modeling and documentation (BPMN 2.0). Map, document, and share business processes across the organization.</td><td>Process owners and business analysts documenting as-is and to-be processes.</td></tr>
        <tr><td><strong>SAP Signavio Process Insights</strong></td><td>Process mining for SAP systems. Extracts event logs from S/4HANA or ECC and shows how processes actually run — not how they were designed.</td><td>Teams preparing for S/4HANA migration or looking for process bottlenecks.</td></tr>
        <tr><td><strong>SAP Signavio Process Intelligence</strong></td><td>Deeper process mining with KPI tracking, conformance checking, and root-cause analysis across SAP and non-SAP systems.</td><td>Process excellence teams measuring and improving operational performance.</td></tr>
        <tr><td><strong>SAP Signavio Journey Modeler</strong></td><td>Customer journey mapping. Connects customer touchpoints to underlying business processes and identifies experience gaps.</td><td>CX teams linking customer experience to internal process changes.</td></tr>
      </tbody>
    </table>

    <h2>Sustainability management</h2>
    <table>
      <thead>
        <tr><th>Product</th><th>What it does</th><th>Who it is for</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>SAP Sustainability Control Tower</strong></td><td>ESG data collection, reporting, and audit-ready sustainability metrics. Pulls data from S/4HANA and other sources for CSRD and other frameworks.</td><td>Sustainability officers preparing regulatory ESG reports.</td></tr>
        <tr><td><strong>SAP Sustainability Footprint Management</strong></td><td>Product carbon footprint calculation. Uses actual production data (not industry averages) to compute emissions per product.</td><td>Manufacturers tracking and reducing product-level emissions.</td></tr>
        <tr><td><strong>SAP EHS (Environment, Health, Safety)</strong></td><td>Incident management, risk assessment, chemical management, and regulatory compliance for workplace safety and environmental protection.</td><td>EHS departments in manufacturing, chemicals, and energy.</td></tr>
        <tr><td><strong>SAP Green Ledger</strong></td><td>Carbon accounting integrated with financial accounting. Treats emissions as a measurable quantity alongside financial data.</td><td>Companies moving from estimated to actual carbon accounting.</td></tr>
      </tbody>
    </table>

    <h2>Notes</h2>

    <h3>Products that appear in multiple categories</h3>
    <p>Some SAP products span categories. For example, SAP Fieldglass appears under both spend management and HCM because it manages external workforce. SAP Analytics Cloud sits under BTP but serves finance, supply chain, and HR analytics. SAP Joule is embedded across all cloud products rather than being a standalone purchase.</p>

    <h3>On-premise vs cloud</h3>
    <p>SAP's strategic direction is cloud-first. S/4HANA on-premise is still supported, but new features, AI capabilities, and integration content ship first (and sometimes only) in cloud editions. Products like SAP Business One and SAP Business ByDesign continue to serve the midmarket, but SAP GROW and S/4HANA Cloud are the preferred path for new midmarket customers.</p>

    <h3>What is not on this page</h3>
    <p>This page covers SAP's primary product portfolio as listed on sap.com/products. It does not include:</p>
    <ul>
      <li>Legacy products in maintenance-only mode (SAP ECC, SAP CRM on-premise, SAP APO).</li>
      <li>Industry-specific solutions (SAP for Retail, SAP for Utilities, etc.) which are pre-configured industry variants of the core products above.</li>
      <li>Partner-built products on SAP BTP.</li>
      <li>Acquisition-stage products not yet integrated into the SAP portfolio.</li>
    </ul>

    <h3>Verification status</h3>
    <p>Product names, categories, and descriptions are sourced from sap.com/products as of <strong>2026-07-14</strong>. Product capabilities change with each release cycle. Specific feature availability, licensing terms, and deployment options must be verified against current SAP documentation before making purchasing or architecture decisions.</p>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-product-landscape-map/">SAP Product Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/sap-business-ai/">SAP Business AI</a></li>
      <li><a href="/atlas/sap/sap-ariba/">SAP Ariba</a></li>
      <li><a href="/atlas/sap/sap-ibp/">SAP IBP</a></li>
      <li><a href="/atlas/sap/sap-ewm/">SAP EWM</a></li>
      <li><a href="/atlas/sap/sap-tm/">SAP TM</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP Product Portfolio — <a href="https://www.sap.com/products.html">sap.com/products.html</a> (accessed 2026-07-14).</li>
      <li>SAP Business Technology Platform — <a href="https://www.sap.com/products/business-technology-platform.html">sap.com/products/business-technology-platform.html</a> (accessed 2026-07-14).</li>
      <li>SAP Spend Management — <a href="https://www.sap.com/products/spend-management.html">sap.com/products/spend-management.html</a> (accessed 2026-07-14).</li>
      <li>SAP Human Capital Management — <a href="https://www.sap.com/products/hcm.html">sap.com/products/hcm.html</a> (accessed 2026-07-14).</li>
      <li>SAP Customer Experience — <a href="https://www.sap.com/products/crm.html">sap.com/products/crm.html</a> (accessed 2026-07-14).</li>
      <li>SAP Supply Chain Management — <a href="https://www.sap.com/products/scm.html">sap.com/products/scm.html</a> (accessed 2026-07-14).</li>
      <li>SAP Financial Management — <a href="https://www.sap.com/products/financial-management.html">sap.com/products/financial-management.html</a> (accessed 2026-07-14).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a reference based on public SAP product pages. Product capabilities, packaging, and licensing terms change with each release. Verify against SAP's current product documentation before making architecture or purchasing decisions.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-product-landscape-map/">SAP Product Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
