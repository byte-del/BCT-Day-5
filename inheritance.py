class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def showName(self):
        print("Name =", self.name)

    def showAge(self):
        print("Age =", self.age)

class Student(Person):
    def __init__(self, n, a, r):  # Corrected the constructor to accept name, age, and rollno
        super().__init__(n, a)  # Calling the constructor of the parent class
        self.rollno = r

    def showRollno(self):  # Corrected the method name
        print("Roll number =", self.rollno)

s1 = Student("Priti", 20, 100)  # Providing name, age, and rollno during instantiation
s1.showName()  # Accessing methods of the parent class
s1.showAge()
s1.showRollno()  # Accessing method of the child class
