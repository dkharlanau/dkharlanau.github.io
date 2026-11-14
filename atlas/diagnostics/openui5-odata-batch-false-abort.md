---
layout: default
title: "OpenUI5 OData batch: a successful save reported as aborted"
description: "A documented OpenUI5 1.38 case shows how to distinguish an OData update response from the result reported by the client event."
permalink: /atlas/diagnostics/openui5-odata-batch-false-abort/
last_modified_at: 2026-11-13
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration
concept_type: documented incident case
sap_area: "OpenUI5 OData V2"
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

# When the save succeeded and the UI reported an abort

The symptom was an aborted save message. The backend had already stored the change. In [OpenUI5 issue #1125](https://github.com/UI5/openui5/issues/1125), the reporter traced the same OData V2 update through both layers: the backend returned HTTP 204, but the client's `batchRequestCompleted` event described the update as aborted with status 0.

That discrepancy changes the first support decision. Before repeating the save or escalating to the service team, find out whether the original write took effect. The browser's network response, the state of the entity, and the event used to display a message can tell different stories.

## How the client cause was narrowed down

The reported app used two-way binding. Saving called `submitChanges()` and sent a batch with an update in a change set and additional read requests. The app inspected each operation in the completion event to decide whether it had worked.

The reporter observed that the backend updated the entity in both versions. The client event reported success in their comparison with 1.28 and reported an abort on 1.38.7. Switching the update from MERGE to PUT did not resolve the discrepancy. The [original report](https://github.com/UI5/openui5/issues/1125) includes the version comparison and links to a small example.

A [maintainer confirmed the issue on 1.38.x](https://github.com/UI5/openui5/issues/1125#issuecomment-251660283). The [fix in commit 44f228f](https://github.com/UI5/openui5/commit/44f228f23c4988f96d9bdbf2b8e3848edaf9582d) checks the internal request queue before aborting a change handle and updates the model tests. The commit describes a request being marked aborted even though it had been processed. The reported status 0 came from the client's event, while the backend response for the update was 204.

The [OpenUI5 1.38.9](https://github.com/UI5/openui5/blob/0cc400fb995fbe5b179c01ecda51a13175e7a530/src/sap.ui.core/src/sap/ui/model/odata/v2/ODataModel.js) source contains the queue-aware abort change. The [OpenUI5 1.38.8](https://github.com/UI5/openui5/blob/f5ac6a5e70fcde8da8e3c03e1e2d353cd5a009b5/src/sap.ui.core/src/sap/ui/model/odata/v2/ODataModel.js) source predates it. Use these tags to identify the upstream boundary and check the installed SAPUI5 patch separately.

The upstream regression test exercises a two-way-bound edit followed by a refresh. It checks the update’s 204 and the read’s 200 in the batch completion event. A support check also reads the persisted entity to establish the result in the deployed application.

## What to check on a similar ticket

1. **Find the write inside the batch.** Match the entity key and change set to the user action. Read the response for that operation; the outer batch status and the statuses of the accompanying reads answer different questions.
2. **Check the persisted value.** Use an authorized read from the service or a trusted backend view. Compare the expected value and the returned value for the same entity. If the result is unclear, leave the write outcome open rather than assuming a retry is safe.
3. **Compare the event with the response.** Record the deployed UI library version, the update response, the event payload for that operation and the stored value. When the operation succeeded and the event disagrees, investigate the client model and the code that turns its events into messages.
4. **Verify the correction at the point of use.** On the version you intend to deploy, check one save across all three layers: the operation response, the stored entity and the visible success or error message.

This is a historical OpenUI5 OData V2 case, not a diagnosis of every status 0 or a guarantee about current SAPUI5 versions. The public record confirms the reported discrepancy and the upstream fix. It does not establish when any particular customer's environment received the patch.

For a service-side fault, follow [SAP OData service diagnostics](/atlas/diagnostics/sap-odata-service-diagnostics/). To write an incident handover, use [SAP incident triage](/atlas/diagnostics/sap-incident-triage-diagnostics/) and keep the three observations separate.
