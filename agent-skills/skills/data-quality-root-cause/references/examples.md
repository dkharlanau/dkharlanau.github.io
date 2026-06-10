# Data Quality Root Cause — Examples

## Good Example: Invoice Blocked by Missing Tax Number

**Symptom:** Invoices for German customers fail because TaxNumber1 is empty.

**Trace:**
1. Billing document shows TaxNumber1 = empty → incompletion procedure failed
2. Incompletion procedure checks at invoice time, not at customer creation
3. Customer was created via CRM integration with no tax number validation
4. CRM integration is the entry point

**Root cause classification:** Missing rule (no tax number validation at CRM entry)

**Correction:** Update affected customers with correct tax numbers via mass update with sample check.

**Prevention:** Add tax number validation at CRM-to-SAP interface; strengthen incompletion procedure to block at customer creation.

**Why this is good:** The trace goes all the way to the entry point. The root cause is classified. Prevention addresses the entry point, not just the billing symptom.

---

## Bad Example: "The Data Is Bad"

**Symptom:** "The COGS report is wrong."

**Analysis attempt:** "The material group mapping table was updated six months ago."

**Root cause stated:** "Wrong mapping table."

**Correction:** "Fix the mapping table."

**Prevention:** "Be more careful with mapping table updates."

**Why this is bad:**
- No exact field, value, or record count documented
- No trace to entry point (who updated the table, why, with what approval?)
- Root cause is a narrative, not a classified type
- Prevention is unenforceable ("be more careful" is not a control)
- No owners named
- No validation with stakeholders

---

## Good Example: Duplicate Vendors in Procurement

**Symptom:** Buyers create new vendor records because they cannot find existing ones. Duplicate payment runs occur.

**Trace:**
1. Duplicate vendors in SAP → payment runs include both
2. Buyers search for existing vendors but search help requires exact name matching
3. No data steward reviews new vendor requests against existing records
4. Entry point: vendor creation transaction with weak search and no stewardship

**Root cause classification:** User error without guardrail (missing fuzzy search and stewardship step)

**Correction:** Merge duplicates using survivorship rules. Validate with Finance.

**Prevention:** Add fuzzy search to vendor creation; add data steward approval step for new vendors.

**Why this is good:** The root cause is not "users are careless" but "the system allows careless behavior without guardrails." The prevention is specific and enforceable.

---

## Bad Example: Blaming the Integration

**Symptom:** IDoc status 51 in customer replication.

**Analysis:** "The integration is broken. We need to fix the IDoc."

**Root cause stated:** "Integration error."

**Correction:** "Reprocess the IDoc."

**Prevention:** "Monitor IDoc status more closely."

**Why this is bad:**
- "Integration error" is a symptom, not a root cause
- No investigation of why the IDoc failed (reference data mismatch? schema change?)
- Reprocessing fixes the symptom but the next IDoc will fail the same way
- Monitoring is not prevention; it is detection

---

## Good Example: Wrong Material Group in COGS Report

**Symptom:** COGS report groups materials incorrectly.

**Trace:**
1. Report shows wrong material group → mapping table updated six months ago
2. Mapping table was updated by IT without notifying Finance
3. No change notification workflow exists for mapping tables
4. No report validation step after mapping changes

**Root cause classification:** Missing rule (no change notification workflow for mapping tables)

**Correction:** Remap historical transactions with validation against source system.

**Prevention:** Add change notification workflow for mapping tables; add report validation step after any mapping change.

**Why this is good:** The trace reveals a process gap, not just a data error. The prevention addresses the process gap.
