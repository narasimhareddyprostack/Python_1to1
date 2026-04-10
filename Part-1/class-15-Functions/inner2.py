def outer():

    print("inside outer function")

    def inner():
        print("inside inner funciton ") 

    return inner


inner=outer()
print(type(inner))  #<class,str>

#invoking inner function from outside
inner()
inner()
inner()
inner()
inner()