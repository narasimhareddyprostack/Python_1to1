class Account:
   acc_id=100            #variable


   #Method
   def open_account():
      print('Account opened successfully')


a1=Account()
a2=Account()
print(a1.__dict__)
print(a2.__dict__)
print(Account.__dict__)