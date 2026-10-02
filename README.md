# Friend.py

Friend.py is a beginner-friendly Python learning app built with Streamlit. It combines a structured curriculum, a built-in browser editor, a chat tutor, a quiz generator, and a sandboxed code runner to help someone learn Python step by step.

The app is designed to work locally with Ollama for privacy and zero-cost inference, while automatically switching to Groq in cloud deployments such as Render.

## Features
- **Structured curriculum** with lessons, challenges, and starter code for each Python topic
- **Browser-based Python editor** using `streamlit-ace`
- **Chat tutor** that explains concepts without giving away the exact answer
- **Quiz generator** that produces topic-specific multiple-choice questions
- **Code reviewer** that gives beginner-friendly hints after running code
- **Sandboxed execution** with a short timeout and blocked unsafe imports
- **Local-first AI** using Ollama, plus cloud fallback on Render

## Local model setup
When `RENDER` is not set, the application connects to the local Ollama OpenAI-compatible endpoint:
- `http://localhost:11434/v1`

The app currently uses:
- Tutor and quiz generation: `llama3.1:8b`
- Code review: `qwen2.5-coder:7b`

If you are running on Render, the app switches to Groq using:
- `https://api.groq.com/openai/v1`
- environment variable: `GROQ_API_KEY`

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start Ollama locally
Install and run [Ollama](https://ollama.com/) then pull the required models:
```bash
ollama pull llama3.1:8b
ollama pull qwen2.5-coder:7b
```

### 3. Run the app
```bash
streamlit run app.py
```

## Render deployment
This project is configured to auto-detect Render and use the Groq API instead of the local Ollama endpoint.

Required environment variables:
```bash
RENDER=true
GROQ_API_KEY=your_key_here
```

Start command:
```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

## Running tests
```bash
pytest
```

## Notes
- The app executes submitted code in a temporary Python file with a 3-second timeout.
- Unsafe code containing imports such as `os`, `sys`, or `subprocess` is blocked by design.
- The project is intentionally designed for a beginner-friendly learning flow without requiring a paid AI provider for local use.