import streamlit as st
from auth import save_professional_profile


def show_profile():

    st.title("👤 Professional Profile")

    st.write("Complete your professional profile.")

    col1, col2 = st.columns(2)

    with col1:

        full_name = st.text_input("Full Name")

        email = st.text_input("Email")

        phone = st.text_input("Phone Number")

        company = st.text_input("Current Company")

        role = st.selectbox(
            "Current Role",
            [
                "Software Engineer",
                "Python Developer",
                "Java Developer",
                "Frontend Developer",
                "Backend Developer",
                "Full Stack Developer",
                "Data Analyst",
                "Data Scientist",
                "AI Engineer",
                "ML Engineer",
                "Cloud Engineer",
                "DevOps Engineer",
                "Cyber Security Analyst",
                "UI/UX Designer",
                "QA Engineer",
                "Project Manager",
                "Business Analyst"
            ]
        )

        experience = st.slider(
            "Years of Experience",
            0,
            25,
            1
        )

    with col2:

        current_salary = st.number_input(
            "Current Salary (LPA)",
            0.0,
            100.0,
            5.0
        )

        target_salary = st.number_input(
            "Target Salary (LPA)",
            0.0,
            200.0,
            10.0
        )

        qualification = st.selectbox(
            "Highest Qualification",
            [
                "B.Tech",
                "M.Tech",
                "B.Sc",
                "M.Sc",
                "MBA",
                "MCA",
                "PhD",
                "Other"
            ]
        )

        skills = st.multiselect(
            "Skills",
            [
                "Python",
                "Java",
                "C++",
                "SQL",
                "HTML",
                "CSS",
                "JavaScript",
                "React",
                "Node.js",
                "Git",
                "Docker",
                "AWS",
                "Azure",
                "Kubernetes",
                "Power BI",
                "Tableau",
                "Machine Learning",
                "Deep Learning",
                "NLP",
                "TensorFlow",
                "PyTorch"
            ]
        )

        location = st.text_input("Preferred Location")

        industry = st.selectbox(
            "Industry",
            [
                "IT",
                "Finance",
                "Healthcare",
                "Education",
                "Manufacturing",
                "Retail",
                "Telecom"
            ]
        )

        linkedin = st.text_input("LinkedIn Profile")

        github = st.text_input("GitHub Profile")

    st.divider()

    if st.button("💾 Save Profile", use_container_width=True):

        save_professional_profile(
            full_name,
            email,
            phone,
            company,
            role,
            experience,
            current_salary,
            target_salary,
            qualification,
            skills,
            location,
            industry,
            linkedin,
            github
        )

        st.success("✅ Profile Saved Successfully!")
        st.session_state.page = "features"
        st.rerun()