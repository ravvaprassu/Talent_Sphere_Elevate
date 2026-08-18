import streamlit as st
from AI.ai_helper import ask_gemini


def show_internship_finder():

    st.title("💼  Internship Finder")

    st.write(
        "Tell us about your internship preferences and let AI "
        "suggest suitable opportunities and preparation steps."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        role = st.text_input(
            " Target Internship Role",
            placeholder="Example: Python Developer"
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

        skills = st.multiselect(
            "Your Skills",
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
                "Machine Learning",
                "Data Science",
                "Git",
                "Cloud Computing"
            ]
        )

    with col2:

        location = st.text_input(
            " Preferred Location",
            placeholder="Example: Hyderabad"
        )

        work_mode = st.selectbox(
            "Work Mode",
            [
                "Any",
                "Remote",
                "On-site",
                "Hybrid"
            ]
        )

        duration = st.selectbox(
            " Internship Duration",
            [
                "Any",
                "1 Month",
                "2 Months",
                "3 Months",
                "6 Months"
            ]
        )

    st.divider()

    if st.button(
        "🤖 Find Internships ",
        use_container_width=True
    ):

        if not role:
            st.warning("Please enter your target internship role.")
            return

        if not skills:
            st.warning("Please select at least one skill.")
            return

        prompt = f"""
You are an expert college internship and placement advisor.

Analyze the student's information below and suggest suitable
internship opportunities.

Student Information:

Target Role:
{role}

Branch:
{branch}

Skills:
{", ".join(skills)}

Preferred Location:
{location if location else "Any"}

Work Mode:
{work_mode}

Duration:
{duration}

Provide 5 realistic internship suggestions.

For each suggestion provide:

1. Internship role
2. Suitable company/domain type
3. Why it matches the student
4. Important required skills
5. Skills the student should improve
6. Preparation advice
7. Match percentage

Do not claim that these are currently open vacancies.
Present them as suitable internship opportunity types
the student should search and apply for.

Use clear headings and bullet points.
"""

        with st.spinner(
            " AI is finding suitable internship opportunities..."
        ):

            try:

                response = ask_gemini(prompt)

                st.session_state.internship_results = response

            except Exception as e:

                st.error(
                    f"❌ Internship analysis failed: {str(e)}"
                )

    if "internship_results" in st.session_state:

        st.divider()

        st.subheader("AI-Matched Internship Suggestions")

        st.write(
            st.session_state.internship_results
        )

    st.divider()

    if st.button("⬅ Back to Student Features", use_container_width=True):

        st.session_state.page = "student_features"
        st.rerun()