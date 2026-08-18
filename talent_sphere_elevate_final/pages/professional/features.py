import streamlit as st

def show_features():

    st.title("💼 Working Professional")

    st.write("Choose a feature to continue.")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button("💰 Salary Growth Planner", use_container_width=True):
            st.session_state.page = "salary_growth"
            st.rerun()

        if st.button("🧠 Skill Gap Analyzer", use_container_width=True):
            st.session_state.page = "skill_gap"
            st.rerun()

        if st.button("🤖 AI Career Coach", use_container_width=True):
            st.session_state.page = "ai_coach"
            st.rerun()

        if st.button("📈 Promotion Readiness", use_container_width=True):
            st.session_state.page = "promotion"
            st.rerun()

    with col2:

        if st.button("🔄 Career Switch Planner", use_container_width=True):
            st.session_state.page = "career_switch"
            st.rerun()

        if st.button("📜 Certification Advisor", use_container_width=True):
            st.session_state.page = "certification"
            st.rerun()


        if st.button("📄 Career Report", use_container_width=True):
            st.session_state.page = "report"
            st.rerun()

        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()