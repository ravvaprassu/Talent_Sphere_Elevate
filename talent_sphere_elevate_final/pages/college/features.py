import streamlit as st


def show_student_features():

    st.title("🎓 College Student")

    st.write("Choose a feature to continue.")

    st.divider()

    col1, col2 = st.columns(2)

    # =========================
    # LEFT COLUMN
    # =========================

    with col1:

        if st.button(
            "📄 Resume Analyzer",
            use_container_width=True
        ):
            st.session_state.page = "ats_check"
            st.rerun()

        if st.button(
            "💼 Internship Finder",
            use_container_width=True
        ):
            st.session_state.page = "intern"
            st.rerun()

        if st.button(
            "🧠 Skill Gap Analyzer",
            use_container_width=True
        ):
            st.session_state.page = "student_skillgap"
            st.rerun()

        if st.button(
            "🤖 AI Career Coach",
            use_container_width=True
        ):
            st.session_state.page = "student_ai"
            st.rerun()


    # =========================
    # RIGHT COLUMN
    # =========================

    with col2:

        if st.button(
            "📜 Certification Advisor",
            use_container_width=True
        ):
            st.session_state.page = "student_certificate"
            st.rerun()

        if st.button(
            "📊 Career Report",
            use_container_width=True
        ):
            st.session_state.page = "student_report"
            st.rerun()

        if st.button(
            "💻 Coding Practice",
            use_container_width=True
        ):
            st.session_state.page = "coding"
            st.rerun()

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):
            st.session_state.user = None
            st.session_state.page = "home"
            st.rerun()