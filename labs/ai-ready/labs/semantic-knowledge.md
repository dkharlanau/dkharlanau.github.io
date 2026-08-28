---
layout: default
title: "AI Ready Lab — Semantic Data and Knowledge Graphs"
description: "Hands-on ERP practice for vocabulary, taxonomy, ontology, RDF, SHACL, SPARQL, property graphs, provenance, Fabric IQ, and AI retrieval decisions."
permalink: /labs/ai-ready/labs/semantic-knowledge/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-28
hide_global_cta: true
tags: [ai, lab, data, semantics, taxonomy, ontology, knowledge-graph, rdf, sparql, shacl, fabric-iq, microsoft-fabric]
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

## Platform case study: Microsoft Fabric IQ

Checked against Microsoft Learn on 28 Aug 2026. Fabric IQ and ontology capabilities described here are still marked as preview, so use this section as an architecture case study, not as a promise that every feature is production-ready for every tenant.

Fabric IQ is useful because it puts several ideas from this lab into one Microsoft Fabric architecture. OneLake provides the data foundation. Power BI semantic models provide curated measures and dimensions. Ontology defines business entities, relationships, properties, rules, and actions. Graph stores and traverses connected data. Data agents answer questions. Operations agents monitor business signals and can recommend or take configured actions.

### Assessment answer in 45 seconds

**Fabric IQ is a semantic and operational context layer in Microsoft Fabric.** It turns governed data into shared business concepts that people, analytics, and agents can use consistently. OneLake is the data foundation, Power BI semantic models provide trusted KPIs, ontology defines business entities and relationships, Graph supports relationship-heavy analysis, and agents consume this context. For SAP, I would use Fabric IQ above governed SAP and non-SAP data. I would not present it as a replacement for S/4HANA, SAP master-data governance, or the integration layer. The Lead questions are data freshness, semantic ownership, permissions, action controls, and where the authoritative business rule still lives.

### Architecture map for an SAP scenario

```text
SAP and non-SAP sources
        ↓
source-specific integration / replication / events
        ↓
Microsoft Fabric data foundation / OneLake
        ↓
Power BI semantic model  +  Fabric IQ ontology
        ↓                         ↓
trusted KPIs                 business meaning
                                  ↓
                                Graph
                         relationships + paths
                         ↙                ↘
                  Data agent       Operations agent
                  ask / analyse    monitor / recommend / act
                         ↘                ↙
                    governed user or workflow
```

The first arrow is important: **getting SAP data into or near Fabric is a separate integration decision. Fabric IQ does not remove it.**

| Fabric component | Main job | SAP-style example | Lead concern |
| --- | --- | --- | --- |
| OneLake | Shared Fabric data foundation | Sales, delivery, inventory, supplier, sensor, and external logistics data | Source, freshness, lineage, access |
| Power BI semantic model | Curated analytics measures and dimensions | OTIF, backlog, order value, supplier delay rate | KPI ownership and calculation consistency |
| Ontology (preview) | Shared business entities, relationships, properties, rules, and actions | Customer, SalesOrder, Material, Delivery, Supplier, Plant | Do not create a second uncontrolled business dictionary |
| Graph | Store and traverse connected data | SalesOrder → Delivery → Shipment → Exception | Relationship quality and provenance |
| Data agent | Conversational analysis over governed Fabric data | “Which blocked orders have the highest value?” | Grounding, permissions, answer evidence |
| Operations agent | Monitor signals and recommend or take configured actions | Alert when a high-value delivery enters a defined risk state | Identity, approval, action scope, audit |
| Ontology MCP | Expose ontology context to supported or custom agents | Let an external agent discover entity types and search governed ontology | Tool permissions and client trust boundary |

The IQ workload also includes Plan for planning and forecasting. It is useful in its own domain, but it is not the main component in this SAP semantic example.

### O2C example: explain a blocked sales order

A practical ontology can stay small:

```text
Customer
SalesOrder
SalesOrderItem
Material
Plant
CreditHold
Delivery
Shipment
Invoice
```

Useful relationships might be:

```text
Customer    --places------> SalesOrder
SalesOrder  --contains----> SalesOrderItem
SalesOrderItem --requests-> Material
SalesOrder  --blockedBy---> CreditHold
SalesOrder  --fulfilledBy-> Delivery
Delivery    --shipsAs-----> Shipment
SalesOrder  --billedBy----> Invoice
```

Now separate the questions by source instead of asking one agent to solve everything:

| Business question | Best first layer |
| --- | --- |
| What does “credit hold” mean? | Ontology + governed business definition |
| Which high-value orders are blocked? | Semantic model + bound data |
| How is this order connected to delivery and shipment exceptions? | Graph traversal |
| What is the current SAP status right now? | Approved live SAP read API/tool when freshness matters |
| Which exception needs attention? | Operations agent when a monitored rule and action boundary are justified |

This is the key design point: **semantic context explains the business. It does not automatically become the system of record.**

### P2P example: supplier delay risk

A second small ontology could connect:

```text
Supplier → PurchaseOrder → ScheduleLine → InboundDelivery → GoodsReceipt
                    ↓
                  Material → Plant
```

A useful question is: “Which purchase orders are at risk of late receipt, which materials and plants are affected, and which supplier relationship is involved?”

Fabric IQ can help when the answer needs several connected domains. If the requirement is only a fixed KPI on one clean table, a semantic model or SQL query may be enough. Do not add a graph because a graph feature exists.

### SAP integration boundary

Microsoft documents SAP HANA and SAP BW connectors in Data Factory for Microsoft Fabric. For example, the SAP HANA connector supports Dataflow Gen2 and pipeline/copy scenarios through an on-premises gateway, while SAP BW Application Server is available through Dataflow Gen2. These connectors are data-access options; they are not the definition of the enterprise integration architecture.

For a real SAP design, decide the source path from business requirements:

```text
latency
change volume
transactional vs analytical purpose
authoritative source
recovery and replay
security
SAP supportability
ownership
```

Do not say “Fabric IQ makes SAP real-time.” A connector, replication path, event flow, or approved API still has its own latency and recovery behavior.

### Five Lead-level checks

1. **Freshness** — Microsoft notes that upstream changes need a refresh before they appear in an ontology item. Test the real freshness path instead of assuming that “real-time” applies to every layer.
2. **Semantic ownership** — decide who owns definitions such as Customer, Material, On-Time Delivery, Credit Hold, and Supplier Risk. A shared ontology without ownership creates a larger shared ambiguity.
3. **Transaction authority** — keep authoritative posting, validation, and process control in the system designed to own it. Do not move SAP transaction rules into an ontology only because an agent can see them there.
4. **Agent authority** — operations agents can recommend and run configured actions. Microsoft documents a dedicated Entra Agent ID, but the agent operates in delegated mode using the creator's permissions. Review least privilege, approval, audit, and the exact action contract.
5. **Lifecycle risk** — Fabric IQ ontology and related integration features are preview. Check current limitations, capacity requirements, refresh behavior, region/tenant settings, and support policy before making a production commitment.

### When Fabric IQ is a good fit

Use it when several systems describe the same business objects differently and analytics or agents need one governed business language. It becomes more useful when questions cross domains, relationships matter, and several experiences should reuse the same definitions.

Do not start with Fabric IQ when the problem is a single report, one deterministic query, a simple API lookup, or a transactional workflow that already has a clear system owner. In those cases, a smaller architecture is usually easier to test and operate.

### How it maps to this lab

```text
This lab                         Microsoft Fabric IQ case study
-----------------------------------------------------------------
controlled vocabulary           shared business language
ontology                         Fabric IQ ontology (preview)
RDF/property graph concepts      Fabric Graph + ontology graph view
semantic analytics              Power BI semantic model
live tool boundary               SAP/API/source integration path
RAG / grounded Q&A               Data agent / Foundry or Copilot agent
monitored business condition     Operations agent
portable agent access            Ontology MCP server
```

Fabric IQ is one product implementation of these ideas. It does not redefine ontology, graph theory, RAG, or enterprise integration. Learn the concepts first; then judge the platform by the business problem and operating boundary.

### Fabric IQ source baseline — checked 28 Aug 2026

- [What is Fabric IQ?](https://learn.microsoft.com/en-us/fabric/iq/overview) — OneLake, semantic models, ontology, Graph, Plan, data agents, and operations agents.
- [What is ontology (preview)?](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview) — entity types, relationships, graph representation, querying, lineage, and refresh behavior.
- [Agent integration options for ontology](https://learn.microsoft.com/en-us/fabric/iq/ontology/concepts-agent-integration) — operations agent, data agent, Foundry IQ, Copilot Studio, and custom agents through ontology MCP.
- [Create and configure operations agents](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/operations-agent) — monitoring, actions, rule queries, Entra Agent ID, and delegated permissions.
- [SAP HANA connector overview](https://learn.microsoft.com/en-us/fabric/data-factory/connector-sap-hana-overview) — current Fabric Data Factory support for SAP HANA.
- [SAP BW Application Server connector overview](https://learn.microsoft.com/en-us/fabric/data-factory/connector-sap-bw-application-server-overview) — current Fabric Data Factory support for SAP BW Application Server.

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
- Do not treat Fabric IQ as an SAP integration shortcut or a replacement for the transactional system of record.

## Done when

You can explain and demonstrate:

1. controlled vocabulary vs taxonomy;
2. ontology vs knowledge graph;
3. RDF graph vs property graph;
4. SHACL validation of a missing relation;
5. SPARQL vs Cypher;
6. open-source tool vs free hosted/proprietary option;
7. static graph fact vs current live system state;
8. normal RAG vs graph-assisted retrieval;
9. how Fabric IQ maps semantic models, ontology, Graph, and agents to the same concepts;
10. why SAP connectivity, source authority, freshness, and action permissions remain separate Lead decisions.

## Tool status baseline — checked 28 Aug 2026

- [Protégé](https://protege.stanford.edu/) — free, open-source ontology editor.
- [VocBench](https://vocbench.uniroma2.it/) — free, open-source vocabulary and ontology platform.
- [Apache Jena](https://jena.apache.org/download/) — Apache RDF framework and Fuseki SPARQL server.
- [Zazuko SHACL Playground](https://zazuko.com/tools/shacl-playground/) — open-source browser SHACL playground.
- [GraphDB documentation](https://graphdb.ontotext.com/documentation/) — current Free edition and license information.
- [Wikidata data access](https://www.wikidata.org/wiki/Wikidata:Data_access) — public Query Service and access guidance.
- [DBpedia SPARQL](https://www.dbpedia.org/resources/sparql/) — public endpoint and usage guidance.
- [Neo4j Aura documentation](https://neo4j.com/docs/aura/) — AuraDB Free learning tier.
- [Microsoft Fabric IQ](https://learn.microsoft.com/en-us/fabric/iq/overview) — Microsoft semantic and operational intelligence case study; preview details are date-sensitive.

Next action: build the vocabulary and taxonomy first. Then model only enough ontology and graph structure to answer the scenario questions. After that, compare the same design with the Fabric IQ case study and identify which parts remain outside the semantic layer.

Read first: [Data and RAG](/labs/ai-ready/data-rag/) · Continue with [Business AI Technology Landscape](/labs/business-ai/technologies/) · [RAG with Evals](/labs/ai-ready/labs/rag-evals/) · [Evals and Reliability](/labs/ai-ready/evals-reliability/)