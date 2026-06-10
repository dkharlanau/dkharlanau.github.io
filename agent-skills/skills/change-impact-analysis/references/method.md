# Change Impact Analysis — Detailed Method

## The Consumer-First Method

The core of this skill is predicting what will break, slow down, or behave differently after a change. It maps all consumers of the changed object before the change is approved.

### Step 1: Change Boundary Definition

Document exactly what is changing:
- Object name, table, field, transaction, program, or configuration path
- Current value
- Proposed value
- System where the change will be applied
- Intended outcome

If the change description is vague ("update the sales config"), demand precision before proceeding.

### Step 2: Direct Consumer Mapping

Use where-used search, cross-reference tools, or SE11/SE16 to find all programs, classes, reports, and transactions that reference the object.

Check:
- ABAP programs and classes
- Reports and queries
- User exits and enhancements
- Custom code
- Standard transactions that use the object

### Step 3: Interface Consumer Mapping

Check all interfaces that send or receive the object:
- IDoc segments
- RFC function modules
- API schemas
- File formats
- Event payloads

Review:
- Segment structures
- API schemas
- Mapping tables
- Field mappings

### Step 4: Process Consumer Mapping

Identify business process steps that use the object:
- Order-to-cash steps
- Procure-to-pay steps
- Record-to-report steps
- Warehouse operations

Check process documentation or interview the process owner.

### Step 5: Data Consumer Mapping

Check analytics and reporting systems:
- BW extractors
- Reporting tables
- Data warehouse loads
- Analytics tools
- Dashboards

### Step 6: Authorization Impact Check

If the change affects transactions or data access:
- Check roles and profiles that grant access (SUIM)
- Identify users who will see changed behavior
- Test with at least one user from each affected role

### Step 7: Risk Assessment

For each affected component, rate the risk:
- **Low:** no change needed, monitor only
- **Medium:** minor adjustment or monitoring needed
- **High:** breaks without update
- **Critical:** revenue-impacting failure

Document the risk rating and the required action for each component.

### Step 8: Testing Scope Definition

Define what must be tested:
- Unit test: does the changed object behave correctly in isolation?
- Integration test: do all consumers still work?
- Regression test: does existing behavior remain unchanged?
- User acceptance test: do business users accept the new behavior?

Name the tester and define test data requirements for each test.

### Step 9: Rollback Plan Definition

Define how to reverse the change:
- Transport reversal
- Configuration rollback
- Data restore
- Emergency procedure

Validate that the rollback is technically feasible before approving the change.

### Step 10: Approval

The assessment must be reviewed by:
- Functional owner
- Integration lead
- Change manager

No change should be approved without a reviewed Change Impact Assessment.

## Common Impact Analysis Pitfalls

1. **Assuming a change is "small" without checking where-used.** A single config field can break three interfaces and a custom report.
2. **Checking only the primary system and ignoring connected systems.** The change works in SAP but fails in CRM, BW, or the data warehouse.
3. **Not testing with realistic data.** The change works in QAS with simple test data but fails in PRD with complex real-world records.
4. **Omitting the rollback plan.** When the change fails, the team improvises a reversal under pressure.
5. **Not involving the integration team early.** Interface impacts are discovered after go-live.
