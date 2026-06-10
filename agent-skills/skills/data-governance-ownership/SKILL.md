---
name: data-governance-ownership
description: Use when data ownership is unclear, data rules are unenforced, multiple systems claim the same source of truth, or a governance gap is blocking a project, audit, or integration. Do not use for technical data quality root cause analysis of a specific defect.
---

# Data Governance Ownership

## Purpose

Diagnose missing data ownership, undefined rules, and unenforced policies. Produce a governance action plan with named owners, decision rights, and enforcement mechanisms.

## Use when

- A data quality initiative has stalled because no one can agree who fixes bad data.
- A new system is being integrated and there is no agreed data ownership model between source and target.
- Master data changes require three emails and two meetings to approve.
- Reports from different systems show different values for the same metric and no one owns the reconciliation.
- An audit or compliance review requires documented data ownership, retention rules, or access policies.
- You are preparing for AI or automation and need to know which data is trustworthy and who vouches for it.

## Do not use when

- You are investigating a single data defect and need to trace its root cause (use `data-quality-root-cause` instead).
- The problem is purely technical (database performance, storage capacity) with no ownership or policy dimension.
- You need a data privacy or security architecture assessment.

## Required inputs

- List of data domains or data elements in scope.
- System inventory showing which systems create, modify, and consume each data domain.
- Organizational chart or contact list for business and technical stakeholders.
- Existing policies, standards, or guidelines (even if outdated or ignored).
- Recent data quality incident log or ticket history (optional but valuable).
- Compliance or audit requirements that apply to the data (optional).

## Workflow

1. **Scope the data domain.** List the data elements, tables, or objects in scope. Do not try to govern everything at once. Pick one domain with visible pain.
2. **Map the system landscape.** For each data element, identify: source system, consuming systems, transformation points, and the system of record.
3. **Identify stakeholders.** For each data element, name: business owner (accountable for quality), technical owner (accountable for systems), data steward (day-to-day caretaker), and consumer representatives.
4. **Surface ownership gaps.** Flag data elements with missing owners, conflicting owners, or owners who lack authority. Document each gap with business risk.
5. **Catalog existing rules.** Collect policies, standards, validation rules, and access controls. Note which are enforced technically, which are enforced by process, and which exist only on paper.
6. **Identify enforcement gaps.** For each rule, ask: where is this checked? What happens when it fails? Who is notified? If any answer is missing, the rule is unenforced.
7. **Define decision rights.** For each data domain, document who can: create, update, delete, approve changes, approve access, and define rules.
8. **Produce the governance action plan.** Combine ownership matrix, rule catalog, enforcement gaps, and decision rights into a single document with priorities and owners.
9. **Validate with stakeholders.** Walk through the plan with named owners. Confirm they accept the role and the authority. Adjust if they refuse.
10. **Set review cycle.** Define how often ownership, rules, and enforcement are reviewed. Assign a review owner.

## Decision rules

- If ownership is unclear, produce an ownership matrix before proposing automation.
- If a rule exists only in a policy document and is not enforced technically, classify it as "process-dependent" and flag the risk.
- If two systems both claim to be the source of truth for the same data element, escalate to architecture; do not guess.
- If a data steward is named but lacks system access or decision authority, the ownership is ceremonial; surface the gap.
- If a compliance requirement has no technical enforcement, treat it as a high-priority gap regardless of current incident count.
- If a data element has no consumers, question whether it should be governed at all; governance has a cost.
- If a rule is enforced in one system but not in another that receives the same data, the rule is porous; document the bypass.

## Output format

Produce three artifacts:

**1. Data Ownership Matrix**

```markdown
| Data Element | System of Record | Business Owner | Technical Owner | Data Steward | Consumers | Ownership Gap |
|--------------|------------------|----------------|-----------------|--------------|-----------|---------------|
| Customer.TaxNumber1 | SAP BP | <name> | <name> | <name or VACANT> | CRM, BW | <gap description or NONE> |
```

**2. Rule Catalog**

```markdown
| Rule | Applies To | Enforcement Point | Failure Action | Review Frequency | Gap |
|------|------------|-------------------|--------------|------------------|-----|
| <rule name> | <data element> | <system/transaction> | <what happens on failure> | <frequency> | <gap or NONE> |
```

**3. Governance Action Plan**

```markdown
## Priority actions
| Priority | Action | Owner | Due Date | Success Criteria | Risk if not done |
|----------|--------|-------|----------|------------------|------------------|
| P1 | <action> | <name> | <date> | <criteria> | <risk> |

## Decision rights charter
| Data Domain | Create | Update | Delete | Approve Changes | Approve Access | Define Rules |
|-------------|--------|--------|--------|-----------------|----------------|--------------|
| <domain> | <who> | <who> | <who> | <who> | <who> | <who> |

## Review cycle
- Frequency: <quarterly / semi-annual / annual>
- Review owner: <name>
- Next review: <date>
```

## Quality gates

- [ ] Every data element in scope has a named business owner and technical owner.
- [ ] Every owner has been asked and has not refused the role.
- [ ] Every rule has a documented enforcement point and failure action.
- [ ] Every enforcement gap has a business risk statement and a proposed closure action.
- [ ] Decision rights are documented and validated with at least one stakeholder per domain.
- [ ] The governance action plan has priorities, owners, and deadlines.
- [ ] No automation or tool purchase is proposed before ownership is clear.

## References

- `references/method.md` — Detailed stakeholder mapping, ownership gap analysis, and decision rights definition.
- `references/templates.md` — Copy-ready templates for Ownership Matrix, Rule Catalog, and Governance Action Plan.
- `references/examples.md` — Good and bad examples from post-merger, SAP MDG, and multi-system reconciliation contexts.

## Safety rules

- Separate facts from assumptions. Label every proposed owner as "confirmed" or "proposed."
- Separate decisions from open questions. List open questions explicitly.
- Do not expose client names, internal org charts, or proprietary system details.
- Do not copy proprietary framework text. Use your own words.
