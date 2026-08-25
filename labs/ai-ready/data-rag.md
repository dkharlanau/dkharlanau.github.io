---
layout: default
title: "AI Ready — Data and RAG"
description: "A practical guide to data semantics, vocabularies, taxonomies, ontologies, knowledge graphs, RAG, provenance, retrieval, and evaluation."
permalink: /labs/ai-ready/data-rag/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-25
hide_global_cta: true
tags: [ai, rag, retrieval, embeddings, data, evals]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/deep-dives/">Deep Dives</a></li><li aria-current="page">Data and RAG</li></ol>
</nav>

# Data and RAG

RAG is not “put documents in a vector database”. It is a controlled way to find evidence at request time and give the model only the useful parts. The architecture begins with source ownership and permissions, not embeddings.

## Problem

A model cannot reliably answer from current or private enterprise knowledge unless retrieval preserves source, permission, and freshness.

## Start from the fact

For every important answer, define:

- source system or document;
- owner;
- effective date or version;
- access classification;
- stable source ID;
- how the fact becomes stale;
- how the user can trace the answer back to it.

If nobody knows which document owns the policy, a better embedding model will not settle the argument.

## From data to knowledge: the ladder of meaning

Before retrieval, it helps to separate a few ideas that are often mixed together: data, controlled vocabulary, taxonomy, thesaurus, ontology, and knowledge graph.

A useful learning model is a **ladder of meaning**. Each step adds more shared structure, relationships, or rules.

```text
More explicit meaning, relationships, and rules
                 ↑
      Knowledge base / knowledge graph
                 ↑
              Ontology
                 ↑
              Thesaurus
                 ↑
              Taxonomy
                 ↑
        Controlled vocabulary
                 ↑
                Data
                 ↓
        More raw volume and values
```

This is a learning ladder, not a mandatory architecture sequence. Higher does not automatically mean better. A real system may stop at a controlled vocabulary, use a taxonomy without an ontology, or build a graph with a lightweight schema. Use the smallest layer that solves a real problem.

### The six levels in one view

| Level | Plain meaning | What it adds |
| --- | --- | --- |
| **Data** | Recorded values and facts | Raw material to store, calculate, and exchange |
| **Controlled vocabulary** | An approved list of terms with agreed definitions | Consistent language |
| **Taxonomy** | Terms arranged in broader / narrower categories | Hierarchy and navigation |
| **Thesaurus** | A structured vocabulary with preferred terms, synonyms, and related concepts | Better search and language mapping |
| **Ontology** | A formal model of classes, properties, relationships, and rules | Machine-readable meaning and reasoning |
| **Knowledge base / graph** | Concrete facts connected using a model | A populated network that can be queried and traversed |

### 1. Data — the recorded facts

Data is the starting material: rows, fields, events, measurements, documents, and values.

Examples:

```text
order_id = SO-4711
customer_id = C-1000
material_id = M-77
plant = P01
quantity = 10
status = CREDIT_HOLD
```

This tells us what was recorded. It does not yet tell every person or system exactly what `CREDIT_HOLD` means, whether `customer` and `buyer` are the same concept, or how an order relates to a plant, product, invoice, and credit decision.

A database schema can define types and columns. That is important, but storage structure is not the same as shared business meaning.

**Analogy:** data is a pile of bricks. Useful, but the bricks do not explain the building.

### 2. Controlled vocabulary — agree on the words

A controlled vocabulary is an approved set of terms and definitions.

Instead of allowing many labels such as:

```text
credit hold
credit block
blocked by credit
payment-risk block
```

we may choose one preferred operational term:

```text
CREDIT_HOLD = the order cannot continue until the defined credit restriction is cleared
```

The main purpose is consistency. Reports, metadata, search filters, interfaces, and people use the same term for the same meaning.

A controlled vocabulary does **not** need to describe a hierarchy or complex relationships.

**Analogy:** it is a shared dictionary for the system.

### 3. Taxonomy — put concepts into a hierarchy

A taxonomy organizes concepts using broader and narrower relationships.

Example:

```text
Order exception
├── Commercial exception
│   ├── Credit hold
│   └── Pricing block
└── Logistics exception
    ├── Delivery block
    └── Stock shortage
```

Now the system knows that `Credit hold` is a kind of `Commercial exception`, which is a kind of `Order exception`.

Taxonomies are useful for navigation, filtering, reporting, classification, content management, and training material.

**Analogy:** a category tree in a well-organized library or online shop.

### 4. Thesaurus — connect different words and nearby ideas

A thesaurus goes beyond a simple hierarchy. It normally adds language relationships such as:

- **preferred term** — the term we want people to use;
- **alternative term** — synonym or variant label;
- **broader / narrower term** — hierarchical relation;
- **related term** — connected idea that is not simply a parent or child.

Example:

```text
Preferred term: Credit hold
Alternative term: Credit block
Broader term: Commercial exception
Related term: Credit exposure
Related term: Payment risk
```

This matters in search. A user may search for `credit block`, while the knowledge base stores `credit hold`. A thesaurus can connect the two without pretending they are different business problems.

**Analogy:** a smart index that knows synonyms and nearby concepts.

### 5. Ontology — define what exists and how it may relate

An ontology is a formal model of a domain. It describes things such as:

- classes of objects;
- properties;
- relationships;
- constraints;
- logical rules or axioms.

A simple enterprise ontology could define:

```text
Customer
SalesOrder
Material
Plant
OrderBlock
CreditHold

SalesOrder --placedBy--> Customer
SalesOrder --contains--> Material
SalesOrder --suppliedFrom--> Plant
SalesOrder --blockedBy--> OrderBlock
CreditHold --isA--> OrderBlock
```

The important difference from a taxonomy is that an ontology is not limited to `is a` hierarchy. It can say how different kinds of things relate and can support formal reasoning.

For example, if the model says:

```text
CreditHold is an OrderBlock
SO-4711 is blockedBy CreditHold-88
```

then software can treat the order as blocked by an `OrderBlock` even if that broader fact was not stored separately.

In description-logic language, the schema and rules are often called the **TBox**. You do not need this term for daily work, but it is useful when reading ontology literature.

**Analogy:** the legend and rules of a map. It defines what types of objects may exist and what kinds of connections are meaningful.

### 6. Knowledge base or knowledge graph — populate the model with real facts

A knowledge base contains concrete facts. A knowledge graph represents facts as connected entities and relationships.

Using the ontology above, the populated graph could contain:

```text
SO-4711 --placedBy--> Customer-C1000
SO-4711 --contains--> Material-M77
SO-4711 --suppliedFrom--> Plant-P01
SO-4711 --blockedBy--> CreditHold-88
```

Now we have both the model and the facts.

The ontology says what `SalesOrder`, `Customer`, and `CreditHold` mean and which relations are valid. The knowledge graph says which actual order belongs to which customer, contains which material, and has which block.

In description-logic language, instance facts are often called the **ABox**.

A useful memory rule is:

```text
Ontology / TBox = the map legend and rules
Knowledge base / ABox = the populated map
```

Not every knowledge graph uses OWL or a formal ontology. Property graphs can use a lighter schema. An ontology can also exist without a populated knowledge graph. Keep the concepts separate.

## One example through the whole ladder

Imagine an order cannot move to delivery because of a credit restriction.

**Data**

```text
SO-4711, C-1000, M-77, P01, CREDIT_HOLD
```

**Controlled vocabulary**

`CREDIT_HOLD` has one approved definition.

**Taxonomy**

`Credit hold` is classified under `Commercial exception` → `Order exception`.

**Thesaurus**

`Credit block` is an alternative label for `Credit hold`; `Credit exposure` is a related concept.

**Ontology**

A `SalesOrder` can be `blockedBy` an `OrderBlock`; `CreditHold` is a type of `OrderBlock`; a `SalesOrder` is `placedBy` a `Customer`.

**Knowledge graph**

`SO-4711` is connected to `Customer-C1000`, `Material-M77`, `Plant-P01`, and `CreditHold-88` as concrete facts.

The raw record did not change. What changed was the amount of shared meaning around it.

## What people often confuse

### Database schema vs ontology

A database schema defines how data is stored: tables, columns, types, keys, and constraints. An ontology defines domain meaning and semantic relationships. They can support each other, but they solve different problems.

### Taxonomy vs ontology

A taxonomy mainly answers: **what category does this belong to?**

An ontology can also answer: **what kinds of things exist, how may they relate, and what follows from those relations?**

### Ontology vs knowledge graph

The ontology is the model. The knowledge graph is the connected set of concrete facts. A graph may use an ontology, but the two words are not synonyms.

### Graph database vs knowledge graph

A graph database is a storage and query technology. A knowledge graph is a way of representing connected knowledge. You can store a knowledge graph in a graph database, but installing a graph database does not automatically give you useful semantics, governance, or knowledge quality.

### RAG vs knowledge graph

RAG does not require an ontology or a knowledge graph. Many useful RAG systems work with documents, metadata, lexical search, embeddings, and reranking.

Add stronger semantic structure when it solves a measured problem such as:

- inconsistent terminology;
- poor entity linking;
- cross-domain relationships;
- synonym expansion;
- complex navigation;
- rule-based reasoning;
- repeated ambiguity across systems.

Do not build an ontology only because the project is called “AI-ready”.

## Choose the smallest useful layer

| If the problem is… | Start with… |
| --- | --- |
| People use different names for the same thing | Controlled vocabulary |
| Users need categories, navigation, or drill-down | Taxonomy |
| Search misses synonyms and related terms | Thesaurus |
| Systems need explicit cross-domain meaning and rules | Ontology |
| Users need to traverse concrete entities and relationships | Knowledge graph |
| The answer must use current document evidence | RAG |
| The answer needs a current structured fact or action | API / tool |

This is the Lead-level decision: **add semantic complexity only when it buys a clear capability.**

## Standards map

You do not need these standards to understand the concepts, but they are useful reference points:

- [SKOS — Simple Knowledge Organization System](https://www.w3.org/TR/skos-reference/) is a W3C model for sharing knowledge organization systems such as thesauri, classification schemes, and taxonomies.
- [OWL 2](https://www.w3.org/TR/owl-overview/) is a W3C ontology language with formally defined semantics for classes, properties, individuals, and relationships.
- [SHACL](https://www.w3.org/TR/shacl/) describes constraints for RDF graphs and is commonly used to validate graph structure.
- [SPARQL](https://www.w3.org/TR/sparql11-overview/) is the standard query language family for RDF data.
- The ISO 25964 family covers thesauri and interoperability with other vocabularies.

A common Semantic Web stack is **RDF + RDFS/OWL + SHACL + SPARQL**. It is one option, not the only way to build a knowledge graph.

## 2026 update: what changed in practice

The basic concepts above are still useful, but current AI systems make one point much clearer: **this is a toolbox, not a maturity ladder**.

A company does not become more advanced simply because it has an ontology or a graph database. The useful question is: **which kind of structure helps this specific task become more correct, explainable, searchable, or governable?**

### The modern picture is usually hybrid

A practical enterprise AI system may use several layers at the same time:

```text
Source systems and documents
        ↓
Stable IDs + ownership + permissions
        ↓
Vocabulary / taxonomy / ontology where useful
        ↓
Search layer
  ├─ exact / lexical search
  ├─ vector search
  ├─ graph traversal
  └─ API / tool calls
        ↓
Context selection
        ↓
LLM answer or bounded action
        ↓
Evidence + trace + evaluation
```

There is no need to choose between “vectors” and “graphs” as if one must replace the other.

- **Lexical search** is strong when exact words and identifiers matter.
- **Vector search** is strong when the same idea is expressed with different wording.
- **Graph traversal** is strong when relationships and multi-step connections matter.
- **Tools / APIs** are strong when the answer depends on live structured state or when an action must be executed.

The model can sit above all four.

### A semantic layer is becoming more useful for AI

When several systems use different names and structures for the same business concepts, a semantic layer can give AI one stable language without copying all operational data into one new system.

Example:

```text
CRM:        Account
ERP:        Customer
Data lake:  sold_to_party
Support:    Client

Semantic concept: Customer
```

The semantic layer can say that these fields refer to the same or closely related business concept, while the original systems remain the sources of truth.

This is where controlled vocabularies, taxonomies, ontologies, mappings, and knowledge graphs can become practical AI infrastructure rather than academic modelling exercises.

### Provenance is now part of the fact

For AI, storing only a relation is often not enough.

Instead of only saying:

```text
SO-4711 --blockedBy--> CreditHold-88
```

we may also need to know:

```text
source       = credit-service
observed_at  = 2026-08-25T08:10Z
valid_from   = 2026-08-25
confidence   = confirmed
owner        = credit-management
```

Why? Because an AI answer should be able to distinguish:

- a current fact from an old fact;
- an authoritative source from an inferred relation;
- a confirmed statement from a possible one;
- two sources that disagree.

This idea is receiving stronger standards support. [RDF 1.2 Concepts](https://www.w3.org/TR/rdf12-concepts/) reached Candidate Recommendation in April 2026 and introduces **triple terms and reification**. In plain language, RDF can refer to a statement itself and attach information to that statement. That is useful for source, time, confidence, authorship, or context.

You do not need RDF to apply the design rule. Even in SQL, JSON, or a property graph, keep provenance next to important facts.

### GraphRAG: useful pattern, not a default upgrade

GraphRAG became popular because flat retrieval can struggle with questions that depend on many connected parts of a corpus.

A useful distinction is:

| Question shape | Good first option |
| --- | --- |
| “What is the status code for this error?” | Lexical / hybrid retrieval |
| “What does this policy say about refunds?” | Document RAG |
| “Which entities, events, and dependencies connect these incidents?” | Graph or graph-assisted retrieval |
| “What are the main themes across thousands of documents?” | Global / graph-assisted retrieval may help |
| “What is order SO-4711 status now?” | Live API / tool |

Microsoft Research's GraphRAG work separates **local** questions from **global** questions. Their BenchmarkQED work also makes this distinction explicit: vector retrieval is naturally strong for local questions where the answer sits in a small number of similar text regions, while graph-based methods can help when the question needs broader structure across a dataset.

But GraphRAG has costs. Graph construction, entity extraction, community building, summarisation, and refresh all add work. Microsoft's open-source GraphRAG repository explicitly warns that indexing can be expensive. As of July 2026 the repository is in maintenance mode; its latest 3.1.x releases focus mainly on maintenance, storage, streaming, validation, and dependency work.

The lesson is not “GraphRAG is obsolete”. The lesson is: **treat graph retrieval as one architecture pattern and benchmark it against simpler retrieval on your own question set.**

### LLMs can help build knowledge structures — but they do not become the authority

Recent research increasingly uses LLMs to help with:

- finding candidate entities and relations in text;
- suggesting taxonomy or ontology concepts;
- mapping similar fields across systems;
- proposing synonyms and labels;
- extracting candidate facts for a graph.

This can reduce manual modelling work, but it creates a new quality boundary.

```text
LLM proposes → deterministic checks validate → source evidence confirms → human / governed rule approves
```

Do not silently convert an LLM extraction into an enterprise fact.

A generated relation such as:

```text
Supplier-X --supplies--> Material-Y
```

is still only a candidate until the source, scope, time, and confidence are known.

### RAG is moving from one retrieval step to a controlled search loop

A simple RAG system retrieves once and answers once. Newer reasoning-and-retrieval systems may search, inspect the result, reformulate the question, retrieve again, and then answer.

That can help with multi-step questions, but it does not remove the need for controls. The search loop needs:

- allowed sources;
- stop conditions;
- cost / token budgets;
- traceable retrieval steps;
- no-answer behaviour;
- evaluation of both retrieval and final claims.

The architecture is becoming more agentic, but the basic rule remains the same: **more autonomy requires more evidence and control, not less.**

## Standards status in 2026

The Semantic Web standards are active again. That matters because many older diagrams still show only the 2009–2017 generation of the stack.

| Area | Current status in Aug 2026 | Why it matters |
| --- | --- | --- |
| **SKOS** | Stable W3C Recommendation | Vocabularies, taxonomies, thesauri |
| **OWL 2** | Stable W3C Recommendation | Formal ontology and reasoning |
| **RDF 1.2** | Candidate Recommendation track | Triple terms, reification, richer statement-level modelling |
| **SPARQL 1.2** | Working Draft family | Query/update support aligned with RDF 1.2 |
| **SHACL 1.2** | Active Working Draft family | Validation plus work on rules, node expressions, profiling, UI and extensions |

Two cautions are important:

1. **Candidate Recommendation and Working Draft do not mean final Recommendation.** Check implementation support before using new 1.2 features in production.
2. Standards help interoperability, but they do not create good business semantics automatically. The hard part is still ownership, definitions, identity, source quality, and lifecycle.

## A practical enterprise pattern

For an ERP landscape, a sensible progression often looks like this:

```text
1. Keep operational truth in source systems.
2. Give important objects stable cross-system IDs.
3. Standardise names and definitions.
4. Add hierarchy where navigation or classification needs it.
5. Add ontology only where cross-domain semantics or rules justify it.
6. Build graph connections where traversal adds value.
7. Use text/vector retrieval for documents.
8. Use APIs/tools for live facts and actions.
9. Attach provenance to every important retrieved or inferred fact.
10. Evaluate the complete path from question to evidence to answer.
```

Example:

```text
Sales order → delivery → warehouse task → shipment → invoice
```

A graph can make this chain easy to traverse. A taxonomy can classify the exception. A thesaurus can connect business language to system language. RAG can retrieve the relevant procedure. A tool can read the current document status. The LLM can explain the situation.

None of those layers replaces the others.

## Updated decision rule

Use this short test before adding semantic technology:

1. **Different words for the same thing?** Start with a controlled vocabulary.
2. **Need categories?** Add a taxonomy.
3. **Need synonyms and related terms?** Add thesaurus-style relationships.
4. **Need formal cross-domain meaning or rules?** Consider an ontology.
5. **Need to traverse real entities and dependencies?** Consider a knowledge graph.
6. **Need evidence from documents?** Use RAG.
7. **Need a live fact or action?** Use a tool / API.
8. **Need several of these at once?** Build a hybrid path, then evaluate it.

The mature answer is often not “we need a knowledge graph”. It is **“we need this relationship to be explicit because this question cannot be answered safely without it.”**

## A 30-second interview answer

> Data is the raw fact layer. A controlled vocabulary makes terms consistent. A taxonomy adds broader and narrower categories. A thesaurus adds synonyms and related concepts. An ontology formally defines classes, relationships, and rules. A knowledge graph then connects real instances using that model. In a modern AI architecture I would not build all layers by default. I would combine only the semantic structure, retrieval, graph traversal, and live tools that the use case needs, and I would keep provenance and evaluation around the whole flow.

## Quick check

1. **Does a taxonomy automatically manage synonyms?** No. It mainly organizes categories and hierarchy.
2. **Is an ontology just a larger taxonomy?** No. It can model many relationship types, properties, constraints, and logical rules.
3. **Are ontology and knowledge graph the same thing?** No. Think model versus populated facts.
4. **Does RAG require a knowledge graph?** No. Start with the simplest retrieval architecture that passes the evals.
5. **What is the main design rule?** Use the smallest semantic layer that solves a concrete problem.
6. **What did RDF 1.2 add that is useful for AI knowledge?** Better support for referring to a statement and describing its source or context through triple terms and reification.
7. **When should GraphRAG be considered?** When relationships, multi-hop structure, or global questions create a measured gap for simpler retrieval.

## Source baseline — reviewed 25 Aug 2026

The dated sources below support the 2026 update. Draft standards can still change.

- [W3C RDF 1.2 Concepts and Abstract Data Model](https://www.w3.org/TR/rdf12-concepts/) — Candidate Recommendation Snapshot, 7 Apr 2026.
- [W3C RDF 1.2 Primer](https://www.w3.org/TR/rdf12-primer/) — examples of triple annotations and reification.
- [W3C SPARQL 1.2 Query Language](https://www.w3.org/TR/sparql12-query/) — Working Draft, 25 Jun 2026.
- [W3C SHACL 1.2 Core](https://www.w3.org/TR/shacl12-core/) and [SHACL 1.2 Rules](https://www.w3.org/TR/shacl12-rules/) — active 2026 Working Drafts.
- [Microsoft Research — Project GraphRAG](https://www.microsoft.com/en-us/research/project/graphrag/) — graph-based retrieval research, local/global search, DRIFT, LazyGraphRAG and evaluation work.
- [Microsoft GraphRAG open-source repository](https://github.com/microsoft/graphrag) — project status, architecture notes, maintenance-mode notice and current releases.
- [Microsoft Research — BenchmarkQED](https://www.microsoft.com/en-us/research/blog/benchmarkqed-automated-benchmarking-of-rag-systems/) — local/global RAG query classes and reproducible benchmarking, 5 Jun 2025.
- [ACL Findings 2025 — A Survey of RAG-Reasoning Systems](https://aclanthology.org/2025.findings-emnlp.648/) — retrieval and reasoning increasingly operate as an iterative search-and-reason loop.

{% include labs/ai-ready/modern-data-platforms.html %}

## Retrieval pipeline

```text
Question
  -> normalize / classify
  -> permission and metadata filters
  -> candidate retrieval
       lexical search
       vector search
       graph traversal when useful
       live tool / API when needed
  -> rerank / organize
  -> context selection
  -> answer with source references
  -> eval + trace
```

Do not add every step by default. Start simple and add complexity only when an eval shows a real gap.

## Lexical, vector, graph, or hybrid?

**Lexical search** is strong for exact terms: error codes, issue IDs, API names, product SKUs, contract clauses, repository symbols, and version numbers.

**Vector search** helps when wording changes but meaning stays similar.

**Graph retrieval** helps when the question depends on explicit relationships, paths, communities, or multi-hop dependencies.

**Hybrid retrieval** is useful when several of these signals matter. Example: `ERR_AUTH_403`, `/v2/session`, and “users cannot sign in after token refresh” may belong to the same investigation but need different matching signals.

## Chunking is a content decision

Do not select a chunk size because a tutorial used it. Split content around useful meaning:

- one procedure step group;
- one product concept;
- one policy rule;
- one error pattern and resolution;
- one table section with its header;
- one decision branch.

Keep metadata beside the chunk. Useful fields often include domain, product, object, language, validity date, security class, source URL, and parent document.

## Reranking and context selection

Retrieval finds candidates. Reranking decides which candidates deserve the limited context budget. The final context builder should remove duplicates, preserve source boundaries, and avoid mixing conflicting versions without telling the model.

A large context is not automatically a better context. Too much irrelevant evidence makes the answer harder to control and more expensive to test.

## Permissions follow the source

Do not create a vector or graph index that quietly removes source permissions. A user who cannot read a document or entity in the source system should not gain access because a copy, embedding, or graph edge was stored elsewhere.

Ask four separate questions:

1. May this content be indexed?
2. May this user retrieve it?
3. May it be sent to the selected model/runtime?
4. May the answer expose the retrieved field?

## Retrieval evals

Measure retrieval separately from answer quality. Useful checks include:

- expected source appears in top K;
- forbidden source never appears;
- correct version wins over obsolete version;
- exact identifiers remain searchable;
- required relationship or path is retrievable;
- no-answer cases stay no-answer cases;
- citations point to evidence that supports the claim.

Also separate question shapes in the test set:

- local fact questions;
- global summary questions;
- relationship / multi-hop questions;
- live-state questions;
- conflicting-source questions.

Then measure the final answer: factual support, completeness, unsafe guessing, citation quality, latency, and cost.

## Practical example

Question: “Why does the current API reject this request after the authentication change?”

A useful retrieval design may combine:

- current authentication documentation;
- migration notes for the latest API version;
- a known-error article;
- project-specific implementation notes;
- relationships between API versions, services, and deployments;
- current runtime facts through read tools such as deployment version and recent error events.

Documentation explains expected behavior. A graph may connect dependencies. Tools provide current system facts. Mixing those sources without labels is how a confident explanation becomes fiction with good formatting.

## RAG or tool?

Use RAG for unstructured knowledge and evidence. Use a tool for a current structured fact.

Examples:

- “What does our refund policy say?” → retrieval.
- “What is ticket INC-204 status right now?” → read tool.
- “Which systems depend on this interface?” → graph or dependency data may help.
- “Why did this deployment fail?” → probably retrieval plus tools, and possibly graph context.

## Failure modes

- Vector search is used for exact IDs and performs badly.
- A knowledge graph is built without a clear question that needs graph structure.
- LLM-extracted relations are treated as confirmed facts without evidence.
- Old and new policy versions are retrieved together without version metadata.
- Chunk text loses the table header that gave it meaning.
- Access rules exist in the UI but not in retrieval.
- The model answers when retrieval found no evidence.
- The team evaluates only final prose and never tests retrieval itself.

## Build checklist

- Define sources of truth.
- Classify data before indexing.
- Keep stable source IDs and provenance.
- Standardize important terms before adding complex semantics.
- Build a lexical baseline first.
- Add vector, graph, or agentic retrieval only against an eval gap.
- Validate LLM-generated entities and relationships before treating them as facts.
- Test local, global, multi-hop, stale, conflicting, forbidden, and missing evidence.
- Trace query, filters, retrieved IDs, graph paths, scores, reranking, tool reads, and final citations.

Related: [Practical Use Cases](/labs/ai-ready/use-cases/) · [Evals and Reliability](/labs/ai-ready/evals-reliability/) · [RAG with Evals Lab](/labs/ai-ready/labs/rag-evals/)