class Test:

    def __init__(self):
        print("Constructor is special method")


    def m1(self):
        print("Instance Method")
    
    @classmethod
    def m2(cls):
        print("Class Method")
    
    @staticmethod
    def m3():
        print("Static Method")

t1=Test()
t2=Test()

t1.m1()
t1.m2()
t1.m3()