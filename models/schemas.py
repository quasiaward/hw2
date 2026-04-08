from pydantic import BaseModel

class ChatRequest(BaseModel):
    text: str

class ChatAnalysisResponse(BaseModel):
    summary: str
    tone: str
    mood: str
    suggested_response: str
