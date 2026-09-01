def validate_name(name):
    return True

def validate_course(course):
    return True

def validate_email(email):
    return True
def validate_password(password):
    return True

def validate_age(age):
    return True


def validate_student(name, email, password):
    if validate_email(email) and validate_name(name) and validate_password(password):
        return True
    elif not validate_name(name):
        raise ValueError("Name must meet all the constraints")
    elif not validate_password(password):
        raise ValueError("Password must meet all the constraints")
    elif not validate_email(email):
        raise ValueError("Email must meet all the constraints")
    return False


