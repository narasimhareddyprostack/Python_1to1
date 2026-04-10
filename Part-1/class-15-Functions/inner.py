def outer():

    print("inside outer function")

    def inner():
        print("inside inner funciton ") 

    return inner  #returning inner function ref



inner=outer()
inner()  
#how to invoke inner function from outside