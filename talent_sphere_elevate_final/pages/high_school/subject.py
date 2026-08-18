import streamlit as st
from AI.ai_helper import ask_gemini


def analyze_subjects(profile):

    prompt = f"""
You are an expert academic and career counselor for high-school students.

Analyze this student's academic profile:

Class: {profile.get("class_level", "")}
Percentage: {profile.get("percentage", "")}

Favorite Subjects:
{", ".join(profile.get("favorite_subjects", []))}

Difficult Subjects:
{", ".join(profile.get("difficult_subjects", []))}

Interests:
{", ".join(profile.get("interests", []))}

Strengths:
{", ".join(profile.get("strengths", []))}

Career Interests:
{", ".join(profile.get("career_interests", []))}

Provide a personalized Subject Strength Analysis.

Include:

1. Strongest subjects
2. Subjects needing improvement
3. Why the student may be strong in those subjects
4. Skills connected to their strongest subjects
5. Careers that match their subject strengths
6. Subjects they should focus on for their career goals
7. Practical improvement tips for difficult subjects
8. A simple weekly academic improvement plan

Do not judge the student only by marks.
Consider interests, strengths and career goals too.

Use simple language suitable for a high-school student.
"""


    return ask_gemini(prompt)


def show_subject():

    st.title("🎯 Subject Strength Analyzer")

    st.write(
        "Understand your strongest subjects, areas for improvement "
        "and how they connect to future careers."
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

    st.subheader(" Your Academic Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Class",
            profile.get("class_level", "N/A")
        )

    with col2:
        st.metric(
            "Overall Score",
            f'{profile.get("percentage", 0)}%'
        )

    with col3:
        st.metric(
            "Favorite Subjects",
            len(profile.get("favorite_subjects", []))
        )

    st.divider()

    st.subheader(" Favorite Subjects")

    favorite_subjects = profile.get(
        "favorite_subjects",
        []
    )

    if favorite_subjects:
        for subject in favorite_subjects:
            st.write(f"✅ {subject}")
    else:
        st.info("No favorite subjects were selected.")

    st.subheader("⚠️ Difficult Subjects")

    difficult_subjects = profile.get(
        "difficult_subjects",
        []
    )

    if difficult_subjects:
        for subject in difficult_subjects:
            st.write(f"⚠️ {subject}")
    else:
        st.success(
            " No difficult subjects were selected."
        )

    st.divider()

    if st.button(
        "🤖 Analyze My Subject Strengths",
        use_container_width=True
    ):

        with st.spinner(
            "analyzing your academic strengths..."
        ):

            try:

                result = analyze_subjects(profile)

                st.session_state.subject_analysis = result

            except Exception as e:

                st.error(
                    f"❌ Subject analysis failed: {str(e)}"
                )

    if "subject_analysis" in st.session_state:

        st.divider()

        st.subheader(
            "📚 Your Personalized Subject Analysis"
        )

        st.write(
            st.session_state.subject_analysis
        )

    st.divider()

    if st.button(
        "⬅ Back to High School Features",
        use_container_width=True
    ):

        st.session_state.page = "high_school_features"
        st.rerun()