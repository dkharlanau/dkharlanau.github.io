# Architecture Decision Record — Examples

## Good Example: Synchronous vs Asynchronous Customer Master Distribution

**Decision question:** "How should customer master data be distributed from SAP MDG to three downstream systems?"

**Context:**
- Two downstream systems have lower availability than MDG
- Synchronous calls would create cascading failures
- Business accepts eventual consistency for customer master

**Options:**
- Option A: Synchronous SOAP services with immediate consistency
- Option B: Asynchronous events via SAP Event Mesh with eventual consistency
- Option C: Hybrid — synchronous for critical fields, asynchronous for others

**Evaluation:**
- Availability: Option B wins (no cascading failures)
- Complexity: Option A wins (simpler to understand)
- Consistency: Option A wins (immediate)
- Operational overhead: Option B wins (less coupling)

**Decision:** Option B. Chosen because availability and decoupling outweigh the complexity of eventual consistency.

**Consequences:**
- Positive: no cascading failures, downstream systems can be down without affecting MDG
- Negative: downstream systems may see stale data for up to 30 seconds; requires event mesh infrastructure

**Reversibility:** Moderately reversible. Would require changing consumer systems from event-driven to API-driven and updating MDG distribution logic.

**Why this is good:** Neutral question, multiple options, honest evaluation, clear consequences, reversibility assessed.

---

## Bad Example: "Why We Chose Microservices"

**Decision question:** "Why did we choose microservices for the SAP extension platform?"

**Options listed:**
- Microservices (chosen)
- Monolith (rejected because "not modern")

**Evaluation:**
- Microservices: "scalable, modern, cloud-native"
- Monolith: "legacy, not scalable"

**Consequences:**
- Positive: "future-proof, scalable"
- Negative: none listed

**Why this is bad:**
- Question is not neutral; it assumes microservices were chosen
- Only one real option evaluated; monolith is a straw man
- No honest cons or risks for the chosen option
- No negative consequences documented
- No reversibility assessment
- No review date

---

## Good Example: Custom Development vs Standard SAP Functionality

**Decision question:** "How should the regional discount matrix be supported in SAP SD?"

**Options:**
- Option A: Custom pricing calculation (requested by business unit)
- Option B: Standard condition technique with new condition type and scale base
- Option C: External pricing engine integration

**Evaluation:**
- Clean core compliance: Option B wins
- Implementation time: Option B wins
- Flexibility: Option A wins (can handle any logic)
- Maintainability: Option B wins (standard SAP support)

**Decision:** Option B. Chosen because it stays within clean core boundaries and reduces long-term maintenance risk. The business unit's flexibility need is addressed through more complex condition record maintenance.

**Consequences:**
- Positive: stays within clean core, standard SAP support, faster implementation
- Negative: more complex condition record maintenance; business unit needs training on condition technique

**Reversibility:** Easily reversible. Can switch to custom development later if condition technique proves insufficient.

**Why this is good:** The decision explicitly addresses a business request while maintaining architectural integrity. Negative consequences are honest and actionable.

---

## Bad Example: Cloud vs On-Premise Data Warehouse

**Decision question:** "Why is SAP Datasphere the best choice for our data warehouse replacement?"

**Options:**
- SAP Datasphere (chosen)
- Cloud data warehouse (rejected — "too generic")
- On-premise HANA upgrade (rejected — "not cloud")

**Evaluation:**
- SAP Datasphere: "preserves BW investments, cloud scalability, SAP integration"
- Cloud data warehouse: "would require redeveloping queries"
- On-premise HANA: "does not meet cloud strategy"

**Consequences:**
- Positive: "cloud scalability, preserves investments"
- Negative: none

**Why this is bad:**
- Question assumes SAP Datasphere is best
- Options are not evaluated at consistent detail
- No negative consequences (hybrid landscape complexity is a real downside)
- No reversibility assessment
- No exit cost evaluation for vendor lock-in
