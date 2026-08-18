import streamlit as st
from AI.ai_helper import ask_gemini


def generate_recommendations(profile):

    prompt = f"""
You are an expert high-school career counselor.

Analyze the following student's profile and provide personalized
career recommendations.

Student Profile:

Name: {profile.get("full_name", "")}
Age: {profile.get("age", "")}
Class: {profile.get("class_level", "")}
School: {profile.get("school", "")}
Education Board: {profile.get("board", "")}
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

Give personalized guidance based on the COMPLETE profile.

Recommend the top 5 suitable career paths.

For each career provide:

1. Career name
2. Suitability score out of 100
3. Why it matches the student
4. Important school subjects
5. Skills to develop
6. Recommended education path
7. Beginner activities or projects
8. Future opportunities

Also provide:

- Overall career direction
- Best-matching career
- Subjects to focus on
- Skills to start developing
- A practical 6-month action plan

Do not judge the student only by marks.
Consider interests, strengths, subjects and goals together.

Use simple language suitable for a high-school student.
Do not guarantee a particular career or job.
"""

    return ask_gemini(prompt)


def show_recommendations():

    st.title("🧭 AI Career Recommendation")

    st.write(
        "Discover career paths that match your academics, "
        "interests, strengths and goals."
    )

    st.divider()

    # Check whether profile exists
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

    # Profile summary
    st.subheader("👤 Your Profile")

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
            "Career Confidence",
            f'{profile.get("confidence", 0)}/10'
        )

    st.divider()

    st.subheader(" Your Interests")

    interests = profile.get("interests", [])

    if interests:
        st.write(" • ".join(interests))
    else:
        st.write("No interests provided.")

    st.subheader(" Favorite Subjects")

    subjects = profile.get("favorite_subjects", [])

    if subjects:
        st.write(" • ".join(subjects))
    else:
        st.write("No favorite subjects provided.")

    st.subheader(" Your Strengths")

    strengths = profile.get("strengths", [])

    if strengths:
        st.write(" • ".join(strengths))
    else:
        st.write("No strengths provided.")

    st.divider()

    if st.button(
        "🤖 Generate My Career Recommendations",
        use_container_width=True
    ):

        with st.spinner(
            "analyzing your profile..."
        ):

            try:

                result = generate_recommendations(profile)

                st.session_state.career_recommendations = result

            except Exception as e:

                st.error(
                    f"❌ Recommendation failed: {str(e)}"
                )

    # Display result
    if "career_recommendations" in st.session_state:

        st.divider()

        st.subheader(" Your Personalized Career Guidance")

        st.write(
            st.session_state.career_recommendations
        )

    st.divider()

    if st.button(
        "⬅ Back to High School Features",
        use_container_width=True
    ):

        st.session_state.page = "high_school_features"
        st.rerun()