# Interface Ownership — Detailed Method

## The Four-Role Ownership Method

Interface failures persist when ownership is unclear. This method assigns four distinct roles per interface and closes gaps before they become incidents.

### Step 1: Interface Discovery

Gather all interfaces from:
- Middleware logs and dashboards
- SAP transactions: WE02, SM58, BD87, SXI_MONITOR, AIF
- API gateway documentation
- File transfer logs
- Project documentation
- Team knowledge

Include:
- Active interfaces
- Dormant interfaces (may reactivate)
- Planned interfaces (ownership should be assigned before go-live)

### Step 2: Interface Classification

For each interface, document:
- **Type:** API, IDoc, RFC, file transfer, event
- **Direction:** inbound, outbound, bidirectional
- **Criticality:** critical, major, minor, dormant
- **Source system:** where data originates
- **Target system:** where data is consumed
- **Middleware:** any intermediary systems

Criticality criteria:
- **Critical:** revenue-impacting, real-time, no workaround
- **Major:** business process affected, workaround exists but is costly
- **Minor:** reporting lag, non-urgent, easy workaround
- **Dormant:** no current consumer, kept for historical reference

### Step 3: Four-Role Assignment

For each interface, assign four roles:

1. **Business owner**
   - Approves schema or format changes
   - Validates data semantics
   - Decides deprecation
   - Accountable for business impact of failures

2. **Technical owner**
   - Designs and maintains the interface
   - Approves implementation changes
   - Accountable for technical quality

3. **Operational owner**
   - Monitors the interface
   - Responds to alerts
   - Performs first-line diagnosis
   - Accountable for MTTR

4. **Consumer representative**
   - Speaks for downstream consumers
   - Validates compatibility of changes
   - Reports consumer-side failures
   - Accountable for consumer readiness

If a role is missing, flag it as a gap. If a role is filled by a distribution list or generic team name, flag it as "weak ownership."

### Step 4: Ownership Matrix Documentation

Record in a structured matrix:
- Interface ID
- Source and target systems
- Direction and type
- Criticality
- All four owners (named individuals)
- SLA
- Status

### Step 5: Gap Identification and Resolution

For each gap:
- **Missing business owner:** assign from the source data domain
- **Missing technical owner:** assign from the integration or development team
- **Missing operational owner:** default to AMS or integration operations
- **Missing consumer representative:** designate for external or cross-business-unit consumers
- **Disputed ownership:** escalate to architecture or governance board
- **Critical and unowned:** treat as P1 risk, assign interim owner within 24 hours

### Step 6: Change Process Definition

Document how ownership is updated:
- When systems change
- When teams reorganize
- When projects end
- When owners leave the organization

Require:
- Update within 48 hours of owner change
- Notification to all stakeholders
- Review of SLA implications

### Step 7: Incident Drill Validation

Simulate a failure for a critical interface:
1. Trigger a test alert
2. Verify the operational owner receives it
3. Verify the operational owner knows who to contact
4. Verify the business owner can make decisions
5. Verify the technical owner can diagnose
6. Verify the consumer representative is notified

If any step fails, update the matrix or runbook.

## Common Ownership Pitfalls

1. **Assigning only a technical owner.** Schema changes are approved by developers who do not understand business semantics.
2. **Creating the matrix once and never updating it.** Owners leave, teams reorganize, and the matrix becomes fiction.
3. **Assuming the vendor owns everything.** Internal accountability is missing; the vendor is blamed for internal decisions.
4. **No escalation path when the owner is unresponsive.** Incidents stall because the primary owner is on vacation.
5. **Storing the matrix in a personal file.** The people who need it during an incident cannot find it.
