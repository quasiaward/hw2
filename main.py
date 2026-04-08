from fastapi import FastAPI
from models.schemas import ChatRequest, ChatAnalysisResponse
from services.summarizer import summarize_text
from services.tone_analyzer import analyze_tone
from services.mood_analyzer import analyze_mood
from services.response_suggester import suggest_response

app = FastAPI(
    title="Chat Analysis API",
    description="A minimalist AI API server to analyze chat conversations.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Chat Analysis API is running!"}

@app.post("/analyze", response_model=ChatAnalysisResponse)
def analyze_chat(request: ChatRequest):
    """
    Analyzes the given text and returns summary, tone, mood, and suggested softer response.
    """
    text = request.text
    
    return ChatAnalysisResponse(
        summary=summarize_text(text),
        tone=analyze_tone(text),
        mood=analyze_mood(text),
        suggested_response=suggest_response(text)
    )

if __name__ == "__main__":
    import uvicorn
    # Make sure this runs easily on Ubuntu/local setup
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
