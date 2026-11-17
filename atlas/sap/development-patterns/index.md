---
layout: default
title: "SAP Development Pattern Library — 150+ Design and Programming Patterns"
description: "A practical design-pattern dictionary for ABAP, RAP and CAP: Specification, Command, Strategy, Factory, State, integration reliability, examples, trade-offs and architecture specification language."
permalink: /atlas/sap/development-patterns/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-17
hide_global_cta: true
tags: [sap, abap, rap, cap, clean-core, design-patterns, programming-patterns, architecture]
related:
  - /labs/enterprise-context/development/
  - /atlas/sap/rap/
  - /atlas/sap/abap-cloud/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Pattern Library</li>
  </ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero">
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">SAP Development / Pattern Language</p>
      <h1>Give the design a name.<br>Then explain the trade-off.</h1>
      <p>A practical programming-pattern dictionary for ABAP, RAP and CAP. Begin with the recurring problem, choose a pattern, name the interfaces and classes, and document what the pattern must <em>not</em> do.</p>
      <p><a class="research-canvas__button" href="#pattern-catalog">Browse patterns <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a></p>
    </div>
    <div class="research-canvas__signal" aria-label="Catalog scope">
      <p>Design vocabulary</p>
      <div class="research-canvas__signal-line"><span>{{ site.data.development_patterns.patterns.size }}</span><strong>Patterns &amp; idioms</strong><small>Short, practical entries</small></div>
      <div class="research-canvas__signal-line"><span>08</span><strong>Families</strong><small>From GoF to SAP implementation</small></div>
      <div class="research-canvas__signal-line"><span>26</span><strong>Deep dives</strong><small>Implementation specifications</small></div>
      <em>Working reference · pending editorial verification</em>
    </div>
  </header>

  <section class="research-canvas__boundary" aria-label="Classification boundary">
    <span class="material-symbols-outlined" aria-hidden="true">category</span>
    <p><strong>Not all names describe the same level of design.</strong> GoF patterns are object-level design solutions. DDD/PoEAA patterns shape domain and data ownership. Enterprise Integration Patterns shape messaging. RAP and CAP idioms explain where to apply those ideas inside SAP framework contracts. We label each family rather than pretending all entries are GoF patterns.</p>
  </section>

  <section class="research-canvas__inventory" id="choose-pattern">
    <header>
      <p class="research-canvas__eyebrow">Fast selection</p>
      <h2>Which problem do you actually have?</h2>
      <p>A pattern is useful when it reduces a recurring design risk—not when it makes a three-line function look sophisticated.</p>
    </header>
    <div class="table-scroll study-table" role="region" tabindex="0" aria-label="Programming pattern chooser">
      <table class="study-table__table">
        <thead><tr><th scope="col">I need to…</th><th scope="col">Start with</th><th scope="col">Distinguishing question</th></tr></thead>
        <tbody>
          <tr><td>Compose reusable yes/no business rules</td><td><a href="/atlas/sap/development-patterns/specification/">Specification</a></td><td>Is the output a decision, with no side effects?</td></tr>
          <tr><td>Turn an operation into a named executable object</td><td><a href="/atlas/sap/development-patterns/command/">Command</a></td><td>Do we need dispatch, audit, retry, queueing or undo?</td></tr>
          <tr><td>Switch between several algorithms</td><td><a href="/atlas/sap/development-patterns/strategy-policy/">Strategy</a></td><td>Is the choice about <em>how</em> to do one job?</td></tr>
          <tr><td>Try handlers in priority order</td><td><a href="/atlas/sap/development-patterns/chain-of-responsibility/">Chain of Responsibility</a></td><td>Can one handler decline and pass the request on?</td></tr>
          <tr><td>Control lifecycle transitions</td><td><a href="/atlas/sap/development-patterns/state/">State</a></td><td>Are actions legal in some states but not others?</td></tr>
          <tr><td>Translate incompatible models</td><td><a href="/atlas/sap/development-patterns/adapter/">Adapter</a> / <a href="/atlas/sap/development-patterns/anti-corruption-layer/">Anti-Corruption Layer</a></td><td>Just an API shape mismatch—or a semantic mismatch?</td></tr>
          <tr><td>Prevent duplicate integration effects</td><td><a href="/atlas/sap/development-patterns/idempotent-consumer/">Idempotent Consumer</a></td><td>What identifies one logical operation across retries?</td></tr>
          <tr><td>Keep SAP transactional logic safe</td><td><a href="/atlas/sap/development-patterns/thin-rap-handler/">Thin RAP Handler</a> / <a href="/atlas/sap/development-patterns/unit-of-work/">Unit of Work</a></td><td>Who owns commit and rollback in this runtime?</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="architecture-specification">
    <header>
      <p class="research-canvas__eyebrow">Write it into the technical specification</p>
      <h2>One shared vocabulary for architects and developers.</h2>
      <p>Keep the specification short enough to review. Name the design intention, the SAP entry point and the contract.</p>
    </header>

    <pre><code>Context: Inbound business-partner message
Intent: Normalize, decide, then execute
Patterns: Adapter + Specification + Strategy + Command
Entry point: Inbound adapter / permitted extension point
Interfaces:
  ZIF_MSG_NORMALIZER=&gt;NORMALIZE( )
  ZIF_BP_SPECIFICATION=&gt;IS_SATISFIED_BY( )
  ZIF_ORG_STRATEGY=&gt;TRANSFORM( )
  ZIF_BP_COMMAND=&gt;EXECUTE( )
Application service:
  ZCL_BP_INBOUND_PROCESSOR=&gt;PROCESS( )
Persistence:
  ZIF_BP_GATEWAY (released API or supported legacy contract)
Configuration:
  Mapping registry + explicit fallback and missing-value behavior
Transaction owner:
  Framework/service boundary; no hidden COMMIT in rules
Failure contract:
  Log correlation, preserve business errors, reject unknown mappings
Tests:
  Specification truth table; strategy selection; command idempotency</code></pre>

    <p><strong>Important:</strong> The names above illustrate a design, not copy-paste SAP APIs or a documented customer implementation. In RAP, the behavior implementation contract governs which operations are permitted. ABAP Cloud requires checking the release state of APIs. Do not silently carry classic ABAP techniques into a restricted runtime.</p>
  </section>

  <section class="research-canvas__inventory" id="pattern-catalog">
    <header>
      <p class="research-canvas__eyebrow">Full catalog · {{ site.data.development_patterns.patterns.size }} entries</p>
      <h2>Search by name, problem or SAP use case.</h2>
      <p>Each entry says what the pattern solves, where it fits and when it is the wrong choice. Selected patterns link to deeper implementation specifications.</p>
    </header>
    <div class="table-scroll" role="group" aria-label="Catalog controls">
      <label for="pattern-search">Find a pattern</label>
      <input id="pattern-search" type="search" placeholder="Try: IDoc, Command, validation, mapping, retry…" autocomplete="off" aria-controls="pattern-results" />
      <label for="pattern-group">Family</label>
      <select id="pattern-group" aria-controls="pattern-results">
        <option value="">All families</option>
        {% for group in site.data.development_patterns.groups %}
        <option value="{{ group.id }}">{{ group.title }}</option>
        {% endfor %}
      </select>
      <p id="pattern-count" role="status" aria-live="polite">{{ site.data.development_patterns.patterns.size }} entries. Search requires JavaScript; all rows are visible without it.</p>
    </div>
    <div id="pattern-results">
    {% for group in site.data.development_patterns.groups %}
      {% assign items = site.data.development_patterns.patterns | where: "category", group.id %}
      <section data-pattern-group="{{ group.id }}" aria-labelledby="group-{{ group.id }}">
        <h3 id="group-{{ group.id }}">{{ group.title }} · {{ items.size }}</h3>
        <p>{{ group.description }}</p>
        <div class="table-scroll study-table" role="region" tabindex="0" aria-label="{{ group.title }} patterns">
          <table class="study-table__table">
            <thead><tr><th scope="col">Pattern</th><th scope="col">Problem and solution</th><th scope="col">Example in SAP</th><th scope="col">Avoid when…</th></tr></thead>
            <tbody>
            {% for pattern in items %}
              <tr id="pattern-{{ pattern.slug }}" data-pattern-row data-pattern-category="{{ group.id }}" data-pattern-search="{{ pattern.name | escape }} {{ pattern.problem | escape }} {{ pattern.solution | escape }} {{ pattern.sap_example | escape }} {{ pattern.pitfall | escape }}">
                <th scope="row">
                {% if pattern.profile %}
                  <a href="{{ pattern.profile | relative_url }}">{{ pattern.name }}</a> <small>↗</small>
                {% else %}
                  {{ pattern.name }}
                {% endif %}
                </th>
                <td>{{ pattern.problem }} <strong>Approach:</strong> {{ pattern.solution }}</td>
                <td>{{ pattern.sap_example }}</td>
                <td>{{ pattern.pitfall }}</td>
              </tr>
            {% endfor %}
            </tbody>
          </table>
        </div>
        <p><small>Family: {{ group.family }} · <a href="{{ group.source }}" rel="noopener noreferrer">Background reference</a></small></p>
      </section>
    {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="featured-specifications">
    <header>
      <p class="research-canvas__eyebrow">Implementation specifications</p>
      <h2>Start with a concrete case and class contract.</h2>
      <p>The deeper pages explain class roles, method signatures, code sketches, trade-offs, tests and how to reference the pattern in a development specification.</p>
    </header>
    <div class="research-route-list">
      <a href="/atlas/sap/development-patterns/specification/"><span>DP-01</span><strong>Specification</strong><small>Turn a business eligibility rule into a reusable yes/no question.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/command/"><span>DP-02</span><strong>Command</strong><small>Represent an operation as an object with one execution contract.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/chain-of-responsibility/"><span>DP-03</span><strong>Chain of Responsibility</strong><small>Try a defined sequence of handlers until one can answer.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/state/"><span>DP-04</span><strong>State</strong><small>Model legal behavior and transitions around lifecycle state.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/adapter/"><span>DP-05</span><strong>Adapter</strong><small>Provide one business-facing interface over incompatible provider contracts.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/decorator/"><span>DP-06</span><strong>Decorator</strong><small>Add logging, metrics or policy around a service without rewriting it.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/factory-method/"><span>DP-07</span><strong>Factory Method</strong><small>Centralize creation of interchangeable implementations.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/unit-of-work/"><span>DP-08</span><strong>Unit of Work</strong><small>Coordinate one logical change set at its legitimate transaction boundary.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/test-data-builder/"><span>DP-09</span><strong>Test Data Builder</strong><small>Make tests show the business difference, not 40 fields of fixture setup.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/thin-rap-handler/"><span>DP-10</span><strong>Thin RAP Handler</strong><small>Keep behavior handlers about framework contracts; delegate pure business rules.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/thin-entry-point/"><span>SDP-01</span><strong>Thin Entry Point</strong><small>A BAdI, user exit or IDoc hook should route work, not become the application.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/strategy-policy/"><span>SDP-02</span><strong>Strategy / Policy Resolver</strong><small>Replace a forest of country, channel or organization CASE branches with named policies.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/repository-and-dependency-injection/"><span>SDP-03</span><strong>Repository + Dependency Injection</strong><small>Hide database and SAP API calls behind a testable boundary.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/anti-corruption-layer/"><span>SDP-04</span><strong>Anti-Corruption Layer (ACL)</strong><small>Translate legacy or external meanings once, before they reach core rules.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/delta-aware-merge/"><span>SDP-05</span><strong>Delta-Aware Merge / Patch Semantics</strong><small>A missing field, an explicitly cleared field and a deleted segment must not mean the same thing.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/decision-table/"><span>SDP-06</span><strong>Decision Table / Rules as Data</strong><small>When the business owns many combinations, stop encoding them as nested IF statements.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/released-api-boundary/"><span>SDP-07</span><strong>Released API Boundary (Clean Core)</strong><small>Depend on an intentional SAP contract, not on a convenient internal table or implementation detail.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/managed-rap-business-object/"><span>SDP-08</span><strong>Managed RAP Business Object</strong><small>Let the RAP runtime own ordinary persistence, locking and transactional plumbing for custom data.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/unmanaged-rap-facade/"><span>SDP-09</span><strong>Unmanaged RAP Facade</strong><small>Modernize the service contract around proven transactional logic without rewriting the engine first.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/behavior-rule-placement/"><span>SDP-10</span><strong>RAP Validation vs Determination vs Action</strong><small>Use the RAP behavior concept that matches the business meaning.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/draft-workflow/"><span>SDP-11</span><strong>RAP Draft Workflow</strong><small>Separate 'I am editing' from 'the active business state has changed'.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/cap-service-facade/"><span>SDP-12</span><strong>CAP Service Facade</strong><small>Expose a purpose-built service contract instead of publishing the database model verbatim.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/cap-event-handler/"><span>SDP-13</span><strong>CAP Event Handler / Lifecycle Hook</strong><small>Add custom logic around CAP's service events while keeping the service contract in charge.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/idempotent-consumer/"><span>SDP-14</span><strong>Idempotent Consumer</strong><small>A retry must not create a second business effect.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/transactional-outbox/"><span>SDP-15</span><strong>Transactional Outbox / Commit-Then-Publish</strong><small>Never claim an event was delivered just because business code reached its last line.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      <a href="/atlas/sap/development-patterns/retry-and-dead-letter/"><span>SDP-16</span><strong>Retry + Dead Letter / Quarantine</strong><small>Retry a temporary outage; quarantine bad data; never run an infinite retry storm.</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="architecture-review-template">
    <header><p class="research-canvas__eyebrow">Common language</p><h2>Write the pattern into an architecture decision.</h2><p>A name helps only when the transaction owner, contract, rejected alternative and acceptance tests are explicit.</p></header>
    <div class="research-route-list">
      <a href="/atlas/sap/development-patterns/design-review/"><span>ADR</span><strong>Design review template</strong><small>Copy a structured architecture decision with context, failure model, alternatives and test contract.</small><i class="material-symbols-outlined" aria-hidden="true">article</i></a>
      <a href="/atlas/sap/development-patterns/manifest.json"><span>JSON</span><strong>16 worked patterns manifest</strong><small>Stable pattern IDs and canonical detail URLs for developer tools and assistants.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="pattern-selection-review">
    <header>
      <p class="research-canvas__eyebrow">Architecture review</p>
      <h2>Five questions before approving a pattern.</h2>
    </header>
    <ol>
      <li><strong>Variation:</strong> What actually changes—algorithm, rule, state, operation, data source or transport?</li>
      <li><strong>Ownership:</strong> Which class owns the invariant and which runtime owns the transaction?</li>
      <li><strong>Boundary:</strong> Is this a released SAP API, BAdI, RAP BO contract or side-by-side API?</li>
      <li><strong>Failure:</strong> What happens on duplicate, timeout, partial failure and missing configuration?</li>
      <li><strong>Proof:</strong> Can ABAP Unit or contract tests demonstrate the behavior without the real remote system?</li>
    </ol>
  </section>

  <section class="research-canvas__inventory" id="patterns-references">
    <header><p class="research-canvas__eyebrow">Evidence and scope</p><h2>Reference families, not invented standards.</h2></header>
    <p>Definitions and examples here are original summaries and synthetic SAP scenarios. GoF, PoEAA, EIP, DDD, cloud resilience, and SAP runtime idioms are intentionally labeled separately. Validate exact framework behavior against the target product version and released APIs before using an example in production.</p>
    <ul>
      <li><a href="https://refactoring.guru/design-patterns/catalog">GoF design pattern catalog</a> — classification and terminology.</li>
      <li><a href="https://www.martinfowler.com/eaaCatalog/index.html">Patterns of Enterprise Application Architecture</a> — domain, persistence, application boundaries.</li>
      <li><a href="https://www.enterpriseintegrationpatterns.com/patterns/messaging/index.html">Enterprise Integration Patterns</a> — routing, message transformation and reliability.</li>
      <li><a href="https://learn.microsoft.com/azure/architecture/patterns/">Azure Architecture Center patterns</a> — resilience and migration trade-offs.</li>
      <li><a href="https://github.com/SAP/styleguides/blob/main/clean-abap/CleanABAP.md">SAP Clean ABAP</a> — ABAP naming, responsibilities, injection, testing.</li>
      <li><a href="https://help.sap.com/docs/abap-cloud/abap-rap/rap-business-object-contract">SAP RAP Business Object Contract</a> — handler and save-sequence boundaries.</li>
      <li><a href="https://help.sap.com/docs/abap-cloud/abap-rap/validations">SAP RAP validations</a> — no EML modify inside validations.</li>
      <li><a href="https://cap.cloud.sap/docs/node.js/core-services">SAP CAP Core Services</a> — <code>before</code>, <code>on</code>, <code>after</code> handlers.</li>
    </ul>
    <p><small>Publication maturity: working reference, pending editorial verification. This independent personal knowledge base is not official SAP guidance.</small></p>
  </section>
  <div class="research-canvas__support">
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
<script src="{{ '/assets/pattern-library.js' | relative_url }}" defer></script>
