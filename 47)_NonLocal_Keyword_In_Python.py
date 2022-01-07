# Nonlocal keyword used to point to the parent local variable , and this feature is from the python 3
# its same as the super keyword in java

def parent_function():
    x = 'parent_variable'
    def child_function():
        nonlocal x         # --> here x will point to the parent_function variable x = 'parent_variable'
        x = 'local variable'  # --> so now the value will get updates/overridden, so now parent_function variable x = 'local variable'
        print('My local varibale value is : ' + x)  

    child_function()
    print('My parent local variable value is : ' + x) 


parent_function()
# O/P :- 
# My local varibale value is : local variable
# My parent local variable value is : local variable


# Suppose in the below code if we comment out the nonlocal keyword ??
def parent_function_1():
    x = 'parent_variable'
    def child_function_1():
        # nonlocal x          # commented the nonlocal keyword 
        x = 'local variable'  # --> so now the value will get updates/overridden, so now parent_function variable x = 'local variable'
        print('My local varibale value is : ' + x)  

    child_function_1()
    print('My parent local variable value is : ' + x) 

parent_function_1()
# O/P :- 
# My local varibale value is : local variable
# My parent local variable value is : parent_variable , so its pointing to the parent_function_1() variable 