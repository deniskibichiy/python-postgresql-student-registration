import re
def validate_name(name):
    """Validate that the name contains only letters and spaces."""
    return isinstance(name, str) and len(name.strip()) >= 2 and name.replace(" ", "").isalpha()
def validate_course(course):
    """Validate that a course has at least 2 characters."""
    return isinstance(course, str) and len(course.strip()) >= 2

def validate_email(email):
    """Validate email format."""
    if not isinstance(email, str):
        return False
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$" 
    return re.match(pattern, email) is not None
def validate_password(password):
    """
    Password must:
        Be at least 8 characters long
        Contain an uppercase letter
        Contain a lowercase letter
        Contain a number
    """
    if not isinstance(password, str):
        return False

    return (
        len(password) >= 8
        and any(char.isupper() for char in password)
        and any(char.islower() for char in password)
        and any(char.isdigit() for char in password)
    )

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


