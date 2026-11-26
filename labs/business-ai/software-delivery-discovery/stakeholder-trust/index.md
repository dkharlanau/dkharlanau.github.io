---
layout: default
title: "Stakeholder Trust in AI-Assisted Engineering — A Discovery Playbook"
description: "How to discuss engineering value, access concerns, human review, and adoption with different enterprise stakeholders without promising controls that have not been validated."
permalink: /labs/business-ai/software-delivery-discovery/stakeholder-trust/
status: reviewed
verified: false
robots: index,follow
sitemap: true
last_modified_at: 2026-11-26
tags: [business-ai, ai-governance, codex, stakeholder-management, presales, solution-architecture]
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li><a href="/labs/business-ai/software-delivery-discovery/">Software Delivery Discovery</a></li><li aria-current="page">Stakeholder Trust</li></ol></nav>
<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise AI / Consulting playbook</p>
      <h1>One AI initiative.<br>Different reasons to trust it.</h1>
      <p>Engineering leadership, product owners, platform teams, and governance stakeholders can agree that delivery needs to improve while disagreeing about what a safe improvement looks like. Learn to discover the concern behind each question before proposing a control or a product.</p>
      <a class="research-canvas__button" href="#stakeholder-outcomes">Map the stakeholders <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <div>
      <p><strong>Core rule:</strong> a stakeholder question is evidence about a need for confidence, not proof of a technical defect. Discover the consequence the stakeholder wants to avoid, then decide which evidence or specialist is needed.</p>
      <p><strong>Boundary:</strong> early discovery can document open access, oversight, and data questions. It cannot establish that a particular workspace, model, integration, or deployment meets the customer's policies.</p>
      <p><strong>Delivery principle:</strong> an agent can prepare engineering work; accountable people and established change controls decide what is accepted and released.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="stakeholder-outcomes" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Stakeholder mapping</p>
      <h2>The same bottleneck creates different business pressures</h2>
      <p>Suppose pull requests routinely wait for review. Do not repeat one generic productivity claim to every participant. Connect the delay to the decision each person owns.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Stakeholder</th><th scope="col">Decision they care about</th><th scope="col">Useful question</th></tr></thead><tbody>
        <tr><th scope="row">Engineering executive</th><td>Whether current capacity can meet committed delivery goals.</td><td>Which engineering delays actually constrain throughput?</td></tr>
        <tr><th scope="row">Platform owner</th><td>Whether teams can use a consistent, supportable workflow.</td><td>Where does tool or process variation create avoidable rework?</td></tr>
        <tr><th scope="row">Product or delivery owner</th><td>Whether important changes reach customers predictably.</td><td>Which review delays have affected promised releases?</td></tr>
        <tr><th scope="row">Risk or governance owner</th><td>Whether changes remain attributable, reviewable, and controllable.</td><td>Who may propose a change, who must approve it, and what evidence must remain?</td></tr>
        <tr><th scope="row">Developer or reviewer</th><td>Whether the tool helps with real work without creating more review burden.</td><td>What information would make a suggested diff easier to evaluate?</td></tr>
      </tbody></table>
    </div>
    <p><strong>Qualification consequence:</strong> a feature that reduces draft preparation time is not necessarily the feature that addresses the executive's delay, the platform team's consistency problem, or the governance owner's concern. Keep each stakeholder's desired evidence separate.</p>
  </section>

  <section class="research-canvas__inventory" id="trust-questions" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Trust discovery / Listen for the underlying risk</p>
      <h2>Three concern types to recognize early</h2>
      <p>Use this guide to categorize the next question to ask. It is not a substitute for security review or architecture design.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Area</th><th scope="col">What the customer may really need</th><th scope="col">Appropriate early response</th></tr></thead><tbody>
        <tr><th scope="row">Context and access</th><td>Confidence that the tool only receives appropriate repositories, tickets, data, and system access.</td><td>Identify required sources and data sensitivity; record who can authorize access and which restrictions must be checked.</td></tr>
        <tr><th scope="row">Agent actions and control</th><td>Confidence that delegated work cannot silently exceed its approved scope or bypass necessary review.</td><td>Identify intended actions, target environment, human checkpoints, and who accepts or rejects output.</td></tr>
        <tr><th scope="row">Visibility and accountability</th><td>Confidence that the organization can understand usage, investigate incidents, and evaluate outcomes.</td><td>Ask which activity, cost, outcome, and review records are required; verify product-specific availability later.</td></tr>
      </tbody></table>
    </div>
    <p><strong>Two people, one question:</strong> “Which systems can the agent reach?” may mean data exposure to Security, technical usefulness to Engineering, or rollout risk to an executive sponsor. Ask what decision the answer will support before delivering a long technical explanation.</p>
  </section>

  <section class="research-canvas__inventory" id="operating-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Operating model / People and delegated work</p>
      <h2>Make human accountability an explicit part of the proposal</h2>
      <p>An engineering agent can assist across several steps, but the organization needs to decide how tasks are selected, where work runs, what evidence comes back, and who is authorized to approve the result. Delegation must not be confused with autonomous release authority.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Moment</th><th scope="col">Illustrative responsibility</th><th scope="col">Question to resolve</th></tr></thead><tbody>
        <tr><th scope="row">Select</th><td>Engineering owner chooses one bounded task with real business value.</td><td>What is in scope, and what is explicitly out of scope?</td></tr>
        <tr><th scope="row">Prepare</th><td>Technical owner confirms repository context, approved data, and execution prerequisites.</td><td>Which environment can actually reproduce the issue?</td></tr>
        <tr><th scope="row">Delegate</th><td>Agent investigates and prepares a proposed artifact within the authorized task.</td><td>Which commands, reads, and writes are expected or restricted?</td></tr>
        <tr><th scope="row">Verify</th><td>Engineers inspect the diff, tests, assumptions, and remaining failures.</td><td>What must pass before the change is acceptable?</td></tr>
        <tr><th scope="row">Approve</th><td>Authorized people apply the normal code review, release, and transport process.</td><td>Who has decision rights and how is that decision recorded?</td></tr>
        <tr><th scope="row">Learn</th><td>Delivery and platform owners review adoption, quality, cost, and rework.</td><td>What did the experiment actually improve?</td></tr>
      </tbody></table>
    </div>
    <p><strong>Illustrative SAP boundary:</strong> an assistant may prepare tests or a patch for a customer-field mapping enhancement. An ABAP reviewer and functional owner still check the behavior against requirements. Production transport remains subject to the actual system's established approval process. Do not put sensitive customer test extracts into a public repository or publication.</p>
  </section>

  <section class="research-canvas__inventory" id="context-patterns" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Context / Adapt the message</p>
      <h2>Start from organizational constraints, not industry stereotypes</h2>
      <p>Organizations often combine several patterns. Use these examples to choose a discovery angle, not to infer capabilities, compliance, or maturity from a company label.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Situation</th><th scope="col">What to lead with</th><th scope="col">What to avoid assuming</th></tr></thead><tbody>
        <tr><th scope="row">Software-heavy organization</th><td>Recurring multi-repository tasks, validation throughput, and release handoffs.</td><td>That the primary constraint is code-writing speed.</td></tr>
        <tr><th scope="row">High-control environment</th><td>Inspectability, accountable approvals, data boundaries, and safe evaluation.</td><td>That any specific compliance or governance requirement is already satisfied.</td></tr>
        <tr><th scope="row">Legacy modernization</th><td>Code comprehension, dependency tracing, regression protection, and scoped maintenance.</td><td>That a complex landscape can be transformed in one automated step.</td></tr>
        <tr><th scope="row">Inconsistent engineering practices</th><td>Shared review criteria, documentation quality, and a repeatable pilot process.</td><td>That adding an AI tool fixes missing engineering discipline.</td></tr>
        <tr><th scope="row">Established engineering platform</th><td>Quality-adjusted throughput and controlled reuse across teams.</td><td>That local pilot results automatically scale across the organization.</td></tr>
      </tbody></table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="trust-evidence-brief" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Workshop artifact / Evidence brief</p>
      <h2>Capture who needs confidence, what would prove it, and who will verify</h2>
      <p>Before moving into solution design, keep a compact record separating stakeholder statements from assumptions and design commitments.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>Example: controlled code review pilot (fictional)</h3>
        <ul>
          <li><strong>Reported concern:</strong> the engineering owner wants review assistance; the governance team is unsure what agent access entails.</li>
          <li><strong>Possible task:</strong> generate review findings for one internal repository change.</li>
          <li><strong>Unknowns:</strong> approved code exposure, tool permissions, evaluation location, required activity visibility.</li>
          <li><strong>Evidence needed:</strong> scoped repository, representative PR, review rubric, accountable reviewer, and approved evaluation boundary.</li>
          <li><strong>Next action:</strong> technical and security owners jointly validate prerequisites before selecting an execution setup.</li>
        </ul>
      </div>
      <div>
        <h3>Customer-ready explanation</h3>
        <blockquote><p>“We can start with one engineering task that your team already knows how to review. Before running it, we should confirm the code and tools it needs, who can authorize that access, and what evidence reviewers expect. Then we can evaluate the benefit without treating a successful demonstration as approval for wider deployment.”</p></blockquote>
        <p><strong>Stop condition:</strong> if required data access cannot be approved or results cannot be independently checked, do not promise that the proposed evaluation is ready.</p>
      </div>
    </div>
    <p><strong>Practice:</strong> a security lead, a VP of Engineering, and a product owner all ask, “What will Codex be allowed to change?” Give each a different 30-second answer. Separate what is known, what remains undecided, and who owns the decision.</p>
  </section>


  <section class="research-canvas__inventory" id="adoption-confidence" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Enterprise adoption / Beyond technical fit</p>
      <h2>A working demo is not an operating model</h2>
      <p>A team can prove that an agent solves a sample issue yet remain unable to use it in regular delivery. People need a repeatable way to choose tasks, prepare context, inspect results, handle mistakes, and learn from real usage. Technical success and adoption confidence are therefore two different decisions.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Confidence question</th><th scope="col">What could reveal a gap</th><th scope="col">Evidence to collect</th></tr></thead>
        <tbody>
          <tr><th scope="row">Will engineers choose to use it?</th><td>Developers test the demo but return to their old process.</td><td>Task-level repeat use, feedback from actual users, and reasons for non-use.</td></tr>
          <tr><th scope="row">Can teams change their routines?</th><td>Agent output is produced, but nobody knows who reviews or accepts it.</td><td>A documented task-to-review workflow with named decision owners.</td></tr>
          <tr><th scope="row">Can leaders see what is happening?</th><td>Usage counts exist, but quality, rework, and operational consequences are invisible.</td><td>Agreed measures of accepted work, errors, human effort, and follow-up actions.</td></tr>
          <tr><th scope="row">Can objections be resolved?</th><td>Security, engineering, and management raise concerns without a clear route to a decision.</td><td>Concern log, accountable owner, required proof, and decision status.</td></tr>
          <tr><th scope="row">Can the scope expand safely?</th><td>The pilot worked in one repository, but other teams have different tools and constraints.</td><td>Prerequisites and verification for each proposed new team or workflow.</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Key distinction:</strong> adoption is not the number of activated accounts, and trust is not the absence of reported complaints. Look for people repeatedly completing meaningful, accepted work with a clear understanding of responsibility and limitations.</p>
  </section>

  <section class="research-canvas__inventory" id="pilot-to-practice" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Controlled expansion / Decision gates</p>
      <h2>Earn the right to scale in small steps</h2>
      <p>Each stage should close a different uncertainty. Moving forward is a decision based on evidence, not simply the end of a calendar period.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Stage</th><th scope="col">What to learn</th><th scope="col">Go / adjust / stop decision</th></tr></thead>
        <tbody>
          <tr><th scope="row">Select</th><td>Identify one valuable, recurring engineering job and the team responsible for it.</td><td>Proceed only if task boundaries and reviewers are clear.</td></tr>
          <tr><th scope="row">Rehearse</th><td>Try representative work with approved code, tools, environment, and a baseline for comparison.</td><td>Inspect whether outputs are correct and reviewers can recognize failure.</td></tr>
          <tr><th scope="row">Use with a small team</th><td>Observe whether engineers voluntarily reuse the workflow in ordinary tasks.</td><td>Check accepted outcomes, review burden, friction, and user concerns.</td></tr>
          <tr><th scope="row">Expand carefully</th><td>Test whether the same pattern works in another repository, team, or task family.</td><td>Reconfirm prerequisites, ownership, approval paths, and expected outcomes.</td></tr>
          <tr><th scope="row">Operate</th><td>Keep reviewing costs, quality, incidents, training needs, and whether the original business problem improved.</td><td>Maintain, narrow, retrain, or stop the workflow when evidence changes.</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Design boundary:</strong> this is an adoption decision model, not an implementation or security architecture. Permissions, data processing, runtime controls, monitoring availability, and region requirements need validation for the selected product, workspace, and customer's policies before broader operation.</p>
  </section>

  <section class="research-canvas__inventory" id="adoption-evidence" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Adoption metrics / Separate activity from impact</p>
      <h2>Measure three different things before celebrating a rollout</h2>
      <p>A high number of agent sessions can reflect curiosity or repeated failure. A useful adoption assessment distinguishes participation, effective use, and business outcomes.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Evidence layer</th><th scope="col">Illustrative measure</th><th scope="col">Interpretation risk</th></tr></thead>
        <tbody>
          <tr><th scope="row">Engagement</th><td>Share of eligible engineers who choose the tool again on relevant tasks.</td><td>Mandatory use or one-off experiments can inflate apparent acceptance.</td></tr>
          <tr><th scope="row">Effective work</th><td>Accepted tasks per eligible task, including review time, corrections, and discarded outputs.</td><td>Counting generated patches without acceptance overstates the result.</td></tr>
          <tr><th scope="row">Delivery impact</th><td>Change lead time, rework frequency, or release confidence for the affected workflow.</td><td>Parallel process or staffing changes may explain the outcome.</td></tr>
          <tr><th scope="row">Guardrails</th><td>Defects, security or data-handling incidents, unauthorized actions, and reviewer overrides.</td><td>“No incidents” is weak evidence when observation and reporting are incomplete.</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Evaluation rule:</strong> define denominators, a baseline, review ownership, and acceptable limits before testing. The first pilot may only justify a second experiment, not a claim of enterprise ROI.</p>
    <p><strong>Related:</strong> <a href="/labs/business-ai/software-delivery-discovery/#cost-per-accepted-task">cost per accepted engineering task</a> provides a more meaningful economic view than cost per model call.</p>
  </section>

  <section class="research-canvas__inventory" id="adoption-resistance" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Change management / Learn from resistance</p>
      <h2>Do not treat every objection as fear of AI</h2>
      <p>Developer hesitation can be rational: unclear task scope, unreliable suggestions, extra review effort, lack of approved access, or concern about how individual performance will be judged. Ask what made the last attempt inconvenient or risky before planning more training.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>Typical resistance signals</h3>
        <ul>
          <li>“The patch looks plausible, but verifying it takes longer than doing the task.”</li>
          <li>“The agent cannot see the test harness that reproduces our failures.”</li>
          <li>“I do not know whether I am allowed to provide this repository.”</li>
          <li>“We are being measured on tool usage rather than accepted delivery work.”</li>
        </ul>
      </div>
      <div>
        <h3>Useful responses</h3>
        <p><strong>Quality gap:</strong> narrow the task and strengthen acceptance checks.</p>
        <p><strong>Environment gap:</strong> validate available context, tools, and approved execution location.</p>
        <p><strong>Policy gap:</strong> route access questions to the authorized owner rather than improvising permission.</p>
        <p><strong>Incentive gap:</strong> measure accepted results and developer experience instead of activity volume.</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="executive-adoption-narrative" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Executive conversation / Proposal without overclaiming</p>
      <h2>Offer a controlled path to evidence, not a transformation promise</h2>
      <div class="ecg-decision-columns">
        <div>
          <h3>Product demonstration alone</h3>
          <p>“The model performed well on a sample task, so we should deploy it to every engineer.”</p>
          <p>This skips operational readiness, everyday acceptance, workload fit, controls, and the cost of changes to current processes.</p>
        </div>
        <div>
          <h3>Decision-ready recommendation</h3>
          <blockquote><p>“We can start with one recurring engineering task and a small group of reviewers. We will check whether the work is genuinely easier to complete, how often the result is accepted, and what control gaps remain. If the evidence is positive, we can test the same approach with another team before proposing wider adoption.”</p></blockquote>
          <p>This gives leaders a useful next decision without suggesting that a pilot has already proved organization-wide benefit.</p>
        </div>
      </div>
    </header>
    <div class="research-canvas__table-wrap">
      <h3>Redirect a feature discussion</h3>
      <table>
        <thead><tr><th scope="col">Conversation starts with</th><th scope="col">Reframe around</th></tr></thead>
        <tbody>
          <tr><th scope="row">Autocomplete and editor convenience</th><td>Which repeatable engineering job is most costly today?</td></tr>
          <tr><th scope="row">Model benchmark rankings</th><td>Which accepted-result measure would make the customer change its workflow?</td></tr>
          <tr><th scope="row">Vendor feature inventory</th><td>Which option can meet the actual task, review, and operating requirements?</td></tr>
          <tr><th scope="row">Positive developer feedback</th><td>Does usage persist, deliver acceptable quality, and fit the organization's decision process?</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Partner role:</strong> help the client isolate the workflow, define success, involve technical and governance owners, observe adoption, and recommend the next decision. Product or compliance claims still require authoritative evidence and specialist validation.</p>
  </section>

  <section class="research-canvas__inventory" id="adoption-sap-case" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SAP simulation / Workshop exercise</p>
      <h2>One ABAP team accepts the pilot. Another refuses.</h2>
      <p>A fictional SAP program tests AI assistance for documenting enhancements and proposing regression cases. The first development team reports useful output. A second team declines because its critical dependencies are only available inside a restricted SAP system.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>Weak program response</h3>
        <p>Assume the second team is resistant to change, mandate tool usage, and report the first team's successful tasks as proof that the approach can scale.</p>
      </div>
      <div>
        <h3>Stronger architecture response</h3>
        <p>Identify which source context is absent, whether an approved evaluation environment can be made available, and how the required behavior would be checked. If not, exclude that task family from the rollout and choose a different candidate instead.</p>
      </div>
    </div>
    <p><strong>Interview prompt (B2):</strong> “Your sponsor wants enterprise-wide adoption after a successful pilot, but developers in another SAP team report missing system context and higher review effort. How would you advise the sponsor, and what evidence would you require before expansion?”</p>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">menu_book</span>
    <div>
      <p><strong>Read further:</strong> <a href="/labs/business-ai/software-delivery-discovery/">Software delivery AI qualification</a> · <a href="/labs/ai-ready/">AI Ready: architecture, security and governance</a>.</p>
      <p>For product-specific verification, use OpenAI's current <a href="https://help.openai.com/en/articles/12289294-managing-your-tenant-in-admin-console">workspace administration guidance</a>, <a href="https://help.openai.com/en/articles/20001510-manage-browser-and-computer-use-in-your-enterprise-workspace">enterprise computer and browser controls</a>, and <a href="https://help.openai.com/en/articles/20001407-managing-admin-keys-in-admin-console">admin API permissions documentation</a>. The controls available depend on product, workspace, and permissions; these links are not proof of a customer's configuration.</p>
      <p><strong>Editorial note:</strong> independent learning synthesis and fictional examples. Not an official OpenAI script, a compliance statement, or a reproduction of course content.</p>
    </div>
  </section>
</div>
