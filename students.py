from db_connection import getConnection

def getStudents():
    with getConnection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM student")
            return cur.fetchall()

def add_student(conn, name, course, email):
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO student(student_name, email, course) VALUES (%s, %s, %s)
            """,
            (name, course, email)
        )