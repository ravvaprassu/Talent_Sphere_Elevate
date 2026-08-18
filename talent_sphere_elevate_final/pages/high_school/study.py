import streamlit as st
from AI.ai_helper import ask_gemini


def generate_study_plan(profile, study_hours, exam_goal):

    prompt = f"""
You are an expert high-school academic mentor.

Create a personalized study plan using the student's profile.

Class:
{profile.get("class_level", "")}

Percentage:
{profile.get("percentage", "")}

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

Available study time:
{study_hours} hours per day

Current Goal:
{exam_goal}

Create a practical and realistic study plan.

Include:

1. Daily study schedule
2. Weekly subject allocation
3. Extra focus for difficult subjects
4. Revision strategy
5. Practice/test strategy
6. Break and rest suggestions
7. Weekend plan
8. One-month improvement target
9. Tips to avoid procrastination
10. Simple progress tracking method

Do not create an unrealistic schedule.
Include adequate breaks and sleep.
Use simple language suitable for a high-school student.
"""


    return ask_gemini(prompt)


def show_study():

    st.title("📚 AI Study Planner")

    st.write(
        "Get a personalized study plan based on your subjects, "
        "career goals and available study time."
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

    st.subheader(" Your Academic Snapshot")

    col1, col2, col3 = st.columns(3)

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
            "Difficult Subjects",
            len(profile.get("difficult_subjects", []))
        )

    st.divider()

    st.subheader(" Study Preferences")

    study_hours = st.slider(
        "How many hours can you study each day?",
        min_value=1,
        max_value=12,
        value=3
    )

    exam_goal = st.text_area(
        " What is your current study goal?",
        placeholder=(
            "Example: I want to score above 90% in my final exams "
            "and improve my Mathematics."
        )
    )

    st.divider()

    st.subheader(" Your Subjects")

    favorite_subjects = profile.get(
        "favorite_subjects",
        []
    )

    difficult_subjects = profile.get(
        "difficult_subjects",
        []
    )

    if favorite_subjects:

        st.write(" Strong/Favorite Subjects")

        for subject in favorite_subjects:
            st.write(f"• {subject}")

    if difficult_subjects:

        st.write("⚠️ Subjects Needing More Attention")

        for subject in difficult_subjects:
            st.write(f"• {subject}")

    st.divider()

    if st.button(
        "🤖 Generate My Study Plan",
        use_container_width=True
    ):

        with st.spinner(
            "  creating your personalized study plan..."
        ):

            try:

                result = generate_study_plan(
                    profile,
                    study_hours,
                    exam_goal
                )

                st.session_state.study_plan = result

            except Exception as e:

                st.error(
                    f"❌ Study plan generation failed: {str(e)}"
                )

    if "study_plan" in st.session_state:

        st.divider()

        st.subheader("🗓️ Your Personalized Study Plan")

        st.write(
            st.session_state.study_plan
        )

    st.divider()

    if st.button(
        "⬅ Back to High School Features",
        use_container_width=True
    ):

        st.session_state.page = "high_school_features"
        st.rerun()