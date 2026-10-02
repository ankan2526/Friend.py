# Antigravity IDE: Workspace Rules & SDD Context

## 1. Project Identity
*   **Project Name:** Friend.py
*   **Goal:** A local, open-source Python learning environment built for a beginner, featuring interactive lessons, code execution, and AI-driven feedback.
*   **Theme:** Hacktoberfest 2026 "Build for a Friend" (Focus on local open-weight models, offline capabilities, and data privacy).

## 2. Core Context Files
Whenever generating code, refactoring, or planning a feature, you MUST first read and align with the following specifications:
*   `docs/specs.md` (System architecture, feature requirements, and execution safeguards)
*   `docs/AGENTS.md` (Agent definitions, system prompts, and model routing)

## 3. Tech Stack & Dependencies
*   **UI Framework:** Streamlit (latest version).
*   **Agent Orchestration:** LangChain or Agno.
*   **Local LLM Engine:** Ollama (`llama3.1:8b` for tutoring, `qwen2.5-coder:7b` for code review/quizzes).
*   **Cloud Fallback:** Groq / HuggingFace API for Render deployments.
*   **Code Execution:** Native Python `subprocess`.

## 4. Coding Standards & Guidelines
*   **Streamlit State:** Rely strictly on `st.session_state` for managing chat history, current topic, and quiz progress. Avoid global variables.
*   **Modular Design:** Keep Streamlit UI logic in `app.py` and isolate all LLM/Agent logic in their respective files (`tutor_agent.py`, `quizmaster_agent.py`, `reviewer_agent.py`).
*   **Security First:** When writing the `subprocess.run()` logic for the integrated IDE, always include a strict `timeout` (e.g., 5 seconds) and a `capture_output=True` parameter. Do not use `eval()` or `exec()`.
*   **Type Hinting:** Use standard Python type hints for all function signatures.
*   **Error Handling:** Provide graceful UI degradation if the local Ollama instance is not running. Instruct the user on how to start it rather than throwing raw tracebacks.

## 5. AI Interaction Rules (For Antigravity IDE)
*   Do not introduce new external UI libraries (like React or Vue) or database systems (like PostgreSQL) unless explicitly requested. We are keeping this weekend-hack friendly.
*   When generating agent system prompts, ensure the Tutor Agent acts as a guide (providing hints) and never writes the exact solution for the user.
*   Before writing code, briefly state which feature from `docs/specs.md` you are implementing to maintain SDD traceability.