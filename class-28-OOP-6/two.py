from abc import ABC,abstractmethod

class Test(ABC):
    @abstractmethod
    def m1(self):
        pass


t1=Test()
print(t1)
print(t1.__dict__)