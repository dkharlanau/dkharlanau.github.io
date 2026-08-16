---
name: ai-evaluation-guardrail-testing
description: Use this skill when an AI assistant or agent, prompt, model, tool workflow, or authority boundary must be evaluated before release or after change. Test task quality, guardrails, tool use, failure handling, unsafe authority, retries, and regression, then produce an evidence-based release decision.
---

# AI Evaluation & Guardrail Testing

## Purpose
Evaluate an AI-assisted workflow as an operational system, not as a demo. Test whether it completes the business task, stays within its authority, uses tools safely, fails correctly, and remains stable after changes.

## Use when
- Introducing an AI assistant or agent into a business process.
- Changing a model, prompt, tool, workflow, or authority level.
- The AI can read or change enterprise data.
- Preparing a pilot, release, or controlled rollout.
- Building regression tests after defects or workflow improvements.

## Do not use when
- The task is only general AI output review with no operational workflow or tools.
- The main problem is designing authority boundaries from scratch; use `ai-agent-authority-design` first.
- A production incident already exists and immediate triage is required.

## Required inputs
- Business task and expected outcome.
- AI workflow or agent definition.
- Allowed and prohibited actions.
- Tool list and authority boundaries.
- Representative normal and edge-case inputs.
- Existing controls, approval gates, schemas, or policies.

## Workflow
1. Define the task contract: inputs, business result, outputs, tools, constraints, and prohibited decisions.
2. Separate authority levels: read, propose, validate, approve, execute.
3. Build evaluation cases covering happy path, ambiguous input, missing data, conflicting evidence, malicious instruction, tool error, duplicate request, and retry.
4. Write expected behaviour before running each case.
5. Execute cases and capture output, tool calls, warnings, refusals, latency, and business result.
6. Classify failures: factual error, missed constraint, unsafe action, tool misuse, hidden assumption, escalation failure, duplicate side effect, or instability.
7. Test deterministic guardrails such as authorization, schema validation, approval gates, idempotency, allow-lists, thresholds, and stop conditions.
8. Set release thresholds. Treat critical authority or integrity failures as blockers regardless of average score.
9. Apply fixes and rerun the regression set.
10. Produce release, limited pilot, or hold decision with limits, monitoring, and ownership.

## Decision rules
- Do not approve production use from happy-path success alone.
- A model's ability to call a tool does not grant business authority to execute the action.
- Critical unauthorized action, data corruption, duplicate side effect, or bypassed approval is a release blocker.
- Write expected behaviour before observing model output to reduce evaluation drift.
- Keep failed cases in the regression set after they are fixed.
- Prefer deterministic enforcement for hard business rules, authorization, mandatory thresholds, idempotency, and schema constraints.

## Output format
Produce an **AI Evaluation & Guardrail Test Record** containing:
- workflow and business task;
- authority boundary and prohibited actions;
- evaluation case list;
- expected versus observed behaviour;
- tool-call evidence;
- failure classification and severity;
- guardrail result;
- regression result;
- release decision;
- known limits, monitoring, and owner.

## Quality gates
- Expected behaviour exists for each scored case.
- Edge, ambiguity, tool-failure, retry, and authority-boundary cases are included.
- Critical failures are separated from average task-quality metrics.
- Tool side effects and duplicate risk are validated.
- Regression covers previously fixed failures.
- Final decision states residual limits and production monitoring.

## References
- `references/method.md`
- `references/templates.md`
- `references/examples.md`
