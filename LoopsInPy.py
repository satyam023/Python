# For loop with Range() in python
# Range() function is imp
range(5)
# it means three things
# start = 0
# condition < 5
# increment default 1
range(1, 6)
# it means three things
# start = 1
# condition < 6
# increment default 1
range(1, 5, 2)
# it means three things
# start = 1
# condition < 5
# increment  2

# how it works with for loop
# for n in range(5):
#     print(n, end=" ")
# print("New loop started")
# Normally, print() ends with a newline (\n) after each call.
#
# By setting end=" ", you replace that
# newline with a space (or anything else you want).
# print()
# for n in range(1, 6):
#     print(n, end=" ")
# print()
# for n in range(1, 5, 2):
#     print(n, end=" ")

# for i in range(1, 11):
#     print( "2 *",i,"=" ,2*i )

# Reverse In Loop
# for i in range(10, -1 , -1):
#     print( "2 *",i,"=" ,2*i )

# While Loop
# start
# condition in while
# increment / decrement
i = 1
while i <= 10:
    print(i)
    i = i + 1

print(i)



