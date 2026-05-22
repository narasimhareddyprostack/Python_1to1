class Account:
    min_bal=500                  #static variable

    def __init__(self,id,name):
        self.acc_id=id
        self.acc_name=name 
        self.acc_bal=0
    
    def deposit(self,amount):
        self.acc_bal=self.acc_bal+amount 

    def withdrawl(self,amount):
        self.acc_bal=self.acc_bal-amount 

    
a1=Account(101,'AniTej')  #How to initlize object values
a2=Account(102,'Narasimha')

print(a1.__dict__)
print(a2.__dict__)

print(Account.__dict__)