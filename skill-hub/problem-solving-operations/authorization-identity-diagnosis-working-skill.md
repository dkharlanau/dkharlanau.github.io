---
author: "Dzmitryi Kharlanau"
layout: default
title: "Authorization & Identity Diagnosis — Working Skill"
description: "A cross-domain method for separating authentication, identity propagation, role assignment, policy, object access, and business authorization failures."
permalink: /skill-hub/problem-solving-operations/authorization-identity-diagnosis-working-skill/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/problem-solving-operations/">Problem Solving &amp; Operations</a></li><li aria-current="page">Authorization &amp; Identity Diagnosis</li></ol></nav>

<article class="section note-detail atlas-page">
<p class="eyebrow">Working skill / Security diagnostics</p>
<h1>First prove who the system thinks you are.</h1>
<p class="lead">Access problems are often discussed as one vague topic called permissions. Split the path into authentication, identity propagation, role or policy evaluation, resource scope, and business authorization before changing access.</p>

<h2>Use when</h2>
<ul>
<li>A user can sign in but cannot open a function, record, API, or action.</li>
<li>An API returns 401 or 403, or a service account behaves differently across environments.</li>
<li>One user works while another user with a similar role fails.</li>
<li>Access changed after role, group, identity-provider, token, or deployment changes.</li>
</ul>

<h2>Required inputs</h2>
<ul>
<li>User or technical identity, environment, resource, action, timestamp, and exact symptom.</li>
<li>Expected access model: role, group, policy, scope, claim, ownership, or business rule.</li>
<li>A known-good identity or scenario when possible.</li>
<li>Relevant sign-in, authorization, application, or gateway evidence.</li>
<li>Recent role, group, policy, identity-provider, or deployment changes.</li>
</ul>

<h2>Workflow</h2>
<ol>
<li><strong>Define the requested action.</strong> State the exact resource and operation. "No access" is not specific enough.</li>
<li><strong>Confirm authentication.</strong> Determine whether the identity was successfully established and by which mechanism.</li>
<li><strong>Confirm effective identity.</strong> Check which user, service principal, technical account, delegated identity, or token subject reaches the target system.</li>
<li><strong>Check propagation.</strong> Verify important claims, groups, scopes, tenant, client, or mapped identity values across boundaries.</li>
<li><strong>Check coarse access.</strong> Does the identity have the application, API, menu, service, or role needed to reach the function?</li>
<li><strong>Check resource-level access.</strong> Determine whether authorization depends on object ownership, organizational unit, company, region, document state, field, or row-level policy.</li>
<li><strong>Check action-level access.</strong> Read, create, approve, change, delete, export, and execute can have different rules.</li>
<li><strong>Compare a known-good case.</strong> Compare effective roles, claims, resource scope, object state, and route. Do not compare job titles.</li>
<li><strong>Check recent changes and cache.</strong> A correct role assignment may not yet be effective everywhere, but do not use cache clearing as the first diagnostic step.</li>
<li><strong>Apply least change.</strong> Correct the smallest proven gap. Avoid broad roles or wildcard permissions as a shortcut.</li>
<li><strong>Validate.</strong> Repeat the original action and verify that unintended extra access was not introduced.</li>
</ol>

<h2>Decision rules</h2>
<ul>
<li>If authentication fails, do not investigate business authorization yet.</li>
<li>If the effective identity is wrong, fix propagation or mapping before adding permissions.</li>
<li>If two users have the same visible role but different results, compare effective claims, groups, organizational scope, and object context.</li>
<li>Never solve an unclear access problem by assigning an administrator role.</li>
<li>If the requested permission changes segregation-of-duties or sensitive access, escalate to the accountable security or process owner.</li>
<li>If access works only after token or session renewal, investigate propagation or cache timing before changing the policy model.</li>
</ul>

<h2>Output</h2>
<p>Produce an <strong>Authorization &amp; Identity Diagnosis Record</strong> with requested action, effective identity, authentication evidence, propagation evidence, expected rule, actual rule result, comparison case, root gap, proposed correction, approval need, and validation.</p>

<h2>Quality gates</h2>
<ul>
<li>The exact resource and action are named.</li>
<li>Authentication and authorization are treated as separate stages.</li>
<li>The effective identity at the failing boundary is known or explicitly unknown.</li>
<li>A known-good comparison is based on effective access data, not job title.</li>
<li>The correction follows least privilege.</li>
<li>Validation checks both restored access and unintended access expansion.</li>
</ul>

<h2>Related skills</h2>
<ul>
<li><a href="/skill-hub/problem-solving-operations/evidence-driven-troubleshooting-working-skill/">Evidence-Driven Troubleshooting</a></li>
<li><a href="/skill-hub/problem-solving-operations/api-contract-troubleshooting-working-skill/">API Contract Troubleshooting</a></li>
<li><a href="/skill-hub/sap-ams/fiori-app-troubleshooting-working-skill/">SAP Fiori App Troubleshooting</a></li>
<li><a href="/skill-hub/sap-ams/change-impact-analysis-working-skill/">Change Impact Analysis</a></li>
</ul>
</article>
