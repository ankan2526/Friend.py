import os
from openai import OpenAI

def get_client():
    if os.environ.get("RENDER"):
        return OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=os.environ.get("GROQ_API_KEY", "dummy_key")
        )
    else:
        return OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama" # required, but unused
        )
