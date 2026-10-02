# Product Specifications: Friend.py

## 1. Overview
Friend.py is a Streamlit-based Python learning environment designed specifically for a friend starting their coding journey. 

**The Open-Source Advantage (Hacktoberfest requirement):** 
This project showcases the flexibility of open-weights models. When running locally, inference is handled by Ollama, meaning the user can practice offline, for free, with 100% privacy. When deployed to Render, it seamlessly switches to an open-weights API provider to serve the exact same Llama 3.1 model, proving that open models prevent vendor lock-in.

## 2. Core Features
*   **Streamlit UI:** A clean, two-column layout. Left column for the curriculum and chat; Right column for the interactive code editor.
*   **Code Editor Component:** Uses `streamlit-ace` or `streamlit-monaco` to provide syntax highlighting right in the browser.
*   **Dual-Environment Inference:**
    *   **Local:** `base_url="http://localhost:11434/v1"` (Ollama OpenAI-compatible endpoint).
    *   **Render:** `base_url="https://api.groq.com/openai/v1"` (using `GROQ_API_KEY` in Render environment secrets).
*   **Sandboxed Execution:** Executes user code via Python's `subprocess` with a 3-second timeout. Includes a basic security filter to block imports like `os`, `sys`, and `subprocess`.

## 3. Deployment & Infrastructure (Render)
*   **Framework:** Streamlit
*   **Start Command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
*   **Dependencies (`requirements.txt`):** `streamlit`, `openai` (works for both Groq and Ollama), `streamlit-ace`
*   **Environment Variables:** `RENDER` (auto-set by Render), `GROQ_API_KEY` (for cloud inference fallback).

## 4. Data Flow (Spec-Driven Development)
1.  **State Management:** `st.session_state` tracks the current module, chat history, and quiz scores.
2.  **Environment Check:** On app boot, check `if os.environ.get("RENDER"):` to configure the LLM client instance.
3.  **Execution Loop:** 
    *   User types code in the Streamlit UI -> Clicks "Run Code".
    *   Backend checks code against a blocked-words list.
    *   Code is saved to a temp file and executed via `subprocess.run(timeout=3)`.
    *   Output (`stdout`/`stderr`) is captured and displayed in the UI.
    *   Code Reviewer Agent provides AI feedback based on the output.