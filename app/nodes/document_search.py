from state import ResearchState
from tools.search_document import search_document

def document_search(state:ResearchState):
    query = state["query"]
    result = search_document.invoke(query)
    return {
        "documents":result
    }