'''
Usage: fetch all users
Rest API URL:https://jsonplaceholder.typicode.com/users
Method Type: GET
Required Fields: None
Access Type:Public
'''
import requests

response=requests.get('https://jsonplaceholder.typicode.com/users')
users=response.json()
status_code=response.status_code

print(status_code)
print(type(users))