# Formatted string means, use the string variable or values in dynamic manner 

# For Example 1 :- 
from typing import AsyncGenerator


name = 'Sri jena'
age = 29
address  = '2nd Street'
# So, above this values are suppose coming from a database 

print('Hi ' + name + '.' + ' You are ' + str(age) + ' and stay at ' + address)
# O/P :- Hi Sri jena. You are 29 and stay at 2nd Street

# OR the second way of doing it 

print(f'Hi {name}. You are {age} and stay at {address}') # this is python 3 syntax
# NOTE :-  f stands for formatted string
# O/P :- Hi Sri jena. You are 29 and stay at 2nd Street

# OR 

# the below is the Python 2 syntax 
print('Hi {}. You are {} and stay at {}'.format(name, age, address))
# O/P :- Hi Sri jena. You are 29 and stay at 2nd Street

# OR 

# Again this is also python 2 syntax
print('Hi {new_name}. You are {new_age} and stay at {new_address}'.
format(new_name = 'Sri', new_age = 34, new_address = '23 Street'))
# O/P :- Hi Sri. You are 34 and stay at 23 Street