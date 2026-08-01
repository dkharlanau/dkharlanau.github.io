---
layout: default
title: "About Dzmitryi Kharlanau — Senior SAP Consultant"
description: "Public profile of Dzmitryi Kharlanau: 12+ years across SAP SD, MM, logistics, MDG, integration, AMS, Automotive, Retail, and practical AI around SAP."
permalink: /about/
last_modified_at: 2026-07-25
profile_page: true
hide_global_cta: true
---

{% assign resume = site.data.resume %}
{% assign social_links = site.data.social.links %}

<div class="profile-canvas">
<section class="profile-canvas__hero" id="person" data-reveal>
  <div class="profile-canvas__hero-copy">
    <p class="profile-canvas__eyebrow">SAP consultant profile</p>
    <h1>Dzmitryi Kharlanau</h1>
    <p>Senior SAP consultant working across sales and logistics processes, master data, integration, AMS delivery, Automotive and Retail environments, and AI-supported work with controlled sources and human review.</p>
    <div class="profile-canvas__actions">
      <a class="profile-canvas__button" href="{{ resume.contact.linkedin }}" target="_blank" rel="noopener noreferrer">Discuss an SAP problem <span class="material-symbols-outlined" aria-hidden="true">north_east</span></a>
      <a class="profile-canvas__text-link" href="/services/">View services <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
    </div>
  </div>
  <div class="profile-canvas__portrait"><img src="/assets/img/DzmitryiKharlanau.webp" alt="Dzmitryi Kharlanau" width="720" height="720" fetchpriority="high" /><span aria-hidden="true"></span></div>
  <dl class="profile-canvas__facts">
    <div><dt>Current context</dt><dd>{{ resume.headline }} at <a href="https://www.epam.com" target="_blank" rel="noopener noreferrer">EPAM Systems</a></dd></div>
    <div><dt>Working scope</dt><dd>SD, MM, O2C, P2P, MDG-related work, master data, integration troubleshooting, AMS, and ABAP-backed analysis.</dd></div>
    <div><dt>Last reviewed</dt><dd>{{ page.last_modified_at | date: "%B %-d, %Y" }}</dd></div>
  </dl>
</section>

<section class="section profile-canvas__scope" data-reveal>
  <div class="section-shell">
    <header class="section-heading"><p class="eyebrow">Operating scope</p><h2>Business problems that cross SAP boundaries</h2></header>
    <div class="prose">
      <p>{{ resume.summary }}</p>
      <p>The work sits where a business process crosses SAP configuration, master data, custom logic, interfaces, and the support model. A blocked order, failed replication, or delayed invoice is rarely a single-module problem. The useful question is which decision, dependency, or control broke—and what evidence separates a local workaround from a durable fix.</p>
      <p>It suits work where teams need a functional lead who can define the failure with application, ABAP, integration, data, and operations colleagues.</p>
    </div>
  </div>
</section>

<section class="section profile-canvas__approach" data-reveal>
  <div class="section-shell">
    <header class="section-heading"><p class="eyebrow">Operating approach</p><h2>How SAP problems are approached</h2></header>
    <div class="process-rail" aria-label="Four-step diagnostic approach">
      <div class="process-rail__step"><strong>1. Make the failure concrete</strong><span>Start with a blocked business outcome, not a technology label.</span></div>
      <div class="process-rail__step"><strong>2. Trace dependencies</strong><span>Follow process, master data, configuration, enhancement, and interface boundaries.</span></div>
      <div class="process-rail__step"><strong>3. Separate evidence from assumption</strong><span>Distinguish confirmed facts, missing evidence, and landscape-specific decisions.</span></div>
      <div class="process-rail__step"><strong>4. Leave a reusable artefact</strong><span>Turn the result into an owner decision, runbook, backlog item, or control.</span></div>
    </div>
    <div class="prose"><p>Avoid fixes that only improve the appearance of control: green SLAs while the same incidents recur, dashboards without an accountable recovery path, AI pilots without a usable knowledge layer, or “clean core” work that moves unowned complexity elsewhere. The result should be a bounded change with an owner, evidence, and a recovery path.</p></div>
  </div>
</section>

<section class="section profile-canvas__domains" data-reveal>
  <div class="section-shell">
    <header class="section-heading"><p class="eyebrow">Where experience connects</p><h2>Domains that meet in real delivery work</h2></header>
    <div class="evidence-grid">
      <article class="evidence-card"><h3>Commercial and logistics flow</h3><p>SD, O2C, delivery, billing, pricing, inventory-facing logistics, and the operational controls around them.</p></article>
      <article class="evidence-card"><h3>Procurement and data</h3><p>MM, P2P touchpoints, Business Partner and MDG-related work, replication, data quality, and governance boundaries.</p></article>
      <article class="evidence-card"><h3>Integration and architecture</h3><p>IDoc, RFC, web services, APIs, OData, AIF, event-driven patterns, interface ownership, and recoverability.</p></article>
      <article class="evidence-card"><h3>Operations and change</h3><p>AMS-heavy delivery, incident diagnosis, ABAP-backed troubleshooting, testing, handover, operational memory, and side-by-side automation.</p></article>
    </div>
    <p class="lead">Industry context in the public record includes Automotive, Retail and apparel, Manufacturing, and IT services and consulting.</p>
  </div>
</section>

<section class="section profile-canvas__outputs" data-reveal>
  <div class="section-shell">
    <header class="section-heading"><p class="eyebrow">What a manager can expect</p><h2>Useful outputs, not generic advice</h2></header>
    <div class="deliverable-grid">
      <article class="deliverable-card"><h3>Diagnostic brief</h3><p>A clear statement of the business symptom, scope boundary, evidence needed, likely failure classes, and open decisions.</p></article>
      <article class="deliverable-card"><h3>Decision and ownership map</h3><p>A practical view of who owns the business outcome, data, integration contract, technical control, and recovery action.</p></article>
      <article class="deliverable-card"><h3>Prioritised improvement backlog</h3><p>Actions separated into immediate control fixes, process or data work, architecture decisions, and longer-term investment.</p></article>
      <article class="deliverable-card"><h3>Reusable operational memory</h3><p>Runbook, KEDB, evidence checklist, or review pattern that reduces rediscovery during future support and change work.</p></article>
    </div>
  </div>
</section>

<section class="section profile-canvas__record" data-reveal>
  <div class="section-shell">
    <header class="section-heading"><p class="eyebrow">Career path</p><h2>Roles represented in the public dataset</h2></header>
    <div class="profile-list">
      {% for item in resume.experience limit: 6 %}
      <article class="profile-list__item">
        <h3>{{ item.title }}</h3>
        <p>{% if item.url %}<a href="{{ item.url }}" target="_blank" rel="noopener noreferrer">{{ item.company }}</a>{% else %}{{ item.company }}{% endif %} · {{ item.start }}{% if item.current %} to present{% elsif item.end %} to {{ item.end }}{% endif %}</p>
        <p>{{ item.summary }}</p>
      </article>
      {% endfor %}
    </div>
    <p><a class="link-arrow" href="/cv/">Read the full public CV</a></p>
  </div>
</section>

<section class="section profile-canvas__evidence" data-reveal>
  <div class="section-shell">
    <header class="section-heading"><p class="eyebrow">Evidence routes</p><h2>How to examine the positioning</h2></header>
    <div class="decision-table"><table><thead><tr><th>Question</th><th>Public evidence</th></tr></thead><tbody>
      <tr><td>What roles and domains are on record?</td><td><a href="/cv/">CV</a> and the canonical <a href="/ai/resume.yml">resume dataset</a>.</td></tr>
      <tr><td>How does the diagnostic approach translate into practice?</td><td><a href="/services/">Service entry points</a>, <a href="/scenarios/">business scenarios</a>, and the <a href="/atlas/">Knowledge Atlas</a>.</td></tr>
      <tr><td>What has been published publicly?</td><td><a href="/publications/">Publications</a> and <a href="/datasets/">datasets</a>.</td></tr>
      <tr><td>Which credentials are linkable?</td><td><a href="/education/">Education and credentials</a> and the public profile audit.</td></tr>
    </tbody></table></div>
  </div>
</section>

<section class="section profile-canvas__credentials" data-reveal>
  <div class="section-shell">
    <header class="section-heading"><p class="eyebrow">Selected credentials</p><h2>Publicly linkable credentials</h2></header>
    <div class="profile-list">
      {% for cert in resume.certifications limit: 8 %}
      <article class="profile-list__item"><h3>{{ cert.name }}</h3><p>{{ cert.issuer }}{% if cert.issued %} · {{ cert.issued }}{% endif %}</p>{% if cert.url %}<p><a href="{{ cert.url }}" target="_blank" rel="noopener noreferrer">Open credential</a></p>{% endif %}</article>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section profile-canvas__writing" data-reveal>
  <div class="section-shell">
    <header class="section-heading"><p class="eyebrow">Public writing</p><h2>Selected published work</h2></header>
    <div class="profile-list">
      {% for publication in resume.publications %}
      <article class="profile-list__item"><h3>{{ publication.name }}</h3><p>{{ publication.publisher }}{% if publication.published %} · {{ publication.published | date: "%B %-d, %Y" }}{% endif %}</p><p><a href="{{ publication.url }}" target="_blank" rel="noopener noreferrer">Open source</a></p></article>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section profile-canvas__verification" data-reveal>
  <div class="section-shell">
    <header class="section-heading"><p class="eyebrow">Verification detail</p><h2>Machine-readable sources and profiles</h2></header>
    <div class="profile-grid">
      <article class="profile-card"><h3>Canonical resume data</h3><p>Public subset of profile data for retrieval and verification.</p><p><a href="/ai/resume.yml">Resume YAML</a> · <a href="/ai/resume.json">Resume JSON</a></p></article>
      <article class="profile-card"><h3>Audit registry</h3><p>Confidence levels, credential registry, publication themes, and verification issues.</p><p><a href="/ai/profile-audit.json">Profile audit JSON</a></p></article>
      <article class="profile-card"><h3>LLM access manifest</h3><p>Retrieval guidance for AI systems and links to canonical public surfaces.</p><p><a href="/llms.txt">llms.txt</a></p></article>
    </div>
    <p>The source-of-truth audit for confidence levels and credential status is available at <a href="/ai/profile-audit.json">/ai/profile-audit.json</a>. These files support verification; the sections above are intended for a manager assessing fit.</p>
  </div>
</section>

<section class="section profile-canvas__profiles" data-reveal>
  <div class="section-shell">
    <header class="section-heading"><p class="eyebrow">Profiles</p><h2>External identity links</h2></header>
    <div class="profile-chip-links">{% for link in social_links %}<a href="{{ link.url }}" target="_blank" rel="noopener noreferrer">{{ link.label }}</a>{% endfor %}</div>
  </div>
</section>
</div>
