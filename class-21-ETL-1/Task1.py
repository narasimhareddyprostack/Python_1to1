'''
Task 1:
Rest API Info:
usage: fetch all users
Rest API URL:https://jsonplaceholder.typicode.com/users
Method Type:GET
Access Type:Public
Invoke Rest API 
and Wriete uid,uname,email,city
into  a)new JSON File
      b)new CSV File 
      c)new user table - mysql

'''
import requests

#Extract data from Rest API
user_resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=user_resp.json()
print(users)