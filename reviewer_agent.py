import os
from llm_client import get_client

def review_code(code: str, output: str, challenge: str = "") -> str:
    client = get_client()
    model = "openai/gpt-oss-20b" if os.environ.get("RENDER") else "qwen2.5-coder:7b"
    
    system_prompt = "You are an expert Python code reviewer. The user is a beginner. Point out where their code fails, explain the 'why' behind the error, and provide a small hint. Do NOT rewrite the entire function."
    
    challenge_context = f"\nThe user is attempting this challenge: {challenge}" if challenge else ""
    user_prompt = f"Code:\n{code}\n\nOutput:\n{output}{challenge_context}"
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Reviewer Error: {e}. (Ensure Ollama is running locally)"

