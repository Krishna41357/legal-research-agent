from embeddings import cohere_embed
from db.vector_store import search_similar_chunks


query = "Can an employee be terminated for misconduct without notice?"

query_embedding = cohere_embed.embed_query(query)

results = search_similar_chunks(query_embedding, top_k=5)

for content, metadata, similarity in results:
    print("\n--- RESULT ---")
    print("Similarity:", similarity)
    print("Metadata:", metadata)
    print("Content:", content[:500])