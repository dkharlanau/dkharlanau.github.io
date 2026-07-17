---
layout: blog
title: "What Managers Should Know Before Adding AI to SAP Support"
description: "It can search thousands of documents, explain an error message, compare similar incidents and prepare a possible response."
slug: what-managers-should-know-before-adding-ai-to-sap-support
permalink: /blog/what-managers-should-know-before-adding-ai-to-sap-support/
date: 2026-07-17
author: "Dzmitryi Kharlanau"
language: en
category: "SAP AMS operations"
tags:
  - sap-ams-operations
  - sap-ams
  - ai-operations
canonical_url: https://dkharlanau.github.io/blog/what-managers-should-know-before-adding-ai-to-sap-support/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: 19
migration_sequence: 4
migration_date_decision: "No reliable original publication date was present; date records the 2026-07-17 integration."
related_articles:
  - /blog/why-sap-teams-keep-solving-the-same-incidents/
  - /blog/sap-ams-is-not-a-ticket-factory-what-a-better-operating-model-looks-like/
---

## On this page

- [AI does not know your SAP system](#ai-does-not-know-your-sap-system)
- [Start with the support problem, not the AI product](#start-with-the-support-problem-not-the-ai-product)
- [Three different levels of AI in SAP support](#three-different-levels-of-ai-in-sap-support)
- [Level 1: AI provides information](#level-1-ai-provides-information)
- [Level 2: AI recommends an action](#level-2-ai-recommends-an-action)
- [Level 3: AI executes an action](#level-3-ai-executes-an-action)
- [The safest use cases are often not the most exciting](#the-safest-use-cases-are-often-not-the-most-exciting)
- [AI quality depends on operational knowledge](#ai-quality-depends-on-operational-knowledge)
- [Current information matters in SAP](#current-information-matters-in-sap)
- [Access control is more complex than chat access](#access-control-is-more-complex-than-chat-access)
- [Human review is not one control](#human-review-is-not-one-control)
- [AI confidence is not business confidence](#ai-confidence-is-not-business-confidence)
- [Read-only is a useful first boundary](#read-only-is-a-useful-first-boundary)
- [Evaluation must use real support cases](#evaluation-must-use-real-support-cases)
- [The baseline must exist before the pilot](#the-baseline-must-exist-before-the-pilot)
- [Productivity claims need careful reading](#productivity-claims-need-careful-reading)
- [AI may reduce junior work and increase senior review](#ai-may-reduce-junior-work-and-increase-senior-review)
- [AI should not become a new source of incidents](#ai-should-not-become-a-new-source-of-incidents)
- [Agentic AI changes the control model](#agentic-ai-changes-the-control-model)
- [A practical risk model for SAP support AI](#a-practical-risk-model-for-sap-support-ai)
- [1. Data sensitivity](#1-data-sensitivity)
- [2. Decision impact](#2-decision-impact)
- [3. Action reversibility](#3-action-reversibility)
- [4. Detectability](#4-detectability)
- [A better implementation sequence](#a-better-implementation-sequence)
- [Questions managers should ask before approval](#questions-managers-should-ask-before-approval)
- [What a good first year should produce](#what-a-good-first-year-should-produce)
- [AI should improve decisions, not only produce answers](#ai-should-improve-decisions-not-only-produce-answers)
- [SAP support AI readiness checklist](#sap-support-ai-readiness-checklist)
- [Sources and further reading](#sources-and-further-reading)

AI can summarize a ticket in seconds.

It can search thousands of documents, explain an error message, compare similar incidents and prepare a possible response.

This is useful.

But it does not mean that AI understands why a customer invoice is wrong, whether an IDoc can be safely reprocessed or which team is allowed to change a business partner.

SAP support is not only a knowledge problem.

It is also a problem of context, ownership, evidence and controlled action.

This is where many AI initiatives become confused. A company sees a convincing demonstration and assumes that the difficult part has been solved.

The model gives a good answer.

The real question is whether the organization can trust that answer in production.

## AI does not know your SAP system

A general AI model may know SAP terminology.

It may explain:

- what an IDoc is;
- how pricing conditions work;
- why a delivery block can appear;
- what business partner replication means;
- which transaction or application is normally used;
- which configuration areas may be relevant.

That is not the same as understanding your landscape.

Your SAP environment contains local decisions:

- custom code;
- specific configuration;
- old workarounds;
- local process variants;
- external interfaces;
- unusual master data rules;
- provider boundaries;
- manual controls;
- historical decisions that nobody documented properly.

The technically correct general answer may be wrong for your company.

For example, an AI assistant may suggest reprocessing a failed message.

Before doing that, someone must know:

- whether the message is idempotent;
- whether the target system already processed part of it;
- whether reprocessing can create a duplicate;
- whether business data was corrected;
- whether message sequence matters;
- whether reconciliation is required;
- who owns the business decision.

The AI may understand the error.

It may not understand the consequence of the action.

## Start with the support problem, not the AI product

A common AI initiative begins with a tool.

Management buys access to a model, assistant or platform. A project team is then asked to find use cases.

This often produces a long list:

- summarize tickets;
- write documentation;
- recommend solutions;
- generate test cases;
- classify incidents;
- analyze logs;
- automate corrections;
- create reports;
- predict failures;
- build autonomous agents.

The list looks impressive because it contains many possibilities.

It does not show which problem is worth solving.

A better starting point is operational evidence:

- Which support activities consume the most time?
- Where do consultants repeat the same analysis?
- Which incidents wait because information is missing?
- Which knowledge is difficult to find?
- Which tasks are low risk but highly repetitive?
- Which decisions depend too much on one expert?
- Which failures could be detected earlier?
- Where does poor communication delay recovery?

AI should enter the operating model at a specific point of friction.

It should not become another technology looking for work.

## Three different levels of AI in SAP support

Managers should separate three levels of AI capability.

They create very different risks.

## Level 1: AI provides information

At the first level, AI helps a person understand the situation.

Examples include:

- summarizing a long incident history;
- finding similar tickets;
- explaining an SAP error message;
- searching internal support documentation;
- identifying relevant SAP Notes or Knowledge Base Articles;
- describing custom code;
- translating technical language for business users;
- preparing a list of diagnostic questions.

The AI does not make a production change.

A human reviews the output and decides what to do.

This is usually the safest starting point.

## Level 2: AI recommends an action

At the second level, AI moves from information to advice.

It may recommend:

- which support team should receive the incident;
- which logs should be checked;
- which known error matches the symptoms;
- whether a recent transport may be related;
- which test cases should be executed;
- whether a failed process can be reprocessed;
- which configuration area may contain the cause.

The value can be higher, but the risk also increases.

The recommendation may sound confident even when important context is missing.

The user must be able to see:

- which evidence was used;
- which assumptions were made;
- which sources support the recommendation;
- what uncertainty remains;
- what could happen if the recommendation is wrong.

A recommendation without visible evidence is difficult to govern.

## Level 3: AI executes an action

At the third level, AI can act.

It may:

- update a ticket;
- start a workflow;
- restart a job;
- reprocess a message;
- create a service request;
- modify master data;
- trigger a test;
- prepare or deploy a change;
- communicate with another system.

This is where an assistant becomes an agent.

SAP currently describes Joule Assistants as using role and process context to coordinate AI agents and execute workflows across business functions. SAP also offers Joule Studio for building agents and workflows, alongside role-specific products such as Joule for Consultants.

These capabilities create new possibilities.

They also make control design more important.

A wrong summary is inconvenient.

A wrong production action may affect orders, invoices, stock, payments or financial reporting.

## The safest use cases are often not the most exciting

Companies often begin with the most ambitious idea:

> Let us build an AI agent that resolves SAP incidents automatically.

This is usually too broad.

Incident resolution contains several different activities:

1. understanding the report;
2. collecting evidence;
3. identifying the affected process;
4. finding similar cases;
5. forming a diagnosis;
6. selecting a correction;
7. evaluating business risk;
8. executing the correction;
9. checking the result;
10. communicating and documenting the decision.

AI does not need to own the full chain to create value.

It may be enough to improve two or three steps.

Good early use cases include:

### Ticket enrichment

AI can extract important information from the incident and add:

- business process;
- system;
- organizational unit;
- affected document;
- error message;
- recent change;
- possible related incidents.

The consultant starts with better context.

### Incident summarization

Long tickets often contain repeated messages, copied logs and several failed attempts.

AI can produce a concise timeline:

- what happened;
- what was checked;
- what changed;
- what remains unknown.

### Similar-case retrieval

The model can help find earlier incidents with related symptoms, causes or process context.

This is more useful than simple keyword search when ticket descriptions are inconsistent.

### Knowledge search

A support assistant can search approved internal procedures, architecture records, known errors and official SAP sources.

SAP positions Joule for Consultants as a conversational solution grounded in SAP-curated knowledge, including SAP Notes and Knowledge Base Articles, and allows organizations to extend that context with their own standards and project material. These are SAP’s product claims and should be validated in the customer’s actual scenario.

### Evidence collection

AI can help prepare a diagnostic package:

- relevant logs;
- document numbers;
- failed steps;
- change references;
- related alerts;
- ownership information.

It reduces search time without making the final decision.

### Communication support

AI can translate technical findings into a clear update for business users.

This sounds simple, but poor communication creates unnecessary escalations and duplicate tickets.

These use cases are less dramatic than an autonomous agent.

They are also easier to evaluate and control.

## AI quality depends on operational knowledge

Many companies assume that AI will solve their documentation problem.

Often, it exposes the problem instead.

An AI assistant cannot reliably answer questions when its source material contains:

- old procedures;
- conflicting instructions;
- screenshots without context;
- undocumented exceptions;
- copied ticket comments;
- incorrect ownership data;
- several versions of the same process;
- technical details without business meaning.

The model may combine this information into a fluent answer.

Fluency can hide inconsistency.

Before connecting AI to the support knowledge base, the organization should understand what the knowledge base actually contains.

At minimum, important records should identify:

- the business process;
- the affected systems;
- the verified symptom;
- the confirmed cause;
- the approved workaround;
- the permanent correction;
- the owner;
- the last review date;
- the source of the information;
- important restrictions.

AI does not remove the need for knowledge governance.

It makes weak knowledge easier to distribute.

## Current information matters in SAP

SAP support knowledge changes.

The correct answer may depend on:

- product version;
- deployment model;
- active scope;
- feature availability;
- support package;
- cloud release;
- configuration;
- country;
- industry;
- licensing;
- a recent SAP Note;
- whether the system is ECC, S/4HANA or a cloud edition.

A support assistant should not only return an answer.

It should show why the answer applies.

Useful output includes:

- source;
- publication or update date;
- relevant product and version;
- system-specific evidence;
- confidence or uncertainty;
- conditions under which the advice is valid.

An answer without this context can be technically correct and operationally useless.

## Access control is more complex than chat access

Giving an AI assistant access to SAP support data creates several questions.

The assistant may see:

- user names;
- customer or supplier information;
- financial data;
- employee information;
- system configuration;
- source code;
- security details;
- interface payloads;
- production logs;
- confidential project records.

Managers need to know:

- Which data is sent to the model?
- Where is it processed?
- Is it retained?
- Can it be used for model training?
- Which users can retrieve it?
- Are permissions inherited from the source system?
- Can the assistant combine information from sources that users could not normally access together?
- How are prompts and outputs logged?
- How are sensitive values masked?
- What happens when a user pastes data into an unapproved tool?

SAP states that customer data entered into its AI technologies remains subject to the applicable cloud agreement and that it does not share customer data with third-party model providers for training their models. SAP also describes tenant isolation, encryption, masking and filtering among its security controls. The exact contractual and technical position still needs to be checked for the specific service, region and subscription.

Vendor security statements are an input to due diligence.

They are not a replacement for it.

## Human review is not one control

AI proposals often include the sentence:

> A human remains in the loop.

This sounds safe, but it is incomplete.

Which human?

What information will that person receive?

Does the person have time to review it?

Can the person reject the recommendation?

Is the reviewer qualified to understand the risk?

Will the interface encourage quick approval?

Is the person reviewing every action or only exceptions?

A human click does not automatically create meaningful control.

Human oversight should match the action.

For a draft ticket summary, a normal consultant review may be enough.

For master data changes, the reviewer may need business ownership.

For financial postings, the control may require segregation of duties.

For interface reprocessing, the reviewer may need to understand duplication and sequence risks.

The important question is not whether a human is present.

It is whether the decision authority is correctly designed.

## AI confidence is not business confidence

A model may provide a probability or confidence score.

This number should not be confused with business safety.

Suppose the AI is 95% accurate when classifying incidents.

That may be excellent for ticket routing.

It may be unacceptable for autonomous financial corrections.

Risk depends on both probability and impact.

A useful decision model considers:

- How often can the AI be wrong?
- How large is the possible impact?
- Can the action be reversed?
- Can the result be checked immediately?
- Is duplicate processing possible?
- Does the action affect financial or regulated data?
- Is an approval required?
- Is there a safe fallback?

A low-risk action can tolerate more uncertainty.

A high-impact action requires stronger evidence, controls and often human approval.

## Read-only is a useful first boundary

The first production AI capability should usually observe and recommend before it acts.

Read-only access allows the organization to learn:

- what the model can understand;
- which data is missing;
- where permissions fail;
- how often answers are correct;
- whether users follow weak suggestions;
- which source documents need improvement;
- where business context is required.

This creates an evaluation period without giving the model direct authority over production transactions.

A good sequence is:

1. summarize;
2. retrieve;
3. recommend;
4. prepare an action;
5. execute with approval;
6. execute a narrow reversible action automatically.

Skipping directly to the final stage creates unnecessary risk.

## Evaluation must use real support cases

A polished demonstration proves little.

AI should be tested against real operational cases, including difficult ones.

The evaluation set should contain:

- common incidents;
- rare incidents;
- incomplete tickets;
- misleading symptoms;
- outdated documentation;
- similar errors with different causes;
- multilingual reports;
- custom code;
- cross-system failures;
- incidents where no safe recommendation is possible.

For each case, evaluate more than whether the final answer looks reasonable.

Measure:

- factual accuracy;
- source quality;
- correct use of system context;
- recognition of uncertainty;
- missing evidence;
- harmful recommendations;
- time saved;
- reviewer effort;
- consistency across repeated runs.

An important test is whether the AI knows when not to answer.

A safe response may be:

> There is not enough evidence to recommend reprocessing. Check whether the target document already exists.

This is more valuable than a confident guess.

## The baseline must exist before the pilot

Without a baseline, almost every AI pilot can be described as successful.

The team can show that:

- users liked the interface;
- summaries looked useful;
- answers appeared quickly;
- the model handled several examples.

But management cannot calculate value.

Before the pilot, record:

- current handling time;
- time spent searching for information;
- number of ticket transfers;
- first-contact resolution;
- repeated analysis effort;
- escalation volume;
- rework caused by incorrect diagnosis;
- time needed to prepare communication;
- reviewer effort.

Then compare the AI-supported process with the existing one.

The useful metric is not the number of AI interactions.

It is the amount of reliable work removed or improved.

## Productivity claims need careful reading

AI product pages often contain productivity estimates.

For example, SAP states that Joule for Consultants can reduce knowledge-search time and accelerate parts of consulting work, while also publishing estimates for code interpretation and project delivery. These are vendor-reported figures with stated conditions and should not be treated as an automatic business case for a specific AMS organization.

A real business case depends on:

- current process quality;
- support volume;
- user adoption;
- knowledge readiness;
- licensing and implementation cost;
- integration effort;
- evaluation effort;
- governance;
- ongoing maintenance;
- time saved after human review.

Saving ten minutes in an activity that occurs once per month has little value.

Saving five minutes in a controlled activity performed thousands of times may matter.

## AI may reduce junior work and increase senior review

A hidden effect of AI is the movement of work between roles.

AI can help junior consultants:

- find information;
- structure analysis;
- understand unfamiliar concepts;
- prepare first drafts;
- compare possible causes.

This can improve productivity.

But senior experts may need to spend more time:

- checking recommendations;
- correcting weak reasoning;
- evaluating unusual cases;
- defining approved patterns;
- maintaining knowledge;
- reviewing autonomous actions.

The total effect depends on whether AI creates better leverage or simply moves quality control upward.

If every AI answer requires a senior consultant to repeat the analysis, the organization has not saved much.

## AI should not become a new source of incidents

An AI support capability is itself a production service.

It needs:

- ownership;
- access management;
- monitoring;
- change control;
- evaluation;
- support procedures;
- usage policies;
- incident handling;
- cost controls;
- fallback processes.

Models, prompts, connectors and source documents change.

An answer that worked three months ago may behave differently after:

- a model update;
- a prompt change;
- a new document source;
- a permission change;
- a product release;
- a process redesign.

The organization should monitor not only availability, but also output quality.

Traditional software tests whether the same input produces the expected result.

Generative AI can produce different wording and reasoning.

Evaluation therefore needs representative cases and acceptable outcome criteria.

## Agentic AI changes the control model

A normal support tool waits for a user command.

An agent may plan several steps, call tools and continue based on intermediate results.

This increases usefulness.

It also increases the number of places where something can go wrong.

An agent may:

- select the wrong tool;
- use incomplete context;
- misunderstand a business condition;
- execute steps in the wrong order;
- repeat an action;
- continue after an unexpected result;
- expose data through a connected system;
- create a larger impact than the original request.

NIST’s Generative AI Profile is intended to help organizations include trustworthiness considerations in the design, development, use and evaluation of generative AI systems. It treats AI risk management as a lifecycle activity, not a one-time approval.

For SAP operations, this means that an agent needs explicit boundaries:

- permitted systems;
- permitted actions;
- transaction limits;
- required approvals;
- stop conditions;
- validation after each step;
- logging;
- rollback;
- escalation to a person.

“Autonomous” should not mean “without limits.”

## A practical risk model for SAP support AI

Managers can classify use cases using four dimensions.

## 1. Data sensitivity

Does the AI process:

- public documentation;
- internal procedures;
- source code;
- production logs;
- personal data;
- financial data;
- credentials or security information?

## 2. Decision impact

Does the output affect:

- ticket administration;
- technical analysis;
- business communication;
- master data;
- logistics execution;
- financial posting;
- compliance;
- access rights?

## 3. Action reversibility

Can the result be easily corrected?

A draft summary is reversible.

A duplicate payment or incorrect stock posting may not be.

## 4. Detectability

Will the organization know quickly when the AI is wrong?

An incorrect ticket category is visible.

An incorrect recommendation that slowly affects many records may remain hidden.

Use cases with sensitive data, high impact, low reversibility and weak detectability need the strongest controls.

## A better implementation sequence

A practical SAP support AI programme can follow eight steps.

### Step 1: Choose one measurable pain

Select a narrow problem such as:

- slow knowledge search;
- poor ticket quality;
- repeated incident analysis;
- unclear incident summaries;
- inefficient evidence collection.

Avoid “improve SAP support with AI.”

It is too broad to evaluate.

### Step 2: Define the current process

Document:

- who performs the task;
- what data is used;
- where time is lost;
- which decisions are made;
- which risks exist;
- what good output looks like.

### Step 3: Prepare approved knowledge

Identify trustworthy sources.

Remove or label:

- duplicates;
- outdated instructions;
- unverified workarounds;
- private notes;
- conflicting procedures.

### Step 4: Define the authority boundary

Decide whether the AI may:

- read;
- summarize;
- recommend;
- prepare an action;
- execute after approval;
- execute automatically.

Do not leave this unclear.

### Step 5: Test with historical cases

Use known outcomes to compare AI results with actual expert decisions.

Include failure cases, not only easy examples.

### Step 6: Run a controlled pilot

Limit:

- users;
- systems;
- data;
- use cases;
- duration;
- permissions.

Record incorrect and rejected outputs.

### Step 7: Compare against the baseline

Measure:

- time saved;
- quality;
- rework;
- reviewer effort;
- adoption;
- risk events;
- total cost.

### Step 8: Expand only after control works

Increase action rights gradually.

A successful search assistant is not automatically ready to reprocess production messages.

## Questions managers should ask before approval

Before funding an AI use case in SAP support, managers should ask:

1. Which operational problem are we solving?
2. What is the current cost of that problem?
3. What evidence will the AI use?
4. Is that evidence current and approved?
5. Which SAP and non-SAP systems provide context?
6. What happens when information is missing?
7. Can users see the sources behind the answer?
8. What action can the AI take?
9. Who approves high-impact actions?
10. Can the action be reversed?
11. How will incorrect output be detected?
12. Which data leaves the source system?
13. Where is that data processed and retained?
14. How will permissions be enforced?
15. How will the model be evaluated after updates?
16. What is the fallback when the AI is unavailable?
17. Which role owns the AI service?
18. How will we prove that it created value?

If these questions cannot be answered, the initiative is not ready for production.

## What a good first year should produce

A realistic first year of AI in SAP support should not be judged by the number of agents created.

It should produce:

- one or two verified high-value use cases;
- a clean set of operational knowledge;
- a repeatable evaluation method;
- clear action and approval boundaries;
- better visibility into support work;
- measured time savings;
- evidence of output quality;
- a governance model that can support later use cases.

This foundation is more valuable than a large catalogue of demonstrations.

## AI should improve decisions, not only produce answers

SAP support already produces many answers.

Consultants write comments, users receive instructions, providers prepare reports and teams document workarounds.

The deeper problem is often decision quality.

Does the organization know:

- which issue should be corrected permanently;
- which workaround is safe;
- which incident is related to a change;
- which process owner must act;
- which automation creates more risk than value;
- which knowledge can be trusted?

AI can help bring evidence together faster.

It cannot remove accountability.

The strongest use of AI in SAP support is not replacing the consultant who understands the process.

It is removing the repetitive search, collection and drafting work that prevents that consultant from investigating the real problem.

The right question is therefore not:

> How much of SAP support can AI automate?

It is:

> Where can AI improve speed without weakening judgment, ownership and control?

That question leads to fewer impressive demonstrations.

It also leads to better production systems.

---

## SAP support AI readiness checklist

- [ ] A specific operational problem has been selected.
- [ ] The current effort and quality baseline are known.
- [ ] Approved knowledge sources are defined.
- [ ] Outdated and unverified content is controlled.
- [ ] Product and version context is available.
- [ ] Data sensitivity has been assessed.
- [ ] User permissions are preserved.
- [ ] AI outputs show supporting evidence.
- [ ] Uncertainty and missing context are visible.
- [ ] Human review has a clear owner and purpose.
- [ ] Production actions are limited and reversible.
- [ ] Historical support cases are used for evaluation.
- [ ] Incorrect recommendations are recorded.
- [ ] Model and prompt changes are governed.
- [ ] The AI service has an operational owner.
- [ ] Value is measured after reviewer effort and total cost.

## Sources and further reading

SAP currently presents Joule as a family of assistants, agents and role-specific AI capabilities. SAP states that Joule Assistants use role and process context to coordinate agents and workflows, while Joule for Consultants is grounded in SAP-curated knowledge and can be extended with organization-specific material.

SAP’s responsible AI materials describe an approach based on ethics, security and compliance, including human oversight, transparency, risk classification and impact assessment. SAP also publishes information about customer-data processing, third-party models and AI security controls. These details should be validated against the specific contract and deployed service.

NIST’s Generative AI Profile complements the AI Risk Management Framework and provides voluntary guidance for incorporating trustworthiness into the design, use and evaluation of generative AI systems.

*Reviewed: July 2026. SAP AI products, commercial terms, regional availability and technical capabilities can change. Product-specific claims and data-processing conditions should be verified in current SAP documentation and contracts.*

## Continue exploring

- [Why SAP Teams Keep Solving the Same Incidents](/blog/why-sap-teams-keep-solving-the-same-incidents/)
- [Knowledge Atlas](/atlas/)
- [SAP services](/services/)
- Previous in the migration: [Why SAP AMS Costs Keep Growing Even When Ticket Volumes Fall](/blog/why-sap-ams-costs-keep-growing-even-when-ticket-volumes-fall/)
- Next in the migration: [Why More SAP Monitoring Does Not Always Create Better Control](/blog/why-more-sap-monitoring-does-not-always-create-better-control/)
