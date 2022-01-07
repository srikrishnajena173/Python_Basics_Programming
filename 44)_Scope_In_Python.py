# Steps that python interperter follows with the scopes in python 
# 1. First look of the local scope, if you dont have any local scope
# 2. Then look for parent local scope, if you dont have any parent local scope
# 3. Then look for the global scope, if you dont have any gobal scope 
# 4. Then at the end look for the built-in python functions

# Lets explore one by one

# Example 1 :- you have a local scope variable. 
a = 'gobal scope'                 # --> global scope

def parent_func():
    a = 'parent local scope'      # --> parent local scope
    def child_func():
        a = 'local scope'         # --> local scope
        return a
    return child_func()    

# sum() , len() ..etc those are the built-in python function
print(parent_func())  # O/P :- local scope
print(a)              # O/P :- global scope
 


# Example 2. if you dont have local scope variable, then how python interperter will look for the parent local scope 
a1 = 'gobal scope'                  # --> global scope

def parent_func_1():
    a1 = 'parent local scope'       # --> parent local scope
    def child_func_1():
        # a1 = 'local scope'        # --> local scope commented 
        return a1
    return child_func_1()   

print(parent_func_1())   # O/P :- parent local scope
print(a1)                # O/P :- gobal scope


# Example 3. if you dont have local scope variable as well as parent local scope variable, 
# then how python interperter will look for the global local scope 
a2 = 'gobal scope'                  # --> global scope

def parent_func_2():
    # a2 = 'parent local scope'     # --> parent local scope commented
    def child_func_2():
        # a2 = 'local scope'        # --> local scope commented 
        return a2
    return child_func_2()   

print(parent_func_2())   # O/P :- gobal scope
print(a2)                # O/P :- gobal scope

# Example 4. if you dont have local scope variable, parent local scope variable and global local scope variable
# then how python interperter will look for built-in python function 
# a3 = 'gobal scope'                # --> global scope commnted

def parent_func_3():
    # a2 = 'parent local scope'     # --> parent local scope commented
    def child_func_3():
        # a2 = 'local scope'        # --> local scope commented 
        return sum                  # --> added a new python built-in function
    return child_func_3()   

print(parent_func_3())   # O/P :- <built-in function sum>