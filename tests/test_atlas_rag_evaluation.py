from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REPORT = REPO_ROOT / "docs" / "atlas" / "ATLAS_SIGNAL_RAG_EVALUATION.md"
WORKFLOW = REPO_ROOT / "docs" / "atlas" / "SIGNAL_DRIVEN_ATLAS_UPDATES.md"


def test_rag_evaluation_report_exists_and_recommends_no_rag_yet():
    content = REPORT.read_text(encoding="utf-8")
    assert "Recommendation: **no RAG/vector search yet**" in content
    assert "Status: `no_rag_yet`" in content
    assert "Issue #51" in content
    assert "does not require implementing it" in content


def test_rag_evaluation_answers_required_questions():
    content = REPORT.read_text(encoding="utf-8")
    for token in [
        "What query types fail",
        "Failure Analysis",
        "RAG V2 Trigger Conditions",
        "Minimal V2 Constraints If Needed Later",
        "corpus: public Atlas Markdown pages only",
        "validate freshness against the current Atlas manifest",
        "fail if private-path patterns appear",
    ]:
        assert token in content


def test_rag_evaluation_prefers_metadata_before_vectors():
    content = REPORT.read_text(encoding="utf-8")
    for token in [
        "Improve metadata first",
        "tags",
        "sap_area",
        "business_process",
        "related",
        "track matcher misses",
    ]:
        assert token in content


def test_workflow_links_rag_evaluation():
    content = WORKFLOW.read_text(encoding="utf-8")
    assert "docs/atlas/ATLAS_SIGNAL_RAG_EVALUATION.md" in content


def test_no_vector_or_embedding_dependencies_added():
    dependency_files = [
        REPO_ROOT / "Gemfile",
        REPO_ROOT / "requirements.txt",
        REPO_ROOT / "package.json",
    ]
    forbidden = [
        "faiss",
        "chromadb",
        "pinecone",
        "weaviate",
        "qdrant",
        "sentence-transformers",
        "openai",
        "embeddings",
    ]
    for path in dependency_files:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8").lower()
        for token in forbidden:
            assert token not in text, f"{path} unexpectedly references {token}"
