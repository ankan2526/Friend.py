# Product Specifications: Friend.py

## 1. Overview
Friend.py is a Streamlit-based Python learning environment designed specifically for a friend starting their coding journey. 

**The Open-Source Advantage (Hacktoberfest requirement):** 
This project showcases the flexibility of open-weights models. When running locally, inference is handled by Ollama, meaning the user can practice offline, for free, with 100% privacy. When deployed to Render, it seamlessly switches to an open-weights API provider to serve the exact same Llama 3.1 model, proving that open models prevent vendor lock-in.

## 2. Core Features
*   **Structured Curriculum:** A predefined, ordered set of Python topics (e.g., Variables, Loops, Functions). Each topic includes lesson content, challenges, and is the context for the AI agents.
*   **Streamlit UI:** A two-column layout with **independent scroll areas**. Left column for the curriculum/lesson content and chat; Right column for the interactive code editor.
*   **Hidable Code Panel:** A toggle button ("Show/Hide Code Panel") to collapse the right column, giving full-width reading space for the lesson content.
*   **Code Editor Component:** Uses `streamlit-ace` to provide syntax highlighting right in the browser.
*   **Dual-Environment Inference:**
    *   **Local:** `base_url="http://localhost:11434/v1"` (Ollama OpenAI-compatible endpoint).
    *   **Render:** `base_url="https://api.groq.com/openai/v1"` (using `GROQ_API_KEY` in Render environment secrets).
*   **Sandboxed Execution:** Executes user code via Python's `subprocess` with a 3-second timeout. Includes a basic security filter to block imports like `os`, `sys`, and `subprocess`.
*   **Interactive Quiz:** Each quiz question displays as a `st.radio()` widget with selectable options. A single "Submit Quiz" button at the bottom evaluates all answers at once, shows per-question ✅/❌ feedback, and records the score in session state.

## 3. Curriculum Structure (`curriculum.py`)
Each topic is a Python dict with the following keys:
```python
{
    "id": "01_variables",
    "title": "Variables & Data Types",
    "lesson": "Markdown string with lesson content",
    "challenge": "A coding challenge description for the user",
    "starter_code": "# Starter code for the editor"
}
```

**Predefined Topics (in order):**
1.  Variables & Data Types
2.  String Formatting
3.  Lists & Tuples
4.  Dictionaries
5.  Conditionals (`if`/`else`)
6.  Loops (`for`/`while`)
7.  Functions
8.  File I/O (read only, sandboxed)
9.  Error Handling (`try`/`except`)
10. Basic OOP (Classes)

## 4. Deployment & Infrastructure (Render)
*   **Framework:** Streamlit
*   **Start Command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
*   **Dependencies (`requirements.txt`):** `streamlit`, `openai`, `streamlit-ace`, `python-dotenv`
*   **Environment Variables:** `RENDER` (auto-set by Render), `GROQ_API_KEY` (for cloud inference fallback).

## 5. Data Flow (Spec-Driven Development)
1.  **State Management:** `st.session_state` tracks the `current_topic_index`, `chat_history` (per topic), `quiz_data` (per topic — the raw LLM output), `quiz_answers` (per topic — dict mapping question index to user's selected option), `quiz_submitted` (per topic — bool), `quiz_scores` (per topic — int correct count), and `show_code_panel` (bool).
2.  **Environment Check:** On app boot, `load_dotenv()` is called, then `if os.environ.get("RENDER"):` configures the LLM client.
3.  **Topic Navigation:** Prev/Next buttons update `current_topic_index`. Switching topics clears the chat history for the new topic.
4.  **Interactive Quiz Flow:**
    *   User clicks "Generate Quiz" → Quizmaster agent returns JSON → stored in `quiz_data[topic_id]`.
    *   Each question renders a `st.radio()` with its options. Selections are stored in `quiz_answers[topic_id][q_index]`.
    *   User clicks "Submit Quiz" → sets `quiz_submitted[topic_id] = True` and calculates `quiz_scores[topic_id]`.
    *   After submission: each question shows ✅ if correct, ❌ with the correct answer if wrong. Score displayed as `X / 3`.
    *   A "Retake Quiz" button resets `quiz_submitted` and `quiz_answers` for the topic (but keeps `quiz_data` to avoid regenerating).
4.  **Execution Loop:** 
    *   User types code in the Streamlit UI -> Clicks "Run Code".
    *   Backend checks code against a blocked-words list.
    *   Code is saved to a temp file and executed via `subprocess.run(timeout=3)`.
    *   Output (`stdout`/`stderr`) is captured and displayed in the UI.
    *   Code Reviewer Agent provides AI feedback based on the output AND the current topic's challenge.