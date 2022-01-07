# Lets explore the some more on __inti__(self) or constructor method in python :- 

# NOTE :- So always remember, the constructor will automatically get invoked when we instantiate the object. 
# And when the constructor get invoked the class will automatoically load.

## You instantiate 
class my_class:

    def __init__(self, name='xyz', age=0):
        if(age > 18):
            self.name = name
            self.age = age

    def my_func(self):
        print(f'my name is {self.name} and age is {self.age}')        

obj = my_class() 

print(obj.my_func()) # O/P :- AttributeError: 'my_class' object has no attribute 'name'
# So the condition is, if age > 18 then only the below code will run and instantiate the attribute, which mean the
# python interpreter allocate a memeory for name and age attribute or memeber.

# So here we instantiate the constructor, however we didnt instantiate the attribute or the memeber of the constructor. Which mean
# the python interpreter didnt allocate the memory for the constructor attribute.




