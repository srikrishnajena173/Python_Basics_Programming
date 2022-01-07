# 1. Positional Parameter
def my_func(first_name, last_name): # first_name and last_name are the positional parameter
    print(f'hello {first_name} {last_name}')

# Invoke/call my_func
# my_func() you get the below error 
# TypeError: my_func() missing 2 required positional arguments: 'first_name' and 'last_name' 

my_func('sri' , 'jena')  # 'sri' and 'jena' are the positional argument
# O/P :- hello sri jena
# so this will take the argument as per the position 


# 2. Keyword argument 
my_func(last_name='jena', first_name='sri') # 'sri' and 'jena' are not in position
# O/P :- hello sri jena
# So, here it look for the parameter keyword 


# 3. Default parameter 
def my_default_func(first_name = 'sri', last_name = 'jena'):
    print(f'hello {first_name} {last_name}')

my_default_func()   # O/P :- hello sri jena
# so here if you dont provide any argument bydefault it will take the defualt argument 

my_default_func('krishna', 'j')  # O/P :- hello krishna j
# so here if you provided any argument then it will override the existing default argument 
# and print the new argument