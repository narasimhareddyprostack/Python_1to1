import mysql.connector
from mysql.connector import Error
def create_table():
    try:
        with mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='7am'
        ) as dbcon:

            with dbcon.cursor() as cursor:
                sql = """
                CREATE TABLE IF NOT EXISTS employees (
                    eid INT PRIMARY KEY,
                    ename VARCHAR(32) NOT NULL,
                    esal FLOAT,
                    loc VARCHAR(32)
                );
                """
                cursor.execute(sql)

            dbcon.commit()
            print("Table created successfully (or already exists)!")

    except Error as err:
        print(f"Error: {err}")

create_table()