---
layout: default
title: "AI Ready Lab — Semantic Data and Knowledge Graphs"
description: "Hands-on ERP practice for vocabulary, taxonomy, ontology, RDF, SHACL, SPARQL, property graphs, provenance, and AI retrieval decisions."
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

## Learning context

Use this lab after the [Data and RAG](/labs/ai-ready/data-rag/) explanation. You should already understand that data, taxonomy, ontology, knowledge graph, RAG, and live tools solve different problems.

The exercise is deliberately small. It is not a reference architecture and it is not a requirement to use every tool in one real solution. The purpose is to compare representations and make architecture choices visible.

## What you will learn

```text
raw data
   ↓
controlled terms
   ↓
taxonomy / thesaurus
   ↓
ontology where stronger semantics are useful
   ↓
concrete graph facts
   ↓
validation + queries
   ↓
RAG / graph retrieval / live tools chosen by question type
```

Main rule: **use the smallest semantic layer that solves a real problem.**

## Scenario

A sales order cannot move to delivery because of a credit restriction.

```csv
order_id,customer_id,material_id,plant,status
SO-4711,C-1000,M-77,P01,CREDIT_HOLD
```

We want to answer:

- What does `CREDIT_HOLD` mean?
- Is `credit block` the same concept?
- What type of exception is it?
- Which customer and material belong to the order?
- Which rule says a sales order must have a customer?
- Which source confirms the current status?
- Which questions belong in RAG and which need a live tool?

## Tool map

Free and open source are not the same thing.

| Tool | Learn | Access model | Exercise |
| --- | --- | --- | --- |
| [Protégé](https://protege.stanford.edu/) | OWL ontology modelling | Free and open source | Model classes and relations |
| [VocBench](https://vocbench.uniroma2.it/) | SKOS vocabulary and thesaurus management | Free and open source | Add preferred, alternative, broader, and related terms |
| [Apache Jena / Fuseki](https://jena.apache.org/) | RDF storage and SPARQL | Apache open source | Load Turtle and query it |
| [Zazuko SHACL Playground](https://zazuko.com/tools/shacl-playground/) | SHACL validation | Open source web tool | Validate a required customer relation |
| [GraphDB Free / Desktop](https://graphdb.ontotext.com/documentation/) | RDF repository and inference | Free edition; proprietary | Compare explicit and inferred facts |
| [Wikidata Query Service](https://query.wikidata.org/) | Public knowledge graph | Public service | Practise SPARQL on real data |
| [DBpedia SPARQL](https://www.dbpedia.org/resources/sparql/) | Linked open data | Public service | Compare another RDF model |
| [Neo4j AuraDB Free](https://neo4j.com/docs/aura/) | Property graphs and Cypher | Free hosted tier; proprietary service | Build the same example as nodes and relationships |

Two current cautions:

- The older playground at `shacl.org` is still online, but its page says that implementation is no longer actively maintained. Use the current Zazuko playground for this exercise.
- Current GraphDB documentation describes a Free edition with a free-license process. Free does not mean open source.

## Step 1: define the vocabulary

Start with language before technology.

```text
Preferred term: Credit hold
Alternative term: Credit block
Broader term: Commercial exception
Broader term above that: Order exception
Related term: Credit exposure
Related term: Payment risk
```

Use VocBench, or write the terms as a small SKOS file.

What changed? Different labels can now point to one agreed concept.

## Step 2: build a taxonomy

```text
Order exception
├── Commercial exception
│   ├── Credit hold
│   └── Pricing block
└── Logistics exception
    ├── Delivery block
    └── Stock shortage
```

A taxonomy answers: **where does this concept belong?**

It does not describe every relationship between orders, customers, products, plants, and blocks.

## Step 3: model an ontology in Protégé

Create only the classes needed for the question:

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

Add class relationships:

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

Do not model the whole ERP landscape. Stop when the model can answer the learning questions.

## Step 4: create RDF facts

Represent the same scenario as Turtle:

```turtle
@prefix ex: <https://example.org/erp/> .
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

The ontology describes the model. These triples describe concrete instances.

## Step 5: validate with SHACL

A graph can be valid RDF and still contain bad business data. Require every `SalesOrder` to have exactly one customer.

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

1. The order has one customer → it should conform.
2. Remove the customer relation → validation should fail.

Remember:

```text
Ontology → what kinds of things and relations make sense
SHACL    → whether this concrete graph meets required constraints
```

## Step 6: query with Jena / Fuseki

Load the Turtle data into Fuseki and run SPARQL:

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

Be able to separate four things: ontology, RDF facts, query, and result.

## Step 7: compare inference in GraphDB

Load the same model and facts into GraphDB if you want to explore reasoning.

```text
explicit fact:  CreditHold-88 is a CreditHold
schema fact:    CreditHold is a subclass of OrderBlock
inferred view:  CreditHold-88 can be treated as an OrderBlock
```

Check the configured reasoning rules before comparing results. Different repositories can use different inference profiles.

## Step 8: build the same example in Neo4j

A property graph can represent useful business relationships without RDF or OWL.

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

Query it with Cypher:

```cypher
MATCH (o:SalesOrder)-[:BLOCKED_BY]->(b)
RETURN o.id AS order_id, labels(b) AS block_types, b.id AS block_id
```

Lead question: should RDF/OWL or a property graph win by default? No. Compare semantics, interoperability, reasoning, query patterns, team skills, operations, and product constraints.

## Step 9: practise on public graphs

### Wikidata Query Service

```sparql
SELECT ?city ?cityLabel
WHERE {
  ?city wdt:P31 wd:Q515 .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
LIMIT 10
```

Wikidata Query Service is useful for learning SPARQL on a large public graph. Follow its documented service limits; it is not an unlimited bulk-data backend.

### DBpedia

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

DBpedia also provides a shared public SPARQL endpoint. Use it for learning and exploration within its fair-use limits.

## Step 10: connect the semantic layer back to AI

Do not finish with “we have a graph, therefore use GraphRAG.” Route each question to the simplest useful source.

| Question | Good first source |
| --- | --- |
| What does “credit block” mean? | Vocabulary / thesaurus + source document |
| What category is it? | Taxonomy |
| Which relations are allowed for a SalesOrder? | Ontology |
| Which order is connected to which block? | RDF/property graph query |
| Does every SalesOrder have a customer? | SHACL validation |
| What does the current credit policy say? | Document RAG |
| What is SO-4711 status right now? | Live API / read tool |
| Which systems and documents connect to this exception? | Graph-assisted retrieval when relationship paths matter |

RAG, semantic models, graph retrieval, and live tools solve different information problems.

## Keep provenance with the fact

For enterprise use, a relation needs context and evidence.

```text
fact:         SO-4711 --blockedBy--> CreditHold-88
source:       credit-service
observed_at:  2026-08-25T08:10Z
owner:        credit-management
confidence:   confirmed
```

An LLM may propose entities and relationships, but a generated edge is not automatically an enterprise fact.

```text
LLM proposes
   ↓
validation checks
   ↓
source evidence confirms
   ↓
governed approval where needed
```

## Constraints and failure modes

- Do not build a full ontology before you have a question that needs it.
- Do not call every graph a knowledge graph without meaning, ownership, and provenance.
- Do not treat a free proprietary edition as open source.
- Do not use a public SPARQL service as an unlimited production dependency.
- Do not trust an LLM-extracted relation without evidence.
- Do not add GraphRAG until simpler retrieval shows a measured relationship or global-query gap.

## Done when

You can explain and demonstrate:

1. controlled vocabulary vs taxonomy;
2. ontology vs knowledge graph;
3. RDF graph vs property graph;
4. SHACL validation of a missing relation;
5. SPARQL vs Cypher;
6. open-source tool vs free hosted/proprietary option;
7. static graph fact vs current live system state;
8. normal RAG vs graph-assisted retrieval.

## Tool status baseline — checked 25 Aug 2026

- [Protégé](https://protege.stanford.edu/) — free, open-source ontology editor.
- [VocBench](https://vocbench.uniroma2.it/) — free, open-source vocabulary and ontology platform.
- [Apache Jena](https://jena.apache.org/download/) — Apache RDF framework and Fuseki SPARQL server.
- [Zazuko SHACL Playground](https://zazuko.com/tools/shacl-playground/) — open-source browser SHACL playground.
- [GraphDB documentation](https://graphdb.ontotext.com/documentation/) — current Free edition and license information.
- [Wikidata data access](https://www.wikidata.org/wiki/Wikidata:Data_access) — public Query Service and access guidance.
- [DBpedia SPARQL](https://www.dbpedia.org/resources/sparql/) — public endpoint and usage guidance.
- [Neo4j Aura documentation](https://neo4j.com/docs/aura/) — AuraDB Free learning tier.

Next action: build the vocabulary and taxonomy first. Then model only enough ontology and graph structure to answer the scenario questions.

Read first: [Data and RAG](/labs/ai-ready/data-rag/) · Continue with [RAG with Evals](/labs/ai-ready/labs/rag-evals/) · [Evals and Reliability](/labs/ai-ready/evals-reliability/)
