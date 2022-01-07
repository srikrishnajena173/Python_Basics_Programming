# In this doc we will explore how the strings are allocated in a indexing manner.

# Suppose lets take the below Example 1:- 
my_string_val = '0123456789'
               # 0123456789 , so here is character have a index.

print(my_string_val[3])
# O/P:- 2 # so here it is returning the 3rd index character of the string

# When you use square [] bracket that means 2 things
# [start:stop:stepover], it says from which index you want me to start and on which index you
# want me to stop. And stepover is how you want me to extract the value.

# Example 2 :- 
print(my_string_val[1:4])
# O/P :- 2 3 , so here it consider the index 1, 2 and 3. Where as the 4th index is not included

# Example 3 :- 
print(my_string_val[1:5:1])
# O/P  :- 1234 , so here it is saying step 1 by 1

# Example 4 :- 
print(my_string_val[1:9:2])
# O/P  :- 1357 , so here it is saying step 2 by 2

# Example 5 :- 
print(my_string_val[1:])
# O/P  :- 123456789, so here it will start from index 1 and stop at the end index, 
# as we didnt provided any stop index, so by defualt it will consider the end index.

# Example 6 :- 
print(my_string_val[:5])
# O/P  :- 01234, so here it will start from index 0 and stop at the index 4, 
# as we didnt provided any start index, so by defualt it will consider the first index.


# Example 7 :- 
print(my_string_val[-1])
# O/P  :- 9, so here it will consider the last index of the string 
# So in python -ve (-) means start from the last index

# NOTE :- Example 8 :- Reverse string in python
print(my_string_val[::-1])
# O/P :- 9876543210, the default start index will be 1st index and default stop index 
# will be the last index and as the stepover is -1, so it will consider the values from reverse format.

# OR 

print(my_string_val[::-2])
# O/P :- 97531, skipping by 2
