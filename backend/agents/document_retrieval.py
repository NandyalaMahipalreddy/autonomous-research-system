from pypdf import PdfReader

from backend.rag.chunker import chunk_text

from backend.rag.qdrant_store import (
    store_chunks,
    retrieve_chunks
)


def document_retrieval_agent(state):

    file_path = state.get("document_path")

    if not file_path:
        print("No PDF uploaded")
        return state

    try:

        print(f"PDF Path: {file_path}")

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        print("PDF Length:", len(text))

        if not text.strip():

            state["findings"] = [
                "PDF contains no extractable text."
            ]

            return state

        chunks = chunk_text(text)

        print("Chunks Created:", len(chunks))

        store_chunks(chunks)

        query = state["query"]

        retrieved_docs = retrieve_chunks(query)

        print("\n===== RETRIEVED PDF CHUNKS =====")

        for i, doc in enumerate(retrieved_docs):

            print(f"\nChunk {i+1}:\n")

            print(doc[:300])

        print("\n===============================\n")

        print(
            "Retrieved Docs:",
            len(retrieved_docs)
        )

        state["findings"] = retrieved_docs

        return state

    except Exception as e:

        print("PDF ERROR:", e)

        state["findings"] = [
            f"PDF Error: {str(e)}"
        ]

        return state