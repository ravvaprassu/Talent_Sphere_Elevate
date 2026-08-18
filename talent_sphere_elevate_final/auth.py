import sqlite3
from database import connect_db


def register_user(full_name, email, phone, password, category):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users
    (full_name,email,phone,password,category)

    VALUES(?,?,?,?,?)
    """,

    (full_name,email,phone,password,category))

    conn.commit()
    conn.close()


def login_user(email,password):

    conn=connect_db()
    cursor=conn.cursor()

    cursor.execute("""

    SELECT * FROM users

    WHERE email=? AND password=?

    """,(email,password))

    user=cursor.fetchone()

    conn.close()

    return user

def save_professional_profile(
    full_name,
    email,
    phone,
    company,
    role,
    experience,
    current_salary,
    target_salary,
    qualification,
    skills,
    location,
    industry,
    linkedin,
    github
):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    INSERT OR REPLACE INTO professional_profile(

    full_name,
    email,
    phone,
    company,
    current_role,
    experience,
    current_salary,
    target_salary,
    qualification,
    skills,
    location,
    industry,
    linkedin,
    github

    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)

    """,

    (

    full_name,
    email,
    phone,
    company,
    role,
    experience,
    current_salary,
    target_salary,
    qualification,
    ",".join(skills),
    location,
    industry,
    linkedin,
    github

    ))

    conn.commit()
    conn.close()
def get_professional_profile(email):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM professional_profile

    WHERE email=?

    """,(email,))

    profile = cursor.fetchone()

    conn.close()

    return profile


def save_student_profile(
    full_name,
    email,
    phone,
    college,
    degree,
    branch,
    year,
    cgpa,
    skills,
    interests,
    career_goal
):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO student_profile(
            full_name,
            email,
            phone,
            college,
            degree,
            branch,
            year,
            cgpa,
            skills,
            interests,
            career_goal
        )
        VALUES(?,?,?,?,?,?,?,?,?,?,?)
    """, (
        full_name,
        email,
        phone,
        college,
        degree,
        branch,
        year,
        cgpa,
        ", ".join(skills),
        interests,
        career_goal
    ))

    conn.commit()
    conn.close()


