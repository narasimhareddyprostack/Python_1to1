emp={'eid':101,'ename':'Rahul','esal':45000.45}


keys=emp.keys()            #return all keys(list of keys)
values=emp.values()        #return all values(list of values)
items=emp.items()          #return all key and values(list of k,v)


for key in keys:
    print(key)

print("***")

for value in values:
    print(value)
    
print("***")

for key,value in items:
    print(key,":",value)