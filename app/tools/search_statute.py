from langchain_core.tools import tool


@tool
def search_statutes(query: str):
    """Search for relevant statutes and legal provisions."""

    print("Searching for relevant statutes...")
    print(f"Search query: {query}")

    return [
        "statute1",
        "statute2",
        "statute3"
    ]