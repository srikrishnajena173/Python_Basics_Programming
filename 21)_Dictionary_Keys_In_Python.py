# Dictionary key should be immutable , i.e. key cannot be changed 
# Dictionary key should not have duplicate keys 

# Example 1. 
my_dict = {
    'a':[1,2,3],
    True:'boolean',
    1.3:2.3,
    1: True
}

# Example 2. 
my_dict_1 = {
    'a':1,
    'a':2 # you can declare a duplicate keys, however the latest key value will override the older key value
}
print(my_dict_1['a'])
# O/P :- 2
