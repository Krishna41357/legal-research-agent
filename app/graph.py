from langgraph.graph import StateGraph, START, END
from state import ResearchState
from nodes.query_analyzer import query_analyzer
from nodes.research_planner import research_planner
from nodes.case_search import case_search
from nodes.statutes_search import statue_search   # function name has typo in source file
from nodes.web_search import web_search
from nodes.document_search import document_search
from nodes.rag_retrieval import rag_retrieve

builder = StateGraph(ResearchState)

# Register all nodes
builder.add_node("query_analyzer", query_analyzer)
builder.add_node("research_planner", research_planner)
builder.add_node("case_search", case_search)
builder.add_node("statutes_search", statue_search)  # node label vs function name
builder.add_node("web_search", web_search)
builder.add_node("document_search", document_search)
builder.add_node("rag_retriever" , rag_retrieve)
# Wire the pipeline
builder.add_edge(START, "query_analyzer")
builder.add_edge("query_analyzer", "research_planner")
builder.add_edge("research_planner", "case_search")
builder.add_edge("case_search", "statutes_search")
builder.add_edge("statutes_search", "web_search")
builder.add_edge("web_search", "document_search")
builder.add_edge("document_search", "rag_retriever")
builder.add_edge("rag_retriever", END)

graph = builder.compile()
