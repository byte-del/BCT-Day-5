class Test:
    i=10 #global variable so its shared across all instances

    def __init__(self): #default constructor / function which can passed without parameters
        print("init")
    
    def f1(self): #instance method which when called will print hello
        print("hello")

t1=Test()
t2=Test()
t3=Test()
