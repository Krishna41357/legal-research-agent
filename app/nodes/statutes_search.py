from state import ResearchState
from tools.search_statute import search_statutes

def statue_search(state:ResearchState):
    query = state["query"]
    result = search_statutes.invoke(query)
    return {
        "statutes":result
    }