# python-postgresql-student-registration
A python CRUD project that integrates postgreSQL
## Features:
1. A function that takes the student details as argument and returns a boolean value of whether the student details are valid or not.
2. Validity checks are done on the name (string + character count), age (int), course (must be member of a list of courses), and email (string matching)
3. PostgreSQL integration such that once the student details are validated, the student is entered in the database. 
4. Ability to retrieve student details using python commands.
## Database connection
1. Update and upgrade `pip` and run the following
``bash
pip install --upgrade pip
pip install "psycopg[binary]"
```
