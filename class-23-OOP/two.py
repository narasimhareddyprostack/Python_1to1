class Emp:
    pass    #to Maintain dummy block


e1=Emp()

 
print(e1)             #<__main__.Emp object at 0x00000195CD1B80E0>
print(type(e1))       #<class '__main__.Emp'>
print(e1.__dict__)    #{}