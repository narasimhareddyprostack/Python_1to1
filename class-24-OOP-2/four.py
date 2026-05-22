class Test:
    a=10            #class variable/static

    def m1(self):
        self.b=20  #instance 
        self.c=30  #instance

    def m2(self):
        d=40

t1=Test()

print(t1.__dict__)  #{}

t1.m1()
print(t1.__dict__)  #{}






