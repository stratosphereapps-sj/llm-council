from ollama_client import query_ollama

class BaseAgent:
    def __init__(self, name: str, role_prompt: str, model="gemma3:4b"):
        self.name = name
        self.role_prompt = role_prompt
        self.model = model

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