import streamlit as st
from AI.ai_helper import ask_gemini


def analyze_salary(role, experience, current_salary, target_salary,
                   skills, industry, location):

    prompt = f"""
You are an expert career and salary growth advisor.

Analyze this professional's salary situation and create a realistic
career growth strategy.

Current Role: {role}
Experience: {experience} years
Current Salary: {current_salary} LPA
Target Salary: {target_salary} LPA
Skills: {", ".join(skills) if skills else "No skills provided"}
Industry: {industry}
Preferred Location: {location if location else "Not specified"}

Provide:

1. Current career position assessment
2. Whether the target salary is realistic
3. Skills needed to reach the target salary
4. Roles the professional should target
5. Actions to increase earning potential
6. A 6-month salary growth roadmap
7. Interview/job-switch preparation advice
8. Final personalized recommendation

Be realistic. Consider experience, skills, industry and location.
Do not guarantee a specific salary.

Give a practical and personalized answer.
"""

    return ask_gemini(prompt)


def show_salary_growth():

    st.title("💰  Salary Growth Planner")

    st.write(
        "Get an AI-powered strategy to improve your career "
        "and increase your earning potential."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        role = st.selectbox(
            "💼 Current Role",
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
                "UI/UX Designer",
                "QA Engineer",
                "Project Manager",
                "Business Analyst"
            ]
        )

        experience = st.slider(
            "Years of Experience",
            0,
            25,
            1
        )

        current_salary = st.number_input(
            " Current Salary (LPA)",
            0.0,
            100.0,
            5.0
        )

    with col2:

        target_salary = st.number_input(
            " Target Salary (LPA)",
            0.0,
            200.0,
            10.0
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

        location = st.text_input(
            " Preferred Location",
            placeholder="Example: Hyderabad"
        )

    skills = st.multiselect(
        "Current Skills",
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
            "PyTorch"
        ]
    )

    st.divider()

    if st.button(
        "🤖 Analyze My Salary Growth",
        use_container_width=True
    ):

        with st.spinner(
            "🤖 AI is analyzing your career and salary growth..."
        ):

            try:

                result = analyze_salary(
                    role,
                    experience,
                    current_salary,
                    target_salary,
                    skills,
                    industry,
                    location
                )

                st.session_state.salary_growth_result = result

            except Exception as e:

                st.error(
                    f"❌ Salary analysis failed: {str(e)}"
                )

    if "salary_growth_result" in st.session_state:

        st.divider()

        st.subheader("📊 AI Salary Growth Analysis")

        st.write(
            st.session_state.salary_growth_result
        )

    st.divider()

    if st.button(
        "⬅ Back to Professional Features",
        use_container_width=True
    ):

        st.session_state.page = "features"
        st.rerun()