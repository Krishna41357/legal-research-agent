from state import ResearchState
from tools.search_cases import search_cases

def case_search(state: ResearchState):
    query = state["query"]
    result = search_cases.invoke(query)
    return {
        "cases":result
    }