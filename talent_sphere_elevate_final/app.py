import streamlit as st
from pages.college.profile import show_student_profile
from pages.college.features import show_student_features
from pages.college.ats_check import show_ats_check
from pages.college.intern import show_internship_finder
from pages.college.skillgap import show_student_skillgap
from pages.college.ai_career_coach import show_student_ai
from pages.college.certificate import show_student_certificate
from pages.college.coding import show_coding
from pages.college.career_report import show_student_report
from pages.high_school.profile import show_high_school_profile
from pages.high_school.features import show_high_school_features
from pages.high_school.recommendations import show_recommendations
from pages.high_school.subject import show_subject
from pages.high_school.quiz import show_quiz
from pages.high_school.roadmap import show_roadmap
from pages.high_school.college import show_college
from pages.high_school.study import show_study
from pages.high_school.skillode import show_skillode
from pages.high_school.report import show_report as show_high_school_report
from pages.professional.report import show_report as show_professional_report
from pages.professional.profile import show_profile
from pages.professional.features import show_features
from pages.professional.salary import show_salary_growth
from pages.professional.skill_gap import show_skill_gap
from pages.professional.ai_coach import show_ai_coach
from pages.professional.promotion import show_promotion
from pages.professional.career_switch import show_career_switch
from pages.professional.certificate import show_certification
from pages.home import show_home
from pages.login import show_login
from pages.register import show_register
from pages.category import show_category

st.set_page_config(
    page_title="TalentSphere Elevate",
    page_icon="🎓",
    layout="wide"
)

# Session State
if "page" not in st.session_state:
    st.session_state.page = "home"

if "user" not in st.session_state:
    st.session_state.user = None
# Hide Streamlit automatic page navigation
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Custom Sidebar Navigation
with st.sidebar:

    st.title("TalentSphere")
    st.caption("Career Development Platform")

    st.divider()

    if st.button("Home", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

    if st.button("Login", use_container_width=True):
        st.session_state.page = "login"
        st.rerun()

    if st.button("Register", use_container_width=True):
        st.session_state.page = "register"
        st.rerun()

    if st.button("User Category", use_container_width=True):
        st.session_state.page = "category"
        st.rerun()

    st.divider()

    st.subheader("Switch Module")

    if st.button("High School", use_container_width=True):
        st.session_state.page = "high_school_profile"
        st.rerun()

    if st.button("College", use_container_width=True):
        st.session_state.page = "student_profile"
        st.rerun()

    if st.button("Working Professional", use_container_width=True):
        st.session_state.page = "profile"
        st.rerun()

    st.divider()

    if st.button("Logout", use_container_width=True):
        st.session_state.user = None
        st.session_state.page = "home"
        st.rerun()

# Navigation
if st.session_state.page == "home":
    show_home()

elif st.session_state.page == "login":
    show_login()

elif st.session_state.page == "register":
    show_register()

elif st.session_state.page == "category":
    show_category()
# Temporary placeholder pages
elif st.session_state.page == "high_school_profile":
    show_high_school_profile()

elif st.session_state.page == "high_school_features":
    show_high_school_features()
elif st.session_state.page == "high_school_recommendations":
    show_recommendations()
elif st.session_state.page == "high_school_subject":
    show_subject()
elif st.session_state.page == "high_school_quiz":
    show_quiz()
elif st.session_state.page == "high_school_roadmap":
    show_roadmap()
elif st.session_state.page == "high_school_college":
    show_college()
elif st.session_state.page == "high_school_study":
    show_study()
elif st.session_state.page == "high_school_skillode":
    show_skillode()
elif st.session_state.page == "high_school_report":
    show_high_school_report()

elif st.session_state.page == "student_profile":
    show_student_profile()
elif st.session_state.page == "student_features":
    show_student_features()
elif st.session_state.page == "ats_check":
    show_ats_check()
elif st.session_state.page == "intern":
    show_internship_finder()
elif st.session_state.page == "student_skillgap":
    show_student_skillgap()
elif st.session_state.page == "student_ai":
    show_student_ai()
elif st.session_state.page == "student_certificate":
    show_student_certificate()
elif st.session_state.page == "coding":
    show_coding()
elif st.session_state.page == "student_report":
    show_student_report()
elif st.session_state.page == "profile":
    show_profile()
elif st.session_state.page == "features":
    show_features()
elif st.session_state.page == "salary_growth":
    show_salary_growth()
elif st.session_state.page == "skill_gap":
    show_skill_gap()
elif st.session_state.page == "ai_coach":
    show_ai_coach()
elif st.session_state.page == "promotion":
    show_promotion()
elif st.session_state.page == "career_switch":
    show_career_switch()
elif st.session_state.page == "certification":
    show_certification()
elif st.session_state.page == "report":
    show_professional_report()

