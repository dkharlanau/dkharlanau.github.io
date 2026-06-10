# Change Impact Analysis — Examples

## Good Example: New Payment Term in SAP

**Change:** Add new payment term Z030 for a specific customer segment.

**Direct consumers:**
- T052 (payment terms table)
- Credit limit calculation custom report
- Dunning procedure configuration
- Ariba integration (sends payment terms to suppliers)

**Risk assessment:**
- Custom report: High (uses payment term in credit calculation)
- Dunning procedure: Medium (may need new dunning level)
- Ariba integration: High (mapping table does not include Z030)

**Testing:**
- Unit: create a customer with Z030, verify it saves
- Integration: run Ariba sync, verify Z030 is mapped correctly
- Regression: run credit report, verify calculation is correct

**Rollback:**
- Delete payment term from T052
- Revert Ariba mapping if updated
- Revert dunning config if changed

**Result:** Go-live delayed until custom report and Ariba mapping are updated. Change approved after updates.

**Why this is good:** A "small" config change was found to affect three consumers. Testing and rollback were defined before approval.

---

## Bad Example: "Just a Small Config Change"

**Change:** "Add a mandatory reference field to sales order type ZOR."

**Bad analysis:**
- "It's just one field."
- No where-used search
- No interface check
- No process check

**Result after go-live:**
- E-commerce API fails (does not send the new field)
- EDI ORDERS interface fails (segment does not include the field)
- BW extractor fails (new field not in extract structure)
- 200 orders blocked in first 2 hours

**Why this is bad:**
- No where-used search on the field or order type
- No check of creation channels (GUI, API, EDI, batch)
- No interface consumer mapping
- No testing with realistic data
- No rollback plan

---

## Good Example: Background Job Schedule Change

**Change:** Move billing job earlier to avoid peak hours.

**Consumer mapping:**
- Direct: billing job
- Dependent: invoice print job (runs after billing)
- Dependent: IDoc generation job (runs after invoice print)
- Dependent: BW delta extraction (runs after billing completion)

**Risk assessment:**
- Invoice print job: Critical (would run on incomplete data)
- IDoc generation: High (would generate IDocs for incomplete invoices)
- BW extraction: Medium (would extract incomplete data)

**Testing:**
- Coordinate schedule change for all four jobs
- Test with full data set in QAS
- Verify sequence and timing

**Rollback:**
- Revert all four job schedules to previous times

**Result:** Change approved as coordinated schedule update for all four jobs.

**Why this is good:** The change to one job was found to affect three dependent jobs. The solution was a coordinated update, not an isolated change.

---

## Bad Example: Updating Business Partner Grouping

**Change:** Change business partner grouping for a customer category.

**Bad analysis:**
- "It's just a grouping change."
- No check of CVI synchronization
- No check of CRM replication filter
- No check of tax reporting interface

**Result:**
- CRM replication stops for affected customers (filter uses old grouping)
- Tax reporting interface fails (grouping used in tax classification)
- CVI synchronization creates duplicate business partners

**Why this is bad:**
- No where-used search on the grouping field
- No interface check
- No data consumer mapping
- No testing with representative data

**Good analysis:**
- Check CVI synchronization settings
- Check CRM replication filter criteria
- Check tax reporting interface mapping
- Test with customers in the affected category
- Update CRM filter before applying change
