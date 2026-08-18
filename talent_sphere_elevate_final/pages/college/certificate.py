import streamlit as st
from AI.ai_helper import ask_gemini
import json
import re


def get_certifications(degree, branch, skills, career_goal):

    prompt = f"""
You are an expert college career and certification advisor.

Recommend useful certifications based on the student's profile.

Degree: {degree}
Branch: {branch}
Current Skills: {", ".join(skills) if skills else "No skills provided"}
Career Goal: {career_goal}

Recommend certifications that are genuinely relevant to the student's
career goal. Do not recommend random certifications.

Return ONLY valid JSON in this format:

{{
    "career_direction": "short career direction",
    "recommended_certifications": [
        {{
            "name": "certification name",
            "provider": "provider",
            "reason": "why this certification is useful",
            "priority": "High / Medium / Low"
        }}
    ],
    "learning_order": [
        "first certification or learning step",
        "second certification or learning step",
        "third certification or learning step"
    ],
    "advice": "short personalized certification advice"
}}
"""

    return ask_gemini(prompt)


def clean_json_response(response):

    response = response.strip()

    response = re.sub(r"```json", "", response)
    response = re.sub(r"```", "", response)

    return response.strip()


def show_student_certificate():

    st.title("📜  Certification Advisor")

    st.write(
        "Get AI-powered certification recommendations based on "
        "your career goal, degree and current skills."
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
        placeholder="Example: I want to become a Cloud Engineer..."
    )

    st.divider()

    if st.button(
        " Find Recommended Certifications",
        use_container_width=True
    ):

        if not career_goal.strip():

            st.warning("⚠️ Please enter your career goal.")

        else:

            with st.spinner(
                " AI is finding suitable certifications..."
            ):

                try:

                    result = get_certifications(
                        degree,
                        branch,
                        skills,
                        career_goal
                    )

                    result = clean_json_response(result)

                    data = json.loads(result)

                    st.session_state.student_certifications = data

                except json.JSONDecodeError:

                    st.error(
                        "❌ AI returned an unexpected response. "
                        "Please try again."
                    )

                except Exception as e:

                    st.error(
                        f"❌ Certification analysis failed: {str(e)}"
                    )

    if "student_certifications" in st.session_state:

        data = st.session_state.student_certifications

        st.divider()

        st.subheader("Career Direction")

        st.info(
            data.get(
                "career_direction",
                "Not available"
            )
        )

        st.subheader("📜 Recommended Certifications")

        certifications = data.get(
            "recommended_certifications",
            []
        )

        for cert in certifications:

            st.markdown(
                f"###  {cert.get('name', 'Certification')}"
            )

            st.write(
                f"**Provider:** {cert.get('provider', 'Not available')}"
            )

            st.write(
                f"**Priority:** {cert.get('priority', 'Not available')}"
            )

            st.write(
                f"**Why:** {cert.get('reason', 'Not available')}"
            )

            st.divider()

        st.subheader(" Suggested Learning Order")

        for step in data.get("learning_order", []):

            st.write(f"• {step}")

        st.subheader(" AI Advice")

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