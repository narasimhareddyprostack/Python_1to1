#read employees.csv file and write all male employees in new male.csv
import csv 

fp1=open('employees.csv','r')
fp2=open('male.csv','w')
emp_csv_data=csv.reader(fp1)
employees=list(emp_csv_data)

male_employees=[]
for emp in employees[1:]:
    if emp[2]=="Male":
        male_employees.append([emp[0],emp[1],emp[2]])

print(len(male_employees))

csv_writer=csv.writer(fp2)
csv_writer.writerow(["empId","empName","gender"])
csv_writer.writerows(male_employees)

