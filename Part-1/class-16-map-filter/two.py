enames=['rahul','sonia','priyanka']

#create new list of employees with upper case - 
#1. using map and 
#2. without map  - ['RAHUL', 'SONIA', 'PRIYANKA']

def changecase(name):
    return name.upper()

map_obj=map(changecase,enames)
new_names=list(map_obj)
print(enames)
print(new_names)