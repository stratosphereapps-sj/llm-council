from ollama_client import query_ollama
from config import COUNCIL_MODELS

class BaseAgent:
    def __init__(self, name: str, role_prompt: str, model=None):
        self.name = name
        self.role_prompt = role_prompt
        # Use the first council model as default if no model specified
        self.model = model if model else COUNCIL_MODELS[0]

    def run(self, input_text: str) -> str:
        full_prompt = f"""
You are {self.name}.

Role:
{self.role_prompt}

Rules:
- You MUST rely on the input below.
- You MUST build on it.
- Do NOT answer independently.

========== INPUT ==========
{input_text}
===========================

Your response:
"""
        return query_ollama(self.model, full_prompt)