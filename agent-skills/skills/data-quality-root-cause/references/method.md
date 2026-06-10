# Data Quality Root Cause — Detailed Method

## The Trace Method

The core of this skill is tracing a data defect backward from symptom to entry point. This is not guesswork. It is a systematic walk through the data lifecycle.

### Step 1: Symptom Precision

A vague symptom guarantees a vague root cause. Before tracing, document:
- **Data element:** exact field name, table, and system
- **Wrong value:** what was observed
- **Expected value:** what should have been there
- **System where observed:** the system that reported the defect
- **Business process affected:** which process stops or slows when this field is wrong
- **Number of records:** how many are affected now
- **First occurrence date:** when the defect was first observed

If any of these are unknown, produce a discovery checklist and ask the user to gather them.

### Step 2: Business Impact Identification

Quantify if possible. If exact numbers are unavailable, describe the consequence in process terms:
- Orders blocked → revenue at risk per hour
- Invoices delayed → cash flow impact, compliance risk
- Reports wrong → decision quality risk
- Master data incomplete → downstream integration failures

### Step 3: Backward Trace

Follow the data from the symptom system to the creation point:
1. **Consumption layer:** where the defect was observed (report, interface, downstream system)
2. **Storage layer:** the database or system where the record is stored
3. **Transformation layer:** any ETL, mapping, or derivation that changed the value
4. **Integration layer:** APIs, IDocs, files, or events that moved the data
5. **Entry layer:** the user interface, batch job, or API that created or last modified the record

At each layer, ask: what validation should have caught this? Why did it not?

### Step 4: Root Cause Classification

Use exactly one of these types:

| Type | Definition | When to choose |
|------|------------|----------------|
| Missing rule | No validation or policy exists | No rule covers this data element at all |
| Unenforced rule | Rule exists but is bypassed | Rule exists in one path but not another (API vs GUI) |
| Wrong rule | Rule exists but allows bad data | Rule logic is incorrect or threshold is wrong |
| Upstream data error | Source system sends bad data | Source validation is missing or wrong |
| Integration mapping error | Field mapped incorrectly | Mapping table, segment, or API field is wrong |
| Reference data mismatch | Code values out of sync | Country codes, material groups, account groups differ |
| User error without guardrail | User entered wrong data | No UI validation, no workflow approval, no duplicate check |
| System bug | Software defect | Patchable defect in standard or custom code |
| Unknown | Cannot determine root cause | Not enough data; plan monitoring to discover |

### Step 5: Scope Assessment

Determine:
- **Currently affected:** exact record count
- **Potentially affected:** records that share the same entry point or rule gap
- **Downstream spread:** whether the defect has propagated to other systems

### Step 6: Correction Design

Choose one method:
- **Manual correction:** for small numbers (< 10) with clear rules
- **Mass update with validation:** for larger numbers; always include sample check and approval
- **Reprocessing:** for integration or batch failures where the source is now correct
- **Mapping fix:** for integration errors; fix mapping before correcting records
- **Record merge:** for duplicates; define survivorship rules

### Step 7: Prevention Control Design

The prevention must address the root cause, not the symptom:
- **Missing rule →** add validation at the entry point
- **Unenforced rule →** close the bypass path
- **Wrong rule →** correct the rule logic
- **Upstream data error →** add source validation or mapping
- **Integration mapping error →** fix mapping and add mapping tests
- **Reference data mismatch →** synchronize reference data and add governance
- **User error without guardrail →** add UI validation or workflow step
- **System bug →** patch and add regression test
- **Unknown →** add logging or monitoring to discover the root cause

## Common Trace Pitfalls

1. **Stopping at the symptom system.** If the defect is in SAP, do not assume SAP is the root cause. Check upstream systems.
2. **Blaming the user without checking guardrails.** "User error" is almost always "missing guardrail."
3. **Mass-correcting before fixing the source.** If the source or mapping is still broken, the correction will be overwritten.
4. **Skipping scope assessment.** A "small" correction can become a multi-system remediation.
5. **Proposing unenforceable prevention.** If the prevention requires manual vigilance, it will fail.
