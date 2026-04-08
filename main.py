from fastapi import FastAPI
from .schemas.analyze import AnalyzeRequest, AnalyzeResponse
from .services.analyzer import analyze_chat

app = FastAPI(title="Chat Analyzer", description="AI-powered chat analysis API")

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_chat_endpoint(request: AnalyzeRequest):
    """
    Analyze user chat text for sentiment, tone, summary, and response suggestion.
    """
    result = analyze_chat(request.text)
    return AnalyzeResponse(**result)