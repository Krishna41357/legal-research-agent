from langchain_core.tools import tool

@tool
def search_document(query:str):
    """Search for relevant legal documents based on the given query."""
    print("Searching for relevant documents...")
    print(f"Search query: {query}")
    return ["document1" , "document2" , "document3"]

    