# Suppose you want to provide a information about your user defined function, you can do that.
# So when the other person access your function it will auto suggest the function with the info.

# Example 1 :-
def my_function(a):
    '''
    Info : Here provide the infomrmation
    about your function. Providing a function description
    inside the method

    '''
    print(a)

# So now invoke your function 
my_function('Sri')

# OR

# there is one one way to see the function infomation, for both python
# in-built function as well as user defined function

help(my_function) # user defined function
# # O/P :-
#     my_function(a)
#     Info : Here provide the infomrmation
#     about your function. Providing a function description
#     inside the method

help(len) ## python in-built function
## O/P :- 
# len(obj, /)
#     Return the number of items in a container.

# NOTE :- help is a python in-built function use to get the function infomration, 
# number of parameter, position of the paramters.

# OR

# there is another way of getting the function info is by using 
# Dunder method or Magic method in python.

print(my_function.__doc__)
# O/P :- 
#     Info : Here provide the infomrmation
#     about your function. Providing a function description
#     inside the method

# In python we have lots of dunder method for intl, string, list ..etc.