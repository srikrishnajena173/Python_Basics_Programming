# OOPs (Object Oriented Programming) :- We use OOPs to structure our code or i can say keep the code in a structural format.
# Advantage of OOPs is, its easy to maintain the code, easy to extend the code, more readable and reusable code or dynamic code
# or more robust code

# There is 4 pillars of Object Oriented Programming (OOPs)
# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism

# NOTE :- Everything in python is object, lets see what is that mean

# When we say everything is object that mean everything is created from a class, like the below exmaples :-
# So by using class you can break you code into small features, so every feature has there own object.

print(type(True))
print(type(1))
print(type(1.1))
print(type('a'))
print(type(()))
print(type([]))
print(type({}))
print(type(None))

# O/P :- 
# <class 'bool'> 
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'tuple'>
# <class 'list'>
# <class 'dict'>
# <class 'NoneType'>

# For each class they have there own method like for list class .append(), .count(), .index()
# For dict class we have .items(), .keys(), .values()



################################################################################################################

# In python i can create my own datatype using class , lets see how

class myClass: ### this is our class
    pass


print(type(myClass)) # O/P :- <class 'type'>, that mean we just created a class and class is a user defined datatype. But
# till now we havn't created the object.

myClass() # here in this step we are created the object i.e. myClass() and that object is pointing to myClass.

print(type(myClass())) # O/P :- <class '__main__.myClass'>, this is the type of my object. 

print(myClass()) # O/P :- <__main__.myClass object at 0x000001BA62705FD0> , so here it return the reference address or the 
# memory location of the object that is pointing to the class called myClass.

obj1 = myClass() ## here we are storing the object in a reference variable called obj1 and my reference variable obj1 is pointing to myClass
obj2 = myClass() ## same here as well, we are storing the object in a referance variable called obj2 and my reference variable obj2 is pointing to myClass

print(obj1) # O/P :- <__main__.myClass object at 0x000001FE493C6BB0>, this is printing a reference address or memory location
print(obj2) # O/P :- <__main__.myClass object at 0x000001FE493C6B80>, this is printing a reference address or memory location

# So, in the above code we have multiple objects and all the objects have different reference address 
# or a unique reference address/memeory location. So everytime you create a new object 
# we will get a unique reference address/memeory location that will be pointing to the class for which we are creating the object.

# To instantiate a class we have create a new instance/object.
myClass() # So in this step we have instantiated a class, which mean we are loading our class.
print(myClass()) # O/P :- <__main__.myClass object at 0x0000020852E56B80>, again we got a unique memory location.

# So everytime you are creating a new list [], that mean we instantiate the list class and and we are 
# able to use the list class methods.