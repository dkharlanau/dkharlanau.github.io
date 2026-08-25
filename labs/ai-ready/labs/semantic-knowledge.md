---
layout: default
title: "AI Ready Lab — Semantic Data and Knowledge Graphs"
description: "A hands-on lab that turns one synthetic ERP scenario into a vocabulary, taxonomy, ontology, RDF graph, SHACL validation, SPARQL queries, a property graph, and AI retrieval decisions."
permalink: /labs/ai-ready/labs/semantic-knowledge/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-25
hide_global_cta: true
tags: [ai, lab, data, semantics, taxonomy, ontology, knowledge-graph, rdf, sparql, shacl]
career_impact: mapped
career_skills:
  - ai-retrieval
  - ai-data-governance
  - ai-readiness
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/data-rag/">Data and RAG</a></li><li aria-current="page">Semantic Data and Knowledge Graphs</li></ol>
</nav>

# Lab 05: Semantic Data and Knowledge Graphs

Use one small ERP-style example to make the semantic stack concrete. The goal is not to install every graph product. The goal is to see what changes when the same business fact is represented as data, vocabulary, hierarchy, ontology, RDF, a validated graph, and a property graph.

Everything in this lab is synthetic. Do not use client, employer, or production data.

## What you will learn

By the end, you should be able to explain this path without treating it as a mandatory maturity model:

```text
raw data
   ↓
controlled terms
   ↓
taxonomy / thesaurus
   ↓
ontology where rules or cross-domain meaning are useful
   ↓
concrete graph facts
   ↓
validation + queries
   ↓
RAG / graph retrieval / live tools chosen by question type
```

The important result is the decision logic: **use the smallest semantic layer that solves a real problem.**

## Scenario

A sales order cannot move to delivery because of a credit restriction.

Start with this small record:

```csv
order_id,customer_id,material_id,plant,status
SO-4711,C-1000,M-77,P01,CREDIT_HOLD
```

We want to answer questions such as:

- What does `CREDIT_HOLD` mean?
- Is `credit block` the same business concept?
- What type of exception is it?
- Which customer and material belong to the blocked order?
- Which rule says a sales order must have a customer?
- Which source confirms the current status?
- Which parts belong in RAG and which parts should come from a live tool?

## Tool map

The tools below do different jobs. They are also not all open source, so **free** and **open source** should not be treated as the same label.

| Tool | Best learning job | Access model | Use it here for |
| --- | --- | --- | --- |
| [Protégé](https://protege.stanford.edu/) | OWL ontology modelling | Free and open source | Classes, properties, restrictions, optional reasoning |
| [VocBench](https://vocbench.uniroma2.it/) | SKOS vocabularies, thesauri, ontologies | Free and open source | Preferred terms, alternative labels, broader and related concepts |
| [Apache Jena / Fuseki](https://jena.apache.org/) | RDF storage and SPARQL | Apache open source | Load Turtle, run a local SPARQL endpoint, inspect RDF data |
| [Zazuko SHACL Playground](https://zazuko.com/tools/shacl-playground/) | Browser-based SHACL validation | Open source web tool | Test a small shape against sample RDF without local setup |
| [GraphDB Free / Desktop](https://graphdb.ontotext.com/documentation/) | RDF repository, inference, SHACL, SPARQL | Free edition; proprietary | Compare storage, inference, validation, and query behaviour |
| [Wikidata Query Service](https://query.wikidata.org/) | Public RDF knowledge graph | Public service | Learn SPARQL on a large real graph |
| [DBpedia SPARQL](https://www.dbpedia.org/resources/sparql/) | Public linked-data graph | Public service | Compare another public RDF model and endpoint |
| [Neo4j AuraDB Free](https://neo4j.com/docs/aura/) | Property graph and Cypher | Free hosted tier; proprietary service | Represent the same facts as nodes and relationships |

### Two current tool notes

**SHACL Playground:** the older playground at `shacl.org` is still online, but its own page says that implementation is no longer actively maintained. For this lab, use the newer Zazuko SHACL Playground for the browser exercise.

**GraphDB Free:** current GraphDB 11 documentation says the Free edition requires a free license request. It is free to use under its terms, but it is not an open-source product. Check the current license and limits before installation.

## Step 1: define the vocabulary

Start with language before technology.

Create these concepts in VocBench, or write them as a small SKOS file if you do not want to install VocBench:

```text
Preferred term: Credit hold
Alternative term: Credit block
Broader term: Commercial exception
Broader term above that: Order exception
Related term: Credit exposure
Related term: Payment risk
```

You have now solved one specific problem: different people can use different words while the system still points to one preferred concept.

### Check

Can you explain why a synonym is not automatically a new business object?

## Step 2: build a small taxonomy

Keep the hierarchy simple:

```text
Order exception
├── Commercial exception
│   ├── Credit hold
│   └── Pricing block
└── Logistics exception
    ├── Delivery block
    └── Stock shortage
```

A taxonomy answers a classification question: **where does this concept belong?**

It does not yet describe all business relationships between orders, customers, materials, plants, and blocks.

## Step 3: model the ontology in Protégé

Create only the classes needed for the scenario:

```text
BusinessDocument
SalesOrder
BusinessPartner
Customer
Product
Material
Plant
OrderBlock
CreditHold
```

Add a few class relationships:

```text
SalesOrder is a BusinessDocument
Customer is a BusinessPartner
Material is a Product
CreditHold is an OrderBlock
```

Add object properties:

```text
SalesOrder --placedBy--> Customer
SalesOrder --contains--> Material
SalesOrder --suppliedFrom--> Plant
SalesOrder --blockedBy--> OrderBlock
```

Do not model the whole ERP system. Stop when the model can answer the learning questions.

If your Protégé setup has a reasoner available, run it and inspect what can be inferred from the class hierarchy. The point is to understand inference, not to collect screenshots.

## Step 4: create RDF facts

Represent the same scenario as Turtle:

```turtle
@prefix ex: <https://example.org/erp/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ex:CreditHold rdfs:subClassOf ex:OrderBlock .

ex:SO-4711
  a ex:SalesOrder ;
  ex:placedBy ex:Customer-C1000 ;
  ex:contains ex:Material-M77 ;
  ex:suppliedFrom ex:Plant-P01 ;
  ex:blockedBy ex:CreditHold-88 .

ex:Customer-C1000 a ex:Customer .
ex:Material-M77 a ex:Material .
ex:Plant-P01 a ex:Plant .
ex:CreditHold-88 a ex:CreditHold .
```

Now the graph contains concrete facts. The ontology describes the model; these triples describe instances.

## Step 5: validate the graph with SHACL

A graph can be syntactically valid RDF and still be bad business data. Add a SHACL rule that says every `SalesOrder` must have exactly one customer.

```turtle
@prefix ex: <https://example.org/erp/> .
@prefix sh: <http://www.w3.org/ns/shacl#> .

ex:SalesOrderShape
  a sh:NodeShape ;
  sh:targetClass ex:SalesOrder ;
  sh:property [
    sh:path ex:placedBy ;
    sh:minCount 1 ;
    sh:maxCount 1
  ] .
```

Test two cases in the Zazuko SHACL Playground:

1. `SO-4711` has one customer → should conform.
2. Remove `ex:placedBy ex:Customer-C1000` → should fail validation.

This separates two ideas that are often mixed together:

```text
Ontology → what kinds of things and relations make sense
SHACL    → whether this concrete graph satisfies required constraints
```

## Step 6: query the RDF graph with Jena / Fuseki

Load the Turtle data into a local Fuseki dataset and run a simple SPARQL query:

```sparql
PREFIX ex: <https://example.org/erp/>

SELECT ?order ?block
WHERE {
  ?order a ex:SalesOrder ;
         ex:blockedBy ?block .
}
```

Then add customer and material to the query:

```sparql
PREFIX ex: <https://example.org/erp/>

SELECT ?order ?customer ?material ?block
WHERE {
  ?order a ex:SalesOrder ;
         ex:placedBy ?customer ;
         ex:contains ?material ;
         ex:blockedBy ?block .
}
```

### Check

Can you explain the difference between:

- the ontology;
- the RDF instance data;
- the SPARQL query;
- the query result?

## Step 7: compare inference in GraphDB

Load the same ontology and instance data into GraphDB Free / Desktop if you want to explore an RDF store with reasoning support.

A useful experiment is to ask whether `CreditHold-88` can also be treated as an `OrderBlock` because `CreditHold` is a subclass of `OrderBlock`.

Compare:

```text
explicit fact:  CreditHold-88 is a CreditHold
schema fact:    CreditHold is a subclass of OrderBlock
inferred view:  CreditHold-88 can be treated as an OrderBlock
```

Do not assume every repository uses the same reasoning profile. Check the configured ruleset before comparing results.

## Step 8: represent the same facts in Neo4j

Now switch mental models. A property graph does not need RDF triples or OWL to be useful.

Create a small graph in AuraDB Free:

```cypher
CREATE (o:SalesOrder {id: 'SO-4711'})
CREATE (c:Customer {id: 'C-1000'})
CREATE (m:Material {id: 'M-77'})
CREATE (p:Plant {id: 'P01'})
CREATE (b:OrderBlock:CreditHold {id: 'CreditHold-88'})
CREATE (o)-[:PLACED_BY]->(c)
CREATE (o)-[:CONTAINS]->(m)
CREATE (o)-[:SUPPLIED_FROM]->(p)
CREATE (o)-[:BLOCKED_BY]->(b)
```

Query it:

```cypher
MATCH (o:SalesOrder)-[:BLOCKED_BY]->(b)
RETURN o.id AS order_id, labels(b) AS block_types, b.id AS block_id
```

The business meaning is similar to the RDF example, but the data model and query language are different.

### Lead question

Would you choose RDF/OWL or a property graph only because one is more fashionable? No. Choose from the required semantics, interoperability, reasoning, query patterns, team skills, operational model, and product constraints.

## Step 9: practise on public graphs

### Wikidata Query Service

Try a small SPARQL query on Wikidata:

```sparql
SELECT ?city ?cityLabel
WHERE {
  ?city wdt:P31 wd:Q515 .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
LIMIT 10
```

Wikidata documents the Query Service as a SPARQL endpoint for querying Wikidata. It is not intended for large bulk extraction or fuzzy text search; use the service within its documented limits.

### DBpedia

Try a small DBpedia query:

```sparql
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?city ?label
WHERE {
  ?city a dbo:City ;
        rdfs:label ?label .
  FILTER(lang(?label) = "en")
}
LIMIT 10
```

DBpedia's public endpoint is a shared service with fair-use limits. Use it for learning and exploration, not as an unlimited production dependency.

## Step 10: connect the semantic layer back to AI

Do not finish the exercise by saying “now we have a knowledge graph, so use GraphRAG.” Route each question to the simplest useful source.

| Question | Best first source |
| --- | --- |
| What does “credit block” mean? | Vocabulary / thesaurus + supporting document |
| What category of exception is it? | Taxonomy |
| Which relations are allowed for a SalesOrder? | Ontology |
| Which synthetic order is blocked by which block? | RDF/property graph query |
| Does every SalesOrder have a customer? | SHACL validation |
| What does the current credit policy say? | Document RAG |
| What is SO-4711 status right now? | Live API / read tool |
| Which systems and documents are connected to this exception? | Graph-assisted retrieval may help if the relationship path matters |

This is the architecture lesson: **RAG, graph retrieval, semantic models, and live tools solve different information problems.**

## Add provenance before you call it knowledge

For a real enterprise fact, keep source and time next to the relation.

```text
fact:         SO-4711 --blockedBy--> CreditHold-88
source:       credit-service
observed_at:  2026-08-25T08:10Z
owner:        credit-management
confidence:   confirmed
```

An LLM may suggest entities or relations, but a generated edge is not automatically an enterprise fact.

```text
LLM proposes
   ↓
validation checks
   ↓
source evidence confirms
   ↓
governed approval where needed
```

## What not to do

- Do not build a full ontology before you have a question that needs it.
- Do not call every graph a knowledge graph without defining meaning, ownership, and provenance.
- Do not treat GraphDB Free or AuraDB Free as open-source products because they are free to start.
- Do not use a public SPARQL endpoint as an unlimited production backend.
- Do not trust an LLM-extracted relation without evidence.
- Do not add GraphRAG until normal retrieval has a measured relationship or global-query gap.

## Done when

You can explain and demonstrate:

1. why a controlled vocabulary and a taxonomy are different;
2. why an ontology and a knowledge graph are different;
3. how the same fact looks in RDF and a property graph;
4. how SHACL catches a missing required relation;
5. how SPARQL and Cypher query different graph models;
6. which tools are open source, free hosted services, or free proprietary editions;
7. why current state belongs in a live tool rather than a static graph snapshot;
8. when graph-assisted retrieval is justified and when normal RAG is enough.

## Tool status baseline — checked 25 Aug 2026

- [Protégé](https://protege.stanford.edu/) describes itself as a free, open-source ontology editor.
- [VocBench](https://vocbench.uniroma2.it/) is a free and open-source platform for OWL ontologies, SKOS/SKOS-XL thesauri, lexicons, and RDF datasets.
- [Apache Jena](https://jena.apache.org/download/) provides the Jena RDF framework and Fuseki SPARQL server as Apache software.
- [Zazuko SHACL Playground](https://zazuko.com/tools/shacl-playground/) is an open-source, client-side SHACL validation playground.
- [GraphDB documentation](https://graphdb.ontotext.com/documentation/) documents a Free edition and its current license requirements; Free does not mean open source.
- [Wikidata data access](https://www.wikidata.org/wiki/Wikidata:Data_access) documents the Wikidata Query Service as a public SPARQL endpoint and explains when not to use it.
- [DBpedia SPARQL](https://www.dbpedia.org/resources/sparql/) documents the public endpoint and fair-use limits.
- [Neo4j Aura documentation](https://neo4j.com/docs/aura/) lists AuraDB Free as the learning tier for the managed graph service.

Read first: [Data and RAG](/labs/ai-ready/data-rag/) · Next: [RAG with Evals](/labs/ai-ready/labs/rag-evals/) · [Evals and Reliability](/labs/ai-ready/evals-reliability/)
