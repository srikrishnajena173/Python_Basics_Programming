# *args :- with this parameter you can provide n munber of arguments 

# Example 1 :- 
def my_func(*args):
    print(args) # so, here the *args return a tuple i.e. (1,2,3,4)
    return sum(args)

# Invoke the function 
print(my_func(1,2,3,4)) # here you can provide any numbers of arguments 

# O/P :- 
# (1, 2, 3, 4)
# 10

# **kwargs :- with this parameter you can provide n munber of keyword arguments 

# Example 1 :- 
def my_keyfunc(**kwargs):
    print(kwargs) # so here the **kwargs retun a dictionary i.e. {'num1': 3, 'num2': 5}
    # so to perform the sum we have to do below steps 
    total_sum = 0
    for items in kwargs.values():
        total_sum += items
    return total_sum    


print(my_keyfunc(num1 = 3, num2 = 5))
# O/P :- 
# {'num1': 3, 'num2': 5}
# 8

# Example 2: - In this example we are passing both *args and **kwargs as parameter
def super_function(*args, **kwargs):
    print(args)    # so, here the *args return a tuple i.e. (1,2,3,4)
    print(kwargs)  # so here the **kwargs retun a dictionary i.e. {'num1': 3, 'num2': 5}
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_function(1,2,3,4, num1 = 1 , num2 = 4))   
# O/P :- 15

# NOTE :- Rule for passing the parameter are 
# 1. params
# 2. *args
# 3. default params
# 4. **kwargs

# Example 3 :- 

def super_function_rule(name, *args, i=10, **kwargs):
    print(name)
    print(args)
    print(i)
    print(kwargs)

# Invoke the the function 
super_function_rule('Sri', 1,2,3,4, i=10, num1 = 33)    

# O/P :- 
# Sri
# (1, 2, 3, 4)
# 10
# {'num1': 33}


