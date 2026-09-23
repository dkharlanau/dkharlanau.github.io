---
layout: default
title: "SAP Authorization Diagnostics"
description: "Diagnose SAP authorization failures from the failed check, execution identity, user buffer, and role design instead of guessing at roles."
permalink: /atlas/diagnostics/sap-authorization-diagnostics/
publish: true
published: true
verification_status: verified
last_reviewed: 2026-09-23
deep_map:
  route: "/labs/enterprise-context/auth-deep-map.json"
  status: "verified"
  label: "Open structured auth map"
  expect: []
tags:
  - SAP
  - Authorization
  - Security
  - Diagnostics
subtitle: "Start with the failed authorization check, then prove which identity, object, field value, and role state caused it."
snippet: "Use SU53 or a targeted authorization trace to move from an access-denied symptom to the exact SAP authorization check, execution identity, and missing value."
principles:
  - "Reproduce the failed action under the real user and business context before changing roles."
  - "Treat a failed authorization check as evidence to interpret, not an instruction to add a wildcard."
  - "Separate the runtime check from role maintenance, generated profiles, user-master assignment, and the current user buffer."
limits:
  - "Some applications perform authorization checks to choose a code path, so not every failed check is the cause of the user's symptom."
  - "Emergency or broad access can prove that authorization is involved while still hiding the smallest correct role change."
related:
  - path: /atlas/sap/identity-access/
    title: Identity and Access
  - path: /atlas/sap/audit-trails/
    title: Audit Trails
  - path: /atlas/sap/fiori-ui5/
    title: Fiori / UI5
---
{% include atlas_symbols.html %}

{% include content_linking.html kind="related" title="Related Content" links=page.related %}

An authorization incident becomes much easier once we stop asking, “Which role is missing?” and ask a narrower question: <strong>which authorization check failed, for which user, with which field values, while doing which business action?</strong>

That distinction matters in SAP because access is evaluated at runtime. A user may have the expected role name and still fail because one organizational value is missing. Another user may see the same error text even though the failing check runs under an RFC, workflow, or background user rather than the person in the browser.

<aside class="callout">
<strong>Working rule:</strong> capture the failed check first. Change the role only after the authorization object, field values, execution identity, and business need agree.
</aside>

## SU53 is the fastest snapshot after a real denial

For a fresh ABAP authorization error, <code>SU53</code> is usually the quickest place to start. SAP documents it as authorization error analysis for an access-denied error that has just occurred. It shows the failed authorization check and lets us compare that check with the user's authorization data.

Timing matters. Reproduce the exact action, then run <code>SU53</code> immediately. If the user performs other actions first, a later failed check can replace the evidence we wanted. Capture the authorization object, every checked field and value, the user, the business action, and the approximate timestamp together.

A failed check is not automatically the root cause. Applications can test an authorization and then follow a different path when the check fails. The useful question is whether the failed object and values correspond to the action that the user could not complete. If the evidence is ambiguous, move to a trace rather than granting access from a single screenshot.

## Use an authorization trace when one snapshot is not enough

<code>STAUTHTRACE</code> records authorization checks during a controlled test. SAP describes it as the authorization-focused form of the system trace: it can be restricted to a user, records the object plus checked field values, and can show the ABAP call point where the check occurred.

That makes a trace more useful when the process performs several checks, the failure happens in another session, or a technical user is involved. Keep the scope narrow: choose the correct user, start the trace, reproduce one representative path, stop the trace, and evaluate the sequence. A long unrestricted trace creates noise and makes an otherwise simple incident harder to read.

The trace also answers an important question that role lists cannot: <strong>what did the application actually check?</strong> PFCG content tells us what a role can grant. Runtime evidence tells us what this execution requested.

## Read the object field by field

Suppose the trace shows an authorization object with <code>ACTVT = 02</code> and a sales organization value that the user does not hold. “The object is missing” is then too coarse. The role may already contain the object for display activity, for a different sales organization, or through another authorization instance.

Interpret each field in the business context. Activity, organizational level, document type, authorization group, and other object-specific fields answer different questions. A correction should grant the approved action for the approved scope, not merely make the red line disappear.

This is why copying a broad role is a poor diagnostic technique. It changes many variables at once. The incident may disappear, but we no longer know whether the missing element was one activity value, one plant, one service start authorization, or something unrelated that arrived with the copied role.

## Separate role design from what the user has at runtime

A common source of confusion is treating the PFCG role, its generated authorization profile, the user assignment, and the user's current authorization buffer as the same thing. They are related, but they are not identical states.

SAP documents that after authorization data in a role changes, its authorization profile must be regenerated. User assignments then have to be reflected in the user master through user comparison or the configured automatic/background process. <code>SU56</code> shows the authorizations available in the user buffer and is useful when the role definition looks correct but runtime behavior still disagrees.

This gives us a cleaner diagnostic sequence:

1. prove the failed runtime check;
2. inspect the values currently available to the user;
3. locate the role or roles intended to supply those values;
4. confirm that the role authorization data and generated profile are current;
5. confirm the assignment is valid for the user and date;
6. retest the same business action.

The order matters. Otherwise a correct role design can be blamed for an assignment problem, or a missing authorization value can be misdiagnosed as a user-buffer problem.

## Diagnose the identity that actually executes the step

The person reporting the error is not always the user evaluated by the failing check. A dialog action can trigger an RFC call, a workflow step, a background job, an OData request, or middleware processing under another identity.

Before changing access, identify the execution context. For a dialog failure, trace the dialog user. For a background step, identify the job user. For an integration, determine whether the backend sees a technical user, a propagated business user, or another configured identity. If the trace is attached to the wrong user, a perfectly accurate authorization trace will still answer the wrong question.

This is also why front-end success does not prove backend authorization. A user can authenticate successfully, open SAP Fiori launchpad, and see an app while the backend later rejects an OData service or business authorization. Current SAP S/4HANA documentation distinguishes launchpad and general OData authorizations from app-specific backend authorizations. In landscapes with separate front-end and back-end layers, both sides can therefore matter to one visible symptom.

## Fix the smallest justified scope, then retest the process

Once the missing check is understood, change the role that owns that business responsibility. Prefer explicit values over wildcards, and keep organizational scope aligned with the user's job. If the proposed fix grants materially more access than the failed action requires, the diagnosis is not finished.

After the role change, regenerate the profile when required, complete the relevant user comparison or assignment update, and retest the exact step that originally failed. Then check one or two adjacent actions that should remain restricted. A successful retest proves the required path works; it does not by itself prove that the resulting role is least-privilege.

For sensitive access, retain the original evidence and the approved change through the local security process. That creates a useful chain: symptom → failed check → business justification → role change → successful retest.

## Source references

- SAP ABAP Platform 2025 FPS01 — [Analyzing Authorization Checks](https://help.sap.com/docs/ABAP_PLATFORM_NEW/ad77b44570314f6d8c3a8a807273084c/526716b3439b11d1896f0000e8322d00.html)
- SAP ABAP Platform — [Using the System Trace to Record Authorization Checks (Transaction STAUTHTRACE)](https://help.sap.com/docs/ABAP_PLATFORM_NEW/c6e6d078ab99452db94ed7b3b7bbcccf/927ac87d293a47d8a17368c9f45661f4.html)
- SAP ABAP Platform 2025 FPS01 — [Regenerate the Authorization Profile Following Changes](https://help.sap.com/docs/ABAP_PLATFORM_NEW/ad77b44570314f6d8c3a8a807273084c/52671538439b11d1896f0000e8322d00.html)
- SAP S/4HANA 2025 FPS01 — [General Authorizations Required for SAP Fiori](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/22bbe89ef68b4d0e98d05f0d56a7f6c8/cd6e1b6b87dd423ca491f2cd38b7bf4f.html)

{% include reference_list.html references=page.reference_list %}

{% include disclaimer.html %}
