import streamlit as st
from auth import get_professional_profile


def show_report():

    st.title("📄 TalentSphere Career Report")
    st.write("Complete AI Career Assessment Report")

    if st.session_state.user is None:
        st.error("Please Login First")
        return

    email = st.session_state.user[2]

    profile = get_professional_profile(email)

    if profile is None:
        st.error("Profile Not Found")
        return

    name = profile[1]
    company = profile[4]
    role = profile[5]
    experience = profile[6]
    current_salary = profile[7]
    target_salary = profile[8]
    qualification = profile[9]
    skills = profile[10]
    location = profile[11]
    industry = profile[12]

    skill_list = [s.strip() for s in skills.split(",")] if skills else []

    score = 0

    if experience >= 5:
        score += 30
    elif experience >= 3:
        score += 25
    elif experience >= 1:
        score += 15
    else:
        score += 10

    score += min(len(skill_list) * 5, 30)
    score += 20
    score += 20

    if score > 100:
        score = 100

    st.divider()

    st.subheader("👤 Professional Profile")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Name:**", name)
        st.write("**Company:**", company)
        st.write("**Role:**", role)
        st.write("**Experience:**", experience, "Years")
        st.write("**Qualification:**", qualification)

    with col2:
        st.write("**Current Salary:** ₹", current_salary, "LPA")
        st.write("**Target Salary:** ₹", target_salary, "LPA")
        st.write("**Industry:**", industry)
        st.write("**Location:**", location)

    st.divider()

    st.subheader("💻 Current Skills")

    for skill in skill_list:
        st.success(skill)

    st.divider()

    st.subheader("📊 Career Readiness Score")

    st.progress(score)

    st.metric("Overall Career Score", f"{score}%")

    st.divider()

    st.subheader("💰 Salary Growth")

    increase = target_salary - current_salary

    st.metric("Expected Salary Growth", f"₹ {increase} LPA")

    st.success("Continue upskilling to achieve your target salary.")

    st.divider()

    st.subheader("📈 Promotion Readiness")

    if score >= 85:
        st.success("Promotion Ready")

    elif score >= 70:
        st.info("Almost Ready")

    else:
        st.warning("Needs Improvement")

    st.divider()

    st.subheader("🧠 Skill Gap Summary")

    if len(skill_list) < 5:
        st.warning("Add more technical skills to strengthen your profile.")
    else:
        st.success("Strong technical skill profile.")

    st.divider()

    st.subheader("📜 Recommended Certifications")

    role_lower = role.lower()

    if "python" in role_lower:

        st.write(" AWS Cloud Practitioner")
        st.write(" Docker Essentials")
        st.write(" Azure AZ-900")

    elif "java" in role_lower:

        st.write(" Oracle Java")
        st.write(" Spring Boot")

    elif "data" in role_lower:

        st.write(" Google Data Analytics")
        st.write(" Microsoft Power BI")

    else:

        st.write(" PMP")
        st.write(" Scrum Master")

    st.divider()

    st.subheader("🤖 AI Career Recommendations")

    st.write("✅ Build real-world projects")
    st.write("✅ Update your resume every 3 months")
    st.write("✅ Improve LinkedIn profile")
    st.write("✅ Practice interview questions")
    st.write("✅ Learn trending technologies")
    st.write("✅ Network with professionals")

    st.divider()

    st.subheader("🎯 Final Career Verdict")

    if score >= 90:
        st.success("Excellent Profile. You are ready for high-paying opportunities.")

    elif score >= 75:
        st.success("Very Good Profile. Keep improving to reach your target salary.")

    elif score >= 60:
        st.info("Good Profile. Focus on upskilling and certifications.")

    else:
        st.warning("Needs Improvement. Follow the recommendations to grow faster.")

    st.divider()

    if st.button("🏠 Back to Features", use_container_width=True):
        st.session_state.page = "features"
        st.rerun()