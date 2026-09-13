from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage , SystemMessage

load_dotenv()


llm = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature = 0
) #intialize llm 

response = llm.invoke([
    SystemMessage(
        content = "You are a legal research assistant specializing in Indian law."
    ),
    HumanMessage(
        content = "Can an employer terminate an employee without notice in India?"
    )
]) # invoke llm

print(response.content)