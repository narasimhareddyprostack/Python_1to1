class Account:
    min_bal=5000

    def open_account(self):
        print("Account Opened successfully")
    def deposit(self):
        print("Amount Deposited")
    def withdrawl(self):
        print("Amount withdrawl")
    def get_bal(self):
        print("Bal low")
    

a1=Account()

print(a1.min_bal)
a1.open_account()
a1.deposit()
a1.withdrawl()
a1.get_bal()