import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

from curriculum import TOPICS
from tutor_agent import get_tutor_response
from quizmaster_agent import generate_quiz
from executor import run_code
from reviewer_agent import review_code

st.set_page_config(page_title="Friend.py", layout="wide")

# ── Custom CSS for independent scrollable columns ──────────────────────────
st.markdown("""
<style>
    /* Make columns independently scrollable */
    [data-testid="stHorizontalBlock"] > div {
        overflow-y: auto;
        max-height: calc(100vh - 160px);
    }
    /* Hide streamlit top decoration */
    #MainMenu, footer { visibility: hidden; }
    /* Challenge box styling */
    .challenge-box {
        background: #1e3a5f;
        border-left: 4px solid #4fa3e3;
        padding: 12px 16px;
        border-radius: 4px;
        margin: 12px 0;
    }
</style>
""", unsafe_allow_html=True)

# ── Session State Initialization ───────────────────────────────────────────
if "current_topic_index" not in st.session_state:
    st.session_state.current_topic_index = 0
if "chat_history" not in st.session_state:
    st.session_state.chat_history = {}    # keyed by topic id
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = {}       # keyed by topic id → raw LLM JSON
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}    # keyed by topic id → {q_index: selected_option}
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = {}  # keyed by topic id → bool
if "quiz_scores" not in st.session_state:
    st.session_state.quiz_scores = {}     # keyed by topic id → int (correct count)
if "show_code_panel" not in st.session_state:
    st.session_state.show_code_panel = True

# ── Helpers ────────────────────────────────────────────────────────────────
def get_current_topic():
    return TOPICS[st.session_state.current_topic_index]

def get_chat_history():
    tid = get_current_topic()["id"]
    if tid not in st.session_state.chat_history:
        st.session_state.chat_history[tid] = []
    return st.session_state.chat_history[tid]

def append_chat(role: str, content: str):
    get_chat_history().append({"role": role, "content": content})

# ── Header ─────────────────────────────────────────────────────────────────
header_left, header_right = st.columns([4, 1])
with header_left:
    st.title("🐍 Friend.py")
    st.caption("Your personal Python learning companion — powered by open-source AI.")

with header_right:
    panel_label = "🙈 Hide Code Editor" if st.session_state.show_code_panel else "💻 Show Code Editor"
    if st.button(panel_label, use_container_width=True):
        st.session_state.show_code_panel = not st.session_state.show_code_panel
        st.rerun()

st.divider()

# ── Topic Navigation Bar ───────────────────────────────────────────────────
topic = get_current_topic()
idx = st.session_state.current_topic_index
total = len(TOPICS)

nav_left, nav_mid, nav_right = st.columns([1, 4, 1])
with nav_left:
    if st.button("← Prev", disabled=(idx == 0), use_container_width=True):
        st.session_state.current_topic_index -= 1
        st.rerun()

with nav_mid:
    st.progress((idx + 1) / total, text=f"Topic {idx + 1} of {total}: **{topic['title']}**")

with nav_right:
    if st.button("Next →", disabled=(idx == total - 1), use_container_width=True):
        st.session_state.current_topic_index += 1
        st.rerun()

st.divider()

# ── Main Layout ────────────────────────────────────────────────────────────
if st.session_state.show_code_panel:
    col1, col2 = st.columns([1, 1], gap="medium")
else:
    col1 = st.container()
    col2 = None

# ── LEFT COLUMN: Lesson + Chat ─────────────────────────────────────────────
with col1:
    tab_lesson, tab_chat, tab_quiz = st.tabs(["📖 Lesson", "💬 Ask Tutor", "🧪 Quiz"])

    # ─ Lesson Tab ─────────────────────────────────────────────────────────
    with tab_lesson:
        st.markdown(topic["lesson"])
        st.markdown(
            f"""<div class="challenge-box">
            🎯 <b>Challenge:</b> {topic['challenge']}
            </div>""",
            unsafe_allow_html=True
        )

    # ─ Chat Tab ───────────────────────────────────────────────────────────
    with tab_chat:
        chat_history = get_chat_history()

        for msg in chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input(f"Ask about '{topic['title']}'..."):
            append_chat("user", prompt)
            with st.chat_message("user"):
                st.markdown(prompt)

            context_prompt = f"[Current topic: {topic['title']}]\n\n{prompt}"
            with st.chat_message("assistant"):
                with st.spinner("Tutor is thinking..."):
                    response = get_tutor_response(context_prompt)
                st.markdown(response)
            append_chat("assistant", response)

    # ─ Quiz Tab ───────────────────────────────────────────────────────────
    with tab_quiz:
        tid = topic["id"]

        # ── Generate / New Quiz button ────────────────────────────────────
        btn_label = "🎲 Generate Quiz" if tid not in st.session_state.quiz_data else "🎲 New Quiz"
        if st.button(btn_label, use_container_width=True):
            with st.spinner(f"Generating quiz on '{topic['title']}'..."):
                result = generate_quiz(topic["title"], lesson_content=topic["lesson"])
            if "error" in result:
                st.error(result["error"])
            else:
                st.session_state.quiz_data[tid] = result
                st.session_state.quiz_answers[tid] = {}
                st.session_state.quiz_submitted[tid] = False
                st.session_state.quiz_scores.pop(tid, None)
                st.rerun()

        # ── Render quiz if data exists ────────────────────────────────────
        if tid in st.session_state.quiz_data:
            quiz = st.session_state.quiz_data[tid]
            questions = quiz.get("questions", [])
            is_submitted = st.session_state.quiz_submitted.get(tid, False)

            # Ensure answer dict exists for this topic
            if tid not in st.session_state.quiz_answers:
                st.session_state.quiz_answers[tid] = {}

            st.markdown("### 📝 Quiz Time!")

            for q_idx, q in enumerate(questions):
                question_text = q.get("question", "")
                options = q.get("options", [])
                correct = q.get("answer", "")

                st.markdown(f"**Q{q_idx + 1}: {question_text}**")

                if not is_submitted:
                    # ── Pre-submission: show radio buttons ────────────────
                    selected = st.radio(
                        label=f"q{q_idx}",
                        options=options,
                        index=None,
                        key=f"quiz_{tid}_{q_idx}",
                        label_visibility="collapsed"
                    )
                    st.session_state.quiz_answers[tid][q_idx] = selected
                else:
                    # ── Post-submission: show result per question ─────────
                    user_answer = st.session_state.quiz_answers[tid].get(q_idx)
                    for opt in options:
                        if opt == correct and opt == user_answer:
                            st.markdown(f"- ✅ **{opt}** ← Your answer (Correct!)", )
                        elif opt == correct:
                            st.markdown(f"- ✅ **{opt}** ← Correct answer")
                        elif opt == user_answer:
                            st.markdown(f"- ❌ ~~{opt}~~ ← Your answer")
                        else:
                            st.markdown(f"- {opt}")

                st.write("")

            # ── Submit / Retake buttons ───────────────────────────────────
            if not is_submitted:
                all_answered = all(
                    st.session_state.quiz_answers[tid].get(i) is not None
                    for i in range(len(questions))
                )
                if st.button(
                    "Submit Quiz ✅",
                    disabled=not all_answered,
                    use_container_width=True,
                    type="primary"
                ):
                    # Score calculation
                    answers = st.session_state.quiz_answers[tid]
                    correct_count = sum(
                        1 for i, q in enumerate(questions)
                        if answers.get(i) == q.get("answer")
                    )
                    st.session_state.quiz_scores[tid] = correct_count
                    st.session_state.quiz_submitted[tid] = True
                    st.rerun()

                if not all_answered:
                    st.caption("⬆️ Answer all questions to enable Submit.")
            else:
                # ── Score banner ──────────────────────────────────────────
                score = st.session_state.quiz_scores.get(tid, 0)
                total_q = len(questions)
                if score == total_q:
                    st.success(f"🎉 Perfect score! You got **{score} / {total_q}**!")
                elif score >= total_q // 2:
                    st.warning(f"👍 Good effort! You scored **{score} / {total_q}**.")
                else:
                    st.error(f"📚 Keep studying! You scored **{score} / {total_q}**.")

                if st.button("🔁 Retake Quiz", use_container_width=True):
                    st.session_state.quiz_answers[tid] = {}
                    st.session_state.quiz_submitted[tid] = False
                    st.session_state.quiz_scores.pop(tid, None)
                    st.rerun()

# ── RIGHT COLUMN: Code Editor ──────────────────────────────────────────────
if col2 is not None:
    with col2:
        st.subheader("💻 Code Editor")
        st.caption(f"🎯 Challenge: {topic['challenge']}")

        from streamlit_ace import st_ace

        code = st_ace(
            value=topic.get("starter_code", "# Write your Python code here\n"),
            language="python",
            theme="monokai",
            keybinding="vscode",
            font_size=14,
            tab_size=4,
            key=f"ace_editor_{topic['id']}"  # reset editor when topic changes
        )

        if st.button("▶ Run Code", use_container_width=True, type="primary"):
            with st.spinner("Executing..."):
                output = run_code(code)

            st.markdown("**Output:**")
            st.code(output, language="text")

            with st.spinner("Reviewing your code..."):
                review = review_code(code, output, challenge=topic["challenge"])

            st.markdown("**🤖 Code Review:**")
            st.info(review)
