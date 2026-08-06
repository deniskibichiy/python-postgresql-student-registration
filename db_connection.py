import psycopg

conn = psycopg.connect(
    dbname="sql_practice",
    user="denis-kibichiy",   # or "postgres"
    password="your_password",
    host="localhost",
    port=5432,
)