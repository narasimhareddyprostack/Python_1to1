import pymongo 

try:
    client=pymongo.MongoClient('mongodb://localhost:27017/')
    db=client['7am']
    emp_col=db['employees']
    #insert one document into mongodb collection
    emp_col.insert_one({"ename":"Rahul","esal":45000.45,"gender":"Male"})
    print("Document inserted successfully") 

except Exception as err:
    print(err)