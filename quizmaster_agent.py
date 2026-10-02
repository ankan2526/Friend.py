import re
import json
import os
from llm_client import get_client


def _strip_markdown(text: str) -> str:
    """
    Convert markdown to clean plain text so the LLM doesn't
    echo markdown syntax back into quiz option strings.
    """
    # Remove fenced code blocks (``` ... ```)
    text = re.sub(r"```[\s\S]*?```", "", text)
    # Remove inline code (`code`)
    text = re.sub(r"`[^`]*`", "", text)
    # Remove headers (## Heading)
    text = re.sub(r"#{1,6}\s*", "", text)
    # Remove bold/italic (**text**, *text*, __text__, _text_)
    text = re.sub(r"\*{1,2}([^*]+)\*{1,2}", r"\1", text)
    text = re.sub(r"_{1,2}([^_]+)_{1,2}", r"\1", text)
    # Remove markdown table separators
    text = re.sub(r"\|[-:]+\|[-|\s:]*", "", text)
    # Remove leading | in table rows
    text = re.sub(r"\|", " ", text)
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Collapse excess whitespace / blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def generate_quiz(topic: str, lesson_content: str = "") -> dict:
    client = get_client()
    model = "openai/gpt-oss-20b" if os.environ.get("RENDER") else "llama3.1:8b"

    system_prompt = """You are an expert Python teacher creating a multiple-choice quiz.

Generate exactly 3 questions based STRICTLY on the lesson content provided.
Do NOT introduce any concept not covered in the lesson.

Return ONLY valid JSON in this exact structure — no extra keys, no markdown:
{
  "questions": [
    {
      "question": "Plain text question here?",
      "options": ["Plain text option 1", "Plain text option 2", "Plain text option 3", "Plain text option 4"],
      "answer": "Exact plain text of the correct option"
    }
  ]
}

STRICT RULES:
- questions, options, and answers must be PLAIN TEXT only — no markdown, no backticks, no code fences
- The "answer" must be the FULL TEXT of one of the 4 options, copied exactly
- Each option must be a complete, meaningful phrase (not just "A", "B", "True", "False")
- One easy question, one medium, one tricky
"""

    # Strip markdown before sending — prevents the model from echoing
    # code fences, header symbols, and bold markers into option text
    clean_lesson = _strip_markdown(lesson_content) if lesson_content else ""
    lesson_context = f"\n\nLesson Content:\n{clean_lesson}" if clean_lesson else ""
    user_message = f"Topic: {topic}{lesson_context}"

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        return {"error": f"Quiz Error: {e}. (Ensure Ollama is running locally)"}

