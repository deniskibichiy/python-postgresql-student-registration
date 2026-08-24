import psycopg

def getConnection ():
    return psycopg.connect(
        host="localhost",
        dbname = "student",
        user="denis",
        password ="Denis"
        )

