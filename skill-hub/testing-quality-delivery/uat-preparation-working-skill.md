---
layout: default
title: "UAT Preparation Working Skill"
description: "Prepare business testers with clear scenarios, test data, environment access, and defect reporting rules so UAT produces valid sign-off."
permalink: /skill-hub/testing-quality-delivery/uat-preparation-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/testing-quality-delivery/">Testing, QA, and Delivery Validation</a></li>
    <li aria-current="page">UAT Preparation</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Testing, QA, and Delivery Validation</p>
  <h1>UAT Preparation Working Skill</h1>
  <p class="lead">Produce a UAT Preparation Pack that gives business testers everything they need to execute acceptance tests, report defects, and produce a valid sign-off without relying on the development team for daily support.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>User Acceptance Testing (UAT) is the phase where business users verify that the system meets their needs before go-live. UAT often fails not because the system is broken, but because the testers are unprepared: they do not know what to test, they lack the right data, they cannot access the environment, or they report defects in a way that the development team cannot act on. This skill prepares the business testers so that UAT produces valid, traceable, and sign-off-ready evidence. The output is a UAT Preparation Pack that includes the test script, test data, environment guide, defect reporting rules, and a schedule. A well-prepared UAT reduces the number of false defects, shortens the UAT cycle, and increases the confidence of the business sign-off.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>UAT is scheduled and the business testers need preparation before the first test session.</li>
      <li>Previous UAT cycles were delayed because testers spent more time asking how to test than actually testing.</li>
      <li>Defects from UAT were vague or untraceable, causing rework and frustration on both sides.</li>
      <li>The business testers are not SAP experts and need simplified instructions for transactions and navigation.</li>
      <li>The UAT environment is new or refreshed, and testers need guidance on how to access it and what data is available.</li>
      <li>The project requires a formal UAT sign-off, and the QA lead wants to ensure the evidence is complete and credible.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>New sales order workflow: business testers need simplified guidance</h3>
    <p>A new sales order workflow is ready for UAT. The business testers are sales managers who know the process but do not know SAP transactions. The UAT preparation must provide: simplified navigation steps (with screenshots), the exact customer and material numbers to use, the expected results in business language (not SAP status codes), and a defect reporting template that asks for the business impact, not only the technical symptom. Without preparation, the testers open VA01, get lost in the incompletion log, and report a defect that is actually a missing field entry.</p>

    <h3>Credit management change: test data and environment confusion</h3>
    <p>A credit management change is in UAT. The testers need customers with specific credit limits and exposures. The preparation must specify: which customers in the UAT environment have the right data, how to verify the credit limit before testing, what to do if the credit limit is wrong, and how to reset the exposure after the test. Without preparation, the testers use the wrong customer, get an unexpected result, and report a defect that is caused by test data, not by the change.</p>

    <h3>Integration scenario: UAT spans two systems</h3>
    <p>A new IDoc integration from the e-commerce platform to SAP is in UAT. The business testers must verify that orders placed in the web shop appear correctly in SAP. The preparation must specify: which test orders to place in the web shop, how to verify them in SAP (WE02, VA03), the expected IDoc status sequence, and who to contact if the IDoc does not arrive. Without preparation, the testers place orders and wait, not knowing how to check the interface, and report a defect that is actually a delay in the queue.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Approved test scenarios and test cases that cover the scope of the UAT.</li>
      <li>UAT environment details: system URL, client, login credentials, and supported browsers or SAP GUI versions.</li>
      <li>Test data catalog: customer numbers, material numbers, vendor codes, and organizational units that are valid in the UAT environment.</li>
      <li>Business process description in plain language, showing what the tester is trying to achieve, not only the SAP transaction.</li>
      <li>Defect reporting tool and template: where to report, what fields to fill, and what evidence to attach.</li>
      <li>Tester roster: names, roles, availability, and SAP experience levels.</li>
      <li>UAT schedule: dates, times, sessions, and deadlines for completion.</li>
      <li>Support contact list: who to ask for technical, functional, or data issues during UAT.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What business process is the tester trying to complete, and what does success look like in business terms?</li>
      <li>Which SAP transactions or screens does the tester need, and can they navigate them without developer help?</li>
      <li>What test data is available, and how does the tester verify that the data is in the right state before testing?</li>
      <li>What should the tester do if a test fails: report a defect, ask for help, or retry with different data?</li>
      <li>How does the tester report a defect, and what information must they include for the development team to reproduce it?</li>
      <li>What is the UAT schedule, and are all testers available for the full duration?</li>
      <li>Who provides technical support during UAT, and what is the escalation path?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Select the UAT scope.</strong> From the approved test cases, pick the subset that covers the business processes the UAT must validate. Exclude purely technical or regression cases unless the business has agreed to test them. Document the scope in the UAT Preparation Pack.</li>
      <li><strong>Translate test cases into business language.</strong> Rewrite the test steps from technical SAP language into business process language. For example, instead of "Enter VA01 and input KUNNR," write "Create a new sales order for customer ABC." Include the SAP transaction in parentheses for reference but make the primary instruction business-oriented.</li>
      <li><strong>Prepare the test data sheet.</strong> List every customer, material, vendor, or order needed for UAT. Include the data value, the business scenario it supports, and how to verify that it is in the correct state before testing. Include a contact for data issues.</li>
      <li><strong>Prepare the environment guide.</strong> Document how to access the UAT environment: URL, client, login instructions, and supported tools. Include a troubleshooting section for common access issues (password reset, firewall, browser compatibility).</li>
      <li><strong>Prepare the defect reporting guide.</strong> Document the defect reporting tool, the required fields, and the evidence to attach (screenshot, order number, IDoc number, steps taken). Include a template for writing a clear defect summary and business impact statement.</li>
      <li><strong>Schedule the UAT sessions.</strong> Create a schedule with dates, times, tester assignments, and expected completion. Allow buffer time for defect resolution and retest. Communicate the schedule to all testers and stakeholders.</li>
      <li><strong>Conduct the UAT kickoff briefing.</strong> Walk the testers through the pack: scope, scripts, data, environment, and defect reporting. Allow time for questions and hands-on practice. Record the briefing for testers who cannot attend.</li>
      <li><strong>Provide daily support during UAT.</strong> Assign a QA analyst or functional consultant to be available during UAT hours. Their role is to answer questions, verify data, and triage defects as they are reported. Do not let testers wait for answers.</li>
      <li><strong>Track progress daily.</strong> Update a progress tracker showing which cases are executed, which are blocked, and which defects are open. Share the tracker with the project lead and business owner.</li>
      <li><strong>Prepare the UAT completion package.</strong> At the end of UAT, collect the executed test evidence, the defect log, and the business sign-off form. Verify that the evidence is complete before asking for sign-off.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a test case is too technical for a business tester, either simplify it or move it to the technical test phase, not UAT.</li>
      <li>If test data is missing or incorrect, do not start UAT until the data is fixed. False defects from bad data waste everyone's time.</li>
      <li>If a tester reports a defect that is caused by a test data issue, close it as "data issue" and fix the data, not the code.</li>
      <li>If a tester cannot access the environment, halt UAT for that tester until access is resolved. Do not let them share another tester's login.</li>
      <li>If a defect is reported without reproduction steps or evidence, request the missing information before the development team acts on it.</li>
      <li>If UAT progress is behind schedule, escalate to the project lead before the last day. Do not surprise stakeholders with incomplete UAT.</li>
      <li>If the business owner is unavailable for sign-off, document the completion evidence and schedule the sign-off for the earliest available date.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>UAT Preparation Pack</strong> — Per UAT cycle or per release. Contains scope, test scripts, test data sheet, environment guide, defect reporting guide, schedule, and support contacts. See template below.</li>
      <li><strong>UAT Progress Tracker</strong> — Daily updated table showing execution status, blocked cases, and open defects.</li>
      <li><strong>UAT Completion Package</strong> — Executed test evidence, defect log, and business sign-off form.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>UAT Preparation Pack (compact)</h3>
    <pre><code>---
artifact: UAT Preparation Pack
release: &lt;Release name&gt;
uat period: &lt;Start date&gt; to &lt;End date&gt;
---

## UAT Scope
- Business processes to validate: &lt;List&gt;
- In scope: &lt;List of features or changes&gt;
- Out of scope: &lt;List of items not tested in UAT&gt;
- Sign-off criteria: &lt;What must be true for UAT to be considered complete&gt;

## Test Scripts
### Script 1: Create standard sales order
- **Business objective:** A sales representative creates a new order for a valid customer.
- **Steps:**
  1. Open Sales Order Creation (VA01).
  2. Select order type Standard (OR) and sales organization 1000.
  3. Enter customer C-UAT-01.
  4. Enter material M-UAT-01, quantity 10.
  5. Save the order.
- **Expected result:** Order is created and displays a number. The customer receives an order confirmation.
- **Test data:** Customer C-UAT-01, Material M-UAT-01.
- **How to verify data:** Check customer credit limit in FD33 before testing. If not 50,000 EUR, contact the Data Team.

### Script 2: Verify credit block
- **Business objective:** A sales order for a customer over their credit limit is blocked.
- **Steps:** (Simplified from technical case)
- **Expected result:** Order is blocked and appears in the credit block list.
- **Test data:** Customer C-UAT-02 with credit limit 50,000 EUR and open exposure 48,000 EUR.

## Test Data Sheet
| Data item | Value | Business scenario | Verification check | Issue contact |
|-----------|-------|-------------------|--------------------|---------------|
| Customer standard | C-UAT-01 | Standard order | Credit limit = 50,000 EUR | Data Team |
| Customer credit block | C-UAT-02 | Credit block | Exposure = 48,000 EUR | Data Team |
| Material standard | M-UAT-01 | Standard order | Stock available | Data Team |

## Environment Guide
- **System:** UAT-ERP.company.com
- **Client:** 400
- **Login:** Your standard domain username and password
- **Browser:** Chrome or Edge latest version
- **Troubleshooting:** If login fails, reset password via the IT portal. If SAP GUI is required, contact IT for installation.

## Defect Reporting Guide
- **Tool:** Jira project UAT-2026
- **Required fields:** Summary, Steps to reproduce, Expected result, Actual result, Business impact, Screenshot, Order/IDoc number if applicable
- **Template:**
  - Summary: "[UAT] Unable to create order for customer C-UAT-01"
  - Steps: 1. Open VA01... 2. Enter customer...
  - Expected: Order creates with confirmation.
  - Actual: Error message appears and order does not save.
  - Impact: Sales team cannot process orders for this customer segment.

## Schedule
| Date | Session | Testers | Focus |
|------|---------|---------|-------|
| 2026-06-14 | Morning | Alice, Bob | Standard orders |
| 2026-06-14 | Afternoon | Carol, Dave | Credit blocks |
| 2026-06-15 | Morning | All | Defect retest and sign-off |

## Support Contacts
- Functional questions: Functional Consultant A (email / chat)
- Data issues: Data Team (email)
- Technical issues: IT Support (ticket portal)
- Escalation: QA Lead D. Kharlanau
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The UAT scope is approved by the business owner and clearly states what is in and out of scope.</li>
      <li>Test scripts are written in business language, with SAP transactions provided for reference only.</li>
      <li>Every script has expected results stated in business terms, not only technical status codes.</li>
      <li>Test data is cataloged with values, scenarios, verification checks, and issue contacts.</li>
      <li>The environment guide includes access instructions, supported tools, and troubleshooting.</li>
      <li>The defect reporting guide includes a template that asks for business impact and reproduction evidence.</li>
      <li>The schedule is realistic and includes buffer time for defect resolution and retest.</li>
      <li>Support contacts are named and available during UAT hours.</li>
      <li>Progress is tracked daily and shared with stakeholders.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Giving business testers raw technical test cases.</strong> Consequence: testers do not understand the steps, create false defects, and spend more time asking for help than testing. UAT timelines slip.</li>
      <li><strong>Providing test data without verification instructions.</strong> Consequence: testers use data that is in the wrong state and report defects caused by data, not by the system.</li>
      <li><strong>Skipping the defect reporting template.</strong> Consequence: defects are reported as "it does not work" with no steps, no evidence, and no business impact. The development team cannot reproduce them and closes them as "not enough info."</li>
      <li><strong>Not scheduling buffer time for retest.</strong> Consequence: UAT ends with open defects that cannot be retested because the schedule is over. The sign-off is delayed or forced with unverified fixes.</li>
      <li><strong>Absence of daily support during UAT.</strong> Consequence: testers stop testing when they hit a question, and hours of UAT time are lost. The schedule assumes full-days but achieves half-days of actual work.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A brief email to the business testers: "UAT starts Monday. Please test the sales order and credit management features. Use the test system. Report any issues in Jira. Let me know if you have questions." No test scripts, no data, no environment guide, no schedule, no defect template, no support contacts.</p>
    <p><strong>Why it fails:</strong> Testers do not know what to test, how to test it, or what data to use. They waste the first two days of UAT asking basic questions. Defects are vague and unactionable. UAT produces no credible evidence for sign-off.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: UAT Preparation Pack
release: S/4 2026.06 Wave 2
uat period: 2026-06-14 to 2026-06-15
---

## UAT Scope
- In scope: Standard sales order creation, credit block verification.
- Out of scope: Returns, billing, reporting.
- Sign-off criteria: All scripts executed, no critical defects open, business owner signs.

## Test Script 1: Standard order
- **Objective:** Create a sales order for a valid customer.
- **Steps:** 1. Open VA01... 2. Enter customer C-UAT-01... 3. Save.
- **Expected:** Order created with confirmation.
- **Data:** C-UAT-01, M-UAT-01. Verify credit limit in FD33 before testing.

## Test Data Sheet
| Data | Value | Scenario | Check | Contact |
|------|-------|----------|-------|---------|
| Customer | C-UAT-01 | Standard order | Credit limit 50k | Data Team |
| Customer | C-UAT-02 | Credit block | Exposure 48k | Data Team |
| Material | M-UAT-01 | Standard order | Stock available | Data Team |

## Environment
- System: UAT-ERP.company.com, Client 400
- Login: Domain credentials
- Browser: Chrome/Edge
- Issues: IT portal for password reset

## Defect Reporting
- Tool: Jira UAT-2026
- Template: Summary, Steps, Expected, Actual, Impact, Screenshot

## Schedule
| Date | Session | Testers | Focus |
|------|---------|---------|-------|
| 2026-06-14 | Morning | Alice, Bob | Standard orders |
| 2026-06-14 | Afternoon | Carol, Dave | Credit blocks |
| 2026-06-15 | Morning | All | Retest and sign-off |

## Support Contacts
- Functional: Consultant A
- Data: Data Team
- Technical: IT Support
- Escalation: QA Lead D. Kharlanau
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> UAT preparation coordinator for an enterprise SAP project.</p>
    <p><strong>Context:</strong> You have approved test cases, a UAT environment, a tester roster, and a defect reporting tool. You need to produce a UAT Preparation Pack that enables business testers to execute acceptance tests without daily dependence on the development team.</p>
    <p><strong>Task:</strong> Translate technical test cases into business language, catalog test data, prepare an environment guide, create a defect reporting template, schedule sessions, and define support contacts. Produce a UAT Preparation Pack.</p>
    <p><strong>Output format:</strong> UAT Preparation Pack in Markdown, using the compact template with sections for Scope, Test Scripts, Test Data, Environment, Defect Reporting, Schedule, and Support Contacts.</p>

    <ul>
      <li><strong>Never give business testers raw technical test cases.</strong> Translate every step into business language. Include SAP transactions only as reference.</li>
      <li><strong>Always provide test data with verification checks.</strong> Tell the tester how to confirm the data is in the right state before testing.</li>
      <li><strong>Always include a defect reporting template.</strong> Require business impact, reproduction steps, and evidence. Do not let testers report "it does not work."</li>
      <li><strong>Always schedule buffer time for retest.</strong> UAT without buffer forces a rushed or incomplete sign-off.</li>
      <li><strong>Always name support contacts and make them available during UAT hours.</strong> Unanswered questions stall UAT and reduce effective testing time.</li>
      <li><strong>Do not invent test data, environment details, or tester names.</strong> Use the inputs provided. If data is missing, flag it and request it before UAT begins.</li>
      <li><strong>Link to Atlas diagnostics</strong> when UAT scripts touch SAP processes. Reference relevant Atlas pages for the functional consultant to use when answering tester questions.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/testing-quality-delivery/test-case-design-working-skill/">Test Case Design</a> — Provides the executable cases that UAT preparation translates into business scripts.</li>
      <li><a href="/skill-hub/testing-quality-delivery/defect-triage-classification-working-skill/">Defect Triage and Classification</a> — Manages the defects reported during UAT.</li>
      <li><a href="/skill-hub/testing-quality-delivery/qa-review-sign-off-working-skill/">QA Review and Sign-Off</a> — Uses the UAT completion package for the quality gate.</li>
      <li><a href="/skill-hub/business-analysis/acceptance-criteria-working-skill/">Acceptance Criteria</a> — Provides the criteria that UAT must verify.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a> — Context for credit block scenarios in UAT.</li>
      <li><a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a> — Reference for order completeness questions during UAT.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of UAT preparation practices. It is not official ISTQB, BABOK, or SAP documentation. It focuses on enterprise SAP contexts where business testers are not SAP experts and require translation, data guidance, and structured support.</p>
    <p>Known limitations: the skill assumes a separate UAT environment and a defined tester roster. It does not cover automated UAT or end-user testing embedded in continuous deployment. It assumes manual test execution by business users. Some organizations use specialized UAT management tools (e.g., Tricentis, Micro Focus) that may require additional metadata beyond the template provided.</p>
  </section>
</article>
