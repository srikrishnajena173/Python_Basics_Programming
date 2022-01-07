
# Here in this doc we will exploring the python Built-in Functions and methods

# abs()                     # delattr()               # hash()
# memoryview()              # set()                   # all()

# These are some of the built-in fuctions of python. The remaning functions you can explore in the 
# below links 
# https://docs.python.org/3/library/functions.html

# Lets explore some of the functions
# Example 1 :-
print(len('Johnny'))
# O/P :- 6 , so it is returning the length of the string character

print(type(len('Johnny')))
# O/P :- <class 'int'> , and the type is always integer 

# Example 2 :- 
my_string_val = '0123456789'
print(my_string_val[0:len(my_string_val)])
# O/P :- 0123456789 , so here the start point is 0th index and end point is len(my_string_val), 
# which is 9

# Important NOTE :- Now whats the difference between the functions and methods in python ?? its simple,

# Functions are like abs() , len() or print(), however methods are alway in .method_name()

# Python strings contains some methods like .format(), .capitalize(), .index()
# Example 1 :- 
my_string = 'srijena'
out_put = my_string.capitalize() # this is a method of string
print(out_put)
# O/P :- Srijena , so here it is capitalized the first character of the string

# Example 2 :- 
out_put1 = my_string.upper()
print(out_put1)
# O/P :-  SRIJENA

# In the below link you can findout more strings methods
# https://www.w3schools.com/python/python_ref_string.asp



