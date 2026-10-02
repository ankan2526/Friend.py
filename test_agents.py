import os
import json
from unittest.mock import patch, MagicMock
import pytest

from llm_client import get_client
from tutor_agent import get_tutor_response
from quizmaster_agent import generate_quiz
from reviewer_agent import review_code

def test_get_client_local():
    if "RENDER" in os.environ:
        del os.environ["RENDER"]
    client = get_client()
    assert str(client.base_url) == "http://localhost:11434/v1/"
    assert client.api_key == "ollama"

def test_get_client_render():
    os.environ["RENDER"] = "true"
    os.environ["GROQ_API_KEY"] = "test_key"
    client = get_client()
    assert str(client.base_url) == "https://api.groq.com/openai/v1/"
    assert client.api_key == "test_key"
    del os.environ["RENDER"]
    del os.environ["GROQ_API_KEY"]

@patch('tutor_agent.get_client')
def test_tutor_agent(mock_get_client):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Mocked tutor response"))]
    mock_client.chat.completions.create.return_value = mock_response
    mock_get_client.return_value = mock_client

    response = get_tutor_response("How do I write a for loop?")
    assert response == "Mocked tutor response"
    mock_client.chat.completions.create.assert_called_once()

@patch('quizmaster_agent.get_client')
def test_quizmaster_agent(mock_get_client):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_json_content = '{"questions": [{"question": "Q1", "options": ["A", "B", "C", "D"], "answer": "A"}]}'
    mock_response.choices = [MagicMock(message=MagicMock(content=mock_json_content))]
    mock_client.chat.completions.create.return_value = mock_response
    mock_get_client.return_value = mock_client

    lesson = "A variable stores a value. Use int for whole numbers."
    response = generate_quiz("Python Variables", lesson_content=lesson)
    assert "questions" in response
    assert len(response["questions"]) == 1
    assert response["questions"][0]["question"] == "Q1"

    # Verify lesson content was passed in the prompt
    call_args = mock_client.chat.completions.create.call_args
    messages = call_args[1]["messages"]
    user_message = next(m["content"] for m in messages if m["role"] == "user")
    assert lesson in user_message

@patch('reviewer_agent.get_client')
def test_reviewer_agent(mock_get_client):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Mocked reviewer response"))]
    mock_client.chat.completions.create.return_value = mock_response
    mock_get_client.return_value = mock_client

    response = review_code("print('hello'", "SyntaxError")
    assert response == "Mocked reviewer response"
    mock_client.chat.completions.create.assert_called_once()

@patch('reviewer_agent.get_client')
def test_reviewer_agent_with_challenge(mock_get_client):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Hint: check your syntax"))]
    mock_client.chat.completions.create.return_value = mock_response
    mock_get_client.return_value = mock_client

    challenge = "Print numbers 1 to 10 using a for loop"
    review_code("for i in range(10): print(i)", "0\n1\n2...", challenge=challenge)

    call_args = mock_client.chat.completions.create.call_args
    messages = call_args[1]["messages"]
    user_message = next(m["content"] for m in messages if m["role"] == "user")
    assert challenge in user_message

def test_curriculum_structure():
    from curriculum import TOPICS
    assert len(TOPICS) == 10
    required_keys = {"id", "title", "lesson", "challenge", "starter_code"}
    for topic in TOPICS:
        assert required_keys.issubset(topic.keys()), f"Topic '{topic.get('id')}' is missing keys"
        assert len(topic["lesson"]) > 50, f"Lesson for '{topic['id']}' is too short"
        assert len(topic["challenge"]) > 10, f"Challenge for '{topic['id']}' is too short"

def test_quiz_scoring_logic():
    """Unit test for the answer comparison logic used in the quiz submit flow."""
    questions = [
        {"question": "Q1", "options": ["A", "B", "C", "D"], "answer": "A"},
        {"question": "Q2", "options": ["A", "B", "C", "D"], "answer": "B"},
        {"question": "Q3", "options": ["A", "B", "C", "D"], "answer": "C"},
    ]
    # User got Q1 and Q3 correct, Q2 wrong
    answers = {0: "A", 1: "D", 2: "C"}

    correct_count = sum(
        1 for i, q in enumerate(questions)
        if answers.get(i) == q.get("answer")
    )
    assert correct_count == 2

    # All correct
    all_correct = {0: "A", 1: "B", 2: "C"}
    assert sum(
        1 for i, q in enumerate(questions)
        if all_correct.get(i) == q.get("answer")
    ) == 3

    # None correct
    none_correct = {0: "D", 1: "D", 2: "D"}
    assert sum(
        1 for i, q in enumerate(questions)
        if none_correct.get(i) == q.get("answer")
    ) == 0


def test_strip_markdown():
    from quizmaster_agent import _strip_markdown

    raw = """
## Variables & Data Types

A **variable** is a named container. Use `int` for whole numbers.

```python
x = 42
print(type(x))  # <class 'int'>
```

| Type | Example |
|------|---------|
| int  | 42      |
"""
    result = _strip_markdown(raw)

    assert "##" not in result,         "Headers should be removed"
    assert "**" not in result,         "Bold markers should be removed"
    assert "```" not in result,        "Code fences should be removed"
    assert "`int`" not in result,      "Inline code backticks should be removed"
    assert "|-" not in result,         "Table separators should be removed"
    assert "variable" in result,       "Regular text should be preserved"
    assert "int" in result,            "Content inside code should still appear"
