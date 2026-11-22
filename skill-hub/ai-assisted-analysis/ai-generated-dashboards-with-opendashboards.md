---
layout: default
title: "Build AI-Generated Operational Dashboards with OpenDashboards"
description: "A practical OpenDashboards skill: create a live dashboard from synthetic data, assess the OpenUI Cloud boundary, and design a safe SAP migration-monitoring pilot."
permalink: /skill-hub/ai-assisted-analysis/ai-generated-dashboards-with-opendashboards/
last_modified_at: 2026-11-22
author: "Dzmitryi Kharlanau"
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
hide_global_cta: true
tags: [ai, data-analytics, dashboards, sap, integration, architecture, skills]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/ai-assisted-analysis/">AI-Assisted Analysis</a></li>
    <li aria-current="page">AI-Generated Dashboards</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub · AI-Assisted Analysis · Practical tool study</p>
  <h1>Build a useful dashboard by asking a question</h1>
  <p class="lead">OpenDashboards lets you explore connected data in natural language and turn the result into a live, editable dashboard. The useful skill is not prompting for attractive charts. It is defining trustworthy metrics, controlled data access, and a view that helps someone act.</p>
  <p><strong>Start here:</strong> <a href="https://opendashboards.com/">OpenDashboards</a> · <a href="https://github.com/thesysdev/opendashboards">Open-source repository</a> · <a href="https://www.youtube.com/watch?v=ypLpjnnHSZw">Video that prompted this study</a>. This is an independent practical analysis based on the current project README and OpenUI documentation, not a verified transcript of the video.</p>

  <section>
    <h2>1. What this skill is for</h2>
    <p>You have operational data in a database, but every new management question seems to require another BI ticket. Use this skill to build a <strong>read-only exploration dashboard</strong>, check the numbers against source queries, and decide whether the result deserves a permanent reporting solution.</p>
    <p><strong>Target outcome:</strong> a working synthetic dashboard, an explicit metric definition, a documented data-access boundary, and a go/no-go decision for a pilot.</p>
  </section>

  <section>
    <h2>2. Understand the product boundary</h2>
    <p><strong>OpenDashboards</strong> is the MIT-licensed application. It connects to supported sources and provides a chat-led workflow. <strong>OpenUI Dashboards API / OpenUI Cloud</strong> is the service used to build and retain dashboards and conversations. Self-hosting the application does <em>not</em> automatically make the full solution local-only.</p>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="OpenDashboards responsibilities and limits">
      <table class="study-table__table">
        <thead><tr><th>Layer</th><th>What it does</th><th>What you still own</th></tr></thead>
        <tbody>
          <tr><td>Data source</td><td>Stores operational records</td><td>Quality, timestamps, data classification, least-privilege access</td></tr>
          <tr><td>OpenDashboards server</td><td>Runs source connections and queries</td><td>Hosting, application auth, secret handling, approved read scope</td></tr>
          <tr><td>OpenUI Dashboards API</td><td>Builds dashboard definitions and supports editing</td><td>Vendor review, data transfer, model choice, cost, retention terms</td></tr>
          <tr><td>Browser</td><td>Displays charts, filters and drill-downs</td><td>Correct interpretation and access to displayed results</td></tr>
        </tbody>
      </table>
    </div>
    <p>According to the project README, exploratory data used to answer a question is sent to the OpenUI Dashboards API; the cloud service also stores dashboard and chat state. Check the exact data flow for your deployment before exposing anything beyond synthetic data. See <a href="https://www.openui.com/docs/dashboards/authentication">OpenUI authentication</a> and the <a href="https://github.com/thesysdev/opendashboards#how-it-works">OpenDashboards data flow</a>.</p>
  </section>

  <section>
    <h2>3. When to use it</h2>
    <ul>
      <li>A migration team needs a quick view of ready, blocked and failed records before a daily call.</li>
      <li>A data owner wants to compare exceptions by business area without asking a developer to create every chart.</li>
      <li>An analyst needs to explore GA4, Search Console or database results before specifying stable KPIs.</li>
      <li>A product team wants to test whether conversational analytics improves decisions, not just presentation speed.</li>
    </ul>
    <p><strong>Do not start here</strong> when a regulated financial KPI must have an approved semantic definition, row-level authorization is missing, or a standard BI report already answers the question reliably.</p>
  </section>

  <section>
    <h2>4. Three realistic work situations (simulations)</h2>
    <h3>SAP migration readiness</h3>
    <p>A cutover lead sees 400 records labelled “blocked” but cannot tell which sales organizations need attention. The dashboard groups records by status and organization, shows the last refresh, and lists individual exception IDs. The decision is which upstream team must correct the next batch.</p>
    <h3>Master data quality</h3>
    <p>A data steward receives weekly exception extracts. Before building a permanent KPI, the steward tests which defect categories are meaningful and checks whether repeated records are counted twice. The decision is whether to improve the extraction or automate a governed report.</p>
    <h3>Website analytics</h3>
    <p>An editor wants to compare Search Console visibility with content releases. A dashboard can expose changes in impressions and clicks, but it cannot prove that an article caused a ranking change. The decision is what to investigate, not what causal story to tell.</p>
  </section>

  <section>
    <h2>5. Inputs required</h2>
    <ul>
      <li><strong>Question and owner:</strong> which decision will be made, by whom, and how frequently?</li>
      <li><strong>Metric contract:</strong> grain, numerator, denominator, filters and freshness threshold.</li>
      <li><strong>Data source:</strong> a supported read-only connection, preferably a synthetic or approved reporting dataset.</li>
      <li><strong>Security decision:</strong> what fields may reach the application, model service and end user's browser?</li>
      <li><strong>Validation query:</strong> a deterministic source query for at least one headline KPI.</li>
    </ul>
    <p>Current built-in sources listed by the project include PostgreSQL, MySQL/MariaDB, ClickHouse, BigQuery, PostHog, GA4 and Search Console. Remote HTTPS MCP servers have limited support with API-key authentication; this is <strong>not</strong> a native SAP connector.</p>
  </section>

  <section>
    <h2>6. Questions to ask before connecting data</h2>
    <ul>
      <li>Does “blocked” mean one object, one failed attempt, or one current exception?</li>
      <li>Can the same object appear twice after retry or replication?</li>
      <li>How old can the last refresh be before the dashboard becomes misleading?</li>
      <li>Which organizational dimension can each viewer see?</li>
      <li>Who approves the dashboard definition, and who investigates an unexpected number?</li>
    </ul>
  </section>

  <section>
    <h2>7. Working method: from zero to a useful view</h2>
    <ol>
      <li><strong>Choose a single decision.</strong> Example: identify which fictional sales organization has the most unresolved migration cases.</li>
      <li><strong>Choose the entry path.</strong> Try <a href="https://opendashboards.com/">the hosted application</a> with an approved reachable source, or run the repository locally for a controlled test.</li>
      <li><strong>Prepare a read-only dataset.</strong> Start with the eight synthetic rows below. Do not connect a productive SAP system for the first exercise.</li>
      <li><strong>Write the metric definition first.</strong> A case is one row, and the status is its current status. “Unresolved” means blocked or failed.</li>
      <li><strong>Generate one dashboard.</strong> Ask for total cases, status split, unresolved rate by sales organization, and the underlying exception list.</li>
      <li><strong>Validate the result.</strong> Compare the generated KPI to SQL; inspect unexpected counts, missing records and update timestamps.</li>
      <li><strong>Refine only what adds value.</strong> Ask for a filter or change one chart. Stop if the view adds no better decision than a simple table.</li>
    </ol>

    <h3>Self-hosted application: quick start</h3>
    <p>As of 22 November 2026, the official README specifies Node.js 20.9+, pnpm, Docker and a Thesys API key. Run the application separately from the example dataset.</p>
    <pre><code>git clone https://github.com/thesysdev/opendashboards.git
cd opendashboards
pnpm install
cp .env.example .env.local
# Add THESYS_API_KEY to .env.local (never commit this file).
pnpm db:up
pnpm db:reset
pnpm dev
# Open http://localhost:3000</code></pre>
    <p>The README warns that local development uses a shared dev identity and stores connection credentials without production encryption. This setup is for a private development machine and synthetic data only. A production deployment needs an authentication provider, proper secret management and a separate security review.</p>
  </section>

  <section>
    <h2>8. Hands-on lab: synthetic SAP-style migration dashboard</h2>
    <p><strong>Duration:</strong> approximately 30–45 minutes once the prerequisites work. These are invented training records, not an SAP export and not actual customer data.</p>
    <h3>Step A — Start a small PostgreSQL source</h3>
    <p>For a local development setup, run a separate database. These commands are for a Docker-enabled terminal; the password is a deliberately disposable demo credential.</p>
    <pre><code>docker run -d --name sap-dashboard-demo \
  -e POSTGRES_PASSWORD=demo_only_password \
  -e POSTGRES_DB=demo_migration \
  -p 127.0.0.1:54330:5432 postgres:16

docker exec -it sap-dashboard-demo psql \
  -U postgres -d demo_migration</code></pre>
    <h3>Step B — Paste this SQL into psql</h3>
    <pre><code>CREATE TABLE demo_migration_status (
  case_id      text PRIMARY KEY,
  sales_org    text NOT NULL,
  object_type  text NOT NULL,
  status       text NOT NULL CHECK
    (status IN ('ready', 'blocked', 'failed')),
  issue_type   text,
  checked_at   timestamptz NOT NULL DEFAULT now()
);

INSERT INTO demo_migration_status
  (case_id, sales_org, object_type, status, issue_type)
VALUES
 ('SYN-001','S001','Customer','ready',NULL),
 ('SYN-002','S001','Customer','blocked','Missing sales area'),
 ('SYN-003','S001','Customer','failed','Interface error'),
 ('SYN-004','S001','Customer','ready',NULL),
 ('SYN-005','S002','Customer','blocked','Missing tax data'),
 ('SYN-006','S002','Customer','ready',NULL),
 ('SYN-007','S002','Customer','blocked','Missing sales area'),
 ('SYN-008','S002','Customer','ready',NULL);

CREATE ROLE dashboard_reader LOGIN PASSWORD 'demo_reader_only';
GRANT CONNECT ON DATABASE demo_migration TO dashboard_reader;
GRANT USAGE ON SCHEMA public TO dashboard_reader;
GRANT SELECT ON demo_migration_status TO dashboard_reader;</code></pre>
    <p>Leave psql with <code>\q</code>. In the locally running OpenDashboards application, configure a PostgreSQL connection: host <code>127.0.0.1</code>, port <code>54330</code>, database <code>demo_migration</code>, user <code>dashboard_reader</code>, password <code>demo_reader_only</code>. This works when the application server can reach your host. A cloud-hosted OpenDashboards instance cannot automatically reach your laptop's localhost.</p>
    <h3>Step C — Ask for a decision-focused dashboard</h3>
    <pre><code>Create a migration readiness dashboard using
demo_migration_status.

- Show total cases, ready cases and unresolved cases.
- Unresolved means status = blocked or failed.
- Compare unresolved cases by sales_org.
- Show issue_type frequency and a list of unresolved case IDs.
- Display the latest checked_at timestamp.
- Use the table data only. Do not invent causes or trends.
- Let me filter by sales_org.</code></pre>
    <h3>Step D — Check the numbers independently</h3>
    <pre><code>SELECT
  sales_org,
  count(*) AS total,
  count(*) FILTER (WHERE status = 'ready') AS ready,
  count(*) FILTER
    (WHERE status IN ('blocked','failed')) AS unresolved
FROM demo_migration_status
GROUP BY sales_org
ORDER BY sales_org;</code></pre>
    <p><strong>Expected result:</strong> eight cases in total, four ready and four unresolved. S001 has two unresolved; S002 has two unresolved. If the dashboard shows a different count, do not accept its explanation until the source rows and filter logic are inspected.</p>
    <h3>Step E — Make one targeted change</h3>
    <p>Ask: “Show the unresolved rate next to the count for each sales organization, and keep the exception table unchanged.” Confirm that both organizations show 50% unresolved (2 of 4). Then test whether changing one source status is reflected after refresh. Record actual behavior rather than assuming all connectors support the same refresh timing.</p>
  </section>

  <section>
    <h2>9. SAP integration: a proposed architecture, not an out-of-box feature</h2>
    <p>For S/4HANA, start with an approved <strong>read-only extraction layer</strong> such as a released API or governed integration service appropriate to the system edition. Write a sanitized, time-stamped reporting projection to a database the dashboard can read. API availability, authentication, extraction cadence and field selection are project- and release-dependent.</p>
    <figure>
      <pre><code>[SAP S/4HANA or migration tool]
            |
            v
[Approved read-only extraction + validation]
            |
            v
[Sanitized reporting database] --&gt; [OpenDashboards server] --&gt; [Browser]
                                         |
                                         v
                                  [OpenUI Cloud API]
                            dashboard state + generation context</code></pre>
      <figcaption>Illustrative design. The cloud boundary must be assessed against the actual API payload and contract; this is not a native SAP connector diagram.</figcaption>
    </figure>
    <p><strong>Data contract example:</strong> case ID, object type, sales organization, current status, exception category, source snapshot timestamp and extraction job ID. Include source freshness and deduplication rules. Exclude personal identifiers, customer names and document content unless their use is specifically approved.</p>
    <p>Do not make the AI query productive SAP tables directly, determine user authorization, or correct master data. A dashboard is a <em>read-side projection</em>, not an operational write interface. For unresolved exceptions, it should direct the user to the governed remediation process.</p>
  </section>

  <section>
    <h2>10. Decision rules: when this is the right tool</h2>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Decision table for AI-generated dashboards">
      <table class="study-table__table">
        <thead><tr><th>If...</th><th>Then...</th></tr></thead>
        <tbody>
          <tr><td>The team is exploring changing questions on approved read-only data</td><td>Pilot OpenDashboards and measure usefulness</td></tr>
          <tr><td>The KPI is regulated, contractual or finance-critical</td><td>Use an approved semantic model and controlled BI/reporting path</td></tr>
          <tr><td>The source data is stale or has ambiguous record grain</td><td>Fix the data contract before prompting</td></tr>
          <tr><td>The dataset cannot legally or contractually leave the approved boundary</td><td>Do not connect it to a cloud-generating service without an approved private deployment</td></tr>
          <tr><td>The use case requires writes, approvals or master-data correction</td><td>Keep the dashboard read-only and use a separate governed workflow</td></tr>
          <tr><td>The same dashboard becomes a stable daily operational control</td><td>Consider promoting it to versioned, tested BI or an owned internal application</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>11. Deliverables and reusable template</h2>
    <p>Produce three small artifacts: a dashboard link or screenshot, a source-query validation note, and an architecture decision. A useful pilot brief fits on one page:</p>
    <pre><code># Dashboard Pilot Brief
Business decision: [What will be decided?]
Audience / owner: [Role]
Source + data classification: [System and sensitivity]
Data grain: [One row represents ...]
Metrics: [Exact formula and filters]
Freshness: [Maximum age and as-of timestamp]
Read permission: [Account, scope, user authorization]
Cloud boundary: [Which fields may reach OpenUI Cloud?]
Validation SQL / source: [Reference query]
Success test: [What result saves time or improves a decision?]
Stop condition: [When do we reject the pilot?]</code></pre>
    <p>Example acceptance test: “For eight synthetic records, totals match SQL exactly; the organization filter changes the counts; the last refresh is visible; and the dashboard exposes no write action.”</p>
  </section>

  <section>
    <h2>12. Quality checklist</h2>
    <ul>
      <li>□ The question names a decision, not just “show insights”.</li>
      <li>□ Every headline metric has a defined grain and formula.</li>
      <li>□ A read-only account has no insert, update or delete privileges.</li>
      <li>□ The dashboard shows source freshness or a clear as-of date.</li>
      <li>□ SQL totals match displayed totals for at least one representative slice.</li>
      <li>□ The team has reviewed which data goes to OpenUI Cloud.</li>
      <li>□ A user can distinguish observed data from AI-generated interpretation.</li>
      <li>□ The next action has a real owner outside the dashboard.</li>
    </ul>
  </section>

  <section>
    <h2>13. Common mistakes</h2>
    <ul>
      <li><strong>Connecting directly to productive SAP data:</strong> unnecessary security exposure and uncontrolled load. Prefer an approved reporting projection.</li>
      <li><strong>Asking AI to define the KPI:</strong> “failed” and “blocked” may be different business states. Write the rule yourself.</li>
      <li><strong>Treating a live dashboard as real time:</strong> source extraction may run once per day. Surface the timestamp.</li>
      <li><strong>Assuming open-source application means offline processing:</strong> check the OpenUI Cloud dependency.</li>
      <li><strong>Building ten charts before checking one number:</strong> first prove accuracy, then improve the view.</li>
    </ul>
  </section>

  <section>
    <h2>14. Instructions for an AI assistant</h2>
    <ol>
      <li>Ask for the business decision, audience, current data source, classification and refresh requirement.</li>
      <li>Separate documented product capabilities from a proposed enterprise integration.</li>
      <li>Define each metric and authorized data boundary before generating a prompt or dashboard.</li>
      <li>Use synthetic samples when production access, data residency or permissions are unapproved.</li>
      <li>Produce a verification SQL query, expected result, risks and explicit unknowns.</li>
      <li>Never invent an SAP API, a connector, real data, a validated calculation, or a successful deployment.</li>
      <li>Stop and request a governed review when the task involves private data transfer or write access.</li>
    </ol>
  </section>

  <section>
    <h2>15. Practice challenge: defend the architecture</h2>
    <p><strong>Scenario:</strong> A migration lead asks for a “real-time AI dashboard” for a nightly batch migration. The source export runs at 02:00 and no new state exists until the next run. Do you build real-time streaming?</p>
    <p><strong>Architect's answer:</strong> “I would not promise real-time visibility when the source updates once per day. I would show a daily snapshot, its timestamp, the exceptions by owner and an explicit stale-data warning. If the business genuinely needs intraday decisions, we should change the extraction contract before changing the dashboard.”</p>
    <p><strong>Your exercise:</strong> explain the recommendation in 60 seconds, define two risks, and name the evidence that would justify an investment in a more frequent integration.</p>
  </section>

  <section>
    <h2>Related skills, Atlas pages and primary sources</h2>
    <p><strong>Skills:</strong> <a href="/skill-hub/ai-assisted-analysis/ai-output-review-working-skill/">AI Output Review</a> · <a href="/skill-hub/ai-assisted-analysis/ai-prompt-briefing-work-artifacts-working-skill/">Prompt Briefing</a> · <a href="/skill-hub/ai-assisted-development/mcp-development-workflow/">MCP Development Workflow</a>.</p>
    <p><strong>Atlas:</strong> <a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a> · <a href="/atlas/automation/rule-based-automation-vs-ai/">Rule-Based Automation vs AI</a>.</p>
    <p><strong>Primary references (checked 22 November 2026):</strong> <a href="https://github.com/thesysdev/opendashboards">OpenDashboards README and license</a> · <a href="https://www.openui.com/docs/dashboards/authentication">OpenUI authentication</a> · <a href="https://www.openui.com/dashboards">OpenUI Dashboards</a>. Product features, prices and source support may change: verify the current release and commercial terms before delivery.</p>
    <p><strong>Verification status:</strong> review candidate, not yet human-reviewed. The setup follows current published documentation; the SAP data model and all examples are deliberately synthetic. No application installation or end-to-end live dashboard test was performed as part of this article.</p>
  </section>
</article>