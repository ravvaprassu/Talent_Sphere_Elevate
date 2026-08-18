import streamlit as st
from auth import login_user

def show_login():

    st.title("🔐 Login")
    st.write("Welcome back! Login to continue.")

    st.divider()

    left, center, right = st.columns([1,2,1])

    with center:

        st.markdown("## Login Account")

        email = st.text_input(
            "📧 Email Address",
            placeholder="Enter your email"
        )

        password = st.text_input(
            "🔑 Password",
            type="password",
            placeholder="Enter your password"
        )

        remember = st.checkbox("Remember Me")

        st.write("")

        login = st.button(
            "🔐 Login",
            use_container_width=True
        )

        st.write("")

        if st.button("📝 Create New Account", use_container_width=True):
            st.session_state.page = "register"
            st.rerun()

        if login:

            if email == "" or password == "":
                st.error("Please enter Email and Password.")

            else:

                user = login_user(email, password)

                if user:
                    st.success("🎉 Login Successful!")

                    st.session_state.user = user
                    st.session_state.page = "category"
                    st.rerun()

                else:
                    st.error("❌ Invalid Email or Password")