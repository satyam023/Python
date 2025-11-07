# A function is a block of reusable code that performs a specific task.
# It helps you organize, reuse, and reduce repetition in your code.

def greet(name="User"):
    print("Hello,", name)


# greet("Satyam")
# greet("Pikki")
# greet("Chikki")

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(7))

# n = int(input("Enter how many terms: "))
# a , b = 0 , 1
# print("Fibonacci series:")
# for i in range(n):
#     print(a, end=" ")
#     a ,b  = b,  a+b

# When Python sees:
#
# a, b = b, a + b
#
#
# It first evaluates the right-hand side (RHS) completely:
#
# temp = (b, a + b)
#
#
# Then it unpacks that tuple into the left-hand side (LHS):
#
# a = temp[0]
# b = temp[1]
#
#
# So effectively:
#
# a becomes the old value of b
#
# b becomes the sum of old a and old b

# Let’s say:
#
# a = 0
# b = 1
#
#
# Now run:
#
# a, b = b, a + b
#
#
# Step by step:
#
# RHS is evaluated first → (b, a + b) = (1, 0 + 1) = (1, 1)
#
# LHS then gets assigned:
#
# a = 1
#
# b = 1


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix)
cols = len(matrix[0])
# mat = [[0 for _ in range(rows)] for _ in range(cols)]
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         mat[j][i] = matrix[i][j]

# [ [expression for x in outer_loop ]for y in inner_loop ]


mat = [[matrix[j][i] for  j in range(rows)] for i in range(cols)]
print(matrix)
print(mat)
# [
# [1, 4],
# [2, 5],
# [3, 6]
# ]

# for row in mat:
#     row.reverse()

# [
# [4, 1],
# [5, 2],
# [6, 3]
# ]

# print(mat)

mat.reverse()

print(mat)
#  original
# [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# after column reverse
# [
# # [3, 6],
# # [2, 5],
# # [1, 4]
# # ]

result = [[f"{i}-{j}" for i in range(2) ] for j in range(3)]

# for row in result:
#     print(" | ".join(map(str, row)))

#***************************
# map(function, iterable)
# → applies the given function to each
# element of the iterable (like a list or tuple).
# map() returns an iterator (a lazy sequence).
# nums = [1, 2, 3, 4]
# result = map(str, nums)
# print(result)
# Output:
# <map object at 0x000001...>   # Not a list yet
# map() returns an iterator (a lazy sequence).
# To actually see the values:
# print(list(result))
# Output:
# ['1', '2', '3', '4']


# ********************************************************************



# 🧠 PYTHON FUNCTION NOTES (with examples)
# 1️⃣ Defining & Calling Functions
# 📘 Definition:
#
# A function is a block of reusable code that performs a specific task.
# It helps avoid repetition and makes programs modular.
#
# 📗 Syntax:
# def function_name(parameters):
#     # code block
#     return value  # optional
#
# 📙 Example:
# def greet(name):
#     print(f"Hello, {name}!")
#
# greet("Satyam")   # function call
#
#
# Output:
#
# Hello, Satyam!
#
# 2️⃣ Arguments — *args and **kwargs
# 🔹 Positional Arguments
#
# Normal arguments passed in order.
#
# def add(a, b):
#     return a + b
#
# print(add(2, 3))
#
#
# ➡️ Output: 5
#
# 🔹 Default Arguments
#
# Provide a default value if no value is passed.
#
# def greet(name="Guest"):
#     print(f"Hello, {name}!")
#
# greet()        # uses default
# greet("Satyam")
#
#
# ➡️ Output:
#
# Hello, Guest!
# Hello, Satyam!
#
# 🔹 Variable-length Arguments — *args
#
# Used when you don’t know how many positional arguments will be passed.
#
# def add_all(*args):
#     print(args)             # args is a tuple
#     return sum(args)
#
# print(add_all(2, 4, 6, 8))
#
#
# ➡️ Output:
#
# (2, 4, 6, 8)
# 20
#
# 🔹 Keyword Arguments — **kwargs
#
# Used when you don’t know how many keyword arguments will be passed.
#
# def print_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_details(name="Satyam", branch="ECE", year=3)
#
#
# ➡️ Output:
#
# name: Satyam
# branch: ECE
# year: 3
#
# 3️⃣ Return Values
# 📘 Definition:
#
# The return statement sends a value back to the caller from a function.
#
# def square(x):
#     return x * x
#
# result = square(5)
# print(result)
#
#
# ➡️ Output: 25
#
# 🧩 Without return, a function returns None by default.
#
# 4️⃣ Lambda Functions (Anonymous Functions)
# 📘 Definition:
#
# A lambda function is a small, one-line anonymous function.
#
# 📗 Syntax:
# lambda arguments: expression
#
# 📙 Example:
# square = lambda x: x * x
# print(square(4))
#
#
# ➡️ Output: 16
#
# You can also use it in sorting or map():
#
# nums = [1, 2, 3, 4]
# doubles = list(map(lambda x: x * 2, nums))
# print(doubles)
#
#
# ➡️ Output: [2, 4, 6, 8]
#
# 5️⃣ Scope and Lifetime of Variables
# 📘 Definition:
#
# Scope → Where a variable can be accessed.
#
# Lifetime → How long a variable exists in memory.
#
# 📗 Types of Scope:
# Type	Defined inside	Accessible
# Local	Function	Only inside that function
# Global	Outside all functions	Anywhere in the file
# 📙 Example:
# x = 10  # global variable
#
# def show():
#     x = 5  # local variable
#     print("Inside function:", x)
#
# show()
# print("Outside function:", x)
#
#
# ➡️ Output:
#
# Inside function: 5
# Outside function: 10
#
# ⚡ Using global keyword
#
# If you want to modify a global variable inside a function:
#
# count = 0
#
# def increment():
#     global count
#     count += 1
#
# increment()
# print(count)
#
#
# ➡️ Output: 1
#
# 6️⃣ Recursion
# 📘 Definition:
#
# A recursive function is a function that calls itself.
# Used for problems like factorial, Fibonacci, tree traversal, etc.
#
# 📗 Example: Factorial
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(5))
#
#
# ➡️ Output:
#
# 120
#
# ⚠️ Note:
#
# Every recursive function must have a base case,
# otherwise it’ll cause an infinite recursion error.