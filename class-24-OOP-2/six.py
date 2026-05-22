class Test:

    def __init__(self):
        print("constructor method")
    
    def m1(self):
        print("Instance Method")

    @classmethod
    def m2(cls):
        print("class Method")
    
    @staticmethod
    def m3():
        print("static Method")