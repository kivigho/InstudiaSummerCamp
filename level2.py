# List Comprehensions
squares = [x ** 2 for x in range(10)]
print(squares)
# Dictionary Comprehensions
my_dict = {x: x ** 2 for x in range(5)}
print(my_dict)
# 2 Modules and Packages

# Importing Modules:
import math
print(math.sqrt(16))
def greet(name):
    return "Hello, " + name

#2 Object-Oriented Programming (OOP)

# Classes and Objects
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

my_dog = Dog("Buddy", 3)
print(my_dog.name)
print(my_dog.bark())
# Basic Calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

while True:
    choice = input("Enter choice (add/subtract/multiply/divide): ")
    if choice in ('add', 'subtract', 'multiply', 'divide'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'add':
            print("Result:", add(num1, num2))
        elif choice == 'subtract':
            print("Result:", subtract(num1, num2))
        elif choice == 'multiply':
            print("Result:", multiply(num1, num2))
        elif choice == 'divide':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")
