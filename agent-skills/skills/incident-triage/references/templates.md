# Incident Triage — Templates

## Template 1: Incident Triage Record

```markdown
---
artifact: Incident Triage Record
id: TRI-001
date: YYYY-MM-DD
reporter: Name / Team
---

## Symptom
<!-- What was reported. Exact error text if available. -->

## System / Transaction
<!-- Where it happened -->

## Business impact
<!-- Critical / High / Medium / Low. Quantify if possible. -->

## Number affected
<!-- Users, records, orders, IDocs -->

## Recent changes (last 48h)
<!-- Transports, config, data loads, patches -->

## Technical domain
<!-- master data | config | code | integration | infrastructure | security | user error | unknown -->

## Containment action
<!-- What was stopped, paused, or worked around -->

## Owner assigned
<!-- Name and team. Specific question they must answer. -->

## Next update
<!-- When the reporter will hear back -->

## Related tickets
<!-- Links to similar or duplicate tickets -->
```

## Template 2: Owner Assignment Note

```markdown
---
artifact: Owner Assignment Note
id: OAN-001
date: YYYY-MM-DD
triage: TRI-001
---

## Assigned to
<!-- Name and team -->

## Specific question
<!-- The exact question they must answer -->

## Context provided
<!-- What the triage found and what is still unknown -->

## Expected response time
<!-- Based on impact classification -->

## Escalation path
<!-- Who to contact if the owner is unresponsive -->
```

## Template 3: Containment Log

```markdown
---
artifact: Containment Log
id: CL-001
date: YYYY-MM-DD
---

## Containment actions

| Time | Action | System | Expected Reversal | Owner |
|------|--------|--------|-------------------|-------|
| <time> | <action> | <system> | <condition> | <name> |

## Impact assessment
- Before containment: <description>
- After containment: <description>

## Risks of containment
<!-- What could go wrong because of the containment action -->
```

## Template 4: Triage Decision Checklist

```markdown
- [ ] Ticket read once without debugging
- [ ] Business impact classified (Critical/High/Medium/Low)
- [ ] Technical domain classified
- [ ] Recent changes checked (last 48h)
- [ ] Containment action taken or reason documented why none needed
- [ ] Owner assigned with specific question
- [ ] Reporter updated with next communication time
- [ ] Triage record documented
```
