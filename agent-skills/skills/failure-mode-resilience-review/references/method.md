# Method

Use a business-capability view first, then move down to technical failure modes.

## Failure-mode structure
For each important dependency or boundary, record:
1. failure condition;
2. business effect;
3. technical and data effect;
4. detection signal;
5. containment;
6. recovery;
7. stop condition;
8. validation test.

## Review lenses
- availability: dependency does not respond;
- latency: dependency responds too late;
- integrity: partial, duplicate, or contradictory state;
- ordering: messages or steps arrive out of sequence;
- capacity: backlog, burst, or sustained load;
- identity: authentication or authorization changes;
- configuration: environment state changes behaviour;
- recovery: human or automated restoration fails.

## Detection
A useful signal must distinguish a real failure from expected delay. Prefer business outcome signals as well as technical signals. A green service metric does not prove that documents, messages, or data reached the intended end state.

## Recovery
State whether recovery is retry, replay, resume, compensate, reconcile, fallback, or manual. Define preconditions and side-effect risk before automating it.

## Prioritization
Prioritize modes with high business impact, weak detection, difficult recovery, or broad cascade potential. A simple qualitative rating is enough when quantitative reliability data is not available.
