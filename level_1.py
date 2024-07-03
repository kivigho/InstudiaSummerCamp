# Syntax and Indentation
if 5 > 2:
    print("Five is greater than two!")
# 2
x = 5
y = "Hello, World!"
print(x)
print(y)
# 3
a = 10
b = 3
# Arithmetic Operators
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
# Comparison Operators
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
# Logical Operators
print(a > b and b < 5)
print(a > b or b > 5)
print(not(a > b))
# Assignment Operators
c = 5
c += 3
print(c)
# Conditional Statements
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")
# Loops
for i in range(5):
    print(i)
i = 0
while i < 5:
    print(i)
    i += 1
# Break, Continue, Pass
for i in range(10):
    if i == 5:
        break
    print(i)
# Defining and Calling Functions
def greet(name):
    return "Hello, " + name

print(greet("Alice"))
# Lambda Functions
add = lambda a, b: a + b
print(add(2, 3))
# Lists
my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list.append(6)
print(my_list)
# Tuples:
my_tuple = (1, 2, 3)
print(my_tuple)
# Dictionaries
my_dict = {"name": "Alice", "age": 25}
print(my_dict)
print(my_dict["name"])
# Sets
my_set = {1, 2, 3, 4, 5}
print(my_set)
# User Input
name = input("Enter your name: ")
print("Hello, " + name)

