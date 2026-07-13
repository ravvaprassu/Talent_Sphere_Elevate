import streamlit as st
st.set_page_config(
    page_title="TalentSphere Elevate",
    page_icon="🎓",
    layout="wide"
)
# Navigation
if "page" not in st.session_state:
    st.session_state.page = "home"
st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right,#EAF4FF,#FDFEFF);
}

/* Hide Streamlit Menu */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.title{
    text-align:center;
    font-size:52px;
    font-weight:bold;
    color:#0F52BA;
}

.subtitle{
    text-align:center;
    font-size:26px;
    color:#444;
    margin-top:-10px;
}

.desc{
    text-align:center;
    font-size:19px;
    color:#555;
    line-height:1.8;
}

.feature{
    background-color:white;
    padding:18px;
    border-radius:15px;
    box-shadow:0px 3px 12px rgba(0,0,0,0.15);
    text-align:center;
    font-size:18px;
    font-weight:600;
    color:#0F52BA;
}

.stButton>button{
    background:#0F52BA;
    color:white;
    width:100%;
    height:60px;
    font-size:22px;
    border-radius:12px;
    border:none;
}

.stButton>button:hover{
    background:#08306B;
    color:white;
}
h1, h2, h3, h4, h5 {
    color: #0F52BA !important;
}

label {
    color: #1F2937 !important;
    font-weight: 600 !important;
}
.stTextInput label,
.stCheckbox label {
    color: #1F2937 !important;
    font-size: 16px !important;
    font-weight: bold !important;
}

.stTextInput input {
    background-color: white !important;
    color: black !important;
}

.stCheckbox {
    color: black !important;
}

</style>
""", unsafe_allow_html=True)

if st.session_state.page == "home":
        
    st.markdown("<div class='title'>🎓 TalentSphere Elevate</div>", unsafe_allow_html=True)

    st.markdown("<div class='subtitle'>One Platform for Every Career Journey</div>", unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class='desc'>

    <b>TalentSphere Elevate</b> is an AI-powered career development platform
    designed to guide students and professionals at every stage of their career.

    Whether you're a High School Student exploring future careers,
    a College Student preparing for placements,
    or a Working Professional looking to upskill,
    TalentSphere Elevate provides personalized guidance,
    skill-gap analysis, AI-based recommendations,
    career roadmaps, and progress tracking — all in one place.

    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='feature'>
        🤖<br><br>
        AI Career Guidance
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='feature'>
        📊<br><br>
        Skill Gap Analysis
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='feature'>
        🎯<br><br>
        Personalized Roadmaps
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
        <div class='feature'>
        💻<br><br>
        Coding Practice
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class='feature'>
        📈<br><br>
        Progress Tracking
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
        <div class='feature'>
        🎓<br><br>
        Placement Preparation
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")


    st.markdown("##  Platform Highlights")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("User Categories", "3")
    c2.metric("AI Features", "10+")
    c3.metric("Career Paths", "50+")
    c4.metric("Learning Modules", "100+")

    st.write("")
    st.write("")


    if st.button("🚀 Get Started"):
        st.session_state.page = "register"
        st.rerun()
    st.write("")
    st.write("")

    st.markdown(
    "<center>© 2026 TalentSphere Elevate | Built with ❤️ using Streamlit</center>",
    unsafe_allow_html=True
    )

elif st.session_state.page == "register":

    st.markdown(
        "<h1 style='text-align:center;color:#0F52BA;'>Create Your Account</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;font-size:18px;color:#444;'>Join TalentSphere Elevate and start your career journey.</p>",
        unsafe_allow_html=True
    )

    st.write("")

    with st.container(border=True):

        fullname = st.text_input(
            "👤 Full Name",
            placeholder="Enter your full name"
        )

        email = st.text_input(
            "📧 Email Address",
            placeholder="Enter your email"
        )

        mobile = st.text_input(
            "📱 Mobile Number",
            placeholder="Enter your mobile number"
        )

        password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="Create a password"
        )

        confirm_password = st.text_input(
            "🔐 Confirm Password",
            type="password",
            placeholder="Confirm password"
        )

        terms = st.checkbox("I agree to the Terms & Conditions")

        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            if st.button("✅ Register", use_container_width=True):

                if fullname == "":
                    st.error("Please enter your Full Name.")

                elif email == "":
                    st.error("Please enter your Email Address.")

                elif mobile == "":
                    st.error("Please enter your Mobile Number.")

                elif password == "":
                    st.error("Please create a Password.")

                elif confirm_password == "":
                    st.error("Please confirm your Password.")

                elif password != confirm_password:
                    st.error("Passwords do not match.")

                elif not terms:
                    st.warning("Please accept the Terms & Conditions.")

                else:
                    st.success("🎉 Registration Successful!")

                    st.session_state.page = "login"
                    st.rerun()

        with col2:

            if st.button("⬅ Back to Home", use_container_width=True):

                st.session_state.page = "home"
                st.rerun()

    st.write("")

    st.markdown(
        """
        <center>
        <span style='font-size:16px;color:#444;'>
        Already have an account?
        <b> Login after registration.</b>
        </span>
        </center>
        """,
        unsafe_allow_html=True
    )

elif st.session_state.page == "login":

    st.markdown(
        "<h1 style='text-align:center;color:#0F52BA;'>🔐 Login</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;font-size:18px;color:#444;'>Welcome back! Login to continue your career journey.</p>",
        unsafe_allow_html=True
    )

    st.write("")

    with st.container(border=True):

        email = st.text_input(
            "📧 Email Address",
            placeholder="Enter your email"
        )

        password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="Enter your password"
        )

        remember = st.checkbox("Remember Me")

        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            if st.button("🔓 Login", use_container_width=True):

                if email == "" or password == "":
                    st.error("Please enter Email and Password.")

                else:
                    st.success("🎉 Login Successful!")

                    st.session_state.page = "selection"
                    st.rerun()

        with col2:

            if st.button("⬅ Back to Register", use_container_width=True):

                st.session_state.page = "register"
                st.rerun()

    st.write("")

    st.markdown(
        "<center><b>TalentSphere Elevate</b> | AI Powered Career Development Platform</center>",
        unsafe_allow_html=True
    )

elif st.session_state.page == "selection":

    st.markdown(
        "<h1 style='text-align:center;color:#0F52BA;'>👋 Welcome to TalentSphere Elevate</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center;color:#555;'>Select Your Career Stage</h3>",
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns(3)


    with col1:

        with st.container(border=True):

            st.markdown("##  High School Student")
            st.markdown("""
            <div style="
            color:#555;
            font-size:18px;
            line-height:1.6;
            text-align:center;
            ">
            Explore your interests, discover career paths and build a strong foundation for your future.
            </div>
            """, unsafe_allow_html=True)
            st.write("")

            if st.button(
                "Continue",
                key="school",
                use_container_width=True
            ):
                st.session_state.user_type = "High School Student"
                st.session_state.page = "student_profile"
                st.rerun()


    with col2:

        with st.container(border=True):

            st.markdown("## College Student")
            st.markdown("""
            <div style="
            color:#555;
            font-size:18px;
            line-height:1.6;
            text-align:center;
            ">
            "Prepare for placements, improve coding skills, and build an impressive resume."
            </div>
            """, unsafe_allow_html=True)

            st.write("")

            if st.button(
                "Continue",
                key="college",
                use_container_width=True
            ):  
                st.session_state.user_type = "College Student"
                st.info("College Student Module Coming Soon!")

    with col3:

        with st.container(border=True):

            st.markdown("##  Working Professional")
            st.markdown("""
            <div style="
            color:#555;
            font-size:18px;
            line-height:1.6;
            text-align:center;
            ">
            Upskill yourself, explore certifications, and achieve your career goals."
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            if st.button(
                "Continue",
                key="professional",
                use_container_width=True
            ):  
                st.session_state.user_type = "Working Professional"
                st.info("Professional Module Coming Soon!")

    st.write("")
    st.write("")

    if st.button("⬅ Logout", use_container_width=True):

        st.session_state.page = "home"
        st.rerun()
# ---------------- STUDENT PROFILE PAGE ---------------- #

elif st.session_state.page == "student_profile":

    st.markdown(
        "<h1 style='text-align:center;color:#0F52BA;'>👤 High School Student Profile</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h4 style='text-align:center;color:#555;'>Complete your profile to receive personalized AI career recommendations.</h4>",
        unsafe_allow_html=True
    )

    st.write("")

    # ---------------- Personal Information ---------------- #

    with st.container(border=True):

        st.subheader(" Personal Information")

        name = st.text_input(
            "Full Name",
            placeholder="Enter your full name"
        )

        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input(
                " Age",
                min_value=10,
                max_value=18,
                step=1
            )

        with col2:
            gender = st.selectbox(
                "Gender",
                ["Select", "Male", "Female", "Other"]
            )

        school = st.text_input(
            " School Name",
            placeholder="Enter school name"
        )

        student_class = st.selectbox(
            " Current Class",
            ["8th", "9th", "10th", "11th", "12th"]
        )

        city = st.text_input(
            " City",
            placeholder="Enter your city"
        )

    st.write("")

    # ---------------- Academic Information ---------------- #

    with st.container(border=True):

        st.subheader("📖 Academic Information")

        subject = st.selectbox(
            "❤️ Favorite Subject",
            [
                "Mathematics",
                "Science",
                "Computer Science",
                "English",
                "Social Studies",
                "Biology",
                "Physics",
                "Chemistry"
            ]
        )

        percentage = st.slider(
            "Current Percentage",
            0,
            100,
            75
        )

        coding = st.selectbox(
        " Do you know Coding?",
        ["Yes", "No"]
        )

        goal = st.text_input(
            " Dream Career",
            placeholder="Example: AI Engineer"
        )

    st.write("")

    # ---------------- Interests ---------------- #

    with st.container(border=True):

        st.subheader("Interests & Hobbies")

        hobbies = st.multiselect(
            "Select your interests",
            [
                "Technology",
                "Mathematics",
                "Science",
                "Reading",
                "Sports",
                "Music",
                "Dance",
                "Drawing",
                "Gaming",
                "Robotics",
                "Photography",
                "Public Speaking"
            ]
        )

    st.write("")
    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Save Profile", use_container_width=True):

            if (
                name == ""
                or school == ""
                or city == ""
                or gender == "Select"
            ):
                st.error("Please complete all required fields.")

            else:
                st.success("✅ Profile Saved Successfully!")

    with col2:

        if st.button("➡ Continue to Assessment", use_container_width=True):

            st.session_state.page = "assessment"
            st.rerun()

# ---------------- INTEREST ASSESSMENT PAGE ---------------- #

elif st.session_state.page == "assessment":

    st.markdown(
        "<h1 style='text-align:center;color:#0F52BA;'>🧠 Interest Assessment</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h4 style='text-align:center;color:#555;'>Answer these questions to discover the best career path for you.</h4>",
        unsafe_allow_html=True
    )

    st.progress(50)

    st.write("")

    q1 = st.selectbox(
        "1️⃣ Which subject do you enjoy the most?",
        ["Mathematics","Science","Computer Science","English","Social Studies"]
    )

    q2 = st.selectbox(
        "2️⃣ What do you enjoy doing in your free time?",
        ["Coding","Reading","Sports","Drawing","Gaming","Music"]
    )

    q3 = st.selectbox(
        "3️⃣ Do you enjoy solving logical problems?",
        ["Yes","No"]
    )

    q4 = st.selectbox(
        "4️⃣ Do you like working with computers?",
        ["Yes","No"]
    )

    q5 = st.selectbox(
        "5️⃣ Which activity excites you the most?",
        ["Building Apps","Designing","Teaching","Research","Business"]
    )

    q6 = st.selectbox(
        "6️⃣ What is your strongest skill?",
        ["Creativity","Communication","Problem Solving","Leadership","Programming"]
    )

    q7 = st.selectbox(
        "7️⃣ Do you enjoy science experiments?",
        ["Yes","No"]
    )

    q8 = st.selectbox(
        "8️⃣ Which environment do you prefer?",
        ["Office","Laboratory","Classroom","Remote Work","Outdoor"]
    )

    q9 = st.selectbox(
        "9️⃣ Do you like teamwork?",
        ["Yes","No"]
    )

    q10 = st.selectbox(
        "🔟 Which career sounds most interesting?",
        [
            "AI Engineer",
            "Software Developer",
            "Doctor",
            "Teacher",
            "Business Analyst",
            "Data Scientist"
        ]
    )

    st.write("")
    if st.button("🎯 Generate Career Recommendation", use_container_width=True):
        st.session_state.q1 = q1
        st.session_state.q2 = q2
        st.session_state.q3 = q3
        st.session_state.q4 = q4
        st.session_state.q5 = q5
        st.session_state.q6 = q6
        st.session_state.q7 = q7
        st.session_state.q8 = q8
        st.session_state.q9 = q9
        st.session_state.q10 = q10

        st.session_state.page = "recommendation"
        st.rerun()
elif st.session_state.page == "recommendation":


    career_scores = {
        "AI Engineer":0,
        "Software Developer":0,
        "Data Scientist":0,
        "Doctor":0,
        "Teacher":0,
        "Business Analyst":0
    }

    # ---------- Q1 ----------
    if st.session_state.q1=="Computer Science":
        career_scores["AI Engineer"]+=4
        career_scores["Software Developer"]+=4
        career_scores["Data Scientist"]+=2

    elif st.session_state.q1=="Mathematics":
        career_scores["Data Scientist"]+=4
        career_scores["AI Engineer"]+=2

    elif st.session_state.q1=="Science":
        career_scores["Doctor"]+=4

    elif st.session_state.q1=="English":
        career_scores["Teacher"]+=3

    elif st.session_state.q1=="Social Studies":
        career_scores["Business Analyst"]+=2

    # ---------- Q2 ----------
    if st.session_state.q2=="Coding":
        career_scores["Software Developer"]+=4
        career_scores["AI Engineer"]+=4

    elif st.session_state.q2=="Reading":
        career_scores["Teacher"]+=2

    elif st.session_state.q2=="Sports":
        career_scores["Business Analyst"]+=1

    elif st.session_state.q2=="Drawing":
        career_scores["Business Analyst"]+=2

    elif st.session_state.q2=="Gaming":
        career_scores["Software Developer"]+=2

    elif st.session_state.q2=="Music":
        career_scores["Teacher"]+=1

    # ---------- Q3 ----------
    if st.session_state.q3=="Yes":
        career_scores["AI Engineer"]+=2
        career_scores["Data Scientist"]+=2

    # ---------- Q4 ----------
    if st.session_state.q4=="Yes":
        career_scores["Software Developer"]+=3
        career_scores["AI Engineer"]+=3

    # ---------- Q5 ----------
    if st.session_state.q5=="Building Apps":
        career_scores["Software Developer"]+=4

    elif st.session_state.q5=="Designing":
        career_scores["Business Analyst"]+=2

    elif st.session_state.q5=="Teaching":
        career_scores["Teacher"]+=4

    elif st.session_state.q5=="Research":
        career_scores["Doctor"]+=3
        career_scores["Data Scientist"]+=2

    elif st.session_state.q5=="Business":
        career_scores["Business Analyst"]+=4
        # ---------- Q6 ----------

    if st.session_state.q6=="Programming":
        career_scores["AI Engineer"]+=4
        career_scores["Software Developer"]+=4

    elif st.session_state.q6=="Problem Solving":
        career_scores["Data Scientist"]+=3
        career_scores["AI Engineer"]+=2

    elif st.session_state.q6=="Communication":
        career_scores["Teacher"]+=3

    elif st.session_state.q6=="Leadership":
        career_scores["Business Analyst"]+=3

    elif st.session_state.q6=="Creativity":
        career_scores["Business Analyst"]+=2

    # ---------- Q7 ----------

    if st.session_state.q7=="Yes":
        career_scores["Doctor"]+=3

    # ---------- Q8 ----------

    if st.session_state.q8=="Laboratory":
        career_scores["Doctor"]+=3

    elif st.session_state.q8=="Office":
        career_scores["Business Analyst"]+=2

    elif st.session_state.q8=="Remote Work":
        career_scores["Software Developer"]+=2

    elif st.session_state.q8=="Classroom":
        career_scores["Teacher"]+=3

    # ---------- Q9 ----------

    if st.session_state.q9=="Yes":
        career_scores["Business Analyst"]+=2
        career_scores["Teacher"]+=2

    # ---------- Q10 ----------

    career_scores[st.session_state.q10]+=5

    sorted_careers=sorted(
        career_scores.items(),
        key=lambda x:x[1],
        reverse=True
    )

    top1=sorted_careers[0][0]
    top2=sorted_careers[1][0]
    top3=sorted_careers[2][0]

    score=sorted_careers[0][1]

    match=min(95,score*5+45)
    top1=sorted_careers[0][0]
    top2=sorted_careers[1][0]
    top3=sorted_careers[2][0]

    score=sorted_careers[0][1]

    match=min(95,score*5+45)

    st.session_state.recommended_career = top1
    st.markdown("""
    <div style="
    background:linear-gradient(90deg,#0F52BA,#4F8EF7);
    padding:35px;
    border-radius:18px;
    text-align:center;
    ">

    <h1 style="color:white;">
    🎉 Career Recommendation
    </h1>

    <h3 style="color:white;">
    Your Assessment has been Successfully Completed
    </h3>

    </div>
    """,unsafe_allow_html=True)

    st.write("")

    st.subheader("🏆 Overall Match")

    st.progress(match / 100)

    st.markdown(f"""
    <h1 style="
    text-align:center;
    color:#0F52BA;
    font-size:55px;
    font-weight:bold;
    ">
    {match}% Career Match
    </h1>
    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("🥇 Top Career Recommendations")

    c1,c2,c3=st.columns(3)

    with c1:
        st.markdown(f"""
        <div style="
        background:#D1FAE5;
        padding:20px;
        border-radius:15px;
        text-align:center;
        ">
        <h3>🥇</h3>
        <h3 style="color:#065F46;">{top1}</h3>
        </div>
        """,unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div style="
        background:#DBEAFE;
        padding:20px;
        border-radius:15px;
        text-align:center;
        ">
        <h3>🥈</h3>
        <h3 style="color:#1E40AF;">{top2}</h3>
        </div>
        """,unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div style="
        background:#FEF3C7;
        padding:20px;
        border-radius:15px;
        text-align:center;
        ">
        <h3>🥉</h3>
        <h3 style="color:#92400E;">{top3}</h3>
        </div>
        """,unsafe_allow_html=True)
    st.write("")

    st.subheader("💡 Why this Recommendation?")

    st.info(f"""

✔ Favorite Subject : {st.session_state.q1}

✔ Favorite Activity : {st.session_state.q2}

✔ Strong Skill : {st.session_state.q6}

✔ Preferred Environment : {st.session_state.q8}

These answers closely match the skills and interests required for **{top1}**.

""")

    skills={

    "AI Engineer":[
    "Python",
    "Machine Learning",
    "Deep Learning",
    "SQL",
    "Data Structures"
    ],

    "Software Developer":[
    "Python",
    "Java",
    "HTML",
    "CSS",
    "JavaScript"
    ],

    "Data Scientist":[
    "Python",
    "Pandas",
    "Statistics",
    "Machine Learning",
    "SQL"
    ],

    "Doctor":[
    "Biology",
    "Chemistry",
    "Patient Care",
    "Critical Thinking",
    "Communication"
    ],

    "Teacher":[
    "Presentation",
    "Leadership",
    "Communication",
    "Subject Knowledge",
    "Patience"
    ],

    "Business Analyst":[
    "Excel",
    "SQL",
    "Power BI",
    "Communication",
    "Problem Solving"
    ]

    }

    st.subheader("🛠 Skills You Should Learn")

    for skill in skills[top1]:
        st.success("✔ "+skill)

    st.write("")

    st.success(f"""
🎉 Congratulations!

Based on your complete assessment, **{top1}** is your best career match.

Keep learning and building your skills.

Click below to continue to your personalized dashboard.
""")

    st.write("")

    if st.button("📊 Continue to Dashboard",use_container_width=True):
        st.session_state.page="dashboard"
        st.rerun()
# ---------------- STUDENT DASHBOARD ---------------- #

elif st.session_state.page == "dashboard":

    career = st.session_state.recommended_career

    st.markdown("""
    <div style='
    background:linear-gradient(90deg,#0F52BA,#4F8EF7);
    padding:30px;
    border-radius:18px;
    text-align:center;
    '>

    <h1 style='color:white;'>🎓 Student Dashboard</h1>

    <h3 style='color:white;'>
    Welcome to TalentSphere Elevate
    </h3>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    c1, c2 = st.columns(2)

    with c1:

        st.container(border=True)

        st.subheader("👤 Student Profile")

        st.markdown(f"""
<div style="
background:white;
padding:20px;
border-radius:12px;
border:1px solid #D1D5DB;
color:black;
line-height:2;
">

<b>🎓 User Type:</b> High School Student<br>

<b>📖 Favourite Subject:</b> {st.session_state.q1}<br>

<b>🎮 Favourite Activity:</b> {st.session_state.q2}<br>

<b>💡 Strong Skill:</b> {st.session_state.q6}<br>

<b>🏫 Preferred Environment:</b> {st.session_state.q8}

</div>
""", unsafe_allow_html=True)

    with c2:

        st.container(border=True)

        st.subheader("🎯 AI Recommended Career")

        st.success(f"### {career}")

        st.progress(0.92)

        st.write("**Career Match : 92%**")

    st.write("")

    st.subheader("📈 Profile Completion")

    st.progress(0.80)

    st.success("Your profile is 80% complete.")

    st.write("")

    skills = {

        "AI Engineer": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "SQL",
            "Data Structures"
        ],

        "Software Developer": [
            "Python",
            "Java",
            "HTML",
            "CSS",
            "JavaScript"
        ],

        "Data Scientist": [
            "Python",
            "Pandas",
            "Statistics",
            "Machine Learning",
            "SQL"
        ],

        "Doctor": [
            "Biology",
            "Chemistry",
            "Patient Care",
            "Critical Thinking",
            "Communication"
        ],

        "Teacher": [
            "Communication",
            "Presentation",
            "Leadership",
            "Patience",
            "Subject Knowledge"
        ],

        "Business Analyst": [
            "Excel",
            "SQL",
            "Power BI",
            "Problem Solving",
            "Communication"
        ]
    }

    st.subheader("🛠 Skills to Learn")

    cols = st.columns(5)

    for i, skill in enumerate(skills[career]):
        cols[i].success(skill)

    st.write("")
    st.write("")

    st.subheader("📚 Learning Progress")

    st.progress(0.35)

    st.info("""
You have completed **35%** of your learning roadmap.

Complete more courses and projects to improve your career readiness.
""")

    st.write("")
    st.write("")
    st.subheader("🎯 Next Steps")

    st.success("✅ Explore different career options")
    st.success("✅ Improve your academic performance")
    st.success("✅ Learn basic coding and digital skills")
    st.success("✅ Participate in science & technology competitions")
    st.success("✅ Build a strong foundation for your future career")
    st.write("")
    st.write("")

    st.subheader("⚡ Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("🔄 Retake Assessment", use_container_width=True):
            st.session_state.page = "assessment"
            st.rerun()

    with col2:

        if st.button("👤 Edit Profile", use_container_width=True):
            st.session_state.page = "student_profile"
            st.rerun()

    with col3:

        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()

    st.write("")
    st.write("")

    st.markdown("---")

    st.markdown("""
    <div style="
    background:#F8FAFC;
    padding:20px;
    border-radius:15px;
    border-left:6px solid #0F52BA;
    ">

    <h3 style="color:#0F52BA;">
    🌟 Career Tip of the Day
    </h3>

    <p style="font-size:18px;color:#333;">
    Every expert was once a beginner.
    Keep learning, stay curious, and build one new skill every month.
    Small improvements today create great opportunities tomorrow.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown(
        """
        <center>
        <h4 style="color:#666;">
        © 2026 TalentSphere Elevate | AI Powered Career Guidance Platform
        </h4>
        </center>
        """,
        unsafe_allow_html=True
    )