#write python script to read csv file and print all employee names:
import csv
fp=open('emp.csv','r')

csv_data=csv.reader(fp)
employees=list(csv_data)


for emp in employees[1:]:    #list slicing
    print(emp[1])
