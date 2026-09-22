---
layout: default
title: "SAP Business Partner API — Data Model, Segments, CVI and Integration Design"
description: "A practical SAP Lead guide to API_BUSINESS_PARTNER: BP, customer and supplier segments, roles, company code, sales area, purchasing organization, deep create, updates, CVI, errors and integration choices."
permalink: /labs/enterprise-context/integrations/business-partner-api/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-21
hide_global_cta: true
career_impact: mapped
career_skills:
  - integration-patterns
  - integration-recovery
  - logistics-master-data
tags:
  - sap
  - s4hana
  - business-partner
  - odata
  - integration
  - master-data
  - cvi
structured_data:
  type: TechArticle
primary_topic: "sap-business-partner-api"
semantic_links:
  - type: "related_topic"
    title: "SAP Integration Architecture"
    url: "/labs/enterprise-context/integrations/"
  - type: "related_topic"
    title: "SAP Master Data"
    url: "/labs/enterprise-context/master-data/"
  - type: "related_topic"
    title: "SAP MDG"
    url: "/labs/enterprise-context/mdg/"
  - type: "deep_dive"
    title: "SAP DRF — Data Replication Framework"
    url: "/labs/enterprise-context/integrations/drf/"
source_links:
  - title: "APIs for Business Partner — SAP S/4HANA On-Premise 2025 FPS01"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/44e06f22436c43e582db6ccd5250e29b/9fca825858239244e10000000a4450e5.html"
  - title: "Business Partner (A2X) — OData API"
    url: "https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/85043858ea0f9244e10000000a4450e5.html"
  - title: "Business Partner Master Data Structure"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/776fbd534f22b44ce10000000a174cb4.html"
  - title: "Create Business Partner Data with Deep Payload"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/44e06f22436c43e582db6ccd5250e29b/a9ce55233bd6419f84b4af05df9134fa.html"
  - title: "Update Business Partner Data"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/44e06f22436c43e582db6ccd5250e29b/81c9afd408d24612a580ad0c3f77c8a5.html"
  - title: "Making Settings for Customer/Vendor Integration"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/79781e03a08248de96ff4d84863488ef/5c8189abfed6435b854f6e73cd53f2f4.html"
  - title: "Extensibility — APIs for Master Data Maintenance"
    url: "https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/f5ea5db84f6d44e6a3f193e3f407ba97.html"
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/labs/">Labs</a></li>
    <li><a href="/labs/enterprise-context/">Enterprise Context</a></li>
    <li><a href="/labs/enterprise-context/integrations/">Integrations</a></li>
    <li aria-current="page">Business Partner API</li>
  </ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Master Data Integration</p>
      <h1>SAP Business Partner API: understand the object before the endpoint</h1>
      <p><code>API_BUSINESS_PARTNER</code> is not one flat customer endpoint. It exposes a hierarchy around the S/4HANA Business Partner, with customer and supplier branches and organizational segments for Finance, Sales, and Purchasing.</p>
      <a class="research-canvas__button" href="#mental-model">Start with the mental model <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Learning scope">
      <p>What this module covers</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>BP</strong><small>Leading object</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>SD</strong><small>Customer sales area</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>MM</strong><small>Supplier purchasing org</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>FI</strong><small>Company code views</small></div>
      <em>Source scope: S/4HANA On-Premise 2025 FPS01 plus current Public Cloud API documentation</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <p><strong>The main idea:</strong> a Business Partner answers “who is this party?”. Customer and supplier views answer “how do we do business with this party?”. Company code, sales area, and purchasing organization segments answer “how do we do business in this organizational context?”.</p>
    <p><strong>Lead rule:</strong> never close a master-data interface test because the BP number exists. Prove that the required role and organizational segment exist and are usable by the real business process.</p>
  </section>

  <section class="research-canvas__inventory" id="mental-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Mental model</p>
      <h2>One partner, several business views.</h2>
      <p>The API mirrors the S/4HANA master-data structure. Start from the root, then move into the customer or supplier branch only when the business process needs it.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Root · Business Partner</h3><p><code>A_BusinessPartner</code> holds central identity such as category, grouping, names, search terms, language, and central status. Think “who is the party?”</p></div>
      <div><h3>Identity and compliance</h3><p>Roles, tax numbers, identification numbers, industries, bank data, ratings, and related classifications sit around the BP root. These are separate entities, not one large field list.</p></div>
      <div><h3>Address and communication</h3><p>Addresses have their own child structure for usage, phone, e-mail, fax, URL, international versions, and address-dependent information. Multiple addresses are normal.</p></div>
      <div><h3>Customer branch</h3><p><code>A_Customer</code> is the customer view. Below it, company-code data supports FI-AR and sales-area data supports SD execution.</p></div>
      <div><h3>Supplier branch</h3><p><code>A_Supplier</code> is the supplier view. Below it, company-code data supports FI-AP and purchasing-organization data supports procurement.</p></div>
      <div><h3>Relationships and contacts</h3><p>Contact persons and BP relationships form another part of the graph. Do not model a contact as a random text field on the organization.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="entity-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Entity map</p>
      <h2>The segments a logistics Lead should recognize.</h2>
      <p>You do not need to memorize every API entity. You do need to know where important data belongs and which organizational key makes it unique.</p>
    </header>
    <div class="research-route-list">
      <a href="#roles"><span>ROOT</span><strong>A_BusinessPartner</strong><small>Central BP identity. Main children include customer, supplier, addresses, roles, tax numbers, bank details, identifications, industries, contacts, and relationships.</small><i class="material-symbols-outlined" aria-hidden="true">person</i></a>
      <a href="#customer"><span>ID</span><strong>Role · Tax · Identification · Bank · Industry</strong><small><code>A_BusinessPartnerRole</code>, <code>A_BusinessPartnerTaxNumber</code>, <code>A_BuPaIdentification</code>, <code>A_BusinessPartnerBank</code>, and <code>A_BuPaIndustry</code> keep important identity and compliance data separate.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a href="#addresses"><span>ADDR</span><strong>A_BusinessPartnerAddress</strong><small>An address can have usage and communication children. Ship-to, bill-to, default, phone, mobile, e-mail, fax, and URL behavior should be treated as structured data.</small><i class="material-symbols-outlined" aria-hidden="true">location_on</i></a>
      <a href="#customer"><span>CUST</span><strong>A_Customer</strong><small>Customer core view. It can have many company codes and many sales areas.</small><i class="material-symbols-outlined" aria-hidden="true">storefront</i></a>
      <a href="#customer"><span>FI</span><strong>A_CustomerCompany</strong><small>Customer data for one company code. This is the FI-AR organizational layer; dunning and withholding-tax entities sit below this level.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="#customer"><span>SD</span><strong>A_CustomerSalesArea</strong><small>Customer data for one sales organization + distribution channel + division. Sales-area tax, texts, partner functions, and address-dependent sales information can sit below it.</small><i class="material-symbols-outlined" aria-hidden="true">shopping_cart</i></a>
      <a href="#supplier"><span>SUPP</span><strong>A_Supplier</strong><small>Supplier core view. It can have many company codes and many purchasing organizations.</small><i class="material-symbols-outlined" aria-hidden="true">factory</i></a>
      <a href="#supplier"><span>FI</span><strong>A_SupplierCompany</strong><small>Supplier data for one company code. This is the FI-AP organizational layer, with dunning and withholding-tax children.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
      <a href="#supplier"><span>MM</span><strong>A_SupplierPurchasingOrg</strong><small>Supplier data for one purchasing organization. Purchasing partner functions and purchasing-organization text are separate children.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">lightbulb</span>
    <p><strong>Memory shortcut:</strong> BP = identity. Customer/Supplier = commercial role. Company Code = accounting. Sales Area = selling. Purchasing Organization = buying.</p>
  </section>

  <section class="research-canvas__inventory" id="keys" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Keys and record identity</p>
      <h2>Organizational segments are separate records with separate keys.</h2>
      <p>This matters for reads, PATCH requests, duplicate prevention, and troubleshooting. Saying “update the customer” is usually too vague.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Customer company</h3><p><strong>Customer + Company Code.</strong> The same customer can have several FI-AR company-code records with different accounting settings.</p></div>
      <div><h3>Customer sales area</h3><p><strong>Customer + Sales Organization + Distribution Channel + Division.</strong> This combination identifies the SD context.</p></div>
      <div><h3>Supplier company</h3><p><strong>Supplier + Company Code.</strong> FI-AP behavior is company-code-dependent.</p></div>
      <div><h3>Supplier purchasing org</h3><p><strong>Supplier + Purchasing Organization.</strong> Procurement behavior can differ by purchasing organization.</p></div>
      <div><h3>Role and classification records</h3><p>Roles, tax numbers, identifications, industries, and similar children use their own keys. Treat them as records with lifecycle, not repeatable fields on one flat object.</p></div>
      <div><h3>Address children</h3><p>Address, usage, and communication records have their own identifiers. Updates must target the intended child instead of assuming “the address” is a single value.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="specialized-entities" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Beyond the logistics core</p>
      <h2>The API is wider than SD and MM.</h2>
      <p>The service also exposes specialized entity families. A Lead should recognize that they exist, but should not force them into every integration scope.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Credit and rating</h3><p>Credit-worthiness and rating entities exist around the BP root. Their relevance depends on the solution and business process.</p></div>
      <div><h3>Financial-services data</h3><p>The service includes financial-services extensions, reporting, and fiscal-year information. These are specialized views, not mandatory “BP basics”.</p></div>
      <div><h3>Data-controller information</h3><p>Data-controller entities support privacy-related master data scenarios. Include them only when the business and legal design requires them.</p></div>
      <div><h3>Payment and other extensions</h3><p>Some releases expose additional payment, address-independent communication, employment, and related entities. Verify the exact release contract before implementation.</p></div>
    </div>
    <p class="ecg-caption"><strong>Scope rule:</strong> separate “available in the service” from “required by my process”. A smaller, owned contract is easier to secure, test, retry, and operate.</p>
  </section>

  <section class="research-canvas__inventory" id="roles" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Roles</p>
      <h2>A role opens a business view. It does not replace the view.</h2>
      <p>This distinction explains many “the BP exists, but the process still fails” incidents.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>FLCU00 · FI Customer</h3><p>Customer accounting role. It is associated with customer company-code processing.</p></div>
      <div><h3>FLCU01 · Sales Customer</h3><p>Customer sales role. Sales-area data can be maintained for the BP, but the required sales area still has to exist.</p></div>
      <div><h3>FLVN00 · FI Supplier</h3><p>Supplier accounting role. It supports supplier data at company-code level.</p></div>
      <div><h3>FLVN01 · Supplier</h3><p>Supplier purchasing role. Purchasing-organization data can be maintained for procurement.</p></div>
    </div>
    <p class="ecg-caption"><strong>Do not confuse role with segment:</strong> assigning <code>FLCU01</code> does not magically create every sales-area record, partner function, tax classification, shipping setting, or business value required by an order.</p>
  </section>

  <section class="research-canvas__inventory" id="customer" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Customer branch</p>
      <h2>General customer, FI customer, and SD customer are different levels.</h2>
      <p>A clean interface design makes ownership explicit for each level instead of sending one oversized “customer payload”.</p>
    </header>
    <div class="research-route-list">
      <a href="#supplier"><span>1</span><strong>Customer general · A_Customer</strong><small>Customer-wide attributes that are not specific to a company code or sales area. The BP-to-customer relationship is one-to-zero-or-one at the API root.</small><i class="material-symbols-outlined" aria-hidden="true">looks_one</i></a>
      <a href="#supplier"><span>2</span><strong>Company code · A_CustomerCompany</strong><small>Accounting behavior for one company code. Ask: can FI-AR post and manage the receivable correctly for this customer?</small><i class="material-symbols-outlined" aria-hidden="true">looks_two</i></a>
      <a href="#supplier"><span>3</span><strong>Sales area · A_CustomerSalesArea</strong><small>SD behavior for one sales org + distribution channel + division. Ask: can this customer participate in the intended order-to-cash flow in this sales area?</small><i class="material-symbols-outlined" aria-hidden="true">looks_3</i></a>
      <a href="#supplier"><span>4</span><strong>Sales-area children</strong><small>Tax data, partner functions, text, and address-dependent sales information have their own entities. Missing child data can break a process even when the sales-area row exists.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
    </div>
    <p class="ecg-caption"><strong>Assessment clue:</strong> if a sales order cannot be created for an otherwise valid customer, check the sales role and the exact sales area before searching the integration middleware.</p>
  </section>

  <section class="research-canvas__inventory" id="supplier" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Supplier branch</p>
      <h2>Supplier general, FI-AP, and purchasing are also different levels.</h2>
      <p>The same supplier can behave differently across company codes and purchasing organizations.</p>
    </header>
    <div class="research-route-list">
      <a href="#addresses"><span>1</span><strong>Supplier general · A_Supplier</strong><small>Supplier-wide attributes. The BP root can have zero or one supplier branch.</small><i class="material-symbols-outlined" aria-hidden="true">looks_one</i></a>
      <a href="#addresses"><span>2</span><strong>Company code · A_SupplierCompany</strong><small>Accounting behavior for one company code. Ask: can FI-AP post and pay correctly?</small><i class="material-symbols-outlined" aria-hidden="true">looks_two</i></a>
      <a href="#addresses"><span>3</span><strong>Purchasing org · A_SupplierPurchasingOrg</strong><small>Procurement behavior for one purchasing organization. Ask: can MM buy from this supplier under the intended purchasing organization?</small><i class="material-symbols-outlined" aria-hidden="true">looks_3</i></a>
      <a href="#addresses"><span>4</span><strong>Purchasing children</strong><small>Partner functions and purchasing-organization texts are separate entities. The wider supplier model can also include data at further retention levels depending on the business scenario.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="addresses" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Addresses and contact data</p>
      <h2>Do not flatten address semantics.</h2>
      <p>A real BP can have several addresses and several communication records. The integration needs stable rules for which address is used for which business purpose.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Address</h3><p><code>A_BusinessPartnerAddress</code> identifies an address object. Treat its key and lifecycle as master data, not as a disposable text block.</p></div>
      <div><h3>Address usage</h3><p><code>A_BuPaAddressUsage</code> describes how an address is used. This is where “default”, shipping, billing, or other usage semantics become important.</p></div>
      <div><h3>Communication</h3><p>Phone, mobile, e-mail, fax, and URL records are child entities. Multiple records and ordinal identifiers can matter when synchronizing changes.</p></div>
      <div><h3>Contact person</h3><p>Contacts are represented through BP/contact entities and relationships. Keep person identity separate from the organization’s central address data.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="cvi" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">CVI behind the API</p>
      <h2>The API does not remove Customer/Vendor Integration.</h2>
      <p>In S/4HANA, Business Partner is the leading object for customer and supplier master data. Customer and supplier creation still depends on CVI mapping and synchronization rules.</p>
    </header>
    <div class="research-route-list">
      <a href="#odata-behaviour"><span>A</span><strong>BP grouping ↔ account group</strong><small>Map Business Partner groupings to the required customer and supplier account groups. This mapping influences the customer/supplier records created behind the BP.</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>
      <a href="#odata-behaviour"><span>B</span><strong>Number assignment</strong><small>Decide whether BP, customer, and supplier numbers should be harmonized. “Same number” is a design choice with number-range prerequisites, not a property to fix later.</small><i class="material-symbols-outlined" aria-hidden="true">pin</i></a>
      <a href="#odata-behaviour"><span>C</span><strong>Mandatory-field alignment</strong><small>BP and customer/supplier field controls must be compatible. A field required on one side but unavailable on the other can stop synchronization.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="#odata-behaviour"><span>D</span><strong>Role and account-group logic</strong><small>Know which BP role and customer/supplier account group the target process requires. Do not let the external system invent these mappings ad hoc.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="#odata-behaviour"><span>E</span><strong>Operational ownership</strong><small>When CVI fails, the API response may be only the start of the investigation. Ownership must cover BP, FI/SD/MM master data, and integration support.</small><i class="material-symbols-outlined" aria-hidden="true">groups</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">warning</span>
    <p><strong>Design trap:</strong> do not postpone number-range and grouping decisions until interface testing. They shape object identity, key mapping, duplicate risk, and migration behavior.</p>
  </section>

  <section class="research-canvas__inventory" id="odata-behaviour" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">OData behavior</p>
      <h2>CRUD is simple. The object graph is not.</h2>
      <p>The technical service is <code>API_BUSINESS_PARTNER</code>. SAP documents GET, POST, PATCH/PUT/MERGE, DELETE, and <code>$batch</code> processing.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Read</h3><p>Use GET and navigate associations. Prefer a narrow request using the exact key and only the fields/expansions needed by the use case.</p></div>
      <div><h3>Create</h3><p>POST can create individual entities. SAP also supports a deep POST for a selected hierarchy rooted at <code>A_BusinessPartner</code>.</p></div>
      <div><h3>Update</h3><p>PATCH, PUT, and MERGE are supported for many individual entities. The entity key matters because company code, sales area, and purchasing organization are different records.</p></div>
      <div><h3>Delete</h3><p>DELETE is entity-specific. Treat deletion of master-data children as a governed business action, not a generic cleanup method.</p></div>
      <div><h3>Batch</h3><p><code>$batch</code> can group service operations. Use it to coordinate multiple entity calls, but design failure handling and reconciliation explicitly.</p></div>
      <div><h3>Response</h3><p>Typical documented responses include 200, 201, 204, 400, 403, 404, and 500. HTTP status is technical evidence, not final business proof.</p></div>
    </div>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">code</span>
      <p><strong>Root examples:</strong> <code>GET /sap/opu/odata/SAP/API_BUSINESS_PARTNER/A_BusinessPartner(...)</code> · <code>POST /sap/opu/odata/SAP/API_BUSINESS_PARTNER/A_BusinessPartner</code> · <code>POST /sap/opu/odata/sap/API_BUSINESS_PARTNER/$batch</code></p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="deep-create" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Deep payload</p>
      <h2>Deep create is useful. Deep update is the trap.</h2>
      <p>For On-Premise 2025 FPS01, SAP documents deep POST support for a defined set of nodes. SAP also states that deep entity maintenance is not supported for operations other than POST.</p>
    </header>
    <div class="research-route-list">
      <a href="#write-strategy"><span>POST</span><strong>Supported deep-create nodes</strong><small><code>A_BusinessPartner</code>, <code>A_BusinessPartnerAddress</code>, <code>A_BusinessPartnerContact</code>, <code>A_CustomerCompany</code>, <code>A_CustomerSalesArea</code>, <code>A_SupplierCompany</code>, and <code>A_SupplierPurchasingOrg</code>.</small><i class="material-symbols-outlined" aria-hidden="true">add_circle</i></a>
      <a href="#write-strategy"><span>PATCH</span><strong>Update the child you mean</strong><small>For changes, address the concrete entity and its full key. Do not resend the original deep-create tree as one PATCH and expect SAP to merge the complete graph.</small><i class="material-symbols-outlined" aria-hidden="true">edit</i></a>
      <a href="#write-strategy"><span>BATCH</span><strong>Coordinate related changes deliberately</strong><small>When several nodes must change together, use a controlled batch or orchestration sequence and define what happens if one business step fails.</small><i class="material-symbols-outlined" aria-hidden="true">dynamic_feed</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="write-strategy" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Write strategy</p>
      <h2>Design writes around ownership and keys.</h2>
      <p>The safest API design is usually smaller than the master-data model.</p>
    </header>
    <div class="research-route-list">
      <a href="#read-strategy"><span>1</span><strong>Define the source of truth per segment</strong><small>Who owns central BP identity? Who owns tax and bank data? Who owns company-code, sales-area, and purchasing-organization records? Do not give every producer write access to every segment.</small><i class="material-symbols-outlined" aria-hidden="true">filter_1</i></a>
      <a href="#read-strategy"><span>2</span><strong>Choose stable external identity</strong><small>Decide how the sender identifies the BP and how SAP number assignment works. Store the mapping outside transient middleware state.</small><i class="material-symbols-outlined" aria-hidden="true">filter_2</i></a>
      <a href="#read-strategy"><span>3</span><strong>Create only the views required by the process</strong><small>A supplier-only scenario does not need random customer roles. A customer used only in one sales area does not need every sales-area combination.</small><i class="material-symbols-outlined" aria-hidden="true">filter_3</i></a>
      <a href="#read-strategy"><span>4</span><strong>Make retries duplicate-safe</strong><small>Do not blindly repeat POST after a timeout. Re-read by your known key or mapping, determine whether the object was committed, then continue from the first missing segment.</small><i class="material-symbols-outlined" aria-hidden="true">filter_4</i></a>
      <a href="#read-strategy"><span>5</span><strong>Reconcile the business state</strong><small>Prove that the intended role and organizational records exist. For SD, validate the required sales area. For MM, validate the purchasing organization. For FI, validate the correct company-code view.</small><i class="material-symbols-outlined" aria-hidden="true">filter_5</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="read-strategy" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Read strategy</p>
      <h2>Do not GET the universe.</h2>
      <p>The service has many associations. Expanding everything for many business partners creates heavy payloads and makes troubleshooting harder.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Use exact keys</h3><p>When you know the BP, customer, supplier, company code, sales area, or purchasing organization, query that scope directly.</p></div>
      <div><h3>Select what you need</h3><p>Use OData query options such as <code>$select</code> for required fields and <code>$expand</code> only for the relationships the use case actually consumes.</p></div>
      <div><h3>Separate operational reads from extraction</h3><p>An online API designed for transactional CRUD is not automatically the best bulk extraction mechanism for analytics or migration.</p></div>
      <div><h3>Handle sensitive reads carefully</h3><p>Bank and identification data are personal-data-relevant areas. SAP documents Read Access Logging behavior for relevant entities.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="integration-choice" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Integration choice</p>
      <h2>OData, SOAP/DRF, and IDoc solve different interaction problems.</h2>
      <p>“Use API because API is modern” is not architecture. Choose from the business interaction, source of truth, volume, timing, and recovery model.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>OData · API_BUSINESS_PARTNER</h3><p>Good for targeted CRUD and request/response integration: create a partner, add a sales area, update a bank record, or read a defined slice of master data.</p></div>
      <div><h3>SOAP + DRF</h3><p>Better aligned with system-to-system master-data replication when SAP owns outbound distribution, change-driven replication, confirmations, and target-system routing.</p></div>
      <div><h3>DEBMAS / CREMAS IDoc</h3><p>Still relevant in established landscapes or when a source only knows classic customer/supplier master data. In an S/4HANA target, BP is created first and CVI creates the customer or supplier view.</p></div>
      <div><h3>Migration</h3><p>A one-time, transformation-heavy conversion is not automatically an OData integration problem. Use the migration approach designed for controlled load, mapping, validation, and cutover.</p></div>
    </div>
    <p class="ecg-caption"><strong>Lead answer:</strong> OData is a CRUD contract. DRF is a replication framework. IDoc is a message format/runtime pattern. They can exist in the same landscape because they operate at different architectural layers.</p>
  </section>

  <section class="research-canvas__inventory" id="security" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Security and privacy</p>
      <h2>Business Partner data is not harmless reference data.</h2>
      <p>It can contain bank accounts, tax identifiers, personal identification, contact data, and other information with strong access requirements.</p>
    </header>
    <div class="research-route-list">
      <a href="#extensibility"><span>AUTH</span><strong>Authorize by business need</strong><small>Separate read and write responsibilities where possible. An integration user that can change every BP segment has a large blast radius.</small><i class="material-symbols-outlined" aria-hidden="true">lock</i></a>
      <a href="#extensibility"><span>RAL</span><strong>Read Access Logging</strong><small>SAP documents RAL for personal-data-relevant bank and identification access in the Business Partner service. Treat logging and privacy controls as part of interface design.</small><i class="material-symbols-outlined" aria-hidden="true">policy</i></a>
      <a href="#extensibility"><span>DATA</span><strong>Minimize payloads and logs</strong><small>Do not copy full BP payloads into middleware logs simply because troubleshooting is easier. Log identifiers, correlation information, and bounded error context.</small><i class="material-symbols-outlined" aria-hidden="true">data_usage</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="extensibility" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Extensibility</p>
      <h2>Custom fields follow business contexts, not one generic API extension.</h2>
      <p>SAP documents separate extensibility contexts for the BP root and the main customer/supplier organizational views.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>BP</h3><p><code>BP_CUSTVEND1</code> · Business Partner master data.</p></div>
      <div><h3>Customer</h3><p><code>CUSTOMER_GENERAL</code> · Customer core view.</p></div>
      <div><h3>Customer company</h3><p><code>CUST_COMPANYCODE</code> · Customer company-code core.</p></div>
      <div><h3>Customer sales</h3><p><code>CUST_SALES</code> · Customer sales-area core.</p></div>
      <div><h3>Supplier</h3><p><code>SUPPLIER_GENERAL</code> · Supplier core view.</p></div>
      <div><h3>Supplier company</h3><p><code>SUP_COMPANYCODE</code> · Supplier company-code core.</p></div>
      <div><h3>Supplier purchasing</h3><p><code>SUP_PURORG</code> · Supplier purchasing-organization core.</p></div>
    </div>
    <p class="ecg-caption"><strong>Cloud example:</strong> custom fields must be enabled for the relevant API usage/data source and published. Always verify availability for the exact S/4HANA release and deployment model.</p>
  </section>

  <section class="research-canvas__inventory" id="restrictions" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Important restrictions</p>
      <h2>Know the edges before you design around the API.</h2>
      <p>Current SAP documentation lists restrictions that are easy to miss if you only read entity names.</p>
    </header>
    <div class="ecg-input-grid">
      <article><span>!</span><h3>No deep update</h3><p>Deep entity maintenance is documented for POST, not for other operations.</p></article>
      <article><span>!</span><h3>Relationship limitation</h3><p>The service cannot maintain relationships whose relationship category uses a non-zero differentiation type.</p></article>
      <article><span>!</span><h3>Workforce roles</h3><p>Employee, Freelancer, and Service Performer roles are listed as unsupported for maintenance through this service.</p></article>
      <article><span>!</span><h3>Worker identification</h3><p>SAP does not recommend this A2X service for workforce-person identification data.</p></article>
      <article><span>!</span><h3>Release differences</h3><p>Entity lists and behavior evolve. Do not use a Public Cloud 2608 field list as proof for an older on-premise release.</p></article>
      <article><span>!</span><h3>Custom fields are not automatic</h3><p>Extension fields need the correct business context and API exposure; simply adding a field to a UI does not guarantee it appears in the API.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="failure-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Failure model</p>
      <h2>Separate transport failure from master-data failure.</h2>
      <p>A strong support path stops at the first missing piece of evidence.</p>
    </header>
    <div class="research-route-list">
      <a href="#troubleshooting"><span>400</span><strong>Request rejected</strong><small>Check payload structure, entity key, mandatory values, domain values, field control, and CVI/business validation. A syntactically valid JSON body can still be invalid SAP master data.</small><i class="material-symbols-outlined" aria-hidden="true">report</i></a>
      <a href="#troubleshooting"><span>403</span><strong>Authorization or request protection</strong><small>Check the technical user, service authorization, communication setup, and request-security requirements for the operation.</small><i class="material-symbols-outlined" aria-hidden="true">lock</i></a>
      <a href="#troubleshooting"><span>404</span><strong>Wrong key or missing entity</strong><small>Confirm the exact BP/customer/supplier key and organizational key. A customer can exist while one requested sales-area or company-code row does not.</small><i class="material-symbols-outlined" aria-hidden="true">search_off</i></a>
      <a href="#troubleshooting"><span>500</span><strong>Backend processing failed</strong><small>Move into SAP Gateway and application evidence. The API layer is reporting a backend failure; do not keep retrying the same POST blindly.</small><i class="material-symbols-outlined" aria-hidden="true">error</i></a>
      <a href="#troubleshooting"><span>2xx</span><strong>Technical success</strong><small>Now verify the target business state: BP, role, customer/supplier view, organizational segment, and a representative downstream process.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="troubleshooting" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Troubleshooting sequence</p>
      <h2>Trace from identity to process readiness.</h2>
      <p>This sequence works better than jumping directly between middleware traces and transaction screens.</p>
    </header>
    <div class="research-route-list">
      <a href="#worked-example"><span>1</span><strong>Was the HTTP request accepted?</strong><small>Capture method, URL, entity key, response code, error body, and correlation information.</small><i class="material-symbols-outlined" aria-hidden="true">filter_1</i></a>
      <a href="#worked-example"><span>2</span><strong>Does the BP exist once?</strong><small>Confirm the intended Business Partner and the expected number/key mapping. Rule out a duplicate created by a retry.</small><i class="material-symbols-outlined" aria-hidden="true">filter_2</i></a>
      <a href="#worked-example"><span>3</span><strong>Is the expected role present?</strong><small>Check FI Customer, Sales Customer, FI Supplier, or Supplier role as required by the business scenario.</small><i class="material-symbols-outlined" aria-hidden="true">filter_3</i></a>
      <a href="#worked-example"><span>4</span><strong>Does the customer/supplier branch exist?</strong><small>Confirm that CVI produced the intended customer or supplier view and that grouping/account-group logic is correct.</small><i class="material-symbols-outlined" aria-hidden="true">filter_4</i></a>
      <a href="#worked-example"><span>5</span><strong>Does the organizational segment exist?</strong><small>Check the exact company code, sales area, or purchasing organization. Do not accept “customer exists” as proof.</small><i class="material-symbols-outlined" aria-hidden="true">filter_5</i></a>
      <a href="#worked-example"><span>6</span><strong>Are required child records present?</strong><small>For example partner functions, tax data, address usage, or other values needed by the concrete process.</small><i class="material-symbols-outlined" aria-hidden="true">filter_6</i></a>
      <a href="#worked-example"><span>7</span><strong>Can the real process use it?</strong><small>Create the bounded business proof: sales-order eligibility, purchase-order eligibility, FI posting readiness, or the exact scenario under test.</small><i class="material-symbols-outlined" aria-hidden="true">done_all</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="worked-example" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Worked example</p>
      <h2>Create a customer that is actually ready for Order-to-Cash.</h2>
      <p>The exact mandatory fields depend on configuration. The purpose of this example is to show the dependency order, not to provide a universal payload.</p>
    </header>
    <div class="research-route-list">
      <a href="#lead-checklist"><span>1</span><strong>Create or identify the BP</strong><small>Resolve grouping, numbering, organization/person category, name, address, language, and the external identity mapping.</small><i class="material-symbols-outlined" aria-hidden="true">person_add</i></a>
      <a href="#lead-checklist"><span>2</span><strong>Add the customer roles</strong><small>Use the FI and/or Sales Customer role required by the scenario. Do not add roles only because a template contains them.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a href="#lead-checklist"><span>3</span><strong>Create customer/company-code data</strong><small>Add the FI-AR company-code segment when the process requires accounting postings.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="#lead-checklist"><span>4</span><strong>Create the exact sales area</strong><small>Add Sales Organization + Distribution Channel + Division and the required SD values for that commercial context.</small><i class="material-symbols-outlined" aria-hidden="true">store</i></a>
      <a href="#lead-checklist"><span>5</span><strong>Add required children</strong><small>Examples can include tax classification and partner functions. Validate the target configuration instead of copying every field from another customer.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#lead-checklist"><span>6</span><strong>Re-read and prove the process</strong><small>Read back the BP/customer/sales-area state and execute a bounded O2C validation. A 201 response alone is not enough.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="lead-checklist" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead checklist</p>
      <h2>Questions to settle before build starts.</h2>
      <p>If these are unanswered, the interface specification is not ready.</p>
    </header>
    <div class="ecg-input-grid">
      <article><span>01</span><h3>Who owns each segment?</h3><p>Central BP, address, tax, bank, customer FI, customer SD, supplier FI, supplier MM.</p></article>
      <article><span>02</span><h3>What is the business key?</h3><p>External ID, SAP BP number, customer/supplier number, UUID, or a governed mapping.</p></article>
      <article><span>03</span><h3>How is numbering configured?</h3><p>Grouping, account group, internal/external ranges, same-number policy.</p></article>
      <article><span>04</span><h3>What is mandatory?</h3><p>Required fields come from configuration, country/legal requirements, roles, and process design.</p></article>
      <article><span>05</span><h3>What is the write pattern?</h3><p>Deep create, entity POST, PATCH, or batch. Avoid an undefined “upsert everything” contract.</p></article>
      <article><span>06</span><h3>How are retries safe?</h3><p>Detect uncertain commits and duplicates before repeating a create.</p></article>
      <article><span>07</span><h3>What is sensitive?</h3><p>Bank, tax, identification, contact data, and logs need appropriate access and retention rules.</p></article>
      <article><span>08</span><h3>How do we reconcile?</h3><p>Define the receiver state and business test that proves completion.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="assessment" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead assessment</p>
      <h2>Questions that expose real understanding.</h2>
      <p>Answer from the data model and failure boundary, not from memorized endpoint names.</p>
    </header>
    <div class="research-route-list">
      <a href="#answer"><span>Q</span><strong>BP exists, but sales order creation fails. What do you check?</strong><small>I verify the Sales Customer role, exact sales area, required sales-area child data such as tax and partner functions, then process-specific configuration. I do not start with middleware if the BP was already committed.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#answer"><span>Q</span><strong>What is the difference between Business Partner and Customer?</strong><small>BP is the leading identity object. Customer is a business view linked to that BP, with its own general, company-code, and sales-area data.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#answer"><span>Q</span><strong>Can one BP be both customer and supplier?</strong><small>Yes. The root can have both customer and supplier branches and the relevant roles. This is one reason to model the BP as the identity layer instead of duplicating a party.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#answer"><span>Q</span><strong>Why did deep POST work but a deep PATCH fail?</strong><small>SAP documents deep entity maintenance for POST only. Updates are performed against supported individual entities, optionally coordinated through batch/orchestration.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#answer"><span>Q</span><strong>What does CVI still matter for if we use API_BUSINESS_PARTNER?</strong><small>CVI maps and synchronizes the BP with customer/supplier master structures. Grouping, account group, number assignment, role mapping, and mandatory-field compatibility still matter.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#answer"><span>Q</span><strong>OData API or DRF?</strong><small>OData is strong for targeted CRUD. DRF supports controlled SAP-side replication and outbound distribution. The choice depends on interaction and recovery, not on which technology sounds newer.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#answer"><span>Q</span><strong>Where does customer accounting data live?</strong><small>At customer company-code level, represented by <code>A_CustomerCompany</code>. Sales-area data is a different SD segment.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#answer"><span>Q</span><strong>Where does supplier purchasing data live?</strong><small>At purchasing-organization level, represented by <code>A_SupplierPurchasingOrg</code>. Supplier company-code data is a separate FI-AP segment.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#answer"><span>Q</span><strong>What makes a successful interface?</strong><small>The target contains one correct BP with the required roles, customer/supplier views, organizational segments, and child data, and the downstream business process can use it. HTTP 2xx is only one piece of evidence.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="answer" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">30-second answer</p>
      <h2>How I would explain the Business Partner API in an assessment.</h2>
    </header>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span>
      <p><strong>“API_BUSINESS_PARTNER is the OData service around the S/4HANA Business Partner leading object. I do not treat it as one flat customer API. I split the model into central BP data, addresses and identity, then customer and supplier branches, and finally the organizational segments: company code for FI, sales area for SD, and purchasing organization for MM. Deep POST can create selected parts of this hierarchy, but deep update is not supported, so changes target individual entities or a controlled batch. I also check CVI grouping, account groups and number assignment before interface testing. For me, success is not only HTTP 2xx; the required BP roles and organizational views must be usable by the real business process.”</strong></p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sources" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary sources</p>
      <h2>Facts checked against SAP documentation.</h2>
      <p>The explanations, mental models, troubleshooting sequence, and assessment framing are independently written. Entity availability and detailed behavior should always be checked for the exact S/4HANA release and deployment model.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/44e06f22436c43e582db6ccd5250e29b/9fca825858239244e10000000a4450e5.html" target="_blank" rel="noopener"><span>SAP</span><strong>APIs for Business Partner — On-Premise 2025 FPS01</strong><small>Overview of OData, IDoc, SOAP, and DRF integration options for Business Partner, Customer, and Supplier.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/85043858ea0f9244e10000000a4450e5.html" target="_blank" rel="noopener"><span>SAP</span><strong>Business Partner (A2X) — OData API</strong><small>Technical service name, CRUD operations, batch, associations, response codes, RAL, and documented restrictions.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/776fbd534f22b44ce10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Business Partner Master Data Structure</strong><small>General data, company-code data, sales-area data, purchasing-organization data, and the business meaning of each level.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/44e06f22436c43e582db6ccd5250e29b/a9ce55233bd6419f84b4af05df9134fa.html" target="_blank" rel="noopener"><span>SAP</span><strong>Create Business Partner Data with Deep Payload</strong><small>Documented deep-POST entity set for On-Premise 2025 FPS01.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/44e06f22436c43e582db6ccd5250e29b/81c9afd408d24612a580ad0c3f77c8a5.html" target="_blank" rel="noopener"><span>SAP</span><strong>Update Business Partner Data</strong><small>PATCH, PUT, and MERGE support for individual Business Partner, Customer, Supplier, and child entities.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/79781e03a08248de96ff4d84863488ef/5c8189abfed6435b854f6e73cd53f2f4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Customer/Vendor Integration settings</strong><small>Grouping/account-group assignment, same-number behavior, synchronization options, and attribute mapping.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/44e06f22436c43e582db6ccd5250e29b/a04825050c1740ef98032dccb2b8d682.html" target="_blank" rel="noopener"><span>SAP</span><strong>IDocs DEBMAS and CREMAS</strong><small>Customer/supplier replication, change pointers, BP-first processing in S/4HANA, and ID determination considerations.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/f5ea5db84f6d44e6a3f193e3f407ba97.html" target="_blank" rel="noopener"><span>SAP</span><strong>Business Partner API extensibility</strong><small>Business contexts for BP, Customer, Customer Company, Customer Sales Area, Supplier, Supplier Company, and Supplier Purchasing Organization.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
