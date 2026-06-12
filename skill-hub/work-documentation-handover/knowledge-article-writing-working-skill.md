---
layout: default
title: "Knowledge Article Writing Working Skill"
description: "Turn a known fix, workaround, or procedure into a self-service knowledge article that reduces repeat tickets and onboarding time."
permalink: /skill-hub/work-documentation-handover/knowledge-article-writing-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/work-documentation-handover/">Work Documentation and Handover</a></li>
    <li aria-current="page">Knowledge Article Writing</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Work Documentation and Handover</p>
  <h1>Knowledge Article Writing Working Skill</h1>
  <p class="lead">Turn a known fix, workaround, or procedure into a self-service knowledge article that reduces repeat tickets and onboarding time.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Support teams spend a significant portion of their time answering the same questions and fixing the same issues. This skill produces a Knowledge Article: a structured, self-service document that enables a user or junior support engineer to resolve a known issue or perform a known procedure without asking an expert. The article is designed for searchability, scanability, and accuracy. It is not a training manual or a comprehensive guide. It is a targeted answer to a specific question or problem. The output reduces ticket volume, shortens resolution time, and preserves institutional knowledge as people move between teams.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A support issue has been resolved three or more times and the team wants to enable self-service for the next occurrence.</li>
      <li>A new team member needs to learn a common procedure without shadowing a senior engineer for every case.</li>
      <li>A workaround exists for a known system limitation and users keep opening tickets because they do not know the workaround.</li>
      <li>A configuration change or update introduces a new behavior that users will ask about repeatedly.</li>
      <li>An AI agent is answering support questions and needs a structured knowledge source to cite.</li>
      <li>A help desk or service desk needs articles to populate a self-service portal or chatbot.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP credit block: enabling self-service for sales admins</h3>
    <p>Sales admins regularly open tickets asking why a customer order is blocked. The support engineer checks VKM1, sees a credit block, and releases it. This happens five times per week. A Knowledge Article is written: "How to Check and Release a Credit Block in S/4HANA." The article includes the symptom (order blocked, cannot deliver), the check (run VKM1 for the customer), the decision rule (if block is due to credit limit, release only if approved by finance), the steps (select order, click release, confirm), and the verification (order status changes to open). After publishing, ticket volume drops by 60% and sales admins handle routine blocks themselves.</p>

    <h3>IDoc reprocessing: documenting the safe procedure</h3>
    <p>Failed IDocs are a common integration issue. Junior support engineers often reprocess IDocs incorrectly: they use BD87 without checking the error, or they reprocess all IDocs in a batch including good ones. A Knowledge Article is written: "How to Safely Reprocess a Failed IDoc in S/4HANA." The article includes the symptom (status 51 or 63), the diagnosis steps (check WE02 for error text, check SM58 for RFC issues), the safe reprocessing steps (use WE19 for single IDoc, BD87 only after error fix, never reprocess without checking), and the verification (status 53, document in IDoc log). After publishing, the rate of incorrectly reprocessed IDocs drops significantly.</p>

    <h3>Master data request: standardizing the vendor creation workflow</h3>
    <p>Business users frequently ask how to request a new vendor. The process involves a form, a validation step, and a master data team entry. The requests arrive via email, chat, and tickets with incomplete information. A Knowledge Article is written: "How to Request a New Vendor in SAP." The article includes the required data (vendor name, tax number, address, bank details, purchase organization), the form location, the validation timeline, and the status check method. After publishing, the master data team receives fewer incomplete requests and processing time improves.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>The specific problem or procedure that the article will address. One problem per article.</li>
      <li>The exact steps to resolve the problem or perform the procedure, verified by an expert.</li>
      <li>The symptoms that a user will see, in their own words, so the article can be found by search.</li>
      <li>The systems, transactions, and programs involved, with exact names and codes.</li>
      <li>The prerequisites or access required to perform the steps.</li>
      <li>The expected outcome and how to verify it.</li>
      <li>Known exceptions, edge cases, or situations where the article does not apply.</li>
      <li>Supporting screenshots, diagrams, or logs (optional but recommended).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the specific problem or question this article answers? If it answers more than one, split it into multiple articles.</li>
      <li>What words would a user type into a search box to find this article? Use those words in the title and the first paragraph.</li>
      <li>What are the exact steps? Can a person who has never done this before follow them?</li>
      <li>What could go wrong at each step? What is the recovery action?</li>
      <li>What are the prerequisites? What access, permissions, or data does the user need before starting?</li>
      <li>How does the user know it worked? What is the verification step?</li>
      <li>When does this article not apply? What are the exceptions that should be escalated?</li>
      <li>Who reviewed this article for accuracy? Has it been tested with a real user?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Identify the problem.</strong> Choose one specific, recurring issue or procedure. Do not combine multiple problems into one article. The article should be answerable in five to ten minutes.</li>
      <li><strong>Interview the expert.</strong> Ask the person who resolves this issue most often to walk through the exact steps. Record the transaction codes, screen names, and decision points.</li>
      <li><strong>Perform the steps yourself or observe a novice.</strong> Verify that the steps are complete and in the right order. If a novice cannot follow them, the article is not ready.</li>
      <li><strong>Write the article using the template.</strong> Use the exact structure: title, symptoms, prerequisites, steps, verification, exceptions, and related articles. Write in the second person ("you") and use imperative verbs ("click," "enter," "select").</li>
      <li><strong>Include screenshots or diagrams if helpful.</strong> Annotate screenshots to highlight the exact field or button. Do not include full-screen screenshots without annotation.</li>
      <li><strong>Document exceptions and escalation paths.</strong> State clearly when the article does not apply and what the user should do instead. This prevents the article from being used in the wrong context.</li>
      <li><strong>Write the search metadata.</strong> Include tags, keywords, and synonyms that users might search for. The title should contain the symptom, not the solution.</li>
      <li><strong>Review with the expert and a target user.</strong> The expert checks accuracy. The target user checks usability. If the target user cannot find or follow the article, revise it.</li>
      <li><strong>Publish and monitor.</strong> Publish the article in the knowledge base. Track views, search terms, and ticket reduction. Update the article when the system or procedure changes.</li>
      <li><strong>Retire when obsolete.</strong> If the issue is fixed permanently or the procedure changes completely, mark the article as obsolete and link to the replacement.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the issue has occurred fewer than three times, consider whether it is common enough to warrant an article. If not, document it in an incident record instead.</li>
      <li>If the procedure requires admin access or could damage data, write the article for support engineers, not end users. Include a warning at the top.</li>
      <li>If the article covers a workaround for a known bug, include the bug ID and the expected fix version. Retire the article when the fix is deployed.</li>
      <li>If the same symptom has multiple causes, write separate articles for each cause or use a decision tree. Do not write one article that covers every possible cause.</li>
      <li>If the article references a runbook, link to the runbook rather than duplicating it. The article is the answer; the runbook is the full procedure.</li>
      <li>If the article is for end users, avoid technical jargon. If it is for engineers, use exact technical terms and transaction codes.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Knowledge Article</strong> — Structured self-service document for a specific issue or procedure. See template below.</li>
      <li><strong>Search Metadata</strong> — Tags, keywords, and synonyms for the knowledge base search engine.</li>
      <li><strong>Usage Metrics</strong> — Optional tracking of views, ticket reduction, and user feedback.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Knowledge Article (compact)</h3>
    <pre><code>---
artifact: Knowledge Article
id: KA-&lt;area&gt;-&lt;number&gt;
title: &lt;Symptom in user language&gt;
audience: &lt;end user | support engineer | admin&gt;
system: &lt;System name&gt;
component: &lt;Component or module&gt;
keywords: &lt;Comma-separated search terms&gt;
tags: &lt;Comma-separated tags&gt;
last_verified: YYYY-MM-DD
author: &lt;Name&gt;
reviewer: &lt;Name&gt;
status: draft | published | obsolete
---

## Symptoms
- &lt;What the user sees or experiences&gt;
- &lt;Error message, status, or behavior&gt;
- &lt;When it happens (e.g., after a change, during a specific process)&gt;

## Applies To
- &lt;System version, client, or environment&gt;
- &lt;User roles or access levels&gt;

## Prerequisites
- &lt;Access or permission required&gt;
- &lt;Data or document needed before starting&gt;
- &lt;System state required (e.g., no open jobs)&gt;

## Steps
1. &lt;Imperative instruction with exact transaction or screen&gt;
2. &lt;Imperative instruction with exact transaction or screen&gt;
3. &lt;Decision point: if X, do Y. If Z, do W instead.&gt;
4. &lt;Imperative instruction&gt;

## Verification
- &lt;How to confirm the issue is resolved or the procedure is complete&gt;
- &lt;Expected outcome or status&gt;

## Exceptions and Escalation
- &lt;When this article does NOT apply&gt;
- &lt;What to do instead&gt;
- &lt;Escalation contact or team&gt;

## Related Articles
- &lt;Link to related knowledge article or runbook&gt;

## Change Log
| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | &lt;Description of change&gt; | &lt;Name&gt; |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The article addresses one specific problem or procedure. It does not try to cover everything.</li>
      <li>The title and first paragraph contain the words a user would search for.</li>
      <li>The steps are exact, sequential, and verifiable. A novice can follow them without asking for help.</li>
      <li>Prerequisites are stated before the steps, not hidden inside them.</li>
      <li>Verification is explicit: the user knows what success looks like.</li>
      <li>Exceptions and escalation paths are clearly stated.</li>
      <li>The article has been reviewed by a subject matter expert for accuracy.</li>
      <li>The article has been tested with a target user for usability.</li>
      <li>The article is tagged and categorized for searchability.</li>
      <li>The article has a review date and a change log.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Writing a comprehensive manual instead of a targeted article.</strong> Consequence: the article is too long to scan, users abandon it, and the ticket volume does not drop. One problem, one article.</li>
      <li><strong>Using technical jargon for end-user articles.</strong> Consequence: the user cannot understand the article and opens a ticket anyway. Match the language to the audience.</li>
      <li><strong>Omitting prerequisites.</strong> Consequence: the user starts the procedure, hits a permission error or missing data halfway through, and escalates. Prerequisites belong at the top.</li>
      <li><strong>Writing the article from the expert's perspective, not the user's.</strong> Consequence: the article assumes knowledge the user does not have. Write for the person who has the problem, not the person who fixes it.</li>
      <li><strong>Not updating the article when the system changes.</strong> Consequence: the article becomes a trap. Users follow outdated steps and create new problems. Set a review date.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A three-page document titled "SAP Credit Management." It covers the entire credit management module, including configuration, customizing, and theoretical concepts. The user who searches for "why is my order blocked" finds this document, reads for five minutes, and still does not know what to do. The document is accurate but useless for self-service.</p>
    <p><strong>Why it fails:</strong> It is not targeted. It is not scannable. It does not answer a specific question. It requires the user to extract the relevant information from a large document. The ticket volume does not drop.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Knowledge Article
id: KA-SD-2026-015
title: "Order blocked — how to check and release a credit block in S/4HANA"
audience: support engineer
system: S/4HANA 2023
component: SD — Credit Management
keywords: credit block, order blocked, VKM1, release order, credit limit
last_verified: 2026-06-10
author: M. Chen
reviewer: S. Mueller
status: published
---

## Symptoms
- Sales order is blocked and cannot be delivered.
- User sees status "Credit block" in VA03 or delivery creation fails in VL01N.
- Customer service reports that the customer has paid but the order is still blocked.

## Applies To
- S/4HANA 2023, all clients
- Sales orders with credit limit check active
- Support engineers with SD and FI-CA access

## Prerequisites
- Access to VA03, VKM1, and FBL5N
- Customer number and sales order number
- Approval from finance if the credit limit is to be overridden (see policy FIN-CR-001)

## Steps
1. Open VA03 and enter the sales order number. Check the status tab for "Credit block." Note the customer number.
2. Open VKM1. Enter the customer number and execute. Find the blocked order in the list.
3. Check the credit exposure in FBL5N. If the customer has paid and the exposure is outdated, run program RVKRED77 to update the credit exposure.
4. In VKM1, select the order. If the block is due to outdated exposure and the customer is current, click "Release." If the block is due to a genuine credit limit breach, do not release. Escalate to finance.
5. In VA03, verify the order status has changed from "Credit block" to "Open."

## Verification
- Order status in VA03 shows "Open" with no credit block.
- Delivery can be created in VL01N without error.
- Customer service confirms the order is unblocked.

## Exceptions and Escalation
- If the order is blocked for reasons other than credit (e.g., delivery block, billing block), this article does not apply. Check the incompletion log in VA03.
- If the customer is a new customer and no credit limit is configured, escalate to the master data team.
- If the credit exposure update fails with an error in RVKRED77, escalate to the basis team.

## Related Articles
- KA-SD-2026-014: How to update customer credit exposure in S/4HANA
- RB-CREDIT-001: Credit management runbook for on-call engineers
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Knowledge article writer for SAP operational support.</p>
    <p><strong>Context:</strong> You have a resolved incident, a known workaround, or a common procedure. You need to produce a Knowledge Article that a user or support engineer can follow without asking an expert.</p>
    <p><strong>Task:</strong> Create a structured Knowledge Article using the template below. Address one specific problem. Write for the audience that will search for it.</p>
    <p><strong>Output format:</strong> Structured Knowledge Article in Markdown with exact steps, prerequisites, verification, and exceptions.</p>

    <ul>
      <li><strong>One problem per article.</strong> If the article covers multiple problems, split it. Users search for symptoms, not modules.</li>
      <li><strong>Write the title in the user's language.</strong> Use the symptom, not the solution. "Order blocked" is better than "Credit management overview."</li>
      <li><strong>Include exact transaction codes, screen names, and field names.</strong> "Check the customer screen" is not enough. Use "VA03, status tab, customer number field."</li>
      <li><strong>State prerequisites before the steps.</strong> Do not let the user discover a missing requirement halfway through.</li>
      <li><strong>Define verification explicitly.</strong> The user must know what success looks like.</li>
      <li><strong>Document exceptions and escalation paths.</strong> Prevent the article from being used in the wrong context.</li>
      <li><strong>Do not invent steps or screenshots.</strong> If you do not have the exact steps, state "Steps to be verified" and flag for review.</li>
      <li><strong>Match the language to the audience.</strong> End users need plain language. Engineers need technical precision.</li>
      <li><strong>Link to Atlas diagnostics</strong> when the article touches documented SAP failure modes. For example, credit block articles should reference <a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/work-documentation-handover/runbook-writing-working-skill/">Runbook Writing Working Skill</a> — Use for the full operational procedure; the knowledge article is the quick answer, the runbook is the complete manual.</li>
      <li><a href="/skill-hub/work-documentation-handover/incident-documentation-working-skill/">Incident Documentation Working Skill</a> — Use to capture the original incident that the knowledge article is based on.</li>
      <li><a href="/skill-hub/work-documentation-handover/process-documentation-working-skill/">Process Documentation Working Skill</a> — Use to document the broader process that the knowledge article fits into.</li>
      <li><a href="/skill-hub/sap-ams/operational-knowledge-capture-working-skill/">Operational Knowledge Capture Working Skill</a> — Use to capture the expert knowledge that feeds into knowledge articles.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a> — Diagnostic context for credit block articles.</li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — Diagnostic context for IDoc reprocessing articles.</li>
      <li><a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a> — Diagnostic context for order block articles.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of knowledge management and technical writing practices. It is not official KCS, ITIL, or SAP documentation. It focuses on practical, self-service knowledge articles for enterprise and SAP operational support.</p>
    <p>Known limitations: the skill does not cover knowledge base platform administration, search engine optimization, or chatbot training. It produces article content that can be pasted into any knowledge management system. It assumes access to a subject matter expert for verification. It does not cover training materials, certification guides, or comprehensive module documentation. The templates should be adapted to the organization's knowledge base format and tagging scheme.</p>
  </section>
</article>
