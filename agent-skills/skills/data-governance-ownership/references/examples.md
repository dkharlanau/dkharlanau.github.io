# Data Governance Ownership — Examples

## Good Example: Post-Merger Customer Master Ownership

**Situation:** Two companies merge. Both have customer master data in different systems. Integration projects stall because no one can agree which system is the source of truth.

**Method application:**
1. Scoped to "Customer.TaxNumber1" and "Customer.PaymentTerms" only
2. Mapped systems: CRM-A (legacy), CRM-B (legacy), SAP S/4 (target), BW (reporting)
3. Identified stakeholders: Sales Director (business owner), IT Data Lead (technical owner), no steward named
4. Found gap: no data steward for cross-system customer record
5. Cataloged rules: tax number required for DE customers (enforced in CRM-A only, not in CRM-B or SAP)
6. Defined decision rights: Sales Director approves changes, IT Data Lead implements, steward reviews daily

**Output:**
- Ownership Matrix with named owners and gap flags
- Rule Catalog showing porous enforcement across systems
- Governance Action Plan with P1 action: assign steward and synchronize validation rules

**Why this is good:** Narrow scope, specific gaps, named owners, enforceable rules. No tool purchase proposed before ownership is clear.

---

## Bad Example: "Let's Buy a Data Governance Tool"

**Situation:** Data quality is poor. Management approves budget for a data governance platform.

**Approach:** Purchase and deploy tool. Configure it with all data domains.

**Result:** Tool enforces nothing because no one was named as steward. Business units ignore alerts. Tool becomes shelfware.

**Why this is bad:**
- Tool purchased before ownership was defined
- No named stewards to configure or respond to alerts
- No decision rights defined, so no one can approve rule changes
- Scope was "all data," which collapsed under volume
- No enforcement gap analysis; rules were assumed to exist

---

## Good Example: Report Reconciliation Dispute

**Situation:** Finance and Operations both publish "revenue" numbers. They differ by 12%. Each team claims their number is correct.

**Method application:**
1. Scoped to "revenue" metric only
2. Mapped systems: SAP (billing), CRM (opportunities), BW (reporting), Excel (manual adjustments)
3. Found: no agreed definition, no system of record, no reconciliation owner
4. Defined: Finance Director owns the definition, IT owns the system of record, BI team owns the reconciliation procedure
5. Cataloged rules: revenue = billed amount minus credit notes (enforced in SAP only; CRM and Excel use different definitions)

**Output:**
- Data element register with definitions, sources, and owners
- Reconciliation procedure with named owner and review cycle
- Governance Action Plan: standardize definition, retire Excel adjustments, add reconciliation report

**Why this is good:** The governance gap was a definition and ownership problem, not a data quality problem. The solution addresses the root cause.

---

## Bad Example: Naming a Department as Owner

**Situation:** Customer master data has no clear owner.

**Approach:** "Sales owns customer master data."

**Result:** Six months later, customer data quality is unchanged. Sales managers point at each other. No one reviews daily changes.

**Why this is bad:**
- "Sales" is not a person. No one is accountable.
- No steward named for day-to-day care.
- No technical owner for system changes.
- No decision rights defined. Sales cannot approve IT changes.
- No enforcement mechanism. The "owner" has no tools or authority.
