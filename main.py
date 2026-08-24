from validators import (
    validate_age,
    validate_course,
    validate_email,
    validate_name
)
from db_connection import getConnection
from students import getStudents, add_student


def validate_student(name, age, course, email):
    return validate_name(name) and validate_email(email) and validate_course(course) and validate_age(age)


with getConnection() as conn:
    add_student(conn, "Denis","denismutai5@gmail.com")
def createTable():
    with conn.cursor() as cur:
        cur.execute( "CREATE TABLE student(student_id serial primary key, student_name VARCHAR(40), course VARCHAR(40), email VARCHAR(40));"
        )
        print("Table created successfully")



def createStudent():
    with conn.cursor() as cur:

        cur.execute(
            "INSERT INTO test(num, data) VALUES (%s, %s)",
            (101, "abc'def"))

        cur.execute("SELECT * FROM test")

    print(cur.fetchone())

createTable();