#without implementation login , hiding essential details
from abc import ABC,abstractmethod

class Bank(ABC):

    
    @abstractmethod
    def cal(self):
        pass


class Account(Bank):

    def cal(self):
        pass 


a1=Account()
print(a1)
print(a1.__dict__)