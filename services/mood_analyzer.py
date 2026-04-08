def analyze_mood(text: str) -> str:
    """
    Analyzes the overall mood (e.g., positive, neutral, tense, negative).
    (This is a simple rule-based mock to be replaced with actual AI logic later)
    """
    text_lower = text.lower()
    
    if "happy" in text_lower or "great" in text_lower or "good" in text_lower:
        return "positive"
    elif "sad" in text_lower or "bad" in text_lower or "awful" in text_lower:
        return "negative"
    elif "worry" in text_lower or "stress" in text_lower:
        return "tense"
    
    return "neutral"
