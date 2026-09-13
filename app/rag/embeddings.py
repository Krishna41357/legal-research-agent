import os
import time
from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv


load_dotenv()

cohere_api_key = os.getenv("COHERE_API_KEY")

if not cohere_api_key:
    raise ValueError("COHERE_API_KEY is not set")

cohere_embed = CohereEmbeddings(
    model="embed-english-v3.0",
    cohere_api_key=cohere_api_key,
)

def create_document_embeddings(documents, batch_size: int = 20, pause_seconds: float = 62):
    """
    Embeds documents in small batches to avoid hitting Cohere's
    trial rate limit (100k tokens/minute).

    Args:
        documents:      List of LangChain Document objects.
        batch_size:     Number of chunks per API call (lower = safer).
        pause_seconds:  Seconds to wait between batches.
    """
    all_embeddings = []

    for i in range(0, len(documents), batch_size):
        batch = documents[i : i + batch_size]
        texts = [doc.page_content for doc in batch]

        print(f"Embedding batch {i // batch_size + 1} / {-(-len(documents) // batch_size)} ({len(texts)} chunks)...")
        batch_embeddings = cohere_embed.embed_documents(texts)
        all_embeddings.extend(batch_embeddings)

        # Pause between batches to respect the rate limit,
        # but skip the wait after the final batch.
        if i + batch_size < len(documents):
            print(f"  Rate-limit pause: waiting {pause_seconds}s...")
            time.sleep(pause_seconds)

    if len(documents) != len(all_embeddings):
        raise ValueError(
            f"Mismatch: {len(documents)} documents but "
            f"{len(all_embeddings)} embeddings"
        )

    return all_embeddings
