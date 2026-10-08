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
<section class="signavio-reader__toc-group" aria-labelledby="btp-route-resources"><h3 id="btp-route-resources">Architecture toolkit</h3><ol>
<li><a href="#btp-guidance">Where to find SAP architecture guidance</a></li>
<li><a href="#btp-methods">Decision guides and methodologies</a></li>
<li><a href="#btp-design-evidence">Diagram, cost and security evidence</a></li>
</ol></section>
<section class="signavio-reader__toc-group" aria-labelledby="btp-route-build"><h3 id="btp-route-build">Build · design and develop</h3><ol>
<li><a href="#build-clean-core">Clean core and extension choice</a></li>
<li><a href="#build-tools">SAP Build vs Joule Studio</a></li>
<li><a href="#build-runtimes">Runtime, CAP and RAP</a></li>
<li><a href="#build-experience">Fiori, Work Zone and mobile</a></li>
</ol></section>
<section class="signavio-reader__toc-group" aria-labelledby="btp-route-integrate"><h3 id="btp-route-integrate">Build · integrate and operate</h3><ol>
<li><a href="#build-integration-strategy">Integration architecture choices</a></li>
<li><a href="#build-integration-suite">Integration Suite components</a></li>
<li><a href="#build-events-agents">Events, MCP and agents</a></li>
<li><a href="#build-operations">Delivery, monitoring and recovery</a></li>
</ol></section>
<section class="signavio-reader__toc-group" aria-labelledby="btp-route-context-data"><h3 id="btp-route-context-data">Contextualize &amp; Reason / Data</h3><ol>
<li><a href="#context-why">Why business context matters</a></li>
<li><a href="#context-language">Data architecture terminology</a></li>
<li><a href="#context-data-products">Data product contract</a></li>
<li><a href="#context-products">Which data service owns what?</a></li>
</ol></section>
<section class="signavio-reader__toc-group" aria-labelledby="btp-route-context-ai"><h3 id="btp-route-context-ai">Contextualize &amp; Reason / AI</h3><ol>
<li><a href="#context-bdc">Business Data Cloud architecture</a></li>
<li><a href="#context-knowledge-models">Knowledge Graph vs SAP-RPT</a></li>
<li><a href="#context-case">Supplier disruption case</a></li>
</ol></section>
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
<p>In the SAP Learning material, BPM is grouped into eight end-to-end process groups. Examples include Source-to-Pay, Lead-to-Cash, Plan-to-Fulfill and Recruit-to-Retire. Study the process hierarchy first; catalog groupings and names may evolve between SAP reference content versions.</p>
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
<p>The three solution diagrams to recognize first are <strong>Solution Value Flow</strong>, <strong>Solution Process Flow</strong> and <strong>Solution Component</strong>. The Solution Data Flow Diagram adds data movement. A Business Value Flow belongs to the business view and should not be confused with a solution flow.</p>
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

<section class="research-canvas__inventory signavio-reader__section" id="btp-guidance" aria-labelledby="btp-guidance-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">13 / Find the right resource</p><h2 id="btp-guidance-title">Start with the architecture question, then open the right SAP resource</h2></header><div class="signavio-reader__content">

<p>These resources have different jobs. A <strong>methodology</strong> gives you a repeatable way to decide. A <strong>reference architecture</strong> shows an established pattern. A <strong>catalog</strong> helps you find real services and interfaces. A <strong>solution diagram</strong> records your proposed design. Mixing them up leads to diagrams without clear decisions.</p>
<div class="table-scroll study-table" role="region" aria-label="Where SAP architects should look first" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Resource</th><th scope="col">Architect's question</th><th scope="col">What you should take away</th></tr></thead><tbody>
<tr><td><a href="https://discovery-center.cloud.sap/">SAP Discovery Center</a></td><td>Which BTP services or guided missions fit the use case?</td><td>Service catalog, missions, regional service details and estimation entry points.</td></tr>
<tr><td><a href="https://help.sap.com/docs/sap_btp_guidance_framework/97dc5926388343be94efd10ae3db716c/what-is-sap-btp-guidance-framework">SAP BTP Guidance Framework</a></td><td>How do I choose an approach instead of guessing a product?</td><td>Decision guides, reference architectures, methodologies, recommendations and DevOps guidance. Access the current content through Discovery Center.</td></tr>
<tr><td><a href="https://api.sap.com/">SAP Business Accelerator Hub</a></td><td>Is there a suitable published interface or reusable integration?</td><td>API and event specifications, integration packages and other product-specific artifacts.</td></tr>
<tr><td><a href="https://architecture.learning.sap.com/docs/ref-arch">SAP Architecture Center</a></td><td>What architecture pattern can I start from?</td><td>Reference architectures, explanations of components, relationships and design considerations.</td></tr>
<tr><td><a href="https://sap.github.io/btp-solution-diagrams/">SAP BTP Solution Diagram Guidelines</a></td><td>How should I communicate the selected solution?</td><td>Diagram notation, examples and editable source templates. A diagram must still reflect the real landscape.</td></tr>
<tr><td><a href="https://www.sap.com/about/trust-center.html">SAP Trust Center</a></td><td>What SAP security, compliance or availability evidence exists?</td><td>SAP cloud controls, certifications, privacy information, agreements and service status. Check product scope.</td></tr>
</tbody></table></div>
<p><strong>2026 update:</strong> SAP Help states that updates to the SAP BTP Guidance Framework are now provided through <a href="https://discovery-center.cloud.sap/">SAP Discovery Center</a>. Use the older Help page for definitions, but follow the Discovery Center for the current material.</p>
<h3>Five parts of the Guidance Framework</h3>
<div class="table-scroll study-table" role="region" aria-label="Five kinds of BTP guidance" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Part</th><th scope="col">Plain-English meaning</th><th scope="col">Use it to</th></tr></thead><tbody>
<tr><td>Decision guides</td><td>Compare viable technology options.</td><td>Choose an extension or integration approach.</td></tr>
<tr><td>Reference architectures</td><td>See a reusable solution pattern.</td><td>Understand components and typical relationships.</td></tr>
<tr><td>Methodologies</td><td>Follow an agreed decision process.</td><td>Make team choices consistent and explainable.</td></tr>
<tr><td>Recommendations</td><td>Review domain-specific safeguards.</td><td>Check security, operations and other implementation choices.</td></tr>
<tr><td>DevOps principles</td><td>Connect development with deployment and support.</td><td>Design testing, delivery, automation, monitoring and recovery.</td></tr>
</tbody></table></div>
<p><strong>First step for a Lead:</strong> Write the business need and the decision you must make. Do not start by searching for a BTP service name.</p>

</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="btp-methods" aria-labelledby="btp-methods-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">14 / Choose a method</p><h2 id="btp-methods-title">Choose a methodology before choosing the product</h2></header><div class="signavio-reader__content">

<p>Use the guide that matches your decision. Some guides describe technology choices; methodologies describe how your organization should reach and govern those choices.</p>
<div class="table-scroll study-table" role="region" aria-label="SAP architecture guides and methods" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">When the question is...</th><th scope="col">Read</th><th scope="col">Expected result</th></tr></thead><tbody>
<tr><td>Should an extension run on-stack or side-by-side?</td><td><a href='https://help.sap.com/docs/sap-btp-guidance-framework/extension-architecture-guide/what-is-extension-architecture-guide'>Extension Architecture Guide</a></td><td>A justified extension option that fits the ERP edition and clean-core boundaries.</td></tr>
<tr><td>How do we assess an extension consistently?</td><td><a href='https://help.sap.com/docs/sap-btp-guidance-framework/sap-application-extension-methodology/cd2664b67373452ab78825897ff99a81.html'>SAP Application Extension Methodology</a></td><td>Use case → extension tasks → technical building blocks → target solution.</td></tr>
<tr><td>Which integration style and platform are appropriate?</td><td><a href='https://help.sap.com/docs/sap-btp-guidance-framework/integration-architecture-guide/sap-integration-solution-advisory-methodology'>Integration Architecture Guide / ISA-M</a></td><td>Integration domains, patterns, technical mapping and governance decisions.</td></tr>
<tr><td>How should an app be implemented and delivered?</td><td><a href='https://help.sap.com/docs/btp/btp-developers-guide/discover'>SAP BTP Developer's Guide</a></td><td>Development, infrastructure, integration and delivery design.</td></tr>
<tr><td>How should a data and analytics solution be planned?</td><td><a href='https://help.sap.com/docs/sap-btp-guidance-framework/sap-data-methodology/sap-data-analytics-advisory-methodology-overview'>Data &amp; Analytics Advisory Methodology</a></td><td>Business outcomes, data capabilities, use-case patterns, architecture and governance.</td></tr>
</tbody></table></div>
<h3>Two approaches worth remembering</h3>
<p><strong>Extension methodology:</strong> Assess the business use case, assess extension technologies, then define the target solution. For a request-approval scenario, separate the presentation need, workflow logic and ERP transaction before choosing SAP Build, CAP or other components. The standard ERP capability is still an option.</p>
<p><strong>Integration Solution Advisory Methodology (ISA-M):</strong> First decide the integration domain and style, such as application-to-application process integration, data replication or analytics integration. Then check the required characteristics and map the need to technology. A direct API, middleware flow and event-based interaction are alternatives to evaluate, not a fixed sequence that every interface must use.</p>
<p><strong>Lead-level point:</strong> “I first classify the problem without a product name. Then I compare suitable technologies and document the decision, constraints and operating responsibilities.”</p>

</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="btp-design-evidence" aria-labelledby="btp-design-evidence-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">15 / Apply the guidance</p><h2 id="btp-design-evidence-title">Turn the reference architecture into a defensible solution</h2></header><div class="signavio-reader__content">

<p>A good architecture is not complete when the drawing looks finished. It is complete enough to implement when the team can explain component ownership, dependencies, how failure is handled, expected cost and how success will be verified.</p>
<h3>A six-step route for a real SAP use case</h3>
<ol>
<li><strong>Describe the outcome and scope.</strong> Example: employees need a controlled way to request items that are not in the catalog. Define approvals, users, business rules and the purchasing system that owns the official document.</li>
<li><strong>Choose the pattern.</strong> Check standard S/4HANA functions first. If an extension is justified, use the extension guide and relevant reference architecture to compare on-stack and side-by-side options.</li>
<li><strong>Prove the interface.</strong> Search <a href="https://api.sap.com/">SAP Business Accelerator Hub</a> for an API or event matching the product and edition. Verify the required operation, communication scenario, authentication, data fields and limitations. A catalog entry does not mean the interface is available or configured in the target tenant.</li>
<li><strong>Draw the actual boundaries.</strong> Identify the user entry point, workflow owner, integration components if needed, S/4HANA transaction owner, identity, data stores and monitoring. Label each arrow with the interaction and protocol where known.</li>
<li><strong>Estimate the service consumption.</strong> Create a service inventory from the chosen diagram. Check the relevant region, commercial model, service plan, usage metric, sizing, support and operations. Use the estimator in <a href="https://discovery-center.cloud.sap/">Discovery Center</a> as a planning aid, not a quotation.</li>
<li><strong>Validate security and completion.</strong> Use the <a href="https://www.sap.com/about/trust-center.html">SAP Trust Center</a> for SAP-managed control evidence and <a href="https://help.sap.com/docs/btp/sap-btp-security-recommendations-c8a9bb59fe624f0981efa0eff2497d7d/sap-btp-security-recommendations">BTP Security Recommendations</a> for customer-side checks. Test access, failed calls, retries, duplicate prevention, reconciliation and business confirmation.</li>
</ol>
<h3>Example: the important relationships, not product icons</h3>
<div class="table-scroll study-table" role="region" aria-label="Procurement solution relationships" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">From</th><th scope="col">Relationship</th><th scope="col">To / owner</th></tr></thead><tbody>
<tr><td>Employee</td><td>Submits the request; sees a clear status.</td><td>Request interface / workflow, if a new interface is justified.</td></tr>
<tr><td>Request interface</td><td>Sends approved, validated input through a released contract.</td><td>SAP S/4HANA purchasing; system of record for the purchase requisition.</td></tr>
<tr><td>Integration layer (if needed)</td><td>Maps, protects and monitors the cross-system call.</td><td>The published ERP API and the originating request.</td></tr>
<tr><td>S/4HANA</td><td>Returns the business document ID or a business error.</td><td>Request tracking and reconciliation.</td></tr>
<tr><td>Operations</td><td>Checks missing, failed or duplicate results.</td><td>An accountable support owner; business process completion.</td></tr>
</tbody></table></div>
<p>This is a <strong>logical relationship map</strong>, not a claim that SAP Integration Suite or a custom app is mandatory. The actual solution might be smaller if standard SAP functionality meets the requirement.</p>
<h3>Which diagram is needed?</h3>
<div class="table-scroll study-table" role="region" aria-label="Distinguish technical architecture artifacts" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Artifact</th><th scope="col">Best for</th><th scope="col">What it cannot prove alone</th></tr></thead><tbody>
<tr><td>Reference architecture</td><td>Starting from an established reusable pattern.</td><td>That a specific customer's interface, plan or security configuration is ready.</td></tr>
<tr><td>Customer solution diagram</td><td>Agreeing on in-scope systems, BTP services, flows and boundaries.</td><td>Detailed payload mappings, runtime status or completed transactions.</td></tr>
<tr><td>Detailed technical model (TAM-style)</td><td>Documenting exact component dependencies, technical configuration and constraints.</td><td>That the business outcome was achieved.</td></tr>
<tr><td>Interface contract and test evidence</td><td>Proving endpoints, payloads, authorization, retries and business acknowledgments.</td><td>That the full architecture remains cost-effective over time.</td></tr>
</tbody></table></div>
<p><strong>Service inventory is not automatically a formal SBOM.</strong> List the BTP services needed for cost estimation; separately maintain software dependencies, versions and licenses when an SBOM is required.</p>
<p><strong>Final check:</strong> A technical HTTP success is not enough. The team must verify the expected business document and provide a recovery route when that document was not created.</p>

</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="build-clean-core" aria-labelledby="build-clean-core-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">16 / Extensibility</p><h2 id="build-clean-core-title">Clean core: where should an extension live?</h2></header><div class="signavio-reader__content">
<p>A clean core aims to keep an ERP system easier to upgrade and operate. It covers five connected areas: <strong>processes, extensions, data, integrations and operations</strong>. Moving code to BTP helps in some cases, but it does not remove the need for stable APIs, clear ownership and recovery.</p>
<h3>Decide whether an extension is needed</h3>
<div class="table-scroll study-table" role="region" aria-label="Extensibility decisions for SAP Cloud ERP" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Option</th><th scope="col">What it means</th><th scope="col">Use when</th></tr></thead><tbody>
<tr><td>Standard process or configuration</td><td>Use supported application behavior before writing new code.</td><td>The requirement can be met without an extension.</td></tr>
<tr><td>Key-user extensibility (on-stack)</td><td>Add a supported field, business logic or UI adjustment using provided tools.</td><td>A small change belongs close to the ERP transaction.</td></tr>
<tr><td>Developer extensibility (on-stack)</td><td>Use ABAP Cloud and released SAP objects, where supported by the ERP edition.</td><td>The application needs tight ERP business-object behavior.</td></tr>
<tr><td>Side-by-side extensibility (outside ERP)</td><td>Run an application or service on BTP, connected through supported contracts.</td><td>The solution spans systems, needs an independent lifecycle or has different runtime requirements.</td></tr>
</tbody></table></div>
<p><strong>One example:</strong> If a buyer needs one extra field in an SAP purchase requisition, first check supported in-app extensibility. If a non-standard request process spans SAP and a supplier portal, a side-by-side solution may fit. Do not create a second purchase-requisition system: the ERP should remain the transaction owner when it is the system of record.</p>
<h3>Clean core levels: A to D</h3>
<div class="table-scroll study-table" role="region" aria-label="SAP clean core extension levels" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Level</th><th scope="col">Meaning</th><th scope="col">Design response</th></tr></thead><tbody>
<tr><td>A</td><td>Uses released, upgrade-stable interfaces and recommended extension methods.</td><td>Preferred baseline.</td></tr>
<tr><td>B</td><td>Also uses documented classic APIs and technologies considered suitable for extension.</td><td>Accept with documented scope, supportability and checks.</td></tr>
<tr><td>C</td><td>Uses internal, unreleased SAP objects where legacy needs require them.</td><td>Treat as upgrade risk; plan monitoring and remediation.</td></tr>
<tr><td>D</td><td>Uses non-recommended techniques such as modifications or unsafe direct table changes.</td><td>Avoid and prioritize replacement.</td></tr>
</tbody></table></div>
<p>Levels A–D are an architecture and quality classification, not a claim that every technique is allowed in every deployment model. SAP Cloud ERP public edition has stricter extension boundaries than private edition or on-premise. Check the target edition, release and the actual API release contract.</p>
<p><strong>Lead answer:</strong> “I use the smallest supported extension that meets the requirement, document the clean-core impact and verify the process after an upgrade.”</p>
<p>Details: <a href="https://news.sap.com/2025/08/extend-sap-s4hana-cloud-right-way-clean-clear/">SAP clean core levels</a> and <a href="https://help.sap.com/docs/abap-cloud/abap-cloud/extensibility">SAP extensibility options</a>.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="build-tools" aria-labelledby="build-tools-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">17 / Development choices</p><h2 id="build-tools-title">SAP Build and Joule Studio: similar goals, different models</h2></header><div class="signavio-reader__content">
<p>Separate <strong>what is being built</strong> from <strong>who manages its runtime</strong>. A Fiori app, a business approval, a CAP service and an AI agent do not require the same tools or operating model.</p>
<div class="table-scroll study-table" role="region" aria-label="Development products compared" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Product or tool</th><th scope="col">Main purpose</th><th scope="col">Architect's boundary</th></tr></thead><tbody>
<tr><td>SAP Build Process Automation</td><td>Business workflows, approvals and task automation.</td><td>Rules and approval authority remain explicit; not every workflow needs an AI agent.</td></tr>
<tr><td>SAP Build Code</td><td>Pro-code applications and extensions, including CAP-based development.</td><td>Define service contracts, persistence, tests and deployment responsibilities.</td></tr>
<tr><td>ABAP Development Tools (ADT)</td><td>Develop ABAP Cloud and RAP artifacts for an ABAP target.</td><td>ADT is an IDE, not an application runtime.</td></tr>
<tr><td>SAP Build Work Zone</td><td>Provide role-based sites and application access.</td><td>A portal does not become the transaction owner.</td></tr>
<tr><td>Joule Studio, classic edition</td><td>Existing customer-managed Joule agent and skill development in SAP Build.</td><td>Check lifecycle and available migration options before extending existing work.</td></tr>
<tr><td>Joule Studio (new, SAP-managed offering)</td><td>AI-first development of agents, applications and workflows using business intent.</td><td>Check availability, managed-runtime scope, agent evaluation and contract before choosing it.</td></tr>
</tbody></table></div>
<p><strong>Current product distinction:</strong> SAP announced the new Joule Studio at SAP Sapphire 2026. Existing SAP Build development remains a valid option, and the new offering is not a reason to rebuild stable applications. SAP also retired <em>SAP Build Apps as a standalone product</em> on 23 March 2026; existing contracts remain supported for their duration. Do not recommend it as an unchanged new standalone purchase.</p>
<h3>What “intent-based development” changes</h3>
<p>A traditional project starts by specifying screens, database tables and program logic. An intent-based project starts with a goal, such as “help a buyer resolve delivery delays”. It can then propose requirements, architecture, implementation and tests. Those outputs still need review.</p>
<p><strong>Intent → requirements → solution design → code or workflow → tests and agent evaluation → deployment → monitoring.</strong></p>
<p>For SAP scenarios, process facts from Signavio, application dependencies from LeanIX and released ERP interfaces may help create useful context. A generated design is still a proposal: the architect must check data access, authorization, error recovery, lifecycle and measurable business results.</p>
<p><strong>Lead answer:</strong> “Use Build for established apps and automation where it fits. Consider new Joule Studio for AI-first use cases, but make the choice from capabilities, operating model, risk and commercial availability.”</p>
<p>Sources: <a href="https://news.sap.com/2026/05/new-joule-studio-enterprise-scale-agentic-development/">SAP announcement on Joule Studio</a> and <a href="https://community.sap.com/t5/technology-blog-posts-by-sap/sap-build-apps-deprecation-and-the-path-forward/bc-p/14357348/highlight/true">SAP Build Apps transition</a>.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="build-runtimes" aria-labelledby="build-runtimes-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">18 / Runtime and programming</p><h2 id="build-runtimes-title">Cloud Foundry, Kyma, ABAP, CAP and RAP: keep the terms separate</h2></header><div class="signavio-reader__content">
<p>A <strong>runtime</strong> is where software executes. A <strong>programming model</strong> gives developers a structured way to build it. An <strong>IDE</strong> is the tool where they write and test code. Confusing these three leads to incorrect architecture choices.</p>
<div class="table-scroll study-table" role="region" aria-label="Runtime choices in SAP BTP" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Runtime</th><th scope="col">Where it fits</th><th scope="col">Main trade-off</th></tr></thead><tbody>
<tr><td>Cloud Foundry</td><td>Managed deployment for cloud applications and services; often used with CAP.</td><td>Less container infrastructure work than self-managed Kubernetes, but runtime rules and quotas apply.</td></tr>
<tr><td>Kyma</td><td>Managed Kubernetes environment for containerized and event-oriented workloads.</td><td>More flexibility for containers and orchestration; also more operational complexity.</td></tr>
<tr><td>SAP BTP ABAP environment</td><td>ABAP Cloud development and runtime with RAP, CDS and released APIs.</td><td>Good for ABAP-oriented transactional services; different language and lifecycle constraints.</td></tr>
<tr><td>Joule Studio runtime (SAP-managed)</td><td>Managed execution model associated with the new Joule Studio offering.</td><td>Check supported workloads, release availability, policy controls and pricing.</td></tr>
</tbody></table></div>
<h3>CAP and RAP are not competing cloud providers</h3>
<div class="table-scroll study-table" role="region" aria-label="CAP versus RAP" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Question</th><th scope="col">CAP</th><th scope="col">RAP</th></tr></thead><tbody>
<tr><td>What is it?</td><td>SAP Cloud Application Programming Model.</td><td>ABAP RESTful Application Programming Model.</td></tr>
<tr><td>Main languages</td><td>Node.js and Java services; CDS domain modeling.</td><td>ABAP Cloud and ABAP CDS business-object modeling.</td></tr>
<tr><td>Typical target</td><td>Cloud Foundry or Kyma.</td><td>SAP BTP ABAP environment or a supported S/4HANA ABAP stack.</td></tr>
<tr><td>Main strengths</td><td>Business services and cross-system extensions using cloud development.</td><td>Transactional business objects, behavior and released ABAP services.</td></tr>
<tr><td>Key concern</td><td>Define domain ownership, service API and persistence.</td><td>Use released objects and the applicable ABAP extensibility model.</td></tr>
</tbody></table></div>
<p>Both can support SAP Fiori applications, but <strong>SAP Fiori is the UX design approach</strong>; SAPUI5 and Fiori elements are UI technologies. Fiori is not a fourth backend runtime.</p>
<p><strong>Procurement example:</strong> A cross-system request service may use CAP on Cloud Foundry. A tightly connected ERP business-object extension may use RAP in the ABAP stack. The same business process does not dictate the same technical choice for every customer.</p>
<p>Read further: <a href="/atlas/sap/cap/">CAP</a>, <a href="/atlas/sap/rap/">RAP</a>, <a href="https://help.sap.com/docs/btp/btp-developers-guide/understanding-available-technology">SAP runtime decision guidance</a>.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="build-experience" aria-labelledby="build-experience-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">19 / User experience</p><h2 id="build-experience-title">Choose the user entry point and mobile approach</h2></header><div class="signavio-reader__content">
<p>An architect separates the <strong>front door</strong> from the <strong>business application</strong>. A launchpad, a mobile shell and a task inbox can help users reach work, but they do not replace the SAP system that owns the business transaction.</p>
<div class="table-scroll study-table" role="region" aria-label="SAP entry points and mobile tools" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Need</th><th scope="col">Consider</th><th scope="col">Remember</th></tr></thead><tbody>
<tr><td>Role-based launchpad for applications</td><td>SAP Build Work Zone, standard edition.</td><td>A central way to launch and organize apps.</td></tr>
<tr><td>Teams need structured workspaces, shared content and collaboration</td><td>SAP Build Work Zone, advanced edition.</td><td>Additional collaboration and content features; check edition scope.</td></tr>
<tr><td>Tasks from several systems in one inbox</td><td>SAP Task Center, where the sources are supported.</td><td>The original application usually owns the task execution and its business state.</td></tr>
<tr><td>Mobile entry point to tasks and business content</td><td>Joule Work mobile app (formerly SAP Mobile Start).</td><td>Product naming and experiences are evolving; check current mobile documentation.</td></tr>
<tr><td>Custom mobile app with shared cross-platform metadata</td><td>SAP Mobile Development Kit (MDK) with Mobile Services.</td><td>Useful for metadata-driven mobile experiences, including supported offline scenarios.</td></tr>
<tr><td>Native iOS or Android capabilities</td><td>SAP BTP SDK for iOS or Android, with Mobile Services.</td><td>Use when device integration, offline work or native UX requirements justify the cost.</td></tr>
</tbody></table></div>
<p><strong>Mobile Services</strong> provides backend capabilities such as connectivity, onboarding, push notifications and offline synchronization for supported mobile applications. The user-facing app, the backend service and the ERP transaction remain different components.</p>
<p><strong>Lead question:</strong> A warehouse worker needs to approve or record a stock-related task while offline. Which component presents the UI, which handles offline synchronization, and which system validates and posts the actual inventory movement?</p>
<p>See <a href="https://help.sap.com/docs/joule-work-mobile/administration-guide-sap-build-work-zone-setup/overview">SAP Joule Work mobile guidance</a> and <a href="https://help.sap.com/docs/build-work-zone-standard-edition">SAP Build Work Zone</a>.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="build-integration-strategy" aria-labelledby="build-integration-strategy-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">20 / Integration design</p><h2 id="build-integration-strategy-title">Choose an integration style from the business dependency</h2></header><div class="signavio-reader__content">
<p>Enterprise integration connects processes, applications and data across organizational boundaries. An API, an event, a file and a data pipeline solve different problems. A good integration strategy defines when each is allowed, which team owns it and how failures can be recovered.</p>
<div class="table-scroll study-table" role="region" aria-label="Common enterprise integration styles" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Business need</th><th scope="col">Candidate style</th><th scope="col">What must be designed</th></tr></thead><tbody>
<tr><td>Request a price or create a document with an immediate answer</td><td>Synchronous API / request-response.</td><td>Authentication, timeout, retries, duplicate prevention and business response.</td></tr>
<tr><td>Tell other systems that an order status changed</td><td>Event-driven, asynchronous.</td><td>Producer, broker, consumers, event contract, idempotency and eventual consistency.</td></tr>
<tr><td>Exchange purchase-order documents with a supplier</td><td>B2B / EDI or supported partner integration.</td><td>Partner agreement, standards, mapping, acknowledgments and exceptions.</td></tr>
<tr><td>Move large datasets for analytics</td><td>Data integration, replication or federation.</td><td>Freshness, lineage, ownership and reconciliation.</td></tr>
<tr><td>Connect an established on-premise interface</td><td>Supported hybrid connection or integration runtime.</td><td>Network, security, availability, migration and monitoring.</td></tr>
</tbody></table></div>
<p>SAP's <strong>Integration Solution Advisory Methodology (ISA-M)</strong> gives an organization a common way to classify integration scenarios and map them to approved patterns and technologies. An Integration Center of Excellence can maintain the patterns, controls, ownership and reusable assets. It should enable teams, not force middleware into every connection.</p>
<p><strong>Important distinction:</strong> Application-to-application integration is sometimes abbreviated A2A. Agent-to-agent integration is also called A2A in agent protocols. Always say which one you mean.</p>
<p><strong>Example:</strong> A buyer submitting a request needs confirmation that the ERP created the document; a synchronous API may be suitable. Updating an analytics dashboard after creation might work well with an event. They can be part of the same process without using the same integration style.</p>
<p>See <a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite concepts</a> and <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/integration-flow-extension-d3741720e29842e4bf547dcd66139f7f-774">SAP's Integration Suite overview</a>.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="build-integration-suite" aria-labelledby="build-integration-suite-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">21 / Integration components</p><h2 id="build-integration-suite-title">SAP Integration Suite: name the component, not just the suite</h2></header><div class="signavio-reader__content">
<p>SAP Integration Suite offers several capabilities. Choose each for a specific job, and remember that <strong>delivery of a message is not the same as completion of a business transaction</strong>.</p>
<div class="table-scroll study-table" role="region" aria-label="Integration Suite components and boundaries" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Capability</th><th scope="col">What it does</th><th scope="col">Key design question</th></tr></thead><tbody>
<tr><td>Cloud Integration</td><td>Build and run message flows (iFlows), with adapters, routing and transformations.</td><td>Where do we correlate, monitor, retry and recover a message?</td></tr>
<tr><td>API Management</td><td>Secure, publish, manage and monitor API consumption.</td><td>Which consumer policies, versions and access rules apply?</td></tr>
<tr><td>Integration Advisor</td><td>Help define structured B2B message formats and mappings.</td><td>What are the partner message structures and validation rules?</td></tr>
<tr><td>Integration Assessment</td><td>Apply ISA-M to document integration scenarios and technology decisions.</td><td>Why was this integration style selected?</td></tr>
<tr><td>Migration Assessment</td><td>Assess existing SAP PI/PO scenarios for migration effort and limitations.</td><td>Which interfaces should migrate, change or retire?</td></tr>
<tr><td>Open Connectors</td><td>Connect to supported third-party SaaS applications.</td><td>Is an appropriate connector available under the target plan?</td></tr>
<tr><td>Edge Integration Cell</td><td>Run supported integration processing in a customer-managed location.</td><td>Do latency, sovereignty or network constraints require local processing?</td></tr>
<tr><td>MCP gateway</td><td>Expose supported enterprise API capabilities as MCP tools for agents.</td><td>Who may call the tool, with what scope and control?</td></tr>
</tbody></table></div>
<h3>How an iFlow works</h3>
<p><strong>Sender → inbound adapter → validation → mapping / routing → receiver adapter → receiving application.</strong> An iFlow can include error handling, logging, stores and additional calls. The sender and receiver contracts must be defined separately from the graphical flow.</p>
<p>Cloud Integration may offer <strong>Best Effort (BE), Exactly Once (EO) and Exactly Once In Order (EOIO)</strong> qualities for supported adapters and scenarios. These describe message-processing behavior and do not automatically prove that the business process ran exactly once. A second purchase requisition after a timeout is still possible unless the design handles idempotency and reconciliation.</p>
<h3>Do not confuse these supporting concepts</h3>
<p><strong>MIG</strong> (Message Implementation Guideline) describes the message structure and constraints for a partner interface. <strong>MAG</strong> (Mapping Guideline) maps source and target structures. SAP Application Interface Framework (<strong>AIF</strong>) operates in supported SAP backend scenarios to help monitor, analyze, correct and reprocess application-level interface messages; it is not a replacement for middleware.</p>
<p>For SAP PI/PO modernization, first assess the current scenario, its business owner, interface contract and relevance. Then decide whether an existing pattern can be migrated, must be adjusted or should be redesigned. Use regression tests to prove the outcome.</p>
<p>Further detail: <a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite in Atlas</a>, <a href="https://help.sap.com/docs/cloud-integration/sap-cloud-integration/what-is-sap-cloud-integration">Cloud Integration</a>, <a href="https://help.sap.com/docs/integration-suite/isuite-integrations-and-apis/model-context-protocol-mcp">MCP in Integration Suite</a>.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="build-events-agents" aria-labelledby="build-events-agents-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">22 / Events and AI</p><h2 id="build-events-agents-title">Events, MCP and agents: connect actions safely</h2></header><div class="signavio-reader__content">
<h3>Event-driven design is a relationship, not a product icon</h3>
<p><strong>Producer → event broker / topic → consumer → business action → confirmation or exception.</strong> A business event is a fact such as “PurchaseOrder.Changed”; a command asks a system to perform an action. They need different handling and business expectations.</p>
<div class="table-scroll study-table" role="region" aria-label="Messaging choices and caveats" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Element</th><th scope="col">Owns</th><th scope="col">Key risk</th></tr></thead><tbody>
<tr><td>Event producer</td><td>Publishes a defined business fact.</td><td>Events are missing, late or contain unstable fields.</td></tr>
<tr><td>Event broker</td><td>Routes events to interested consumers and, where configured, holds messages.</td><td>Retention, redelivery, duplication, ordering and subscriptions.</td></tr>
<tr><td>Event consumer</td><td>Processes the event and updates its own state.</td><td>Duplicate actions, poison messages and eventual consistency.</td></tr>
<tr><td>SAP Integration Suite, advanced event mesh</td><td>Enterprise event-broker capabilities for more complex hybrid and distributed scenarios.</td><td>Broker design, protocol compatibility, regional needs and operational costs.</td></tr>
<tr><td>Earlier SAP Event Mesh offerings / Event Mesh capability</td><td>Existing message/event integrations depending on the customer's landscape.</td><td>Check SAP's current migration guidance to advanced event mesh instead of assuming service names mean identical technology.</td></tr>
</tbody></table></div>
<p>Reliable asynchronous processing still needs <strong>idempotent consumers, business keys, retries, dead-letter handling, monitoring and reconciliation</strong>. A queue can support reliable delivery, but it cannot guarantee that an external ERP transaction succeeded.</p>
<h3>MCP versus agent-to-agent</h3>
<p><strong>MCP</strong> exposes callable tools and data through a defined interface for agents. SAP Integration Suite's MCP gateway can expose supported API operations with governance, depending on the service plan. MCP is not an automatic adapter for every legacy mainframe: the underlying function must still be implemented and safely exposed.</p>
<p><strong>Agent-to-agent (A2A)</strong> communication is for delegating and coordinating work between agents. It is not the same thing as an ERP business API. An agent proposing a supplier change still needs permission checks and a controlled process before a purchase order is posted.</p>
<h3>One procurement chain</h3>
<p><strong>Carrier delay detected → event received → affected purchase order identified → alternative evaluated → authorized approval → ERP transaction via released API → business confirmation.</strong></p>
<p>The decision point belongs between recommendation and execution. The process owner sets approval thresholds; the solution architect defines service permissions, human review for material decisions, a correlation ID, error handling and audit evidence. The exact products vary by scenario.</p>
<p>See <a href="https://help.sap.com/docs/integration-suite/migration-from-event-mesh-capability-in-sap-integration-suite-to-sap-integration-suite-advanced-event-mesh-7a447ab211064dcfacff35ac177ae9b9/adapting-sender-and-consumer-applications">SAP Event Mesh migration guidance</a> and <a href="https://help.sap.com/docs/integration-suite/isuite-integrations-and-apis/how-model-context-protocol-mcp-enables-ai-integration-with-apis">SAP MCP Gateway guidance</a>.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="build-operations" aria-labelledby="build-operations-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">23 / Delivery and operations</p><h2 id="build-operations-title">Build, transport, observe and recover the solution</h2></header><div class="signavio-reader__content">
<p>Deployment is one stage of delivery. A Lead must know who releases the change, what is monitored, which team handles exceptions, and what business evidence proves the service is working.</p>
<div class="table-scroll study-table" role="region" aria-label="Operations and delivery toolchain" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Product or service</th><th scope="col">Primary responsibility</th><th scope="col">Do not confuse it with</th></tr></thead><tbody>
<tr><td>SAP Continuous Integration and Delivery</td><td>Build, automated tests and deployment pipelines.</td><td>Approval of business results or cross-landscape transport governance.</td></tr>
<tr><td>SAP Cloud Transport Management</td><td>Transport supported artifacts and content through a landscape.</td><td>A full application test suite or source control system.</td></tr>
<tr><td>SAP Cloud Logging</td><td>Store and analyze supported logs, metrics and traces.</td><td>Business reconciliation across several systems.</td></tr>
<tr><td>SAP Cloud ALM</td><td>Application lifecycle activities and SAP landscape monitoring for supported scenarios.</td><td>The transaction owner or every product's native log viewer.</td></tr>
<tr><td>SAP Focused Run</td><td>Advanced monitoring for large and complex SAP landscapes.</td><td>A substitute for all application-level business error handling.</td></tr>
<tr><td>SAP Solution Manager</td><td>Established ALM platform for many on-premise landscapes.</td><td>A reason to start new ALM designs without checking SAP Cloud ALM.</td></tr>
<tr><td>Cloud Integration Automation Service (CIAS)</td><td>Guide and automate supported integration setup tasks.</td><td>The middleware runtime that carries productive messages.</td></tr>
<tr><td>SAP Build Work Zone / SAP Task Center</td><td>User entry points, applications and tasks.</td><td>The component that automatically owns the originating business transaction.</td></tr>
</tbody></table></div>
<p>For an existing SAP Solution Manager landscape, include its support lifecycle in the roadmap. SAP states mainstream maintenance for Solution Manager 7.2 ends in 2027 and recommends planning the transition to SAP Cloud ALM. Check actual scope and migration options before selecting ALM tooling.</p>
<h3>Diagnose an incomplete business result</h3>
<p><strong>Symptom:</strong> A request app reports success, but the buyer cannot find the purchase requisition.</p>
<ol>
<li>Confirm the originating request, correlation key and expected target document.</li>
<li>Check whether the API or iFlow was called and which response was returned.</li>
<li>Check ERP application logs, authorization, validations and document creation status.</li>
<li>Determine whether the call failed, succeeded after a timeout, or created a document that the originating app did not record.</li>
<li>Recover with a controlled retry or reconciliation path; never blindly resend a posting request.</li>
<li>Prove that the intended business document exists and the user-visible status matches it.</li>
</ol>
<p><strong>IAS/IPS, BTP roles, backend roles and API policies</strong> may all affect the access chain. CIAS may help configure a supported integration scenario; it does not validate its business outcome.</p>
<p><strong>Lead answer:</strong> “A production-ready design needs the interface contract, service ownership, transport and test evidence, monitoring, support response, rollback plan and business completion proof.”</p>
<p>Sources: <a href="https://help.sap.com/docs/cloud-logging">SAP Cloud Logging</a>, <a href="https://help.sap.com/docs/cloud-transport-management">Cloud Transport Management</a>, <a href="https://help.sap.com/docs/cloud-integration-automation/user-guide/overview">CIAS</a> and <a href="https://help.sap.com/docs/SAP_Solution_Manager">Solution Manager transition information</a>.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="context-why" aria-labelledby="context-why-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">24 / Business context</p><h2 id="context-why-title">Why AI needs business context before it can reason</h2></header><div class="signavio-reader__content">
<p>An AI agent can call the correct API and still make the wrong business decision. A lower price is not necessarily a better purchase. A supplier in a spreadsheet is not necessarily an approved supplier. An ERP lead time may not reflect a disruption that happened yesterday.</p>
<p>The Contextualize &amp; Reason pillar addresses the evidence and interpretation behind decisions. It connects business data with meaning, relationships and suitable models. <strong>Build</strong> enables an application or agent to work; <strong>Contextualize</strong> provides grounded facts and business meaning; <strong>Reason</strong> helps evaluate options; <strong>Govern</strong> controls permitted actions.</p>
<div class="table-scroll study-table" tabindex="0" role="region" aria-label="Why disconnected AI fails in business processes"><table class="study-table__table"><thead><tr><th scope="col">Scenario</th><th scope="col">Missing context</th><th scope="col">Safer decision</th></tr></thead><tbody>
<tr><td>An agent discounts a popular material.</td><td>Margin of related products and commercial rules.</td><td>Compare the full product portfolio and margin impact before proposing a discount.</td></tr>
<tr><td>An agent selects a low-price supplier from a spreadsheet.</td><td>Supplier approval status, master-data source and contract validity.</td><td>Treat the spreadsheet as a supplier lead, not as authorization to place a purchase order.</td></tr>
<tr><td>An agent schedules material using an old lead time.</td><td>Current disruptions, route constraints and data timestamp.</td><td>Recalculate delivery risk and request confirmation before changing purchasing commitments.</td></tr>
</tbody></table></div>
<p><strong>Three checks before an agent acts:</strong> Is the fact authoritative? Is it still current? Does this role have permission to use it for this action? A data platform can expose answers to these questions, but an application still must enforce its business rules.</p>
<p><strong>Remember:</strong> Context is not only more data. It is the meaning, authority, relationships, and validity of data.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="context-language" aria-labelledby="context-language-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">25 / Data concepts</p><h2 id="context-language-title">Data warehouse, lake, fabric, mesh and product: six different ideas</h2></header><div class="signavio-reader__content">
<p>These terms are related, but they refer to different kinds of things. A repository stores data, a fabric connects and governs it, a mesh changes who owns it, and a data product packages it for a consumer.</p>
<div class="table-scroll study-table" tabindex="0" role="region" aria-label="Business data architecture vocabulary"><table class="study-table__table"><thead><tr><th scope="col">Concept</th><th scope="col">What it means</th><th scope="col">When it is useful</th></tr></thead><tbody>
<tr><td>Data warehouse</td><td>A structured store optimized for reporting and analysis.</td><td>Combine historical sales and purchasing facts for reliable KPIs.</td></tr>
<tr><td>Data lake</td><td>A store for data in varied formats, often including files and raw records.</td><td>Keep large raw datasets for later engineering, analytics or ML.</td></tr>
<tr><td>Data fabric</td><td>An architecture to connect, access, manage and govern data across sources.</td><td>Reduce fragmented access without requiring everything to move into one database.</td></tr>
<tr><td>Business data fabric</td><td>A data fabric that preserves business definitions, semantics and context.</td><td>Make 'supplier', 'net amount' and 'open PO' mean the right thing across systems.</td></tr>
<tr><td>Data mesh</td><td>A decentralized operating model with domain-owned data products and shared standards.</td><td>Give purchasing and sales teams ownership of reusable data without abandoning common governance.</td></tr>
<tr><td>Data product</td><td>A reusable, documented dataset or data service with a defined consumer contract.</td><td>Offer a governed 'Purchase Orders' dataset instead of a one-off table extraction.</td></tr>
</tbody></table></div>
<h3>What the architect must not assume</h3>
<p>A business data fabric is <strong>not automatically a new central database</strong>. It may use replication, virtualization, sharing or combinations of these. A data mesh does not require separate infrastructure for every department. A warehouse and a lake are not mutually exclusive. A data product is more than a renamed table.</p>
<p><strong>Practical test:</strong> Before selecting technology, ask whether the team needs persistent historical storage, near-real-time access, standard business meaning, decentralized ownership, or a consumer-ready contract. Different answers produce different designs.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="context-data-products" aria-labelledby="context-data-products-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">26 / Reusable data</p><h2 id="context-data-products-title">A data product is a contract, not an export file</h2></header><div class="signavio-reader__content">
<p>Suppose a procurement manager needs an overview of delayed purchase orders. Extracting three ERP tables may produce a report, but it does not explain what “delayed” means or whether canceled items and partial deliveries are included.</p>
<p>A <strong>Purchase Order Status data product</strong> could expose the agreed business objects and measures, a documented definition of lateness, data refresh rules and access controls. The report, data scientist and AI agent then reuse the same meaning rather than each inventing a calculation.</p>
<div class="table-scroll study-table" tabindex="0" role="region" aria-label="Data product checklist"><table class="study-table__table"><thead><tr><th scope="col">Contract element</th><th scope="col">Question</th><th scope="col">Example</th></tr></thead><tbody>
<tr><td>Business meaning</td><td>Which event or condition does each measure represent?</td><td>Delayed means open schedule lines after their agreed delivery date.</td></tr>
<tr><td>Owner and source</td><td>Who owns the definition and which application is authoritative?</td><td>Procurement process owner and purchasing transaction source.</td></tr>
<tr><td>Grain and identity</td><td>What is one record?</td><td>A purchase-order schedule line, not just a purchase order header.</td></tr>
<tr><td>Refresh and quality</td><td>How old can data be and which quality checks apply?</td><td>Source timestamp, rejected rows and completeness checks are visible.</td></tr>
<tr><td>Security</td><td>Who can consume each field or record?</td><td>Purchasers see only authorized organizational data.</td></tr>
<tr><td>Interface and lifecycle</td><td>How do consumers access it and what happens when it changes?</td><td>Published schema, supported access method, version and change notice.</td></tr>
</tbody></table></div>
<p>In SAP Business Data Cloud, SAP-managed data products are grouped into packages and can be activated for supported consumption paths. SAP also documents creation and sharing of custom data products in supported landscapes. <strong>Availability, source coverage and prerequisites must be checked</strong>; a product listed in a catalog is not proof that it is activated for the customer's tenant.</p>
<p><strong>Lead question:</strong> If two reports show different delayed-PO counts, first compare their business definition, record grain, source time and authorization filters. Do not start by changing the dashboard layout.</p>
<p>See <a href="https://help.sap.com/docs/SAP_BUSINESS_DATA_CLOUD/f7acf8c9dad54e99b5ce5ebc633ed8e1/fcf9975b49ea4adeb837e4be16116175.html">SAP Help: Working with Data Products</a> and <a href="https://help.sap.com/docs/SAP_DATASPHERE/e4059f908d16406492956e5dbcf142dc/b07e95d07a1e4569b87d9bb57b732bcf.html">Creating Custom Data Products</a>.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="context-products" aria-labelledby="context-products-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">27 / Product roles</p><h2 id="context-products-title">Which SAP data product or service owns which job?</h2></header><div class="signavio-reader__content">
<p>Do not choose SAP HANA Cloud, Datasphere, Analytics Cloud, Master Data Integration and Master Data Governance as if they were alternatives for the same requirement. Each has a different primary responsibility.</p>
<div class="table-scroll study-table" tabindex="0" role="region" aria-label="SAP data and analytics product responsibilities"><table class="study-table__table"><thead><tr><th scope="col">Product</th><th scope="col">Main job</th><th scope="col">Boundary to remember</th></tr></thead><tbody>
<tr><td><a href='/atlas/sap/sap-datasphere/'>SAP Datasphere</a></td><td>Connect, model and expose governed business data; support data warehousing and virtualization.</td><td>A semantic model does not approve or correct a business partner by itself.</td></tr>
<tr><td><a href='/atlas/sap/sap-analytics-cloud/'>SAP Analytics Cloud</a></td><td>Business intelligence, stories, dashboards and planning.</td><td>A story is a consumption experience, not the authoritative purchasing transaction.</td></tr>
<tr><td>SAP HANA Cloud</td><td>Managed database for transactional, analytical and multi-model workloads.</td><td>A database does not create business semantics or data governance automatically.</td></tr>
<tr><td>SAP Master Data Integration (MDI)</td><td>Synchronize supported master data objects between applications using integration models.</td><td>It distributes master data; it is not the approval workflow that defines a valid supplier.</td></tr>
<tr><td>SAP Master Data Governance (MDG)</td><td>Govern, validate, consolidate and maintain master data within supported scope.</td><td>Governance decides what is accepted; replication is a separate responsibility.</td></tr>
<tr><td>SAP Databricks</td><td>Data engineering, large-scale processing and machine-learning work within supported BDC offerings.</td><td>A data science workspace does not replace ERP ownership of business documents.</td></tr>
<tr><td>SAP BW and BW bridge</td><td>Preserve or modernize supported BW data warehousing assets.</td><td>Migration paths depend on BW version, edition, source extractors and target architecture.</td></tr>
</tbody></table></div>
<h3>One master-data example</h3>
<p>An employee proposes a new supplier. An <strong>MDG governance process</strong>, where implemented for the scenario, checks the data and makes an approved record available. <strong>MDI</strong> can then help synchronize supported master data to participating applications. <strong>Datasphere</strong> models procurement measures, and <strong>Analytics Cloud</strong> displays them. Each component has a distinct owner and a distinct completion signal.</p>
<p>MDI uses SAP One Domain Model integration models for supported objects. These are <strong>integration representations</strong>, not necessarily complete copies of each application's data model. The receiving application still owns its local use of the data.</p>
<p>References: <a href="https://help.sap.com/docs/master-data-integration/sap-master-data-integration-prod/synchronization-of-master-data">SAP MDI synchronization</a>, <a href="https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/5c1e3d4a49554fcd8fcf199d664d1109.html">Datasphere semantic modeling</a>, <a href="https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/18850a0e13944f53aa8a8b7c094ea29e/0ebd87416257410d910bea925d27f4cb.html">Analytics Cloud stories</a>.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="context-bdc" aria-labelledby="context-bdc-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">28 / Data platform</p><h2 id="context-bdc-title">SAP Business Data Cloud: connect sources to useful insights</h2></header><div class="signavio-reader__content">
<p>SAP Business Data Cloud (BDC) brings together data products and capabilities for modeling, analytics, planning and AI. Think of it as an <strong>integrated offering and data architecture</strong>, not as a replacement name for every database, ERP or reporting system.</p>
<div class="table-scroll study-table" tabindex="0" role="region" aria-label="A practical view of the SAP Business Data Cloud architecture"><table class="study-table__table"><thead><tr><th scope="col">Layer</th><th scope="col">What it contains</th><th scope="col">Why it matters</th></tr></thead><tbody>
<tr><td>Source systems</td><td>SAP applications, selected non-SAP systems and existing data platforms.</td><td>This is where original business events and documents are created.</td></tr>
<tr><td>Governed data products</td><td>Curated datasets with meaning, metadata, ownership and consumption contracts.</td><td>Consumers reuse defined business objects instead of reverse-engineering tables.</td></tr>
<tr><td>Business data fabric</td><td>Semantic modeling, data integration, sharing and analytical capabilities including Datasphere, Analytics Cloud and supported partner tools.</td><td>Connect data with business context while managing security and movement.</td></tr>
<tr><td>Intelligent content and applications</td><td>SAP-managed content using data products and analytical models, plus customer-developed consumption paths.</td><td>Deliver measurable analysis, planning and AI use cases.</td></tr>
</tbody></table></div>
<p><strong>Logical relationship:</strong> Source system → governed data product → business model → dashboard, prediction or agent context. This is a view of ownership and consumption, <em>not</em> a mandatory physical pipeline. Some paths replicate data, some access it remotely, and some support open sharing such as Delta Sharing.</p>
<h3>Where BW and Databricks fit</h3>
<p>Existing SAP BW investments can follow supported modernization approaches; SAP Datasphere, BW bridge and SAP Business Data Cloud are related options but not identical migration methods. SAP Databricks adds a data engineering and ML environment for appropriate use cases. The decision depends on source compatibility, data gravity, cost, service entitlement and whether business definitions can be preserved.</p>
<h3>Intelligent content versus custom reporting</h3>
<p>SAP-managed BDC intelligent content can combine delivered data products, Datasphere models and Analytics Cloud stories. Customer-specific reporting may still require configuration, source integration, new models or custom data products. Check the exact packaged content, required entitlements, tenant formation and supported source systems before promising a ready-to-run solution.</p>
<p><strong>Design question:</strong> Which existing assets should we reuse, which new data products must we own, and how will we know when a source definition changes?</p>
<p>Sources: <a href="https://www.sap.com/products/data-cloud/what-is-sap-business-data-cloud.html">SAP BDC architecture overview</a>, <a href="https://help.sap.com/docs/business-data-cloud/administering-sap-business-data-cloud/install-intelligent-applications">SAP-managed intelligent content</a>, <a href="https://architecture.learning.sap.com/docs/ai-native-north-star-architecture/foundation-layer">SAP Architecture Center: Foundation Layer</a>.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="context-knowledge-models" aria-labelledby="context-knowledge-models-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">29 / Semantics and models</p><h2 id="context-knowledge-models-title">Knowledge Graph and SAP-RPT: relationships are not predictions</h2></header><div class="signavio-reader__content">
<p><strong>Business data</strong> tells us which transactions exist. <strong>Semantic relationships</strong> explain how objects relate. <strong>AI models</strong> analyze the available context or estimate an outcome. These are three different jobs.</p>
<h3>See a knowledge graph as business relationships</h3>
<div class="table-scroll study-table" tabindex="0" role="region" aria-label="Example business relationship graph"><table class="study-table__table"><thead><tr><th scope="col">Entity A</th><th scope="col">Relationship</th><th scope="col">Entity B</th></tr></thead><tbody>
<tr><td>Purchase Order</td><td>has supplier</td><td>Business Partner</td></tr>
<tr><td>Purchase Order Item</td><td>requests</td><td>Material</td></tr>
<tr><td>Material</td><td>is required for</td><td>Production Order</td></tr>
<tr><td>Supplier</td><td>is covered by</td><td>Purchasing Contract</td></tr>
<tr><td>Delivery Route</td><td>has current risk</td><td>Logistics Disruption</td></tr>
</tbody></table></div>
<p>Each row is a relationship, but together they form a <strong>graph</strong>: one supplier links to many orders, one material affects many production orders, and one disruption may affect several routes. The graph is not a list of steps to execute.</p>
<p>SAP Knowledge Graph is positioned to support semantic grounding of SAP business context. SAP HANA Cloud also offers technical graph capabilities for customer-built solutions. Do not confuse a delivered semantic product with a database engine; the content, availability, access and maintenance model may differ.</p>
<h3>What SAP-RPT does</h3>
<p><strong>SAP-RPT</strong> is a relational pretrained transformer for prediction tasks on structured business data. SAP documents classification and regression without a separate task-specific training cycle, using in-context examples. In 2026, SAP also describes <strong>SAP-RPT-1.5</strong>. A typical question is “What is the likely delivery delay or risk category for this order?”, not “Write a marketing email”.</p>
<div class="table-scroll study-table" tabindex="0" role="region" aria-label="Knowledge and model roles"><table class="study-table__table"><thead><tr><th scope="col">Capability</th><th scope="col">What question it helps answer</th><th scope="col">What it does not guarantee</th></tr></thead><tbody>
<tr><td>Knowledge Graph</td><td>Which business objects and policies are related?</td><td>That all customer-specific relationships are available, correct or current.</td></tr>
<tr><td>SAP-RPT family</td><td>What classification or numeric value is likely from structured examples?</td><td>That a prediction is a valid business decision or requires no evaluation.</td></tr>
<tr><td>Generative language model</td><td>How should we summarize or interpret text and propose possible steps?</td><td>That the explanation is grounded, authorized or factually correct.</td></tr>
<tr><td>Business rules and authorization</td><td>May this action be executed under policy?</td><td>That the prediction or recommendation is economically optimal.</td></tr>
</tbody></table></div>
<p>Neither a knowledge graph nor a data fabric <strong>eliminates hallucinations or removes the need for human review</strong>. Reliable decisions need valid relationships, permission checks, time-aware source data, model evaluation and clear execution limits.</p>
<p>Sources: <a href="https://architecture.learning.sap.com/docs/ai-native-north-star-architecture/foundation-layer">SAP Knowledge Graph context</a>, <a href="https://help.sap.com/docs/sap-ai-core/generative-ai/sap-rpt-1">SAP-RPT-1 model guide</a>, <a href="https://www.sap.com/canada/products/artificial-intelligence/sap-rpt.html">SAP-RPT-1.5</a>.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="context-case" aria-labelledby="context-case-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">30 / Architecture exercise</p><h2 id="context-case-title">Trace one supplier disruption from data to a controlled decision</h2></header><div class="signavio-reader__content">
<p><strong>Illustrative scenario:</strong> A delayed component threatens a production order. An assistant must identify the impact, suggest a valid alternative and help a buyer act. This example is a design exercise, not a measured customer project or a promise of autonomous execution.</p>
<div class="table-scroll study-table" tabindex="0" role="region" aria-label="Supplier disruption: evidence to action"><table class="study-table__table"><thead><tr><th scope="col">Step</th><th scope="col">Responsible information or capability</th><th scope="col">What must be proved</th></tr></thead><tbody>
<tr><td>1. Detect</td><td>Logistics alert with source, route and timestamp.</td><td>The alert applies to this supplier or shipment, not just a similar location.</td></tr>
<tr><td>2. Connect</td><td>Business relationships between supplier, material, PO and production requirement.</td><td>Identifiers match and the relationships are valid for the relevant dates.</td></tr>
<tr><td>3. Compare</td><td>Purchasing contracts, approved supplier list, lead times, capacity and inventory.</td><td>Alternative suppliers are authorized and the total cost is acceptable.</td></tr>
<tr><td>4. Recommend</td><td>Rules and, where useful, predictive or generative AI.</td><td>The recommendation includes assumptions, confidence and missing information.</td></tr>
<tr><td>5. Approve</td><td>Purchasing decision owner and policy-based limits.</td><td>The required authority approves material commercial changes.</td></tr>
<tr><td>6. Execute</td><td>Released ERP API or a supported standard transaction.</td><td>The intended purchase document changes exactly as authorized.</td></tr>
<tr><td>7. Reconcile</td><td>ERP confirmation, integration monitoring and audit trail.</td><td>The business document and resulting production risk reflect the decision.</td></tr>
</tbody></table></div>
<h3>Architectural choices</h3>
<p>If the need is only a dashboard, governed data products and analytics may be enough. If the need is a recommendation, include relevant relationships and an evaluated model only where they add value. If an agent can update purchasing documents, <strong>action authorization, audit, idempotency and rollback become mandatory design questions</strong>.</p>
<p><strong>45-second interview answer:</strong> “I separate data access from business context and execution. First I identify authoritative sources and model the links between supplier, material, order and risk. Then I choose data products and SAP services based on the actual information needs. For predictions, I evaluate the model and show its assumptions. Finally, I keep ERP as the transaction owner and define approval, monitoring and reconciliation. Business context makes the answer useful; governance makes the action safe.”</p>
<p><strong>Review challenge:</strong> The cheapest alternative supplier appears in a spreadsheet but has not passed quality approval. Should the agent create a purchase order? Explain which data or policy is missing and who owns the next step.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="client-explanation" aria-labelledby="client-explanation-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">31 / Communication</p><h2 id="client-explanation-title">How to explain the architecture to a client</h2></header><div class="signavio-reader__content">
<h3>30-second explanation</h3>
<p>“We start with what the business needs to improve. SAP Signavio helps us understand the process, while SAP LeanIX shows which applications support it. We use SAP reference architecture to connect that business need to a possible solution. BTP gives us options for extensions and integrations where standard applications have a gap. We then check security, costs, operating responsibility and measurable results.”</p>
<h3>90-second explanation</h3>
<p>“I would first agree on the business outcome and the current process. Then I would identify the business capability, the process activities and the applications involved. This tells us where ownership sits and whether the problem comes from the process, data, integration or missing functionality. Next I compare standard SAP capability with in-app and side-by-side extension options. If we need BTP, I select the concrete runtime and services, check identity and entitlements, and document the API and data contracts. Finally, I define tests, monitoring, recovery and the KPI that will show whether the change worked. The output is a supportable solution, not just a technical diagram.”</p>
<h3>Three questions to ask the customer</h3>
<ul><li>Which business result must improve, and what is the current baseline?</li><li>Which system owns each official business document or master data object?</li><li>What happens when the integration, workflow or AI step fails?</li></ul>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="interview" aria-labelledby="interview-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">32 / Self-check</p><h2 id="interview-title">Assessment questions: answer with a decision</h2></header><div class="signavio-reader__content">
<ol>
<li><strong>What is the difference between an EA and an SA?</strong><p>EA defines enterprise-wide direction and governance. SA designs a specific solution within business, technical and delivery constraints. They exchange feedback.</p></li>
<li><strong>Capability versus process?</strong><p>Capability is what the company must be able to do; process is the sequence of activities used to deliver an outcome. A capability may support several processes.</p></li>
<li><strong>RBA versus RSA?</strong><p>RBA uses business language for capabilities and processes. RSA describes software capabilities, solution components, process implementation and data flows that support them.</p></li>
<li><strong>What is the difference between a solution value flow and a process flow?</strong><p>The value flow explains the high-level contribution to business value. The process flow details activities, order and integration handoffs.</p></li>
<li><strong>What is the SAP EA Framework made of?</strong><p>Methodology, Reference Architecture Content, Tooling, Practice and Services.</p></li>
<li><strong>Is SAP Business AI Platform the same as SAP BTP?</strong><p>No. In SAP's 2026 positioning, Business AI Platform is the broader portfolio. BTP remains the platform foundation and one of its parts.</p></li>
<li><strong>Where are BTP applications deployed?</strong><p>Into a regional subaccount using a suitable environment. Cloud Foundry uses orgs/spaces; Kyma uses clusters/namespaces. Managed service subscriptions follow their own model.</p></li>
<li><strong>Where do you find published SAP APIs and events?</strong><p>In SAP Business Accelerator Hub. Check the exact product edition, operations, access requirements and documentation before using the interface.</p></li>
<li><strong>When do you use a methodology instead of a reference architecture?</strong><p>A methodology helps you make and govern the decision. A reference architecture offers a pattern that you adapt after deciding what you need.</p></li>
<li><strong>What is ISA-M used for?</strong><p>To classify integration needs, compare styles and technologies, define standards and support integration governance. It does not require middleware for every interface.</p></li>
<li><strong>Where do you estimate BTP service cost and verify compliance?</strong><p>Use Discovery Center and the relevant service information for planning. Use SAP Trust Center for SAP-managed assurance evidence, then check the customer's responsibilities and actual contract.</p></li>
<li><strong>When do you choose key-user, developer, or side-by-side extensibility?</strong><p>Use key-user tools for small supported changes, developer extensibility for close ERP business-object logic, and side-by-side for cross-system or independent-lifecycle needs. Start with standard capabilities.</p></li>
<li><strong>What do clean core levels A, B, C and D mean?</strong><p>A uses released stable interfaces; B adds supported classic APIs; C depends on internal objects and requires stronger upgrade controls; D uses non-recommended techniques.</p></li>
<li><strong>SAP Build or Joule Studio?</strong><p>SAP Build remains suitable for existing apps, workflow automation and ABAP-linked development. New Joule Studio is aimed at AI-first, SAP-managed use cases. Compare availability, runtime, controls and costs.</p></li>
<li><strong>How do CAP, RAP, Cloud Foundry and Kyma relate?</strong><p>CAP and RAP are programming models; Cloud Foundry, Kyma and the BTP ABAP environment are runtimes. CAP commonly runs on Cloud Foundry or Kyma; RAP is ABAP-based.</p></li>
<li><strong>What is the difference between Cloud Integration and API Management?</strong><p>Cloud Integration processes integration messages and iFlows. API Management governs API exposure, policies and consumption.</p></li>
<li><strong>When are events better than synchronous APIs?</strong><p>Use events when consumers should react independently to facts and can handle eventual consistency. Use synchronous APIs when a caller needs an immediate result; design retries in either approach.</p></li>
<li><strong>Why does exactly-once messaging not always mean exactly-once business processing?</strong><p>A message contract cannot prevent duplicate business effects across systems by itself. Use idempotency, business IDs and reconciliation.</p></li>
<li><strong>What do MCP and A2A solve for agents?</strong><p>MCP exposes tools and data to agents through controlled interfaces. Agent-to-agent protocols enable delegation between agents. Neither removes the need for authorization and audit.</p></li>
<li><strong>How do you prove integration completion?</strong><p>Trace the originating request through middleware and backend logs, confirm the intended document exists, and reconcile its business state.</p></li>
<li><strong>How do CI/CD, transport management, Cloud ALM and CIAS differ?</strong><p>CI/CD builds and tests code, transport management promotes supported artifacts, Cloud ALM handles supported lifecycle and monitoring scenarios, and CIAS guides configuration of supported integrations.</p></li>
<li><strong>What is the difference between context and reasoning?</strong><p>Context gives an agent authoritative facts, business meaning and relationships. Reasoning compares options or predicts an outcome. Business rules and approval still control actions.</p></li>
<li><strong>Data warehouse, data fabric, and data mesh: what changes?</strong><p>A warehouse stores structured analytical data. A fabric connects and governs distributed data. A mesh distributes ownership of reusable data products across business domains.</p></li>
<li><strong>What makes a data product reusable?</strong><p>Its contract defines business meaning, record grain, owner, quality, freshness, access and lifecycle. A raw table extract does not supply all of these.</p></li>
<li><strong>How do Datasphere, Analytics Cloud and HANA Cloud differ?</strong><p>Datasphere connects and models business data; Analytics Cloud delivers reporting and planning; HANA Cloud provides managed data persistence and processing.</p></li>
<li><strong>What is the difference between SAP MDG and MDI?</strong><p>MDG governs and validates supported master data. MDI synchronizes supported master data between connected applications. Their approval and distribution responsibilities differ.</p></li>
<li><strong>What does SAP Business Data Cloud add?</strong><p>It connects governed data products with business modeling, analytics, planning and AI capabilities. It does not replace the systems of record or remove source dependencies.</p></li>
<li><strong>When would you use a knowledge graph instead of a table?</strong><p>When the decision must traverse meaningful many-to-many relations among orders, suppliers, materials and risks. Tables can still store the underlying data.</p></li>
<li><strong>SAP-RPT versus a generative LLM?</strong><p>SAP-RPT predicts classes or numeric values from structured business data. A generative LLM produces or interprets language. Both require evaluation and appropriate context.</p></li>
<li><strong>Does Knowledge Graph guarantee no hallucinations?</strong><p>No. The graph can improve grounding if sources and relationships are accurate and accessible, but results still require checks, policy enforcement and suitable human review.</p></li>
<li><strong>Does side-by-side automatically mean clean core?</strong><p>No. The solution still needs released interfaces, clear ownership, secure access, controlled coupling and an operational recovery path.</p></li>
</ol>
<p><strong>Practice variation:</strong> The customer already has a standard S/4HANA approval function. Would you still propose a custom BTP workflow? Explain the cost, support risk and evidence required before choosing the custom option.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="next" aria-labelledby="next-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">33 / Learning sequence</p><h2 id="next-title">What we will study next</h2></header><div class="signavio-reader__content">
<p>This guide is the architecture foundation. The next BTP lessons should deepen the areas that determine whether a platform solution can be deployed and operated.</p>
<div class="table-scroll study-table" role="region" aria-label="BTP study sequence" tabindex="0"><table class="study-table__table"><thead><tr><th scope="col">Topic</th><th scope="col">What you should be able to decide</th></tr></thead><tbody><tr><td>1. Platform administration</td><td>Design account, region, service and cost boundaries.</td></tr>
<tr><td>2. Identity and connectivity</td><td>Explain trust, destinations, roles and private-network access.</td></tr>
<tr><td>3. Extensions and runtimes</td><td>Compare CAP, ABAP Cloud/RAP, Cloud Foundry and Kyma where relevant.</td></tr>
<tr><td>4. Integration design</td><td>Choose APIs, events, iFlows and recovery patterns.</td></tr>
<tr><td>5. Data and AI architecture</td><td>Choose data access, grounding, governance and evaluations for AI.</td></tr>
<tr><td>6. Delivery and operations</td><td>Define lifecycle, monitoring, security, ownership and service evidence.</td></tr></tbody></table></div>
<p><strong>Architecture resources now covered:</strong> Discovery Center, SAP BTP Guidance Framework, Architecture Center, SAP Business Accelerator Hub, solution diagrams, extension and integration methods, cost-estimation entry points and SAP Trust Center.</p>
<p><strong>Build is covered:</strong> clean core, SAP Build and Joule Studio, runtimes and programming models, integration and operational controls.</p>
<p><strong>Contextualize &amp; Reason is covered:</strong> data foundations, governed data products, Datasphere and Analytics Cloud, SAP Business Data Cloud, Knowledge Graph, SAP-RPT and an end-to-end procurement case. The next study area is the Govern pillar: identity, policy enforcement, lifecycle controls and AI agent oversight.</p>
<p>Use this page as the continuing reference. Add new material to the relevant chapter only when it improves an explanation, design choice or assessment answer.</p>
</div></section>

<section class="research-canvas__inventory signavio-reader__section" id="sources" aria-labelledby="sources-title"><header class="signavio-reader__section-head"><p class="research-canvas__eyebrow">34 / Evidence</p><h2 id="sources-title">Sources and what must be checked</h2></header><div class="signavio-reader__content">
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
<li><a href="https://discovery-center.cloud.sap/">SAP Discovery Center — services, missions and guidance</a></li>
<li><a href="https://help.sap.com/docs/sap_btp_guidance_framework/97dc5926388343be94efd10ae3db716c/what-is-sap-btp-guidance-framework">SAP Help — Guidance Framework and its move to Discovery Center</a></li>
<li><a href="https://help.sap.com/docs/sap-btp-guidance-framework/extension-architecture-guide/what-is-extension-architecture-guide">SAP Help — Extension Architecture Guide</a></li>
<li><a href="https://help.sap.com/docs/sap-btp-guidance-framework/sap-application-extension-methodology/cd2664b67373452ab78825897ff99a81.html">SAP Help — Application Extension Methodology</a></li>
<li><a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/sap-integration-solution-advisory-methodology">SAP Help — Integration Solution Advisory Methodology</a></li>
<li><a href="https://help.sap.com/docs/sap-btp-guidance-framework/sap-data-methodology/sap-data-analytics-advisory-methodology-overview">SAP Help — Data and Analytics Advisory Methodology</a></li>
<li><a href="https://api.sap.com/">SAP Business Accelerator Hub — APIs, events and integrations</a></li>
<li><a href="https://architecture.learning.sap.com/docs/ref-arch">SAP Architecture Center — reference architectures</a></li>
<li><a href="https://sap.github.io/btp-solution-diagrams/">SAP BTP Solution Diagram Guidelines</a></li>
<li><a href="https://www.sap.com/about/trust-center.html">SAP Trust Center</a></li>
<li><a href="https://news.sap.com/2025/08/extend-sap-s4hana-cloud-right-way-clean-clear/">SAP News — Clean core levels</a></li>
<li><a href="https://help.sap.com/docs/abap-cloud/abap-cloud/extensibility">SAP Help — ABAP extensibility</a></li>
<li><a href="https://news.sap.com/2026/05/new-joule-studio-enterprise-scale-agentic-development/">SAP News — new Joule Studio (May 2026)</a></li>
<li><a href="https://community.sap.com/t5/technology-blog-posts-by-sap/sap-build-apps-deprecation-and-the-path-forward/bc-p/14357348/highlight/true">SAP Community — Build Apps deprecation (March 2026)</a></li>
<li><a href="https://help.sap.com/docs/btp/btp-developers-guide/understanding-available-technology">SAP Help — BTP runtimes and programming models</a></li>
<li><a href="https://help.sap.com/docs/cloud-integration/sap-cloud-integration/what-is-sap-cloud-integration">SAP Help — SAP Cloud Integration</a></li>
<li><a href="https://help.sap.com/docs/integration-suite/isuite-integrations-and-apis/model-context-protocol-mcp">SAP Help — Integration Suite MCP gateway</a></li>
<li><a href="https://help.sap.com/docs/integration-suite/migration-from-event-mesh-capability-in-sap-integration-suite-to-sap-integration-suite-advanced-event-mesh-7a447ab211064dcfacff35ac177ae9b9/adapting-sender-and-consumer-applications">SAP Help — Event Mesh migration to Advanced Event Mesh</a></li>
<li><a href="https://help.sap.com/docs/cloud-integration-automation/user-guide/overview">SAP Help — Cloud Integration Automation Service</a></li>
<li><a href="https://help.sap.com/docs/cloud-transport-management">SAP Help — Cloud Transport Management</a></li>
<li><a href="https://help.sap.com/docs/cloud-logging">SAP Help — Cloud Logging</a></li>
<li><a href="https://help.sap.com/docs/SAP_Solution_Manager">SAP Help — SAP Solution Manager transition</a></li>
<li><a href="https://help.sap.com/docs/joule-work-mobile/administration-guide-sap-build-work-zone-setup/overview">SAP Help — Joule Work mobile (formerly SAP Mobile Start)</a></li>
<li><a href="https://www.sap.com/products/data-cloud/what-is-sap-business-data-cloud.html">SAP: Business Data Cloud architecture</a></li>
<li><a href="https://help.sap.com/docs/SAP_BUSINESS_DATA_CLOUD/f7acf8c9dad54e99b5ce5ebc633ed8e1/fcf9975b49ea4adeb837e4be16116175.html">SAP Help: Business Data Cloud data products</a></li>
<li><a href="https://help.sap.com/docs/business-data-cloud/administering-sap-business-data-cloud/install-intelligent-applications">SAP Help: Managed intelligent content</a></li>
<li><a href="https://help.sap.com/docs/SAP_DATASPHERE/e4059f908d16406492956e5dbcf142dc/b07e95d07a1e4569b87d9bb57b732bcf.html">SAP Help: Custom data products for BDC</a></li>
<li><a href="https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/5c1e3d4a49554fcd8fcf199d664d1109.html">SAP Help: Datasphere business semantic model</a></li>
<li><a href="https://help.sap.com/docs/master-data-integration/sap-master-data-integration-prod/synchronization-of-master-data">SAP Help: MDI master data synchronization</a></li>
<li><a href="https://architecture.learning.sap.com/docs/ai-native-north-star-architecture/foundation-layer">SAP Architecture Center: AI and data foundation</a></li>
<li><a href="https://help.sap.com/docs/sap-ai-core/generative-ai/sap-rpt-1">SAP Help: SAP-RPT-1 model</a></li>
<li><a href="https://www.sap.com/canada/products/artificial-intelligence/sap-rpt.html">SAP: SAP-RPT-1.5</a></li>
<li><a href="https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/18850a0e13944f53aa8a8b7c094ea29e/0ebd87416257410d910bea925d27f4cb.html">SAP Help: Analytics Cloud stories</a></li>
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
