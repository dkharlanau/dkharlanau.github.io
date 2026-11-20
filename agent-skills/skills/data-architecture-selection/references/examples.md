# Data Architecture Selection — Synthetic Examples

These examples are teaching cases. They are not evidence of real client implementations.

## Example A — ERP revenue by customer

**Request:** “One Customer 360 dashboard across ERP and CRM by the end of the quarter.”

**Weak response:** “Use a lakehouse; it unifies all data automatically.”

**Better response:** Identify whether the report is by Business Partner, sold-to, payer or legal entity; define a conformed customer dimension and historical rule; confirm the SLA; compare a managed warehouse/semantic layer with a lakehouse plus serving model; test mapping, authorization and financial reconciliation. A lakehouse is a candidate, not a conclusion.

**Change one condition:** The report must refresh once nightly, not every two minutes. Remove the unproven requirement for streaming and recalculate operating cost.

## Example B — Distributed domains

**Request:** “Every domain wants its own lake; we need Data Mesh.”

**Weak response:** “Data Mesh is a storage topology. Purchase a mesh tool.”

**Better response:** Identify producers, consumers, funded data-product ownership, a catalog, quality contracts, support model and federated policies. Pilot one product with real consumers. If ownership cannot be funded, use centralized engineering plus explicit domain stewardship instead.

**Change one condition:** Domains have teams but no cross-domain standards. Delay scale-out until interoperability is testable.

## Example C — Documents plus operational facts

**Request:** “Let an AI assistant answer customer delivery questions from PDFs and ERP data.”

**Weak response:** “Copy all ERP records and PDFs to an unrestricted vector store.”

**Better response:** Classify data; keep ERP operational facts in an authorized interface, use document retrieval for cited untrusted text, bind identities and timestamps, enforce access in both retrieval paths, require grounded answers and human review for actions. A raw lake is not a substitute for a trustworthy semantic model.

**Change one condition:** Some documents contain sensitive personal data. Add classification and minimization controls before ingesting anything.

## Review red flags

- “Real time” appears without an SLA.
- Full extracts are used because incremental change handling was not specified.
- Data Mesh is proposed without owners, budgets or data contracts.
- Fabric is claimed to fix source-system master-data errors.
- An architecture diagram has boxes but no failed-path or recovery behavior.
- SCD Type 3 is described as full row-version history (that is Type 2 in Kimball's classification).
