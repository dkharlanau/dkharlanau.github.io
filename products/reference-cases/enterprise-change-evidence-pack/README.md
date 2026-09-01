# Enterprise change evidence pack

This bounded reference case shows how one public research-context packet can remain traceable through a synthetic architecture decision, a deterministic visual projection, and a Project Evidence Graph assurance view without turning any link into production proof.

The scenario is client-free. The business context, decision input, graph, and retained outputs are synthetic. The Signal to Insight packet is an unchanged detached copy of an existing public, reviewed reference packet; it contains source attribution and no raw source content.

## What the chain establishes

| Edge | Status in this case | What is actually verified | Boundary |
|---|---|---|---|
| Signal to Insight research context → Enterprise Architecture Composer decision | `demonstration-only` | The producer packet validates, selected claim IDs exist, and the synthetic decision-basis sidecar retains the research trust boundary. | Composer has no runtime consumer for this packet. The context and simulated decision input were authored manually and grant no approval. |
| Enterprise Architecture Composer decision → Visual Workbench render | `implemented` | Composer generates a deterministic blueprint and native coordinate-free Visual Workbench Markdown; Visual Workbench validates it and renders the executive SVG. | Composer owns architecture semantics and the simulated decision record. Visual Workbench owns layout and presentation only. |
| Visual Workbench render → Project Evidence Graph assurance | `demonstration-only` | The graph binds the retained SVG by exact SHA-256 and Project Evidence Graph validates the synthetic graph. | No Visual Workbench-to-Project Evidence importer exists. The implemented adapter runs in the opposite direction, from Project Evidence Graph to Visual Workbench. |
| Synthetic evidence graph → Project Evidence Graph analysis | `implemented` | Project Evidence Graph reports a structurally valid graph with complete test/evidence reachability for the narrow artifact-reconstruction requirement. | Coverage describes this reference graph only. It is not evidence of architecture fitness, implementation, cutover readiness, or a production outcome. |

The machine-readable edge ledger, verification commands, and boundaries are in [`manifest.json`](manifest.json). Exact file hashes and expected structural assertions are in [`expected-artifacts.json`](expected-artifacts.json).

## Read the retained chain

1. [`fixtures/research-context.json`](fixtures/research-context.json) is a detached Signal to Insight `external_research_context` packet. Its embedded canonical payload digest remains valid.
2. [`fixtures/decision-basis.json`](fixtures/decision-basis.json) records which claims were used as synthetic review cautions. It explicitly declares that no adapter, automatic adoption, authorization, or completed human review exists.
3. [`fixtures/architecture-context.json`](fixtures/architecture-context.json) simulates an order-to-cash architecture context and an accepted synchronous-API decision input. The rationale labels the decision synthetic and not a production approval.
4. [`artifacts/architecture.blueprint.json`](artifacts/architecture.blueprint.json) is the deterministic Composer result. It retains the decision record and effective `pattern.sync-api` choice.
5. [`artifacts/architecture.visual.txt`](artifacts/architecture.visual.txt) is Composer's coordinate-free Markdown projection, retained with a static-safe extension so GitHub Pages serves the exact bytes instead of rendering it as a standalone page. [`artifacts/architecture.executive.svg`](artifacts/architecture.executive.svg) is the deterministic Visual Workbench render.
6. [`fixtures/project-evidence.json`](fixtures/project-evidence.json) binds the detached research packet, decision basis, blueprint, visual source, and render by case-owned logical identities and exact hashes.
7. [`artifacts/project-evidence.analysis.json`](artifacts/project-evidence.analysis.json) is the deterministic structural analysis. Its `1.0` coverage values apply only to the pack's reconstructability requirement.

## Validate locally

The local validator uses only the Python standard library. It checks file hashes and sizes, the Signal to Insight canonical payload digest, English/public hygiene, case-owned `eac://` syntax, every edge status and boundary, the Composer decision record, the expected visual labels and views, graph integrity, and the retained Project Evidence analysis.

Run from this directory:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 validate.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_validate.py
```

The validator does not call other repositories. This keeps the committed pack check deterministic and makes product-runtime reproduction a separate, explicit step.

## Reproduce the implemented product steps

Set these variables to checked-out repositories whose current contracts support the documented commands:

```sh
export STI_REPO=/path/to/signal-to-insight
export EAC_REPO=/path/to/enterprise-architecture-composer
export VW_REPO=/path/to/visual-workbench
export PEG_REPO=/path/to/project-evidence-graph
export CASE_DIR="$(pwd)"
```

Create a temporary output directory and validate the producer packet:

```sh
CASE_OUTPUT="$(mktemp -d)"
python3 "$STI_REPO/sti.py" handoff validate "$CASE_DIR/fixtures/research-context.json"
```

Reproduce the Composer artifacts:

```sh
node "$EAC_REPO/bin/eac.mjs" compose "$CASE_DIR/fixtures/architecture-context.json" \
  > "$CASE_OUTPUT/architecture.blueprint.json"

node "$EAC_REPO/bin/eac.mjs" visual "$CASE_DIR/fixtures/architecture-context.json" \
  --markdown \
  --output "$CASE_OUTPUT/architecture.visual.md"

cmp artifacts/architecture.blueprint.json "$CASE_OUTPUT/architecture.blueprint.json"
cmp artifacts/architecture.visual.txt "$CASE_OUTPUT/architecture.visual.md"
```

Build Visual Workbench according to its repository instructions if `dist/cli.js` is not present, then validate and render the native projection:

```sh
node "$VW_REPO/dist/cli.js" validate "$CASE_OUTPUT/architecture.visual.md"
node "$VW_REPO/dist/cli.js" render "$CASE_OUTPUT/architecture.visual.md" \
  --view executive \
  --output "$CASE_OUTPUT/architecture.executive.svg"
python3 "$CASE_DIR/normalize_render.py" "$CASE_OUTPUT/architecture.executive.svg"

cmp artifacts/architecture.executive.svg "$CASE_OUTPUT/architecture.executive.svg"
```

Reproduce the Project Evidence structural analysis:

```sh
python3 "$PEG_REPO/evidence_graph.py" "$CASE_DIR/fixtures/project-evidence.json" analyze \
  > "$CASE_OUTPUT/project-evidence.analysis.json"

cmp artifacts/project-evidence.analysis.json \
  "$CASE_OUTPUT/project-evidence.analysis.json"
```

Finish by running `python3 "$CASE_DIR/validate.py"` again. A byte mismatch should trigger review rather than an automatic metadata update.

## Logical identity and trust

The graph uses references such as:

```text
eac://dkharlanau/dkharlanau.github.io/reference-case/enterprise-change-evidence-pack/executive-render?version=1.0.0
```

These identities are owned by this detached reference-case pack. They do not assign new artifact kinds to Signal to Insight, Composer, Visual Workbench, or Project Evidence Graph. Producer-native IDs such as `sti:enterprise-agents-production-substrate:research-evidence-handoff:v1` and `decision.sales-order-request-durability` remain in the retained metadata.

An `eac://` value is identity only. It is not a URL, resolver request, signature, authorization, or proof that the referenced file is trustworthy. The Project Evidence graph therefore pairs each case identity with an exact local document digest and an explicit non-production boundary.

## Optional reconciliation and cutover boundary

Reconciliation as Code and Cutover Graph are intentionally outside the executable pack. No source/target data, reconciliation run, external-evidence registry, cutover task, checkpoint, or go/no-go decision is included.

The portfolio documents a stronger optional path:

```text
Reconciliation as Code run evidence
  → verified Cutover Graph external-evidence binding
  → Cutover artifact index
  → Project Evidence Graph import
```

Use the [Cutover artifact-index contract](https://github.com/dkharlanau/cutover-graph/blob/main/docs/ARTIFACT-INDEX.md) when that evidence exists. A reconciliation `eac://` reference without the verified evidence document and registry remains a reference, not positive evidence. An unverified checkpoint must remain an assurance gap.

## Limits

- The case does not prove an end-to-end runtime integration across all four main products.
- The research-to-Composer and visual-to-Project-Evidence edges are explicit demonstrations, not adapters.
- The simulated Composer decision is not human approval and is not suitable for a real landscape.
- Matching hashes prove byte identity for retained artifacts; they do not establish signer identity, authorization, correctness, or business acceptance.
- The SVG explains one bounded architecture view. It is not architecture truth and does not close Composer findings.
- The Project Evidence analysis validates a synthetic graph. It does not establish production readiness or external adoption.
