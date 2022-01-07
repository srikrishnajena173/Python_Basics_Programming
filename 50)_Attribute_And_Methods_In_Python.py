# Example 1:- 
class my_class:
    def __init__(self):
        pass

    def my_meth(self):
        pass

my_object = my_class()    

# print(help(my_object))    

# O/P :- so here it is returning the blue print of our object 
# class my_class(builtins.object)
#  |  Methods defined here:
#  |
#  |  __init__(self)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  my_meth(self)
#  |


# Same lets try for list#

#print(help(list))

# O/P :- so here its providing the blue print of the list object 
# class list(object)
#  |  list(iterable=(), /)
#  |
#  |  Built-in mutable sequence.
#  |
#  |  If no argument is given, the constructor creates a new empty list.
#  |  The argument must be an iterable if specified.
#  |
#  |  Methods defined here:
#  |
#  |  __add__(self, value, /)
#  |      Return self+value.
#  |
#  |  __contains__(self, key, /)
#  |      Return key in self.
#  |
#  |  __delitem__(self, key, /)
#  |      Delete self[key].


# Example 2 :- 
class my_class_new:
    my_class_attribute = True # this is a class object attruibute and the scope is global.
    
    def __init__(self, name , age): # NOTE :- self is same as this keyword in java
        if (self.my_class_attribute): # using self keyword only we can access class object attribute called my_class_attribute
            self.name = name ## here name is a dynamic attribute 
            self.age = 12 ## however here the age is constant attribute 

    def my_method(self):
        print(f'my name is {self.name}') # using the self keyword only we can access the name attribute
        return 'Done'

    # NOTE :- Self represents the instance of the class. 
    # By using the “self” keyword we can access the attributes and methods of the class in python

my_object_new = my_class_new('sri', 13)
print(my_object_new.name)  # O/P :- sir , here as name is dynamic attribute, so while creating the object we provide
# any value as an argument, the same value will reflect while printing.
 
print(my_object_new.age)   # O/P :- 12, however the age is constant attribute, so  while creating the object we provide any value
# as an argument, it will always print the constant value that you have provided at the time of creating the attribute.

print(my_object_new.my_class_attribute) # O/P :- True, this is a constant class object attruibute. 

print(my_object_new.my_method()) 
# O/P :- 
# my name is sri, so here we can access the name attribute and able to print the name using self keyword
# Done , as we are returning a Done string at the end of the method


# Example 3 :- 

class my_class_new_new:
    my_class_attribute = True # this is a class object attruibute and the scope is global.
    
    def __init__(self, name , age):
        if (my_class_new_new.my_class_attribute): # using class name called 'my_class_new_new' we can also able to access
            # class object attribute called my_class_attribute inside the constructor.
            self.name = name ## here name is a dynamic attribute 
            self.age = 12 ## however here the age is constant attribute 

    def my_method_new(self):
        #print(f'my name is {my_class_new_new.name}') # using class name we cannot access the constructor attribute called name.
        # As the scope of that attribute is belongs to constructor. 
        print(f'my name is {self.name}') # so you can only access the constructor attribute by self keyword
        print(my_class_new_new.my_class_attribute) # so here again you can access the class object attribute using the class name
        return 'Done'

my_obj_new_new = my_class_new_new('Sir', 34)
print(my_obj_new_new.name) # O/P :- Sri

print(my_obj_new_new.my_method_new())
# O/P :- AttributeError: type object 'my_class_new_new' has no attribute 'name' 
# So using the class name called 'my_class_new_new.name' we cannot access the constructor attribute called name. As the 
# scope of that attribute is belongs to constructor. 
# So to access the any constructor/method attribute we should always use the self keyword.

