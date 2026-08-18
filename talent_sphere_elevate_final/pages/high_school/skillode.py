import streamlit as st
import random


def show_skillode():

    st.title("🏆 Skills & Coding Challenge")

    st.write(
        "Test your Python knowledge and solve simple coding problems."
    )

    st.divider()

    # =========================================================
    # QUESTION BANK
    # =========================================================

    mcq_bank = [
        {
            "q": "Which function displays output in Python?",
            "options": ["input()", "print()", "display()", "output()"],
            "answer": "print()"
        },
        {
            "q": "Which symbol is used to assign a value?",
            "options": ["==", "=", "!=", ":"],
            "answer": "="
        },
        {
            "q": "What is the output of print(2 + 3)?",
            "options": ["23", "5", "6", "Error"],
            "answer": "5"
        },
        {
            "q": "Which data type stores whole numbers?",
            "options": ["str", "float", "int", "list"],
            "answer": "int"
        },
        {
            "q": "Which symbol is used for a comment?",
            "options": ["//", "#", "/*", "--"],
            "answer": "#"
        },
        {
            "q": "What is the output of print(10 % 3)?",
            "options": ["1", "3", "0", "10"],
            "answer": "1"
        },
        {
            "q": "Which keyword is used for a condition?",
            "options": ["for", "if", "while", "def"],
            "answer": "if"
        },
        {
            "q": "Which loop is commonly used with a list?",
            "options": ["if", "for", "try", "def"],
            "answer": "for"
        },
        {
            "q": 'What is the output of print(len("Hello"))?',
            "options": ["4", "5", "6", "Error"],
            "answer": "5"
        },
        {
            "q": "Which keyword defines a function?",
            "options": ["function", "fun", "def", "define"],
            "answer": "def"
        },
        {
            "q": "Which data type stores text?",
            "options": ["int", "str", "float", "bool"],
            "answer": "str"
        },
        {
            "q": "What is 5 * 2?",
            "options": ["7", "10", "25", "52"],
            "answer": "10"
        },
        {
            "q": "Which operator checks equality?",
            "options": ["=", "==", "!=", ">"],
            "answer": "=="
        },
        {
            "q": "Which keyword is used to repeat while a condition is true?",
            "options": ["if", "for", "while", "def"],
            "answer": "while"
        },
        {
            "q": "What is the first index of a Python list?",
            "options": ["0", "1", "-1", "2"],
            "answer": "0"
        },
        {
            "q": "Which function gets input from the user?",
            "options": ["get()", "input()", "read()", "scan()"],
            "answer": "input()"
        },
        {
            "q": "What is the output of print(10 // 3)?",
            "options": ["3", "3.33", "1", "0"],
            "answer": "3"
        },
        {
            "q": "Which brackets are used to create a list?",
            "options": ["()", "{}", "[]", "<>"],
            "answer": "[]"
        },
        {
            "q": "Which value represents True or False?",
            "options": ["bool", "int", "str", "float"],
            "answer": "bool"
        },
        {
            "q": "What is the output of print(4 ** 2)?",
            "options": ["6", "8", "16", "12"],
            "answer": "16"
        }
    ]

    coding_bank = [
        {
            "title": "💻 Print Hello",
            "problem": "Write a Python program to print Hello World."
        },
        {
            "title": "➕ Add Two Numbers",
            "problem": "Write a program that takes two numbers and prints their sum."
        },
        {
            "title": "🔢 Even or Odd",
            "problem": "Write a program that checks whether a number is even or odd."
        },
        {
            "title": "📈 Largest of Two",
            "problem": "Write a program that takes two numbers and prints the larger number."
        },
        {
            "title": "🔢 Sum from 1 to N",
            "problem": "Write a program that takes N and prints the sum from 1 to N."
        },
        {
            "title": "🔤 Count Characters",
            "problem": "Write a program that takes a word and prints its length."
        },
        {
            "title": "🔄 Reverse a String",
            "problem": "Write a program that takes a string and prints it in reverse."
        },
        {
            "title": "🔢 Positive or Negative",
            "problem": "Write a program that checks whether a number is positive, negative or zero."
        },
        {
            "title": "✖️ Multiplication Table",
            "problem": "Write a program to print the multiplication table of a number."
        },
        {
            "title": "🔢 Count Even Numbers",
            "problem": "Write a program to count even numbers in a list."
        },
        {
            "title": "⭐ Largest in a List",
            "problem": "Write a program to find the largest number in a list."
        },
        {
            "title": "🔢 Factorial",
            "problem": "Write a program to find the factorial of a number."
        },
        {
            "title": "🔍 Search a Number",
            "problem": "Write a program to check whether a number exists in a list."
        },
        {
            "title": "➕ Sum of List",
            "problem": "Write a program to find the sum of all numbers in a list."
        },
        {
            "title": "🔢 Odd Numbers",
            "problem": "Write a program to print all odd numbers from 1 to N."
        }
    ]

    # =========================================================
    # RANDOM QUESTIONS
    # =========================================================

    if "selected_mcqs" not in st.session_state:

        st.session_state.selected_mcqs = random.sample(
            mcq_bank,
            10
        )

    if "selected_coding" not in st.session_state:

        st.session_state.selected_coding = random.sample(
            coding_bank,
            5
        )

    # =========================================================
    # MCQ SECTION
    # =========================================================

    st.header(" Part 1: Python Basics Quiz")

    st.info(
        "10 random questions are selected for this challenge."
    )

    answers = {}

    for i, question in enumerate(
        st.session_state.selected_mcqs
    ):

        st.subheader(
            f"Question {i + 1}"
        )

        st.write(question["q"])

        answers[i] = st.radio(
            "Choose your answer:",
            question["options"],
            key=f"mcq_{i}"
        )

    if st.button(
        "📝 Submit MCQ Quiz",
        use_container_width=True
    ):

        score = 0

        for i, question in enumerate(
            st.session_state.selected_mcqs
        ):

            if answers[i] == question["answer"]:
                score += 1

        st.session_state.mcq_score = score

    if "mcq_score" in st.session_state:

        st.success(
            f"Your MCQ Score: "
            f"{st.session_state.mcq_score}/10"
        )

    st.divider()

    # =========================================================
    # CODING SECTION
    # =========================================================

    st.header("Part 2: Coding Challenge")

    st.info(
        "5 random beginner coding problems have been selected."
    )

    for i, question in enumerate(
        st.session_state.selected_coding
    ):

        st.subheader(
            f"{i + 1}. {question['title']}"
        )

        st.write(
            question["problem"]
        )

        st.text_area(
            "Write your Python code:",
            height=150,
            key=f"code_{i}",
            placeholder="Write your Python code here..."
        )

    if st.button(
        " Submit Coding Challenge",
        use_container_width=True
    ):

        st.success(
            "✅ Your coding solutions have been submitted!"
        )

        st.info(
            "💡 Keep practicing and improve your solutions."
        )

    st.divider()

    # =========================================================
    # NEW CHALLENGE
    # =========================================================

    if st.button(
        " Try Another Challenge",
        use_container_width=True
    ):

        # Remove old questions
        st.session_state.pop(
            "selected_mcqs",
            None
        )

        st.session_state.pop(
            "selected_coding",
            None
        )

        st.session_state.pop(
            "mcq_score",
            None
        )

        st.rerun()

    st.divider()

    # =========================================================
    # BACK BUTTON
    # =========================================================

    if st.button(
        "⬅ Back to High School Features",
        use_container_width=True
    ):

        st.session_state.page = "high_school_features"
        st.rerun()