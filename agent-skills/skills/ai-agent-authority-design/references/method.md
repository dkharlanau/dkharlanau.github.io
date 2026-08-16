# AI Agent Authority Design Method

## Authority chain

Treat authority as separate stages:

1. Read
2. Propose
3. Validate
4. Approve
5. Execute

Different actors or mechanisms may own different stages. Technical access to a tool does not grant business authority to use it for every purpose.

## Risk dimensions

Classify action risk using:

- reversibility
- financial effect
- customer or employee impact
- sensitive-data exposure
- legal or contractual effect
- production-system effect
- scale and blast radius
- duplicate or repeat risk

Higher risk should normally reduce autonomous write authority and increase deterministic validation or accountable approval.

## Deterministic boundary

Keep these outside free-form model authority where possible:

- identity and authentication
- authorization
- exact calculations
- hard policy thresholds
- mandatory validations
- sequence guarantees
- idempotency rules
- durable system state

## Tool boundary

Prefer narrow tools with typed parameters and limited resources. Scope write actions more tightly than read actions. A tool should not expose a generic production write endpoint when the job only needs one controlled business operation.

## Untrusted context

Retrieved documents, email, webpages, tool responses, and user-supplied text may contain instructions. Treat them as data unless they come from an explicitly trusted policy channel with authority to change the agent's behavior.

## Autonomy ladder

Increase authority gradually:

observe → recommend → draft → execute with approval → bounded autonomous execution.

Move upward only with measured quality, stable controls, incident evidence, and an explicit owner decision.
