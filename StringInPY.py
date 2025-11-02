# String In Python
# left to right indexing 0 to n-1
# right to left -1 to -n

w="My Name is Satyam"
# print(w[-17]) M

# Slicing
# w[start: len+1 : increment]

# print(w[0:7]) My Name
# with increment
# print(w[0::2])
# :: means start to end
# with increment of 2
# result=>  M aei aym
# print(w[0: ])
# colon white space means start from 0 end at last
# Reverse slice start from -1
# print(w[-1::-1]) maytaS si emaN yM

#  to get length of string
t = len(w) #17
# for i in range(t): # 0 to 16
#     print(w[i], end="")

# Reverse string
# w = w[-1::-1]
# for i in range(t-1, -1, -1): # 16 to 0 decrement -1
#     print(w[i], end="")
# we can also pass string directly in for loop
#  range will give number if we pass string it give char
# for i in w:
#     print(i, end="")


# Feature	      Method	                   Function
# Called using	  object.method()	           function(object)
# Belongs to	  A specific object/class
#                  (like str, list, etc.)	    Global / built-in namespace
# Example	      "abc".upper()	                 len("abc")


# Methods of Strings
# lower()
# Upper()
# title()
# capitalize()
n = w.lower() # all lower
m = w.upper() # all upper
l = w.title() # first letter of every word capital
o = w.capitalize() # first letter of string capital rest lower case
# print(o)

# find()
# find(char , startInd)
# to find index of char, sub-string
# it will give first match
# else it will give -1
# print(w.find('z'))  => -1

# index()
# index(char , StartInd)
# if not present char in string then give error
# this is only diff in index and find
# return index


# Bool methods false/true
# isalpha()
# isdigit()
# isalnum()

# w="mynameissatyam"
# print(w.isalpha())
# only alphabets if space or any num then false
# w="1233"
# print(w.isdigit())
# only digit if space or any alphabet then false
w="alp135w4"
# print(w.isalnum())
# only alphanumeric if space then false



# chr()
# for a particular integer what is char
# ord()
# reverse of chr() for char what is integer
# use to find ascii uni-code of char

# y = chr(65)
# print(type(y) , y)
# <class 'str'> A


# a = ord('A')
# print(type(a) , a)
# <class 'int'> 65


# format() method
# format() is a string method, not a standalone function.
# It is used to insert values into a string at specific placeholders ({}).
# name = "Satyam"
# age = 21
# print("My name is {} and I am {} years old.".format(name, age))
# Output:
# My name is Satyam and I am 21 years old.

# print("{:<10}".format("left"))   # left align
# print("{:^10}".format("center")) # center align
# print("{:>10}".format("right"))  # right align


# left
#   center
#      right



# Positional Formatting
#
# You can specify the position of arguments using numbers inside {}.
#
# print("{0} is {1} years old".format("Satyam", 21))
# print("{1} is {0} years old".format(21, "Satyam"))
#
#
# Output:
#
# Satyam is 21 years old
# Satyam is 21 years old


# 🏷️ Named Placeholders
#
# You can use keyword arguments too:
#
# print("My name is {name} and I study {branch}".format(name="Satyam", branch="ECE"))
#
#
# Output:
#
# My name is Satyam and I study ECE


# You can format decimals, padding, and alignment easily:
#
# pi = 3.14159265
# print("Pi = {:.2f}".format(pi))   # 2 decimal places
# print("Pi = {:10.3f}".format(pi)) # width 10, 3 decimal places
#
#
# Output:
#
# Pi = 3.14
# Pi =      3.142


# **********************
# Modern
# ****************

# Modern Alternative: f-strings (Python 3.6+)
#
# The same thing can now be done more easily using f-strings:
#
# name = "Satyam"
# age = 21
# print(f"My name is {name} and I am {age} years old.")

# Remember — strings are immutable, so all these methods return new strings.

# # ========================================
# # 📘 STRING METHODS IN PYTHON
# # ========================================
#
text = " hello world "
# s = "python"
# num = "123"
#
# # ---------- CASE CONVERSION ----------
# text.capitalize()        # Capitalize first letter → ' hello world ' → ' hello world '
# text.title()             # Each word starts with uppercase → 'Hello World'
# text.upper()             # Convert all to uppercase → 'HELLO WORLD'
# text.lower()             # Convert all to lowercase → 'hello world'
# text.swapcase()          # Swap case → 'HELLO world' → 'hello WORLD'
# text.casefold()          # Aggressive lowercase (for case-insensitive compare)
#
# # ---------- STRIPPING WHITESPACES ----------
# text.strip()             # Remove spaces from both ends → 'hello world'
# text.lstrip()            # Remove spaces from left → 'hello world '
# text.rstrip()            # Remove spaces from right → ' hello world'
#
# # ---------- SEARCHING ----------
# text.find("o")           # Returns index of first 'o' → 5, or -1 if not found
# text.rfind("o")          # Returns index of last 'o'
# text.index("w")          # Like find() but raises ValueError if not found
# text.count("l")          # Count occurrences of substring → 3
# text.startswith(" he")   # Returns True if string starts with substring
# text.endswith("ld ")     # Returns True if string ends with substring
#
# # ---------- REPLACE & TRANSLATE ----------
# text.replace("world", "Python")   # Replace all occurrences → ' hello Python '
# table = str.maketrans("aeiou", "12345")
# "text".translate(table)           # Replace chars using table (a→1, e→2...)
#
# # ---------- SPLITTING & JOINING ----------
# text.split()              # Split by spaces → ['hello', 'world']
# text.split(",")           # Split by comma
# text.rsplit(" ", 1)       # Split from right once
# text.splitlines()         # Split by line breaks (\n, \r\n)
# "-".join(["a", "b", "c"]) # Join list → 'a-b-c'
#
# # ---------- ALIGNMENT ----------
# s.center(10, "-")         # Center align with '-' padding → '--python--'
# s.ljust(10, ".")          # Left align → 'python....'
# s.rjust(10, ".")          # Right align → '....python'
# num.zfill(6)              # Pad with zeros → '000123'
#
# # ---------- CHECKING TYPES ----------
# s.isalpha()        # True if all alphabetic
# num.isdigit()      # True if all digits
# num.isdecimal()    # True if all decimal chars (0–9 only)
# num.isnumeric()    # True if numeric (includes ½, Ⅳ, etc.)
# s.isalnum()        # True if alphanumeric (letters+numbers)
# s.islower()        # True if all lowercase
# s.isupper()        # True if all uppercase
# s.istitle()        # True if Title Case
# "   ".isspace()    # True if only whitespace
# s.isascii()        # True if all ASCII chars
# s.isidentifier()   # True if valid Python identifier (variable name)
# "print".isprintable() # True if all printable chars
#
# # ---------- FORMATTING ----------
# "{} is {}".format("Python", "cool")      # → 'Python is cool'
# "{name} is {adj}".format(name="Python", adj="powerful")  # Named args
# "{:.2f}".format(3.14159)                 # Decimal precision → '3.14'
# "{:>10}".format("hi")                    # Right align → '        hi'
# "{:<10}".format("hi")                    # Left align  → 'hi        '
# "{:^10}".format("hi")                    # Center align → '    hi    '
# data = {"name": "Satyam", "lang": "Python"}
# "{name} codes in {lang}".format_map(data)  # Using dict for values
#
# # ---------- PARTITIONING ----------
# "apple-banana".partition("-")   # → ('apple', '-', 'banana')
# "apple-banana".rpartition("-")  # Split from right → ('apple', '-', 'banana')
#
# # ---------- NEW IN PYTHON 3.9 ----------
# "unhappy".removeprefix("un")    # → 'happy'
# "data.txt".removesuffix(".txt") # → 'data'
#
# # ---------- EXPAND TABS ----------
# "one\ttwo\tthree".expandtabs(4) # Replace \t with 4 spaces → 'one    two    three'





