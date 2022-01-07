# We can iterate through each and every items in the python collections like :- 
# List, Sets , Dictionary and Tuple

# Example 1 :-  iterating through the List 
my_list = [1,2,3,4,5,6]
for li in my_list:
    print(li)

# Example 2 :- iterating through the tuple
my_tuple = (1,2,3,4,5,6)
for tup in my_tuple:
    print(tup)

# Example 3 :- iterating through the sets
my_sets = {1,2,3,4,4,5,6}
for se in my_sets:
    print(se) # Here it will remove the duplicate the print the unique values/object

# Example 4 :- iterating through the dictionary
my_dict = {
    'a':1,
    'b':2,
    'c':3
}
for d in my_dict.items(): # to get the key:value 
    print(d)

# O/P :- 
# ('a', 1)
# ('b', 2)
# ('c', 3) , so here its returning the key:value pair in a tuple format

# Unpacking the key value from the dictionary
for key, value in my_dict.items():
    print(key, value)

# O/P :- 
# a 1
# b 2
# c 3

for d in my_dict.values(): # to get the values
    print(d)

# O/P :- 
# 1
# 2
# 3

for d in my_dict.keys(): # to get the keys
    print(d)

# O/P :- 
# a
# b
# c    






