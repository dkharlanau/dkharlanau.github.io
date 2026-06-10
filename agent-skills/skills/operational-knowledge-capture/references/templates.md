# Operational Knowledge Capture — Templates

## Template 1: Operational Knowledge Capture Note

```markdown
---
artifact: Operational Knowledge Capture Note
id: OKC-001
date: YYYY-MM-DD
author: Name
topic: Incident | Procedure | Workaround | Decision
---

## Situation
<!-- What was happening. Context, urgency, systems involved. -->

## Symptom
<!-- Exact error, behavior, or observation -->

## What was done
<!-- Step by step. Commands, transactions, settings. -->

## Why it worked
<!-- Causal explanation, not just description -->

## What was tried and failed
<!-- Dead ends, wrong paths, false assumptions -->

## What almost went wrong
<!-- Near misses or risks that were avoided -->

## Preconditions
<!-- When this knowledge applies and when it does not -->

## Limitations
<!-- What this procedure does not cover -->

## Verification
<!-- How to confirm the procedure is still valid -->

## Owner
<!-- Who maintains this knowledge -->

## Review date
<!-- When this note should be revalidated -->

## Related knowledge
<!-- Links to other capture notes, runbooks, tickets -->
```

## Template 2: Runbook Update

```markdown
---
artifact: Runbook Update
id: RBU-001
date: YYYY-MM-DD
source: OKC-001
---

## Runbook
<!-- Name and location of the updated runbook -->

## Changes made
<!-- What was added, modified, or removed -->

## Reason for update
<!-- Why the runbook needed updating -->

## Verification
<!-- How to confirm the updated runbook is correct -->

## Owner
<!-- Who maintains the runbook -->

## Review date
<!-- When the runbook should be revalidated -->
```

## Template 3: Stakeholder Notification

```markdown
---
artifact: Stakeholder Notification
id: SN-001
date: YYYY-MM-DD
source: OKC-001
---

## To
<!-- Stakeholder name and team -->

## Subject
<!-- Brief subject line -->

## Summary
<!-- What was captured and why it matters to this stakeholder -->

## Action required
<!-- What the stakeholder needs to do, if anything -->

## Link
<!-- Link to the capture note or runbook -->
```

## Template 4: Knowledge Discovery Checklist

```markdown
- [ ] Note written within 24 hours of resolution
- [ ] Symptom described with exact error text and transaction
- [ ] Resolution steps include exact transaction codes or program names
- [ ] Causal explanation is present and distinct from step description
- [ ] At least one failed attempt documented
- [ ] Preconditions and limitations stated
- [ ] Verification method defined
- [ ] Owner named and review date set
- [ ] Note stored in discoverable location with tags
- [ ] Related knowledge linked
```
