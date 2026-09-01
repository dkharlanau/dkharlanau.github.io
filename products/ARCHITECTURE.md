# Enterprise Transformation Toolkit architecture

This portfolio is a set of bounded products, not one distributed application and not a requirement to adopt the whole chain.

The primary rule is simple:

> Start from one problem. Use the product that owns that problem. Connect another product only when the next boundary becomes useful.

## Why this architecture exists

Enterprise transformation work fragments because the same fact is copied into process diagrams, mapping workbooks, interface documents, cutover trackers, reconciliation scripts and status decks. A portfolio of small tools only helps if it avoids recreating the same duplication in code.

The architecture therefore distinguishes three things:

1. **authoritative contracts** — maintained intent owned by one product;
2. **evidence-producing consumers** — execute or inspect contracts and retain observations;
3. **derived projections/views** — reproducible representations that must not quietly become a second source of truth.

## Start from the problem

| I need to… | Start with | It owns |
| --- | --- | --- |
| compose architecture options from explicit context and constraints | Enterprise Architecture Composer | candidate composition, decision trace, constraint evaluation and alternative comparison |
| describe how work should flow | Process as Code | process steps, transitions, roles, gates and process semantics |
| make a deterministic business decision | Decision Tables as Code | facts, rules, precedence and decision trace semantics |
| document how systems exchange something | Interface as Code | trigger, transport, ownership, retry/recovery, monitoring and operational interface semantics |
| define how source data becomes target data | Mapping as Code | field/value transformation intent and mapping governance |
| prove source/target or stage state | Reconciliation as Code | comparison controls and retained reconciliation evidence |
| coordinate a migration/cutover | Cutover Graph | cutover tasks, dependencies, timing, readiness and checkpoints |
| connect claims to supporting artifacts | Project Evidence Graph | assurance claims, evidence relationships and freshness |
| turn structured artifacts or a directly authored semantic visual model into business visuals | Visual Workbench | visual semantic model, views and rendering; imported domain semantics remain upstream |
| expose safe SAP operational capabilities | SAP Agentic Operations | bounded operational capability contracts and policy-gated execution evidence |
| turn selected external material into retained understanding | Signal to Insight | source model, Knowledge Delta, evidence boundaries and learning state |
| resolve machine/agent interfaces exposed by a public site | Agent-Ready Web Profile Resolver | discovery/resolution evidence and intent-specific interface selection |
| publish a portable professional profile | AI CV Builder | profile input and deterministic HTML, JSON and JSON-LD outputs |
| cite or reuse a public structured evidence collection | Dkharlanau Datasets | dataset records, schemas, releases and citation context |

A user does **not** need Transformation Graph, Enterprise Change Graph or Data Relationship Map merely because they use Mapping as Code. Those graph products are useful when the graph itself answers a concrete analysis question.

## Ownership matrix

| Product | Portfolio role | Maintained truth | May consume | Must not become |
| --- | --- | --- | --- | --- |
| Enterprise Architecture Composer | architecture composer | architecture candidates, constraints and decision traces | explicit business and technical context | universal enterprise architecture repository |
| Process as Code | authoritative contract | process intent | decision/interface references | project-status database |
| Decision Tables as Code | authoritative contract | deterministic business rules | explicit facts | process engine |
| Interface as Code | authoritative contract | interface operational contract | mapping refs, schemas | mapping authoring system |
| Mapping as Code | authoritative contract | transformation intent | source/target metadata, interface binding | reconciliation result store |
| Reconciliation as Code | evidence producer | reconciliation control + run evidence | mapping artifacts, datasets, SQL extracts | duplicate mapping authoring system |
| Cutover Graph | evidence-aware execution model | cutover plan/checkpoint state | reconciliation evidence and other evidence refs | general project manager |
| Project Evidence Graph | assurance graph | claims/evidence relationships | cutover and external evidence artifacts | owner of upstream domain semantics |
| Transformation Graph | derived analysis | graph-specific annotations only | mapping/interface projections | second mapping/interface source |
| Enterprise Change Graph | derived analysis | change-analysis annotations only | process/data/interface/change projections | universal enterprise CMDB |
| Data Relationship Map | bounded lineage analysis | record/identity lineage when explicitly authored | data extracts and mappings | universal data catalog |
| Visual Workbench | visual modeling layer | visual semantic model, view/render configuration | structured artifacts from other products | owner of imported Process/Mapping/Interface semantics |
| SAP Agentic Operations | adjacent execution product | bounded SAP capability/policy contract | operational observations | unrestricted autonomous SAP agent |
| Signal to Insight | adjacent knowledge product | evidence-backed learning model | selected external sources | generic summarizer/read-later store |
| ARWP Resolver | adjacent interoperability product | resolver observation/selection evidence | public web discovery surfaces | another mandatory publisher manifest |
| AI CV Builder | adjacent profile product | profile input and deterministic public outputs | explicit profile data | inferred credential or employment authority |
| Dkharlanau Datasets | adjacent evidence product | dataset records, schemas and release metadata | public, citable source material | proof that every downstream claim is verified |

## Reader map and Jekyll projection

`products/manifest.json` is the sole editable source for the 17-project inventory, its
three reader tracks, project summaries, URLs, ownership, and claim boundaries. The
human-readable Machine route needs the same data through Jekyll, so a deterministic
projection is generated at `_data/public_portfolio.yml`.

```sh
python3 scripts/generate_public_portfolio.py
python3 scripts/generate_public_portfolio.py --check
```

Do not edit the `_data` projection by hand. The generator records the canonical
manifest schema and SHA-256 digest; tests also compare every projected project and
track with the manifest. `/ai/public-portfolio.json` renders this projection for
machine clients, while `/machine/portfolio/` is the reader-facing map. Classification
is navigation, not evidence of interoperability, adoption, or production readiness.

The runnable synthetic reference case is maintained under
`products/reference-cases/enterprise-change-evidence-pack/`. Its `manifest.json` and
`expected-artifacts.json` are the canonical edge and digest ledgers. The public case
page uses a deterministic Jekyll projection:

```sh
python3 products/reference-cases/enterprise-change-evidence-pack/validate.py
python3 scripts/generate_portfolio_reference_case.py
python3 scripts/generate_portfolio_reference_case.py --check
```

Do not edit `_data/portfolio_reference_case.yml` by hand. Each edge in the case keeps
its own `implemented`, `demonstration-only`, or `documented` status; the presence of
several products in one pack does not create an end-to-end runtime claim.

## Reference before copy

When one maintained product needs another product's truth, prefer a **reference with stable identity and provenance** over copying the business rule.

Current canonical example:

```text
Mapping as Code artifact
        │ field id + SHA-256
        ▼
Reconciliation as Code map_ref
        │ deterministic run
        ▼
RAC evidence
        │ eac:// logical run ref + document/config hash
        ▼
Cutover checkpoint
```

The Mapping artifact remains the transformation source of truth. RAC owns the reconciliation control and the evidence produced from it. Cutover owns the decision about whether that evidence satisfies a checkpoint.

The implemented `eac://` convention is a logical producer-owned artifact reference, not a network URL or trust assertion. Its syntax, ownership, evidence-binding rules and non-goals are defined in [Portfolio interoperability contract](INTEROPERABILITY.md). A valid reference identifies an artifact; positive assurance still requires an explicit verified binding.

## Projection rule

A derived artifact is safe when all of the following are true:

- its upstream source is explicit;
- it can be regenerated deterministically;
- provenance/version/hash is retained where the target contract supports it;
- downstream edits are either forbidden or clearly become a new independent artifact;
- the projection never silently claims semantics its source did not contain.

Examples:

- Mapping → Transformation Graph: derived topology, not a second mapping workbook;
- Mapping → Visual Workbench: a derived visual model/view, not mapping truth. When a Visual Workbench model is authored directly rather than projected from another product, that visual model is its own maintained source for the visual;
- Mapping → Enterprise Change Graph: impact seeds/projection, not a universal change model;
- Cutover → Project Evidence Graph: imported evidence/change nodes, while Cutover still owns cutover semantics.

## Detached snapshots

Sometimes a self-contained artifact is useful for an archive, release bundle, fixture or handoff. A copied projection is allowed when it is explicitly marked as a **detached snapshot**.

A detached snapshot has a different lifecycle:

- it represents one point in time;
- it should retain provenance to the source that created it;
- modifying it later creates an independent source and must not be mistaken for automatic synchronization.

For example, Mapping as Code can generate a self-contained RAC spec with inline lookup values, but linked `map_ref` mode is the normal maintained integration.

## No universal graph

The portfolio deliberately does not introduce one canonical enterprise mega-schema.

A process graph, transformation graph, cutover graph and assurance graph answer different questions. They may share stable external references, but collapsing them into one writable graph would recreate the coupling these products are meant to avoid.

Cross-product integration should therefore use:

- stable product-native IDs;
- explicit external references;
- version/hash provenance;
- small adapters at boundaries;
- deterministic projections where appropriate.

These references remain intentionally bounded. The portfolio does not currently define a universal `eac://` dereference service or central artifact registry; producer/consumer adapters resolve only the contracts they actually support.

## One golden scenario

The reference portfolio scenario is a synthetic customer migration:

1. **Process as Code** describes the migration/review flow and where a business decision is required.
2. **Decision Tables as Code** expresses an explicit deterministic eligibility/routing rule.
3. **Interface as Code** describes the customer replication interface and operational recovery semantics.
4. **Mapping as Code** owns legacy-customer → target-business-partner transformation intent.
5. **Reconciliation as Code** references the Mapping artifact and proves target state with retained evidence.
6. **Cutover Graph** consumes verified reconciliation evidence at a checkpoint before opening dependent tasks.
7. **Project Evidence Graph** can connect the change/control/checkpoint artifacts into an assurance view.
8. **Visual Workbench** can render selected artifacts for a human review without becoming their source.

Not every step must live in one demo repository. The contract between steps is the product: stable IDs, provenance, deterministic evidence and explicit ownership.

The currently executable assurance slice is tested across current repository heads: Mapping as Code → Reconciliation as Code → Cutover Graph → Project Evidence Graph. The test includes both the verified path and the same external checkpoint without its verification registry, which must remain unverified.

## Maturity is not architecture

A clean architecture does not imply external validation. Repository maturity is tracked separately:

- `experimental` — useful hypothesis; contracts or evidence still moving;
- `usable` — clean run, representative example and CI;
- `release-ready` — versioned distribution and compatibility/release discipline;
- `validated` — independent/external usage evidence exists.

Pages, commit count and generated documentation do not by themselves move a product to `validated`.

## Rules for adding another repository

A new repository needs all three:

1. an independent user problem;
2. a semantic owner that is not already clear in an existing product;
3. evidence that an adapter/module/view inside the current portfolio is insufficient.

If the idea is only another representation of existing truth, it should normally be a projection, adapter or view—not a new product.
