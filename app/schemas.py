from pydantic import BaseModel

class QueryAnalysis(BaseModel):
    jurisdiction :str
    legal_domain:str
    legal_issue:str

class ResearchStep(BaseModel):
    step: str
    priority: str 

class ResearchPlan(BaseModel):
    research_plan : list[ResearchStep]