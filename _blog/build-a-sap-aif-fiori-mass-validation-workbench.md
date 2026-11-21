---
layout: blog
title: "Build a SAP AIF Mass Validation Workbench: From Fiori File Upload to ABAP Actions"
description: "A step-by-step S/4HANA implementation pattern for CSV uploads, AIF XML or structured persistence, validation actions, BAPI simulations, error monitoring, and safe retries."
slug: build-a-sap-aif-fiori-mass-validation-workbench
permalink: /blog/build-a-sap-aif-fiori-mass-validation-workbench/
date: 2026-11-03
last_modified_at: 2026-11-03
author: "Dzmitryi Kharlanau"
language: en
category: "SAP integration and migration"
tags:
  - sap-s4hana
  - sap-aif
  - sap-fiori
  - abap
  - data-migration
  - mass-validation
canonical_url: https://dkharlanau.github.io/blog/build-a-sap-aif-fiori-mass-validation-workbench/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: 16
related_articles:
  - /blog/how-to-automate-sap-interface-monitoring-and-recovery-without-creating/
  - /blog/sepa-direct-debit-sap-s4hana-customer-mandate-migration/
  - /blog/why-master-data-distribution-fails-even-when-every-interface-is-green/
---

You open an AIF message. Its processing function calls a sales-order BAPI, commits a transaction, and returns errors to a monitoring worklist. But where did the message come from? Was it an IDoc, a Fiori file upload, or a custom ABAP program?

The function module is only one part of the answer. In SAP Application Interface Framework (AIF), **the code that submits a message** and **the action that processes it** are often different components.

This guide builds a practical migration pattern: upload a small CSV file, check sales-order prerequisites, see row-level errors in AIF, correct the source data, and retry. It also shows how to trace an existing solution from the Fiori screen back to the business BAPI.

**Outcome:** by the end, you should be able to identify an AIF entry point, configure a demonstration interface, implement a validation action, submit messages from ABAP, and explain which transaction is responsible for persistence.

> **Scope and evidence:** This is a reproducible *implementation blueprint*, not a tested copy of a customer system. Object names, sales areas, and customers are synthetic. Exact configuration labels, function signatures, authorizations, and BAPI behavior must be checked against your installed SAP AIF and S/4HANA release. The AIF runtime and action model are documented by SAP; the Fiori upload app described here is a proposed custom component. Start in a sandbox. The article is pending practitioner review.

## One model, three separate responsibilities

<figure>
<pre aria-label="Architecture: Fiori file upload calls a backend parser, which submits raw messages to AIF. AIF maps and validates messages, calls an action function module, and exposes errors through monitoring.">
Fiori upload / ABAP report / file adapter
                  |
         Parse + check file
                  |
      AIF message submission
                  |
        AIF persistence + runtime
                  |
        Mapping / checks / actions
                  |
       Z... action function module
          /                  \
    VALIDATE mode         EXECUTE mode
    No business write     Optional business BAPI
          \                  /
        Per-message status + log
                  |
        /AIF/ERR  +  /AIF/IFMON
</pre>
<figcaption>Reference flow. The Fiori UI is an optional entry channel, not a built-in requirement for AIF.</figcaption>
</figure>

The three responsibilities are:

1. **Ingress:** the Fiori OData or RAP handler (or an ABAP batch report) accepts and parses the file. It should not silently create business documents.
2. **AIF processing:** AIF stores individual raw messages, determines the interface, executes mappings/checks/actions, and makes failures monitorable.
3. **Business logic:** an AIF Action FM can validate data, run a simulation, or call a posting BAPI. Its transaction handling must agree with AIF's configured commit mode and level.

AIF supports IDoc, proxy, XML/structured persistence, and other integration scenarios. **Seeing a BAPI in an Action FM does not prove that the source was an IDoc.** SAP explicitly documents calling AIF from a report or function module using the XML enabler. [SAP Help: AIF persistence and runtime](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4db1676c3f114f119b500bd80ccd944d/5857a106a19843fcb5007616a5373395.html).

## First, reverse-engineer the existing upload

Before building anything new, pick *one* message with a known creation time and answer these questions.

<div class="table-scroll study-table" tabindex="0" role="region" aria-label="Existing AIF interface tracing checklist">
<table class="study-table__table">
<thead><tr><th scope="col">Question</th><th scope="col">Where to look</th><th scope="col">Evidence to record</th></tr></thead>
<tbody>
<tr><td>Which AIF interface handled it?</td><td><code>/AIF/ERR</code> → message details; <code>/AIF/CUST</code> → Define Interfaces</td><td>Namespace, interface name, version, message GUID and time</td></tr>
<tr><td>Which runtime stores the message?</td><td><code>/AIF/CUST</code> → Additional Interface Properties → Specify Interface Engines</td><td>Application, persistence, selection and logging engines</td></tr>
<tr><td>Which code called the BAPI?</td><td><code>/AIF/CUST</code> → Define Actions / Define Structure Mappings; <code>SE37</code></td><td>Action FM, calling sequence, commit settings, returned messages</td></tr>
<tr><td>Who submitted data to AIF?</td><td>Where-used search for <code>/AIF/CL_ENABLER_XML</code>, <code>TRANSFER_TO_AIF</code> and <code>TRANSFER_TO_AIF_MULT</code>; debug the upload handler</td><td>Feeder report/class/FM, run or service identity, file batch ID</td></tr>
<tr><td>Did a Fiori app send the file?</td><td>Browser Network tab → upload request; <code>/IWFND/MAINT_SERVICE</code> or RAP service binding; <code>/IWFND/ERROR_LOG</code> when needed</td><td>UI app, OData endpoint, backend handler and request correlation ID</td></tr>
<tr><td>Was it really an IDoc?</td><td>Configured IDoc engine and actual record in <code>WE02</code>/<code>WE05</code></td><td>Basic type, message type, IDoc number, sender, port</td></tr>
</tbody>
</table>
</div>

**Two implementations can look similar in the monitor.** Pattern A is *file → AIF persistence → AIF Action → BAPI*. Pattern B is *file → custom FM → BAPI → custom AIF logging*. In Pattern B, AIF may not own the transaction or the replay mechanism. Inspect the caller of the AIF API and the interface engines before claiming which pattern you have.

If you find a direct call to <code>BAPI_TRANSACTION_COMMIT</code> inside an Action FM, inspect **AIF Action Commit Mode, Commit Level, and retry flags** before changing anything. Do not introduce a second commit simply because another program uses one. SAP's AIF learning material explicitly covers commit mode and commit level as part of Action design.

## The example we will build

Imagine a migration team needs to check whether proposed sales orders can be created after customer, material, tax and route data have been loaded. The initial objective is **readiness**, not posting.

- One external order is one AIF message. Multiple item rows belonging to one order should be grouped into one structured message before submission.
- The default mode is **VALIDATE**. No business documents are created.
- Each message carries a batch ID, row ID and external order key.
- Errors are visible against a business key, not merely as a generic "upload failed" notification.
- **EXECUTE** is a separate, controlled enhancement; it is not enabled in this demo.

Download the [synthetic sample CSV](/assets/examples/sap-aif-mass-validation-sample.csv). Replace its example master-data keys with valid test data for your own sandbox. Rows 2 and 3 contain deliberate omissions; row 1 is *not* guaranteed to pass in your system.

<div class="table-scroll study-table" tabindex="0" role="region" aria-label="Example source fields and validation">
<table class="study-table__table">
<thead><tr><th scope="col">Field</th><th scope="col">Why it exists</th><th scope="col">First validation</th></tr></thead>
<tbody>
<tr><td><code>external_key</code></td><td>Stable source/business identity</td><td>Required; unique within agreed migration scope</td></tr>
<tr><td><code>sold_to</code>, <code>ship_to</code></td><td>Partner readiness</td><td>Required and extended to the relevant sales area</td></tr>
<tr><td><code>sales_org</code>, <code>dist_channel</code>, <code>division</code></td><td>Sales-area context</td><td>Allowed combination; data exists in target</td></tr>
<tr><td><code>material</code>, <code>quantity</code></td><td>Item readiness</td><td>Material available for sales; quantity positive</td></tr>
<tr><td><code>batch_id</code>, <code>row_id</code></td><td>Traceability</td><td>Known upload and source position</td></tr>
</tbody>
</table>
</div>

## Build it step by step

### Step 1 — Decide the transaction boundary

Choose one business object as the unit of processing. Here, the unit is **one sales order**, not the whole spreadsheet and not necessarily one spreadsheet row.

Create an upload contract that defines required fields, allowed modes, stable external keys, file version, maximum size, maximum row count, and error format. Agree on whether the same external key can be submitted again for validation. Decide how successful posting will be reconciled with that key if EXECUTE is added later.

**Why this matters:** if 300 rows form 50 orders, blindly creating 300 AIF messages may split a transaction across unrelated retries.

### Step 2 — Create the ABAP Dictionary structures

In <code>SE11</code>, create demonstration structures such as:

- <code>ZMG_S_SO_RAW</code> — batch ID, external order ID, source row, requested mode, header, partners and nested items.
- <code>ZMG_S_SO_WORK</code> — the internal format consumed by checks and the action. Reuse the raw structure if no transformation is needed.
- <code>ZMG_T_SO_RAW</code> — table type of <code>ZMG_S_SO_RAW</code> for multiple messages.

Use SAP DDIC types where possible; decide field conversion explicitly. File parsing and field mapping are different problems. A malformed CSV should fail at the upload boundary, while a syntactically valid but business-invalid sales order should produce an AIF error.

For a minimal first run, use one item per order and include fields matching the sample CSV. Extend to nested item tables only after you have confirmed the first end-to-end trace.

### Step 3 — Define the AIF interface

In <code>/AIF/CUST</code>:

1. Go to **Interface Development → Define Namespace**. Create a demonstration namespace such as <code>ZMG</code>.
2. Go to **Define Interfaces**. Create <code>SO_CHECK</code>, version <code>1</code>, with the chosen raw and SAP data structures.
3. Go to **Additional Interface Properties → Specify Interface Engines**. Select engines appropriate for AIF-owned persistence/runtime.
4. Create an XML interface determination if several interfaces use the same raw structure.
5. Assign recipients and monitoring permissions if users need alerts or scoped worklists.

For new interfaces on SAP HANA, SAP recommends **structured persistence** over XML persistence; the API is nevertheless named <code>/AIF/CL_ENABLER_XML</code>. Verify which engines and persistence options your release supports. [SAP Help: configuring AIF XML runtime and structured persistence](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4db1676c3f114f119b500bd80ccd944d/5857a106a19843fcb5007616a5373395.html).

### Step 4 — Define mappings and checks

In <code>/AIF/CUST</code> → **Define Structure Mappings**, map source fields to the SAP working structure. Start with transparent one-to-one mappings, then add field conversions where needed. Use <code>/AIF/IFB</code> if the graphical mapping view is more convenient.

Add checks for the first demo:

1. External key is present.
2. Sold-to party is present.
3. Sales area is complete.
4. At least one item exists and has a positive quantity.
5. A supplied material identifier is not blank.

Business-dependent checks (such as customer sales-area extensions, tax conditions, route determination, or credit setup) need explicit business rules and target-system evidence. Do not invent a valid tax rate or a route in a migration utility.

### Step 5 — Create a validation Action FM

In <code>/AIF/CUST</code> → **Define Actions**, create a validation-only action such as <code>ZMG_SO_VALIDATE</code>, then assign it in the structure mapping.

An AIF Action consists of one or more function modules. SAP provides templates such as <code>/AIF/FILE_TEMPL_PROCESS</code> and a documented Action FM signature. Copy the relevant template in <code>SE37</code> rather than creating an arbitrary FM signature. In the template, <code>CURR_LINE</code> carries the component being processed, <code>RETURN_TAB</code> carries <code>BAPIRET2</code> messages, and <code>SUCCESS</code> indicates the result.

The following is an **illustrative body**, assuming your main component has the fields shown. Adapt the interface parameters and DDIC types from the generated template:

~~~abap
"Inside the AIF Action FM; use the installed AIF template signature.
IF curr_line-external_key IS INITIAL.
  APPEND VALUE bapiret2(
    type    = 'E'
    id      = 'ZMG'
    number  = '001'
    message = 'External order key is missing' ) TO return_tab.
  CLEAR success.
  RETURN.
ENDIF.

IF curr_line-sold_to IS INITIAL.
  APPEND VALUE bapiret2(
    type    = 'E'
    id      = 'ZMG'
    number  = '002'
    message = 'Sold-to party is missing' ) TO return_tab.
  CLEAR success.
  RETURN.
ENDIF.

IF curr_line-quantity <= 0.
  APPEND VALUE bapiret2(
    type    = 'E'
    id      = 'ZMG'
    number  = '003'
    message = 'Quantity must be greater than zero' ) TO return_tab.
  CLEAR success.
  RETURN.
ENDIF.

success = 'X'. "No business write in VALIDATE mode.
~~~

Create the corresponding message class in <code>SE91</code>, use the correct message number and variables, and confirm how your AIF release maps <code>RETURN_TAB</code> to the error log. For a production implementation, prefer several precise checks with actionable error messages over one opaque "validation failed" message.

Configure **Stop Processing on Error** when a later Action depends on successful validation. Do not enable **Restart Always** indiscriminately on business-creation actions; SAP's Action course shows why it can cause repeated execution.

### Step 6 — Submit messages from a feeder program

AIF must receive raw messages. SAP documents two methods:

- <code>/AIF/CL_ENABLER_XML=>TRANSFER_TO_AIF</code> for one message.
- <code>/AIF/CL_ENABLER_XML=>TRANSFER_TO_AIF_MULT</code> for multiple messages.

Build the CSV parser and row grouping in a report or service class. Then submit the resulting DDIC-typed messages. This snippet shows **only the AIF handoff**, not a complete parser or Fiori implementation:

~~~abap
"Prerequisite: lt_messages is a table of ZMG_S_SO_RAW.
"Populate it from a validated, parsed, grouped file first.

TRY.
    /aif/cl_enabler_xml=>transfer_to_aif_mult(
      EXPORTING
        it_any_structure = lt_messages ).
  CATCH cx_root INTO DATA(lx_aif).
    "Translate to your upload API's error response
    "and log the failed submission without exposing file contents.
ENDTRY.
~~~

The exact available optional queue parameters depend on the installed release; inspect the method in <code>SE24</code>. If a runtime configuration group is not supplied, SAP documents that the default configuration group is used. Importantly, **an accepted AIF submission is not proof that the sales-order check has finished**.

For the first technical test, submit one message from <code>SE38</code>. This isolates AIF configuration from Fiori file handling.

### Step 7 — Configure execution and monitoring

Use <code>/AIF/PERS_CGR</code> to configure the runtime group and its background execution strategy. The group controls how persisted messages are scheduled and grouped. Use <code>SM37</code> for related background jobs.

Open <code>/AIF/ERR</code> and select the namespace, interface and version. Confirm the raw data, mapped data, log messages, business keys and reprocessing behavior. Use <code>/AIF/IFMON</code> for the wider interface view.

AIF's queue/runtime statuses are separate from the business result. A message that was submitted or scheduled may still fail during its Action.

### Step 8 — Connect a small Fiori upload screen

A custom SAPUI5/Fiori UI can expose an upload control and a simple results view. Its backend may be implemented using an OData/Gateway service or a RAP service, depending on the landscape.

The minimal backend contract is:

1. Accept the file, verify permissions, enforce size/type limits, and scan or sanitize it.
2. Parse CSV to your **versioned upload contract**; reject malformed headers and duplicates.
3. Group records by external order key and perform structural validation.
4. Assign a <code>batch_id</code> and submit one AIF message per business object via the feeder.
5. Return the batch correlation ID immediately; display AIF processing results separately.
6. Let authorized support users navigate to AIF for detailed errors and controlled retries.

Do not describe this as a standard SAP-delivered Fiori mass-upload application. The UI and its Gateway/RAP handler are **custom work** in this blueprint. For file-upload hardening, SAPUI5 guidance covers media-type restrictions, file-size checks, virus scanning, and backend sanitation. [SAP Help: enabling stream support](https://help.sap.com/docs/SAPUI5/d625376e710e40cb9d40e43e1b02933b/b236d32d48b74304887b3dd5163548c1.html).

An even smaller first iteration is to **skip Fiori** and run the feeder as an authorized ABAP report. Once AIF messages and results behave correctly, add the browser UI.

### Step 9 — Only then consider sales-order simulation

If you need SAP SD's own application checks rather than just master-data and file validation, a separate controlled branch can call <code>BAPI_SALESORDER_CREATEFROMDAT2</code> with <code>TESTRUN = 'X'</code> using properly assembled header, partner, item and schedule-line tables. Treat the BAPI test result as **a simulation**, not as evidence that a later posted order will succeed under changed configuration or data.

~~~abap
"Illustrative call fragment inside a dedicated simulation action.
CALL FUNCTION 'BAPI_SALESORDER_CREATEFROMDAT2'
  EXPORTING
    order_header_in  = ls_header
    order_header_inx = ls_headerx
    testrun          = 'X'
  IMPORTING
    salesdocument    = lv_sales_doc
  TABLES
    return           = lt_return
    order_items_in   = lt_items
    order_items_inx  = lt_itemsx
    order_partners   = lt_partners.
~~~

Map <code>lt_return</code> into the AIF Action's <code>RETURN_TAB</code>, decide which errors should stop processing, and verify the test-run behavior in your target release. Never call <code>BAPI_TRANSACTION_COMMIT</code> for a validation-only flow.

**If EXECUTE is added:** design a separate authorized posting path, an idempotency registry keyed by source order, a business-object lock, reconciliation against the created sales document, and documented commit ownership. AIF Actions have **Commit Mode** and **Commit Level** settings. A manual <code>BAPI_TRANSACTION_COMMIT</code> inside the FM may conflict with framework-managed commits or retry semantics. Review that LUW design as a whole rather than copying a commit statement into every example. See [SAP Learning: AIF Actions](https://learning.sap.com/courses/mastering-sap-application-interface-framework/exploring-the-role-of-actions-in-the-sap-application-interface-framework) and [SAP Help: BAPI transaction model](https://help.sap.com/docs/ABAP_PLATFORM_NEW/166400f6be7b46e8adc6b90fd20f3516/4d5b102ba1483d8fe10000000a42189e.html).

## Test the failure path, not just the happy path

Use the sample CSV and run these acceptance checks in a sandbox. The expected results are **design targets**, not evidence that the code above has been deployed or tested.

<div class="table-scroll study-table" tabindex="0" role="region" aria-label="Mass validation acceptance scenarios">
<table class="study-table__table">
<thead><tr><th scope="col">Test</th><th scope="col">Expected result</th><th scope="col">What it proves</th></tr></thead>
<tbody>
<tr><td>Complete source row with real sandbox master data</td><td>AIF processing succeeds; zero documents posted</td><td>Ingress, mapping, checks and success log</td></tr>
<tr><td>Missing sold-to or material</td><td>Action/check error linked to external order key</td><td>Business-readable diagnosis</td></tr>
<tr><td>Invalid CSV header</td><td>Upload rejected before AIF submission</td><td>File/schema boundary</td></tr>
<tr><td>Same file submitted twice</td><td>Controlled duplicate policy; no silent posting</td><td>Batch correlation and idempotency design</td></tr>
<tr><td>One message corrected and reprocessed</td><td>Only eligible failed message is retried</td><td>Safe recovery scope</td></tr>
<tr><td>Runtime/background job interrupted</td><td>Failure found by operations; no blind bulk replay</td><td>Operational control</td></tr>
</tbody>
</table>
</div>

For a stuck XML or structured-persistence message that cannot be restarted from normal monitoring, SAP documents <code>/AIF/XML_RESTART</code>. Treat it as an administrator recovery path, not a default batch-retry button. [SAP Help: AIF runtime and restart](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4db1676c3f114f119b500bd80ccd944d/5857a106a19843fcb5007616a5373395.html).

## The questions to answer before go-live

- **Who owns the data?** The migration team supplies candidate records; sales and tax owners approve rules the system cannot infer.
- **What is a failure?** Invalid file, master-data gap, missing condition record, configuration gap, BAPI error, or technical runtime failure must not all get the same label.
- **Can a message be retried?** Validation can normally be repeated. Posting can be repeated only after checking the external key and the actual SAP document.
- **Who commits?** The Action FM or the framework-controlled transaction design — never both without deliberate, tested coordination.
- **What is the evidence?** Batch ID → external order key → AIF message GUID → AIF result → (only if posted) SAP sales document number.
- **What is protected?** Upload roles, allowed MIME types, virus scanning, PII in payloads and logs, retention, and access to the results.

A green AIF interface is an integration status. It does not automatically prove that the target migration scenario is business-ready. Reconcile actual master data and test outcomes separately.

## Reference checklist: what you should have after the exercise

1. A documented upload schema and a synthetic CSV test file.
2. Raw/SAP DDIC structures and one namespace/interface/version.
3. Appropriate persistence/runtime engines and interface determination if needed.
4. Mapping, validation checks, and one Action FM based on the AIF template.
5. A feeder report that submits messages using <code>TRANSFER_TO_AIF_MULT</code>.
6. A visible AIF error for a deliberately invalid test row.
7. A documented retry policy and a clear boundary between validation and creation.
8. Only after that: a Fiori file-upload screen.

## Official documentation and further reading

- [SAP Help — AIF prerequisites: reports, FMs, BAPIs, IDoc and XML interface options](https://help.sap.com/docs/SUPPORT_CONTENT/abapconn/3354079451.html)
- [SAP Help — Configuring XML runtime with structured persistence, enabler methods, queue groups and restart](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4db1676c3f114f119b500bd80ccd944d/5857a106a19843fcb5007616a5373395.html)
- [SAP Learning — Exploring Actions, Action FMs, commit settings and restart behavior](https://learning.sap.com/courses/mastering-sap-application-interface-framework/exploring-the-role-of-actions-in-the-sap-application-interface-framework)
- [SAP Help — Interface Creation, mappings, checks and actions](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4db1676c3f114f119b500bd80ccd944d/f0d1b60ff43c45efad71398b1214db04.html)
- [SAP Developer Center — IDoc-specific AIF tutorial](https://developers.sap.com/tutorials/aif-idoc-monitoring-interface-customize/) — a **different** scenario, useful for comparison.
- [SAP Help — BAPI transaction model](https://help.sap.com/docs/ABAP_PLATFORM_NEW/166400f6be7b46e8adc6b90fd20f3516/4d5b102ba1483d8fe10000000a42189e.html)
- [SAP Help — SAPUI5 file-upload/stream security](https://help.sap.com/docs/SAPUI5/d625376e710e40cb9d40e43e1b02933b/b236d32d48b74304887b3dd5163548c1.html)

The practical architectural lesson is simple: **separate submission, validation, persistence, and business posting**. Then a mass-upload utility becomes an inspectable migration control, rather than a spreadsheet that can accidentally create 300 transactions twice.
