---
layout: default
title: "AI Ready — Data and RAG"
description: "A practical architecture guide for retrieval, metadata, chunking, hybrid search, reranking, grounding, and retrieval evaluation."
permalink: /labs/ai-ready/data-rag/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-18
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

## Modern data platforms

An SAP Lead does not need to become a platform engineer. But you should understand where common data platforms sit in enterprise architecture, why companies use them, and what changes when SAP data leaves the transactional system.

The useful question is not **“Which platform is best?”** Ask **“Which workload, data boundary, operating model, and ecosystem are we designing for?”**

| Platform | Core idea | Typical strength | SAP Lead lens |
|---|---|---|---|
| **Databricks** | Lakehouse-based data and AI platform | Data engineering, analytics, ML and AI on a shared platform | Useful when SAP data must be combined with large non-SAP datasets, engineering pipelines, data science, or AI workloads |
| **Snowflake** | Cloud data platform with separated storage and compute | Governed SQL analytics, data engineering, sharing, and elastic workloads | Useful as a central analytical layer where SAP and non-SAP data are modeled and consumed across teams |
| **Microsoft Fabric** | End-to-end SaaS analytics platform built around OneLake | Integrated ingestion, engineering, warehouse, real-time analytics, and Power BI | Strong architectural fit when the enterprise already uses Microsoft data and BI services |
| **Google BigQuery** | Fully managed serverless data platform | Large-scale analytics without infrastructure management | Strong fit when the data estate and analytics workloads are centered on Google Cloud |
| **Amazon Redshift** | Fully managed cloud data warehouse with provisioned and serverless options | SQL analytics inside the AWS ecosystem | Strong fit when AWS is the strategic cloud and governed analytical warehousing is the main need |

This is a positioning map, not a product ranking. The platforms overlap and their product boundaries change. Use the comparison model, then verify current features in vendor documentation.

### Databricks

**Remember:** lakehouse + data engineering + analytics + AI.

Databricks positions its platform around enterprise data, analytics, and AI on a lakehouse architecture. For an SAP Lead, the important point is the architectural role: SAP data can become one governed source among many and can be combined with logs, documents, IoT, external data, analytics, and AI workloads.

**Interview signal:** explain why a lakehouse may be useful when the problem is broader than classic BI and includes engineering or AI workloads.

Official reference: [Databricks — What is Databricks?](https://docs.databricks.com/aws/en/introduction/)

### Snowflake

**Remember:** cloud data platform + elastic compute + analytical workload separation.

Snowflake separates persisted storage from independent compute resources called virtual warehouses. For an SAP Lead, focus on ingestion or replication, batch versus change-data-capture patterns, semantic ownership after extraction, access, quality, and downstream consumption.

**Interview signal:** explain why moving SAP tables into a warehouse is not the same as moving an SAP business model.

Official reference: [Snowflake — Key concepts and architecture](https://docs.snowflake.com/en/user-guide/intro-key-concepts)

### Microsoft Fabric

**Remember:** integrated analytics SaaS + OneLake + Power BI ecosystem.

Microsoft Fabric combines ingestion, engineering, data science, real-time analytics, warehousing, databases, and Power BI. OneLake is the shared logical data lake across Fabric workloads.

For an SAP Lead, discuss how SAP data reaches Fabric, where transformation logic belongs, how semantic models relate to SAP business definitions, and whether the architecture duplicates logic already available in SAP analytical products.

**Interview signal:** explain the difference between an analytics platform and the SAP transactional system that still owns operational execution.

Official reference: [Microsoft Fabric overview](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview)

### Google BigQuery

**Remember:** serverless analytics at Google Cloud scale.

BigQuery is a fully managed data platform with a serverless architecture. For an SAP Lead, the design questions remain familiar: extraction pattern, freshness, business semantics, raw versus curated data, access, lineage, and cost.

**Interview signal:** explain why serverless infrastructure removes some platform operations but does not remove data architecture or governance work.

Official reference: [BigQuery overview](https://cloud.google.com/bigquery/docs/introduction)

### Amazon Redshift

**Remember:** managed AWS data warehouse + SQL analytics.

Amazon Redshift is a fully managed cloud data warehouse, and AWS also provides Redshift Serverless. For an SAP Lead, focus on the SAP ingestion boundary, analytical modeling, integration with the wider AWS estate, workload and cost decisions, monitoring, and recovery.

**Interview signal:** explain why a managed warehouse can simplify infrastructure while end-to-end data ownership remains an enterprise responsibility.

Official reference: [Amazon Redshift overview](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)

### What changes when SAP data leaves SAP?

The platform name is less important than the boundary you create.

1. **Transaction ownership does not move.** The operational ERP still executes the business transaction. The target platform normally receives data for analytics, AI, reporting, data products, or cross-system processing.
2. **Business semantics can be lost.** SAP meaning may depend on document flow, status logic, organizational structure, units, currencies, master data validity, configuration, and authorization context.
3. **Freshness becomes a design decision.** Choose daily batch, incremental loads, CDC, streaming, or live access from the business requirement, not from fashion.
4. **Recovery must be designed.** Define checkpoints, duplicate handling, replay, late-arriving data, schema changes, monitoring, reconciliation, and ownership.
5. **Governance crosses systems.** Security, retention, lineage, privacy, data quality, and access rules must survive the movement.

### Compare platforms with the same questions

| Dimension | Questions to ask |
|---|---|
| **Workload** | BI only, engineering, ML/AI, streaming, data products, or a mix? |
| **Cloud strategy** | AWS, Azure/Microsoft, Google Cloud, multi-cloud, or platform-neutral? |
| **Data model** | Warehouse-first, lakehouse, open files, curated marts, semantic layer? |
| **SAP integration** | Batch, CDC, APIs, events, files, replication product, or virtual access? |
| **Latency** | What freshness is actually required by the business decision? |
| **Semantics** | Where are SAP business definitions preserved and governed? |
| **Governance** | Who owns lineage, access, quality, retention, and sensitive fields? |
| **Operations** | Who monitors failed loads, duplicates, schema drift, and reconciliation? |
| **Skills** | Which platform can the organization realistically build and operate? |
| **Cost** | How do storage, compute, concurrency, data movement, and idle capacity affect cost? |
| **Portability** | How much depends on proprietary services or formats? |
| **AI readiness** | Can governed enterprise data be safely reused for ML, retrieval, and agent workloads? |

### SAP Lead assessment drill

You should be able to answer these without opening product documentation:

1. What is the practical difference between a data warehouse and a lakehouse?
2. Why might a company choose Databricks for a data-and-AI program?
3. What is the architectural value of Snowflake separating storage and compute?
4. Why is OneLake important to the Microsoft Fabric model?
5. What does serverless change in BigQuery, and what responsibilities remain?
6. Where does Redshift fit in an AWS-centered data architecture?
7. If SAP data is replicated to one of these platforms, where should business semantics be owned?
8. When is daily batch enough, and when would CDC or streaming be justified?
9. How do you prove that the target contains complete and reconciled SAP data?
10. When should you challenge the requirement to copy SAP data at all?

A useful Lead-level answer pattern is:

> **Business decision → required data → source of truth → latency → movement pattern → target platform → semantic ownership → controls → operations → cost and trade-offs.**

Do not choose Databricks, Snowflake, Fabric, BigQuery, or Redshift from the product name first. Start from the workload, required freshness, SAP semantics, cloud strategy, governance, operating skills, recovery model, and cost.

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
