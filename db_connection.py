import psycopg

with psycopg.connect("host = localhost dbname = student user= denis password= Denis") as conn:
    print("Connection to database established")
