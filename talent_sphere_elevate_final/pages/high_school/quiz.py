import streamlit as st
from AI.ai_helper import ask_gemini


def analyze_quiz(answers):

    prompt = f"""
You are a high-school career counselor.

Analyze the student's answers to this career-interest quiz.

Answers:
{answers}

Identify the student's strongest interest areas.

Possible areas include:
- Technology
- Science
- Medicine
- Engineering
- Business
- Creativity & Design
- Communication
- Leadership
- Research
- Social/Helping careers

Provide:

1. Top 3 interest areas
2. Explanation of why each area matches
3. Suitable career examples
4. Subjects the student should explore
5. Skills they should develop
6. One practical activity/project they can try

Keep the explanation simple and suitable for a high-school student.
Do not make the result sound like a guaranteed career decision.
"""

    return ask_gemini(prompt)


def show_quiz():

    st.title("🧠 Career Interest Quiz")

    st.write(
        "Answer these questions based on what you genuinely enjoy. "
        "There are no right or wrong answers!"
    )

    st.divider()

    questions = [
        " I enjoy using computers and technology.",
        " I enjoy understanding how things work and doing experiments.",
        " I enjoy helping people and learning about health.",
        " I enjoy drawing, designing or creating things.",
        " I enjoy planning, organizing and starting new ideas.",
        " I enjoy speaking, presenting and communicating with people.",
        " I enjoy solving puzzles and challenging problems.",
        " I enjoy taking responsibility and leading a team.",
        " I enjoy researching and learning new information.",
        " I enjoy building or creating practical things."
    ]

    answers = {}

    for i, question in enumerate(questions, start=1):

        st.subheader(f"Question {i}")

        answers[question] = st.radio(
            question,
            [
                " Love it",
                " Like it",
                " Not sure",
                " Not really",
                " Don't like it"
            ],
            key=f"quiz_{i}",
            horizontal=True
        )

    st.divider()

    if st.button(
        "🤖 Analyze My Interests",
        use_container_width=True
    ):

        with st.spinner(
            " discovering your interest areas..."
        ):

            try:

                result = analyze_quiz(answers)

                st.session_state.quiz_result = result

            except Exception as e:

                st.error(
                    f"❌ Quiz analysis failed: {str(e)}"
                )

    if "quiz_result" in st.session_state:

        st.divider()

        st.subheader(" Your Interest Analysis")

        st.write(
            st.session_state.quiz_result
        )

    st.divider()

    if st.button(
        "⬅ Back to High School Features",
        use_container_width=True
    ):

        st.session_state.page = "high_school_features"
        st.rerun()