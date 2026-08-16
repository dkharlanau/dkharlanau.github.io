---
author: "Dzmitryi Kharlanau"
layout: default
title: "Non-Functional Requirements — Working Skill"
description: "Turn vague quality expectations into measurable, testable, owned requirements that shape architecture and operations."
permalink: /skill-hub/problem-solving-operations/non-functional-requirements-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

# Non-Functional Requirements

"Fast, secure and highly available" is not a requirement. It is a wish list wearing a tie.

## What this skill does
It converts quality expectations into measurable conditions that architecture, testing, release, and operations can use.

## Working method
1. Start from a business outcome and failure impact.
2. Identify relevant quality attributes: availability, latency, throughput, scalability, recoverability, consistency, security, privacy, auditability, maintainability, supportability, portability, and cost.
3. Add context. A target without workload, data volume, geography, user group, or time window is incomplete.
4. Define measurable targets and tolerances.
5. Define the measurement point. Client latency, API latency, queue delay, and end-to-end business completion are different metrics.
6. Define normal, peak, degraded, and recovery conditions.
7. Record dependencies and assumptions behind the target.
8. Assign an owner and verification method.
9. Link the requirement to architecture decisions, tests, monitoring, and release gates.
10. Review conflicts between attributes, such as stronger consistency versus availability or deeper logging versus privacy/cost.

## Output
A **Non-Functional Requirement Set** should state the scenario, metric, target, tolerance, measurement point, verification method, owner, and related trade-off.

## Lead signal
A Lead does not merely collect NFRs. They expose which quality attributes actually matter to the business and which architectural trade-offs those targets create.
