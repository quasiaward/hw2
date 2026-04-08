def suggest_response(text: str) -> str:
    """
    Suggests a softer or more polite version of the message.
    (This is a simple template/mock to be replaced with actual AI logic later)
    """
    if not text.strip():
        return ""
    
    return f"I understand your point. Could we discuss this further? (Polite version of: '{text[:20]}...')"
