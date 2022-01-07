# Encapsulation :- Binding of data and function in a single unit called object and 
# then manipulate the data according to your requirement.
# NOTE :- data and function we called as attributes and methods 

# So here we create a class and bind all the data member/attributes and memember function/methods
# Typical example of Encapsulation is the below class 

class myClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_name_func(self):
        print(f'my name is {self.name}')    

    def my_age_func(self):
        print(f'my age is {self.age}')   

    def my_own_func(self, *args):
        return [args]   

obj = myClass('sir', 12)
print(obj.name) # O/P :- sir
print(obj.age)  # O/P :- 12   

print(obj.my_own_func(1,2,3,4)) # O/P :- [(1, 2, 3, 4)]