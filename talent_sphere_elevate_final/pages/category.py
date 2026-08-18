import streamlit as st

def show_category():

    st.title("🎯 Select Your Career Category")
    st.write("Choose your current career stage to continue.")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🎓 High School")
        st.write("Career guidance and assessments.")
        if st.button("Continue", key="hs"):
            st.session_state.page = "high_school_profile"
            st.rerun()
    with col2:
        st.subheader("👨‍🎓 College")
        st.write("Resume, coding, AI coach, ATS, internships.")
        if st.button("Continue", key="college"):
            st.session_state.page = "student_profile"
            st.rerun()


    with col3:
        st.subheader("💼 Professional")
        st.write("Career growth and certifications.")
        if st.button("Continue", key="pro"):
            st.session_state.page = "profile"
            st.rerun()
    st.divider()

    if st.button("⬅ Logout"):
        st.session_state.page = "home"
        st.rerun()
    