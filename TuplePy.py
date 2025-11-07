# Welcome
# Tuple is immutable
# used when we need any constant value
# ordered data type
# In Python, an ordered data type
# means the items have a defined
# order, and that order will not
# change unless you explicitly do so.
from operator import index

# t = (10 , 20 , 30 , 40)
# for i in t:
#     print(i)
# Always in the same order as you inserted.
# 🧮 In short:
# Category	Ordered Data Types	   Unordered Data Types
# Ordered	list, tuple, str,
#            dict (Python 3.7+)
# Unordered		                     set, frozenset
# print(t)

# # to make tuple more than ane element should present
# t = ("py")
# print(type(t)) <class 'str'>

# Iterate in tuple
# t = (10 , 20 , 30 , 40)
# l = len(t)
# for i in range(l):
#     print(t[i])
#
# t = (10 , 20 , 30 , 40)
# l = len(t)
# for i in t:
#     print(i)

# reverse
# t = (10 , 20 , 30 , 40)
# l = len(t)
# for i in range(l-1,-1,-1):
#     print(t[i])


# to get min
t = (40 , 90 , 10 , 40 , 2 , 3,  1, -1, 0 , 100, 10 , 20 , 30 , 40)
m = min(t)
ma = max(t)
count40 = t.count(40)
# to get index

ind1 = t.index(1)

# s = sum(t)
# sum always work with only int and float if string give error
# it works with two params also
# sum(t , default_val=0)
# s= sum(t, 0)

# print('Min', m , 'Max', ma, 'Count40', count40 ,'Ind1', ind1 , 'Sum', s)


# Methods 
# min(t) , max(t) , sum(t), sum(t, any_val)  , t.count(item) , t.index(item)
