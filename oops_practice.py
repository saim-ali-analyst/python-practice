# ==========================================
#   OOP Practice — All Concepts in One File
#   Author: Saim Ali
# ==========================================

# --------------------------------------------------
#   1. BASIC CLASS
# --------------------------------------------------
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def show_info(self):
        print(f"Name: {self.name}, Roll No: {self.rollno}")


# --------------------------------------------------
#   2. CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES
# --------------------------------------------------
class College:
    college_name = "Govt College Mardan"      # class attribute (shared)

    def __init__(self, student_name):
        self.student_name = student_name        # instance attribute (unique)


# --------------------------------------------------
#   3. ENCAPSULATION (private attributes)
# --------------------------------------------------
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance                # private

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"Balance: {self.__balance}")


# --------------------------------------------------
#   4. MAGIC METHODS
# --------------------------------------------------
class Money:
    def __init__(self, rupees, paisa):
        self.rupees = rupees
        self.paisa = paisa

    def __add__(self, other):
        total_paisa = self.paisa + other.paisa
        total_rupees = self.rupees + other.rupees
        if total_paisa >= 100:
            total_rupees += total_paisa // 100
            total_paisa = total_paisa % 100
        return Money(total_rupees, total_paisa)

    def __str__(self):
        return f"Rs. {self.rupees}.{self.paisa:02d}"


# --------------------------------------------------
#   5. SINGLE INHERITANCE
# --------------------------------------------------
class Animal:
    def sound(self):
        print("Some animal sound")


class Dog(Animal):
    def sound(self):
        print("Woof!")


# --------------------------------------------------
#   6. METHOD OVERRIDING + super()
# --------------------------------------------------
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def greet(self):
        super().greet()
        print(f"I earn {self.salary}")


# --------------------------------------------------
#   7. MULTILEVEL INHERITANCE
# --------------------------------------------------
class Human:
    def __init__(self, name):
        self.name = name


class StudentHuman(Human):
    def __init__(self, name, rollno):
        super().__init__(name)
        self.rollno = rollno


class CollegeStudent(StudentHuman):
    def __init__(self, name, rollno, major):
        super().__init__(name, rollno)
        self.major = major


# --------------------------------------------------
#   8. MULTIPLE INHERITANCE
# --------------------------------------------------
class Teacher:
    def teach(self):
        print("Teaching...")


class Researcher:
    def research(self):
        print("Researching...")


class Professor(Teacher, Researcher):
    pass


# --------------------------------------------------
#   9. POLYMORPHISM (method overriding)
# --------------------------------------------------
class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# --------------------------------------------------
#   10. ABSTRACTION (ABC)
# --------------------------------------------------
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starting...")



# ==================================================
#   TESTING ALL CONCEPTS
# ==================================================
print("=" * 50)
print("   OOP PRACTICE — SAIM ALI")
print("=" * 50)

# 1. Basic class
print("\n--- 1. Basic Class ---")
s = Student("Saim", 101)
s.show_info()

# 2. Class vs instance attributes
print("\n--- 2. Class vs Instance Attributes ---")
c = College("Saim")
print(f"College: {College.college_name}")
print(f"Student: {c.student_name}")

# 3. Encapsulation
print("\n--- 3. Encapsulation ---")
account = BankAccount("Saim", 5000)
account.deposit(1000)
account.show_balance()

# 4. Magic methods
print("\n--- 4. Magic Methods ---")
m1 = Money(100, 50)
m2 = Money(200, 75)
print(f"{m1} + {m2} = {m1 + m2}")

# 5. Single inheritance
print("\n--- 5. Single Inheritance ---")
d = Dog()
d.sound()

# 6. Overriding + super()
print("\n--- 6. Method Overriding + super() ---")
e = Employee("Saim", 50000)
e.greet()

# 7. Multilevel inheritance
print("\n--- 7. Multilevel Inheritance ---")
cs = CollegeStudent("Saim", 101, "Computer Science")
print(f"Name: {cs.name}, Roll: {cs.rollno}, Major: {cs.major}")

# 8. Multiple inheritance
print("\n--- 8. Multiple Inheritance ---")
p = Professor()
p.teach()
p.research()

# 9. Polymorphism
print("\n--- 9. Polymorphism ---")
shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    print(f"Area: {shape.area()}")

# 10. Abstraction
print("\n--- 10. Abstraction ---")
car = Car()
car.start()

print("\n" + "=" * 50)
print("   ALL CONCEPTS TESTED SUCCESSFULLY")
print("=" * 50)