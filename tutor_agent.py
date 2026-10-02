import os
from llm_client import get_client

def get_tutor_response(prompt: str) -> str:
    client = get_client()
    model = "openai/gpt-oss-20b" if os.environ.get("RENDER") else "llama3.1:8b"
    
    system_prompt = "You are a patient, encouraging Python tutor teaching a beginner. Explain concepts using simple analogies. Never give the exact code immediately; instead, guide the user to the answer."
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Tutor Error: {e}. (Ensure Ollama is running locally)"

