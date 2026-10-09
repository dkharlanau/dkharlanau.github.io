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

Use the [runtime lock](runtime-lock.json), not the latest branches. The baseline was
reconstructed and checked on 7 October 2026 against all four retained output files.
It is not a record of the original run. Current Composer main adds security fields
and a visual view, so it does not reproduce this pack's exact blueprint and visual
source. Do not change retained hashes to make a newer version pass.

| Product | Pinned commit |
|---|---|
| Signal to Insight | `01193da937f438605169a9cab6b6a440e2b88e1d` |
| Enterprise Architecture Composer | `0a90cc714c4c5653953062c80ae87d4b708f5156` |
| Visual Workbench | `4eb394c430629f3f063f1d5058586e810c09275e` |
| Project Evidence Graph | `80b31b85e0135620ca0ca71115f48b4ea93dd726` |

### Prepare once

Use Python 3.10 or later, Node.js 20 or later, Git, and npm. The observed run used
Python 3.12.14 and Node.js 24.19.0. Other supported runtime versions still need to
pass the same byte comparisons.

From this case directory, choose a new directory outside existing checkouts. These
commands download public source into separate pinned checkouts; they do not change
your working branches. Review each product's license before use.

```sh
export CASE_DIR="$(pwd)"
export TOOLS_DIR="$(mktemp -d)"
python3 -c 'import json; d=json.load(open("runtime-lock.json")); [print(k, v["commit"]) for k,v in d["repositories"].items()]' |
while read -r repo commit; do
  git clone --no-checkout "https://github.com/dkharlanau/$repo.git" "$TOOLS_DIR/$repo" &&
  git -C "$TOOLS_DIR/$repo" checkout --detach "$commit" || exit 1
done

export STI_REPO="$TOOLS_DIR/signal-to-insight"
export EAC_REPO="$TOOLS_DIR/enterprise-architecture-composer"
export VW_REPO="$TOOLS_DIR/visual-workbench"
export PEG_REPO="$TOOLS_DIR/project-evidence-graph"
npm ci --prefix "$VW_REPO" --ignore-scripts --no-audit --no-fund
```

Alternatively, set these four variables to existing clean checkouts at the exact
locked commits. Install Visual Workbench dependencies with its locked `npm ci`
command. The runner rebuilds its ignored `dist/` output from the pinned source, so
an old build cannot silently supply the renderer. The dependency installation is
user-prepared; the receipt does not attest to every installed dependency byte.

### Run and inspect

```sh
CASE_OUTPUT="$(mktemp -d)/reproduction"
PYTHONDONTWRITEBYTECODE=1 python3 "$CASE_DIR/reproduce.py" --output "$CASE_OUTPUT"
```

The runner makes no downloads and never switches branches or updates the pack. It:

1. Validates the retained pack and requires all four clean, pinned checkouts.
2. Rebuilds Visual Workbench with its already installed TypeScript compiler.
3. Validates the research packet with Signal to Insight.
4. Asks Composer to produce the blueprint and native Markdown projection, then
   checks both against the retained bytes before handing the projection onward.
5. Validates and renders that same projection with Visual Workbench, using the
   existing whitespace normalizer for the SVG.
6. Runs Project Evidence Graph analysis and compares all four retained outputs.

Success prints `PASS: four retained outputs match exactly`. The new output
directory contains the outputs, separate command logs, and `receipt.json` with
status, exact repository commits, runtime versions, input/output hashes, and step
exit codes. A failed run keeps its logs and a failed receipt. Existing output
folders are refused, so a retry cannot replace earlier evidence.

A wrong revision, dirty checkout, missing dependency, failed product command, or
byte mismatch stops the run. Read the failure before preparing another output
directory. A receipt with `status: failed` or without all four output matches is
not a passing reproduction.

The receipt proves this pinned reproduction only. It does not establish current
main compatibility, package supply-chain integrity, external adoption, human
approval, or production suitability. Research-to-Composer and visual-to-assurance
remain manually authored demonstration bridges; reconciliation and cutover stay
outside this pack. For individual product commands, see the
[edge ledger](manifest.json) and the pinned source links in the runtime lock.

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
