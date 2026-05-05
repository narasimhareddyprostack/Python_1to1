import pymongo

try:
    client=pymongo.MongoClient('mongodb://localhost:27017/')
    db=client['7am']
    emp_col=db['employees']
    employees=list(emp_col.find())
    #print(employees)

    for employee in employees:
        print(employee['ename'])

except Exception as err:
    print(err)