import streamlit as st
from AI.ai_helper import ask_gemini


def generate_college_guidance(profile, course, preferred_location):

    prompt = f"""
You are an expert education and college counselor.

Analyze this student's profile and provide personalized college
and course guidance.

Student Class: {profile.get("class_level", "")}
Academic Percentage: {profile.get("percentage", "")}

Favorite Subjects:
{", ".join(profile.get("favorite_subjects", []))}

Interests:
{", ".join(profile.get("interests", []))}

Strengths:
{", ".join(profile.get("strengths", []))}

Career Interests:
{", ".join(profile.get("career_interests", []))}

Future Goal:
{profile.get("career_goal", "")}

Student's Preferred Course:
{course}

Preferred Location:
{preferred_location}

Provide:

1. Suitable degree/course options
2. Suitable college types
3. Entrance exams they may need to consider
4. Important subjects to prepare
5. Skills to develop before college
6. How to shortlist colleges
7. What factors to compare:
   - Course quality
   - Fees
   - Location
   - Placements
   - Infrastructure
   - Faculty
   - Accreditation
8. A simple college-selection checklist
9. Suggested next steps

Do not claim that a particular college guarantees admission or a job.
Do not invent current fees, rankings or admission deadlines.
Use simple language suitable for a high-school student.
"""


    return ask_gemini(prompt)


def show_college():

    st.title("🎓 College Explorer")

    st.write(
        "Explore suitable courses and learn how to choose "
        "the right college for your future."
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
            "Board",
            profile.get("board", "N/A")
        )

    st.divider()

    st.subheader(" What do you want to study?")

    course = st.selectbox(
        "Select your preferred course area",
        [
            "Not Sure Yet",
            "Computer Science / IT",
            "Artificial Intelligence / Data Science",
            "Engineering",
            "Medicine",
            "Biotechnology",
            "Commerce / Finance",
            "Business / Management",
            "Law",
            "Design",
            "Architecture",
            "Arts / Humanities",
            "Pure Science",
            "Other"
        ]
    )

    preferred_location = st.text_input(
        " Preferred College Location",
        placeholder="Example: Hyderabad, Bangalore, Chennai, Delhi..."
    )

    st.divider()

    st.subheader(" Your Career Interests")

    career_interests = profile.get(
        "career_interests",
        []
    )

    if career_interests:

        for career in career_interests:
            st.write(f"• {career}")

    else:

        st.info(
            "No career interests selected in your profile."
        )

    st.divider()

    if st.button(
        "🤖 Explore My College & Course Options",
        use_container_width=True
    ):

        with st.spinner(
            "AI is preparing your education guidance..."
        ):

            try:

                result = generate_college_guidance(
                    profile,
                    course,
                    preferred_location
                )

                st.session_state.college_guidance = result

            except Exception as e:

                st.error(
                    f"❌ College guidance failed: {str(e)}"
                )

    if "college_guidance" in st.session_state:

        st.divider()

        st.subheader(
            " Your Personalized College Guidance"
        )

        st.write(
            st.session_state.college_guidance
        )

    st.divider()

    if st.button(
        "⬅ Back to High School Features",
        use_container_width=True
    ):

        st.session_state.page = "high_school_features"
        st.rerun()