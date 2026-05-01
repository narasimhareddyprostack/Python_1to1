import mysql.connector
from mysql.connector import Error
def insert_one_row():
    try:
        with mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='7am'
        ) as dbcon:

            with dbcon.cursor() as cursor:
                sql = """
                INSERT INTO employees VALUES(1, "JOHN", 50000.45, "Capitol");
                """
                cursor.execute(sql)

            dbcon.commit()
            print("Row Inserted successfully !")

    except Error as err:
        print(f"Error: {err}")

insert_one_row()