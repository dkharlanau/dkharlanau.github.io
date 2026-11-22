---
layout: default
title: "Data File Formats: CSV, JSON, Parquet, ORC, Avro and Beyond"
description: "A practical guide to choosing data file formats for SAP exports, APIs, S3 data lakes, analytics, dbt and AI: comparisons, design trade-offs, and a runnable DuckDB lab."
permalink: /atlas/concepts/data-file-formats/
parent: Concepts
content_model: article
author: Dzmitryi Kharlanau
status: needs_verification
verified: false
robots: noindex, follow
sitemap: false
last_modified_at: 2026-11-22
tags:
  - data-architecture
  - data-engineering
  - file-formats
  - sap-integration
  - analytics
  - parquet
  - avro
  - data-lake
related:
  - /atlas/concepts/data-contracts/
  - /atlas/concepts/data-lineage/
  - /atlas/concepts/data-quality-controls/
  - /atlas/concepts/cdc-change-data-capture/
  - /labs/ai-ready/data-rag/
  - /labs/enterprise-context/end-to-end-analytics/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/concepts/">Concepts</a></li>
    <li aria-current="page">Data File Formats</li>
  </ol>
</nav>

# Data File Formats: What to Use, When and Why

**A 20-row SAP mapping file, a live business event, and 50 million sales-order items should not automatically use the same format.** The right choice depends on who reads the data, how often it changes, and what work comes next.

This guide covers the familiar **CSV, JSON, Parquet, ORC and Avro**, plus JSON Lines, XML, Excel, Arrow/Feather, Protocol Buffers and other useful options. It also explains why **S3, dbt, Iceberg and Delta Lake are different layers**, not alternative file extensions.

> **The memory rule:** Text files make exchange easy. Columnar files make analytical scans efficient. Schema-based binary records make structured exchange reliable. Table formats manage many data files as one changing table.

## Choose in 30 seconds

| I need to… | Start with… | Why |
| --- | --- | --- |
| Give business users a small SAP mapping or reconciliation extract | **CSV** (or **XLSX** for manual review) | Easy to inspect; define types and encoding explicitly |
| Exchange one nested object through an API | **JSON** | Readable objects and arrays |
| Append millions of independent events or log records | **JSON Lines / NDJSON** | One JSON object per line; easy streaming and partial processing |
| Send structured records between services with an agreed schema | **Avro** or **Protobuf** | Compact binary serialization with schema tooling |
| Store large history for selective SQL analytics | **Parquet** | Columnar scans, compression and column pruning |
| Work in a Hive/Hadoop-oriented analytics estate | **ORC** or **Parquet** | Both are columnar; choose based on engine compatibility |
| Exchange data frames efficiently between analytical processes | **Arrow IPC / Feather** | Closely aligned with Arrow's in-memory representation |
| Update, delete or time-travel across many lake files | **Iceberg / Delta Lake / Hudi** | These manage *tables*, not just individual files |

This is a starting point, not a speed ranking. Measure real queries, file sizes, update patterns and engine support before standardising.

## First: four layers that people often confuse

```text
SAP API / export / event
          |
          v
FILE FORMAT       CSV | JSONL | Avro | Parquet | ORC
          |
          v
COMPRESSION       gzip | zstd | snappy | none
          |
          v
OBJECT STORAGE    Amazon S3 (or another object store)
          |
          v
TABLE MANAGEMENT  Optional: Iceberg | Delta Lake | Hudi
          |
          v
QUERY / TRANSFORM DuckDB | Athena | Spark | warehouse + dbt
```

This diagram is a *conceptual stack*, not a required installation order. Compression may be built into a format (such as Parquet), and a query engine can read ordinary files without a lake table format.

- **File format** defines how bytes represent data *within a file*.
- **Compression** reduces bytes. A `.csv.gz` is still CSV after decompression; a ZIP is an archive, not a relational schema.
- **Object storage** such as S3 stores objects and keys. It does not automatically enforce data types, relational keys, transactions or business meaning.
- **Table format** manages a set of data files with metadata and, depending on the implementation, snapshots, transactions and schema evolution.
- **dbt** typically executes transformations and tests through a compatible data-platform adapter. It is not a universal file reader or a file format.

## See the difference: rows, columns and events

Imagine a tiny SAP sales extract with two order items.

**CSV — a flat table:**

```csv
sales_order,item,plant,currency,net_amount
0000004711,000010,1000,EUR,125.50
0000004711,000020,1000,EUR,65.00
```

**JSON — one nested business object:**

```json
{
  "salesOrder": "0000004711",
  "currency": "EUR",
  "items": [
    {"item": "000010", "plant": "1000", "netAmount": 125.50},
    {"item": "000020", "plant": "1000", "netAmount": 65.00}
  ]
}
```

**JSON Lines — independent records, one per line:**

```jsonl
{"salesOrder":"0000004711","item":"000010","plant":"1000","netAmount":125.50}
{"salesOrder":"0000004711","item":"000020","plant":"1000","netAmount":65.00}
```

A **Parquet** or **ORC** file is binary, so you cannot inspect it meaningfully with a text editor. Their physical layouts are more complex than this, but the key idea is:

```text
Row-style concept:
  [4711, 000010, 1000, EUR, 125.50] [4711, 000020, 1000, EUR, 65.00]

Column-style concept:
  sales_order -> [4711, 4711]
  item        -> [000010, 000020]
  currency    -> [EUR, EUR]
  net_amount  -> [125.50, 65.00]
```

If a dashboard needs only `currency` and `net_amount` from 30 columns, columnar storage can avoid reading unrelated column values. Parquet also supports compression and statistics that compatible engines can use to skip work.

**Important:** An identifier such as `0000004711` is *text*, even if it contains only digits. Automatic number conversion can silently destroy leading zeros.

## The format comparison you will actually use

| Format | Best fit | Main trade-off or risk |
| --- | --- | --- |
| **CSV / TSV** | Flat exchange, mapping files, small extracts | No reliable built-in data types; delimiters, quotes, decimal conventions and encodings need an explicit contract |
| **JSON** | REST APIs, nested messages, configuration payloads | Verbose; timestamps, large integers and monetary amounts require careful handling |
| **JSONL / NDJSON** | Event logs, batch APIs, AI evaluation datasets | Per-record structure can drift; not a single JSON array |
| **XML** | Document exchange, SOAP, XML-based integrations | Verbose, but namespaces and schemas can be valuable |
| **XLSX** | Human validation, sign-off and exception lists | Easy to change by hand; formulas, formatting and automatic type conversions create reproducibility risks |
| **Parquet** | Large SQL datasets and historical analytics | Binary, not ideal for record-by-record updates; benefit depends on scan and file layout |
| **ORC** | Columnar analytical storage, often in Hive-oriented ecosystems | Great column statistics and indexing, but confirm support in the chosen engines |
| **Avro** | Schema-based events, data pipelines and record exchange | Great at record serialization; not the first choice for scanning a few columns from a huge analytical dataset |
| **Arrow IPC / Feather** | Fast local or inter-process data-frame exchange | Optimised for computation and interchange, not typically as compact as Parquet for long-term storage |
| **Protocol Buffers** | Typed service calls and event payloads | Requires schema definitions and compatible tooling |
| **MessagePack** | Compact application-level binary messages | Less inspectable than JSON; schema governance is external |
| **YAML** | Human-maintained configuration and metadata | Not a large-data analytics format; parsing and implicit types need care |
| **Fixed-width text** | Legacy systems with strict record layouts | Brittle column positions; exact lengths and encoding matter |
| **GeoJSON** | Maps and spatial features | Not a general replacement for analytical tables |

Two further distinctions matter in practice. **PDF and Markdown** are useful for documents and RAG source material, but are not alternatives to Parquet for structured sales records. **EDI (such as EDIFACT or X12)** defines business-message standards; it should not be treated as one interchangeable analytics format.

## Parquet vs ORC vs Avro: the architectural distinction

| Question | Parquet | ORC | Avro |
| --- | --- | --- | --- |
| Primary organisation | Columnar | Columnar | Record-oriented |
| Typical strength | SQL analytics and selective column reads | Analytical scans, type-aware encoding and indexes | Efficient serialization and schema-based data interchange |
| Human-readable? | No | No | No (binary data file) |
| Good for frequent per-record events? | Usually not first choice | Usually not first choice | Often a good fit |
| Good for scanning a subset of many columns? | Yes | Yes | Typically less efficient |
| Schema handling | Schema in file metadata; cross-file compatibility still needs governance | Type-aware file schema; table-level evolution needs governance | Writer and reader schemas support defined resolution rules |

A useful shortcut: **Parquet and ORC are usually queried by analysts; Avro is often produced and consumed by pipelines.** These are patterns, not exclusive use restrictions.

An Avro object-container file includes its writer schema. An individual Avro-encoded message in a stream does *not* automatically include a full embedded schema: a wire protocol or schema registry may be needed. Likewise, an ORC file does not create multi-file ACID transactions by itself.

## Three real-world design cases (synthetic examples)

### Case 1 — SAP customer master-data migration

**Problem:** A team needs to review a customer-to-sales-area mapping, correct ten rows, then import the approved result.

**Choose:** CSV with a written column contract; XLSX can be a *review surface* if operations need comments or controlled dropdowns.

**Checks:** Preserve BP/customer IDs as strings; validate account groups, sales-area keys and duplicates against approved reference data; compare row counts and scoped key sets before posting. Treat the mapping file as an input to validation, not proof that the target master data is correct.

**Avoid:** Reading an identifier as a number, making business-critical changes by filtering manually, or storing unapproved production extracts in Git.

### Case 2 — Millions of SAP sales items for reporting

**Problem:** Analytics repeatedly groups sales items by period, sales organisation, currency and product.

**Choose:** A governed extraction path into S3, with **Parquet** as a strong candidate for curated analytical data. Organise files by useful query partitions, not by every individual order. Keep the grain at **one sales-order item**, or explicitly model a different grain.

**Checks:** Count source and target records; reconcile amounts *within each currency*; validate keys, date semantics, late-arriving changes and access permissions. Consider Iceberg or another supported table format if consumers need atomic changes, deletes or reliable snapshots.

**Avoid:** Summing different currencies as one amount, creating thousands of tiny files, or assuming that a Parquet file is automatically a managed table.

### Case 3 — Business events from an SAP-connected integration

**Problem:** A downstream application needs to react when a business object changes.

**Choose:** JSON when simple, readable API or event contracts are enough; consider Avro or Protobuf when payload efficiency and schema governance matter and the chosen event platform supports them.

**Checks:** Define stable business keys, event type, schema version, timestamp, retry behaviour and idempotency. Choose a supported SAP integration or event mechanism rather than assuming every business object exposes a native event.

**Avoid:** Confusing an SAP IDoc *message structure* with one file format. IDoc communication can use different representations and adapters; the payload and transport are separate design choices.

## Hands-on lab: SAP-style CSV to Parquet with DuckDB

**Outcome:** You will create a small synthetic extract, preserve SAP-style identifiers, convert the data into Parquet and verify the result with SQL. No S3 account or SAP system is needed.

Install the dependency:

```bash
python -m pip install duckdb
```

Save as `file_formats_lab.py`:

```python
import csv
import duckdb

rows = [
    ["0000004711", "000010", "1000", "EUR", "125.50"],
    ["0000004711", "000020", "1000", "EUR", "65.00"],
    ["0000004712", "000010", "2000", "USD", "40.00"],
]

with open("sap_sales.csv", "w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerow(["sales_order", "item", "plant", "currency", "net_amount"])
    writer.writerows(rows)

con = duckdb.connect()
con.execute("""
    CREATE OR REPLACE VIEW sales AS
    SELECT * FROM read_csv(
        'sap_sales.csv',
        header = true,
        columns = {
            'sales_order': 'VARCHAR',
            'item': 'VARCHAR',
            'plant': 'VARCHAR',
            'currency': 'VARCHAR',
            'net_amount': 'DECIMAL(12,2)'
        }
    )
""")
con.execute("""
    COPY (SELECT * FROM sales)
    TO 'sap_sales.parquet' (FORMAT PARQUET, COMPRESSION ZSTD)
""")

result = con.execute("""
    SELECT currency, COUNT(*) AS items, SUM(net_amount) AS total
    FROM read_parquet('sap_sales.parquet')
    GROUP BY currency
    ORDER BY currency
""").fetchall()

print(result)
# Expected totals: EUR 190.50 across 2 items; USD 40.00 across 1 item.
```

Now inspect `sap_sales.parquet` with a Parquet-capable tool. It will not look like the CSV in a text editor. Try querying just `sales_order` and `net_amount` and compare the schema and file size. With **three rows**, do not expect the Parquet file to be smaller; its metadata has overhead. The gains become meaningful only with an appropriate dataset and workload.

**Next experiment:** Generate 100,000 synthetic records, query a single analytical column from CSV and Parquet, and compare timings *after repeating runs*. This is a local demonstration, not a universal benchmark.

## Where S3 and dbt fit

```text
Approved SAP extract / API / event
                |
                v
      Ingestion + validation
                |
                v
S3 raw zone: CSV / JSONL / Avro (example choices)
                |
                v
      SQL / Spark transformation
                |
                v
S3 curated zone: Parquet
                |
                +--> Optional Iceberg / Delta / Hudi metadata
                |
                v
Compatible query engine or warehouse
                |
                v
     dbt models + tests + documentation
                |
                v
   Governed reports / data products / AI
```

**S3 is storage, not a database.** A compatible query engine and catalog configuration are required for SQL access. dbt runs its SQL models *inside a supported platform through an adapter*; it does not make all files in S3 queryable by itself.

One useful exception is **`dbt seed`**: a small, relatively static CSV mapping in the dbt repository can be loaded with `dbt seed`. The dbt documentation explicitly discourages using seeds as a bulk raw-data ingestion method or for sensitive production extracts.

For SAP, this architecture is a **possible external analytics pattern**, not a native S/4HANA configuration recipe. Confirm approved extraction interfaces, licensing, data residency, access controls, update semantics and the exact target engine before adopting it.

## Do not skip these six controls

1. **Grain and keys.** Decide whether one row means an order header, item, event or snapshot. Keep identifiers as strings where leading zeros matter.
2. **Types and business meaning.** Freeze decimal precision, currencies, units, timestamps, null values and the meaning of each field.
3. **Schema evolution.** Define what happens when producers add, remove or reinterpret a field. File metadata is not a full [data contract](/atlas/concepts/data-contracts/).
4. **Reconciliation.** Compare counts, distinct business keys and business totals *within appropriate dimensions*, before and after conversion.
5. **Security and retention.** Classify SAP data, minimise exports, encrypt where required, control access and apply retention/deletion rules.
6. **Operational file design.** Monitor delivery frequency, duplicate batches, partition pruning, small files and recovery from failed writes.

The failure to watch for is **a perfectly readable file that represents the wrong business data**. Choosing Parquet cannot fix a missing company-code filter or an incorrect sales-order population.

## The table-format bonus: Iceberg, Delta Lake and Hudi

These are not direct replacements for CSV or Parquet. They add a **table-management layer** over collections of files.

| Table format | What it adds | Typical design question |
| --- | --- | --- |
| **Apache Iceberg** | Table metadata, snapshots, schema/partition evolution, and support for data files such as Parquet, Avro and ORC | Must different engines read and update the same governed table? |
| **Delta Lake** | A transaction log alongside Parquet data, with table-level transactions and version history | Do we need reliable upserts, deletes and history with supported engines? |
| **Apache Hudi** | Transactional lake tables with incremental data processing, indexing and update-oriented storage options | Are frequent record changes and incremental consumption the main workload? |

Compatibility, concurrency and write features differ by engine and version. Pick a table format only after deciding how the table is written, read, catalogued, maintained and recovered.

## Check your architecture judgment

**Question:** A logistics dashboard scans 30 million SAP document items every morning. It needs only five fields. The source may later send corrections to previously loaded items. Should the team choose CSV, Parquet or Iceberg?

<details>
<summary>Reveal the reasoning</summary>
<p><strong>Start with Parquet</strong> for a columnar analytical dataset. But ask how corrections arrive, who applies them, and whether consumers require atomic reads or historical snapshots. If the files must behave as a mutable table, <strong>Iceberg (or another supported table format)</strong> may be justified on top of the data files. CSV is still useful for a small controlled mapping, not the primary large-scale scan format. Validate engine compatibility, update volume, currency semantics and reconciliation before making the decision.</p>
</details>

## Further reading

- [Data Contracts](/atlas/concepts/data-contracts/) — what a producer must promise beyond the file schema.
- [Data Quality Controls](/atlas/concepts/data-quality-controls/) — why successful parsing is not data correctness.
- [CDC: Change Data Capture](/atlas/concepts/cdc-change-data-capture/) — how later changes reach the lake.
- [End-to-End Logistics Analytics](/labs/enterprise-context/end-to-end-analytics/) — business grain, metrics and cross-process ownership.
- [AI Ready: Data and RAG](/labs/ai-ready/data-rag/) — keep retrieval and unstructured evidence separate from structured analytics.

## Primary sources

- [Apache Parquet — Overview](https://parquet.apache.org/docs/overview/)
- [Apache ORC — Background and file design](https://orc.apache.org/docs/)
- [Apache Avro — Documentation and schema handling](https://avro.apache.org/docs/)
- [Apache Arrow — Arrow vs Parquet and Feather](https://arrow.apache.org/faq/)
- [Apache Iceberg — Table specification](https://iceberg.apache.org/spec/)
- [Delta Lake — Frequently asked questions](https://docs.delta.io/delta-faq/)
- [Apache Hudi — Overview](https://hudi.apache.org/docs/overview.html/)
- [DuckDB — Reading and writing Parquet](https://duckdb.org/docs/stable/data/parquet/overview)
- [dbt — Seeds](https://docs.getdbt.com/docs/build/seeds)
- [dbt — Supported data platforms](https://docs.getdbt.com/docs/supported-data-platforms)

**Editorial status:** Working guide pending site review. General format properties are based on the linked official documentation; platform-specific integration choices, benchmarks and SAP extraction methods require validation in the target landscape. All example records are synthetic.
