fp=open('user.txt','r')

print(fp.name)            #user.txt
print(fp.mode)            #read
print(fp.readable())      #True
print(fp.writable())      #False 
      
print(fp.closed)          #False

fp.close()

print(fp.closed)