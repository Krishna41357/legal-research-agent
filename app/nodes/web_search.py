from state import ResearchState
from tools.search_web import search_web

def web_search(state:ResearchState):
    query = state["query"]
    result = search_web.invoke(query)
    return {
        "web_results":result
    }