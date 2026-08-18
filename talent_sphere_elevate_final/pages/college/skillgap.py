import streamlit as st
from AI.ai_helper import ask_gemini
import json
import re


def analyze_skill_gap(skills, career_goal, degree, branch):

    prompt = f"""
You are an expert college career advisor.

Analyze this student's current skills and career goal.

Degree: {degree}
Branch: {branch}
Current Skills: {", ".join(skills) if skills else "No skills provided"}
Career Goal: {career_goal if career_goal else "Not provided"}

Identify the most important skill gaps for the student's career goal.

Return ONLY valid JSON in this exact format:

{{
    "career_direction": "short career direction",
    "current_level": "Beginner / Intermediate / Advanced",
    "missing_skills": [
        "skill 1",
        "skill 2",
        "skill 3",
        "skill 4",
        "skill 5"
    ],
    "priority_skills": [
        "highest priority skill",
        "second priority skill",
        "third priority skill"
    ],
    "learning_plan": [
        "step 1",
        "step 2",
        "step 3",
        "step 4"
    ],
    "projects": [
        "project idea 1",
        "project idea 2",
        "project idea 3"
    ],
    "advice": "short personalized career advice"
}}
"""

    return ask_gemini(prompt)


def clean_json_response(response):

    response = response.strip()

    response = re.sub(r"```json", "", response)
    response = re.sub(r"```", "", response)

    return response.strip()


def show_student_skillgap():

    st.title("🧠 AI Skill Gap Analyzer")

    st.write(
        "Tell us about your current skills and career goal. "
        "AI will identify the skills you need to develop."
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

    career_goal = st.text_area(
        " Career Goal",
        placeholder="Example: I want to become a Data Scientist..."
    )

    st.divider()

    if st.button(
        " Analyze My Skill Gap",
        use_container_width=True
    ):

        if not career_goal.strip():

            st.warning("⚠️ Please enter your career goal.")

        else:

            with st.spinner("analyzing your skill gap..."):

                try:

                    result = analyze_skill_gap(
                        skills,
                        career_goal,
                        degree,
                        branch
                    )

                    result = clean_json_response(result)

                    data = json.loads(result)

                    st.session_state.skill_gap_analysis = data

                except json.JSONDecodeError:

                    st.error(
                        "❌ AI returned an unexpected response. "
                        "Please try again."
                    )

                except Exception as e:

                    st.error(
                        f"❌ Skill gap analysis failed: {str(e)}"
                    )

    if "skill_gap_analysis" in st.session_state:

        data = st.session_state.skill_gap_analysis

        st.divider()

        st.subheader(" Career Direction")

        st.info(
            data.get(
                "career_direction",
                "Not available"
            )
        )

        st.subheader(" Current Skill Level")

        st.write(
            data.get(
                "current_level",
                "Not available"
            )
        )

        st.subheader("❌ Missing Skills")

        for skill in data.get("missing_skills", []):
            st.write(f"• {skill}")

        st.subheader(" Priority Skills")

        for skill in data.get("priority_skills", []):
            st.write(f"• {skill}")

        st.subheader(" Recommended Learning Plan")

        for step in data.get("learning_plan", []):
            st.write(f"• {step}")

        st.subheader(" Recommended Projects")

        for project in data.get("projects", []):
            st.write(f"• {project}")

        st.subheader(" AI Career Advice")

        st.info(
            data.get(
                "advice",
                "No advice available."
            )
        )

    st.divider()

    if st.button(
        "⬅ Back to Student Features",
        use_container_width=True
    ):

        st.session_state.page = "student_features"
        st.rerun()