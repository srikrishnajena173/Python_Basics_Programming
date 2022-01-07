# Enumerate returns an object and iterator must an object which can iterable 

# Example 1 :- 
# my_string = 'Hellooo'
# for index, i in my_string:
#     print(index, i) # ValueError: not enough values to unpack (expected 2, got 1)

# The above error can be resolved by enumerator
my_string = 'Hellooo'
for index_val, char in enumerate(my_string):
    print(index_val, char)

# O/P :- 
# 0 H
# 1 e
# 2 l
# 3 l
# 4 o
# 5 o
# 6 o

# Example 2 :- 
for index_val, my_list_val in enumerate([1,2,3]):
    print(index_val, my_list_val)

# O/P :- 
# 0 1
# 1 2
# 2 3

# Example 3 :- find out the index value of list value 50
for index_val, list_val in enumerate(list(range(100))):
    if list_val == 50:
        print(f'index value is : {index_val}') # O/P :- index value is : 50
