import uuid

from qdrant_client import QdrantClient

from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct
)

from sentence_transformers import (
    SentenceTransformer
)

# ---------------------------
# Qdrant Connection
# ---------------------------

client = QdrantClient(
    host="localhost",
    port=6333
)

# ---------------------------
# Embedding Model
# ---------------------------

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# ---------------------------
# Collection Creation
# ---------------------------

def create_collection():

    collections = client.get_collections()

    collection_names = [

        collection.name

        for collection
        in collections.collections

    ]

    if "research_docs" not in collection_names:

        client.create_collection(

            collection_name="research_docs",

            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )

        )

        print(
            "Qdrant Collection Created"
        )

# ---------------------------
# Store Chunks
# ---------------------------

def store_chunks(chunks):

    create_collection()

    points = []

    for idx, chunk in enumerate(chunks):

        vector = model.encode(
            chunk
        ).tolist()

        points.append(

            PointStruct(

                id=str(
                    uuid.uuid4()
                ),

                vector=vector,

                payload={

                    "text": chunk,

                    "chunk_id": idx

                }

            )

        )

    client.upsert(

        collection_name="research_docs",

        points=points

    )

    print(
        f"{len(chunks)} Chunks Stored"
    )

# ---------------------------
# Retrieve Chunks
# ---------------------------

def retrieve_chunks(
    query,
    limit=3
):

    create_collection()

    query_vector = model.encode(
        query
    ).tolist()

    results = client.search(

        collection_name="research_docs",

        query_vector=query_vector,

        limit=limit

    )

    retrieved_texts = []

    for result in results:

        retrieved_texts.append(

            result.payload["text"]

        )

    return retrieved_texts

# ---------------------------
# Auto Create Collection
# ---------------------------

create_collection()