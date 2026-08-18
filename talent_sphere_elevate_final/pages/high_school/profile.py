import streamlit as st


def show_high_school_profile():

    st.title("🎓 High School Student Profile")

    st.write(
        "Complete your profile to receive personalized career guidance."
    )

    st.divider()

    # Basic Information
    st.subheader("👤 Basic Information")

    col1, col2 = st.columns(2)

    with col1:

        full_name = st.text_input("Full Name")

        email = st.text_input("Email")

        age = st.number_input(
            "Age",
            min_value=10,
            max_value=20,
            value=15
        )

        school = st.text_input("School Name")

    with col2:

        class_level = st.selectbox(
            " Class",
            ["8th", "9th", "10th", "11th", "12th"]
        )

        location = st.text_input(" Location")

        board = st.selectbox(
            " Education Board",
            [
                "CBSE",
                "ICSE",
                "State Board",
                "IB",
                "Other"
            ]
        )

    st.divider()

    # Academic Information
    st.subheader(" Academic Information")

    col1, col2 = st.columns(2)

    with col1:

        percentage = st.number_input(
            "Overall Percentage",
            min_value=0.0,
            max_value=100.0,
            value=70.0
        )

        favorite_subjects = st.multiselect(
            " Favorite Subjects",
            [
                "Mathematics",
                "Physics",
                "Chemistry",
                "Biology",
                "Computer Science",
                "English",
                "Social Studies",
                "Economics",
                "Accountancy",
                "Business Studies",
                "Art"
            ]
        )

    with col2:

        difficult_subjects = st.multiselect(
            "⚠️ Difficult Subjects",
            [
                "Mathematics",
                "Physics",
                "Chemistry",
                "Biology",
                "Computer Science",
                "English",
                "Social Studies",
                "Economics",
                "Accountancy",
                "Business Studies",
                "Art"
            ]
        )

    st.divider()

    # Interests
    st.subheader(" Interests")

    interests = st.multiselect(
        "What do you enjoy?",
        [
            " Technology",
            " Science",
            " Problem Solving",
            " Art & Design",
            " Writing",
            " Public Speaking",
            " Sports",
            " Music",
            " Reading",
            " Building Things",
            " Experiments",
            " Helping People",
            " Leadership",
            " Business"
        ]
    )

    st.divider()

    # Career Interests
    st.subheader(" Career Interests")

    career_interests = st.multiselect(
        "Which careers interest you?",
        [
            " AI & Technology",
            " Engineering",
            " Medicine",
            " Research",
            " Law",
            " Business",
            " Design",
            " Aviation",
            " Media",
            " Government Services",
            " Software Development",
            " Data Science",
            " Teaching",
            " Not Sure Yet"
        ]
    )

    st.divider()

    # Strengths
    st.subheader(" Your Strengths")

    strengths = st.multiselect(
        "What are you good at?",
        [
            "Problem Solving",
            "Creativity",
            "Communication",
            "Leadership",
            "Teamwork",
            "Logical Thinking",
            "Critical Thinking",
            "Programming",
            "Writing",
            "Presentation",
            "Time Management",
            "Learning Quickly"
        ]
    )

    st.divider()

    # Future Goal
    st.subheader("Future Goal")

    career_goal = st.text_area(
        "Tell us about your future goal",
        placeholder=(
            "Example: I want to become an AI Engineer "
            "and study Computer Science."
        )
    )

    confidence = st.slider(
        " How confident are you about your career choice?",
        1,
        10,
        5
    )

    st.divider()

    if st.button(
        "💾 Save Profile & Continue",
        use_container_width=True
    ):

        # Store profile temporarily in session
        st.session_state.high_school_profile = {
            "full_name": full_name,
            "email": email,
            "age": age,
            "school": school,
            "class_level": class_level,
            "location": location,
            "board": board,
            "percentage": percentage,
            "favorite_subjects": favorite_subjects,
            "difficult_subjects": difficult_subjects,
            "interests": interests,
            "career_interests": career_interests,
            "strengths": strengths,
            "career_goal": career_goal,
            "confidence": confidence
        }

        st.success("✅ Profile saved successfully!")

        st.session_state.page = "high_school_features"
        st.rerun()