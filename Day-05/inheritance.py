# inheritance problem 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")    

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")

s = Student("Alice", 20, "S12345")
s.display()

p= Person("Bob", 30)
p.display()
s.hello()
