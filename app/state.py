from typing import TypedDict

class ResearchState(TypedDict):
    query : str
    jurisdiction : str
    legal_domain: str
    legal_issue: str
    research_plan: list[dict]
    cases: list[dict]
    statutes:list[dict]
    documents:list[dict]
    web_results:list[dict]
    retrieved_chunks:list[dict]