# List
# Just like string
# indexing 0 to n-1
# last element to first by using -1 to n
# check list by using type function

# l = [1 , 2 , 2 ,4]
# print(l)
# print(len(l))
# print(type(l))
# OUTPUT:
# [1, 2, 2, 4]
# 4
# <class 'list'>

# nested list
# l = [1, 2, 3 , [3 , 4,  5]]
# print(len(l))
# print(l[3][2])

# 🧩 Most Common List Methods to Remember
# Category            	Methods
# Add	                append(), extend(), insert()
# Remove	            remove(), pop(), clear()
# Search / Count	    index(), count()
# Order	                sort(), reverse()
# Utility	            copy()


# nums = [1, 2, 3]
# nums.append(4)          # [1, 2, 3, 4]
# nums.insert(1, 10)      # [1, 10, 2, 3, 4]
# nums.remove(3)          # [1, 10, 2, 4]
# nums.sort()             # [1, 2, 4, 10]
# nums.reverse()          # [10, 4, 2, 1]
# print(len(nums))        # 4

# ========================================
# 📘 LIST METHODS IN PYTHON
# ========================================

# Lists are mutable sequences — you can change, add, or remove elements.
# Example list:
nums = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", True, 3.14]

# ---------- ADDING ELEMENTS ----------

nums.append(60)
# → Adds a single element to the end
# nums = [10, 20, 30, 40, 50, 60]

nums.extend([70, 80])
# → Adds multiple elements (list/tuple) at the end
# nums = [10, 20, 30, 40, 50, 60, 70, 80]

nums.insert(2, 25)
# → Inserts element at specific index (index, value)
# nums = [10, 20, 25, 30, 40, 50, 60, 70, 80]

# ---------- REMOVING ELEMENTS ----------

nums.remove(40)
# → Removes the *first occurrence* of given value
# nums = [10, 20, 25, 30, 50, 60, 70, 80]

nums.pop()          # Removes last element
nums.pop(2)         # Removes element at index 2
# nums = [10, 20, 30, 50, 60, 70]

del nums[1]         # Deletes element at index 1
# nums = [10, 30, 50, 60, 70]

nums.clear()
# → Removes all elements; becomes []
# nums = []

# ---------- COPYING & COUNTING ----------

fruits2 = fruits.copy()
# → Returns a shallow copy of list
# fruits2 = ['apple', 'banana', 'cherry']

fruits.count("apple")
# → Counts how many times a value appears
# returns 1

# ---------- SEARCHING ----------

fruits.index("banana")
# → Returns index of first occurrence (ValueError if not found)
# returns 1

# ---------- SORTING & REVERSING ----------

numbers = [5, 3, 1, 4, 2]

numbers.sort()
# → Sorts the list in ascending order (in-place)
# numbers = [1, 2, 3, 4, 5]

numbers.sort(reverse=True)
# → Sorts in descending order
# numbers = [5, 4, 3, 2, 1]

fruits.reverse()
# → Reverses the order of elements (in-place)
# fruits = ['cherry', 'banana', 'apple']

# ---------- NESTED LISTS ----------

matrix = [[1, 2], [3, 4], [5, 6]]
var = matrix[1][0]
# → Access inner elements (3 in this case)

# ---------- UNPACKING ----------
a, b, c = fruits
# → Unpacks list values into variables
# a='apple', b='banana', c='cherry'

# ---------- NEW PYTHON 3.10+ ----------
nums = [1, 2, 3]
nums *= 2
# → List repetition → [1, 2, 3, 1, 2, 3]


# slicing in list is same as string
l = [5, 3, 1, 4, 2]
# print(l[0::2])
# 0::2 means start from 0  then :len : increment / decrement
# :: no len means from 0 to last
# reverse
# print(l[-1::-1])

# to get two number then u can use slice
# print(l[0:2]) # default increment1
# print(l[:2])  # same as above
# print(l[2:])  from 2 to last
# print(l[2],l[4])

# List Iteration


# using for loop
t = len(l)
# for i in range(t):
#     print(l[i])

# for i in l :
#     print(i, end=" ")

# print in reverse
# for i in range(t-1 ,-1, -1):   startInd , lastInd+1 , increment/decrement
#     print(l[i])
# print(l)
# del l[2]
# print(l)
# print(l.pop(2))
# # pop return also which ever delete but del not
# print(l)

l.remove(3)
# print(l.remove(5)) none
# print(l)
# l.clear()
# print(l)

# insert()
# append()
# extends()
l.append(60)
# l.insert(0, 10) insert is used to insert at specific position
# insert(index , value) , not replaced but  shift [10, 60]
# print(l)
n = [90,90]
l.append(n)
l.pop()
# pop() without index remove last element
# append is used data types as given
# print(l)
# l.extend([90, 80 , 70 , 2002])
# extend is work with list only take value and extend in list
# used to insert multiple value at once
# print(l) [60, 90, 80, 70, 2002]
# l.extend((90, 90 , 90))
# print(l)    [60, 90, 80, 70, 2002, 90, 90, 90]

# List Comprehension:-
# List Comprehension is an elegant way to define and create lists based on existing lists
# List comprehension is generally more compact and faster than
# normal functions and loops for creating list

# syntax
# [expression for item in list]

l =[]
for a in range(1, 101):
    l.append(a)
# print(l)
# n = [m for m in range(1,101)]
# n = [m for m in range(1, 101) if m % 2 == 0]
# s = "Satyam"
# l = list(s)
# l = [g for g in s]
# print(l)
# print("n = ", n)

# count()
# count the freq of element in list
# l = [10 , 30 , 10 , 20 , 30 , 30 , 40]
# print(l.count(10)) 2
# max()  to get maximum value in list
# m = max(l)
# print(m)
# n = ['Hello' , 'world']
# print(max(n))
# print(min(n))
# print(min(l))
# l.sort()
# to sort in reverse order
# l.sort(reverse=True)
# print("sorted" , l)
# print(l)
# l.reverse()  # to reverse the data as it is
# print("reversed" , l)
# l.index(20)



# ******************************
# ZIP FUNCTION
# used to combine list and take equal length
# greater length will ignore
# ******************************
l = [10 , 30 , 10 , 20 , 30 , 30 , 40]
n = [m for m in range(1, 21) if m % 2 == 0]

# Iterate in both list at same time

# for a , b in zip(l,n):
#     print(a, b)

#  Convert String to List
# s=input("Enter the text:- ")

# use split method
# convert string in list broke strike with spae

# l=s.split()
# l = list(s)
# print(l)


# *********************************
# Implementation of Stack and Queue
# **********************************

# operation , push , pop , peak , display , exit

# l = []
#
# while True:
#     print("\nChoose an option:")
#     c = int(input('''
#     1. Push Element
#     2. Pop Element
#     3. Peek Element
#     4. Display Stack
#     5. Exit
#
#
#     '''))
#
#     if c == 1:
#         n = input("Enter the value: ")
#         l.append(n)
#         print(f"'{n}' pushed into stack.")
#
#     elif c == 2:
#         if len(l) > 0:
#             popped = l.pop()
#             print(f"Popped element: {popped}")
#         else:
#             print("Stack is empty. Nothing to pop!")
#
#     elif c == 3:
#         if len(l) > 0:
#             print(f"Top element: {l[-1]}")
#         else:
#             print("Stack is empty. No top element!")
#
#     elif c == 4:
#         if len(l) > 0:
#             print("Current stack:", l)
#         else:
#             print("Stack is empty.")
#
#     elif c == 5:
#         print("Exiting...")
#         break
#
#     else:
#         print("Invalid choice! Please enter a number between 1 and 5.")
#
#
# *********************************
# Implementation of  Queue
# **********************************

l = []

while True:
    c = int(input('''
    1. Enqueue Element
    2. Dequeue Element
    3. Front Element
    4. Rear Element
    5. Display Queue
    6. Exit
    '''))

    if c == 1:
        n = input("Enter the value: ")
        l.append(n)
        print(f"'{n}' pushed into queue.")

    elif c == 2:
        if len(l) > 0:
            popped = l.pop(0)
            print(f"Popped element: {popped}")
        else:
            print("Queue is empty. Nothing to pop!")

    elif c == 3:
        if len(l) > 0:
            print(f"Front element: {l[0]}")
        else:
            print("Queue is empty. No front element!")

    elif c == 4:
        if len(l) > 0:
            print(f" Rear element: {l[-1]}")
        else:
            print("Queue is empty. No rear element!")

    elif c == 5:
        if len(l) > 0:
            print("Current Queue:", l)
        else:
            print("Queue is empty.")

    elif c == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
