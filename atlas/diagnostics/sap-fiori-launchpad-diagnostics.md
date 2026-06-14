---
layout: default
title: "SAP Fiori Launchpad Diagnostics"
description: "A conservative diagnostic frame for missing tiles, catalogs, groups, and semantic object resolution in SAP Fiori launchpad."
permalink: /atlas/diagnostics/sap-fiori-launchpad-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration and interfaces
concept_type: diagnostic guide
sap_area: "Fiori / UI5"
business_process: User interface access
status: needs_verification
verified: false
level: 1
author: Dzmitryi Kharlanau
tags:
  - diagnostics
  - sap-ams
  - fiori
related:
  - /atlas/diagnostics/sap-odata-service-diagnostics/
  - /atlas/diagnostics/sap-authorization-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Fiori Launchpad Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP Fiori launchpad diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a Fiori tile, group, or app is missing or fails to launch.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>User interface access</dd></div>
      <div><dt>SAP area</dt><dd>Fiori / UI5</dd></div>
      <div><dt>Indexing</dt><dd>Noindex, review candidate</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>The SAP Fiori launchpad assembles tiles from catalogs and groups based on user roles, PFCG authorization, and backend OData service activation. A missing tile usually means the catalog is not assigned, the target mapping is missing, the OData service is inactive, or the app index is stale. The diagnostic task is to separate frontend configuration from backend authorization and service availability.</p>
    <p>This guide covers launchpad content and app launch issues, not UI5 application development or deep Frontend Server administration.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>A tile expected by the user is not visible on the launchpad home page.</li>
      <li>A tile is visible but clicking it shows a blank screen or "App could not be opened" error.</li>
      <li>A group is missing even though the catalog appears assigned.</li>
      <li>The launchpad loads slowly or shows outdated tile counts.</li>
      <li>Search navigation from the Fiori search page returns no results for an app.</li>
      <li>Semantic object navigation from another app fails with "Could not open app."</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing catalog or group assignment:</strong> the user role does not include the catalog, or the group is not assigned to the user.</li>
      <li><strong>Missing target mapping:</strong> the tile points to an intent that has no corresponding target mapping in the catalog.</li>
      <li><strong>Authorization failure:</strong> the user lacks the business catalog group (BCG) or the start authorization for the app.</li>
      <li><strong>Inactive OData service:</strong> the backend service for the app is not activated in /IWFND/MAINT_SERVICE or /IWBEP/REG_SERVICE.</li>
      <li><strong>Stale app index:</strong> the UI5 application index in /UI2/AppIndexInfo does not reflect recent deployments.</li>
      <li><strong>Cache issue:</strong> the launchpad cache, browser cache, or CDN cache holds outdated metadata.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>/UI2/FLP</strong> — launchpad designer or content manager; inspect catalogs, groups, target mappings, and chip definitions.</li>
      <li><strong>/UI2/FLPD_CUST</strong> — Fiori launchpad designer for custom content.</li>
      <li><strong>/UI2/FLPD_CONF</strong> — Fiori launchpad designer for configuration content.</li>
      <li><strong>PFCG</strong> — role maintenance; verify business catalog groups and start authorizations.</li>
      <li><strong>/UI5/AppIndexInfo</strong> — UI5 application index; check for indexing errors.</li>
      <li><strong>/IWFND/MAINT_SERVICE</strong> — activate and test Gateway services.</li>
      <li><strong>/IWFND/ERROR_LOG</strong> — Gateway error log for failed service calls.</li>
      <li><strong>SU53</strong> — display authorization check values after a failed launch.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>/UI2/PB_C_CTG</strong> — catalog assignments.</li>
      <li><strong>/UI2/PB_C_GRP</strong> — group assignments.</li>
      <li><strong>/UI2/APPDESCR</strong> — app descriptor information.</li>
      <li><strong>/UI2/APPCHB</strong> — app index changelog.</li>
      <li><strong>/IWFND/I_MED_SRH</strong> — Gateway service repository metadata.</li>
      <li><strong>LPD_CUST</strong> — legacy launchpad content, sometimes still referenced.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Confirm the exact tile name, app ID, and the role assigned to the user.</li>
      <li>Check the catalog and group assignment in /UI2/FLPD_CUST or /UI2/FLPD_CONF.</li>
      <li>Verify the target mapping exists for the tile's semantic object and action.</li>
      <li>Run SU53 immediately after a failed launch to capture missing authorizations.</li>
      <li>Test the OData service in /IWFND/MAINT_SERVICE for the app's backend system.</li>
      <li>Check /UI5/AppIndexInfo for errors related to the app ID.</li>
      <li>Clear the launchpad personalization and browser cache if metadata appears stale.</li>
      <li>Review /IWFND/ERROR_LOG for service or navigation errors.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Assign the correct catalog and group to the user's PFCG role.</li>
      <li>Add the missing target mapping for the semantic object and action.</li>
      <li>Grant missing start authorization or business catalog group in PFCG.</li>
      <li>Activate the OData service in /IWFND/MAINT_SERVICE if it is inactive.</li>
      <li>Run the app index update report /UI5/APP_INDEX_CALCULATE for the affected app.</li>
      <li>Clear caches on the frontend server and ask the user to refresh the browser.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>Capture the user ID, role, tile name, app ID, semantic object/action, exact error message, browser and device type, and whether the issue is reproducible in a private browser window. Include screenshots of the launchpad if permitted.</p>

    <h2>Escalation signals</h2>
    <ul>
      <li>Many users across roles cannot access the launchpad at all.</li>
      <li>Multiple OData services are inactive or returning errors.</li>
      <li>App index calculation jobs are failing consistently.</li>
      <li>Navigation errors appear after a recent upgrade or support package.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame for launchpad content and access issues, not a UI5 development or Gateway architecture guide. It does not cover SAP Build Work Zone, SAP Cloud Portal, or custom UI5 controller debugging.</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
