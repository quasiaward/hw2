def analyze_tone(text: str) -> str:
    """
    Analyzes the tone of the conversation (e.g., friendly, formal, aggressive, urgent).
    (This is a simple rule-based mock to be replaced with actual AI logic later)
    """
    text_lower = text.lower()
    
    if "!" in text or "asap" in text_lower or "urgent" in text_lower:
        return "urgent"
    elif "stupid" in text_lower or "terrible" in text_lower:
        return "aggressive"
    elif "please" in text_lower or "thank" in text_lower:
        return "friendly"
    
    return "formal"
