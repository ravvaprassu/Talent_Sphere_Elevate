import streamlit as st
from AI.ai_helper import ask_gemini


def get_certification_advice(
    role,
    experience,
    skills,
    target_role,
    industry
):

    prompt = f"""
You are an expert professional certification advisor.

Analyze this professional's profile:

Current Role: {role}
Experience: {experience} years
Current Skills: {", ".join(skills) if skills else "No skills provided"}
Target Role: {target_role}
Industry: {industry}

Recommend certifications that genuinely help this professional
move toward the target role.

Include:

1. Most relevant certifications
2. Why each certification is useful
3. Priority: High / Medium / Low
4. Skills each certification develops
5. Recommended learning order
6. Whether certification is actually necessary or experience/projects
   may be more valuable
7. A practical certification roadmap

Do NOT recommend certifications just because they are popular.
Keep recommendations relevant to the target role and current skills.
"""


    return ask_gemini(prompt)


def show_certification():

    st.title("📜  Certification Advisor")

    st.write(
        "Find certifications that are relevant to your current "
        "experience and target career."
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
            2
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

        target_role = st.text_input(
            " Target Role",
            placeholder="Example: Senior Cloud Engineer"
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
                "Leadership",
                "Communication",
                "Project Management"
            ]
        )

    st.divider()

    if st.button(
        "🤖 Find Best Certifications",
        use_container_width=True
    ):

        if not target_role.strip():

            st.warning("⚠️ Please enter your target role.")

        else:

            with st.spinner(
                "finding relevant certifications..."
            ):

                try:

                    result = get_certification_advice(
                        role,
                        experience,
                        skills,
                        target_role,
                        industry
                    )

                    st.session_state.professional_certification = result

                except Exception as e:

                    st.error(
                        f"❌ Certification analysis failed: {str(e)}"
                    )

    if st.session_state.get("professional_certification"):

        st.divider()

        st.subheader("📜 AI Certification Recommendations")

        st.write(
            st.session_state.professional_certification
        )

    st.divider()

    if st.button(
        "⬅ Back to Professional Features",
        use_container_width=True
    ):

        st.session_state.page = "features"
        st.rerun()