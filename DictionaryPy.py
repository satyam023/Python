# Unorder Data Type
# In Moder pyhton dictionaries are ordered data types
# 'key' :value
# key is mutable
# d = { 'name': 'satya', 'age': 21 }
# key is unique again define then duplicate key error
# value can be same

# print(d['name'])
      #  access using for loop
# for n in d:   # d gives only key
#     print(n,':', d[n])

# dictionary is mutable data type
d = { 'name': 'satya', 'branch': 'ECE',  'age': 21 , 'cgpa': 8.96  }
# dictionary methods
# get() to retrieve data
# keys() to get key used in loop
# values() to get values in loop
# items()  give both  key , value in for loop
# n = d.get('name')
# for i  in d.keys():
#     print(i)
# print()
# for j in d.values():
#     print(j)
# print()
# for a , b in d.items():
#     print(a, ':', b)
# print(n)


di = { 'name': 'satya', 'branch': 'ECE',  'age': 21 , 'cgpa': 8.96  }
# delete item in dict is through keys only
# del di['cgpa']
# print(di)
# pop does same as del and return also
# print(di.pop('cgpa'))

# p = dict(name='satyam', cg = 8.96)
# to make dictionary
# update to update item of dict
# p.update({'cg': 9.00})
# p.clear()
#  to clear the value of dict
# p['year'] = 2026
# if this is available key then update if not then insert
# print(p)


# NESTED DICTIONARY

course = {
    'php':{'duration': '2 Months', 'Fees':'15000'},
    'python':{'duration': '3 Months', 'Fees':'1600'},
    'sql':{'duration': '1 Months', 'Fees':'1000'},
    'mongo':{'duration': '3 Months', 'Fees':'19000'},
}

# print(course)

#  how to retrieve particular data
# let's say php fee
# print(course['php'])
# this will give php row
# in php check fee
# print(course['php']['Fees'])
# in this way we get particular data

# Iterate complete dict
# for k, v in course.items():        # outer loop → subject and its info dict
#     for j, i in v.items():         # inner loop → key/value from inner dict
#         print(k, ":", j, "=", i)


# Update
# course['php']['duration'] = '5 Months'
# print(course)

