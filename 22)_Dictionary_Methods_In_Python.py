# Lets explore some dictionary methods
# Method	       Description

# clear()	       Removes all the elements from the dictionary
# copy()	       Returns a copy of the dictionary
# fromkeys()	   Returns a dictionary with the specified keys and value
# get()	           Returns the value of the specified key
# items()	       Returns a list containing a tuple for each key value pair
# keys()	       Returns a list containing the dictionary's keys
# pop()	           Removes the element with the specified key
# popitem()	       Removes the last inserted key-value pair
# setdefault()	   Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	       Updates the dictionary with the specified key-value pairs
# values()	       Returns a list of all the values in the dictionary


# Example 1 :- get(key) method --> to get the value of the given key
my_dict = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}

print(my_dict.get('a')) # O/P :- 1

# print(my_dict['e']) # O/P :- KeyError: 'e' , so here i got an error, becasue we dont have any key called 'e'
# and to avoid such kind of error which breaks you code flow, you can use 'get() method'

print(my_dict.get('e')) # O/P :- None
# So, here rather throwing an error and breaking the code flow, its just return None.
# So here we avoided the code flow break.

print(my_dict.get('e', 6)) # O/P :- 6, in case you dont have any key called 'e' , then it will return 
# the value assgined i.e. 6. Else it will return the original value.

# Example 2 :- another way of creating a dictionary 
my_dict_1 = dict(name='Sri')
print(my_dict_1)
# O/P :- {'name': 'Sri'}

# Example 3 :- keys() method  --> returns the keys of dict
my_dict_keys = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
print(my_dict_keys.keys())
# O/P :- dict_keys(['a', 'b', 'c', 'd'])

print('a' in my_dict_keys.keys()) # O/P :- Ture
print('e' in my_dict_keys.keys()) # O/P :- False

# Example 4 :- values() method --> return the values of dict
my_dict_value = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
print(my_dict_value.values())
# O/P :- dict_values([1, 2, 3, 4])

print(1 in my_dict_value.values()) # O/P :- Ture
print(9 in my_dict_value.values()) # O/P :- False

# Example 5 :- clear() method --> to clean the dict
my_dict_clean = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
my_dict_clean.clear()
print(my_dict_clean) # O/P :- {} it returns a empty dictionary


# Example 6 :- copy() method 
my_dict_copy = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
my_dict_copy_new = my_dict_copy.copy()
print(my_dict_copy_new) # O/P :-  {'a': 1, 'b': 2, 'c': 3, 'd': 4} , create a copy of old dict

# print(my_dict_copy_new + my_dict_copy)
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# It doesnt support concanating 2 dictionary 

# Example 6 :- pop() method --> remove the key:value pair from the dictionary and return the removed value
my_dict_pop = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
pop_val = my_dict_pop.pop('a')
print(pop_val) # O/P :- 1, retuned the removed value of the dictionary 

print(my_dict_pop) # O/P :- {'b': 2, 'c': 3, 'd': 4}, the also removed 

# Example 7 :- popitem() method --> remove any random key:value pair from the dictionary and return
# the removed key:value pair
my_dict_pop_item = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
pop_item_val = my_dict_pop_item.popitem()
print(pop_item_val) # O/P :- ('d', 4), it just ramdomly removed the key:value from the dictionary and 
# return the key:value pair
print(my_dict_pop_item) # O/P :- {'a': 1, 'b': 2, 'c': 3}

# Example 8 :- update() method --> update a key's value
my_dict_update = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
my_dict_update.update({'a': 55}) # this doesnt return any value, it just do the operation 
print(my_dict_update) # O/P :- {'a': 55, 'b': 2, 'c': 3, 'd': 4}

my_dict_update.update({'a': 51, 'b':34}) # updating mutiple key's value at a time
print(my_dict_update) # O/P :- {'a': 51, 'b': 34, 'c': 3, 'd': 4}

# Example 9 :- 
