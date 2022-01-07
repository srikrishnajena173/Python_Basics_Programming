######################################### classmethod ###############################################
# Example 1 :- 
class my_class:
    my_class_attribute = True # this is a class object attruibute and the scope is global/class level
    # and this is also called as static variable in java.

    @classmethod # this is a decorator in python , however in java we say annotation
    def my_sum(cls, num1 , num2): # this is a classmethod 
        # cls is same as self, however in classmethod we use cls, which pointing to the class and using cls we can point to the 
        # different members of the class. 
        return num1 + num2

# Here lets access the my_sum() method using class name
print(my_class.my_sum(2,3)) # O/P:- 5   
# Without creating an object and instantiating  we the constructor we are able to access the method called my_sum()
# directly using class name. However, the class loaded but we didnt created any object.


# Here lets access the my_sum() method using the object
obj = my_class()
print(obj.my_sum(1, 3)) # O/P :- 4
# NOTE :- So here the difference is you are again creating a new object and which consuming a extra memory.
# So, its always good to access the classmethod using class name.


# Example 2 :- Suppose you want to instantiate the constructor, then follow the below code
class my_class_new:
    
    def __init__(self, name, age):
        self.name = name  
        self.age = age

    @classmethod
    def add_number(cls, num1, num2):
        return cls('Sir', num1 + num2) # so here we are instantiate the constrcutor and loading the class

print(my_class_new.add_number(23, 12).name) # O/P :- Sir
print(my_class_new.add_number(23, 12).age) # O?P :- 35#
# But still we didnt create any object and we are able to access the method using class name 




############################################ staticmethod ##################################################

class static_class:

    def __init__(self):
        pass

    @staticmethod
    def add_number(num1, num2): ## this is same as the static method in java 
        return(num1 + num2)
    # here in the static method we dont have cls, which mean you cannot instantiate the constructor  
    # however you can access the method using class name or even we can access by object 

# Lets access the static method using class name 
print(static_class.add_number(11,11))  # O/P :- 22

# Lets access the static method using object 
stat_obj = static_class() 
print(stat_obj.add_number(11, 11)) # O/P :- 22
# NOTE :- So here the difference is you are again creating a new object and which consuming a extra memory.
# So, its always good to access the classmethod using class name.



