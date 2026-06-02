class Parent:
    def __init__(self):
        print("Parent Class Constructor")
    def m1(self):
        print("Parnet Class m1 method-instance")
    def m2(self):
        print("Parent class m2 method - instance")

class Child(Parent):
    def __init__(self):
        #super().__init__()
        print("Child class constructor")
    def m3(self):
        print("Child class m3 method - instance")

c1=Child()
c1.m1()
c1.m2()
c1.m3()
