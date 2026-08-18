import streamlit as st
from AI.ai_helper import ask_gemini


def get_career_advice(role, experience, skills, goal, industry):

    prompt = f"""
You are an expert AI career coach for working professionals.

Professional Details:
Current Role: {role}
Experience: {experience} years
Skills: {", ".join(skills) if skills else "No skills provided"}
Industry: {industry}
Career Goal: {goal}

Give personalized career coaching based on the information above.

Cover:

1. Current career assessment
2. Strengths
3. Biggest career risks or weaknesses
4. Skills to improve
5. Recommended next career move
6. How to increase salary and career growth
7. Specific actions for the next 30 days
8. Specific actions for the next 3 months
9. Long-term career direction
10. Final personalized advice

Do not give generic motivational advice.
Be practical, realistic and specific to this professional.
"""

    return ask_gemini(prompt)


def show_ai_coach():

    st.title("🤖 AI Career Coach")

    st.write(
        "Get personalized career guidance based on your "
        "current experience, skills and career goals."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        role = st.selectbox(
            " Current Role",
            [
                "Software Engineer",
                "Python Developer",
                "Java Developer",
                "Frontend Developer",
                "Backend Developer",
                "Full Stack Developer",
                "Data Analyst",
                "Data Scientist",
                "AI Engineer",
                "ML Engineer",
                "Cloud Engineer",
                "DevOps Engineer",
                "Cyber Security Analyst",
                "QA Engineer",
                "Project Manager",
                "Business Analyst"
            ]
        )

        experience = st.slider(
            " Years of Experience",
            0,
            25,
            1
        )

        industry = st.selectbox(
            " Industry",
            [
                "IT",
                "Finance",
                "Healthcare",
                "Education",
                "Manufacturing",
                "Retail",
                "Telecom"
            ]
        )

    with col2:

        skills = st.multiselect(
            " Current Skills",
            [
                "Python",
                "Java",
                "C++",
                "SQL",
                "JavaScript",
                "React",
                "Node.js",
                "Git",
                "Docker",
                "AWS",
                "Azure",
                "Kubernetes",
                "Machine Learning",
                "Deep Learning",
                "NLP",
                "TensorFlow",
                "PyTorch",
                "Power BI",
                "Tableau",
                "Communication",
                "Leadership",
                "Problem Solving",
                "Project Management"
            ]
        )

        goal = st.text_area(
            "Career Goal",
            placeholder=(
                "Example: I want to become a Senior AI Engineer "
                "within the next 2 years."
            )
        )

    st.divider()

    if st.button(
        "🤖 Ask AI Career Coach",
        use_container_width=True
    ):

        if not goal.strip():

            st.warning("⚠️ Please enter your career goal.")

        else:

            with st.spinner(
                "🤖 AI Career Coach is analyzing your career..."
            ):

                try:

                    advice = get_career_advice(
                        role,
                        experience,
                        skills,
                        goal,
                        industry
                    )

                    st.session_state.professional_ai_coach = advice

                except Exception as e:

                    st.error(
                        f"❌ Career coaching failed: {str(e)}"
                    )

    if st.session_state.get("professional_ai_coach"):

        st.divider()

        st.subheader("💡 Your Personalized AI Career Advice")

        st.write(
            st.session_state.professional_ai_coach
        )

    st.divider()

    if st.button(
        "⬅ Back to Professional Features",
        use_container_width=True
    ):

        st.session_state.page = "features"
        st.rerun()