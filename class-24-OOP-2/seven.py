class Account:
    min__bal=500            #staitc Variable

    def open_account(self):
        print("Account Opened Successfully")

    def deposit(self):
        print("Amount Deposited Successfully")

    def withdrawl(self):
        print("Amount withdrawl Successfully")

a1=Account()
a2=Account()


a1.open_account()
a1.deposit()
a1.withdrawl()
print(a1.min__bal)