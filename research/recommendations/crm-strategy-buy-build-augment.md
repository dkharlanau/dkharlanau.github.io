---
layout: default
title: "CRM Strategy in 2026: Buy, Build, or Augment?"
description: "An independent SAP-centric CRM architecture recommendation comparing SAP Sales Cloud V2, major CRM alternatives, custom builds, and governed AI agents."
permalink: /research/recommendations/crm-strategy-buy-build-augment/
type: recommendation
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
date: 2026-10-30
updated: 2026-10-30
evidence_level: medium
hide_global_cta: true
topics:
  - crm
  - sap-sales-cloud
  - sap-service-cloud
  - s4hana
  - build-vs-buy
  - ai-agents
  - integration-architecture
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/research/">Research</a></li>
    <li><a href="/research/recommendations/">Independent recommendations</a></li>
    <li aria-current="page">CRM strategy: Buy, build, or augment</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Architecture Point of View / Decision 001 / October 2026</p>
    <h1>CRM strategy: Buy, build, or augment?</h1>
    <p class="note-subtitle">A vendor-neutral recommendation for SAP-centered companies considering a CRM replacement, a custom platform, or AI-enabled improvement.</p>
  </header>
  <div class="note-body" markdown="1">

## The decision I would make

**I would not approve a full CRM replacement as the first step.** I would retain the existing CRM for a short, measured assessment, address the most expensive user problems with targeted changes, and compare a replacement against evidence from that work.

This is not a recommendation to keep a weak platform forever. It is a recommendation to **earn the right to replace it** with a clear business case.

My default target is a **hybrid, composable CRM architecture**:

- **Buy or retain a proven CRM core** for opportunities, activities, cases, permissions, history, reporting, and reliable workflows.
- **Keep SAP S/4HANA responsible** for operational truth such as sales orders, inventory, pricing, credit, delivery, and billing, according to the landscape's process ownership.
- **Keep business partner governance** in the designated master-data system, such as SAP MDG where it is used. Do not turn the CRM into an uncontrolled second customer master.
- **Build small, differentiated capabilities** only where standard CRM functions and configuration cannot meet a valuable requirement.
- **Add AI assistants and agents around controlled actions**, not as a replacement for transactional controls or a reliable data model.

This is a *conditional architectural position*, not a claim that I have assessed a specific company's CRM. The scenarios below are illustrative, and all vendor details require a release, edition, and contractual fit check.

## Why I challenge the question

The phrase “Our CRM is outdated” is not a business requirement. It may describe five very different failures:

1. **Poor adoption:** salespeople do not enter their activities or trust the system.
2. **Poor integration:** teams cannot see prices, stock, orders, invoices, or cases in one work context.
3. **Poor process design:** approvals, territories, lead hand-offs, and service routing are slow.
4. **Poor data quality:** duplicate customers, missing contacts, stale opportunities, or unclear ownership.
5. **Platform limits:** the CRM cannot support essential functions, scale, security, or a sustainable change model.

Each failure points to a different investment. A replacement can carry the same broken process into a more expensive platform. AI can make a bad process faster without making it correct.

Before discussing products, I would ask: **Which sales or service outcome is failing, how is that failure measured, and what have we already tried to fix?**

## Buy: Which CRM belongs on the shortlist?

The table describes architectural fit, not a product ranking. “Cost pressure” is a **qualitative planning assumption**, not a verified quotation. Actual spend depends on edition, user types, integration, storage, AI consumption, service, implementation, and contract terms.

<div class="table-scroll study-table" tabindex="0" role="region" aria-label="CRM platform comparison for an SAP-centered enterprise">
<table class="study-table__table">
<thead>
<tr><th scope="col">Option</th><th scope="col">Where I would shortlist it</th><th scope="col">Main challenge</th><th scope="col">Cost pressure</th></tr>
</thead>
<tbody>
<tr><th scope="row">SAP Sales Cloud V2 / Service Cloud V2</th><td>SAP-centered B2B processes needing supported S/4HANA integration and connected sales or service work.</td><td>Fit gaps, commercial terms, C4C V1 transition effort, and the need to validate each integration scenario.</td><td>High</td></tr>
<tr><th scope="row">Microsoft Dynamics 365 Sales / Customer Service</th><td>Companies using Microsoft 365, Teams, Power Platform, and Dataverse heavily.</td><td>Custom integration and ownership boundaries with SAP; licensing and platform administration.</td><td>Medium–high</td></tr>
<tr><th scope="row">Salesforce Sales Cloud / Service Cloud</th><td>Complex sales, service, partner ecosystems, and large-scale CRM platform programs.</td><td>Implementation and ongoing administration; extra integration, data, and AI consumption costs.</td><td>High–very high</td></tr>
<tr><th scope="row">HubSpot</th><td>Teams prioritizing usable lead, marketing, and sales workflows with fast adoption.</td><td>Advanced enterprise process fit and SAP synchronization require careful testing.</td><td>Medium; higher with enterprise scope</td></tr>
<tr><th scope="row">Creatio</th><td>Process-heavy companies wanting configurable workflows and a composable low-code environment.</td><td>Partner skills, platform dependence, and the true cost of substantial custom process logic.</td><td>Medium–high</td></tr>
<tr><th scope="row">Zoho CRM</th><td>Cost-sensitive organizations with less complex enterprise requirements.</td><td>Prove deep SAP integration, governance, and nonstandard process coverage rather than assume them.</td><td>Low–medium</td></tr>
<tr><th scope="row">SuiteCRM / Odoo CRM</th><td>Teams with strong in-house engineering, control requirements, and manageable CRM scope.</td><td>Security, upgrades, operations, feature ownership, and integration become your responsibility.</td><td>Lower license cost; variable total cost</td></tr>
<tr><th scope="row">Fully custom CRM</th><td>Only when the workflow is narrow, genuinely unique, and commercially justified.</td><td>You must build and maintain every core CRM capability you did not buy.</td><td>Very high delivery and lifecycle risk</td></tr>
</tbody>
</table>
</div>

**What I would not do:** compare a low-tier CRM subscription against a fully implemented enterprise suite and call the first one cheaper. They do not deliver the same scope.

### Is SAP C4C the right platform?

First, I would resolve a naming problem. **SAP Cloud for Customer (C4C / Version 1)** and **SAP Sales Cloud Version 2 / SAP Service Cloud Version 2** are distinct product generations. A V1-to-V2 transition is a project, not a routine upgrade. SAP provides transition tools, but migration coverage has restrictions, including restrictions for some lead-related information and extension fields. [SAP transition tools](https://help.sap.com/docs/sap-cloud-for-customer/4ca099b3968e4b1d8201e98bc0b96edc/886e8109b3c74fbca224252afa46fdb3.html) · [Lead transition limitations](https://help.sap.com/docs/PRODUCTS/4ca099b3968e4b1d8201e98bc0b96edc/95d48114a36e40d28df49e27ea4312c1.html) · [SAP V1-to-V2 guidance, October 2026](https://community.sap.com/t5/crm-and-cx-blog-posts-by-sap/from-v1-to-v2-transitioning-to-sap-sales-cloud-amp-sap-service-cloud-v2/ba-p/14510810).

**If the company already runs C4C V1:** I would not invest in a large, long-lived custom feature without first checking the product roadmap and the V2 transition implications. However, I would not invent an end-of-support date: the exact contractual and product lifecycle position must be checked in SAP's current support documents.

**If choosing a new SAP CRM:** I would assess Sales Cloud V2 and, when service management is relevant, Service Cloud V2 as distinct options. I would demonstrate the actual account-to-opportunity-to-quote process, case management, extensions, authorizations, reporting, and S/4HANA integration before recommending them. SAP documents integration and APIs, but “standard integration exists” is not the same as “every process works without project effort.” [SAP Sales Cloud V2 Help](https://help.sap.com/docs/CX_NG_SALES) · [SAP integration learning journey](https://learning.sap.com/courses/integrating-sap-sales-and-service-cloud-version-2-with-sap-s-4hana-private-cloud).

**My SAP-specific position:** SAP Sales Cloud V2 earns a place on the shortlist because of its SAP process context, not because the organization already owns SAP. It wins only if the end-to-end process is better and the lifecycle cost is defensible.

### When another CRM may be better

I would give **Dynamics 365** serious consideration if collaboration, Outlook, Teams, Dataverse, and Power Platform are central to the business. Microsoft announced general availability of its Dynamics 365 CX MCP Server for Sales on **29 October 2026**. The documented 59 governed tools make CRM data and actions accessible to supported AI experiences under Dataverse permissions. This is a meaningful architectural option; it does not remove the need to design SAP integration. [Microsoft announcement](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/10/29/dynamics-365-cx-mcp-server-sales/) · [Microsoft SAP integration overview](https://learn.microsoft.com/en-us/power-platform/sap/explore/power-platform-and-sap-integration).

I would consider **Salesforce** when the organization needs a broad CRM ecosystem, advanced CRM configuration, or complex sales and service operating models. MuleSoft and Salesforce's integration capabilities are relevant, but separate platform, integration, and AI charges must be understood. [Salesforce platform](https://www.salesforce.com/platform/agentforce-platform/) · [AI billing model](https://help.salesforce.com/s/articleView?id=ai.generative_ai_usage.htm&language=en_US).

I would consider **HubSpot, Zoho, or Creatio** when simplicity, time to value, workflow flexibility, or cost matters more than deep SAP-oriented functions. Their marketing claims are not proof of enterprise fit. The evaluation must include complex account hierarchies, quote ownership, customer roles, compliance, and SAP integration. [HubSpot APIs](https://developers.hubspot.com/docs/reference/api/overview) · [Zoho Zia limitations](https://help.zoho.com/portal/en/kb/crm/zia-artificial-intelligence/conversational-ai/articles/ask-zia) · [Creatio sales capabilities](https://academy.creatio.com/guides/creatio-apps/overview/sales-creatio-overview).

I would include **SuiteCRM or Odoo** as a control option when teams have engineering capacity and want more ownership over the code and deployment. Open source can reduce license dependence, but it does not remove operational dependence or the cost of maintenance. [SuiteCRM pricing and hosting](https://suitecrm.com/pricing/) · [Odoo 19 CRM documentation](https://www.odoo.com/documentation/19.0/applications/sales.html).

## Build: How much CRM can AI really replace?

I separate **a better user experience**, **a business process**, and **a system of record**. AI can improve the first, support parts of the second, but it should not be treated as a replacement for the third.

<div class="table-scroll study-table" tabindex="0" role="region" aria-label="Recommended automation method by CRM capability">
<table class="study-table__table">
<thead><tr><th scope="col">Capability</th><th scope="col">Preferred approach</th><th scope="col">Why</th></tr></thead>
<tbody>
<tr><th scope="row">Meeting and email summary</th><td>GenAI assistant</td><td>Human checks the content; value comes from faster preparation.</td></tr>
<tr><th scope="row">Opportunity briefing / next-best-action draft</th><td>AI with CRM + ERP context</td><td>Useful recommendation, but a salesperson owns the decision.</td></tr>
<tr><th scope="row">Lead enrichment and deduplication suggestions</th><td>AI-assisted checks + deterministic validation</td><td>Suggestions are useful; identity and merge rules need control.</td></tr>
<tr><th scope="row">Case classification and response draft</th><td>Bounded agent + review</td><td>Good pilot if routing, confidence, and escalation are measured.</td></tr>
<tr><th scope="row">Price, ATP, credit, order creation</th><td>Released ERP interfaces + business rules</td><td>Use SAP as the authority for transactional decisions and checks.</td></tr>
<tr><th scope="row">Customer master data approval</th><td>Governed MDG / master data workflow</td><td>AI may draft inputs; it must not silently bypass governance.</td></tr>
<tr><th scope="row">Permissions, audit, consent, lifecycle</th><td>CRM/platform services and deterministic controls</td><td>These need durable policy enforcement, not model judgment.</td></tr>
</tbody>
</table>
</div>

**A useful reality check:** the 2025 [CRMArena-Pro research](https://arxiv.org/abs/2505.18878) reported approximately **58% success for leading tested agents on single-turn tasks** and **35% on multi-turn tasks**. The benchmark is a defined historical test, not a measurement of every current product. It is still enough to challenge the idea that a general agent should own sensitive CRM workflows without evaluation, permissions, and human oversight.

### A composable architecture I would consider

<figure aria-label="Conceptual target architecture for a hybrid CRM with SAP ERP, governance and AI" markdown="1">
<pre><code>Sales / service users
        |
        +------ CRM core ------+------ Focused web apps
        |  leads, opportunities|     special workflows
        |  activities, cases   |
        +----------+-----------+
                   |
        Controlled API / event layer
        identity, consent, authorization
        retry, monitoring, audit, mapping
                   |
      +------------+------------+
      |                         |
 SAP S/4HANA                SAP MDG or
 orders, price, ATP,         designated BP
 credit, delivery,          master-data
 billing                    governance
      |
 Read-only business context
 + released, scoped actions
      |
 AI assistants / bounded agents
 summarise, classify, suggest,
 prepare actions for approval
</code></pre>
<figcaption>Conceptual responsibility boundaries. Exact data owners and integration directions depend on the landscape.</figcaption>
</figure>

I would design the integration contract before choosing the AI model:

- **Customer identity:** one authoritative business partner identity and explicit cross-system keys. Record who creates a prospect and when it becomes a governed customer.
- **Transaction ownership:** do not copy complex ERP pricing, ATP, or credit rules into an AI prompt or a CRM extension.
- **Synchronous calls:** use appropriately released APIs for business decisions that need a fresh answer, with timeouts and explicit error handling.
- **Asynchronous updates:** use governed messages/events for noncritical state propagation where the product supports them; implement idempotency, retry, reconciliation, and monitoring.
- **AI actions:** allowlisted tools, least-privilege identity, sensitive-data restrictions, observable logs, approval for high-impact writes, and rollback or compensation paths.
- **Portability:** keep business rules, mappings, integration contracts, and test cases outside proprietary prompts wherever feasible. An API alone does not guarantee an easy vendor exit.

### Example: A better quote process without replacing the CRM

*Hypothetical B2B distribution case, not a description of a real customer.*

A salesperson gets a customer request by email. Today they search product information, check availability, prepare a quote, and chase an order status across multiple systems.

**My first experiment would not be a CRM replacement.** It would be a narrowly scoped quote assistant that:

1. Extracts requested products and quantities from an email into a draft for review.
2. Resolves product and customer identifiers against governed data.
3. Retrieves current price and availability through approved ERP interfaces.
4. Produces a traceable draft response and, when allowed, prepares the CRM or ERP follow-up action.
5. Requires user confirmation before a quote or order is submitted.

If this removes most of the observed friction without undermining controls, the business case for replacing the entire CRM becomes weaker. If the existing CRM cannot support the required object, workflow, or security model, the case for a platform change becomes stronger.

## The decision is not a vendor popularity contest

I would evaluate three *architecture options* before ranking products.

<div class="table-scroll study-table" tabindex="0" role="region" aria-label="Decision options compared on value and risk">
<table class="study-table__table">
<thead><tr><th scope="col">Architecture</th><th scope="col">Strongest reason to choose it</th><th scope="col">Main failure mode</th><th scope="col">My default position</th></tr></thead>
<tbody>
<tr><th scope="row">Keep + improve</th><td>Core CRM is adequate; problems are data, adoption, or a few processes.</td><td>Incremental fixes prolong a structurally unsuitable product.</td><td>Test first</td></tr>
<tr><th scope="row">Buy + integrate</th><td>Core functions, security, scale, or maintainability are missing.</td><td>Expensive migration reproduces old process and data problems.</td><td>Choose after evidence</td></tr>
<tr><th scope="row">Build custom CRM</th><td>Highly differentiated, narrow scope with a team to own the full lifecycle.</td><td>Hidden maintenance, security, and feature costs.</td><td>Avoid for full CRM core</td></tr>
<tr><th scope="row">Hybrid CRM + targeted apps + AI</th><td>Good core plus specific high-value gaps and cross-system work.</td><td>Integration sprawl, unclear data ownership, agent mistakes.</td><td>Preferred hypothesis</td></tr>
</tbody>
</table>
</div>

For a formal selection I would agree on a weighted scorecard *before* vendor demos. One reasonable starting model is: **process fit 30%, SAP/integration fit 20%, user adoption 15%, three-year total cost 15%, security/governance 10%, and change/exit flexibility 10%.** These weights are a proposed method, not an evidence-based result for a specific company. Business stakeholders can change them, but should explain why.

Vendors should demonstrate the **same end-to-end scenarios with realistic data**, not present their strongest generic slides. Score direct observed behavior, workarounds, unsupported requirements, and lifecycle effort separately.

### What the real cost comparison must include

A low subscription fee is not the same as low total cost.

**Three-year TCO = licenses and user roles + implementation + migration + SAP integration + extensions + operations + AI usage + support and testing + expected exit costs.**

I would request commercial quotes only after the mandatory scenarios and user population are defined. I would also challenge “AI included” claims: model access, agent actions, data ingestion, testing, monitoring, and premium features can have separate consumption or licensing conditions. [Microsoft Sales licensing](https://www.microsoft.com/en-us/dynamics-365/products/sales/pricing) · [Salesforce AI usage](https://help.salesforce.com/s/articleView?id=ai.generative_ai_usage.htm&language=en_US) · [SAP Sales Cloud quote-based pricing](https://www.sap.com/products/crm/sales-cloud/pricing.html) · [Creatio plan structure](https://www.creatio.com/products/pricing?products%5B0%5D=sales).

## How I would make the decision in eight weeks

The sequence is an illustrative assessment plan, not a promise of a production go-live.

<div class="table-scroll study-table" tabindex="0" role="region" aria-label="Eight-week CRM architecture assessment plan">
<table class="study-table__table">
<thead><tr><th scope="col">Period</th><th scope="col">Activity</th><th scope="col">Evidence produced</th></tr></thead>
<tbody>
<tr><th scope="row">Weeks 1–2</th><td>Interview sales, service, IT, security and integration teams; measure usage, hand-offs, and process failures.</td><td>Process map, baseline metrics, pain ranked by cost and severity, system-of-record map.</td></tr>
<tr><th scope="row">Weeks 3–4</th><td>Assess the current CRM and run the same three realistic scenarios on two shortlisted alternatives.</td><td>Fit-gap log, integration inventory, migration risk, security and extensibility findings.</td></tr>
<tr><th scope="row">Weeks 5–7</th><td>Deliver one bounded AI/automation pilot on existing systems with controlled SAP access.</td><td>Actual time saved, error rates, approval outcomes, user feedback, operating cost, incident data.</td></tr>
<tr><th scope="row">Week 8</th><td>Compare results against the scored options and three-year TCO range.</td><td>Architecture Decision Record: retain, augment, replace, or stop investing.</td></tr>
</tbody>
</table>
</div>

A strong pilot has **measured business value** and a safe operating boundary. I would use task completion time, data correctness, user adoption, error recovery, permission violations, integration reconciliation, and cost per successful task. Targets should be agreed with stakeholders before running the pilot. **Zero unauthorized writes** is a mandatory safety condition, not an average performance goal.

### What would change my recommendation?

I would recommend a **replacement** if the current platform repeatedly fails critical process or security requirements; if meaningful vendor support and maintainability are at risk; if core integration is unsustainable; or if a comparable platform proves a better three-year outcome *after* migration risks.

I would recommend **retaining the core** if failure is mainly adoption, data quality, or a few avoidable workflow steps, and if targeted improvements produce better outcomes at lower lifecycle cost.

I would recommend **a small custom module** when its business logic is genuinely different, its ownership is clear, and it can be removed without breaking the customer system of record.

I would **stop the AI pilot** if it cannot meet permissions, accuracy, audit, and process safety gates—even if its demo is impressive.

## The recommendation I would defend in an architecture board

> “My recommendation is to separate the CRM platform decision from the AI opportunity. First, we establish which capabilities must remain reliable systems of record. Then we test the current platform, targeted improvements, and two market alternatives against identical business scenarios. I would prefer a hybrid solution if it gives users better outcomes without adding a second customer master or weakening SAP controls. If the evidence shows a fundamental platform gap, I would support a full replacement with a justified migration and operating model.”

**Decision today:** **Retain and assess; pilot governed AI augmentation; keep SAP Sales Cloud V2 and at least one non-SAP CRM on the shortlist. Do not authorize a full replacement or a full custom build without a comparative business case.**

**Confidence:** Moderate for the general architecture principle; low for any specific company recommendation until workflow, landscape, cost, and adoption evidence are available.

## Questions I would ask at the first workshop

- Do we need **Sales**, **Service**, **Marketing**, or all three? Which end-to-end outcomes matter most?
- What is the current CRM product and edition, and which features or users actually fail today?
- Which system owns prospects, legal customers, contacts, prices, quotes, orders, and service cases?
- What does SAP S/4HANA need to expose in real time? What can be eventually consistent?
- Where are the largest measurable manual delays and correction efforts?
- Which customizations, integrations, and historical objects would have to migrate?
- How are customer data, consent, identity, access, retention, and audit governed?
- What would convince us **not** to replace the CRM?

## Evidence and limitations

This point of view is an independent, public technical analysis based on published primary documentation and research reviewed on **30 October 2026**. It is not sponsored, does not represent an employer or client, and does not claim experience with a named company's CRM implementation. Vendor capabilities vary by edition, region, release, and contract. “Cost pressure” is editorial judgment rather than procurement data.

**Selected primary references**

1. [SAP Sales Cloud V2 documentation and integration guides](https://help.sap.com/docs/CX_NG_SALES) — product scope and SAP integration. Product documentation.
2. [SAP Cloud for Customer transition tools](https://help.sap.com/docs/sap-cloud-for-customer/4ca099b3968e4b1d8201e98bc0b96edc/886e8109b3c74fbca224252afa46fdb3.html) and [lead transition limits](https://help.sap.com/docs/PRODUCTS/4ca099b3968e4b1d8201e98bc0b96edc/95d48114a36e40d28df49e27ea4312c1.html) — migration is not a simple version upgrade.
3. [Microsoft Dynamics 365 CX MCP Server — Sales, 29 October 2026](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/10/29/dynamics-365-cx-mcp-server-sales/) — governed CRM tools for supported agents.
4. [Microsoft Power Platform and SAP integration](https://learn.microsoft.com/en-us/power-platform/sap/explore/power-platform-and-sap-integration) — practical integration options, not a guarantee of end-to-end business fit.
5. [Salesforce Agentforce platform and MuleSoft](https://www.salesforce.com/platform/agentforce-platform/) and [usage billing](https://help.salesforce.com/s/articleView?id=ai.generative_ai_usage.htm&language=en_US) — integration and consumption considerations.
6. [HubSpot 2026 API documentation](https://developers.hubspot.com/docs/reference/api/overview) — integration capabilities and versioning.
7. [Creatio Sales product documentation](https://academy.creatio.com/guides/creatio-apps/overview/sales-creatio-overview) — no-code and process configuration.
8. [Zoho Ask Zia documentation](https://help.zoho.com/portal/en/kb/crm/zia-artificial-intelligence/conversational-ai/articles/ask-zia) — example of practical current AI limits.
9. [SuiteCRM hosting and licensing](https://suitecrm.com/pricing/) and [Odoo CRM](https://www.odoo.com/documentation/19.0/applications/sales.html) — open-source implementation options.
10. [CRMArena-Pro (2025)](https://arxiv.org/abs/2505.18878) — historical benchmark of CRM agent performance, not a prediction for a specific 2026 deployment.

### Related work

- [SAP MDG vs Custom MDM and Knowledge Graph](/research/comparisons/sap-mdg-vs-custom-mdm-knowledge-graph/)
- [Joule / SAP Business AI vs General Enterprise Agents](/research/comparisons/joule-sap-business-ai-vs-general-enterprise-agents/)
- [Independent Recommendations](/research/recommendations/)

  </div>
  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
