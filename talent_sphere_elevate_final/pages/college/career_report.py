import streamlit as st
from AI.ai_helper import ask_gemini


def generate_career_report(
    degree,
    branch,
    year,
    cgpa,
    skills,
    interests,
    career_goal
):

    prompt = f"""
You are an expert college placement and career advisor.

Create a personalized career readiness report for this student.

Student Profile:
Degree: {degree}
Branch: {branch}
Year: {year}
CGPA: {cgpa}
Skills: {", ".join(skills) if skills else "No skills provided"}
Interests: {interests if interests else "Not provided"}
Career Goal: {career_goal if career_goal else "Not provided"}

Analyze the student's overall career readiness.

Include:

1. Career direction
2. Current strengths
3. Skill gaps
4. Resume and project recommendations
5. Internship readiness
6. Placement preparation
7. Recommended learning areas
8. A practical 6-month roadmap
9. Overall readiness rating out of 100
10. Personalized final advice

Be realistic and specific. Do not give a generic report.
"""


    return ask_gemini(prompt)


def show_student_report():

    st.title("📊 AI Career Report")

    st.write(
        "Generate a personalized career readiness report "
        "based on your academic profile, skills and career goals."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        degree = st.selectbox(
            " Degree",
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
            "Branch",
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

        cgpa = st.number_input(
            " CGPA",
            min_value=0.0,
            max_value=10.0,
            value=7.5,
            step=0.1
        )

    with col2:

        skills = st.multiselect(
            "Current Skills",
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
            " Areas of Interest",
            placeholder="Example: AI, Data Science, Web Development..."
        )

        career_goal = st.text_area(
            " Career Goal",
            placeholder="Example: I want to become a Data Scientist..."
        )

    st.divider()

    if st.button(
        " Generate Career Report",
        use_container_width=True
    ):

        if not career_goal.strip():

            st.warning(
                "⚠️ Please enter your career goal."
            )

        else:

            with st.spinner(
                " AI is preparing your career report..."
            ):

                try:

                    report = generate_career_report(
                        degree,
                        branch,
                        year,
                        cgpa,
                        skills,
                        interests,
                        career_goal
                    )

                    st.session_state.student_career_report = report

                except Exception as e:

                    st.error(
                        f"❌ Career report generation failed: {str(e)}"
                    )

    if st.session_state.get("student_career_report"):

        st.divider()

        st.subheader("Your AI Career Report")

        st.write(
            st.session_state.student_career_report
        )

    st.divider()

    if st.button(
        "⬅ Back to Student Features",
        use_container_width=True
    ):

        st.session_state.page = "student_features"
        st.rerun()