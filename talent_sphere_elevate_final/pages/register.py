import streamlit as st
from auth import register_user

def show_register():

    st.title("📝 Create Your Account")
    st.write("Join TalentSphere Elevate and start your career journey.")

    st.divider()

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.markdown("## Register")

        full_name = st.text_input(
            "👤 Full Name",
            placeholder="Enter your full name"
        )

        email = st.text_input(
            "📧 Email Address",
            placeholder="Enter your email"
        )

        phone = st.text_input(
            "📱 Phone Number",
            placeholder="Enter your phone number"
        )

        password = st.text_input(
            "🔑 Password",
            type="password",
            placeholder="Create a password"
        )

        confirm_password = st.text_input(
            "🔒 Confirm Password",
            type="password",
            placeholder="Confirm your password"
        )

        category = st.selectbox(
            "🎓 Select Career Category",
            [
                "High School Student",
                "College Student",
                "Working Professional"
            ]
        )

        agree = st.checkbox("I agree to the Terms & Conditions")

        st.write("")

        register = st.button(
            "📝 Register",
            use_container_width=True
        )

        st.write("")

        if st.button("🔐 Already have an account? Login", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()

        if register:

            if (
                full_name == "" or
                email == "" or
                phone == "" or
                password == "" or
                confirm_password == ""
            ):
                st.error("Please fill in all fields.")

            elif password != confirm_password:
                st.error("Passwords do not match.")

            elif not agree:
                st.warning("Please accept the Terms & Conditions.")

            else:
                try:
                    register_user(
                        full_name,
                        email,
                        phone,
                        password,
                        category
                    )

                    st.success("🎉 Registration Successful!")

                    st.info("You can now login using your credentials.")

                except Exception:
                    st.error("Email already exists or registration failed.")