import streamlit as st
from AI.ai_helper import ask_gemini


def get_career_advice(
    degree,
    branch,
    year,
    skills,
    interests,
    career_goal,
    question
):

    prompt = f"""
You are an expert AI career coach for college students.

Give personalized, practical career guidance based on the student's
actual information.

Student Profile:

Degree: {degree}
Branch: {branch}
Current Year: {year}
Skills: {", ".join(skills) if skills else "No skills provided"}
Interests: {interests if interests else "Not provided"}
Career Goal: {career_goal if career_goal else "Not provided"}

Student's Question:
{question}

Provide:

1. Direct answer to the student's question
2. Recommended career direction
3. Skills they should develop
4. Projects they should build
5. Internship/job preparation advice
6. A practical 3-month action plan

Be realistic and specific.
Do not give generic motivational answers.
"""


    return ask_gemini(prompt)


def show_student_ai():

    st.title("🤖 AI Career Coach")

    st.write(
        "Ask your personal AI career coach anything about your "
        "career, skills, projects, internships or placement preparation."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        degree = st.selectbox(
            "Degree",
            [
                "B.Tech",
                "B.E",
                "B.Sc",
                "BCA",
                "M.Tech",
                "MBA",
                "Other"
            ]
        )

        branch = st.selectbox(
            " Branch",
            [
                "Computer Science",
                "Information Technology",
                "AI & ML",
                "Data Science",
                "ECE",
                "EEE",
                "Mechanical",
                "Civil",
                "Other"
            ]
        )

        year = st.selectbox(
            " Current Year",
            [
                "1st Year",
                "2nd Year",
                "3rd Year",
                "4th Year"
            ]
        )

    with col2:

        skills = st.multiselect(
            " Current Skills",
            [
                "Python",
                "Java",
                "C",
                "C++",
                "SQL",
                "HTML",
                "CSS",
                "JavaScript",
                "React",
                "Node.js",
                "Git",
                "Machine Learning",
                "Data Science",
                "Cloud Computing",
                "Cybersecurity"
            ]
        )

        interests = st.text_area(
            "Areas of Interest",
            placeholder="Example: AI, web development, data science..."
        )

        career_goal = st.text_input(
            "Career Goal",
            placeholder="Example: I want to become an AI Engineer"
        )

    st.divider()

    question = st.text_area(
        " Ask Your Career Coach",
        placeholder=(
            "Example: I know Python and SQL. "
            "What should I learn next to get a data science internship?"
        ),
        height=120
    )

    if st.button(
        "Ask AI Career Coach",
        use_container_width=True
    ):

        if not question.strip():

            st.warning(
                "⚠️ Please enter a question for your career coach."
            )

        else:

            with st.spinner(
                " AI Career Coach is thinking..."
            ):

                try:

                    advice = get_career_advice(
                        degree,
                        branch,
                        year,
                        skills,
                        interests,
                        career_goal,
                        question
                    )

                    st.session_state.student_ai_advice = advice

                except Exception as e:

                    st.error(
                        f"❌ Career coaching failed: {str(e)}"
                    )

    if "student_ai_advice" in st.session_state:

        st.divider()

        st.subheader(" AI Career Coach Response")

        st.write(
            st.session_state.student_ai_advice
        )

    st.divider()

    if st.button(
        "⬅ Back to Student Features",
        use_container_width=True
    ):

        st.session_state.page = "student_features"
        st.rerun()