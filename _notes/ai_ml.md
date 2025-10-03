---
title: "AI & ML Around SAP"
subtitle: "Deterministic core. Probabilistic edge."
tags:
  - AI
  - Machine Learning
  - SAP
excerpt: "Keep SAP clean while probabilistic services around it drive forecasts, risk signals, and intelligent automation."
permalink: /notes/ai-ml/
---

Enterprise systems like SAP were designed as **deterministic machines**. Their strength is predictability: every transaction posts the same way, every document follows strict rules. But the world is shifting — demand forecasts, delivery risks, and customer churn are not rules, they are **probabilities**. And this is where AI and ML come in.

This difference — rules vs. probabilities — explains why we cannot just “drop” AI into the ERP core. **Determinism does not tolerate uncertainty.** 

## Is It Worth It? When AI/ML Makes Sense (and When It Doesn’t)

Not every problem deserves an AI or ML solution. Sometimes a clear rule or a standard SAP function solves it faster and cheaper. The question is always: *is the juice worth the squeeze?*

A few ways I think about it:

- **If the process is rule-driven and stable →** keep it in SAP with validations or BRF+. Don’t complicate it.
- **If the outcome depends on probability or patterns →** consider AI/ML outside the core. Forecasts, risks, and recommendations belong here.
- **If the gain is measurable in money or defects →** it is usually worth a pilot. If not, think twice.
- **If training data is poor or rare →** start with clustering, anomalies, or rules; ML can wait.
- **If speed is critical on screen →** keep it simple. Heavy models can run async and feed back later.

**Typical tasks where AI/ML adds value:**

- Forecasting demand, ETA, or workload → *time-series (Prophet, ARIMA, LSTM)*
- Predicting risk (late payment, churn, stockout) → *classification (Logistic, XGBoost)*
- Grouping customers or detecting duplicates → *clustering, embeddings*
- Reading invoices or contracts → *OCR, NLP, GenAI with RAG*
- Summarizing incidents or tickets → *LLMs (GPT-4, Claude, Llama)*
- Optimizing transport or shifts → *solvers (OR-Tools, CPLEX)*

But there is one more point to remember: **AI/ML itself is also a cost.**

Every model must be built, integrated, monitored, retrained, and supported. That lifecycle is not free. The same discipline that applies to SAP projects applies here: *the value must exceed the cost.*

## Where should the data live, and how do we use it?

Every AI/ML story comes back to one thing — data. The question is not just *which model to train*, but *where does the data sit, and how do we keep it usable without drowning in cost or complexity?*

My way of looking at it is simple:

- **Facts stay in SAP.** Master data and transactions remain the system of record. They are deterministic, and that’s their strength.
- **History and patterns live outside.** For training and analysis you need a lakehouse — raw history in cheap storage, curated views for BI and ML. That’s where forecasts and risks are learned.
- **Signals flow in events.** Real-time changes — a sales order created, a delivery posted — should travel through events. Streams scale better than point-to-point integrations.
- **Features need consistency.** What the model sees in training must match what it sees in production. A feature store helps keep that contract.
- **Knowledge for GenAI has its own shape.** Documents, contracts, SOPs don’t fit neatly in tables. They need embeddings and a vector index to be useful in retrieval.

In practice this means: SAP holds the core truth, the lakehouse holds history, Kafka carries the signals, a feature store bridges training and inference, and a vector DB powers retrieval-augmented generation.

The rule of thumb: **move only what is needed, keep it explainable, and always weigh the value of a new dataset against the cost of storing, securing, and governing it.**

## 3-tier extensibility

SAP runs stable, while new AI-driven capabilities connect through interfaces.

SAP itself offers a model for extensions — the 3-tier approach. Let’s see how our AI/ML philosophy fits into this structure.

**What they propose (3 tiers):**

- **Tier A — In-App / Key-User inside S/4**: fields, validations, BRF+, lightweight enhancements.
- **Tier B — ABAP Cloud inside S/4 (embedded)**: “clean” ABAP extensions next to the core, upgrade-safe. Transactional consistiency required, closely coupled extensions.
- **Tier C — Side-by-Side app**: separate app/service (ABAP on BTP or any external runtime) that talks to S/4 via released APIs/events.

> **Guiding idea:** Deterministic stays inside; probabilistic lives outside.

SAP should remain a stable, deterministic system — rules, validations, and short UX checks belong in **Tier A/B**. AI/ML, by nature probabilistic, should live in **Tier C** as side-by-side services that return **results + confidence + reasons** back into S/4.

From this idea follow five principles for how AI/ML should be built around SAP:

**1. Clean Core, Contracted Edge**

Keep S/4 clean and upgrade-safe. All AI/ML logic runs outside, connected through released APIs and business events with clear, versioned contracts.

**2. AI/ML as Products, Not Projects**

Treat every model as a product with an owner, KPIs, and lifecycle. Build on shared rails (FastAPI/Spring, MLflow, vector DBs) so one service can support SAP, CRM, and beyond.

**3. Events First**

Use events (Kafka or SAP Event Mesh) as the backbone for scale and decoupling. Synchronous calls are only for fast UX hints; heavy inference runs asynchronously. Add schema registry, DLQ, and monitoring to stay resilient.

**4. Trust by Design**

Predictions must be transparent. Always return reason codes, model version, and audit trail. Enforce security (Keycloak, mTLS, OPA) and observability (OpenTelemetry, Prometheus, drift checks) from the start.

**5. Portability & Cost Discipline**

Avoid lock-in and hidden platform tax. Use open, containerized components (Python/Java, MLflow, Kafka, Qdrant). Track **unit cost per decision**, minimize data transfer, and prove redeployability across environments.

## Inside vs. Outside: Choosing the Right Place to Build

There is a question every SAP program faces today: *should new functionality live inside the SAP ecosystem, or outside of it?*

Building **inside SAP** has its comfort. ABAP and BTP services keep everything under one vendor, rules and workflows are close to the transactions, and certification comes out of the box. Yet the trade-offs are clear: limited AI/ML libraries, slower change cycles, and the hidden “tax” of data transfer and service subscriptions. Every integration with BTP adds cost, and every extension built there deepens the lock-in.

On the other side, building **outside SAP** has never been easier. Python, Java, Node.js — all come with rich ecosystems of open libraries, world-class ML frameworks, and modern DevOps tooling. With today’s code copilots and AI-assisted development, writing and maintaining independent services is faster than ever. One tool, many systems, same quality. And there is no extra charge for simply moving data around.

When AI or ML logic runs **outside S/4**, we can use a small but proven set of tools that are easy to repeat across projects:

- **Runtime:** lightweight microservices in **Python (FastAPI)** for quick builds or **Java (Spring)** for enterprise-grade delivery.
- **Machine Learning:** core models with **scikit-learn, XGBoost, LightGBM**; time-series forecasting with **Prophet**; deep learning with **PyTorch** or **TensorFlow** when complexity requires it.
- **NLP & GenAI:** modern text handling via **Hugging Face Transformers** (e.g. DistilBERT) and large language models from **OpenAI, Claude**, or self-hosted deployments. For enterprise retrieval, add **RAG patterns** with **LangChain**.
- **Events & Messaging:** **Kafka** as the default event backbone.
- **Security:** enterprise-grade setup with **Keycloak** for identity, **mTLS** for encrypted service-to-service calls, and **OPA** for policy enforcement.
- **Observability:** end-to-end tracing with **OpenTelemetry**, monitoring with **Prometheus/Grafana.**

The pattern is consistent: **deterministic ERP at the core, probabilistic AI at the edge, connected through APIs and events.** This is how we cut cost, accelerate change, and avoid lock-in.

“There is no single blueprint for every enterprise. If you are weighing similar choices, I’d be glad to exchange perspectives.
