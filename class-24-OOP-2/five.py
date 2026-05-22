class Account:
    min_bal = 500

    def __init__(self,id,name,bal):
        self.acc_id=id 
        self.acc_name=name 
        self.acc_bal=bal 

    def open_account(self):
        print("Account Opened")
    
    def deposit(self):
        print("Amount Deposited successfully")

a1=Account(101,'RG',5000)
a2=Account(102,'SG',10000)
a3=Account(103,'PG',15000)
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
print(Account.__dict__)


