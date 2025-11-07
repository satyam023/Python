# welcome
# Sets
# Unordered , unindexed data type
# define by curly braces
# function set() or use { }
# store unique element

# s = {10 , 20 , 30}
# Iterate through
# for i in s:
#     print(i)

# Methods and function
# set() , add() , pop() , remove() ,
# clear() , update() , discard()

#  to convert in list
# s = "abl"
# st = set(s)
# print(st)  {'l', 'b', 'a'}
# l = [12 , 20 , 29]
# print(set(l)) {29, 12, 20}

# to add new element in set

s = {10 , 0 , 40 , 80 , 90}
s.add(50)

# to remove one element randomly
# s.pop()

#  it also returns element which has popped
# can't pass index as unindexed

# to remove particular element
# s.remove(10)
# ✅ Removes the element if it exists.
# ❌ But if the element does not exist, it raises an error:

# to remove particular element
s.discard(10)
# ✅ Removes the element if it exists.
# ✅ If it does not exist, it does nothing (no error).
# print(s)

# after clear how to distinguish set vs dict
s.clear()
print(s)
# after clear it returns
# set() -> a function it will not return {} this means dict

# ⚙️ In short: update with set
# Operation  	        Description
# s.add(x)	            Adds one element
# s.update(iterable)	Adds multiple elements

# ⚙️ In short (for dicts):
# Case          	    Behavior
# Key exists	        Updates value
# Key doesn’t exist	    Adds new key–value pair


# in set
l = [10 , 30 , 30 , 40 , 300 , 8]
s.update(l)
# print(s)