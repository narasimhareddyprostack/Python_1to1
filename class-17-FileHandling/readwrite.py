#read data.txt and write data into new file ie user.txt


fp1=open('data.txt','r')
data=fp1.read()

fp2=open('user.txt','w')

fp2.write(data)
print("New File Created")