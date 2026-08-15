# TRIZ for Digital Systems — Practice Template Pack

Use these templates in workshops, design reviews, incidents, change requests, architecture discussions and AI use-case reviews. Start with evidence. Keep facts separate from assumptions. Do not choose technology before the contradiction and boundary are clear.

---

## T01 — Problem Framing Card

**Use when:** the requirement is vague, several teams describe the problem differently, or the discussion starts from a preferred solution.

```text
Problem / topic:

Observed behavior:
- What happens now?
- Give 1–3 concrete examples.

Useful function:
- What useful outcome must remain?

Actors:
- Who needs the outcome?
- Who owns the result?

Business object:
- Which object changes state?

Business impact:
- Delay / cost / quality / risk / revenue / compliance / manual effort

Evidence already available:
- Process data:
- Transactions / documents:
- Logs / traces:
- User observations:

Boundary:
- Inside:
- Outside:

Known constraints:
- Policy:
- Authorization:
- Timing:
- Integration:
- Data / legal:

Facts:
-

Assumptions:
-

Unknowns to verify:
-
```

---

## T02 — Contradiction Canvas

**Use when:** improving one useful property makes another useful property worse.

```text
Useful property A to improve:

Why A matters:

Useful property B to preserve:

Why B matters:

Contradiction:
If we improve ____________________, then ____________________ becomes worse.
We still need both because ____________________.

Physical form, if useful:
The same element / step should ____________________ when ____________________,
and should not ____________________ when ____________________.

Separation test:
[ ] Time — must both properties be active at the same moment?
[ ] Condition — does every case need the same behavior?
[ ] Context — which part is common and which is local/contextual?
[ ] System level — are we solving the problem at the wrong level?
[ ] Authority — can read / propose / validate / approve / execute be separated?
[ ] Representation — does every consumer need the same raw data or full object?

Selected operator(s):

What changes in the design space after separation?
-
```

---

## T03 — Business Process Redesign Canvas

**Use when:** approvals, queues, handoffs, exceptions or rework make a process slow or fragile.

```text
Process / scope:

Useful end-to-end outcome:

Business object(s):

Current path:
1.
2.
3.

For each step, ask:
- What useful function does this step protect?
- What input does it need?
- What state changes?
- Who owns the decision?
- What is the wait time?
- What exception can occur?

Waiting points:
-

Handoffs:
-

Rework loops:
-

Controls that must remain independent:
-

Normal cases:
-

Exception / high-risk cases:
-

Can we move earlier?
- Validation:
- Evidence collection:
- Classification:

Can we remove?
- Step:
- Copy:
- Approval:
- Queue:
- Sync dependency:

Target shape A — remove / simplify:

Target shape B — deterministic redesign:

Target shape C — uncertainty-assisted, only if useful:

Primary metric:

Counter-metric:

Small reversible experiment:
```

---

## T04 — Integration Decision Template

**Use when:** choosing API, event, queue, file, batch or synchronous/asynchronous behavior.

```text
Integration purpose:

Producer:

Consumer(s):

Business object / message:

Interaction type:
[ ] Command
[ ] Query
[ ] Notification / event
[ ] Bulk transfer

Trigger:

Does the caller need immediate business confirmation?

System of record / durable state owner:

Freshness needed for the real business decision:

Consistency requirement:

Can producer continue when consumer is unavailable?

Expected volume / peaks:

Ordering requirement:

Replay requirement:

Duplicate delivery strategy:

Idempotency key / rule:

Retry rule:

Dead-letter / recovery rule:

Does the consumer need raw data or a purpose-specific projection?

Security / authorization boundary:

Observability:
- Correlation ID:
- Business key:
- Success signal:
- Failure signal:
- Owner of recovery:

Candidate shape A — simpler boundary:

Candidate shape B — deterministic integration:

Candidate shape C — AI-assisted interpretation, only if uncertainty exists:

Decision and reason:
```

---

## T05 — SAP Change and Extension Template

**Use when:** a change request may require configuration, extension or custom development.

```text
Business request:

Missing useful outcome:

Current SAP behavior:

Affected process:

Affected business object(s):

Affected lifecycle event(s):

Standard configuration available?
- Option:
- Limitation:

Is the variation:
[ ] Stable enterprise policy
[ ] Local/contextual rule
[ ] Customer-specific behavior
[ ] Integration concern
[ ] UI concern
[ ] Analytical concern

Candidate 1 — standard configuration:

Candidate 2 — in-app / key-user extension:

Candidate 3 — developer extension:

Candidate 4 — side-by-side extension:

Why is custom behavior needed, if at all?

Data boundary:

Authorization boundary:

Upgrade / clean-core impact:

Operational owner:

Reversibility / fallback:

Regression areas:

Primary success metric:

Counter-metric on the standard process:

Decision:
```

---

## T06 — AI Use-Case Boundary Template

**Use when:** AI, RAG, copilots or agents are proposed inside a business or technical process.

```text
Business outcome:

Current manual or deterministic process:

What is genuinely uncertain or interpretive?
-

What must remain deterministic?
- Exact rules:
- Mandatory thresholds:
- Authorization:
- Durable state:
- Sequence / idempotency:

AI responsibility:
[ ] Classify
[ ] Extract
[ ] Summarize
[ ] Search / retrieve
[ ] Generate candidates
[ ] Investigate adaptively
[ ] Other:

Authority chain:
READ
- What can the model or agent inspect?

PROPOSE
- What may it prepare or recommend?

VALIDATE
- Which deterministic checks run before action?

APPROVE
- Which policy or accountable role approves material action?

EXECUTE
- What narrow, auditable action can be performed?

Risk tier:
[ ] R0 advisory
[ ] R1 low-impact reversible
[ ] R2 business-significant
[ ] R3 high-impact / difficult to reverse

Tool allowlist:
-

Agent budgets:
- Max tool calls:
- Max time:
- Cost limit:
- Stop conditions:

Evidence shown with output:

Fallback when confidence/evidence is weak:

Evaluation:
- Task success:
- Wrong action / rework:
- Unsafe attempt rate:
- Latency:
- Cost:
- Human escalation:
```

---

## T07 — Incident to Systemic Problem Template

**Use when:** incidents repeat or recovery restores service but not the underlying mechanism.

```text
Incident / pattern:

Business impact:

Useful function that failed:

Timeline:
1.
2.
3.

Expected state:

Observed state:

First observable deviation:

Evidence:
- Logs:
- Traces:
- Business documents:
- Process events:
- User actions:

Negative signals already available:
- Errors:
- Retries:
- Rejects:
- Delays:
- Overrides:

Recovery action used:

Did recovery fix the cause or only the symptom?

Where was state or ownership unclear?

Which boundary made diagnosis difficult?

What could make this failure visible earlier?

Option A — remove failure mechanism:

Option B — deterministic prevention / recovery:

Option C — AI-assisted diagnosis, only if useful:

Preventive experiment:

New observable signals required:
```

---

## T08 — Contradiction-Driven ADR

**Use when:** an architecture choice has several plausible system shapes and long-term consequences.

```text
# ADR: <decision title>

Status: proposed / accepted / superseded
Date:
Owners:

## Context
Observed behavior:
Useful function:
Constraints:
Evidence:

## Contradiction
Improve:
Preserve:
Statement:
Selected separation operator(s):

## Options
### A — Remove / simplify
Shape:
Benefits:
Complexity tax:
Risks:

### B — Deterministic redesign
Shape:
Benefits:
Complexity tax:
Risks:

### C — Uncertainty-assisted
Only include if uncertainty creates value.
Shape:
Benefits:
Complexity tax:
Risks:

## Decision
Chosen option:
Why:

## Consequences
Positive:
Negative:
Operational ownership:
Security / authority impact:

## Assumptions
-

## Review triggers
- Volume changes to:
- Latency changes to:
- Failure rate changes to:
- Business policy changes:
- New platform capability:

## Evidence after implementation
Primary metric:
Counter-metric:
```

---

## T09 — Data and Master Data Governance Template

**Use when:** data quality, duplicates, ownership, global/local variation or distribution cause process problems.

```text
Data object:

Business decisions that depend on it:
-

Semantic owner:

Operational data steward:

Consumers:
-

Authority chain:
CREATE / PROPOSE:
VALIDATE:
APPROVE:
PUBLISH:
CORRECT:

Global attributes:
-

Contextual / local attributes:
-

Exact quality rules:
-

Judgment-based quality decisions:
-

Duplicate detection point:

Golden / authoritative state owner:

Consumer-specific representations:
-

Distribution mechanism:

Reconciliation mechanism:

Primary quality metric:

Counter-metric such as request lead time:

Known workaround risk:

Experiment / rollout slice:
```

---

## T10 — Reversible Experiment Template

**Use when:** the preferred design is plausible but evidence is not strong enough for a broad rollout.

```text
Hypothesis:
If we change ____________________, then ____________________ improves without unacceptable damage to ____________________.

Baseline:

Change under test:

Smallest reversible scope:
[ ] Shadow
[ ] Replay
[ ] One process variant
[ ] One country / company code / sales area
[ ] One interface
[ ] One user group
[ ] One low-risk action class
[ ] Other:

Primary metric:

Counter-metric:

Success threshold:

Failure / stop condition:

Rollback or recovery path:

Observation period:

Evidence to collect:
-

Decision after experiment:
[ ] Adopt
[ ] Adjust and retest
[ ] Reject
[ ] Need more evidence

New contradiction discovered:
```
