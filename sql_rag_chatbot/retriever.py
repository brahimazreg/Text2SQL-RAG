from sql_rag_chatbot.embeddings import embed_documents, embed_query
from sql_rag_chatbot.vector_store import create_index, search
from sql_rag_chatbot.schema_loader import extract_schema


# Build once when the application starts
schema = extract_schema()

schema_texts = [
    f"Table: {table}\nColumns: {', '.join(columns)}"
    for table, columns in schema.items()
]

schema_vectors = embed_documents(schema_texts)
index = create_index(schema_vectors)

def retrieve(question, top_k=3):
    """
    Retrieve relevant schema for a user question
    """
    # Convert user question into vector
    query_vector = embed_query(question)

    # Search FAISS
    results = search(
        index,
        query_vector,
        top_k
    )

    # Convert returned ids into schema texts
    retrieved_schema = [
        schema_texts[i]
        for i in results
    ]

    return retrieved_schema