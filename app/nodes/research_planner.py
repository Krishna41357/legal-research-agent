from state import ResearchState
from schemas import ResearchPlan
from langchain_core.messages import SystemMessage , HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature = 0
)

structured_llm = llm.with_structured_output(ResearchPlan ,method = "json_mode")

def research_planner(state: ResearchState):
    print("creating research plan........")

    result = structured_llm.invoke([
        SystemMessage(
            content="""
            You are an expert legal research planner.

            Create a specific and actionable research plan for the given legal issue.

            Do not answer the legal question. Instead, identify the research steps
            that another legal research agent should perform.

            The research should cover, where relevant:
            - Applicable laws, acts, and regulations
            - Relevant legal sections and provisions
            - Exceptions and conditions
            - Relevant judicial precedents and case law
            - Recent amendments or changes
            - Conflicting legal interpretations
            - Important facts that may affect the outcome
            - give priority of each step with the step classified into high/medium/low

             rules : 
             - Each research step should be specific and searchable.
             - Avoid vague instructions such as "research the law".
             - Generate 4 to 7 research steps.
             - Prioritize the most important research steps first.
             - Do not generate unnecessary or repetitive steps.
             - Do not invent specific case names or citations unless they are provided in the input.
            
            
            Return the research plan as JSON matching this structure:

            {
                "research_plan": [
                    {
                        "step": "step 1",
                        "priority": "high"
                    },
                    {
                        "step": "step 2",
                        "priority": "medium"
                    },
                    {
                        "step": "step 3",
                        "priority": "low"
                    }
                ]
            }
            
            """
                    ),

                    HumanMessage(
                        content=f"""
            Legal Query: {state["query"]}

            Jurisdiction: {state["jurisdiction"]}
            Legal Domain: {state["legal_domain"]}
            Legal Issue: {state["legal_issue"]}

            Create the research plan.
            """
                    )
            ])

    return {
        "research_plan": result.research_plan
    }