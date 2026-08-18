import streamlit as st
from auth import save_student_profile
def show_student_profile():

    st.title("🎓 Student Profile")
    st.write("Complete your profile.")

    col1, col2 = st.columns(2)

    with col1:
        full_name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        college = st.text_input("College Name")

        degree = st.selectbox(
            "Degree",
            ["B.Tech", "B.E", "B.Sc", "BCA", "M.Tech", "MBA", "Other"]
        )

    with col2:
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
            "Current Year",
            ["1st Year", "2nd Year", "3rd Year", "4th Year"]
        )

        cgpa = st.number_input("CGPA", 0.0, 10.0, 7.5)

        skills = st.multiselect(
            "Skills",
            ["Python", "Java", "C", "C++", "SQL", "HTML", "CSS", "JavaScript", "React", "Node.js", "Git"]
        )

        interests = st.text_area("Areas of Interest")
        career_goal = st.text_area("Career Goal")
    st.divider()
    if st.button("💾 Save Profile", use_container_width=True):
        save_student_profile(
            full_name,
            email,
            phone,
            college,
            degree,
            branch,
            year,
            cgpa,
            skills,
            interests,
            career_goal
        )
        st.success("✅ Student Profile Saved Successfully!")
        st.session_state.page = "student_features"
        st.rerun()
    