import streamlit as st

def show_home():

    st.title("🎓 TalentSphere Elevate")
    st.subheader("AI Powered Career Development Platform")

    st.write("""
    Welcome to **TalentSphere Elevate**, an intelligent career guidance platform
    designed to support students and professionals throughout their career journey.

    Whether you are a High School Student, College Student,
    or Working Professional, TalentSphere provides personalized
    learning, skill analysis, resume guidance, interview preparation,
    and career recommendations.
    """)

    st.divider()

    st.header("🚀 Platform Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
### 🎓 High School Student

✔ Career Guidance

✔ Interest Assessment

✔ AI Recommendations

✔ Learning Roadmap
""")

    with col2:
        st.success("""
### 👨‍🎓 College Student

✔ Resume Builder

✔ ATS Resume Checker

✔ Coding Practice

✔ Skill Gap Analysis

✔ Mock Interview
""")

    with col3:
        st.warning("""
### 💼 Working Professional

✔ Career Growth

✔ Certifications

✔ AI Career Coach

✔ Industry Trends
""")

    st.divider()

    st.header("⭐ Why Choose TalentSphere?")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Users Supported", "3 Categories")

    with c2:
        st.metric("AI Modules", "10+")

    with c3:
        st.metric("Career Services", "20+")

    with c4:
        st.metric("Placement Focus", "100%")

    st.divider()

    st.header("📈 How It Works")

    st.success("1️⃣ Register an Account")
    st.success("2️⃣ Login Securely")
    st.success("3️⃣ Choose Your Career Category")
    st.success("4️⃣ Complete Assessment")
    st.success("5️⃣ Receive AI Recommendations")
    st.success("6️⃣ Track Your Progress")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔐 Login", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()

    with col2:
        if st.button("📝 Register", use_container_width=True):
            st.session_state.page = "register"
            st.rerun()

    st.divider()

    st.caption("© 2026 TalentSphere Elevate | AI Career Development Platform")