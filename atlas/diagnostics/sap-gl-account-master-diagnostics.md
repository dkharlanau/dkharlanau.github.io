---
layout: default
title: "SAP GL Account Master Diagnostics"
description: "A conservative diagnostic frame for GL account master data, company code/global data, and field status issues in SAP."
permalink: /atlas/diagnostics/sap-gl-account-master-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Master data governance
concept_type: diagnostic guide
sap_area: "FI-GL"
business_process: Financial accounting
status: needs_verification
verified: false
level: 1
author: Dzmitryi Kharlanau
tags:
  - diagnostics
  - sap-ams
  - gl-account
related:
  - /atlas/diagnostics/sap-account-assignment-diagnostics/
  - /atlas/diagnostics/sap-company-code-data-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP GL Account Master Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP GL account master diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a G/L account cannot be posted to, extended, or used in account determination.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Financial accounting</dd></div>
      <div><dt>SAP area</dt><dd>FI-GL</dd></div>
      <div><dt>Indexing</dt><dd>Noindex, review candidate</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>G/L account master data is split between chart-of-accounts data and company-code-specific data. Posting failures often trace to missing company code assignments, field status conflicts, or open item management settings. The diagnostic task is to verify that the account exists for the relevant chart of accounts, is extended to the company code, and matches the posting key and field status group required by the transaction.</p>
    <p>This guide covers operational G/L account issues, not chart of accounts redesign or group reporting consolidation.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Posting fails with "G/L account is not defined in company code."</li>
      <li>Account assignment error: a required field such as cost center or profit center is hidden or optional.</li>
      <li>Line item display does not show open items for an account that should manage open items.</li>
      <li>Account determination in MM or SD picks an unexpected G/L account.</li>
      <li>Account is blocked for posting in the company code.</li>
      <li>Foreign currency valuation does not include the account.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing company code extension:</strong> the account exists in the chart of accounts but not for the company code.</li>
      <li><strong>Field status conflict:</strong> the account field status group and the posting key field status have conflicting requirements.</li>
      <li><strong>Account blocked:</strong> the account is flagged for deletion or blocked for posting.</li>
      <li><strong>Open item management mismatch:</strong> the account is set to line item display but not open item management.</li>
      <li><strong>Account type mismatch:</strong> the account category is not valid for the transaction.</li>
      <li><strong>Account determination wrong:</strong> the automatic account determination table points to an old or incorrect account.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>FS00</strong> — display or change G/L account master data centrally.</li>
      <li><strong>FSP0</strong> — chart of accounts data.</li>
      <li><strong>FSS0</strong> — company code data.</li>
      <li><strong>OB53</strong> — retained earnings account assignment.</li>
      <li><strong>FS10N</strong> — account balance and line item display.</li>
      <li><strong>SE16 / SE16N</strong> — table SKA1/SKB1 for mass checks.</li>
      <li><strong>OB62</strong> — chart of accounts assignment to company code.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>SKA1</strong> — chart of accounts segment (general data).</li>
      <li><strong>SKB1</strong> — company code segment.</li>
      <li><strong>SKAT</strong> — chart of accounts descriptions.</li>
      <li><strong>T077D</strong> — field status groups for G/L accounts.</li>
      <li><strong>TBSL</strong> — posting keys with field status groups.</li>
      <li><strong>TKA01</strong> — controlling area assignments relevant for account master.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Confirm the chart of accounts and company code from the error document.</li>
      <li>Open FS00 and verify the account exists for the chart of accounts and is extended to the company code.</li>
      <li>Check the account status flags: blocked for posting, marked for deletion, and open item management.</li>
      <li>Compare the account field status group with the posting key field status to find conflicts.</li>
      <li>Review account determination in the relevant module if the wrong account is selected.</li>
      <li>Check FS10N to confirm whether the account accepts postings and shows expected balances.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Extend the G/L account to the company code in FSS0 or FS00.</li>
      <li>Remove the posting block or deletion flag if the account must remain active.</li>
      <li>Adjust the field status group or posting key so required fields are consistent.</li>
      <li>Activate open item management if the account is a balance sheet account that requires clearing.</li>
      <li>Update automatic account determination to point to the correct account.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>Capture the G/L account number, company code, chart of accounts, exact error message, transaction code, posting key, account field status group, and whether the issue is isolated to one account or many accounts.</p>

    <h2>Escalation signals</h2>
    <ul>
      <li>Many G/L accounts are missing for a newly created company code.</li>
      <li>Field status conflicts block an entire account type or transaction group.</li>
      <li>Automatic account determination points to deleted accounts across multiple processes.</li>
      <li>Open item management is incorrectly set on many balance sheet accounts.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame for G/L account master data issues, not a guide to chart of accounts design, consolidation, or group reporting. It does not cover special G/L transactions or customer/vendor reconciliation accounts.</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
