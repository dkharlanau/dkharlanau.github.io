---
layout: default
title: "SAP Incident Lab — Synthetic Cases for Diagnosis Practice"
description: "A small, transparent dataset of synthetic SAP support incidents for practising diagnosis, evidence collection, ownership, recovery decisions, and verification."
permalink: /datasets/incident-lab/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_reviewed: 2026-08-16
last_modified_at: 2026-08-16
tags:
  - SAP
  - AMS
  - diagnostics
  - incident-management
  - dataset
structured_data:
  type: Dataset
  name: "SAP Incident Lab"
  description: "Synthetic SAP support incidents designed for diagnosis and decision practice. The cases contain no production or customer data."
  distribution:
    - "@type": DataDownload
      encodingFormat: application/json
      contentUrl: https://dkharlanau.github.io/datasets/incident-lab/cases.json
    - "@type": DataDownload
      encodingFormat: application/schema+json
      contentUrl: https://dkharlanau.github.io/datasets/incident-lab/cases.schema.json
---

# SAP Incident Lab

Incident Lab is a small practice dataset for SAP support and operations work. It is designed around a simple question: **what evidence would you need before making a technical or business decision?**

The cases are synthetic. They do not contain production data, customer names, system identifiers, tickets, or copied project material. This makes the dataset safe to inspect and useful for repeatable exercises.

## What is inside

- [Cases in JSON](/datasets/incident-lab/cases.json) — incident situations with symptoms, context, evidence and decision points.
- [JSON Schema](/datasets/incident-lab/cases.schema.json) — the contract used to validate the dataset structure.

The cases can be used to practise five things: separating symptoms from causes, asking for evidence, finding the correct owner, choosing a safe recovery path, and defining how the result will be verified.

## Usage

A useful incident review should not start with a transaction code. Start with business impact and observable facts. Then move through the chain:

**Impact → Evidence → Ownership → Hypothesis → Safe action → Verification → Prevention**

The dataset supports this flow without pretending that a short case can reproduce a real SAP landscape. The point is decision quality, not theatre.

## Update policy

The dataset is updated only when a case, field, or validation rule changes. Each update should keep the JSON Schema and examples aligned, and the page review date records when the public contract was checked.

## Trust boundary

**What this dataset can show:** a consistent diagnostic method, explicit assumptions, structured evidence and repeatable reasoning exercises.

**What it cannot show:** production experience, customer outcomes, benchmark results, or proof that one recovery action is correct for every SAP system. Real incidents depend on configuration, releases, integrations, data and operational constraints.

For the wider operating model, see [AMS Next Gen](/notes/ams/). For technical investigation patterns, use [Atlas Diagnostics](/atlas/diagnostics/). For business process and integration context, continue to [Enterprise Context Lab](/labs/enterprise-context/).
