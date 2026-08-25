---
layout: default
title: "AI Ready — Data and RAG"
description: "A practical architecture guide for retrieval, metadata, chunking, hybrid search, reranking, grounding, and retrieval evaluation."
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

## A 30-second interview answer

> Data is the raw fact layer. A controlled vocabulary makes terms consistent. A taxonomy adds broader and narrower categories. A thesaurus adds synonyms and related concepts. An ontology formally defines classes, relationships, and rules. A knowledge graph then connects real instances using that model. I would not build all six layers by default: I would add only the semantic structure needed for search, governance, integration, reasoning, or AI grounding.

## Quick check

1. **Does a taxonomy automatically manage synonyms?** No. It mainly organizes categories and hierarchy.
2. **Is an ontology just a larger taxonomy?** No. It can model many relationship types, properties, constraints, and logical rules.
3. **Are ontology and knowledge graph the same thing?** No. Think model versus populated facts.
4. **Does RAG require a knowledge graph?** No. Start with the simplest retrieval architecture that passes the evals.
5. **What is the main design rule?** Use the smallest semantic layer that solves a concrete problem.

{% include labs/ai-ready/modern-data-platforms.html %}

## Retrieval pipeline

```text
Question
  -> normalize / classify
  -> permission and metadata filters
  -> candidate retrieval
       lexical search
       vector search
       or both
  -> rerank
  -> context selection
  -> answer with source references
  -> eval + trace
```

Do not add every step by default. Start simple and add complexity only when an eval shows a real gap.

## Lexical, vector, or hybrid?

**Lexical search** is strong for exact terms: error codes, issue IDs, API names, product SKUs, contract clauses, repository symbols, and version numbers.

**Vector search** helps when wording changes but meaning stays similar.

**Hybrid search** is useful when both exact identifiers and semantic language matter. Example: `ERR_AUTH_403`, `/v2/session`, and “users cannot sign in after token refresh” may belong to the same investigation but need different matching signals.

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

Do not create a vector index that quietly removes source permissions. A user who cannot read a document in the source system should not gain access because an embedding was stored elsewhere.

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
- no-answer cases stay no-answer cases;
- citations point to evidence that supports the claim.

Then measure the final answer: factual support, completeness, unsafe guessing, citation quality, latency, and cost.

## Practical example

Question: “Why does the current API reject this request after the authentication change?”

A useful retrieval design may combine:

- current authentication documentation;
- migration notes for the latest API version;
- a known-error article;
- project-specific implementation notes;
- current runtime facts through read tools such as deployment version and recent error events.

Documentation explains expected behavior. Tools provide current system facts. Mixing those sources without labels is how a confident explanation becomes fiction with good formatting.

## RAG or tool?

Use RAG for unstructured knowledge and evidence. Use a tool for a current structured fact.

Examples:

- “What does our refund policy say?” → retrieval.
- “What is ticket INC-204 status right now?” → read tool.
- “Why did this deployment fail?” → probably both retrieval and tools.

## Failure modes

- Vector search is used for exact IDs and performs badly.
- Old and new policy versions are retrieved together without version metadata.
- Chunk text loses the table header that gave it meaning.
- Access rules exist in the UI but not in retrieval.
- The model answers when retrieval found no evidence.
- The team evaluates only final prose and never tests retrieval itself.

## Build checklist

- Define sources of truth.
- Classify data before indexing.
- Keep stable source IDs and provenance.
- Build a lexical baseline first.
- Add vector/hybrid only against an eval gap.
- Test stale, conflicting, forbidden, and missing evidence.
- Trace query, filters, retrieved IDs, scores, reranking, and final citations.

Related: [Practical Use Cases](/labs/ai-ready/use-cases/) · [Evals and Reliability](/labs/ai-ready/evals-reliability/) · [RAG with Evals Lab](/labs/ai-ready/labs/rag-evals/)
