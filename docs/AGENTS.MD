# AI Agents Architecture

This project utilizes a multi-agent system powered by open-weights models (Llama-3.1-8B and Qwen2.5-Coder). The app is environment-aware: it uses a local Ollama instance for offline privacy, and gracefully falls back to a high-speed open-weights API (e.g., Groq) when hosted on Render.

## 1. The Lesson Curator (Tutor Agent)
*   **Role:** Acts as the primary teacher and conversational interface.
*   **System Prompt Focus:** "You are a patient, encouraging Python tutor teaching a beginner. Explain concepts using simple analogies. Never give the exact code immediately; instead, guide the user to the answer."
*   **Model:** Llama-3.1-8B (via local Ollama or Groq API fallback).

## 2. The Quizmaster (Assessment Agent)
*   **Role:** Generates dynamic, context-aware quizzes based on the current lesson.
*   **System Prompt Focus:** "Generate 3 multiple-choice questions based on the provided Python topic. Format output in strict JSON."
*   **Model:** Llama-3.1-8B. (Using JSON mode for reliable parsing in Streamlit).

## 3. The Code Reviewer (IDE Assistant Agent)
*   **Role:** Analyzes the user's code submissions, checks for syntax errors, and provides hints.
*   **System Prompt Focus:** "You are an expert Python code reviewer. The user is a beginner. Point out where their code fails, explain the 'why' behind the error, and provide a small hint. Do NOT rewrite the entire function."
*   **Model:** Qwen2.5-Coder-7B or Llama-3.1-8B (optimized for code reasoning).