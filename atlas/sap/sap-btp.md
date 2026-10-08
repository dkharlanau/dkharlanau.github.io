---
layout: default
btp_reader: true
hide_global_cta: true
title: "SAP Business AI Platform & BTP — Solution Architect Study Guide"
description: "An SAP Lead study guide connecting enterprise architecture, SAP reference business and solution models, platform design, real procurement cases and architecture decisions."
permalink: /atlas/sap/sap-btp/
atlas_section: sap
domain: SAP operations
subdomain: SAP Business AI Platform and BTP
concept_type: product
sap_area: "SAP BTP"
business_process: "Enterprise and solution architecture"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
last_modified_at: 2026-10-08
author: Dzmitryi Kharlanau
tags:
  - sap-btp
  - sap-business-ai-platform
  - enterprise-architecture
  - solution-architecture
  - reference-business-architecture
  - reference-solution-architecture
  - clean-core
  - sap-lead
related:
  - /atlas/sap/sap-signavio/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-build/
  - /labs/assessment/
  - /labs/business-ai/
robots: noindex,follow
sitemap: false
---
<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/sap/">SAP</a></li><li aria-current="page">Business AI Platform &amp; BTP</li></ol></nav>

<article class="research-canvas signavio-reader btp-reader" aria-label="SAP Business AI Platform and BTP Solution Architect Study Guide">
<header class="research-canvas__hero signavio-reader__hero">
<div class="research-canvas__hero-copy">
<p class="research-canvas__eyebrow">Knowledge Atlas / SAP Lead / Solution Architecture</p>
<h1>SAP Business AI Platform &amp; BTP</h1>
<p>Understand how business architecture becomes a working SAP solution. Learn the models, choose the right products, explain the trade-offs and defend the design.</p>
<div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
<a class="research-canvas__button" href="#reading-map">Open the study map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
</div>
<aside class="research-canvas__signal" aria-label="Study outcomes">
<p>After reading, you can</p>
<div class="research-canvas__signal-line"><span>01</span><strong>Explain EA and SA roles</strong></div>
<div class="research-canvas__signal-line"><span>02</span><strong>Trace RBA into RSA</strong></div>
<div class="research-canvas__signal-line"><span>03</span><strong>Defend a BTP solution design</strong></div>
<em>A practical architecture foundation for SAP Lead assessment and customer discussions.</em>
</aside>
</header>
<aside class="research-canvas__boundary" aria-label="How to use this guide">
<span class="material-symbols-outlined" aria-hidden="true">menu_book</span>
<p><strong>Suggested route:</strong> Begin with the business-to-solution map, then study reference models and the SAP toolchain. Finish with the procurement example and answer the assessment questions aloud. This page expands as new lessons are added.</p>
</aside>
<nav class="research-canvas__inventory signavio-reader__toc" id="reading-map" aria-label="Study chapters">
<header><p class="research-canvas__eyebrow">On this page</p><h2>Study the decision, not only the definition.</h2><p>Follow the full path or jump to one model, product or interview answer.</p></header>
<div class="signavio-reader__toc-grid"><section class="signavio-reader__toc-group" aria-labelledby="btp-route-0"><h3 id="btp-route-0">Architecture thinking</h3><ol><li><a href="#big-picture">Start with one picture</a></li>
<li><a href="#architect-roles">Enterprise vs Solution Architect</a></li>
<li><a href="#ea-value">Why enterprise architecture matters</a></li>
<li><a href="#frameworks">EA frameworks and SAP method</a></li></ol></section>
<section class="signavio-reader__toc-group" aria-labelledby="btp-route-1"><h3 id="btp-route-1">SAP reference architecture</h3><ol><li><a href="#toolchain">Tools and responsibilities</a></li>
<li><a href="#rba">Reference Business Architecture</a></li>
<li><a href="#rsa">Reference Solution Architecture</a></li>
<li><a href="#trace">Trace business need to solution</a></li></ol></section>
<section class="signavio-reader__toc-group" aria-labelledby="btp-route-2"><h3 id="btp-route-2">Platform solution design</h3><ol><li><a href="#platform-scope">Business AI Platform vs BTP</a></li>
<li><a href="#accounts">BTP account and runtime model</a></li>
<li><a href="#design-choices">Choose an extension approach</a></li>
<li><a href="#procurement-case">End-to-end procurement case</a></li></ol></section>
<section class="signavio-reader__toc-group" aria-labelledby="btp-route-3"><h3 id="btp-route-3">Explain and practice</h3><ol><li><a href="#client-explanation">Explain to business</a></li>
<li><a href="#interview">Assessment questions and answers</a></li>
<li><a href="#next">Learning path and future chapters</a></li>
<li><a href="#sources">Sources and verification boundary</a></li></ol></section></div>
</nav>
<section class="research-canvas__inventory signavio-reader__section" id="big-picture" aria-labelledby="big-picture-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">01 / Orientation</p><h2 id="big-picture-title">Start with one picture</h2></header><div class="signavio-reader__content">
<p>An architect should be able to trace one business need all the way to a solution that can run, be secured, and be supported. Start with the business result, not a list of SAP products.</p>
<p><strong>Business goal → Business capability → Business process → Solution capability → Solution component → Integration and data flow → Measured result.</strong></p>
<div class="table-scroll study-table" role="region" aria-label="Business to technology translation" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Layer</th><th scope="col">Question</th><th scope="col">Simple procurement example</th></tr></thead><tbody><tr><td>Business outcome</td><td>Why do we need change?</td><td>Reduce purchases made outside the agreed buying process.</td></tr>
<tr><td>Business capability</td><td>What must the company be able to do?</td><td>Control purchasing and approvals.</td></tr>
<tr><td>Business process</td><td>How does work happen?</td><td>Request → approve → purchase → receive → pay.</td></tr>
<tr><td>Solution design</td><td>Which parts of IT support the process?</td><td>S/4HANA for purchasing; an extension only where a gap remains.</td></tr>
<tr><td>Integration and controls</td><td>How does the design stay reliable?</td><td>Released APIs, identity, audit trail, monitoring and recovery.</td></tr>
<tr><td>Value</td><td>What evidence shows improvement?</td><td>Fewer exceptions and faster approved requests.</td></tr></tbody></table></div>
<p><strong>Remember:</strong> A capability is what the business can do. A process is how work is performed. A solution component is software that helps perform it. They are related, but they are not the same thing.</p>
<p>In 2026, SAP positions <strong>SAP Business AI Platform</strong> as a broader portfolio that includes SAP BTP, Business Data Cloud, Business Transformation Management solutions and AI capabilities. BTP remains a useful name for the platform foundation. Do not treat these names as identical products.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="architect-roles" aria-labelledby="architect-roles-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">02 / Responsibilities</p><h2 id="architect-roles-title">Enterprise Architect vs Solution Architect</h2></header><div class="signavio-reader__content">
<p>Think of a city planner and a building architect. The city planner protects the whole city's development. The building architect delivers one building within that plan. The two roles work together, but one does not always formally report to the other.</p>
<div class="table-scroll study-table" role="region" aria-label="Enterprise and solution architects compared" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Dimension</th><th scope="col">Enterprise Architect (EA)</th><th scope="col">Solution Architect (SA)</th></tr></thead><tbody><tr><td>Main concern</td><td>Business and IT direction across the enterprise.</td><td>A working end-to-end design for a specific problem.</td></tr>
<tr><td>Key question</td><td>What should we standardize, invest in, replace or retire?</td><td>How should the selected solution be built and operated?</td></tr>
<tr><td>Scope</td><td>Capabilities, processes, applications, technologies and roadmaps.</td><td>Components, integrations, data, security, NFRs and delivery constraints.</td></tr>
<tr><td>Typical output</td><td>Target architecture, principles, portfolio decisions, transition roadmap.</td><td>Solution diagram, integration contracts, NFRs, design decisions and handover.</td></tr>
<tr><td>Partners</td><td>Business leaders, CIO/CTO, portfolio owners and domain architects.</td><td>Business owners, developers, integration, security, operations and delivery teams.</td></tr></tbody></table></div>
<h3>A practical handoff</h3>
<p>A company wants one procurement approach for all regions. The EA sets the target application landscape, integration principles and roadmap. The SA designs a purchase-request extension that fits those standards. If an approved standard creates a real project problem, the SA brings evidence back to the EA for a decision.</p>
<p><strong>Assessment sentence:</strong> “The EA protects coherence across the landscape. The SA protects the quality of a specific solution and its fit within that landscape.”</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="ea-value" aria-labelledby="ea-value-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">03 / Business value</p><h2 id="ea-value-title">Why enterprise architecture matters</h2></header><div class="signavio-reader__content">
<p>Without an architecture view, local teams can solve the same need using separate applications and inconsistent data. Each local success then becomes another integration or support problem. Enterprise architecture makes dependencies and investment decisions visible before they become expensive.</p>
<p>It helps leaders align IT with business strategy, reduce duplicate applications, improve change speed, manage security and compliance, and see the effect of retiring or changing a system. The goal is better decisions, not more diagrams.</p>
<h3>Nine common situations where EA is useful</h3>
<div class="table-scroll study-table" role="region" aria-label="Nine use cases for enterprise architecture" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Business pressure</th><th scope="col">Use case</th><th scope="col">Architecture decision</th></tr></thead><tbody><tr><td>Reduce complexity</td><td>Post-merger integration</td><td>Which applications and data models should converge?</td></tr>
<tr><td>Reduce complexity</td><td>Application rationalization</td><td>What should we keep, consolidate or retire?</td></tr>
<tr><td>Reduce complexity</td><td>Integration architecture</td><td>Which systems own data, and how should they communicate?</td></tr>
<tr><td>Ensure compliance</td><td>Technology risk</td><td>Where are unsupported or high-risk dependencies?</td></tr>
<tr><td>Ensure compliance</td><td>Data compliance</td><td>How do we control access, location, retention and lineage?</td></tr>
<tr><td>Ensure compliance</td><td>Governance standards</td><td>Which principles are mandatory and where are exceptions justified?</td></tr>
<tr><td>Promote growth</td><td>Monolith modernization</td><td>What should remain together and what can be separated safely?</td></tr>
<tr><td>Promote growth</td><td>Cloud transformation</td><td>Which workloads, operating models and migration steps make sense?</td></tr>
<tr><td>Promote growth</td><td>IoT architecture</td><td>How do devices, events, data and enterprise systems connect safely?</td></tr></tbody></table></div>
<p><strong>Lead question:</strong> “What decision becomes safer because we have this architecture?” If a diagram cannot answer that, its purpose is unclear.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="frameworks" aria-labelledby="frameworks-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">04 / Method</p><h2 id="frameworks-title">Frameworks and the SAP EA method</h2></header><div class="signavio-reader__content">
<p>An architecture framework gives people a shared structure for work. It does not decide the target design for them.</p>
<div class="table-scroll study-table" role="region" aria-label="Architecture frameworks in context" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Framework</th><th scope="col">Useful mental model</th><th scope="col">When it helps</th></tr></thead><tbody><tr><td>TOGAF and ADM</td><td>A structured, iterative method for architecture development.</td><td>Plan baseline, target, gaps, migration and governance.</td></tr>
<tr><td>Zachman</td><td>A classification of architecture descriptions and viewpoints.</td><td>Check whether important perspectives are missing.</td></tr>
<tr><td>FEAF</td><td>An enterprise architecture approach developed for the US federal context.</td><td>Coordinate capabilities and investments across public institutions.</td></tr>
<tr><td>Gartner's EA approach</td><td>Focus on business outcomes and decision support.</td><td>Keep architecture tied to visible strategic value.</td></tr></tbody></table></div>
<p>The <strong>SAP Enterprise Architecture Framework</strong> combines five connected pillars: Methodology, Reference Architecture Content, Tooling, Practice and Services. SAP's methodology connects strategy, business architecture, solution architecture, technology, roadmaps and governance.</p>
<p>The practical working cycle is <strong>understand the baseline → define the target → find gaps → design transitions → govern delivery → measure results</strong>. Work is iterative: new evidence may change the roadmap or the solution.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="toolchain" aria-labelledby="toolchain-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">05 / Toolchain</p><h2 id="toolchain-title">Which SAP tool solves which architecture problem?</h2></header><div class="signavio-reader__content">
<p>These tools are complementary, not interchangeable. A good architect names the question each tool answers and the handoff to the next tool.</p>
<div class="table-scroll study-table" role="region" aria-label="SAP architecture toolchain" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Product or area</th><th scope="col">Primary job</th><th scope="col">Typical output</th></tr></thead><tbody><tr><td><a href='/atlas/sap/sap-signavio/'>SAP Signavio</a></td><td>Understand, model and improve business processes.</td><td>Process model, process performance evidence, improvement opportunities.</td></tr>
<tr><td>SAP LeanIX</td><td>Map capabilities, applications, interfaces, technologies and transformation plans.</td><td>Application portfolio, dependencies and target-state roadmap.</td></tr>
<tr><td>SAP Cloud ALM</td><td>Coordinate SAP implementation and operations.</td><td>Requirements, tests, deployment and operational monitoring evidence.</td></tr>
<tr><td><a href='/atlas/sap/sap-build/'>SAP Build</a></td><td>Build applications and business automations where needed.</td><td>Extension UI, workflow, automation and related artifacts.</td></tr>
<tr><td>SAP Integration Suite</td><td>Connect and manage exchanges between systems.</td><td>Integration flows, APIs, policies and integration monitoring.</td></tr>
<tr><td>WalkMe and SAP Enable Now</td><td>Support user adoption and learning in daily work.</td><td>In-app guidance, learning and adoption feedback.</td></tr>
<tr><td>SAP Business AI Platform</td><td>Provide platform and AI-related capabilities across the SAP portfolio.</td><td>Platform services, runtime, integration, data and AI building blocks.</td></tr></tbody></table></div>
<h3>How the tools work together</h3>
<p>Suppose supplier invoice approvals take too long. Signavio helps identify where delays happen and model the future process. LeanIX shows the applications that support that process. The solution architect chooses whether standard ERP configuration or an extension is needed. SAP Build and Integration Suite may implement the gap. Cloud ALM supports delivery and operational follow-up. User adoption tools can help staff work with the new process.</p>
<p><strong>Do not assume</strong> a process model automatically creates a production workflow, or that having an application recorded in LeanIX proves its integration works. The handoffs require design, configuration, ownership and validation.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="rba" aria-labelledby="rba-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">06 / Business language</p><h2 id="rba-title">Reference Business Architecture (RBA)</h2></header><div class="signavio-reader__content">
<p>RBA describes the business without first choosing software. It helps business and IT agree on what must happen before they debate technology.</p>
<h3>Two models that answer different questions</h3>
<div class="table-scroll study-table" role="region" aria-label="RBA models and hierarchy" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Model</th><th scope="col">Structure</th><th scope="col">Question it answers</th></tr></thead><tbody><tr><td>Business Capability Model (BCM)</td><td>Enterprise domain → business domain → business area → capability.</td><td>What abilities does the organization need?</td></tr>
<tr><td>Business Process Model (BPM)</td><td>End-to-end process → process module → process segment → business activity.</td><td>How does the organization deliver value?</td></tr></tbody></table></div>
<p>For example, <strong>Purchasing Management</strong> is a business capability. <strong>Source-to-Pay</strong> is an end-to-end process that can use this capability across several activities. One capability may support more than one process. SAP's business activities are aligned with the APQC Process Classification Framework (PCF).</p>
<p>BCM aims to organize capabilities using the <strong>MECE principle</strong>: mutually exclusive, collectively exhaustive. In simple terms, avoid unnecessary overlap and important gaps. The course term is MECE, not “MISI”.</p>
<h3>The four enterprise domains</h3>
<div class="table-scroll study-table" role="region" aria-label="Enterprise domains in SAP reference business architecture" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Domain</th><th scope="col">What it broadly covers</th></tr></thead><tbody><tr><td>Develop Product and Service</td><td>Define and develop products and services.</td></tr>
<tr><td>Supply / Fulfill Demand</td><td>Plan, make, source, deliver and support fulfillment.</td></tr>
<tr><td>Customer / Generate Demand</td><td>Attract, sell and serve customers.</td></tr>
<tr><td>Corporate / Plan and Manage Enterprise</td><td>Manage finance, people, compliance and enterprise operations.</td></tr></tbody></table></div>
<p><strong>Boundary to remember:</strong> A business capability does not become an SAP product just because the product can support it. Define the business need first.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="rsa" aria-labelledby="rsa-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">07 / Technology realization</p><h2 id="rsa-title">Reference Solution Architecture (RSA)</h2></header><div class="signavio-reader__content">
<p>RSA connects the business view to a proposed solution using SAP products, solution capabilities, components, processes and data. It helps the architect move from “what the business needs” to “how the solution can support it”.</p>
<div class="table-scroll study-table" role="region" aria-label="RSA artifacts and what they explain" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Artifact</th><th scope="col">What to read from it</th><th scope="col">Question to ask</th></tr></thead><tbody><tr><td>Solution Capability Model / product map</td><td>Which software capabilities and components support a business capability.</td><td>Which products cover the required scope, and what remains missing?</td></tr>
<tr><td>Solution Value Flow Diagram</td><td>A high-level view of value-adding solution activities and their supporting components.</td><td>Where does each component contribute to the outcome?</td></tr>
<tr><td>Solution Process Flow Diagram</td><td>Detailed activities and handoffs, typically with BPMN-based notation.</td><td>Which step runs where, and what triggers the next step?</td></tr>
<tr><td>Solution Component Diagram</td><td>Solution building blocks and their interactions.</td><td>Which components depend on which others?</td></tr>
<tr><td>Solution Data Flow Diagram</td><td>Movement of master and transactional data across solution components.</td><td>Which system owns, changes and receives the data?</td></tr></tbody></table></div>
<p>Start with <strong>business coverage</strong>: which products are recommended for the scope. Then study <strong>detailed architecture</strong>: actual process steps, interfaces and data movement. SAP reference content is a starting point, not a guarantee that every component or API is available under a customer's contract, release or edition.</p>
<h3>Do not confuse these diagrams</h3>
<p>The value flow explains <em>why each step adds value</em>. The process flow explains <em>what happens and in which order</em>. The component diagram explains <em>which systems interact</em>. The data flow explains <em>what information crosses their boundaries</em>.</p>
<p>For actual implementations, continue to the <a href="https://api.sap.com/">SAP Business Accelerator Hub</a> to inspect released APIs, events and integration artifacts that fit the customer's products and versions.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="trace" aria-labelledby="trace-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">08 / Working example</p><h2 id="trace-title">Trace one requirement across the architecture</h2></header><div class="signavio-reader__content">
<p><strong>Scenario:</strong> Employees buy non-standard items by email. Approvals are inconsistent and procurement has limited visibility.</p>
<div class="table-scroll study-table" role="region" aria-label="Traceability example from business to solution" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Step</th><th scope="col">Architecture view</th><th scope="col">What to capture</th></tr></thead><tbody><tr><td>1. Define outcome</td><td>Strategy</td><td>Reduce purchases outside the controlled process.</td></tr>
<tr><td>2. Map capability</td><td>BCM</td><td>Purchasing and approval control.</td></tr>
<tr><td>3. Map process</td><td>BPM</td><td>Request item → approve → create purchase requisition → follow procurement.</td></tr>
<tr><td>4. Identify gap</td><td>Baseline with Signavio and LeanIX</td><td>Missing request experience and unclear process ownership.</td></tr>
<tr><td>5. Design solution</td><td>RSA</td><td>Standard S/4HANA process where possible; only extend missing steps.</td></tr>
<tr><td>6. Design boundaries</td><td>Solution component + data flow</td><td>Owner of requisition, API contract, identity, error handling and monitoring.</td></tr>
<tr><td>7. Verify outcome</td><td>Process and operations evidence</td><td>Process compliance, cycle time and failed integration cases.</td></tr></tbody></table></div>
<p>The most important decision is not which tool can draw the process. It is <strong>which system owns the official purchase requisition and how we prove that it was created successfully</strong>.</p>
<p>In a workshop, start from a real transaction or a realistic synthetic example. Trace the business requirement to the responsible application, a documented interface, and a measurable result. That is the point where an architecture diagram becomes useful.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="platform-scope" aria-labelledby="platform-scope-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">09 / Portfolio boundaries</p><h2 id="platform-scope-title">SAP Business AI Platform and SAP BTP</h2></header><div class="signavio-reader__content">
<p><strong>SAP BTP</strong> provides cloud platform capabilities for applications, extensions, integration, security, connectivity and managed services. <strong>SAP Business AI Platform</strong> is SAP's broader 2026 portfolio positioning, combining BTP with data, AI and business transformation capabilities. The portfolio description can change faster than the underlying technical contracts.</p>
<p>Do not use “BTP” as the name of a single runtime or integration service. A solution diagram must identify the actual service, environment, region, identity boundary and owner.</p>
<h3>A platform architect thinks in layers</h3>
<div class="table-scroll study-table" role="region" aria-label="Practical platform layers" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Concern</th><th scope="col">Examples</th><th scope="col">Design decision</th></tr></thead><tbody><tr><td>Business applications</td><td>SAP S/4HANA and other SAP or non-SAP applications.</td><td>Which system is the system of record?</td></tr>
<tr><td>Application and workflow</td><td>SAP Build, CAP applications, ABAP environment and supported extensions.</td><td>Configure, extend in-app, or build side-by-side?</td></tr>
<tr><td>Integration</td><td>Integration Suite, APIs, events, destinations, connectivity.</td><td>Synchronous or asynchronous? How do we recover?</td></tr>
<tr><td>Data and AI</td><td>SAP Business Data Cloud, AI services, governed business context.</td><td>What data may be used, who can see it, and how do we evaluate results?</td></tr>
<tr><td>Platform operations</td><td>Runtime, identities, entitlements, observability, transport and cost.</td><td>Who deploys, secures, pays for and supports it?</td></tr></tbody></table></div>
<p><strong>AI is a design option, not the starting requirement.</strong> Use a clear rule or approval workflow for deterministic decisions. Consider AI for tasks such as interpreting unstructured requests only when data protection, evaluation, human review and failure handling are designed.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="accounts" aria-labelledby="accounts-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">10 / Foundations</p><h2 id="accounts-title">BTP account model: where a solution runs</h2></header><div class="signavio-reader__content">
<p>A <strong>global account</strong> is the top-level commercial and administrative boundary. Optional <strong>directories</strong> organize the landscape. Regional <strong>subaccounts</strong> are used to deploy applications, use services and manage subscriptions, members and authorizations.</p>
<div class="table-scroll study-table" role="region" aria-label="SAP BTP account and environment terms" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Term</th><th scope="col">Meaning</th><th scope="col">Architect's concern</th></tr></thead><tbody><tr><td>Global account</td><td>Contract-related top-level account; entitlements and quotas are managed here.</td><td>Commercial model, governance and cost allocation.</td></tr>
<tr><td>Directory (optional)</td><td>Groups directories and subaccounts.</td><td>Organization, delegated management and possible quota assignment.</td></tr>
<tr><td>Subaccount</td><td>Region-specific boundary for applications, services, identity and authorization.</td><td>Landscape separation, residency, service availability and trust.</td></tr>
<tr><td>Cloud Foundry org / space</td><td>Runtime-specific structure for Cloud Foundry applications.</td><td>Deployment isolation and environment access.</td></tr>
<tr><td>Kyma cluster / namespace</td><td>Runtime-specific structure for Kubernetes workloads.</td><td>Container operations, resource and access boundaries.</td></tr>
<tr><td>Entitlement / service plan</td><td>Permission and quota for using a specific offering.</td><td>Can this subaccount consume the required service here?</td></tr></tbody></table></div>
<p><strong>Common exam trap:</strong> A Cloud Foundry space is not the same as a BTP subaccount. A Kyma namespace is not a global BTP account object. The hierarchy below a subaccount depends on the enabled environment.</p>
<p>For identity, distinguish authentication by an identity provider from authorization inside BTP applications and backend systems. Role collections, app roles and S/4HANA authorizations may all matter. For private-network access, investigate supported SAP Cloud Connector and destination scenarios rather than assuming a direct public endpoint.</p>
<p>Use separate development, test and production boundaries where appropriate. Before promising a service, check <strong>region, entitlement, plan, quota, contract, security and operations</strong>.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="design-choices" aria-labelledby="design-choices-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">11 / Trade-offs</p><h2 id="design-choices-title">Choose the simplest safe solution</h2></header><div class="signavio-reader__content">
<p>“Can we build this on BTP?” is not the right first question. Ask whether the business need is already covered by the standard application. Then compare a small number of valid options.</p>
<div class="table-scroll study-table" role="region" aria-label="SAP extension and integration decisions" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Need</th><th scope="col">Consider first</th><th scope="col">Choose differently when</th></tr></thead><tbody><tr><td>A standard approval or validation</td><td>Supported ERP configuration and standard process.</td><td>A genuine cross-application workflow cannot be covered cleanly.</td></tr>
<tr><td>An ERP-specific enhancement</td><td>Released in-app extensibility appropriate to the ERP edition.</td><td>Independent scaling, lifecycle or cross-system UI is required.</td></tr>
<tr><td>A new cross-system app</td><td>Side-by-side extension on suitable BTP runtime.</td><td>The added runtime and operations are not justified.</td></tr>
<tr><td>An integration contract</td><td>A released API, event or supported integration pattern.</td><td>Direct coupling creates poor transformation or recovery options.</td></tr>
<tr><td>Complex mapping or mediation</td><td>SAP Integration Suite, where it fits.</td><td>A simple supported direct connection meets all requirements.</td></tr>
<tr><td>Unstructured text understanding</td><td>A narrowly bounded AI capability with evaluation and review.</td><td>Rules, forms and validation are sufficient and more reliable.</td></tr></tbody></table></div>
<h3>Clean core is more than moving code</h3>
<p>Side-by-side development can protect the ERP core, but it can still create technical debt through unstable interfaces, duplicated business logic, weak data ownership or missing monitoring. Choose released contracts; design authorization, idempotency, retries and reconciliation; document who can recover an incomplete business transaction.</p>
<p><strong>Technical check:</strong> If an API returns a technical success but the business document is not created, how will the process owner know? Define the acknowledgment, error state, reconciliation and recovery path before deployment.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="procurement-case" aria-labelledby="procurement-case-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">12 / Apply</p><h2 id="procurement-case-title">Case study: improve a non-standard purchase request</h2></header><div class="signavio-reader__content">
<p><strong>Business problem:</strong> Employees bypass purchasing controls because requesting a non-standard item is difficult. The target is easier requests without losing approval or audit quality.</p>
<ol>
<li><strong>Discover with Signavio.</strong> Find which requests bypass the process, where work waits and which variants need support. Confirm data quality before treating a dashboard as fact.</li>
<li><strong>Map with LeanIX.</strong> Identify the purchasing applications, portals, interfaces, ownership and lifecycle risks. Check whether a similar request tool already exists.</li>
<li><strong>Design the target.</strong> Prefer standard S/4HANA functions where they cover the need. If there is a gap, design a small request app and an approval flow rather than replacing procurement.</li>
<li><strong>Integrate through a supported contract.</strong> Validate input, authenticate the caller and create the purchasing object via an appropriate released API. Keep the purchasing system as the transaction owner.</li>
<li><strong>Control failure.</strong> Preserve the request ID, correlate technical calls, avoid duplicate creation, route failures to a responsible team and reconcile incomplete cases.</li>
<li><strong>Govern and measure.</strong> Record application ownership and change impact, test end to end in Cloud ALM where applicable, support users and measure outcomes after rollout.</li>
</ol>
<p>Possible implementation tools are SAP Build for a request UI or workflow and SAP Integration Suite for mediation. They are <em>options</em>, not mandatory products for every scenario.</p>
<p><strong>Illustrative targets only:</strong> A hypothetical baseline might show 30% of requests outside the policy, with a target of 5%. Those numbers are an example of how to frame success, not measured client results. Real targets require baseline evidence and an agreed KPI definition.</p>
<p><strong>Lead decision:</strong> Would this extension create less complexity than standard SAP functionality, training or a process change? If not, reject the extension.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="client-explanation" aria-labelledby="client-explanation-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">13 / Communication</p><h2 id="client-explanation-title">How to explain the architecture to a client</h2></header><div class="signavio-reader__content">
<h3>30-second explanation</h3>
<p>“We start with what the business needs to improve. SAP Signavio helps us understand the process, while SAP LeanIX shows which applications support it. We use SAP reference architecture to connect that business need to a possible solution. BTP gives us options for extensions and integrations where standard applications have a gap. We then check security, costs, operating responsibility and measurable results.”</p>
<h3>90-second explanation</h3>
<p>“I would first agree on the business outcome and the current process. Then I would identify the business capability, the process activities and the applications involved. This tells us where ownership sits and whether the problem comes from the process, data, integration or missing functionality. Next I compare standard SAP capability with in-app and side-by-side extension options. If we need BTP, I select the concrete runtime and services, check identity and entitlements, and document the API and data contracts. Finally, I define tests, monitoring, recovery and the KPI that will show whether the change worked. The output is a supportable solution, not just a technical diagram.”</p>
<h3>Three questions to ask the customer</h3>
<ul><li>Which business result must improve, and what is the current baseline?</li><li>Which system owns each official business document or master data object?</li><li>What happens when the integration, workflow or AI step fails?</li></ul>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="interview" aria-labelledby="interview-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">14 / Self-check</p><h2 id="interview-title">Assessment questions: answer with a decision</h2></header><div class="signavio-reader__content">
<ol>
<li><strong>What is the difference between an EA and an SA?</strong><p>EA defines enterprise-wide direction and governance. SA designs a specific solution within business, technical and delivery constraints. They exchange feedback.</p></li>
<li><strong>Capability versus process?</strong><p>Capability is what the company must be able to do; process is the sequence of activities used to deliver an outcome. A capability may support several processes.</p></li>
<li><strong>RBA versus RSA?</strong><p>RBA uses business language for capabilities and processes. RSA describes software capabilities, solution components, process implementation and data flows that support them.</p></li>
<li><strong>What is the difference between a solution value flow and a process flow?</strong><p>The value flow explains the high-level contribution to business value. The process flow details activities, order and integration handoffs.</p></li>
<li><strong>What is the SAP EA Framework made of?</strong><p>Methodology, Reference Architecture Content, Tooling, Practice and Services.</p></li>
<li><strong>Is SAP Business AI Platform the same as SAP BTP?</strong><p>No. In SAP's 2026 positioning, Business AI Platform is the broader portfolio. BTP remains the platform foundation and one of its parts.</p></li>
<li><strong>Where are BTP applications deployed?</strong><p>Into a regional subaccount using a suitable environment. Cloud Foundry uses orgs/spaces; Kyma uses clusters/namespaces. Managed service subscriptions follow their own model.</p></li>
<li><strong>Does side-by-side automatically mean clean core?</strong><p>No. The solution still needs released interfaces, clear ownership, secure access, controlled coupling and an operational recovery path.</p></li>
</ol>
<p><strong>Practice variation:</strong> The customer already has a standard S/4HANA approval function. Would you still propose a custom BTP workflow? Explain the cost, support risk and evidence required before choosing the custom option.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="next" aria-labelledby="next-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">15 / Learning sequence</p><h2 id="next-title">What we will study next</h2></header><div class="signavio-reader__content">
<p>This guide is the architecture foundation. The next BTP lessons should deepen the areas that determine whether a platform solution can be deployed and operated.</p>
<div class="table-scroll study-table" role="region" aria-label="BTP study sequence" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Topic</th><th scope="col">What you should be able to decide</th></tr></thead><tbody><tr><td>1. Platform administration</td><td>Design account, region, service and cost boundaries.</td></tr>
<tr><td>2. Identity and connectivity</td><td>Explain trust, destinations, roles and private-network access.</td></tr>
<tr><td>3. Extensions and runtimes</td><td>Compare CAP, ABAP Cloud/RAP, Cloud Foundry and Kyma where relevant.</td></tr>
<tr><td>4. Integration design</td><td>Choose APIs, events, iFlows and recovery patterns.</td></tr>
<tr><td>5. Data and AI architecture</td><td>Choose data access, grounding, governance and evaluations for AI.</td></tr>
<tr><td>6. Delivery and operations</td><td>Define lifecycle, monitoring, security, ownership and service evidence.</td></tr></tbody></table></div>
<p>Use this page as the continuing reference. Add new material to the relevant chapter only when it improves an explanation, design choice or assessment answer.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="sources" aria-labelledby="sources-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">16 / Evidence</p><h2 id="sources-title">Sources and what must be checked</h2></header><div class="signavio-reader__content">
<p>This is an independent study guide based on SAP public learning and help content, rewritten for comprehension. It is not an official certification guide or a statement of contractual product availability.</p>
<ul>
<li><a href="https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/investigating-the-sap-enterprise-architecture-methodology">SAP Learning — EA methodology and architect roles</a></li>
<li><a href="https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/outlining-the-sap-enterprise-architecture-framework">SAP Learning — SAP EA Framework and its pillars</a></li>
<li><a href="https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content">SAP Learning — Reference Business and Solution Architecture</a></li>
<li><a href="https://learning.sap.com/courses/exploring-sap-reference-content-as-enterprise-architect/structuring-sap-reference-architecture-from-business-to-solution">SAP Learning — Reference architecture content and process mapping</a></li>
<li><a href="https://help.sap.com/docs/btp/sap-business-technology-platform/account-model">SAP Help — BTP account model</a></li>
<li><a href="https://help.sap.com/docs/btp/btp-admin-guide/setting-up-your-account-model">SAP Help — BTP landscape structure</a></li>
<li><a href="https://events.sap.com/sap-user-groups/en_us/sap_btp.html">SAP — Business AI Platform and SAP BTP positioning in 2026</a></li>
<li><a href="https://architecture.learning.sap.com/docs/ai-native-north-star-architecture/executive-summary">SAP Architecture Center — AI-native architecture</a></li>
</ul>
<p><strong>Verification boundary:</strong> Always check the exact SAP edition, release, commercial plan, region, service availability and published interface before making a delivery commitment. SAP's product naming and reference catalog can change. This page remains in review until a separate human publication check.</p>
</div></section>
<section class="research-canvas__inventory signavio-reader__related" aria-labelledby="btp-related-title">
<header><p class="research-canvas__eyebrow">Continue learning</p><h2 id="btp-related-title">Related study guides</h2></header>
<div class="research-route-list">
<a href="/atlas/sap/sap-signavio/"><span>PROCESS</span><strong>SAP Signavio</strong><small>Process modeling, business value, process governance and process intelligence.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
<a href="/labs/assessment/"><span>LEAD</span><strong>SAP Lead Assessment</strong><small>Practice ownership, trade-offs, integration, architecture and operational reasoning.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
<a href="/atlas/sap/sap-integration-suite/"><span>INT</span><strong>SAP Integration Suite</strong><small>APIs, integration flows, events and operational interface design.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
<a href="/labs/business-ai/"><span>AI</span><strong>Business AI Lab</strong><small>AI architecture, business context, guardrails and implementation trade-offs.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
</div>
</section>
<div class="research-canvas__support">{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</article>
