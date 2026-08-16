---
name: failure-mode-resilience-review
description: Use this skill when a service, interface, workflow, data pipeline, batch process, or AI agent needs a structured resilience review. Identify realistic failure modes, business effects, detection, containment, recovery, stop conditions, and evidence-based resilience tests before release.
---

# Failure Mode / Resilience Review

## Purpose
Identify how an enterprise capability can fail, how the failure affects business and data, how it is detected and contained, and how recovery is tested.

## Use when
- Reviewing a new or changed service, interface, workflow, data pipeline, batch process, or AI agent.
- Preparing a major release, migration, cutover, or architecture decision.
- A recurring incident exposes weak detection or recovery.
- External or asynchronous dependencies create uncertainty.
- Monitoring, retry, fallback, or manual recovery design is required.

## Do not use when
- A specific production incident already needs immediate diagnosis; use troubleshooting or flow-trace skills.
- The only goal is dependency discovery; use `service-dependency-mapping` first.
- A full quantitative reliability model is required and the necessary operational data is unavailable.

## Required inputs
- Business capability and critical outcome.
- Architecture or process scope.
- Known dependencies and interfaces.
- Existing monitoring, retries, fallback, and recovery procedures.
- Known incident history where available.
- Risk or release context.

## Workflow
1. Define the business capability and critical outcome that must survive failure.
2. Map relevant dependencies: systems, APIs, queues, data, identity, configuration, schedules, people, and external services.
3. List realistic failure modes for each dependency and boundary.
4. Describe business, technical, and data effects for each mode.
5. Determine how the failure is detected and how quickly it can be distinguished from normal delay.
6. Assess containment: duplicates, partial state, cascade, retry storms, incorrect documents, or data inconsistency.
7. Define recovery: retry, resume, compensate, replay, reconcile, fallback, or controlled manual action.
8. Define stop conditions where automation must stop instead of retrying.
9. Design a safe resilience test for critical modes.
10. Record gaps, improvements, validation, residual risk, and owner.

## Decision rules
- Review business and data failure modes, not only infrastructure outages.
- A retry is not safe until duplicate and side-effect behaviour is understood.
- A failure without a reliable detection signal is an observability gap.
- Recovery that depends on undocumented expert knowledge is a control gap.
- Critical modes should have explicit stop conditions and ownership.
- Treat residual risk as a decision input, not as wording to hide uncertainty.

## Output format
Produce a **Failure Mode / Resilience Review** containing:
- capability and business criticality;
- dependency or boundary;
- failure mode and trigger;
- business, technical, and data effects;
- detection signal;
- containment and stop condition;
- recovery path;
- resilience test and result;
- gap, improvement, residual risk, and owner.

## Quality gates
- Critical dependencies and business outcomes are included.
- Failure modes cover availability, latency, integrity, ordering, capacity, identity, configuration, and human recovery where relevant.
- Detection is specific and actionable.
- Retry and recovery paths address duplicate and partial-state risk.
- Critical modes have tests or explicit reasons why testing is not feasible.
- Residual risks and owners are explicit.

## References
- `references/method.md`
- `references/templates.md`
- `references/examples.md`
