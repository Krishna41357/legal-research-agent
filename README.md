# Legal Research Agent

An agentic AI system that takes a natural-language legal query, analyzes it, generates a prioritized research plan, and searches across multiple sources to gather relevant legal information.

> **Status:** Active development. Core pipeline is functional. Several nodes are currently stubs and real integrations are in progress.

---

## What It Does

You ask a legal question in plain English. The agent:

1. **Analyzes** the query to identify jurisdiction, legal domain, and the core legal issue
2. **Plans** a prioritized list of research steps tailored to that issue
3. **Searches** across cases, statutes, documents, the web, and an internal vector knowledge base
4. **Returns** a structured state with all gathered results

---

## Architecture

The system is built as a **stateful LangGraph pipeline**. Each stage is an independent node that reads from and writes to a shared `ResearchState`.

```
START
  → query_analyzer       # LLM extracts jurisdiction, domain, issue
  → research_planner     # LLM generates prioritized research steps
  → case_search          # Searches for relevant case law
  → statutes_search      # Searches for applicable statutes
  → web_search           # Searches the web for legal information
  → document_search      # Searches uploaded legal documents
  → rag_retriever        # Semantic search over embedded legal chunks (pgvector)
  → END
```

### State Schema

```python
class ResearchState(TypedDict):
    query: str
    jurisdiction: str
    legal_domain: str
    legal_issue: str
    research_plan: list[dict]   # [{step, priority}]
    cases: list[dict]
    statutes: list[dict]
    documents: list[dict]
    web_results: list[dict]
    retrieved_chunks: list[dict]
```

---

## What Is Actually Built

### Fully Implemented

| Component | Details |
|---|---|
| **Query Analyzer** | Uses Groq LLM with structured output to extract `jurisdiction`, `legal_domain`, `legal_issue` from any query |
| **Research Planner** | Uses Groq LLM to generate 4-7 prioritized, actionable research steps |
| **RAG Pipeline** | PDF parsing -> text cleaning -> chunking -> Cohere embedding -> pgvector storage |
| **Vector Store** | PostgreSQL + pgvector with cosine similarity search (`<=>` operator) |
| **Embeddings** | Cohere `embed-english-v3.0` (1024-dim), with rate-limit-aware batched ingestion |
| **RAG Retriever Node** | Queries vector store using embedded query, returns top-k semantically similar chunks |
| **LangGraph Graph** | Full pipeline compiled and runnable end-to-end |
| **DB Schema** | `legal_chunks` table with `VECTOR(1024)` embedding column |

### Stub / In Progress

| Component | Current State |
|---|---|
| **Case Search** | Returns hardcoded placeholder data — real legal database integration pending |
| **Statute Search** | Returns hardcoded placeholder data — real integration pending |
| **Web Search** | Returns hardcoded placeholder data — real web search API pending |
| **Document Search** | Returns hardcoded placeholder data — real integration pending |
| **FastAPI Layer** | Not yet built — currently runs via `main.py` script |
| **Legal Memo Generation** | Not yet built — planned as a final synthesis node |
| **Docker Setup** | Not yet configured |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Agent Orchestration | LangGraph |
| LLM | Groq (`openai/gpt-oss-120b`) via LangChain-Groq |
| Embeddings | Cohere `embed-english-v3.0` |
| Vector Store | PostgreSQL + pgvector |
| DB Driver | psycopg3 |
| PDF Parsing | PyMuPDF |
| Data Validation | Pydantic v2 |
| Environment | Python 3.11+, Conda |

---

## Project Structure

```
legal-research-agent/
├── app/
│   ├── main.py                  # Entry point
│   ├── graph.py                 # LangGraph pipeline definition
│   ├── state.py                 # ResearchState TypedDict
│   ├── schemas.py               # Pydantic schemas for LLM structured output
│   │
│   ├── nodes/                   # One file per graph node
│   │   ├── query_analyzer.py
│   │   ├── research_planner.py
│   │   ├── case_search.py
│   │   ├── statutes_search.py
│   │   ├── web_search.py
│   │   ├── document_search.py
│   │   └── rag_retrieval.py
│   │
│   ├── rag/                     # RAG pipeline
│   │   ├── embeddings.py        # Cohere embedding with rate-limit handling
│   │   ├── pdf_parser.py        # PDF to text
│   │   ├── text_cleaner.py      # Text preprocessing
│   │   ├── chunker.py           # Text chunking
│   │   ├── document_builder.py  # LangChain Document assembly
│   │   └── retriever.py        # Query embedding + vector search
│   │
│   ├── db/
│   │   ├── connection.py        # psycopg3 connection
│   │   ├── vector_store.py      # store_documents + search_similar_chunks
│   │   └── migrations/
│   │       └── 001_create_legal_chunks.sql
│   │
│   └── tools/                   # LangChain @tool definitions
│       ├── search_cases.py
│       ├── search_statute.py
│       ├── search_web.py
│       └── search_document.py
│
├── requirements.txt
└── .gitignore
```

---

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL with the `pgvector` extension installed
- A Groq API key
- A Cohere API key

### 1. Clone and Set Up Environment

```bash
git clone https://github.com/Krishna41357/legal-research-agent.git
cd legal-research-agent

conda create -n legal-agent python=3.11
conda activate legal-agent
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/your_db
GROQ_API_KEY=your_groq_api_key
COHERE_API_KEY=your_cohere_api_key
```

### 3. Set Up the Database

```bash
psql -U your_user -d your_db -f app/db/migrations/001_create_legal_chunks.sql
```

### 4. Run

```bash
# From the project root (PowerShell)
$env:PYTHONPATH = ".\app"
python app/main.py
```

---

## Planned Features

- [ ] Real case law search integration (e.g., Indian Kanoon API)
- [ ] Real statute search integration
- [ ] Web search via Tavily or SerpAPI
- [ ] Legal memo generation node (final synthesis with citations)
- [ ] FastAPI REST API layer
- [ ] Docker + docker-compose setup
- [ ] Memory across research sessions
- [ ] Replanning and failure recovery
