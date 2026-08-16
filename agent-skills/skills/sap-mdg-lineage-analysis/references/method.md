# Method

Use the path `Object → Grain → Provenance → CR/Staging → Rules → Workflow → Audit → Activation → Replication → Mapping → Target → Consumer Proof`.

At every boundary, keep five things together: stable identity, expected state, observed state, timestamp/context, and evidence. Stop at the first boundary where expected and observed diverge. Later failures may be consequences rather than causes.

Treat MDG lineage as governance/runtime lineage. If the question concerns SQL/data-flow transformations, analytics assets, or catalog-wide upstream/downstream dependencies outside MDG, hand off to enterprise metadata-lineage analysis instead of stretching MDG beyond its evidence boundary.
