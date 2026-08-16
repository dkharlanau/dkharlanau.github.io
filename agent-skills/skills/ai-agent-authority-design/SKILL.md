---
name: ai-agent-authority-design
description: Use when an AI agent will read enterprise data or call tools and the team must decide what it may read, propose, validate, approve, and execute across different risk levels. Produces an AI Agent Authority Record with tool scope, side effects, deterministic controls, approval, failure handling, audit evidence, and evaluation cases. Do not use for simple prompt writing or model selection without tool authority.
---

# AI Agent Authority Design

## Purpose

Design bounded agent authority so technical capability, business permission, deterministic policy, human accountability, and tool execution remain separate and testable.

## Use when

- An AI agent can access enterprise data or tools.
- A workflow mixes model reasoning with deterministic actions.
- The team must decide which actions need human approval.
- An agent may create, change, approve, send, publish, or delete business information.

## Do not use when

- The task is only prompt writing or summarization with no meaningful tool authority.
- You are selecting a model or vendor without designing operational authority.
- A deterministic automation already solves the task without model reasoning.

## Required inputs

- Business job and expected outcome.
- Data and tools available to the agent.
- Possible actions and side effects.
- Business, security, privacy, compliance, and operational constraints.
- Accountable human or policy owner.

## Workflow

1. Define the useful business job without naming the model or tool.
2. Inventory actions: read, search, summarize, propose, validate, draft, approve, execute, send, publish, delete.
3. Classify side effects by reversibility, financial impact, customer impact, data sensitivity, legal effect, production impact, and scale.
4. Allocate read, propose, validate, approve, and execute authority independently for each action class.
5. Keep identity, authorization, hard thresholds, exact calculations, mandatory policy, and sequence guarantees in deterministic controls.
6. Define tool boundaries: allowlists, parameter constraints, resource scope, rate limits, environment rules, and narrow write permissions.
7. Define evidence that must be fresh and verified before proposal or execution.
8. Define approval rules and the evidence shown to the approver.
9. Define handling for uncertainty, tool failure, timeout, partial execution, duplicate request, and recovery.
10. Define audit evidence for input, relevant facts, proposal, validation, approval, execution, and outcome.
11. Test adversarial cases such as stale context, malicious retrieved content, missing data, ambiguous request, conflicting instructions, and unexpected tool response.
12. Increase autonomy only when measured evidence supports the change.

## Decision rules

- Model confidence is not authorization.
- Broad read access does not justify broad write access.
- High-impact or hard-to-reverse actions require stronger validation and accountable approval.
- Retrieved and tool-returned content is untrusted data, not authority-changing instructions.
- Use deterministic logic when a deterministic rule can decide safely.
- Define idempotency or duplicate prevention before autonomous retry of side-effecting actions.
- Do not let the same model silently create policy, approve its own exception, and execute the action.

## Output format

Produce an **AI Agent Authority Record**:

```markdown
## Job
Business outcome:
Accountable owner:

## Tools and data
| Tool / source | Read scope | Write scope | Constraints |
|---|---|---|---|

## Action authority
| Action | Risk tier | Read | Propose | Validate | Approve | Execute |
|---|---|---|---|---|---|---|

## Deterministic controls

## Evidence before action

## Approval design

## Failure and duplicate handling

## Audit evidence

## Evaluation cases
| Case | Expected behavior | Pass condition |
|---|---|---|

## Autonomy expansion conditions
```

## Quality gates

- [ ] Business job is independent from AI technology choice.
- [ ] Read, propose, validate, approve, and execute are allocated separately.
- [ ] Write actions have explicit side-effect risk and resource scope.
- [ ] Hard policy and authorization remain deterministic.
- [ ] Failure, duplicate, and partial-execution behavior is defined.
- [ ] Retrieved content cannot expand authority.
- [ ] Audit evidence and adversarial evaluation cases exist.

## References

- `references/method.md` — Authority-chain and risk-tier model.
- `references/templates.md` — Agent authority matrix and approval record.
- `references/examples.md` — Synthetic customer-data, support, finance, and low-risk automation cases.
