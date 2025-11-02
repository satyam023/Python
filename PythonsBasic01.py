# 🧩 1. INTRODUCTION TO Python programming language
#
# Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
#
# It is designed for readability and ease of use.
#
# Developed by Guido van Rossum in 1991.
#
# 🔹 Key Features:
#
# Interpreted: Executes code line by line (no compilation step).
#
# High-level: Programmer-friendly, close to human language.
#
# Object-Oriented: Supports classes and objects.
#
# Dynamically Typed: No need to declare variable types explicitly.
#
# Extensive Libraries: Comes with a large standard library.
#
# Portable: Runs on multiple platforms (Windows, macOS, Linux).
#
# Open Source: Freely available to everyone.
#
# Supports GUI Programming.
#
# ⚙️ 2. PYTHON EXECUTION LOGIC
#
# Python code is executed by the Python Interpreter.
#
# The interpreter reads code line by line (interpreted execution).
#
# Uses indentation (whitespace) to define code blocks.
#
# No need for { } or ; like in C or Java.
#
# Example:
#
# if True:
#     print("Hello Python")
#
# 🧠 3. PYTHON IDENTIFIERS & VARIABLES
# Rules for variable names:
#
# ✅ Must begin with a letter or underscore _
# ✅ Can contain letters, digits, and underscores
# ❌ Cannot start with a digit
# ❌ Cannot contain spaces or special symbols (-, @, #, etc.)
# ❌ Cannot use reserved keywords
#
# Example:
#
# name = "Satyam"
# _age = 19
# total_sum = 250
#
# 🧮 4. PYTHON NUMBER SYSTEMS
#
# Python supports:
#
# Decimal (base 10)
#
# Binary (base 2)
#
# Octal (base 8)
#
# Hexadecimal (base 16)
#
# Conversion Functions:
# Function	Converts To	Example	Output
# bin()	Binary	bin(10)	'0b1010'
# oct()	Octal	oct(10)	'0o12'
# hex()	Hexadecimal	hex(10)	'0xa'
# Example:
# print(0b1010)  # Binary → 10
# print(0o12)    # Octal  → 10
# print(0xa)     # Hex    → 10
#
# 🧾 5. PYTHON 2 vs PYTHON 3
# Feature	Python 2	Python 3
# Print Statement	print "Hello"	print("Hello")
# Division	5 / 2 = 2	5 / 2 = 2.5
# Unicode	Default: ASCII	Default: Unicode
# Octal Literal	02	0o2
# Support	Discontinued	Ongoing

# variable in python
## In python memory allocation is done based on value not variable
## for example if a = 10 , b = 10 then memory address of a and b is same
## we can find it by using print(id(a))

# ===============================================
# STRING CONCATENATION
# ===============================================

# a = "Hello"
# b = "World"
#
# # Using + operator to join strings
# print(a + " " + b)     # Output: Hello World
#
# # You cannot concatenate a string with an integer directly
# # print(a + 10)  # ❌ Error: TypeError
#
# # ✅ Correct way:
# print(a + str(10))      # Output: Hello10

# NOTE: Concatenation works only between the same data types (str + str, int + int, etc.)

# ===============================================
# ARITHMETIC OPERATORS
# ===============================================

# Operators: +, -, *, /, %, //, **

# a = 10
# b = 3
#
# print(a + b)   # Addition          → 13
# print(a - b)   # Subtraction       → 7
# print(a * b)   # Multiplication    → 30
# print(a / b)   # Division          → 3.3333333333333335
# print(a % b)   # Modulus (Remainder) → 1
# print(a ** b)  # Exponent (Power)  → 1000 (10³)
# print(a // b)  # Floor Division    → 3 (removes fractional part)

# Floor division (//) removes the decimal part and rounds down the result
# Example: 10 // 3 → 3,  -10 // 3 → -4 (rounds down to next lower integer)

# ===============================================
# ASSIGNMENT OPERATORS
# ===============================================

# x = 5
# print(x)       # 5
#
# x += 3         # x = x + 3
# print(x)       # 8
#
# x -= 3         # x = x - 3
# print(x)       # 5
#
# x *= 2         # x = x * 2
# print(x)       # 10
#
# x /= 5         # x = x / 5
# print(x)       # 2.0
#
# x **= 3        # x = x ** 3
# print(x)       # 8.0

# ⚠️ Note:
# x++ or x-- are invalid in Python lang
# Python does NOT support increment (++) or decrement (--) operators

# ===============================================
# COMPARISON OPERATORS
# ===============================================

# Used to compare two values, result is always True or False

# a = 10
# b = 3
#
# print(a == b)   # Equal to          → False
# print(a != b)   # Not equal to      → True
# print(a > b)    # Greater than      → True
# print(a < b)    # Less than         → False
# print(a >= b)   # Greater or equal  → True
# print(a <= b)   # Less or equal     → False

# ===============================================
# SUMMARY
# ===============================================

# ➤ Arithmetic Operators: +, -, *, /, %, //, **
# ➤ Assignment Operators: =, +=, -=, *=, /=, **=
# ➤ Comparison Operators: ==, !=, >, <, >=, <=
# ➤ ++ and -- do NOT exist in Python
# ➤ String concatenation only works between strings

