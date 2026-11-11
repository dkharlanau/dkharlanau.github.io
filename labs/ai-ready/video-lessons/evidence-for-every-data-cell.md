---
layout: default
title: "One Changed Cell, One Defensible Decision"
description: "Practical AI Engineer lesson on data quality, evidence per change, audit, human approval. Source-based insights, SAP decisions and an exercise."
permalink: /labs/ai-ready/video-lessons/evidence-for-every-data-cell/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, video-learning, architecture, sap, evaluation]
career_impact: mapped
career_skills: [ai-data-governance, ai-business-value, integration-ownership]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# One Changed Cell, One Defensible Decision

**Problem and context:** In bulk master-data migration, a detected difference is not an approved correction. A reviewer needs the authoritative source, a versioned business rule and the owner of each proposed value.

A bulk spreadsheet contains 15,000 records. Some cells are wrong, some are blank, and some are legitimately different between systems. A tool can find differences in seconds. **Deciding which differences should be changed** is a different job.

In [How Agents Cut Hour-Long Data Checks to 5 Minutes](https://aietalks.com/talks/how-agents-cut-hour-long-data-checks-to-5-minutes), Amol Kapoor and Clifford Ressel (Nori Agentic) describe an AI-assisted review process for complex financial master data: collect evidence, explain each proposed cell change and ask an accountable owner to accept or reject it. The reported time reduction is their case study, not a generic productivity forecast.

This pattern transfers well to SAP data migration without copying private finance use cases.

## Distinguish three data operations

**Detect:** find missing or conflicting values.

**Recommend:** use approved documents, mappings and business rules to explain a proposed correction.

**Apply:** execute a validated, authorized update only after the required approval and preflight controls.

Many migration utilities combine the first and third steps and skip the second. That creates fast bad updates.

## The evidence package for one cell

~~~json
{
  "record": "SYN-CUSTOMER-014",
  "field": "delivery_rule",
  "source_value": "A",
  "target_value": "",
  "proposed_value": "A",
  "change_type": "UPDATE",
  "rule_id": "SYN-RULE-07",
  "source_ref": "synthetic-extract-v2-row-14",
  "evidence_status": "review_required",
  "decision_owner": "master_data_owner",
  "write_performed": false
}
~~~

This is a **synthetic review contract**, not a SAP API. Preserve enough identity to find the field while minimizing private data in logs.

The key is an **explainable recommendation**: "Target is blank, source is A, rule v2 permits the value for this segment; source extraction was observed at time T." Avoid "AI says A is correct." If business exceptions exist, they should be represented as separate rules or review states.

## Which changes are safe to automate?

| Change | Reasonable default |
| --- | --- |
| Exact whitespace normalization with approved contract | Deterministic update after standard checks |
| Blank target and authoritative source, rule unambiguous | Controlled candidate; automate only if explicitly authorized |
| Conflicting source systems | Human review |
| Different meaning by sales area / customer category | Business rule and segment evaluation first |
| Deletion of a dependent object | Protected human decision with downstream dependency checks |
| Unknown source or outdated mapping | Stop; request evidence |

Do not use the LLM to decide exact equality, file format, mapping precedence or legal deletion. That belongs to deterministic logic and configured governance.

## Build a practical review workbook

Create a synthetic extract with 100 records, five fields, an authoritative source column and an exception rule table. Produce two outputs:

1. **Review ledger:** record, field, old, proposed, reason, evidence, risk, owner and decision.
2. **Upload template:** exact approved target format, built **only from approved updates**.

Highlight changed cells for the reviewer, but don't encode change meaning only with color. Use an explicit Insert/Update/Delete column. A separate rejected or unresolved list prevents ambiguous data from quietly disappearing.

Run three checks before calling the process complete: source/target identity matching, exact upload template structure and downstream verification after controlled execution.

**Architect question:** Can the AI recommend changing 15,000 cells if only 500 have source-backed evidence? How would you make the remaining 14,500 visible and safe?

Related: [Data Quality Atlas](/atlas/data-quality/) · [Reusable Data Procedures](/reusable-data-procedures/) · [Talk transcript](https://ainotes.us/summary/how-agents-cut-hour-long-data-checks-to-5-minutes-amol-kapoor-clifford-ressel).

**Source boundary:** Nori Agentic's production description and time savings are speaker-reported. The SAP workbook design is synthetic.

*Editorial status: working study material, pending human review; noindex. All SAP scenarios are synthetic.*
