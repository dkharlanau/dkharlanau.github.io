---
author: "Dzmitryi Kharlanau"
layout: default
title: "Architecture Fitness Review — Working Skill"
description: "Check whether an architecture still satisfies its intended outcomes, quality attributes, boundaries, controls, and operating assumptions after real change."
permalink: /skill-hub/problem-solving-operations/architecture-fitness-review-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

# Architecture Fitness Review

An architecture diagram can remain unchanged while the architecture itself drifts underneath it.

## Working method
1. Recover the intended outcomes, constraints, and key architecture decisions.
2. Review current quality attributes and whether workload or business criticality changed.
3. Compare current dependencies, data flows, ownership, controls, and deployment boundaries with the intended model.
4. Review incidents, operational metrics, exception volume, change lead time, and recurring workarounds.
5. Test important architecture principles as observable fitness conditions.
6. Identify drift: accidental coupling, duplicated rules, ownership gaps, hidden manual steps, unsupported technology, or monitoring blind spots.
7. Classify findings as healthy, watch, corrective action, or architecture decision required.
8. Record evidence and the next review trigger.

## Output
An **Architecture Fitness Review** contains intended properties, current evidence, fitness checks, drift findings, risk, action, owner, and review triggers.

## Lead signal
The goal is not architectural purity. The goal is to know whether the system is still fit for the business conditions it now has.
