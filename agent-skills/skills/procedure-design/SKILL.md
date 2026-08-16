---
name: procedure-design
description: Use when repeated operational work, support recovery, controlled execution, or agent-assisted work needs a stable runbook. Define trigger, preconditions, decision-sized steps, expected results, evidence, stop conditions, rollback, escalation, ownership, and completion criteria. Produces a Procedure Definition and Run Record Template. Do not use when the task still requires open-ended diagnosis.
---

# Procedure / Runbook Design

## Purpose

Turn repeated work into an executable and reviewable procedure without hiding expert judgment.

## Use when

- The same task or recovery action is performed repeatedly.
- Work depends too much on one person's memory.
- The task includes approvals, risk, rollback, escalation, or evidence requirements.
- A junior consultant or agent should execute part of the work under clear boundaries.

## Do not use when

- The failing layer is still unknown. Use `evidence-driven-troubleshooting` first.
- The task is a one-time decision with no expected reuse.

## Required inputs

- Purpose and observable success outcome.
- Trigger, frequency, scope, and exclusions.
- Preconditions, access, tools, and dependencies.
- Known risks and irreversible actions.
- Executor, approver, business owner, and escalation owner.
- At least one real or synthetic execution example.

## Workflow

1. Define observable success.
2. Define the trigger and explicit exclusions.
3. List preconditions, access, approvals, backups, and dependency state.
4. Split work into decision-sized steps.
5. Add input, expected result, and evidence to critical steps.
6. Add continue, retry, branch, stop, rollback, and escalation rules.
7. Put stop conditions before risky actions.
8. Define rollback and recovery, including what cannot be reversed.
9. Define executor, approver, business decision, and escalation ownership.
10. Define completion criteria including business validation or reconciliation.
11. Dry-run with someone who did not author the procedure.
12. Version the procedure and define review triggers.

## Decision rules

- A step without an observable expected result is too vague.
- A risky action without rollback or escalation is not operationally ready.
- If execution requires hidden expert judgment, write the decision rule or link another Skill.
- If a branch becomes diagnostic, call a troubleshooting Skill instead of expanding the runbook indefinitely.
- Keep the stable method in the procedure and case-specific values in the Run Record Template.

## Output format

Produce:

1. **Procedure Definition** — purpose, trigger, scope, preconditions, roles, ordered steps, decision rules, risk controls, rollback, escalation, completion criteria, and version history.
2. **Run Record Template** — one execution with inputs, actions, evidence, decisions, exceptions, and validation.

## Quality gates

- [ ] Trigger and exclusions are explicit.
- [ ] Every critical step has an expected result.
- [ ] Evidence requirements are named.
- [ ] Stop conditions appear before risky actions.
- [ ] Rollback is defined or explicitly impossible.
- [ ] Ownership is separated by role.
- [ ] Completion includes business validation.
- [ ] A second person can execute the procedure without undocumented memory.

## References

- `references/method.md` — Procedure design method and step contract.
- `references/templates.md` — Procedure Definition and Run Record templates.
- `references/examples.md` — Operational examples.

## Safety rules

- Do not automate or normalize unsafe actions by hiding approval requirements inside a procedure.
- Mark irreversible actions clearly.
- Do not place passwords, tokens, or secrets in the procedure.
- Require explicit human approval for high-impact production changes unless an approved control already exists.
