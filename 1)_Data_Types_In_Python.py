# Fundamental Data type in python 
int 
float
bool
str
list 
tuple
set
dict

# Classes are the custome type (created by users/us)

# Specialized data type :- which we get it from 3rd party libraries  

None # NOTE :- this is keyword in python which means null or zero

# Lets start with the fundamental data type :

# int type - which stores numbers 
print(type(2 + 3))
# O/P :- <class 'int'>

# float type - which stores decimal values 
print(type(1 + 3.2))
# O/P :- <class 'float'>

print(type(1.1 + 3.2))
# O/P :- <class 'float'>

print(type(1 / 1)) 
# O/P :- <class 'float'>
# NOTE :- Remember that division mathematical operation always return float type data, 
# even both the inputs are number or decimal

print(5 // 4) 
# O/P :- 1 , that means the // mean always round up the output value
print(type(5 // 4))
# O/P :- <class 'int'> , and the type is always integer 

print(2 ** 2) # 2 the power of 2
# O/P :- 4

print(9 % 4) # This is a % modular which returns the remainder 
# O/P :- 1