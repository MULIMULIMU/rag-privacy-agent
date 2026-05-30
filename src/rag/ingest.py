"""
RAG ingestion module: chunk fake_docs, embed chunks, and store them in ChromaDB.
"""
import os
import re
from pathlib import Path
from typing import Dict, List

import chromadb
from chromadb.utils import embedding_functions


def chunk_markdown(content: str, max_chars: int = 800, overlap: int = 100) -> List[str]:
    """
    Split a Markdown document into chunks.

    Prefer paragraph boundaries. If a paragraph is too long, split it by
    character length with overlap.
    """
    paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
    chunks = []
    current = ""

    for para in paragraphs:
        # Hard-split paragraphs that are too long.
        if len(para) > max_chars:
            if current:
                chunks.append(current.strip())
                current = ""
            for i in range(0, len(para), max_chars - overlap):
                chunks.append(para[i:i + max_chars])
        # Accumulate paragraphs until the chunk reaches max_chars.
        elif len(current) + len(para) + 2 <= max_chars:
            current = (current + "\n\n" + para) if current else para
        else:
            chunks.append(current.strip())
            current = para

    if current:
        chunks.append(current.strip())

    return chunks


def build_vector_db(
    docs_dir: str = "data/fake_docs",
    db_path: str = "data/chroma_db",
    collection_name: str = "iot_docs",
    embedding_device: str = "cuda",
) -> chromadb.Collection:
    """
    Scan Markdown files under docs_dir, chunk them, and store them in ChromaDB.
    """
    docs_dir = Path(docs_dir)
    if not docs_dir.exists():
        raise FileNotFoundError(f"Docs directory not found: {docs_dir}")

    # Use GPU for embedding when available.
    embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2",
        device=embedding_device,
    )

    # Initialize persistent ChromaDB storage.
    client = chromadb.PersistentClient(path=db_path)

    # Delete the existing collection so rebuilds are deterministic.
    try:
        client.delete_collection(collection_name)
        print(f"  Deleted existing collection: {collection_name}")
    except Exception:
        pass

    collection = client.create_collection(
        name=collection_name,
        embedding_function=embed_fn,
        metadata={"hnsw:space": "cosine"},
    )

    # Iterate through Markdown files, chunk them, and collect metadata.
    all_chunks: List[str] = []
    all_ids: List[str] = []
    all_metas: List[Dict] = []

    for filepath in sorted(docs_dir.rglob("*.md")):
        if filepath.name.endswith(".bak"):
            continue

        content = filepath.read_text(encoding="utf-8")
        sensitivity = filepath.parent.name  # public / internal / confidential
        chunks = chunk_markdown(content)

        for i, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            all_ids.append(f"{filepath.stem}_chunk_{i}")
            all_metas.append({
                "source": str(filepath.relative_to(docs_dir.parent)),
                "filename": filepath.name,
                "sensitivity": sensitivity,
                "chunk_index": i,
                "total_chunks_in_file": len(chunks),
            })

    # ChromaDB computes embeddings internally using the embedding function.
    if all_chunks:
        collection.add(documents=all_chunks, ids=all_ids, metadatas=all_metas)

    print(f"\nIndexed {len(all_chunks)} chunks from {len(list(docs_dir.rglob('*.md')))} files")
    print(f"   DB path: {db_path}")
    print(f"   Collection: {collection_name}")

    return collection


def get_collection(
    db_path: str = "data/chroma_db",
    collection_name: str = "iot_docs",
    embedding_device: str = "cpu",
) -> chromadb.Collection:
    """Return an existing ChromaDB collection without rebuilding it."""
    embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2",
        device=embedding_device,
        local_files_only=True,
    )
    client = chromadb.PersistentClient(path=db_path)
    return client.get_collection(name=collection_name, embedding_function=embed_fn)
