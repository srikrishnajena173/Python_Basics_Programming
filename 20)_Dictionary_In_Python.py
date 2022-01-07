# Dict is data type in python, but its is also a data structure of python

# Dictionary store the data in key:value format and in an unordered way, which means in the memory 
# it doesnt store the value next each other, the way list does, so in list can access the value by index.
# However in dictionary you cannot access the value by index.

# Key must be a immutable type which cannot be change 
# and value is object, which mean it can store any type of value/literals 

# Example 1. Syntax of dictinary 
my_dict = {
    'a':1,
    'b':2
}
print(my_dict['a'])
# O/P :- 1

# Example 2. 
my_dict_1 = {
    'a':[1,2,3],
    'b':2,
    'c':2.3,
    'd': True
}
print(my_dict_1) # which means you can store any type of value/literals 
# O/P :- 
# {'a': [1, 2, 3], 'b': 2, 'c': 2.3, 'd': True}

# Example 3 :- Now get the list 2nd index value from the key 'a'
my_dict_2 = {
    'a':[1,2,3],
    'b':2,
    'c':2.3,
    'd': True
}
print(my_dict_1['a'][2])

# O/P :- 
# 3

# Example 4 :- 
my_list = [
    {
    'a':[1,2,3],
    'b':2,
    'c':2.3,
    'd': True
}, 
{
    'a':[4,5,6],
    'b':2,
    'c':2.3,
    'd': True
}
]
print(my_list[1]['a'][2]) 
# so here you want to access the 1st index of the list, then the key 'a' and
# then you access the 2nd index of key 'a'.


