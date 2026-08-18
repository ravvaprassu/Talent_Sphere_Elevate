import streamlit as st
from AI.ai_helper import ask_gemini


def analyze_skill_gap(role, experience, skills, target_role, industry):

    prompt = f"""
You are an expert career development and skill-gap advisor.

Analyze the professional's current skills against their target career.

Current Role: {role}
Experience: {experience} years
Current Skills: {", ".join(skills) if skills else "No skills provided"}
Target Role: {target_role}
Industry: {industry}

Identify:

1. Current strengths
2. Missing technical skills
3. Missing soft skills
4. Most important skills to learn first
5. Recommended projects to build
6. Recommended certifications if useful
7. A practical 3-month learning roadmap
8. A practical 6-month career roadmap
9. Overall readiness for the target role out of 100

Prioritize skills based on actual importance for the target role.
Do not simply list generic skills.

Give a personalized and realistic analysis.
"""

    return ask_gemini(prompt)


def show_skill_gap():

    st.title("🧠  Skill Gap Analyzer")

    st.write(
        "Compare your current skills with your target role "
        "and discover exactly what you need to learn."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        role = st.selectbox(
            "Current Role",
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

        target_role = st.selectbox(
            " Target Role",
            [
                "Senior Software Engineer",
                "Senior Python Developer",
                "Senior Java Developer",
                "Full Stack Developer",
                "Data Scientist",
                "Data Engineer",
                "AI Engineer",
                "ML Engineer",
                "Cloud Engineer",
                "DevOps Engineer",
                "Cybersecurity Engineer",
                "Engineering Manager",
                "Product Manager",
                "Business Analyst"
            ]
        )

        skills = st.multiselect(
            " Your Current Skills",
            [
                "Python",
                "Java",
                "C++",
                "SQL",
                "HTML",
                "CSS",
                "JavaScript",
                "React",
                "Node.js",
                "Git",
                "Docker",
                "AWS",
                "Azure",
                "Kubernetes",
                "Power BI",
                "Tableau",
                "Machine Learning",
                "Deep Learning",
                "NLP",
                "TensorFlow",
                "PyTorch",
                "Communication",
                "Leadership",
                "Problem Solving",
                "Project Management"
            ]
        )

    st.divider()

    if st.button(
        "🤖 Analyze My Skill Gap",
        use_container_width=True
    ):

        with st.spinner(
            "🤖 AI is comparing your skills with the target role..."
        ):

            try:

                result = analyze_skill_gap(
                    role,
                    experience,
                    skills,
                    target_role,
                    industry
                )

                st.session_state.professional_skill_gap = result

            except Exception as e:

                st.error(
                    f"❌ Skill gap analysis failed: {str(e)}"
                )

    if st.session_state.get("professional_skill_gap"):

        st.divider()

        st.subheader("📊  Skill Gap Analysis")

        st.write(
            st.session_state.professional_skill_gap
        )

    st.divider()

    if st.button(
        "⬅ Back to Professional Features",
        use_container_width=True
    ):

        st.session_state.page = "features"
        st.rerun()