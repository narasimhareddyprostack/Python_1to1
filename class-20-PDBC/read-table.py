import mysql.connector
dbcon=None 
cursor=None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='7am')
    cursor=dbcon.cursor()
    
    sql_st='''select *from employees''' 
    cursor.execute(sql_st)
    employees=cursor.fetchall()
    for emp in employees:
        print(emp)

    
except mysql.connector.Error as err:
    print(err)

finally:
    cursor.close()
    dbcon.close()