import pymongo 

try:
    client=pymongo.MongoClient('mongodb://localhost:27017/')
    db=client['7am']
    emp_col=db['employees']
   
    #insert many document into mongodb collection
    employees_data=[{"ename":"Urson","gender":"Male"},
                    {"ename":"Hulda","gender":"Female"},
                    {"ename":"Rose","gender":"Female"},
                    {"ename":"Orlando","gender":"Male"},
                    {"ename":"Clayson","gender":"Male"},
                    {"ename":"Orbadiah","gender":"Male"},
                    {"ename":"Carly","gender":"Male"},
                    {"ename":"Dionne","gender":"Female"},
                    {"ename":"Oates","gender":"Male"},
                    {"ename":"Leta","gender":"Female"}
                    ]
    emp_col.insert_many(employees_data)
    print("Many Employees Documents inserted successfully") 

except Exception as err:
    print(err)