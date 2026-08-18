import streamlit as st
from AI.ai_helper import ask_gemini


def generate_report(profile):

    prompt = f"""
You are an expert high-school career counselor.

Create a complete and personalized Student Career Report.

Student Information:
Name: {profile.get("full_name", "")}
Class: {profile.get("class_level", "")}
Age: {profile.get("age", "")}
School: {profile.get("school", "")}
Board: {profile.get("board", "")}
Percentage: {profile.get("percentage", "")}

Favorite Subjects:
{", ".join(profile.get("favorite_subjects", []))}

Difficult Subjects:
{", ".join(profile.get("difficult_subjects", []))}

Interests:
{", ".join(profile.get("interests", []))}

Career Interests:
{", ".join(profile.get("career_interests", []))}

Strengths:
{", ".join(profile.get("strengths", []))}

Future Goal:
{profile.get("career_goal", "")}

Career Confidence:
{profile.get("confidence", "")}/10

Create a complete student analysis.

Include these sections:

1.  Student Overview
2.  Academic Analysis
3.  Strength Analysis
4.  Interest Analysis
5.  Top Career Recommendations
6.  Recommended Education Paths
7.  Career Roadmap
8.  Skills to Develop
9.  Subjects to Focus On
10. Suggested Projects and Activities
11. Six-Month Action Plan
12. Final Career Guidance

Give practical and encouraging advice.

Do not judge the student only by marks.
Consider interests, strengths, motivation and goals.
Do not guarantee admission, jobs or career success.

Use simple language suitable for a high-school student.
"""


    return ask_gemini(prompt)


def show_report():

    st.title("📊 Student Career Report")

    st.write(
        "Get a complete AI-powered analysis of your academic profile, "
        "interests, strengths and future career direction."
    )

    st.divider()

    if "high_school_profile" not in st.session_state:

        st.warning(
            "⚠️ Please complete your High School Profile first."
        )

        if st.button(
            "🎓 Go to Profile",
            use_container_width=True
        ):
            st.session_state.page = "high_school_profile"
            st.rerun()

        return

    profile = st.session_state.high_school_profile

    st.subheader("👤 Student Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Class",
            profile.get("class_level", "N/A")
        )

    with col2:
        st.metric(
            "Percentage",
            f'{profile.get("percentage", 0)}%'
        )

    with col3:
        st.metric(
            "Interests",
            len(profile.get("interests", []))
        )

    with col4:
        st.metric(
            "Strengths",
            len(profile.get("strengths", []))
        )

    st.divider()

    st.subheader(" Academic Snapshot")

    favorite_subjects = profile.get(
        "favorite_subjects",
        []
    )

    difficult_subjects = profile.get(
        "difficult_subjects",
        []
    )

    if favorite_subjects:
        st.write(" Favorite Subjects:")
        st.write(", ".join(favorite_subjects))

    if difficult_subjects:
        st.write("⚠️ Subjects Needing Improvement:")
        st.write(", ".join(difficult_subjects))

    st.subheader(" Career Interests")

    career_interests = profile.get(
        "career_interests",
        []
    )

    if career_interests:
        st.write(", ".join(career_interests))
    else:
        st.info("No specific career interests selected.")

    st.divider()

    if st.button(
        "🤖 Generate Complete Career Report",
        use_container_width=True
    ):

        with st.spinner(
            "AI is preparing your complete career report..."
        ):

            try:

                result = generate_report(profile)

                st.session_state.student_career_report = result

            except Exception as e:

                st.error(
                    f"❌ Report generation failed: {str(e)}"
                )

    if "student_career_report" in st.session_state:

        st.divider()

        st.subheader(" Your Complete Career Report")

        st.write(
            st.session_state.student_career_report
        )

    st.divider()

    if st.button(
        "⬅ Back to High School Features",
        use_container_width=True
    ):

        st.session_state.page = "high_school_features"
        st.rerun()