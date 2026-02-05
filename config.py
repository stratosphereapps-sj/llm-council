"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Council members - list of Gemini model identifiers
# Using Gemini 3 Flash Preview for all agents
COUNCIL_MODELS = [
    "gemini-3-flash-preview",
    "gemini-3-flash-preview",
    "gemini-3-flash-preview",
    "gemini-3-flash-preview",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "gemini-3-flash-preview"

# Gemini API base endpoint
GEMINI_API_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
