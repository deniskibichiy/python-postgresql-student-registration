from validators import (
    validate_age,
    validate_course,
    validate_email,
    validate_name
)

def validate_student(name, age, course, email):
    return validate_name(name) and validate_email(email) and validate_course(course) and validate_age(age)