from state import ResearchState

from schemas import QueryAnalysis
from langchain_core.messages import SystemMessage , HumanMessage
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature = 0
)

structured_llm = llm.with_structured_output(QueryAnalysis, method="json_mode")


def query_analyzer(state: ResearchState):
    query = state["query"]
    print("Analyzing legal query......")
    result = structured_llm.invoke(
        [
            SystemMessage(
                content = (
                    "Role :\n"
                    "You are a legal research assistant specializing in Indian law. "
                    
                    "Task:\n"
                    "Analyze the user's legal question and identify:\n"
                    "- jurisdiction\n"
                    "- legal domain\n"
                    "- primary legal issue\n\n"

                    "Rules:\n"
                    "- Identify the jurisdiction from the query when possible.\n"
                    "- Identify the most relevant legal domain.\n"
                    "- Summarize the central legal issue concisely.\n"
                    "- Do not answer the legal question.\n"
                    "- Do not provide legal advice.\n\n"

                    "Output Requirement:\n"
                    "Respond ONLY with a JSON object containing exactly these keys:\n"
                    "\"jurisdiction\", \"legal_domain\", and \"legal_issue\"."
                    "Return only the requested structured fields.\n"
                    "Do not include explanations, reasoning, or additional fields."
                )
            ),
            HumanMessage(
                content = query
            )
        ]
    )
    return {
        "jurisdiction": result.jurisdiction,
        "legal_domain": result.legal_domain,
        "legal_issue": result.legal_issue
    }