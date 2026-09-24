---
layout: default
title: "Data Quality Controls"
description: "Data quality controls prevent, detect, measure, and correct data that is not fit for its intended business use."
tags:
  - concept
  - sap-master-data
  - sap-s4hana
  - sap-datasphere
  - data-quality
  - ai-operations
  - automation
permalink: /atlas/concepts/data-quality-controls/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
last_reviewed: 2026-09-23
related:
  - /atlas/maps/data-mesh-architecture-map/
  - /atlas/maps/sap-data-products-map/
  - /atlas/concepts/data-mesh-for-sap-landscapes/
  - /atlas/concepts/data-lineage/
  - /atlas/concepts/data-product/
  - /atlas/sap/sap-mdg/
  - /atlas/sap/sap-datasphere/
  - /atlas/sap/sap-s4hana/
---

# Data Quality Controls

> **Status**: Under review.  
> **Scope**: Preventive, detective, and corrective controls for important SAP data.

A data quality control is not simply a mandatory field. It is any control that helps keep data fit for a defined business use. Some controls stop bad data before it is saved, some detect problems after the fact, and some support correction once a problem is known.

That distinction matters in SAP because data quality problems appear at different layers. A missing tax classification may block an order. A duplicate business partner may not fail immediately but can fragment reporting and credit exposure. A stale analytical extract may be technically valid and still be unsuitable for a daily decision.

## Start with the business use, not the dimension list

Terms such as completeness, validity, consistency, timeliness, uniqueness, and accuracy are useful, but they are not controls by themselves. The useful question is: **what must be true for this data to support the process safely?**

For a business partner, that might mean required address fields, valid tax information, and no probable duplicate above an agreed threshold. For an analytical data product, the concern may be freshness, reconciliation to a source total, and stable semantics. The same field can therefore have different quality expectations in different processes.

We usually separate controls into three layers:

1. **Preventive controls** reject or constrain data before it enters the productive process.
2. **Detective controls** measure existing data and surface exceptions, duplicates, or rule violations.
3. **Corrective controls** route bad data to an owner or governed process for repair.

A strong design uses all three where the business risk justifies them. Trying to prevent every possible error at entry time often creates unusable forms and brittle rules; detecting everything downstream leaves operations cleaning up avoidable problems.

## Where SAP MDG fits

SAP Master Data Governance provides several mechanisms that belong to different parts of this control model. In MDG processes, validation can check whether a record meets defined quality requirements before it is accepted. SAP's current documentation uses the simple example that data can be saved only when Street and House Number are maintained.

MDG also supports duplicate checking for master data. For example, when a new business partner is created, configured matching logic can compare entered attributes with existing records and warn about potential duplicates. The result is not the same as a hard uniqueness constraint: duplicate detection is often probabilistic and depends on the configured search and thresholds.

For ongoing quality management, SAP MDG Data Quality Management supports validation rules, derivation scenarios, data quality KPIs, evaluation results, and trend monitoring for supported master-data domains. This is important because a rule that protects one change request does not tell us whether thousands of existing records are already inconsistent.

## Operational controls are related, but not the same thing

S/4HANA process configuration can also protect data and transactions: required fields, incompletion checks, status controls, tolerances, and business validations all reduce the chance that unusable information moves forward. These controls are valuable, but we should not label every process check as “data quality governance.”

A three-way match, for example, is primarily a transactional control over purchasing and invoice processing. It may reveal a data problem, but its main purpose is not to maintain master-data quality. Keeping that distinction clear makes ownership easier: master-data governance, application configuration, and process control are related disciplines, not interchangeable labels.

## A practical control chain

Suppose supplier bank data is business-critical. A sensible control chain might look like this:

- validate required structure when the record is created or changed;
- apply approval for sensitive changes;
- run duplicate or consistency checks where they are meaningful;
- monitor existing records for rule violations;
- route exceptions to an accountable data owner;
- measure whether the exception population is actually shrinking.

The last step is often missed. A dashboard that counts errors but does not connect them to ownership and correction is monitoring, not control.

## What we would check when quality drops

When a quality KPI worsens, the first question is not “which tool failed?” We check whether the business rule changed, whether a new source or migration introduced data, whether a validation stopped running, whether users found a workaround, and whether the metric itself still represents the intended business rule. Good quality management treats the rule, the process, and the measurement as one system.

## Related Atlas pages

- [Data Lineage](/atlas/concepts/data-lineage/)
- [Data Mesh for SAP Landscapes](/atlas/concepts/data-mesh-for-sap-landscapes/)
- [SAP MDG](/atlas/sap/sap-mdg/)
- [SAP Datasphere](/atlas/sap/sap-datasphere/)

## Source references

- SAP Help Portal — [Working with MDG, Data Quality Management](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/03f3f2e3d99a47b39fc106e52304e665.html)
- SAP Help Portal — [Configure Validation](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/d2207d5496ac104ee10000000a423f68.html)
- SAP Help Portal — [Duplicate Check](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/4d523f354bf74b049cfd5f59aa56aac4.html)

## Verification limitations

Exact validation, matching, and monitoring options depend on the master-data domain, deployment model, and enabled SAP components. This page describes the control model and verified MDG capabilities without assuming that the same rule engine or quality metric exists for every data object.
