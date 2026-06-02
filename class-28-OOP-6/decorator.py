def smart_div(func):
    
    def inner(a,b):
        if b==0:
            print("Can't Divibe by zero")
        else:
            return func(a,b)
    return inner  

@smart_div
def cal_div(a,b):
    print(a/b) 

cal_div(10,5)   #2.0
cal_div(10,0)   #ZeroDivision Error

print("GM")     

'''
what is decorator?
Decorator is function, it take function as argument.
and modify existing functionaly , and return new function
'''