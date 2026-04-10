#create
enames=["Rahul","Sonia","Priya"]
#index    0       1         2
#read list
print(enames)

#read list elments - using indexing
print(enames[0])
print(enames[1])
print(enames[2])  #Priya
#print(enames[8])  #IndexError:index out of range

#update
enames[0]="Rahul Gandhi"
print(enames)

#delete
del enames[0]
print(enames)