from langchain_core.tools import tool


@tool
def search_cases(query:str):
    """Search for relevant legal cases based on the given query."""
    print("Searching for relevant cases...")
    print(f"Search query: {query}")
    return ["case1" , "case2" , "case3" , "case4" , "case5"]
