"""Client for Google Gemini API."""

import requests
from config import GEMINI_API_KEY, GEMINI_API_BASE_URL


def query_ollama(model: str, prompt: str) -> str:
    """
    Query Google Gemini API with the given model and prompt.

    Note: Function name kept as query_ollama for backward compatibility.
    """
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file")

    # Construct the full endpoint URL
    endpoint_url = f"{GEMINI_API_BASE_URL}/{model}:generateContent"

    headers = {
        "x-goog-api-key": GEMINI_API_KEY,
        "Content-Type": "application/json",
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(endpoint_url, headers=headers, json=payload)
    response.raise_for_status()

    data = response.json()
    # Extract text from Gemini's response format
    return data["candidates"][0]["content"]["parts"][0]["text"]
