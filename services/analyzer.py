from textblob import TextBlob

def analyze_chat(text: str) -> dict:
    """
    Analyze the chat text and return sentiment, tone, summary, and response suggestion.
    """
    blob = TextBlob(text)
    
    # Sentiment analysis
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        sentiment = "positive"
    elif polarity < -0.1:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    # Tone analysis (simple mapping from sentiment)
    if sentiment == "positive":
        tone = "friendly"
    elif sentiment == "negative":
        tone = "angry"
    else:
        tone = "neutral"
    
    # Summary (simple: first sentence or truncated text)
    sentences = blob.sentences
    if sentences:
        summary = str(sentences[0])
    else:
        summary = text[:100] + "..." if len(text) > 100 else text
    
    # Response suggestion based on sentiment
    if sentiment == "positive":
        response_suggestion = "That's great! Glad to hear it."
    elif sentiment == "negative":
        response_suggestion = "I'm sorry to hear that. How can I help?"
    else:
        response_suggestion = "Thanks for sharing."
    
    return {
        "sentiment": sentiment,
        "tone": tone,
        "summary": summary,
        "response_suggestion": response_suggestion
    }