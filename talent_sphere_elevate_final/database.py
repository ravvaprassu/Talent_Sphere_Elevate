import sqlite3

DB_NAME = "database/talentsphere.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_tables():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT,
        password TEXT NOT NULL,
        category TEXT
    )
    """)

    conn.commit()
    conn.close()


def create_professional_table():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS professional_profile(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        full_name TEXT,
        email TEXT UNIQUE,
        phone TEXT,

        company TEXT,
        current_role TEXT,
        experience INTEGER,

        current_salary REAL,
        target_salary REAL,

        qualification TEXT,
        skills TEXT,

        location TEXT,

        industry TEXT,

        linkedin TEXT,

        github TEXT

    )
    """)

    conn.commit()
    conn.close()


# Create all tables
create_tables()
create_professional_table()
def create_student_profile_table():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_profile(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        email TEXT,
        phone TEXT,
        college TEXT,
        degree TEXT,
        branch TEXT,
        year TEXT,
        cgpa REAL,
        skills TEXT,
        interests TEXT,
        career_goal TEXT
    )
    """)

    conn.commit()
    conn.close()
create_student_profile_table()