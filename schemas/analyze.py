from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    text: str

class AnalyzeResponse(BaseModel):
    sentiment: str  # "positive", "negative", "neutral"
    tone: str  # "friendly", "angry", "neutral"
    summary: str
    response_suggestion: str