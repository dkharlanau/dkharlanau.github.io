---
name: non-functional-requirements
description: Use when vague quality expectations such as fast, secure, resilient, scalable, or supportable must become measurable and testable architecture requirements.
---

# Non-Functional Requirements

## Purpose
Translate quality expectations into measurable, testable, owned requirements.

## Use when
- Designing or reviewing an enterprise solution.
- Preparing architecture options or release criteria.
- Quality attributes are described with vague adjectives.

## Do not use when
- The request is only for functional process behavior.
- A current incident requires immediate containment rather than requirement design.

## Required inputs
- Business outcome and impact of failure.
- Workload, users, data volume, geography, time windows, and dependencies where known.
- Existing service levels, policies, and operational evidence.

## Workflow
1. Identify business-critical quality attributes.
2. Define scenarios and operating conditions.
3. Add metric, target, tolerance, and measurement point.
4. Cover normal, peak, degraded, and recovery conditions where relevant.
5. Define assumptions and dependency conditions.
6. Assign verification method and owner.
7. Link each NFR to architecture decisions, tests, monitoring, and release gates.
8. Record conflicts between quality attributes.

## Decision rules
- Avoid adjectives without a metric and context.
- Measure at the boundary that represents the business outcome.
- Separate end-to-end targets from component targets.
- Do not promise availability or recovery beyond dependency capabilities without an explicit mitigation.

## Output format
Produce a **Non-Functional Requirement Set** with scenario, quality attribute, metric, target, tolerance, measurement point, conditions, dependencies, verification, owner, and trade-offs.

## Quality gates
- [ ] Every NFR is measurable or explicitly exploratory.
- [ ] Measurement point is defined.
- [ ] Workload or operating context is included.
- [ ] Verification and owner are present.
- [ ] Conflicting attributes are visible.

## References
- `references/method.md`
- `references/templates.md`
- `references/examples.md`
