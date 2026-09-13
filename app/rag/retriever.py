from rag.embeddings import cohere_embed
from db.vector_store import search_similar_chunks



def retrieve_relevant_chunks(query: str , top_k : int = 5):
    query_embedding = cohere_embed.embed_query(query)
    results = search_similar_chunks(
        query_embedding,
        top_k=top_k
    )
    structured_results = []
    for content , metadata , similarity in results:
        structured_results.append({
            "content":content,
            "metadata":metadata,
            "similarity": similarity
        })
    return structured_results