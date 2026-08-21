def getStudents(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM students")
        return cur.fetchall()

def add_student(conn, name, email):
    with conn.cursor as cur:
        cur.execute(
            "INSERT INTO students (name, email) VALUES (%s, %s)",
            (name, email)
        )