---
layout: note
title: "SAP Cloud ALM gets a Clean Core governance dashboard"
description: "SAP released a RISE with SAP Methodology Dashboard in Cloud ALM that provides real-time visibility into clean core compliance, extensibility health, and customer object governance across S/4HANA landscapes."
date: 2026-05-15
permalink: /news/2026-05-15-sap-clean-core-dashboard-cloud-alm/
last_modified_at: 2026-05-27
robots: noindex,follow
sitemap: false
tags:
  - sap
  - s4hana
  - clean-core
  - cloud-alm
---

**Source:** [SAP Community — Clean Core Part 1](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/clean-core-part-1-activation-of-rise-with-sap-methodology-dashboard-on/ba-p/14328522)
**Date checked:** 2026-05-27
**Confidence:** high
**Related page/topic:** [/ai/sap-ams-improvement/](/ai/sap-ams-improvement/)
**Practical implication:** AMS teams supporting S/4HANA Cloud should verify whether their customer's Cloud ALM tenant has the RISE Methodology Dashboard activated and understand the clean core KPIs it surfaces.
**Tags:** sap, s4hana, clean-core, cloud-alm

<h2>Clean core compliance is moving from annual audits to real-time dashboards</h2>

<p>SAP's Cloud ALM now includes a RISE with SAP Methodology Dashboard that tracks clean core compliance across the S/4HANA landscape. This shifts clean core governance from a project-phase checklist to an ongoing operational metric — which changes how AMS teams respond to upgrade readiness questions.</p>

<p>The dashboard covers three areas relevant to operations:</p>

<ul>
  <li><strong>Clean Core Extensibility KPIs</strong> — tracks whether extensions use released APIs, BAdIs, or ABAP Cloud extension points versus legacy modifications.</li>
  <li><strong>Customer Objects</strong> — provides a deep dive into custom code and objects, with visibility into which items block upgrade paths.</li>
  <li><strong>Data Principles</strong> — surfaces data quality and governance metrics tied to clean core readiness.</li>
</ul>

<p>The dashboard requires activation in Cloud ALM and links to SAP Learning Hub training resources. A demo tenant is available for hands-on evaluation. For AMS providers, this means clean core assessments can now be data-driven rather than based on static documentation reviews.</p>

<p>Watch item: the dashboard measures compliance against SAP's extensibility framework, but it does not automatically remediate violations. The gap between "knowing what is non-compliant" and "fixing it before the next upgrade" remains a services opportunity.</p>

<div class="section-actions">
  <a class="button" href="/ai/sap-ams-improvement/">Related: SAP AMS Improvement</a>
  <a class="button button--secondary" href="https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/clean-core-part-1-activation-of-rise-with-sap-methodology-dashboard-on/ba-p/14328522">Read source</a>
</div>
