---
layout: blog
title: "SEPA Direct Debit in SAP S/4HANA: Customer Data, Mandates, and Migration"
description: "A practical guide to SEPA customer mandates in SAP: how direct debit works, what a Business Partner must have, how to migrate mandates, and how to test."
slug: sepa-direct-debit-sap-s4hana-customer-mandate-migration
permalink: /blog/sepa-direct-debit-sap-s4hana-customer-mandate-migration/
date: 2026-10-29
last_modified_at: 2026-10-29
author: "Dzmitryi Kharlanau"
language: en
category: "SAP master data"
tags:
  - sap-s4hana
  - sap-master-data
  - fi-ar
  - sepa
  - data-migration
canonical_url: https://dkharlanau.github.io/blog/sepa-direct-debit-sap-s4hana-customer-mandate-migration/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: 14
related_articles:
  - /blog/the-hidden-operational-cost-of-poor-master-data-in-sap/
  - /blog/why-master-data-distribution-fails-even-when-every-interface-is-green/
---

A customer is already in SAP S/4HANA. Their address is correct. Their bank account is available. The finance team now asks: **“Have we migrated SEPA?”**

It sounds like another customer master data field. It is not.

If the company wants to collect money directly from that customer's bank account, it needs more than an IBAN. It needs a valid **SEPA Direct Debit mandate**: the customer's authorisation to collect payments.

This difference is easy to miss during migration. A customer can be fully available for sales and invoicing, but still be unable to pay by direct debit.

This guide explains what SEPA means, where the data lives in SAP, what needs to move to S/4HANA, and how to check that the result works. The focus is **incoming customer payments in FI-AR**, not supplier payments or an FI-CA implementation.

## First: SEPA is not one payment method

SEPA stands for **Single Euro Payments Area**. It supports common rules for euro payments across participating countries.

Two payment flows are especially important:

| Payment flow | Who starts the payment? | Simple example |
| --- | --- | --- |
| **SEPA Credit Transfer (SCT)** | The payer sends money. | A customer makes a bank transfer to pay an invoice. |
| **SEPA Direct Debit (SDD)** | The creditor asks the bank to collect money from the payer. | A company collects a monthly service fee from its customer. |

This article is about **SDD**. A signed mandate is essential here. Do not confuse it with the customer's bank details or with the ability to receive a normal bank transfer.

There are two SDD schemes:

- **Core** is used for consumers and can also be used for business payers. It offers stronger refund rights. Under the scheme, a payer can request a refund for an authorised collection within eight weeks.
- **B2B** is designed only for business payers. The payer's bank must check that an appropriate mandate is confirmed. Refund rights for authorised collections are different from Core.

The exact scheme matters during migration. Do not automatically treat all mandates as Core or convert B2B mandates without an explicit business and banking decision. See the [European Payments Council overview of SEPA Direct Debit](https://www.europeanpaymentscouncil.eu/what-we-do/sepa-direct-debit).

## A customer, a bank account, and a mandate are different objects

Think of customer direct debit as four connected layers.

| Layer | Business question | SAP responsibility |
| --- | --- | --- |
| **Customer / Business Partner** | Who owes us money? | Business Partner and customer master data; FI customer role and relevant company code |
| **Customer bank details** | Which bank account may be debited? | Bank details of the Business Partner or customer |
| **SEPA mandate** | Has this customer authorised us to collect from that account? | SEPA mandate management in Financial Accounting (FI-AR) |
| **Payment process** | Can SAP select the invoice and produce the correct collection? | Payment method, creditor ID, payment program, bank and payment-medium configuration |

**Important:** the presence of a customer and an IBAN does not prove that a valid mandate exists.

For an FI-AR scenario, the Business Partner normally needs the appropriate **FI Customer** data (for example, role `FLCU00` and the company code segment). A separate Sales role and sales area are relevant if the process starts in SD, but they are not universal prerequisites for every FI-only direct debit.

### A simple example

All values below are fictional.

- Customer in the old SAP system: `00004567`
- Customer in S/4HANA: `10004567`
- Customer bank account: IBAN ending in `1234`
- Mandate reference: `SDD-2026-0042`
- Creditor ID: the company's registered SEPA creditor identifier
- Mandate state: active
- Payment scheme: Core

The customer number changed during migration. The bank account did not. **The mandate must still point to the correct target customer and account**, while keeping its legally relevant identity and evidence.

Creating customer `10004567` in S/4HANA does not create mandate `SDD-2026-0042` automatically.

## What is stored in a SEPA mandate?

A mandate is permission to collect payments. It is also an object that SAP must be able to select during payment processing.

Typical data includes:

| Mandate information | Why it matters |
| --- | --- |
| Mandate reference | Identifies the authorisation; often called the unique mandate reference (UMR) |
| Creditor identifier | Identifies the company collecting payment |
| Customer or payer reference | Connects the authorisation to the correct debtor |
| Debtor IBAN | Identifies the account to be debited |
| Scheme and collection type | Distinguishes Core/B2B and one-off/recurring use |
| Signature date and evidence | Helps demonstrate that the authorisation was given |
| Status, validity and usage | Helps decide whether a mandate can be used again |

Some SAP migration templates expose technical fields such as `MNDID` (mandate reference), `REC_CRDID` (creditor ID), `SND_ID` (sender/debtor ID), `SND_TYPE`, `SND_IBAN`, `SIGN_DATE`, `SIGN_CITY`, and `SND_BIC`. **Do not assume the same mandatory fields in every release or migration approach.** Check the template generated by your target Migration Cockpit.

For example, SAP's Cloud Public Edition documentation lists additional required data for an active mandate, including signature information and creditor/debtor information. That is a useful reference, not a replacement for your system's actual field rules. See [SAP Help: FI - SEPA mandate](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/1d1601c422e94d569d37263875ee4ff6.html).

**Keep the evidence, not just the fields.** If you cannot show that the customer granted authorisation, copying a record into a new database does not solve the compliance problem. Check the scheme rules for cancellations, changes, retention and mandates that have not been used for a long time. The European Payments Council explains the [SDD mandate](https://www.europeanpaymentscouncil.eu/what-we-do/epc-payment-schemes/sepa-direct-debit/sdd-mandate) and publishes [operational clarifications](https://www.europeanpaymentscouncil.eu/document-library/guidance-documents/clarification-paper-sepa-direct-debit-core-and-sepa-direct).

## Where to find SEPA data in SAP

In a typical SAP GUI-based FI-AR environment, these transactions are useful:

| Transaction or object | What to check |
| --- | --- |
| `BP` | Customer identity, FI customer role, company code and bank details |
| `FSEPA_M1` | Create a mandate |
| `FSEPA_M2` | Change a mandate |
| `FSEPA_M3` | Display a mandate |
| `FSEPA_M4` | Find and list mandates |
| `SEPA_MANDATE` | Technical table for read-only investigation, where available |
| `F110` | Payment proposal and payment-run checks if the classic automatic payment program is used |

Transactions, authorisations and Fiori alternatives depend on the SAP release and deployment. The FI mandate transaction codes are documented in [SAP Help: SEPA Direct Debits in Treasury and Risk Management](https://help.sap.com/docs/SAP_ERP/5bf929284e00453ba04be76690e6bed4/d5ff4252ba5f1b13e10000000a44176d.html).

Do not update a SEPA mandate directly through database tables. Use an SAP-supported maintenance or migration process so that validations and business logic are applied.

## How a direct debit moves through the business process

A working customer direct debit is more than a successful data load.

1. **Customer setup.** The payer and bank details exist in S/4HANA.
2. **Mandate setup.** A valid mandate is available for the payer, account and collecting company.
3. **Sales and invoice.** In an SD scenario, the sales document is relevant for SEPA and the correct payer/payment method is determined. The invoice creates an open receivable.
4. **Payment selection.** The payment program identifies due receivables and the required mandate using the configured payment method.
5. **Collection preparation.** SAP creates the payment data or bank file using the configured payment medium.
6. **Bank result and accounting.** The actual collection and any return or rejection must be monitored and reconciled through the agreed banking process.

SAP documents that SD can select an existing FI-AR mandate or create one from a SEPA-relevant sales document. The payer and relevant payment terms can affect this determination. See [SAP Help: SEPA Direct Debits in SD](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/ad0bef26b37045ddb256f0bcfb8ff445.html) and [Process a Sales Document with a SEPA Mandate](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/6f1d59146ff144748b1ee315026ff2df.html).

This creates a useful diagnostic rule:

**If the customer exists but a direct debit fails, investigate the payer, bank details, mandate and payment configuration separately.** Do not immediately treat the failure as missing customer master data.

## Migration plan: customers already exist in S/4HANA

Imagine a source SAP system contains customer mandates and the target S/4HANA already contains the Business Partners. The task is to migrate the mandates without creating wrong authorisations or broken links.

### Step 1 — Agree on the scope and owners

Before extracting data, confirm:

- Is the source SAP ERP/AFS or another application?
- Is the target S/4HANA on-premise, private cloud or public cloud? Which release?
- Is the process FI-AR or FI-CA?
- Which company codes, creditor identifiers, schemes and customer groups are in scope?
- Will historic, expired, cancelled and unused mandates be migrated, archived, or excluded after an approved decision?
- Who confirms the legal mandate evidence and who owns the FI payment configuration?

The answers determine both the migration object and the acceptance criteria.

### Step 2 — Inventory the source mandates

Use `FSEPA_M4` to inspect and list source mandates. If technical access is permitted, use `SEPA_MANDATE` for read-only analysis.

Create an inventory with source customer, mandate reference, creditor ID, scheme, IBAN, status, signature details, relevant validity or usage dates and evidence availability.

Do not count only the active ones. Separate **all found**, **in scope**, **ready**, **excluded with reason**, and **requiring business review**. Otherwise, a small target count may look like a successful migration when records were simply lost.

### Step 3 — Map each mandate to the target payer

Build a mapping table:

| Source field | Target question |
| --- | --- |
| Source customer / payer | What is the corresponding S/4HANA customer? |
| Source bank account | Is the same authorised IBAN present on that target Business Partner? |
| Creditor ID / collecting entity | Is the intended creditor and company-code context configured? |
| Mandate reference | Does it already exist in the target? |
| Scheme / status / dates | Is the record still eligible for the intended payment use? |
| Signature proof | Can the business retrieve the original authorisation? |

**Check the actual payer, not only the sold-to party.** In SD, the payer may be a different partner. A valid mandate for the sold-to customer does not automatically authorise a debit from someone else's account.

### Step 4 — Perform a pre-migration readiness check

For every mandate, assign one result:

- **READY:** customer and payer mapping, bank account, creditor context, mandate evidence and target prerequisites are consistent.
- **BLOCKED:** a required customer, bank account or target setup is missing.
- **REVIEW:** legal validity, duplicate status, changed bank account, cancelled mandate or payer ownership is unclear.

Do not resolve **REVIEW** by guessing a value. FI-AR, business and compliance owners should decide.

A compact control sheet can use these columns:

`Source Mandate | Source Payer | Target Payer | Company Code | Creditor ID | Scheme | IBAN Match | Mandate Status | Evidence | Target Duplicate | Readiness | Error/Owner`

This is more useful than a raw source extract: it tells the team what can be loaded and what needs attention.

### Step 5 — Choose the supported migration method

In SAP S/4HANA Migration Cockpit, look for **FI - SEPA mandate**. SAP's on-premise object catalogue lists **Staging Table**, **Direct Transfer - ERP**, and **Direct Transfer - AFS** approaches. Which ones you can actually use depends on the release, activated scope and migration approach.

- **Direct Transfer - AFS / ERP:** consider this when the source is supported and the relevant source-to-target connection is available. Verify selection, mappings and simulation results in your environment.
- **Staging Table:** use the template or staging structure provided by your target version, prepare source data in the required format, and follow the cockpit's validation and migration steps.
- **Special replication or custom approach:** consider only with documented justification and an FI-led technical design, if the standard object does not meet the migration scope.

SAP's [Available Migration Objects for S/4HANA](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/29193bf0ebdd4583930b2176cb993268/8dd142b479f9481891fa8b3f86648df3.html) is the starting point, but the **target system** is the final source of truth for what is available.

**Do not confuse this with Central Finance.** SAP documents an `FSEPA_M4` **Migrate** action in a specific Central Finance process. That does not make it a universal migration method for every S/4HANA project. See [SAP Help: Migrating SEPA Mandates in Central Finance](https://help.sap.com/docs/SAP_S4HANA_ONPREMISE/26c2d5e366bc44c1a98f2a9212a0c49d/b96998502ced4252b0cb5a301a0e7d40.html).

### Step 6 — Load a small pilot batch

Start in a non-production system with a representative sample: different company codes, Core and B2B if used, recurring mandates, different payer relationships and known exceptions.

Record the source count, selected count, rejected count, created count and errors. Correct mapping or configuration issues at the proper owner level and repeat the pilot. Never manufacture a signature date or activate an unsupported mandate merely to make the load pass.

### Step 7 — Reconcile, then test the business flow

Compare source and target by **business keys**, not only by the total number of rows. Check mandate reference, payer mapping, creditor ID, IBAN, scheme, status and dates.

Then test one safe end-to-end case:

1. Find a migrated mandate in `FSEPA_M4` or the supported target app.
2. Confirm the payer and bank account in `BP`.
3. Confirm the SEPA payment method and company-code setup with FI.
4. Prepare a representative test receivable.
5. Run a **payment proposal or equivalent simulation** and inspect mandate selection.
6. Check the intended payment-medium output only in a controlled test setup.

**Do not send a real direct debit to a bank as part of a migration test.** The finance and banking teams own any external end-to-end test and its approvals.

### Step 8 — Plan the cutover delta

A successful dry run is not the final state. Mandates may be created, changed, cancelled or used between the extraction date and go-live.

Agree on a change window or delta mechanism, recheck validity and duplicates, then reconcile the final target state against the approved cutover scope. Keep an audit trail of exclusions, corrections, approvals and the route to the original signed mandate.

## Common problems and how to narrow them down

| Symptom | First evidence to collect | Likely owner |
| --- | --- | --- |
| Customer exists, but no mandate appears | Payer mapping, `FSEPA_M4` search, migration logs | FI-AR / migration |
| Mandate exists, but uses the wrong customer | Source-to-target customer mapping and SD payer | Master data / FI-AR |
| IBAN differs between mandate and BP | Bank details, authorised account and amendment evidence | Master data / finance |
| Mandate rejected during upload | Migration object field errors, status and required signature data | FI-AR / migration |
| Mandate loaded, but payment proposal cannot use it | Status, eligibility, creditor ID, payment method and company-code settings | FI-AR / payments |
| B2B collection rejected by the bank | Mandate confirmation with debtor bank, scheme and bank feedback | Treasury / bank |
| Counts match, but the process fails | Business-key reconciliation and a controlled payment test | Cross-functional team |

There is no useful shortcut from **“mandate exists in a table”** to **“the company can collect money.”** The second statement requires a process check.

## Who should own what?

This work touches several domains, so ownership should be explicit.

- **Master data / MDG:** correct Business Partner identity, customer mapping, FI extension and bank details according to the agreed source of truth.
- **FI-AR:** mandate lifecycle, validation, payment method and business acceptance.
- **Treasury / payments and banking:** creditor identifier, payment-medium setup, external banking arrangements and bank-side tests.
- **Migration team:** extract, mapping logic, controlled load, logs, reconciliation and cutover.
- **Business and compliance owners:** signature evidence, mandate eligibility, scheme rules, retention and approved exclusions.

MDG may govern customer data. **It does not by itself prove that an FI-AR SEPA mandate was migrated or remains valid.**

## Test your understanding

A company has already migrated customer `10004567` to S/4HANA. The customer has the FI role and a valid IBAN. In the sales document, however, a *different* customer is assigned as **payer**. The payment proposal cannot find a valid mandate.

Where should you start?

Do not create a new mandate immediately. First identify the payer used by the payment process, the bank account to be debited, and the mandate authorising that particular payer/account. Then compare those values with the FI configuration and the existing mandate inventory.

This investigation separates a **wrong relationship** from a **missing authorisation**. Both can create a similar payment error, but they require different fixes.

## What “migration complete” should mean

Agree on these acceptance checks before the first load:

1. Every in-scope mandate has an explicit result: migrated, excluded with approved reason, or blocked with an owner.
2. Every migrated record has the correct target payer, creditor reference, bank account, scheme and status.
3. No unexpected duplicate mandate was created, and required signature evidence remains accessible.
4. A controlled payment proposal can select representative migrated mandates, with no external bank collection.
5. Final cutover changes have been captured, reconciled and approved.

The point is not to move rows. It is to preserve **authorised payment capability** while changing systems.

## Sources and scope

The explanation is based on public vendor and scheme-owner documentation, checked on **29 October 2026**:

- [European Payments Council — SEPA Direct Debit overview](https://www.europeanpaymentscouncil.eu/what-we-do/sepa-direct-debit): Core/B2B schemes, authorisation and collection responsibilities.
- [European Payments Council — SDD mandate](https://www.europeanpaymentscouncil.eu/what-we-do/epc-payment-schemes/sepa-direct-debit/sdd-mandate): mandate rules and electronic mandates.
- [SAP Help — SEPA Direct Debits in SD](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/ad0bef26b37045ddb256f0bcfb8ff445.html): sales-document relevance and FI-AR mandates.
- [SAP Help — FI - SEPA mandate (Cloud Public Edition)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/1d1601c422e94d569d37263875ee4ff6.html): staging template and field dependencies.
- [SAP Help — Available Migration Objects (S/4HANA On-Premise)](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/29193bf0ebdd4583930b2176cb993268/8dd142b479f9481891fa8b3f86648df3.html): migration approaches by object.
- [SAP Help — Migrating SEPA Mandates (Central Finance)](https://help.sap.com/docs/SAP_S4HANA_ONPREMISE/26c2d5e366bc44c1a98f2a9212a0c49d/b96998502ced4252b0cb5a301a0e7d40.html): the Central Finance-specific migration action.

**Important boundary:** transaction availability, mandatory template fields, payment-method setup and supported migration objects vary by SAP release and deployment. Confirm them in the target system before execution. Mandate validity and evidence requirements must also be checked against the current scheme rules and your organisation's legal guidance. This article is a practical SAP learning guide, not legal advice.
