---
layout: default
title: "OpenUI5 OData V4: the model read finished before the refresh"
description: "A reported OpenUI5 1.78 timing issue shows how to check whether an OData V4 read waited for a refresh, and what requestRefresh added in 1.87.0."
permalink: /atlas/diagnostics/openui5-odata-v4-refresh-race/
last_modified_at: 2026-11-13
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration
concept_type: documented incident case
sap_area: "OpenUI5 OData V4"
business_process: "Application support"
status: needs_verification
verified: false
author: MetalHatsCats
tags:
  - sap
  - openui5
  - odata
  - incident-triage
related:
  - /atlas/diagnostics/sap-odata-service-diagnostics/
  - /atlas/diagnostics/sap-incident-triage-diagnostics/
robots: noindex,follow
sitemap: false
---

# When an OData V4 read finishes before the refresh

In [OpenUI5 issue #3135](https://github.com/UI5/openui5/issues/3135), an application called `refresh()` and then `requestObject()` on an OData V4 context. On OpenUI5 1.78, the reporter saw the read promise resolve immediately. To decide whether to investigate the service or the application, first establish whether the refresh response had arrived when the application consumed the value.

## The symptom in the network trace

The [reporter's follow-up](https://github.com/UI5/openui5/issues/3135#issuecomment-769458861) described a Northwind example where the refresh request was still pending when the promise resolved. At that moment the read could not establish what the refresh returned. This is a useful distinction when a user reports stale data just after pressing Refresh.

The [reporter's attached example](https://github.com/SAP/openui5/files/5890476/com.myorg.v4promise.zip) declares OpenUI5 1.84.0. The [original issue](https://github.com/UI5/openui5/issues/3135) reports 1.78. Keep both versions in the incident record when comparing the attachment with the initial report.

## Why the read could finish early

A [maintainer reported the change on the 1.87.0 development line](https://github.com/UI5/openui5/issues/3135#issuecomment-774010522). The [linked fix, commit 7bdb33b](https://github.com/UI5/openui5/commit/7bdb33bbeff606ed2f3beea6b83cb3cfbb25de86), adds `requestRefresh()` to the context and bindings. The context method returns a promise that resolves without a payload after the refresh and rejects on refresh failure. The existing `refresh()` call keeps its error handling and does not expose that promise.

The [OpenUI5 1.87.0](https://github.com/UI5/openui5/blob/8d6e9357813bcb9e7d4ea0976fe021aac7eecf3c/src/sap.ui.core/src/sap/ui/model/odata/v4/Context.js) context source exposes `requestRefresh()`. The method is absent from [OpenUI5 1.86.0](https://github.com/UI5/openui5/blob/c339097b0bae21fab94407f7baf1c632d9b3d522/src/sap.ui.core/src/sap/ui/model/odata/v4/Context.js). Use the installed context API to check whether the application can await refresh completion.

The upstream integration test waits for `requestRefresh()` on both the binding and its context, then reads the updated property. This demonstrates the assertion to look for when checking the client sequence.

## How to check a similar report

1. **Match the context to the network response.** Note the deployed UI5 version, binding, entity key and request group. Capture when the application starts the refresh, when the matching response arrives and when the application uses the read result.
2. **Wait explicitly on a version with the API.** Await `requestRefresh()` and handle its failure. Then read the object from the same context. Compare the field the application uses with the field in the matching refresh response.
3. **Route the finding from the evidence.** An early read points to the application sequence. If the response itself contains the old value, investigate the service read path. If the response is current and the displayed value is old, inspect the context, binding and display logic.

## Version boundary

The report covers one OData V4 path on OpenUI5 1.78. The fix establishes the API introduced in 1.87.0. Check the installed version and binding before applying the same sequence to another application. For evidence to keep in a handover, see [SAP OData service diagnostics](/atlas/diagnostics/sap-odata-service-diagnostics/).
