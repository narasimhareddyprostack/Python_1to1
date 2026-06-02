#python not supported cyclic inheritance

#single inheritance
#mutliple Inheritance
#Mutlilevel Inheritance
#Hybird
#Hirarchacal Inheritance

class Test(Test):
    def m1(self):
        print("Test Class m1 method")

t1=Test()
t1.m1()