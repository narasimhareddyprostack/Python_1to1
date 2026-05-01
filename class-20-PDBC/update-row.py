import mysql.connector
dbcon=None 
cursor=None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='7am')
    cursor=dbcon.cursor()
    
    sql_st='''UPDATE employees SET ename = "Anitej" where eid = 1;''' 
    cursor.execute(sql_st)
    dbcon.commit()
    print("Data Updated successfully!")
    

    
except mysql.connector.Error as err:
    print(err)

finally:
    cursor.close()
    dbcon.close()