import streamlit as st
from AI.ai_helper import ask_gemini


def generate_roadmap(profile):

    prompt = f"""
You are an expert high-school career counselor.

Create a personalized career roadmap for this student.

Student Class: {profile.get("class_level", "")}
Academic Percentage: {profile.get("percentage", "")}

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

Future Goal:
{profile.get("career_goal", "")}

Create a realistic roadmap from the student's current class
towards higher education and a possible career.

Include:

1. Current stage
2. What to focus on right now
3. Class 10 preparation
4. Class 11-12 subject/stream guidance
5. Entrance exam options if relevant
6. Suitable undergraduate courses
7. Skills to develop
8. Projects and activities
9. Internship/exposure opportunities
10. College preparation
11. Long-term career direction
12. A 6-month action plan

If the student is not sure about a career, provide an
exploration roadmap instead of forcing one career.

Use simple language suitable for a high-school student.
Do not guarantee admission, jobs or career outcomes.
"""

    return ask_gemini(prompt)


def show_roadmap():

    st.title(" Career Roadmap")

    st.write(
        "Get a step-by-step roadmap from your current class "
        "towards your future education and career."
    )

    st.divider()

    if "high_school_profile" not in st.session_state:

        st.warning(
            " Please complete your High School Profile first."
        )

        if st.button(
            "Go to Profile",
            use_container_width=True
        ):
            st.session_state.page = "high_school_profile"
            st.rerun()

        return

    profile = st.session_state.high_school_profile

    st.subheader(" Your Current Stage")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Current Class",
            profile.get("class_level", "N/A")
        )

    with col2:
        st.metric(
            "Academic Score",
            f'{profile.get("percentage", 0)}%'
        )

    with col3:
        career_interests = profile.get(
            "career_interests",
            []
        )

        st.metric(
            "Career Interests",
            len(career_interests)
        )

    st.divider()

    st.subheader(" Your Career Interests")

    if career_interests:

        for career in career_interests:
            st.write(f"• {career}")

    else:

        st.info(
            "No specific career interests selected yet."
        )

    st.subheader(" Your Goal")

    goal = profile.get("career_goal", "")

    if goal:
        st.write(goal)
    else:
        st.info(
            "You haven't added a specific career goal yet."
        )

    st.divider()

    if st.button(
        "🤖 Generate My Career Roadmap",
        use_container_width=True
    ):

        with st.spinner(
            "AI is building your personalized roadmap..."
        ):

            try:

                result = generate_roadmap(profile)

                st.session_state.career_roadmap = result

            except Exception as e:

                st.error(
                    f"❌ Roadmap generation failed: {str(e)}"
                )

    if "career_roadmap" in st.session_state:

        st.divider()

        st.subheader("🗺️ Your Personalized Career Roadmap")

        st.write(
            st.session_state.career_roadmap
        )

    st.divider()

    if st.button(
        "⬅ Back to High School Features",
        use_container_width=True
    ):

        st.session_state.page = "high_school_features"
        st.rerun()