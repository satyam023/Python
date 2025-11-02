# Logic Operator
# and -> both true then true else false
# or -> any one true then true
# not -> reverse the result

# Membership Operators
# in , not in

# str1 = "Hello"
# print('h' in str1) # false as python is case-sensitive
# print('h' not in str1)  #true

# Identity Operators
# is , is not
# is '=' ==
# is not '=' !=
# x = 10
# y = 10
# print(x is y == x ==y) # true
# x is y true
# y == x true
# x == y true,
# true and true and true
# print(x is not y == x != y) # false
# x is not y false
# y == x true
# x == y false,
# false and true and false
# Why “and” is important
#
# Without and, you might think Python compares everything at once —
# but it doesn’t.
# It checks each link in the chain one by one and joins them with logical AND.
#
# That’s how Python allows beautiful expressions like:
#
# if 10 < x < 20:
#
#
# which means:
#
# (10 < x) and (x < 20)
# print((x is not y )== (x != y)) # true
# (x is not y) → checks object identity
# (x != y) → checks value inequality
# That’s why you’re seeing True in output —
# because both expressions give the same Boolean value (False),
# and False == False is True.

#Bitwise Operator
# & , | , ^

# x=8
# y=8
# print(bin(x), bin(y))
# print(x & (x-1) , bin((x & (x-1))))
# If x is a power of two,
# then x & (x - 1) = 0

# Data types in python
# Function	 Converts To
# int()	     Integer
# float()	 Floating-point number
# str()	     String
# list()	 List
# tuple()	 Tuple
# set()	     Set
# dict()	 Dictionary

# Category:	    Data Type	           Example
# Numeric:	    int, float, complex 	10, 10.5, 2+3j
# Sequence:	    list, tuple, range  	[1,2,3], (1,2,3), range(5)
# Text: 	     str	                    "Hello"
# Set:	         set, frozenset      	{1,2,3}
# Mapping	     dict	                {"a":1, "b":2}
# Boolean	      bool	                True, False
# None Type      	NoneType	            None


# 🔹 1️⃣ Meaning in Simple Terms
# Term	    Meaning
# Mutable	    Can be changed/modified after creation
# Immutable 	Cannot be changed once created

# Mutable means the object
# itself can be modified
# without creating a new one.

# Immutable means the object
# cannot be changed —
# any “change”
# creates a new object in memory.


# 🔹 2️⃣ Logical Explanation (What Happens in Memory)
#
# Think of every variable in Python as a label (name) attached to an object (value) in memory.
#
# When you modify a variable,
# Python may or may not create a new object —
# depending on whether the data type
# is mutable or immutable.
#
# 🧱 Example 1: Immutable (int, str, tuple)
# x = 10
# y = x
# x = x + 5
#
#
# 🧠 Step-by-step:
#
# x → object 10
#
# y = x → now both point to the same memory address
#
# x = x + 5 → Python creates a new object (15) and x now points to it
# but y still points to old 10
#
# 📊 So:
#
# Variable	Value	Memory Address (example)
# x	15	0x1002
# y	10	0x1001
#
# ✅ int is immutable →
# value change →
# new memory created.
#
# 🧾 Example 2: Mutable (list, dict, set)
# a = [1, 2, 3]
# b = a
# a.append(4)
#
#
# 🧠 Step-by-step:
#
# a → list object [1, 2, 3]
#
# b = a → both a and b
# refer to the same memory
#
# a.append(4) → list is modified
# in-place,
# not recreated
#
# 📊 So:
#
# Variable	Value	Memory Address
# a	[1, 2, 3, 4]	0x2001
# b	[1, 2, 3, 4]	0x2001
#
# ✅ list is mutable →
# value modified →
# same memory reused.
#
# 🔹 3️⃣ Logical Difference (Inside Python)
# Type	    Can modify same memory?	Creates new memory on change?
# Mutable	    ✅ Yes	                ❌ No
# Immutable	     ❌ No	                 ✅ Yes
# 🧠 4️⃣ Why It Matters
#
# Performance:
# Mutable can be changed in place →
# faster updates.
# Immutables need new memory →
# safer but slower for
# large changes.
#
# Hash-ability
# Immutable objects
# can be used as
# dictionary keys or set elements.
# Mutable objects cannot.
#
# Example:
#
# my_dict = { (1, 2): "ok" }  # ✅ tuple works (immutable)
# my_dict = { [1, 2]: "error" }  # ❌ list is unhashable
#
#
# Predictability:
# Immutable data prevents unintended side effects (like accidental modification in functions).
#
# 🔹 5️⃣ Common Examples
# Mutable Types	   Immutable Types
# list          	int
# dict          	float
# set           	str
# 	                tuple
#               	bool
# 	                frozenset
# 🧩 6️⃣ Visual Memory Example
# Immutable Example:
# x = "Hi"
# y = x
# x += " Python"
#
#
# Memory visualization:
#
# x → "Hi"  (0x100)
# y → "Hi"  (0x100)
# x → "Hi Python" (0x200) ← new object created
#
# Mutable Example:
# a = [1, 2]
# b = a
# a.append(3)
#
#
# Memory visualization:
#
# a → [1, 2, 3] (0x500)
# b → [1, 2, 3] (0x500)

# ⚡ Summary Table
# Data Type	    Can modify in place?	Reassignment creates new object?	Example
# int	        ❌ No	                ✅ Yes                           	x = 5 → x = 6
# float	        ❌ No	                ✅ Yes	                            y = 2.5 → y = 5.0
# str	        ❌ No	                ✅ Yes	                            "hi" → "hi there"
# tuple	        ❌ No	                ✅ Yes	                            (1,2) → (1,2,3)
# bool	        ❌ No	                ✅ Yes	                            True → False
# frozenset	    ❌ No	                ✅ Yes	                            {1,2} → {1,2,3}

# ✅ Final Key Idea
#
# 🔸 Immutable: The object’s content
# cannot change.
# Variable reassignment creates
# a new object → new memory address.
#
# 🔸 Mutable: The object’s content can
# change without creating a
# new object → same memory address.

# String:-
#  A string is a collection of one or more char put in single
# double , triple quote
# Multi line strings can be denoted using
# triple quote ('''or """)
#
# print('''My Name is Satyam
# I am currently pursuing bachelor's degree in ECE''')
#
# # My Name is Satyam
# # I am currently pursuing bachelor's degree in ECE

# List:- Mutable
# List is an ordered sequence of items
# it is one of the most used datatype in python and is very flexible
# []

# ex
# a = [1 , 2.2 , 'ws']
# print(id(a))
# print(len(a))
# print(a[0])
# print(a[1])
# print(a[2])
# print(a.append(3))  # -> none
# a.append(3)
# print(id(a))
# print(a[3])

# s = "HEllO"
# print(id(s))
# s[0] = '4' error
# print(id(s))


# Tuple :- Immutable
# Tuple is an ordered seq. of items same as list
# it is defined within parentheses() where items
# are separated by commas , single element in () is not tuple
# to be called a tuple there should be at-least 2 elements

# t = (2, 'program', 1+1j)
# print(t) (2, 'program', (1+1j))
# print(type(t)) <class 'tuple'>


# Dictionary: Mutable
# It is an unordered collection of key value pairs
# in python, dict are defined within {} with each item being a pair int the form key : value

# d = {1:'value', 'key': 2}
# print(d)
# print(type(d)) <class 'dict'>


# Set: Immutable
# A set is an unordered collection of items
# Every set element is unique and must be immutable
# {}

# my_set = {1 , 2 , 2, 3}
# print(my_set)  => {1, 2, 3}
