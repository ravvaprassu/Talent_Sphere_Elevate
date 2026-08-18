import streamlit as st


def show_high_school_features():

    st.title("🎓 High School Student")

    st.write(
        "Explore tools designed to help you discover your future."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🧭 AI Career Recommendation",
            use_container_width=True
        ):
            st.session_state.page = "high_school_recommendations"
            st.rerun()

        if st.button(
            "🎯 Subject Strength Analyzer",
            use_container_width=True
        ):
            st.session_state.page = "high_school_subject"
            st.rerun()

        if st.button(
            "🧠 Interest Quiz",
            use_container_width=True
        ):
            st.session_state.page = "high_school_quiz"
            st.rerun()

        if st.button(
            "🛣️ Career Roadmap",
            use_container_width=True
        ):
            st.session_state.page = "high_school_roadmap"
            st.rerun()

    with col2:

        if st.button(
            "🎓 College Explorer",
            use_container_width=True
        ):
            st.session_state.page = "high_school_college"
            st.rerun()

        if st.button(
            "📚 AI Study Planner",
            use_container_width=True
        ):
            st.session_state.page = "high_school_study"
            st.rerun()

        if st.button(
            "🏆 Skills & Coding Challenge",
            use_container_width=True
        ):
            st.session_state.page = "high_school_skillode"
            st.rerun()

        if st.button(
            "📊 Student Career Report",
            use_container_width=True
        ):
            st.session_state.page = "high_school_report"
            st.rerun()

    st.divider()

    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.user = None
        st.session_state.page = "home"
        st.rerun()