#read csv file and Write emp data into new json file.
import csv, json
fp1=open("employee.csv", "r")
employee_csv_data=csv.reader(fp1)
employees=list(employee_csv_data)

#print(employees)
#Transform data for json file.
employee_json=[]
for employee in employees[1:]:
    employee_json.append({"empid":employee[0],
                          "ename":employee[1],
                          "gender":employee[2]})
    

fp2=open("employee.json", "w")
json.dump(employee_json,fp2)
print("New Employee Json File Created")

fp1.close()
fp2.close()