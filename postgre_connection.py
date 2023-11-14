import psycopg2
from psycopg2.extras import DictCursor

db_params = {
    "dbname": "polban4",
    "user": "postgres",
    "password": "MustoBeStruggle05",
    "host": "localhost",
    "port": "5432",
    }
    
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor(cursor_factory= DictCursor)

    cursor.execute("select nim, nama from mhs")
    data = cursor.fetchall()

    for row in data:
        print(dict(row)['nama'])

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL: ", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")