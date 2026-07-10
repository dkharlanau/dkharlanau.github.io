from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


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
