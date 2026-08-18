import streamlit as st
from AI.ai_helper import ask_gemini


def analyze_career_switch(
    current_role,
    experience,
    skills,
    current_industry,
    target_role,
    target_industry,
    reason
):

    prompt = f"""
You are an expert career transition advisor.

Analyze this professional's career-switch plan.

Current Role: {current_role}
Experience: {experience} years
Current Skills: {", ".join(skills) if skills else "No skills provided"}
Current Industry: {current_industry}

Target Role: {target_role}
Target Industry: {target_industry}

Reason for Career Switch:
{reason}

Provide a realistic and personalized career transition analysis.

Include:

1. Career switch feasibility
2. Transferable skills
3. Missing technical skills
4. Missing soft skills
5. Skills that should be learned first
6. Recommended projects to build
7. Recommended certifications if useful
8. Possible entry-level/intermediate roles during transition
9. Expected challenges
10. A 3-month transition roadmap
11. A 6-month transition roadmap
12. Resume and interview preparation advice
13. Final recommendation

Do not discourage the professional unnecessarily.
Do not make unrealistic salary or job guarantees.
Focus on practical steps based on their current experience and skills.
"""

    return ask_gemini(prompt)


def show_career_switch():

    st.title("🔄  Career Switch Planner")

    st.write(
        "Plan your transition from your current career "
        "to your target career using AI."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        current_role = st.selectbox(
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
            2
        )

        current_industry = st.selectbox(
            " Current Industry",
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

        target_role = st.selectbox(
            "Target Role",
            [
                "Senior Software Engineer",
                "Full Stack Developer",
                "Data Scientist",
                "Data Engineer",
                "AI Engineer",
                "ML Engineer",
                "Cloud Engineer",
                "DevOps Engineer",
                "Cybersecurity Engineer",
                "Product Manager",
                "Engineering Manager",
                "Business Analyst"
            ]
        )

        target_industry = st.selectbox(
            "Target Industry",
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

    reason = st.text_area(
        " Why do you want to switch careers?",
        placeholder=(
            "Example: I want to move from software development "
            "to AI because I enjoy machine learning and want to "
            "work on AI-based products."
        )
    )

    st.divider()

    if st.button(
        "🤖 Analyze Career Switch",
        use_container_width=True
    ):

        if not reason.strip():

            st.warning(
                "⚠️ Please explain why you want to switch careers."
            )

        else:

            with st.spinner(
                "🤖 AI is analyzing your career transition..."
            ):

                try:

                    result = analyze_career_switch(
                        current_role,
                        experience,
                        skills,
                        current_industry,
                        target_role,
                        target_industry,
                        reason
                    )

                    st.session_state.career_switch_result = result

                except Exception as e:

                    st.error(
                        f"❌ Career switch analysis failed: {str(e)}"
                    )

    if st.session_state.get("career_switch_result"):

        st.divider()

        st.subheader("📊 AI Career Switch Analysis")

        st.write(
            st.session_state.career_switch_result
        )

    st.divider()

    if st.button(
        "⬅ Back to Professional Features",
        use_container_width=True
    ):

        st.session_state.page = "features"
        st.rerun()