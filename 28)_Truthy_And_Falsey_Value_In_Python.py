######################## Truthy and Falsey Value in Python #######################

# 1. Truthy Values in Python :- 
value_1 = 'Hello'
value_2 = 23

if value_1 and value_2:
    print('Its Ture')
else:
    print('Its False')   
     
# O/P :- Its True
# And you will always get the condition as true because internally the python converting those values
# to either True or False 
print(bool(value_1))
print(bool(value_2))
# O/P :- 
# True
# True , so you can see both are True

# 2. False Value in Python :- 
# All values are considered "truthy" except for the following, which are "falsy":

# None
# False
# 0
# 0.0
# 0j
# decimal.Decimal(0)
# fraction.Fraction(0, 1)
# [] - an empty list
# {} - an empty dict
# () - an empty tuple
# '' - an empty str
# b'' - an empty bytes
# set() - an empty set
# an empty range, like range(0)
# objects for which
# obj.__bool__() returns False
# obj.__len__() returns 0

# An Example 
value_1 = ''
value_2 = 0

if value_1 and value_2:
    print('Its Ture')
else:
    print('Its False')   

# O/P :- Its False, as all the value comes under the falsey value 