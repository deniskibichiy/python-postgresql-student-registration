from validators import (
    validate_age,
    validate_course,
    validate_email,
    validate_name
)
from db_connection import getConnection
from students import getStudents, add_student


def validate_student(name, course, email):
    return validate_name(name) and validate_email(email) and validate_course(course)

def createTable():
    with getConnection() as conn:
        with conn.cursor() as cur:
            cur.execute( "CREATE TABLE IF NOT EXISTS student(student_id SERIAL primary key, student_name VARCHAR(40), course VARCHAR(40), email VARCHAR(40));"
            )
            print("Table created successfully")



def createStudent(name, course, email):
    validate_student(name, course, email)
    with getConnection() as conn:
        add_student(conn,name,course, email)

createTable()
createStudent("Denis","denismutai5@gmail.com", "Computer Science")
print(getStudents())