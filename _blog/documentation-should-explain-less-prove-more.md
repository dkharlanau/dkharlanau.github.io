---
layout: blog
title: "Documentation Should Explain Less, Prove More"
description: "A practical proposal for concise, human-first documentation that tools can describe, test, render, and keep aligned with their behavior."
slug: documentation-should-explain-less-prove-more
permalink: /blog/documentation-should-explain-less-prove-more/
date: 2026-11-06
author: "Dzmitryi Kharlanau"
language: en
category: "Enterprise engineering"
tags:
  - documentation
  - developer-experience
  - architecture
  - ai-agents
  - docs-as-code
canonical_url: https://dkharlanau.github.io/blog/documentation-should-explain-less-prove-more/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: 9
related_articles:
  - /blog/why-sap-knowledge-disappears-after-every-support-transition/
---

Most technical documentation has a strange problem: it grows faster than the reader's understanding.

A developer wants to know whether an API can change a record. A SAP consultant wants to know which input controls a determination rule. An architect wants to know the failure boundary. Instead, they open a long page with repeated explanations, outdated diagrams, and examples that may no longer work.

A shorter page is not automatically a better page. An omitted dependency can cost more than ten unnecessary paragraphs. The objective should be **the least information needed for a correct decision**, not the fewest tokens at any cost.

I propose a working design called the **Living Documentation Contract (LDC)**. It combines short human-readable explanations, structured tool descriptions, generated diagrams, tests, and explicit responsibility for facts that cannot be verified by code.

[Open the proposed LDC v0.1 specification and synthetic example](/frameworks/living-documentation/).

## The documentation approaches we already have

There is no need to invent everything again. Several mature ideas solve different parts of the problem.

| Approach | What it solves | What remains difficult |
|---|---|---|
| Traditional wiki or long guide | Provides narrative, decisions, and historical context | Easy to duplicate; hard to detect behavioral drift |
| Docs as code / Backstage TechDocs | Versions Markdown with code and publishes searchable HTML | A successful build does not prove that a claim is true |
| Diátaxis | Separates tutorial, how-to, reference, and explanation by reader need | Organizes content; does not verify implementation behavior |
| OpenAPI / JSON Schema | Describes API structure and data constraints in a machine-readable form | Does not explain all business rules, exceptions, or operational trade-offs |
| MCP tool metadata | Lets clients discover a tool name, description, and input schema | Descriptions and annotations are not a security or correctness guarantee |
| Mermaid / diagram-as-code | Makes diagrams reviewable and reproducible from text | A diagram can still represent the wrong process |
| Living Documentation Contract (proposal) | Connects reader tasks, tool contracts, examples, diagrams, and verification | Requires ownership, tests, and a controlled update process |

Google's documentation guidance already prefers a small set of accurate, maintained pages to a larger collection of stale material. Diátaxis explains why a reference page and a tutorial should not try to do the same job. OpenAPI formalizes HTTP API descriptions. MCP adds tool discovery and schemas. These are complementary building blocks, not competing replacements.

Sources: [Google documentation practices](https://google.github.io/styleguide/docguide/best_practices.html), [Diátaxis](https://diataxis.fr/), [Backstage TechDocs](https://backstage.io/docs/features/techdocs/), [OpenAPI 3.2.1](https://spec.openapis.org/oas/v3.2.1.html), [MCP tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools), [JSON Schema annotations](https://json-schema.org/understanding-json-schema/reference/annotations), [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli).

## A compact page should answer an actual task

Consider a synthetic SAP SD sales-order upload case. A test order has no determined route. The upload program accepts Shipping Condition, but the customer master also has a value. Different shipping points or plants may require different inputs and configuration.

An unhelpful page might say:

> Route determination is an important logistics functionality. SAP provides flexible capabilities to configure it. Please ensure that all necessary information is maintained correctly.

That says almost nothing.

A useful expert-facing card could be:

> **Task:** Diagnose a missing route after order upload.
>
> **Inspect:** Effective Shipping Condition in the sales document; departure and destination country/transportation zones; transportation group; relevant configuration and master data.
>
> **Do not assume:** Changing the customer master will fix an individual test order. An upload may supply its own Shipping Condition when the specific interface supports it.
>
> **Next check:** Compare a successful and a failed document using the same system, configuration, and processing stage.
>
> **Limit:** This is a diagnostic checklist, not a guarantee about route determination in every SAP release or custom implementation.

The second version is longer in substance but shorter in the path from question to action. It also identifies assumptions instead of hiding them.

The example is deliberately synthetic. Actual SAP behavior must be checked against the relevant release, settings, enhancements, and interface mapping.

## The contract: one core, multiple views

A tool should expose a minimal description of its capabilities rather than wait for somebody to write a disconnected manual.

The proposed core has eight fields:

1. **Identity and version** — what is this tool, and which behavior does this page describe?
2. **Purpose and audience** — when should a reader use it?
3. **Inputs and outputs** — required fields, meaning, and results.
4. **Preconditions** — rights, dependencies, supported environments, and scope.
5. **Boundaries** — what this tool cannot do; what it does not guarantee.
6. **Failure modes and recovery** — meaningful errors and safe next checks.
7. **Examples and evidence** — executable cases, test links, and observed behavior.
8. **Owner and freshness** — where authoritative changes start, and who reviews them.

The human card shows only what the current task requires. The full contract remains available behind links, a reference tab, or a machine-readable endpoint. Compact does not mean inaccessible detail.

A practical stack is **Markdown for editable human content, JSON Schema/OpenAPI/MCP for applicable machine contracts, SVG generated from semantic diagram models, and HTML as the reading surface**. HTML should be a publication output, not a second manual source of truth.

The existing [Visual Workbench](https://github.com/dkharlanau/visual-workbench) project is an example of semantic models producing SVG without manual coordinates. [Process as Code](https://github.com/dkharlanau/process-as-code) can validate versioned process contracts and generate Markdown, Mermaid, and other views. These are useful building blocks for the diagram layer; they are not evidence that an arbitrary SAP process has been verified.

## How a tool can describe itself

For an HTTP service, start with its OpenAPI description where one exists. For a CLI, provide a short help screen and a structured describe command. For an MCP server, clients discover tool metadata through the protocol's tools/list capability. For a business process, a versioned model can expose the steps, actors, controls, and links to evidence.

The key rule is **derive descriptions from the same contract the executable tool uses**, whenever possible. Do not maintain a separate copy of input fields inside an article.

Here is a deliberately small custom manifest example. It is a proposed LDC shape, not an official MCP or OpenAPI schema:

~~~json
{
  "contract": "ldc/0.1",
  "id": "order-upload-input-check",
  "audience": "SAP SD consultant",
  "purpose": "Find missing route-analysis inputs in a sample order.",
  "inputs": ["shipping_condition", "departure_country", "departure_zone"],
  "result": "missing-input report",
  "boundary": "Does not determine an SAP route or call SAP.",
  "evidence": "synthetic fixture + repeatable test"
}
~~~

The complete [executable example](https://github.com/dkharlanau/dkharlanau.github.io/blob/main/scripts/living_docs_demo.py) is a small Python pre-check. It reads its own manifest, exposes a describe command, checks a synthetic payload, and generates both a Markdown tool card and a Mermaid flow. A check command detects when generated files are stale.

This is not autonomous documentation in the strong sense. It proves a narrower and more valuable property: **for fields represented in the contract, displayed documentation can be checked against the same source used by the tool.**

## What should update automatically?

A safe process separates derivation from judgment.

| Change | Automatic action | Human decision |
|---|---|---|
| Input field added to an API/tool contract | Regenerate parameter reference and flag changed examples | Confirm business meaning and compatibility |
| A test example stops working | Fail the documentation check and link the evidence | Determine whether code, test, or documentation is wrong |
| A version is released | Attach the version and changelog reference | Approve release notes and supported-scope claims |
| A process model changes | Regenerate diagrams and list semantic differences | Confirm real process ownership and exceptions |
| A sentence claims a performance or business benefit | None without measurement | Review the evidence and scope of the claim |

A sensible pipeline is:

1. Change the implementation or authoritative contract.
2. Generate machine and human projections.
3. Validate schema, links, examples, diagrams, and accessibility.
4. Run behavior tests and detect changes in meaning.
5. Open a reviewable pull request for any generated changes.
6. Publish only the reviewed version, with provenance and supported version visible.

A scheduled check can identify stale versions and missing evidence. It must not invent explanations, change business rules, or mark a page verified simply because a language model rewrote it.

## Token economy is a constraint, not the score

Token count measures size. It does not measure understanding.

I would evaluate the design with expert readers using real tasks. Start with the same question in two documentation formats and record:

| Measure | Why it matters |
|---|---|
| Correct task completion | The reader reached the right result |
| Time to first correct action | The page supports fast scanning and navigation |
| Critical omission rate | Compact wording did not remove necessary constraints |
| Retrieval success | A reader or agent can locate the right section |
| Documentation drift | Generated claims and examples match the tested contract |
| Maintenance effort | The method is cheaper to keep accurate |

Token count and rendered word count remain useful **guardrails**. They are not the primary success metric. Do not claim improvement before a controlled comparison provides evidence.

## The risks are architectural

Generated references can look authoritative while missing real-world exceptions. A test can prove one example and say nothing about another. Auto-generated diagrams may conceal manual activities or undocumented integrations. Tool descriptions from untrusted sources can mislead agents; the MCP specification explicitly treats annotations as untrusted hints unless the server is trusted.

For SAP, the strongest separation is between **system-observable facts**, **release-specific standard behavior**, **project configuration**, and **business decisions**. A generated page should say which layer each claim belongs to. Not every important fact can be extracted from code, and that is not a defect to hide.

A living document is therefore not a document that writes itself without control. It is a document whose **claims have known owners, whose derived sections can be reproduced, and whose uncertainty remains visible**.

## A focused pilot

Use one existing tool rather than rewriting an entire documentation portal. The order-upload input pre-check is a small, synthetic example; a production pilot could use a real, safe, read-only CLI or API.

Set a baseline with a handful of representative expert questions. Produce a compact card, a machine-readable capability contract, one generated diagram, and at least one executable example. Deliberately change an input field and check that CI detects stale generated documentation. Then test whether a consultant can find the right answer without opening a long guide.

If the generated reference stays aligned but readers still misunderstand the decision, the tool needs better human explanation, not more auto-generated text.

**The goal is not a documentation system that produces more documentation. It is a system that makes the right information easy to find, difficult to misrepresent, and less expensive to maintain.**

Explore the companion [Living Documentation Contract v0.1](/frameworks/living-documentation/) for the detailed rules and prototype commands.
