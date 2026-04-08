def summarize_text(text: str) -> str:
    """
    Summarizes the given chat text into 1-2 sentences.
    (This is a simple template/mock to be replaced with actual AI logic later)
    """
    if not text.strip():
        return "No text provided."
    return f"This is a 1-2 sentence summary of the chat. The user talked about '{text[:30]}...'."
