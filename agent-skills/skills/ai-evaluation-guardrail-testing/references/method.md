# Method

Use the evaluation as a controlled experiment around a business task.

## 1. Task contract
Record the business outcome, input, output, allowed tools, forbidden actions, required approvals, and hard rules. The evaluation is weak if the target behaviour is vague.

## 2. Test dimensions
Cover at least:
- normal task completion;
- ambiguous or incomplete input;
- conflicting evidence;
- malformed or malicious instructions;
- authorization boundary attempts;
- tool error, timeout, or unavailable dependency;
- duplicate or repeated request;
- stale context;
- recovery and escalation;
- regression after a fix.

## 3. Evidence
Capture the model result and the operational path: tool calls, parameters, approvals, validation errors, retries, side effects, and final business state.

## 4. Failure severity
Treat failures differently. A weak summary is not the same as an unauthorized financial action. Suggested classes:
- critical: unauthorized or harmful side effect, data corruption, approval bypass;
- high: wrong business decision or repeatable incorrect action;
- medium: incomplete reasoning, missed constraint, poor escalation;
- low: wording or presentation issue without business impact.

## 5. Guardrails
Hard rules should not rely only on probabilistic model behaviour. Where practical, use deterministic authorization, validation, schema, threshold, idempotency, approval, and tool allow-list controls.

## 6. Release decision
Use three outcomes:
- release: thresholds met and critical controls passed;
- limited pilot: useful but constrained by explicit authority, scope, monitoring, or human review;
- hold: critical failures or insufficient evidence remain.
