# Data Architecture Selection — Templates

## 1. Discovery snapshot

```markdown
# Data Architecture Discovery
Decision owner / date:
Consumer / action:
Example question:
Wrong-answer consequence:
Known sources and system of record:
Business keys and relationships:
Data formats / volume / growth:
Refresh SLA / load cadence:
History and deletion requirements:
Security / residency:
Reporting and AI consumer needs:
Operating owner and skills:
Budget / deadline:
Facts with evidence:
Assumptions:
Open questions (owner / due date):
```

## 2. Option comparison

```markdown
| Criterion | Baseline | Option A | Option B | Evidence / unknown |
|---|---|---|---|---|
| Correctness and history | | | | |
| Freshness and latency | | | | |
| Consumer usability | | | | |
| Security and lineage | | | | |
| Failure recovery | | | | |
| Delivery and operations | | | | |
| Total cost and portability | | | | |
```

Never fabricate numerical scores or cost savings.

## 3. Architecture Decision Record

```markdown
# ADR: [Neutral decision question]
Status: proposed
Owner:
Date:
Business job:
Required behavior:
Alternatives:
- Current state:
- Option A:
- Option B:
Recommendation and why:
Consequences and accepted disadvantages:
Evidence / unknowns:
Pilot:
Validation / rollback:
Security and governance approvals:
Review trigger:
```

## 4. Proof-of-value checks

```markdown
| Test | Input / disruption | Expected evidence | Owner | Pass? |
|---|---|---|---|---|
| Source-to-target reconciliation | Known day | Counts + amounts + exceptions | | |
| Upsert / delete | Change one test record | Target matches approved semantics | | |
| Failure + replay | Stop pipeline halfway | No loss or double counting | | |
| Historical query | Changed customer attribute | Report matches as-of date | | |
| Access denial | Restricted persona | No unauthorized data returned | | |
| Freshness | Peak load period | P95 latency within SLA | | |
```
