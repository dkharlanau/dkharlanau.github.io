---
name: control-design
description: Use when a business, data, integration, security, AI, or operational risk needs an explicit preventive, detective, corrective, or compensating control with ownership and evidence.
---

# Control Design

## Purpose
Design proportionate controls around meaningful enterprise risks.

## Use when
- A process or system change introduces material risk.
- A policy or business rule needs an enforceable control.
- A manual approval should be challenged or redesigned.

## Do not use when
- The task is only to document an existing control without evaluating it.
- The risk is too unclear to define an objective or evidence.

## Required inputs
- Risk event and business consequence.
- Existing process, system boundary, and authority model.
- Evidence sources, owners, thresholds, and known bypass paths.

## Workflow
1. State the risk and control objective.
2. Identify controllable causes or conditions.
3. Choose preventive, detective, corrective, or compensating control shape.
4. Select the earliest reliable enforcement or detection point.
5. Define trigger, evidence, owner, threshold, and response.
6. Test bypass and privileged paths.
7. Estimate false-positive and operating cost.
8. Define effectiveness metric and review cycle.

## Decision rules
- Do not add approval when a deterministic rule can safely enforce the same policy.
- One strong control at the right boundary is often better than duplicated weak controls.
- A control without evidence and response is only an intention.
- Compensating controls must state the residual risk they accept.

## Output format
Produce a **Control Design Record** with risk, objective, type, enforcement point, trigger, evidence, owner, response, bypass, test, residual risk, and effectiveness metric.

## Quality gates
- [ ] Risk and control objective are explicit.
- [ ] Control type is justified.
- [ ] Owner and evidence are defined.
- [ ] Bypass paths are tested.
- [ ] Operating cost and false positives are considered.
- [ ] Effectiveness can be measured.

## References
- `references/method.md`
- `references/templates.md`
- `references/examples.md`
