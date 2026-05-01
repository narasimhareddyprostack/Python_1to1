import mysql.connector
dbcon=None 
cursor=None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='7am')
    cursor=dbcon.cursor()
    sql_st='''
            CREATE table employees(
            eid int,
            ename VARCHAR(32),
            esal float,
            loc VARCHAR(32)
            );
            ''' 
    cursor.execute(sql_st)
    dbcon.commit()
    print("New Table Created Successfully!")
except mysql.connector.Error as err:
    print(err)

finally:
    cursor.close()
    dbcon.close()