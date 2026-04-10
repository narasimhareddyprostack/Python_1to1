def user():

    print("inside outer function")

    def login():
        print("Login success") 

    def logout():
        print("Logout") 
    

user()

