emp={'eid':101,'ename':'Rahul','esal':45000.45}


#how to read dict values
print(emp['eid'])    #101
print(emp['ename'])  #Rahul
print(emp['esal'])   #45000.45
#print(emp['location']) #KeyError

print("***using get Method")
print(emp.get('eid'))      #101
print(emp.get('ename'))
print(emp.get('esal'))      #45000.45
print(emp.get('location'))  #None

#dict.get() method return value of specified key.
#if key is not present it return None