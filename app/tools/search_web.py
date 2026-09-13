from langchain_core.tools import tool

@tool
def search_web(query:str):
    """Search the web for relevant legal information based on the given query."""
    print("Searching the web...")
    print(f"Search query: {query}")
    return ["web result1", "web result2", "web result3"]
    