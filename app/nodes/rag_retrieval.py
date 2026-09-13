from state import ResearchState
from rag.retriever import retrieve_relevant_chunks

def rag_retrieve(state:ResearchState):
    query = state["query"]
    result = retrieve_relevant_chunks(
        query,
        top_k = 10
        )
    return {
        "retrieved_chunks":result
    }