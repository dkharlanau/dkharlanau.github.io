---
layout: default
title: "SAP Output and Message Control Diagnostics"
description: "A conservative diagnostic frame for output determination and message control issues in SAP."
permalink: /atlas/diagnostics/sap-output-message-control-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration and interfaces
concept_type: diagnostic guide
sap_area: "S/4HANA Output Control / classic output determination"
business_process: Integration
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - integration
  - sap-sd
  - diagnostics
  - output-determination
related:
  - /atlas/diagnostics/idoc-aif-integration-diagnostics/
  - /atlas/diagnostics/sap-inbound-processing-diagnostics/
  - /atlas/diagnostics/sap-outbound-processing-diagnostics/
  - /atlas/diagnostics/sap-idoc-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Output and Message Control Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP output and message control diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a document output (print, email, IDoc, fax) was not created, not sent, or sent to the wrong recipient.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Integration</dd></div>
      <div><dt>SAP area</dt><dd>Output determination / NAST</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until output determination behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>First question: which output framework owns the document?</h2>
    <p>Before opening NACE, NAST, BRFplus, SOST, or a spool monitor, identify the framework. SAP S/4HANA Sales can use either classic Output Determination (SD-BF-OC) or SAP S/4HANA Output Control for the application object type <code>Sales_Document</code>. A framework change applies to new documents; existing documents remain with the framework that was active when they were created.</p>

    <div class="table-wrap" role="region" aria-label="Output diagnostic branch" tabindex="0">
      <table>
        <thead><tr><th>If the document uses...</th><th>Start with...</th><th>Do not assume...</th></tr></thead>
        <tbody>
          <tr><td>Classic output determination</td><td>Output condition technique, message record, partner/medium, NAST processing</td><td>That BRFplus decision tables control this document</td></tr>
          <tr><td>SAP S/4HANA Output Control</td><td>Output item, Output Parameter Determination, receiver/channel/relevance/form, then technical processing</td><td>That NACE or a missing NAST record explains the failure</td></tr>
        </tbody>
      </table>
    </div>

    <p>For the modern framework, trace the layers in this order: <strong>framework → output type → receiver → channel → output relevance → form → technical processing</strong>. Use the dedicated <a href="/atlas/sap/output-control/">SAP S/4HANA Output Control guide</a> for configuration and decision-table logic.</p>

    <h2>Core idea</h2>
    <p>An output incident can fail in three different places: <strong>determination</strong> (what should be produced and for whom), <strong>business relevance</strong> (whether the document is allowed to issue the output), or <strong>technical processing</strong> (rendering and delivery through print, email, or integration). The exact configuration objects depend on the active output framework.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Expected printout, email, or IDoc was not generated for a sales or purchase document.</li>
      <li>Output was created but remains in status 'not processed' or 'error'.</li>
      <li>Email was sent to the wrong address or with wrong attachment.</li>
      <li>IDoc output was generated but the partner reports it never arrived.</li>
      <li>Multiple outputs were created for the same document unexpectedly.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Wrong framework assumption:</strong> the consultant checks NAST while the document uses S/4HANA Output Control, or checks BRFplus while the document uses classic output determination.</li>
      <li><strong>Determination rule not matched:</strong> document attributes do not satisfy the expected classic condition record or modern decision-table rule.</li>
      <li><strong>Wrong receiver or channel:</strong> partner data, rule order, or non-exclusive rules produce an unexpected target or multiple outputs.</li>
      <li><strong>Output not relevant:</strong> in S/4HANA Output Control, business status checks can keep an output item in preparation.</li>
      <li><strong>Form or rendering error:</strong> the selected template, data source, form logic, or Adobe rendering fails.</li>
      <li><strong>Communication issue:</strong> spool, mail, EDI/SOA, or another channel fails after determination was already correct.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <h3>SAP S/4HANA Output Control</h3>
    <ul>
      <li>Check the output items and determined parameters in the business document or relevant output UI.</li>
      <li>Use <strong>Output Parameter Determination</strong> to inspect and simulate the relevant decision step.</li>
      <li>Check Output Relevance before treating a prepared item as a technical send failure.</li>
      <li>Then move to the selected channel: spool/print, mail transmission, EDI/SOA, or form rendering.</li>
    </ul>

    <h3>Classic output determination</h3>
    <ul>
      <li>NACE and application-specific output Customizing — condition-technique design.</li>
      <li>Application-specific condition records — verify the key that should determine the message.</li>
      <li>NAST — message existence, processing status, timing, and error context.</li>
      <li>SP01 / SOST — print and email processing where applicable.</li>
      <li>WE02 / WE05 — IDoc processing when classic message output creates an IDoc.</li>
    </ul>

    <h2>Key objects</h2>
    <p>Do not expect one shared runtime table for both frameworks. In the classic branch, <strong>NAST</strong> is a key message-control object and <strong>TNAPR</strong> links output types to processing programs/forms. In S/4HANA Output Control, diagnose the output item and its determined parameters instead of treating a missing NAST record as proof of failure.</p>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the business document, expected output type, receiver, channel, and timing.</li>
      <li>Prove which output framework owns this document.</li>
      <li>If it uses S/4HANA Output Control, compare the actual output item with the expected decision-table results: output type → receiver → channel → relevance → form.</li>
      <li>If it uses classic output determination, prove message determination through the relevant condition technique and message record.</li>
      <li>Only after determination is correct, move to technical processing: rendering, spool, mail, EDI/IDoc/SOA, or another supported channel.</li>
      <li>Prove final delivery and record whether the failure affected one document, one partner, one rule, or the whole channel.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Correct the matching rule: classic condition record or S/4HANA decision-table condition.</li>
      <li>Correct receiver/partner or address data when determination points to the wrong party.</li>
      <li>Fix rule order or the Exclusive setting when several modern rules match unexpectedly.</li>
      <li>Correct Output Relevance when a valid output item is blocked by the wrong status logic.</li>
      <li>Fix the selected form/template or rendering logic when determination is correct but the document is wrong.</li>
      <li>Resolve channel infrastructure only after the functional parameters are proven.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>A useful output ticket should include the document number, active output framework, expected output type, expected receiver/channel, actual output-item or message status, error text, and whether the issue is isolated or recurring. This prevents a classic NAST incident and a modern Output Control incident from being investigated with the same checklist.</p>

    <h2>Purchase order output troubleshooting: classic branch example</h2>
    <p>The checklist below is specifically for a purchasing scenario that uses classic NAST-based message determination. Do not apply it to a purchase order that uses SAP S/4HANA Output Management. When a supplier reports they did not receive a purchase order, first prove the active framework, then trace output from determination through processing to delivery.</p>
    <ul>
      <li><strong>Check output determination (NACE):</strong> verify that the output type for purchase orders is active for the document type and purchasing organization.</li>
      <li><strong>Check condition records (VV23):</strong> confirm that an output condition record exists for the supplier, document type, and output medium (print, email, EDI, Business Network).</li>
      <li><strong>Check NAST table:</strong> review the output message status. Status 0 = not processed, 1 = successfully processed, 2 = error.</li>
      <li><strong>Check SOST for email:</strong> if the medium is email, SOST shows send status, recipient address, and any delivery errors.</li>
      <li><strong>Check SP01 for print:</strong> if the medium is print, SP01 shows spool requests and printer status.</li>
      <li><strong>Check WE02 for EDI:</strong> if the medium is EDI or IDoc, WE02 shows IDoc generation status and any segment errors.</li>
      <li><strong>Check partner master:</strong> the supplier master (LFA1/LFB1) must have correct communication data for the chosen medium.</li>
    </ul>
    <p>A useful PO output ticket should include: PO number, output type, expected medium, supplier number, NAST status, error text if any, and whether the issue affects one supplier or multiple suppliers.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a complete configuration guide. The detailed S/4HANA decision-table model, channel assignment, callback-class boundary, form selection, and technical prerequisites are explained in the <a href="/atlas/sap/output-control/">Output Control guide</a>. Classic condition-technique design remains a separate branch.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>

    <h2>Next diagnostic steps</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-interface-monitoring-diagnostics/">SAP Interface Monitoring Diagnostics</a> — use this when output failures appear alongside broader interface symptoms.</li>
      <li><a href="/atlas/diagnostics/sap-inbound-processing-diagnostics/">SAP Inbound Processing Diagnostics</a> — go here when the failing output is an inbound message.</li>
      <li><a href="/atlas/diagnostics/sap-outbound-processing-diagnostics/">SAP Outbound Processing Diagnostics</a> — check this when the failing output is an outbound message.</li>
      <li><a href="/atlas/diagnostics/sap-spool-output-diagnostics/">SAP Spool and Print Output Diagnostics</a> — use this for print-specific failures.</li>
      <li><a href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">IDoc and AIF Integration Diagnostics</a> — go here when the output medium is IDoc or EDI.</li>
    </ul>

    <h2>Practical checklist</h2>
    <div markdown="1">
- [ ] Collect document number, output type, expected medium, partner/supplier, and NAST status. **Synthetic example:** PO 1234567890, output NEU, medium 6, partner TEST_VENDOR_01.

- [ ] Check the document output screen (VF03/ME23N) and NAST for status and error text.

- [ ] Verify output condition records (VV33/VV23) and output type activation (NACE).

- [ ] Check SOST for email errors, SP01 for spool issues, or WE02 for IDoc output.

- [ ] Confirm partner master communication data matches the chosen medium.

- [ ] Document whether the issue is isolated to one document, partner, or output type.

- [ ] Safety limit: do not resend IDoc or email output to a production partner before confirming the original failure cause.
</div>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">Idoc Aif Integration Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-inbound-processing-diagnostics/">SAP Inbound Processing Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-outbound-processing-diagnostics/">SAP Outbound Processing Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-spool-output-diagnostics/">SAP Spool and Print Output Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
