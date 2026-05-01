#Write a python script to read employee table data and print all employee names
import mysql.connector
from mysql.connector import Error


def read_employees():
    try:
        with mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='7am'
        ) as dbcon:

            with dbcon.cursor() as cursor: 
                sql_st=''' select *from employees '''
                cursor.execute(sql_st)
                employees=cursor.fetchall()

                for emp in employees:
                    print(emp)

    except Error as err:
        print(f"Error: {err}")

read_employees()