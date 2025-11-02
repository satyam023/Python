# To Get user input
# raw_input() in Python 2 ≈ input() in Python 3
from operator import truediv

# age = input("Enter your age: ")
# print(int(age) + 3)

# age = int(input("Enter your age: "))
# print("After 3 years, you will be:", age + 3)

# Assignment operator — modifies a variable
# Cannot use inside print
# print(age += 3) ❌ invalid syntax
# Python 2	          VS            Python 3
# raw_input() → string input	    input() → string input
# input() → evaluates expression	eval() → use explicitly if needed
# Python 2 => input() → evaluates expression
# age = input("Enter your age: ")
# print age + 1

# If you type:
# Enter your age: 20
# ✅ Works fine → 21

# But if you type:
# Enter your age: "Satyam"

# It will throw an error or
# even execute arbitrary
# code (since it evaluates
# your input as Python code).

# a = input("Enter a number: ")
# b = input("Enter another number: ")
# print(a + b) : concat as string default
# print(a - b) : unsupported operand type(s) for -: 'str' and 'str'
#


# typecasting
# a = int(input("Enter a number: "))
# b = float(input("Enter another number: "))
# print(a + b)

# typecasting in int then you can't
# give input as float but
# if you type cast in float
# then you can give integer input

# a = eval(input("Enter a number: "))
# b = eval(input("Enter another number: "))
# print(a + b)

# if you  typecast using eval then
# you give input as integer, float
# binary(0b1010) ,
# octal(0o10) , hexadecimal (0x10)

# print(hex(10)) => 0xa

# Conditional Statement
# If, If Else & If Elif Else
# Conditional Statements in Python


# a = int(input('Enter a number: '))
# b = int(input('Enter another number: '))
# if a<b:
#     print(a ,' is less than' , b)
# elif a>b:
#     print(a ,' is greater than ', b)
# else:
#      print(a ,' is equal to ',b)


# indentation and whitespace should be equal
# All the statements
# that belong to the
# same block must have equal
# indentation.

# if True:
#     print("Line 1")
#       print("Line 2")  # Error: inconsistent indentation


# for i in range(3):
#     if i % 2 == 0:
#         print(i, "is even")
#     else:
#         print(i, "is odd")
# print("Loop completed")


