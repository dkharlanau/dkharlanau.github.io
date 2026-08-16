---
author: "Dzmitryi Kharlanau"
layout: default
title: "Exception Strategy — Working Skill"
description: "Design how expected exceptions are detected, classified, routed, corrected, approved, retried, reconciled, and learned from."
permalink: /skill-hub/problem-solving-operations/exception-strategy-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

# Exception Strategy

A process is not designed when only the happy path has a diagram.

## Working method
1. Define the normal path and business completion state.
2. Enumerate expected exception classes: validation, missing data, authorization, dependency outage, timeout, duplicate, sequencing, partial completion, business rejection, and manual hold.
3. Separate expected exceptions from unknown failures.
4. Define detection and evidence for every important class.
5. Define whether the response is reject, hold, retry, compensate, reroute, correct-and-resubmit, approve, or escalate.
6. Define ownership and decision rights.
7. Define idempotency and duplicate protection before enabling automatic retries.
8. Define maximum retry or waiting boundaries.
9. Define reconciliation for partial or uncertain outcomes.
10. Feed recurring exceptions into root-cause analysis or process redesign rather than treating permanent workarounds as normal operations.

## Output
An **Exception Strategy Record** contains exception classes, detection, action, owner, retry/compensation policy, evidence, escalation, and closure criteria.
