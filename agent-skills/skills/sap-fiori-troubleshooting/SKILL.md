---
name: sap-fiori-troubleshooting
description: Use when a SAP Fiori app is missing, cannot open, shows no data, returns HTTP errors, behaves with stale resources, or is unexpectedly slow. Isolate the failing layer with browser, launchpad, Gateway, backend, authorization, and cache evidence before proposing a fix. Produces a Fiori Troubleshooting Record. Do not use for broad incident classification before the affected app or layer is known.
---

# SAP Fiori Troubleshooting

## Purpose

Isolate SAP Fiori application failures by following evidence from the browser to the responsible system layer. Produce a case record that another consultant can reproduce, review, and validate.

The main rule is: **find the first failing layer before changing the system**.

## Use when

- A Fiori app or tile is missing for a user.
- Launchpad navigation cannot resolve or open an app.
- The app opens but shows no data or a technical error.
- Browser Network shows HTTP 4xx or 5xx responses.
- The app behaves differently for another user, client, role, or business object.
- The UI shows stale content after a deployment or configuration change.
- The app is slow and the slow layer is not known.

## Do not use when

- The production impact is still broad or the affected application is not known. Use `incident-triage` first.
- The failing layer is already isolated and a deeper causal analysis is required. Use `root-cause-analysis`.
- The problem is a generic IDoc, queue, RFC, or middleware failure with no Fiori entry point. Use the relevant integration skill.
- The request is only to clear caches without evidence of a cache problem.

## Required inputs

Collect before changing the system:

- App name and launch path.
- User, system, client, date, and exact timestamp.
- Observed behavior and expected behavior.
- Known-good comparison if available.
- Browser Console output relevant to the failure.
- Browser Network request that failed or took unusually long.
- HTTP method, request path, status code, response text, and request/correlation identifier when available.
- Semantic object/action or launch target when navigation is involved.
- Recent transport, role, app-content, service, UI, or cache-related change.
- Access to relevant SAP logs and authorization analysis tools for the landscape.

## Workflow

1. **Reproduce once under controlled conditions.** Record app, user, system/client, timestamp, exact action, observed result, and expected result.
2. **Classify the symptom shape.** Use one of: missing content, navigation failure, resource/UI load failure, service/backend failure, wrong business result, performance, stale content, unknown.
3. **Capture browser evidence.** Open developer tools. Save relevant Console errors and Network requests. Identify the first meaningful failure rather than the final UI error.
4. **If launchpad navigation fails, stay in the launchpad layer.** Check target intent, role/content assignment, target mapping, and system alias before opening application code. Use launchpad analysis tools available in the landscape.
5. **If an HTTP request fails, follow that request.** Record method, path, status, response, payload when safe, and timestamp. Identify which system rejected or failed it.
6. **For ABAP Gateway OData scenarios, correlate Gateway evidence.** Check `/IWFND/ERROR_LOG` for the same user/time. If backend processing failed, inspect backend error information and `/IWBEP/ERROR_LOG` where applicable.
7. **Separate technical transport from business validation.** If the request reached backend application logic and returned a business rule or document error, move to the relevant functional diagnostic method. Do not keep treating it as a frontend defect.
8. **Check authorization only when evidence points there.** For missing backend authorizations, collect evidence with tools such as `SU53` or an authorization trace such as `ST01` where appropriate. Do not broaden roles as a diagnostic shortcut.
9. **Use the cache branch only for stale or unavailable resources.** Capture the stale/missing resource first. Then use landscape-appropriate browser or launchpad cache invalidation. In relevant ABAP launchpad scenarios, `/UI2/INVALIDATE_GLOBAL_CACHES` may be part of the corrective action.
10. **For performance, name the slow component.** Use Network timing to distinguish static resource delay from service/backend delay. Do not assign “Fiori performance” without a slow request or resource.
11. **State the failing layer and owner.** Choose launchpad/content, UI/frontend, service/Gateway, backend application, authorization, cache, platform/connectivity, or unknown.
12. **Apply one controlled action.** Record the action, risk, rollback, and owner. Avoid multiple simultaneous changes.
13. **Validate the original case.** Repeat the same business action. Confirm the request, UI behavior, and business result. Check that no new relevant Console or Gateway errors appear.
14. **Produce the Fiori Troubleshooting Record.** Include evidence, rejected hypotheses, action, and validation.

## Decision rules

- If the app is missing only for one user, compare role/content assignment before checking backend logic.
- If navigation fails before app bootstrap, stay in launchpad content and intent resolution.
- If one Network request returns 4xx/5xx, follow that request before debugging unrelated code.
- If the request reaches backend logic and returns a business validation message, switch to functional process analysis.
- If a Gateway error exists at the same timestamp and user, treat it as primary technical evidence for that request.
- If authorization evidence is missing, do not propose broad role additions.
- If stale resources appear after a deployment, treat cache/version behavior as a hypothesis and capture the affected resource first.
- If the app is slow, identify the slow request or resource before routing ownership.
- If several unrelated Fiori apps fail at the same time, return to incident triage and check shared platform, connectivity, identity, or recent change.
- If the same symptom has already been “fixed” more than once, create a root cause analysis after containment.
- If the architecture is not ABAP Gateway based, do not force Gateway transactions into the path. Adapt the layer model to the actual deployment.

## Output format

Produce a **Fiori Troubleshooting Record**:

```markdown
---
artifact: Fiori Troubleshooting Record
id: FIORI-001
date: YYYY-MM-DD
owner: Name / Team
status: open | isolated | fixed | validated
---

## Case
App:
System / client:
User:
Timestamp:
Business process:

## Symptom
Observed:
Expected:
Working comparison:

## Launch identity
Semantic object / action:
Launchpad content / role:
Target system / alias:

## Browser evidence
Console error:
Failed or slow request:
HTTP method:
HTTP status:
Response:
Request / correlation ID:

## Layer classification
<!-- launchpad | ui | service | gateway | backend | authorization | cache | performance | platform | unknown -->

## SAP evidence
/IWFND/ERROR_LOG result:
/IWBEP/ERROR_LOG result:
Application log / dump / document evidence:
Authorization evidence:

## Recent changes

## Hypotheses tested
1. Hypothesis:
   Test:
   Evidence:
   Result: keep | reject

## Root cause or failing layer

## Action
Containment:
Fix:
Risk / rollback:
Owner:

## Validation
Original case retested:
Network result:
Business result:
Regression check:

## Reusable lesson
Next skill / runbook update:
```

If the root cause remains unknown, the output must still state the isolated layer, what has been ruled out, and what evidence is missing.

## Quality gates

- [ ] Exact user, system/client, timestamp, app, and action are recorded.
- [ ] Observed and expected behavior are both clear.
- [ ] Browser Console and Network were checked before system changes.
- [ ] The first meaningful failed or slow request/resource is captured when present.
- [ ] A failing layer is named, or the record explains why it remains unknown.
- [ ] Gateway logs are checked only when the request uses the relevant ABAP Gateway path.
- [ ] Authorization changes are supported by authorization evidence.
- [ ] Cache invalidation is linked to a stale/resource hypothesis.
- [ ] One controlled fix is recorded with owner and rollback/risk.
- [ ] Validation repeats the original business action.
- [ ] The final record contains enough evidence for another consultant to continue without restarting the investigation.

## References

- `references/method.md` — Layer model, evidence path, and owner routing.
- `references/templates.md` — Copy-ready Fiori Troubleshooting Record and compact evidence table.
- `references/examples.md` — Synthetic examples for navigation, OData/backend, authorization, and stale-resource cases.

## Safety rules

- Do not expose client names, real users, internal URLs, ticket numbers, production payloads, or proprietary data in public artifacts.
- Redact credentials, tokens, session cookies, personal data, and sensitive business payload fields from browser traces.
- Treat recent changes as hypotheses, not proof.
- Do not clear global caches, broaden authorizations, restart services, or change configuration only to “see if it helps.” Require evidence and follow landscape change controls.
- Separate technical success from business success. A HTTP 200 response does not prove that the business result is correct.
