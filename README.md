# Friend.py

Friend.py is a Streamlit-based Python learning environment designed for beginners. It features a built-in code editor with syntax highlighting, an interactive chat-based tutor, and a sandboxed execution environment. 

It is designed to run locally using Ollama for 100% privacy and zero cost, but it can seamlessly fall back to the Groq API when deployed to the cloud (e.g., Render).

## Features
- **Local Inference First:** Uses `llama3.1:8b` and `qwen2.5-coder:7b` via Ollama for tutoring, code review, and quiz generation.
- **Built-in IDE:** Write Python code directly in the browser using `streamlit-ace`.
- **Sandboxed Execution:** Safely executes user code locally with a strict timeout and blocked words filter.
- **Multi-Agent System:**
  - **Tutor Agent:** Explains concepts patiently without giving away the exact code.
  - **Reviewer Agent:** Analyzes code and output to provide hints.
  - **Quizmaster Agent:** Generates context-aware multiple-choice questions.

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Locally (Ollama)
Ensure you have [Ollama](https://ollama.com/) installed and running on your machine.
Pull the required models:
```bash
ollama run llama3.1:8b
ollama run qwen2.5-coder:7b
```

Run the application:
```bash
streamlit run app.py
```

### 3. Deploy to Render
This project is configured to automatically fall back to Groq when deployed on Render.
1. Set the environment variable `RENDER=true` (this is usually auto-set by Render).
2. Set your Groq API key as an environment variable: `GROQ_API_KEY=your_key_here`.
3. Render Start Command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`