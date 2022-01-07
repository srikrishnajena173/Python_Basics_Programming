# Here lets create our own object 

# Example 1 :- 
class myClass:
    def __init__(self): # this is a default constructor of class myClass
        pass

    def my_func(self): # user defined method 
        print('my_func')

# NOTE :- Self represents the instance of the class. 
# By using the “self” keyword we can access the attributes and methods of the class in python.

## so lets create an object
my_obj = myClass() # here we have created the object for our class myClass
print(my_obj) # O/P :- <__main__.myClass object at 0x0000026F6DA26850>

# How internally the object is instantiating the class ?
# when we invoke or call the object (myclass()) or the object reference (my_obj) in line number 16, the object will point to the 
# def __init__(self) and then the class will load.

# So  def __init__(self) is a defult constructor with a default parameter called self
# So if we dont define the constructor def __init__(self) explicitly, even though by default the object will point to the default
# constructor and will load/instantiate the class.
class class_abc:
    
    def my_abc_func():
        pass

obj_abc = class_abc() ## so here it is by defualt pointing to the defualt constructor called __init__(self) 
print(obj_abc.my_abc_func)


# Example 2 :- 
class myClass_new:
    def __init__(self, my_name): ## so here this is an parameterized constructor with a parameter called my_name
        self.my_name = my_name ## here self is pointing to the parameter my_name

    def my_new_func():
         print('print my new func')   

# myClass_new()
# So here we get this error :- TypeError: __init__() missing 1 required positional argument: 'my_name'
# As the constructor is looking for a parameter


obj1 = myClass_new('sir') # provided a string parameter 
obj2 = myClass_new('jena') 


print(obj1) # O/P :- <__main__.myClass_new object at 0x00000206DFE45D90>
print(obj2) # O/P :- <__main__.myClass_new object at 0x00000206DFD8F760>

# But if you want to print the name value then the object should point to the attribute called my_name
print(obj1.my_name) # O/P :- sir
print(obj2.my_name) # O/P :- jena
## so here i am able to create dynamic code, just the change the parameter and you have your output accordingly 

# OR 

print(myClass_new('krishna').my_name) # O/P :- krishna


# Example 3 :- 
class myClass_new_new:
    def __init__(self, my_name, age): ## so here this is an parameterized constructor with a parameter called my_name
        self.my_name = my_name ## here self is pointing to the parameter my_name
        self.age = age

    def my_new_new_func(self):
         print('print my new func')   


obj_new = myClass_new_new('Sri', 23)

print(obj_new.my_name) ## so here my object obj_new is pointing to an attribute called my_name.
# O/P :- Sri

print(obj_new.age) ## same here as well, my object obj_new is pointing to an attribute called age.
# O/P :- 23

print(obj_new.my_new_new_func()) ## here my object obj_new is pointing to a method called my_new_new_func().
# O/P :- 
# print my new func , so here it invoke the method called my_new_new_func() and print the print statment 
# None , here we have None as the  my_new_new_func() does not have any return type.

