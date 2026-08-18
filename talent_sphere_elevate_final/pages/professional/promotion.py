import streamlit as st
from AI.ai_helper import ask_gemini


def analyze_promotion(
    role,
    experience,
    skills,
    achievements,
    responsibilities,
    target_role
):

    prompt = f"""
You are an expert corporate career and promotion advisor.

Evaluate whether this working professional is ready for promotion.

Current Role: {role}
Experience: {experience} years
Skills: {", ".join(skills) if skills else "No skills provided"}
Major Achievements: {achievements}
Current Responsibilities: {responsibilities}
Target Promotion Role: {target_role}

Analyze the ACTUAL information provided.

Evaluate:

1. Promotion readiness score from 0 to 100
2. Current strengths
3. Evidence supporting promotion readiness
4. Missing skills or competencies
5. Leadership readiness
6. Areas that need improvement
7. Achievements that should be highlighted during appraisal
8. Actions to take before requesting promotion
9. A practical 90-day promotion preparation plan
10. How to discuss promotion with the manager

Do NOT give a high score simply because the professional has many years
of experience.

Focus on responsibilities, achievements, impact, skills and leadership.

Return a realistic and personalized assessment.
"""

    return ask_gemini(prompt)


def show_promotion():

    st.title("📈  Promotion Readiness")

    st.write(
        "Find out how ready you are for your next promotion "
        "using AI-powered career analysis."
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
            3
        )

        target_role = st.text_input(
            " Target Promotion Role",
            placeholder="Example: Senior Software Engineer"
        )

    with col2:

        skills = st.multiselect(
            "Current Skills",
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

    achievements = st.text_area(
        " Major Achievements",
        placeholder=(
            "Example: Improved application performance by 30%, "
            "led a team of 4 developers, delivered 5 major projects..."
        )
    )

    responsibilities = st.text_area(
        " Current Responsibilities",
        placeholder=(
            "Describe your current responsibilities, projects, "
            "team responsibilities and ownership..."
        )
    )

    st.divider()

    if st.button(
        "🤖 Check Promotion Readiness",
        use_container_width=True
    ):

        if not target_role.strip():

            st.warning(
                "⚠️ Please enter your target promotion role."
            )

        elif not achievements.strip():

            st.warning(
                "⚠️ Please describe at least some of your achievements."
            )

        else:

            with st.spinner(
                "🤖 AI is evaluating your promotion readiness..."
            ):

                try:

                    result = analyze_promotion(
                        role,
                        experience,
                        skills,
                        achievements,
                        responsibilities,
                        target_role
                    )

                    st.session_state.promotion_result = result

                except Exception as e:

                    st.error(
                        f"❌ Promotion analysis failed: {str(e)}"
                    )

    if st.session_state.get("promotion_result"):

        st.divider()

        st.subheader("📊 AI Promotion Readiness Assessment")

        st.write(
            st.session_state.promotion_result
        )

    st.divider()

    if st.button(
        "⬅ Back to Professional Features",
        use_container_width=True
    ):

        st.session_state.page = "features"
        st.rerun()