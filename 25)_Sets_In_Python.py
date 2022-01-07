# Sets is an unordered collection of unique objects 

# Example 1.
my_sets = {'e', 'a', 'b', 'c', 'd', 'e'}
print(my_sets)
# O/P :- {'c', 'a', 'd', 'e', 'b'} , sets remove the duplicate items and retun the value in an unordered format


# Example 2 :- 
# Suppose we have a list and that list contains duplicate items, so how you will remove the duplicate items 
my_list_duplicate = [1,2,3,4,3,2,1]
my_set_val = set(my_list_duplicate)
print(my_set_val) # O/P :- {1, 2, 3, 4}

# Example 3 :- 
my_sets_1 = {'e', 'a', 'b', 'c', 'd', 'e'}
# Now can you access the set value by index ??
# print(my_set_val[0]) # TypeError: 'set' object is not subscriptable
# So, you cannot access the sets by index's, only you can access by value/item name.

# Example 4 :- 
my_set_2 = {'e', 'a', 'b', 'c', 'd', 'e'}
print('e' in my_set_2) # O/P :- True

# Example 5 :- len() in-built method of python to count the length/size of the list
my_set_3 = {'e', 'a', 'b', 'c', 'd', 'e', 'e', 'd'}
set_len = len(my_set_3)
print(set_len) # O/P :- 5 , as its remove the duplicate value and return the rest of the value length 

# Example 6 :- Even you convert a set to list 
my_set_4 = {'e', 'a', 'b', 'c', 'd', 'e', 'e', 'd'}
my_list_4 = list(my_set_4)
print(my_list_4) # O/P :- ['a', 'b', 'e', 'd', 'c'], remove the duplicates and return a list 